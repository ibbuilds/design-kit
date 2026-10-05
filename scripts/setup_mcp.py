#!/usr/bin/env python3
"""Plan selected reference MCPs; --apply writes the selected project or user config."""
import argparse
import copy
import json
import os
from pathlib import Path
import sys
import uuid
from urllib.parse import urlsplit, urlunsplit

try:
    import tomllib
except ImportError:  # JSON hosts work on Python 3.9; Codex needs Python 3.11+.
    tomllib = None

from install import atomic_write, guarded_path, installation_root

HOSTS = {
    "codex": (".codex/config.toml", "mcp_servers", "url"),
    "claude-code": (".mcp.json", "mcpServers", "url"),
    "gemini-cli": (".gemini/settings.json", "mcpServers", "httpUrl"),
    "antigravity": (".agents/mcp_config.json", "mcpServers", "serverUrl"),
}
USER_CONFIGS = {
    "codex": ".codex/config.toml",
    "claude-code": ".claude.json",
    "gemini-cli": ".gemini/settings.json",
    "antigravity": ".gemini/config/mcp_config.json",
}
PROVIDERS = ("awwwards", "onepagelove")
OPL_URL = "https://api.onepagelove.com/mcp"


def provider_spec(host, provider, windows=None):
    if host not in HOSTS or provider not in PROVIDERS:
        raise ValueError("Unsupported host or provider")
    if windows is None:
        windows = os.name == "nt"
    if provider == "awwwards":
        spec = {"command": "cmd.exe" if windows else "npx",
                "args": ["/d", "/c", "npx.cmd", "-y", "awwwards-mcp"] if windows
                else ["-y", "awwwards-mcp"]}
        if host == "claude-code":
            spec["type"] = "stdio"
        return spec
    spec = {HOSTS[host][2]: OPL_URL}
    if host == "claude-code":
        spec["type"] = "http"
    return spec


def normalized_url(value):
    if not isinstance(value, str):
        return None
    parsed = urlsplit(value)
    return urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(),
                      parsed.path.rstrip("/"), parsed.query, parsed.fragment))


def is_provider(spec, host, provider):
    if not isinstance(spec, dict):
        return False
    if provider == "onepagelove":
        if host == "claude-code" and spec.get("type") not in ("http", "streamable-http"):
            return False
        return normalized_url(spec.get(HOSTS[host][2])) == normalized_url(OPL_URL)
    command = spec.get("command")
    args = spec.get("args")
    if not isinstance(command, str) or not isinstance(args, list):
        return False
    executable = command.replace("\\", "/").rsplit("/", 1)[-1].lower()
    if executable in ("cmd", "cmd.exe"):
        # Recognize the documented Windows wrapper without parsing shell strings.
        flags = args[:2] if args[:1] == ["/d"] else args[:1]
        count = len(flags)
        if flags not in (["/c"], ["/d", "/c"]) or len(args) <= count:
            return False
        command = args[count]
        if not isinstance(command, str):
            return False
        executable = command.replace("\\", "/").rsplit("/", 1)[-1].lower()
        args = args[count + 1:]
    return executable in ("npx", "npx.cmd", "npx.exe") and any(
        isinstance(arg, str) and (arg == "awwwards-mcp" or arg.startswith("awwwards-mcp@"))
        for arg in args)


def is_disabled(spec):
    return spec.get("enabled") is False or spec.get("disabled") is True


def json_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON key; review config before changing it: " + key)
        result[key] = value
    return result


def load_config(raw, host):
    if host == "codex":
        if tomllib is None:
            raise ValueError("Codex config validation needs Python 3.11+; use the host's native MCP settings instead")
        return tomllib.loads(raw.decode("utf-8"))
    if not raw.strip():
        return {}
    try:
        data = json.loads(raw.decode("utf-8"), object_pairs_hook=json_object)
    except json.JSONDecodeError as error:
        raise ValueError("Invalid JSON or JSONC; use native settings to preserve comments: " + str(error)) from error
    if not isinstance(data, dict):
        raise ValueError("MCP config must be an object")
    return data


