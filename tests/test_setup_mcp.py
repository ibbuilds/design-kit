"""Offline setup tests: configuration safety, not live provider/model behavior."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
try:
    SPEC = importlib.util.spec_from_file_location("design_kit_mcp", ROOT / "scripts/setup_mcp.py")
    setup = importlib.util.module_from_spec(SPEC)
    SPEC.loader.exec_module(setup)
finally:
    sys.path.pop(0)


class SetupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        # Normalize Windows 8.3 aliases before comparing planned config paths.
        self.target = Path(self.temp.name).resolve()

    def write_json(self, data, host="claude-code"):
        path = self.target / setup.HOSTS[host][0]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def test_plan_never_creates_files(self):
        for host in setup.HOSTS:
            if host == "codex" and setup.tomllib is None:
                continue
            with self.subTest(host=host):
                result = setup.configure(self.target, host)
                self.assertEqual(["awwwards", "onepagelove"], result["added"])
                self.assertFalse(result["path"].exists())
        self.assertEqual([], list(self.target.iterdir()))

    def test_user_scope_uses_native_global_files_and_preserves_other_settings(self):
        for host, relative in setup.USER_CONFIGS.items():
            if host == "codex" and setup.tomllib is None:
                continue
            with self.subTest(host=host), tempfile.TemporaryDirectory() as folder:
                home = Path(folder).resolve()
                path = home / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                original = (b'model = "keep-current-model"\n' if host == "codex" else
                            b'{"projects": {"existing-project": {"keep": true}}, "theme": "keep"}\n')
                path.write_bytes(original)
                plan = setup.configure(host=host, scope="user", user_home=home)
                self.assertEqual(path, plan["path"])
                self.assertEqual(original, path.read_bytes())
                result = setup.configure(host=host, scope="user", user_home=home, apply=True)
                self.assertEqual(original, result["backup"].read_bytes())
                data = setup.load_config(path.read_bytes(), host)
                if host == "codex":
                    self.assertEqual("keep-current-model", data["model"])
                else:
                    self.assertEqual({"existing-project": {"keep": True}}, data["projects"])
                    self.assertEqual("keep", data["theme"])
                self.assertEqual({"awwwards", "onepagelove"}, set(data[setup.HOSTS[host][1]]))
                self.assertEqual([], setup.configure(host=host, scope="user", user_home=home, apply=True)["added"])

    def test_user_scope_cannot_confuse_a_project_target_or_profile(self):
        for arguments in ({"scope": "user", "target": self.target},
                          {"scope": "project", "target": self.target, "user_home": self.target}):
            with self.subTest(arguments=arguments), self.assertRaises(ValueError):
                setup.configure(**arguments, apply=True)
        self.assertEqual([], list(self.target.iterdir()))

    def test_user_scope_cli_plans_without_touching_project_config(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/setup_mcp.py"),
                                 "--scope", "user", "--user-home", str(self.target),
                                 "--host", "claude-code"], capture_output=True, text=True, timeout=15)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn(".claude.json", result.stdout)
        self.assertIn("PLAN ONLY", result.stdout)
        self.assertEqual([], list(self.target.iterdir()))

    def test_json_host_schemas_and_idempotence(self):
        for host, url_key in (("claude-code", "url"), ("gemini-cli", "httpUrl"), ("antigravity", "serverUrl")):
            with self.subTest(host=host):
                result = setup.configure(self.target, host, apply=True, windows=True)
                servers = json.loads(result["path"].read_text())["mcpServers"]
                self.assertEqual(setup.OPL_URL, servers["onepagelove"][url_key])
                self.assertEqual("cmd.exe", servers["awwwards"]["command"])
                self.assertEqual(["/d", "/c", "npx.cmd", "-y", "awwwards-mcp"], servers["awwwards"]["args"])
                if host == "claude-code":
                    self.assertEqual("http", servers["onepagelove"]["type"])
                    self.assertEqual("stdio", servers["awwwards"]["type"])
                before = result["path"].read_bytes()
                repeated = setup.configure(self.target, host, apply=True)
                self.assertEqual([], repeated["added"])
                self.assertIsNone(repeated["backup"])
                self.assertEqual(before, result["path"].read_bytes())

    @unittest.skipIf(setup.tomllib is None, "Codex TOML needs Python 3.11+")
    def test_codex_preserves_comments_settings_and_other_servers(self):
        path = self.target / ".codex/config.toml"
        path.parent.mkdir()
        original = b'# Personal settings\nmodel = "current-choice"\n[mcp_servers.other]\ncommand = "local-tool"\n'
        path.write_bytes(original)
        result = setup.configure(self.target, "codex", apply=True, windows=False)
        self.assertTrue(path.read_bytes().startswith(original))
        data = setup.tomllib.loads(path.read_text())
        self.assertEqual("current-choice", data["model"])
        self.assertEqual("local-tool", data["mcp_servers"]["other"]["command"])
        self.assertEqual("npx", data["mcp_servers"]["awwwards"]["command"])
        self.assertEqual(setup.OPL_URL, data["mcp_servers"]["onepagelove"]["url"])
        self.assertEqual(original, result["backup"].read_bytes())
        self.assertEqual([], setup.configure(self.target, "codex", apply=True)["added"])

    def test_existing_aliases_are_reused_with_their_options(self):
        original = {"mcpServers": {
            "my-opl": {"url": setup.OPL_URL + "/", "type": "http", "headers": {"X-Custom": "retain"}},
            "my-awards": {"command": "C:\\node\\npx.cmd", "args": ["-y", "awwwards-mcp@1.7.2"], "env": {"CUSTOM": "retain"}}
        }}
        path = self.write_json(original)
        before = path.read_bytes()
        result = setup.configure(self.target, "claude-code", apply=True)
        self.assertEqual([], result["added"])
        self.assertEqual(before, path.read_bytes())
        self.assertEqual([], list(self.target.glob("*.design-kit-backup-*")))

    def test_add_only_selected_provider_preserves_unrelated_configuration(self):
        original = {"theme": "custom", "mcpServers": {"other": {"command": "keep", "env": {"PRIVATE": "do-not-print"}}}}
        path = self.write_json(original, "gemini-cli")
        before = path.read_bytes()
        result = setup.configure(self.target, "gemini-cli", ["onepagelove"], apply=True)
        updated = json.loads(path.read_text())
        self.assertEqual("custom", updated["theme"])
        self.assertEqual(original["mcpServers"]["other"], updated["mcpServers"]["other"])
        self.assertNotIn("awwwards", updated["mcpServers"])
        self.assertEqual(before, result["backup"].read_bytes())

    def test_existing_windows_wrapper_is_reused(self):
        for command, args in (("cmd", ["/c", "npx", "-y", "awwwards-mcp"]),
                              ("C:\\Windows\\System32\\cmd.exe", ["/d", "/c", "npx.cmd", "-y", "awwwards-mcp"])):
            path = self.write_json({"mcpServers": {"my-awards": {"command": command, "args": args}}})
            before = path.read_bytes()
            result = setup.configure(self.target, "claude-code", ["awwwards"], apply=True)
            self.assertEqual([], result["added"])
            self.assertEqual(before, path.read_bytes())

    def test_claude_missing_http_type_is_not_claimed_configured(self):
        path = self.write_json({"mcpServers": {"alias": {"url": setup.OPL_URL}}})
        before = path.read_bytes()
        with self.assertRaisesRegex(ValueError, "transport type"):
            setup.configure(self.target, "claude-code", apply=True)
        self.assertEqual(before, path.read_bytes())

    def test_conflict_preflights_all_changes(self):
        path = self.write_json({"mcpServers": {"onepagelove": {"type": "http", "url": "https://other.example/mcp"}}})
        before = path.read_bytes()
        with self.assertRaisesRegex(ValueError, "Conflicting"):
            setup.configure(self.target, "claude-code", apply=True)
        self.assertEqual(before, path.read_bytes())
        self.assertEqual([path], list(self.target.iterdir()))

    def test_disabled_providers_are_never_reenabled_or_duplicated(self):
        for field, value in (("enabled", False), ("disabled", True)):
            path = self.write_json({"mcpServers": {"user-opl": {"type": "http", "url": setup.OPL_URL, field: value}}})
            before = path.read_bytes()
            with self.assertRaisesRegex(ValueError, "disabled"):
                setup.configure(self.target, "claude-code", apply=True)
            self.assertEqual(before, path.read_bytes())

    def test_invalid_json_jsonc_and_duplicate_keys_are_not_rewritten(self):
        path = self.target / ".mcp.json"
        for invalid in ('{"mcpServers":', '{/* comment */ "mcpServers": {}}', '{"mcpServers": {}, "mcpServers": {}}', '[]'):
            path.write_text(invalid)
            with self.assertRaises(ValueError):
                setup.configure(self.target, "claude-code", apply=True)
            self.assertEqual(invalid, path.read_text())

    @unittest.skipIf(setup.tomllib is None, "Codex TOML needs Python 3.11+")
    def test_invalid_or_frozen_toml_is_not_rewritten(self):
        path = self.target / ".codex/config.toml"
        path.parent.mkdir()
        for invalid in ('model = [', 'mcp_servers = {}\n'):
            path.write_text(invalid)
            with self.assertRaises(ValueError):
                setup.configure(self.target, "codex", apply=True)
            self.assertEqual(invalid, path.read_text())
            self.assertEqual([path], list(path.parent.iterdir()))

    def test_missing_or_unsupported_target_does_not_write(self):
        with self.assertRaisesRegex(ValueError, "existing project"):
            setup.configure(self.target / "missing", "claude-code", apply=True)
        with self.assertRaisesRegex(ValueError, "Unsupported"):
            setup.configure(self.target, "cursor", apply=True)
        with self.assertRaisesRegex(ValueError, "supported providers"):
            setup.configure(self.target, "claude-code", ["inspo"], apply=True)
        self.assertEqual([], list(self.target.iterdir()))

    def test_shared_kit_cannot_be_a_configuration_target(self):
        with self.assertRaisesRegex(ValueError, "not the shared kit"):
            setup.configure(ROOT, "claude-code", apply=True)

    def test_atomic_write_failure_preserves_original_and_backup(self):
        path = self.write_json({"mcpServers": {"other": {"command": "keep"}}})
        before = path.read_bytes()
        with patch.object(setup, "atomic_write", side_effect=OSError("disk failure")):
            with self.assertRaises(OSError):
                setup.configure(self.target, "claude-code", apply=True)
        self.assertEqual(before, path.read_bytes())
        backups = list(self.target.glob("*.design-kit-backup-*"))
        self.assertEqual(1, len(backups))
        self.assertEqual(before, backups[0].read_bytes())

    def test_concurrent_change_is_not_overwritten(self):
        path = self.write_json({"mcpServers": {}})
        real_plan = setup.plan
        def racing_plan(*args, **kwargs):
            result = real_plan(*args, **kwargs)
            path.write_text('{"human-edit": true}')
            return result
        with patch.object(setup, "plan", side_effect=racing_plan):
            with self.assertRaisesRegex(ValueError, "changed during"):
                setup.configure(self.target, "claude-code", apply=True)
        self.assertEqual('{"human-edit": true}', path.read_text())

    def test_symlinked_config_parent_is_refused(self):
        outside = self.target / "outside"
        outside.mkdir()
        try:
            (self.target / ".gemini").symlink_to(outside, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks unavailable")
        with self.assertRaisesRegex(ValueError, "symlink"):
            setup.configure(self.target, "gemini-cli", apply=True)
        self.assertEqual([], list(outside.iterdir()))

    def test_cli_defaults_to_plan_without_writes(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/setup_mcp.py"), str(self.target),
                                 "--host", "claude-code"], capture_output=True, text=True, timeout=15)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("PLAN ONLY", result.stdout)
        self.assertEqual([], list(self.target.iterdir()))


if __name__ == "__main__":
    unittest.main()
