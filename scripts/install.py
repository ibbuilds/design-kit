#!/usr/bin/env python3
"""Install this skill locally without network access or application changes."""
import argparse
import hashlib
import json
import os
import stat
from pathlib import Path
import sys
import tempfile

PACKAGE = (
    "SKILL.md", "IMAGE_WORKFLOW.md", "FOUNDATION.md", "agents/openai.yaml", "README.md", "BRIEF.md", "TASTE.md",
    "GUIDELINES.md", "CRAFT.md", "QA.md", "REFERENCES.md", "WORKFLOW.md", "RESEARCH.md",
    "docs/EXECUTION_DECISION.md", "scripts/install.py", "tests/test_install.py",
    "REFERENCE_ROUTER.md", "EXECUTION.md", "SOFTWARE.md",
    "DESIGN_DIRECTION.md", "docs/QUALITY_EVIDENCE.md",
    "PRODUCT_DELIVERY.md", "docs/WORKFLOW_RESEARCH.md",
    "scripts/reference_scope.py", "tests/test_reference_scope.py", "ONBOARDING.md", "PENPOT.md",
    "PROVIDERS.md", "HOSTS.md", "PROMPT.md", "scripts/setup_mcp.py", "tests/test_setup_mcp.py",
    "docs/GENERAL_GUIDE.txt", "docs/01_design_from_scratch.txt",
    "docs/02_improve_existing_design.txt", "docs/03_frontend_engineering.txt",
    "scripts/check_mcp.py", "tests/test_check_mcp.py", "docs/WORKFLOW_EVALUATION.md",
    "scripts/onepagelove_compat.py", "tests/test_onepagelove_compat.py",
)
HOSTS = {
    "codex": (".agents/skills/design-kit", "AGENTS.md"),
    "claude-code": (".claude/skills/design-kit", "CLAUDE.md"),
    "gemini-cli": (".agents/skills/design-kit", "GEMINI.md"),
    "antigravity": (".agents/skills/design-kit", "GEMINI.md"),
}
USER_HOSTS = {
    "codex": ".agents/skills/design-kit",
    "claude-code": ".claude/skills/design-kit",
    "gemini-cli": ".agents/skills/design-kit",
    "antigravity": ".gemini/config/skills/design-kit",
}
MANIFEST = ".design-kit-manifest.json"
START = "<!-- design-kit:begin -->"
END = "<!-- design-kit:end -->"
POINTER = (
    START + "\nFor image-first visual exploration, section images, references and review, read and apply\n"
    "`.agents/skills/design-kit/SKILL.md`. Preserve this project's own\n"
    "instructions and use its existing brief and accepted implementation.\n" + END + "\n"
)
SOFTWARE_RULE = (
    "For separately user-requested frontend code and QA, read and apply `.agents/skills/design-kit/SOFTWARE.md`.\n"
    "Preserve accepted design and existing API contracts; backend implementation\n"
    "is outside Design Kit's scope.\n"
)
LEGACY = (
    "For frontend design, implementation or review, read `.design-kit/AGENTS.md`\n"
    "as supplemental guidance and follow its selective reading routes.\n"
    "Preserve this project's instructions, stack and conventions.\n"
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def guarded_path(root, relative):
    """Refuse symlinked write paths and non-directory parents."""
    path = root / relative
    if not path.is_relative_to(root):
        raise ValueError("Path outside target: " + str(path))
    current = root
    for part in Path(relative).parts:
        if part in ("..", ""):
            raise ValueError("Unsafe relative path")
        current = current / part
        if current.is_symlink():
            raise ValueError("Refusing symlink: " + str(current))
        if current != path and current.exists() and not current.is_dir():
            raise ValueError("Parent is not a directory: " + str(current))
    if path.exists() and not path.is_file():
        raise ValueError("Expected a file: " + str(path))
    return path


def pointer_text(text, with_software=None, bundle=".agents/skills/design-kit"):
    """Replace only our block or the exact documented legacy pointer."""
    if text.count(START) != text.count(END) or text.count(START) > 1:
        raise ValueError("Malformed or duplicate Design Kit markers in instruction file")
    if START in text:
        start, end = text.index(START), text.index(END)
        if end < start:
            raise ValueError("Reversed Design Kit markers in instruction file")
        end += len(END)
        # Older manifests derive the choice only from our marked block,
        # never from arbitrary project prose.
        if with_software is None:
            with_software = "design-kit/SOFTWARE.md" in text[start:end]
        if text[end:end + 2] == "\r\n":
            end += 2
        elif text[end:end + 1] == "\n":
            end += 1
        pointer = POINTER.replace(END, SOFTWARE_RULE + END) if with_software else POINTER
        pointer = pointer.replace(".agents/skills/design-kit", bundle)
        return text[:start] + pointer + text[end:]
    text = text.replace(LEGACY, "").replace(LEGACY.replace("\n", "\r\n"), "")
    separator = "" if not text or text.endswith("\n") else "\n"
    pointer = POINTER.replace(END, SOFTWARE_RULE + END) if with_software else POINTER
    pointer = pointer.replace(".agents/skills/design-kit", bundle)
    return text + separator + pointer


def instruction_path(target, host="codex"):
    """Write into the active root instruction file, not one Codex will skip."""
    filename = HOSTS[host][1]
    if host != "codex":
        return guarded_path(target, filename)
    override = guarded_path(target, "AGENTS.override.md")
    if override.exists() and override.read_bytes().strip():
        return override
    return guarded_path(target, "AGENTS.md")


def installation_root(target, scope="project", user_home=None):
    """Keep user installation separate from project paths and instructions."""
    if scope not in ("project", "user"):
        raise ValueError("Unsupported installation scope")
    if scope == "user":
        if target is not None:
            raise ValueError("User scope takes no project target; use --user-home for a different profile")
        root = Path(user_home) if user_home is not None else Path.home()
    else:
        if user_home is not None:
            raise ValueError("--user-home requires user scope")
        if target is None:
            raise ValueError("Project scope requires an existing project target")
        root = Path(target)
    root = root.resolve()
    if not root.is_dir():
        raise ValueError("Target must be an existing project directory or user home")
    return root


def installation_plan(source, target=None, with_software=None, host="codex", scope="project", user_home=None):
    source = Path(source).resolve()
    target = installation_root(target, scope, user_home)
    if not target.is_dir():
        raise ValueError("Target must be an existing project directory")
    if target == source:
        raise ValueError("Select the application project, not the kit checkout")
    if host not in HOSTS:
        raise ValueError("Unsupported host: " + host)
    if scope == "user" and with_software is not None:
        raise ValueError("Software pointer options apply only to project instructions; the global skill already covers requested frontend code")
    bundle = Path(USER_HOSTS[host] if scope == "user" else HOSTS[host][0])
    manifest_path = guarded_path(target, bundle / MANIFEST)
    destination = target / bundle
    previous = {}
    previous_software = None
    if manifest_path.exists():
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("format") != 1 or data.get("name") != "design-kit":
            raise ValueError("Unrecognized installation manifest")
        previous = data.get("files")
        if not isinstance(previous, dict) or not set(previous).issubset(PACKAGE):
            raise ValueError("Invalid managed-file list")
        if not all(isinstance(v, str) and len(v) == 64 for v in previous.values()):
            raise ValueError("Invalid managed-file hashes")
        previous_software = data.get("software")
        if previous_software is not None and not isinstance(previous_software, bool):
            raise ValueError("Invalid software routing state")
    elif destination.exists() and any(destination.iterdir()):
        raise ValueError("Existing skill is not managed by this installer; review it first")

    planned, hashes = [], {}
    for relative in PACKAGE:
        incoming = guarded_path(source, relative)
        if not incoming.is_file():
            raise ValueError("Missing or symlinked package file: " + relative)
        payload = incoming.read_bytes()
        hashes[relative] = digest(payload)
        output = guarded_path(target, bundle / relative)
        if output.exists():
            current = output.read_bytes()
            if current == payload:
                continue
            if digest(current) != previous.get(relative):
                raise ValueError("Locally edited/unmanaged file; refusing overwrite: " + str(output))
        planned.append((output, payload))

    agents = instruction_path(target, host) if scope == "project" else None
    old = agents.read_bytes() if agents is not None and agents.exists() else b""
    text = old.decode("utf-8")
    # The saved choice survives a new override or a return to a stale fallback
    # block. Older manifests derive their initial choice from the active block.
    routing = previous_software if with_software is None else with_software
    new = pointer_text(text, routing, bundle.as_posix()).encode("utf-8") if agents is not None else b""
    software_rule = SOFTWARE_RULE.replace(".agents/skills/design-kit", bundle.as_posix()).encode("utf-8")
    data = {"format": 1, "name": "design-kit", "files": hashes,
            "software": software_rule in new if agents is not None else bool(routing)}
    payload = (json.dumps(data, indent=2, sort_keys=True) + "\n").encode()
    if not manifest_path.exists() or manifest_path.read_bytes() != payload:
        planned.append((manifest_path, payload))
    if agents is not None and old != new:
        planned.append((agents, new))
    return planned


def atomic_write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else None
    fd, name = tempfile.mkstemp(prefix=".design-kit-", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(content)
        if mode is not None:
            os.chmod(name, mode)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def install(source, target=None, check=False, with_software=None, host="codex", scope="project", user_home=None):
    # Preflight every conflict before changing any file. Writes are atomic per file.
    planned = installation_plan(source, target, with_software, host, scope, user_home)
    if check:
        return planned
    originals = [(path, path.read_bytes() if path.exists() else None) for path, _ in planned]
    completed = []
    try:
        for (path, payload), (_, original) in zip(planned, originals):
            atomic_write(path, payload)
            completed.append((path, original))
    except OSError:
        # Best-effort rollback for ordinary write errors; not a crash transaction.
        for path, original in reversed(completed):
            try:
                path.unlink() if original is None else atomic_write(path, original)
            except OSError:
                pass
        raise
    return planned


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, nargs="?", help="Existing project directory (project scope only)")
    parser.add_argument("--scope", choices=("project", "user"), default="project", help="Install for one project or globally for this user")
    parser.add_argument("--user-home", type=Path, help="Explicit existing user/profile home (user scope only)")
    parser.add_argument("--host", choices=HOSTS, default="codex", help="Target interface/runtime (three supported platforms)")
    parser.add_argument("--check", action="store_true", help="Report drift without writes (exit 1 if changes needed)")
    routing = parser.add_mutually_exclusive_group()
    routing.add_argument("--with-software", dest="with_software", action="store_true", help="Legacy opt-in to separate frontend guidance outside image-first Design Kit")
    routing.add_argument("--design-only", dest="with_software", action="store_false", help="Keep the image-first skill pointer, removing the legacy frontend route")
    parser.set_defaults(with_software=None)
    args = parser.parse_args()
    try:
        root = installation_root(args.target, args.scope, args.user_home)
        planned = install(Path(__file__).resolve().parents[1], args.target, args.check, args.with_software, args.host, args.scope, args.user_home)
    except (ValueError, OSError) as error:
        print("ERROR: " + str(error), file=sys.stderr)
        return 2
    print(("CHECK: " if args.check else "INSTALL: ") + str(len(planned)) + " file(s) " + ("need changes" if args.check else "changed"))
    print("Scope: " + args.scope + "; host: " + args.host + "; root: " + str(root))
    for path, _ in planned:
        print(path.relative_to(root))
    if args.scope == "user":
        print("Global skill available for relevant tasks; project records and global instruction files were not changed.")
    print("No model calls, dependency installation, or network requests performed.")
    print("This is a package check, not a test of model activation or design quality.")
    return 1 if args.check and planned else 0


if __name__ == "__main__":
    raise SystemExit(main())