def plan(target=None, host="codex", providers=PROVIDERS, windows=None, scope="project", user_home=None):
    target = installation_root(target, scope, user_home)
    if target == Path(__file__).resolve().parents[1]:
        raise ValueError("Select the application project, not the shared kit or installed skill directory")
    if host not in HOSTS:
        raise ValueError("Unsupported host: " + host)
    chosen = tuple(dict.fromkeys(providers))
    if not chosen or any(p not in PROVIDERS for p in chosen):
        raise ValueError("Select only supported providers")
    filename, key, _ = HOSTS[host]
    if scope == "user":
        filename = USER_CONFIGS[host]
    path = guarded_path(target, filename)
    original = path.read_bytes() if path.exists() else None
    raw = original if original is not None else b""
    data = load_config(raw, host)
    servers = data.get(key, {})
    if not isinstance(servers, dict) or any(not isinstance(v, dict) for v in servers.values()):
        raise ValueError("Invalid MCP server map; review existing config")
    if host == "claude-code" and any(
            isinstance(spec.get("url"), str) and spec.get("type") not in ("http", "streamable-http", "sse", "ws")
            for spec in servers.values()):
        raise ValueError("Claude remote server needs an explicit transport type; review existing config")
    servers = copy.deepcopy(servers)
    additions, existing = {}, []
    for provider in chosen:
        # A conflicting reserved name must never be silently bypassed via alias.
        if provider in servers and not is_provider(servers[provider], host, provider):
            raise ValueError("Conflicting MCP name; refusing overwrite: " + provider)
        matches = [(name, spec) for name, spec in servers.items() if is_provider(spec, host, provider)]
        if any(is_disabled(spec) for _, spec in matches):
            raise ValueError("Provider is explicitly disabled; review in the host: " + provider)
        if matches:
            existing.append(provider)
            continue
        additions[provider] = provider_spec(host, provider, windows)
    if not additions:
        return {"path": path, "original": original, "payload": raw,
                "added": [], "existing": existing}
    if host == "codex":
        # Append validated tables, preserving unrelated values and comments byte-for-byte.
        parts = [raw.decode("utf-8").rstrip("\n"), ""]
        for name, spec in additions.items():
            parts.append("[mcp_servers." + name + "]")
            parts.extend(k + " = " + json.dumps(v) for k, v in spec.items())
            parts.append("")
        payload = ("\n".join(parts) + "\n").encode("utf-8")
        load_config(payload, host)  # Inline/frozen tables and conflicts must fail before writes.
    else:
        data[key] = {**servers, **additions}
        payload = (json.dumps(data, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    return {"path": path, "original": original, "payload": payload,
            "added": list(additions), "existing": existing}


def configure(target=None, host="codex", providers=PROVIDERS, apply=False, windows=None, scope="project", user_home=None):
    result = plan(target, host, providers, windows, scope, user_home)
    result["backup"] = None
    if not apply or not result["added"]:
        return result
    path = result["path"]
    original = result["original"]
    # Recheck the write path and bytes before applying a previously computed plan.
    root = installation_root(target, scope, user_home)
    guarded_path(root, path.relative_to(root))
    current = path.read_bytes() if path.exists() else None
    if current != original:
        raise ValueError("Config changed during setup; rerun the plan")
    if original is not None:
        backup = path.with_name(path.name + ".design-kit-backup-" + uuid.uuid4().hex)
        guarded_path(root, backup.relative_to(root))
        # Preserve originals for manual recovery, without replacing an existing backup.
        with backup.open("xb") as stream:
            stream.write(original)
        if os.name == "posix":
            os.chmod(backup, path.stat().st_mode & 0o777)
        result["backup"] = backup
    atomic_write(path, result["payload"])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, nargs="?", help="Existing project directory (project scope only)")
    parser.add_argument("--scope", choices=("project", "user"), default="project")
    parser.add_argument("--user-home", type=Path, help="Explicit existing user/profile home (user scope only)")
    parser.add_argument("--host", choices=HOSTS, default="codex")
    parser.add_argument("--provider", choices=PROVIDERS, action="append")
    parser.add_argument("--apply", action="store_true", help="Apply the reviewed config; creates a backup if it exists")
    args = parser.parse_args()
    try:
        result = configure(args.target, args.host, args.provider or PROVIDERS, args.apply, scope=args.scope, user_home=args.user_home)
    except (ValueError, OSError) as error:
        print("ERROR: " + str(error), file=sys.stderr)
        return 2
    print(("APPLY: " if args.apply else "PLAN ONLY: ") + str(result["path"]))
    print("Scope: " + args.scope + "; host: " + args.host)
    print("Add: " + (", ".join(result["added"]) or "none"))
    print("Already configured locally: " + (", ".join(result["existing"]) or "none"))
    if result["backup"] is not None:
        print("Backup: " + str(result["backup"]))
    print("No package downloads, model calls or server launches performed.")
    print("Other config scopes and native connections were not inspected. Reload if needed, then verify actual tools and a readable result.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
