"""Offline package tests; they do not evaluate model behavior or visual quality."""
import importlib.util
import json
import os
import re
import stat
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("design_kit_install", ROOT / "scripts/install.py")
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.source, self.target = root / "kit", root / "project"
        self.source.mkdir()
        self.target.mkdir()
        # Small deterministic fixtures exercise the real installer, not any LLM.
        for relative in installer.PACKAGE:
            path = self.source / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("fixture for " + relative + "\n", encoding="utf-8")
        self.dest = self.target / ".agents/skills/design-kit"

    def test_install_copies_complete_bundle_and_adds_pointer(self):
        installer.install(self.source, self.target)
        for relative in installer.PACKAGE:
            self.assertEqual((self.source / relative).read_bytes(), (self.dest / relative).read_bytes())
        self.assertIn(".agents/skills/design-kit/SKILL.md", (self.target / "AGENTS.md").read_text())

    def test_repeat_install_is_no_op(self):
        installer.install(self.source, self.target)
        self.assertEqual([], installer.install(self.source, self.target))

    def test_software_is_opt_in_on_new_install(self):
        installer.install(self.source, self.target)
        self.assertNotIn(installer.SOFTWARE_RULE, (self.target / "AGENTS.md").read_text())

    def test_software_install_survives_ordinary_updates(self):
        installer.install(self.source, self.target, with_software=True)
        original = (self.target / "AGENTS.md").read_bytes()
        self.assertIn(installer.SOFTWARE_RULE.encode(), original)
        (self.source / "SOFTWARE.md").write_text("Updated engineering workflow")
        installer.install(self.source, self.target)
        self.assertEqual(original, (self.target / "AGENTS.md").read_bytes())
        self.assertEqual("Updated engineering workflow", (self.dest / "SOFTWARE.md").read_text())
        self.assertEqual([], installer.install(self.source, self.target))

    def test_software_pointer_can_be_enabled_and_disabled_without_losing_rules(self):
        before, after = "# Project\nPreserve contracts.\n", "\nKeep tests.\n"
        (self.target / "AGENTS.md").write_text(before)
        installer.install(self.source, self.target)
        agents = self.target / "AGENTS.md"
        agents.write_text(agents.read_text() + after)
        installer.install(self.source, self.target, with_software=True)
        self.assertIn(installer.SOFTWARE_RULE, agents.read_text())
        installer.install(self.source, self.target, with_software=False)
        self.assertEqual(before + installer.POINTER + after, agents.read_text())
        self.assertEqual([], installer.install(self.source, self.target, with_software=False))

    def test_check_software_route_does_not_write(self):
        installer.install(self.source, self.target)
        agents = self.target / "AGENTS.md"
        before = {p: p.read_bytes() for p in self.target.rglob("*") if p.is_file()}
        planned = installer.install(self.source, self.target, check=True, with_software=True)
        self.assertEqual({agents, self.dest / installer.MANIFEST}, {path for path, _ in planned})
        self.assertEqual(before, {p: p.read_bytes() for p in self.target.rglob("*") if p.is_file()})

    def test_project_prose_cannot_silently_enable_software_route(self):
        text = "Reference only: .agents/skills/design-kit/SOFTWARE.md\n"
        (self.target / "AGENTS.md").write_text(text)
        installer.install(self.source, self.target)
        self.assertEqual(text + installer.POINTER, (self.target / "AGENTS.md").read_text())
        self.assertEqual([], installer.install(self.source, self.target))

    def test_update_from_previous_bundle_adds_new_resources(self):
        added = {"REFERENCE_ROUTER.md", "EXECUTION.md", "SOFTWARE.md", "DESIGN_DIRECTION.md", "docs/QUALITY_EVIDENCE.md"}
        old_package = tuple(path for path in installer.PACKAGE if path not in added)
        with patch.object(installer, "PACKAGE", old_package):
            installer.install(self.source, self.target)
        manifest = self.dest / installer.MANIFEST
        previous = json.loads(manifest.read_text())
        previous.pop("software")
        manifest.write_text(json.dumps(previous))
        self.assertFalse((self.dest / "SOFTWARE.md").exists())
        installer.install(self.source, self.target, with_software=True)
        for relative in added:
            self.assertEqual((self.source / relative).read_bytes(), (self.dest / relative).read_bytes())
        self.assertIn(installer.SOFTWARE_RULE, (self.target / "AGENTS.md").read_text())
        self.assertEqual([], installer.install(self.source, self.target))

    def test_check_does_not_write(self):
        self.assertTrue(installer.install(self.source, self.target, check=True))
        self.assertEqual([], list(self.target.iterdir()))

    def test_target_instructions_and_legacy_brief_survive(self):
        original = b"# Project\r\nKeep my instructions.\r\n"
        (self.target / "AGENTS.md").write_bytes(original)
        legacy = self.target / ".design-kit/BRIEF.md"
        legacy.parent.mkdir()
        legacy.write_text("Actual product facts")
        installer.install(self.source, self.target)
        self.assertTrue((self.target / "AGENTS.md").read_bytes().startswith(original))
        self.assertEqual("Actual product facts", legacy.read_text())

    def test_utf8_project_instructions_and_resources_survive_update(self):
        original = "# Proyecto\nDiseño aprobado: tipografía y navegación.\n".encode("utf-8")
        (self.target / "AGENTS.md").write_bytes(original)
        (self.source / "SOFTWARE.md").write_text("Programación: éxito y recuperación.\n", encoding="utf-8")
        installer.install(self.source, self.target, with_software=True)
        self.assertTrue((self.target / "AGENTS.md").read_bytes().startswith(original))
        self.assertEqual((self.source / "SOFTWARE.md").read_bytes(), (self.dest / "SOFTWARE.md").read_bytes())
        self.assertEqual([], installer.install(self.source, self.target))

    def test_exact_legacy_pointer_is_replaced(self):
        old = "# App\n" + installer.LEGACY + "\nOther rules.\n"
        (self.target / "AGENTS.md").write_text(old)
        installer.install(self.source, self.target)
        text = (self.target / "AGENTS.md").read_text()
        self.assertNotIn(installer.LEGACY, text)
        self.assertIn("Other rules.", text)
        self.assertEqual(1, text.count(installer.START))

    def test_local_edit_prevents_all_updates(self):
        installer.install(self.source, self.target)
        (self.dest / "REFERENCES.md").write_text("Local references")
        (self.source / "SKILL.md").write_text("New upstream skill")
        old_skill = (self.dest / "SKILL.md").read_bytes()
        with self.assertRaisesRegex(ValueError, "refusing overwrite"):
            installer.install(self.source, self.target)
        self.assertEqual(old_skill, (self.dest / "SKILL.md").read_bytes())
        self.assertEqual("Local references", (self.dest / "REFERENCES.md").read_text())

    def test_upstream_update_preserves_unmanaged_extra_files(self):
        installer.install(self.source, self.target)
        (self.dest / "local-note.txt").write_text("Keep")
        (self.source / "SKILL.md").write_text("Updated")
        installer.install(self.source, self.target)
        self.assertEqual("Updated", (self.dest / "SKILL.md").read_text())
        self.assertEqual("Keep", (self.dest / "local-note.txt").read_text())

    def test_missing_source_is_rejected_before_writes(self):
        (self.source / "REFERENCES.md").unlink()
        with self.assertRaisesRegex(ValueError, "Missing"):
            installer.install(self.source, self.target)
        self.assertEqual([], list(self.target.iterdir()))

    def test_unmanaged_existing_skill_is_not_overwritten(self):
        self.dest.mkdir(parents=True)
        (self.dest / "SKILL.md").write_text("Handwritten")
        with self.assertRaisesRegex(ValueError, "not managed"):
            installer.install(self.source, self.target)

    def test_invalid_manifest_is_rejected(self):
        self.dest.mkdir(parents=True)
        (self.dest / installer.MANIFEST).write_text(json.dumps({"format": 1, "name": "design-kit", "files": {"../escape": "0" * 64}}))
        with self.assertRaisesRegex(ValueError, "Invalid"):
            installer.install(self.source, self.target)

    def test_invalid_manifest_routing_is_rejected_before_writes(self):
        installer.install(self.source, self.target)
        manifest = self.dest / installer.MANIFEST
        data = json.loads(manifest.read_text())
        data["software"] = "true"
        manifest.write_text(json.dumps(data))
        before = {p: p.read_bytes() for p in self.target.rglob("*") if p.is_file()}
        with self.assertRaisesRegex(ValueError, "Invalid software"):
            installer.install(self.source, self.target, with_software=True)
        self.assertEqual(before, {p: p.read_bytes() for p in self.target.rglob("*") if p.is_file()})

    def test_malformed_pointer_rejects_install_before_writes(self):
        (self.target / "AGENTS.md").write_text(installer.START)
        with self.assertRaisesRegex(ValueError, "Malformed"):
            installer.install(self.source, self.target)
        self.assertFalse(self.dest.exists())

    def test_kit_is_not_a_target(self):
        with self.assertRaisesRegex(ValueError, "not the kit"):
            installer.install(self.source, self.source)

    def test_nonexistent_target_is_not_created(self):
        target = self.target / "missing"
        with self.assertRaisesRegex(ValueError, "existing project"):
            installer.install(self.source, target)
        self.assertFalse(target.exists())

    def test_symlinked_destination_is_refused(self):
        other = self.source / "outside"
        other.mkdir()
        try:
            (self.target / ".agents").symlink_to(other, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks unavailable")
        with self.assertRaisesRegex(ValueError, "symlink"):
            installer.install(self.source, self.target)
        self.assertEqual([], list(other.iterdir()))

    def test_source_library_survives_byte_for_byte(self):
        before = {p: (self.source / p).read_bytes() for p in installer.PACKAGE}
        installer.install(self.source, self.target)
        self.assertEqual(before, {p: (self.source / p).read_bytes() for p in installer.PACKAGE})

    def test_partial_write_error_rolls_back_completed_files(self):
        real_write = installer.atomic_write
        calls = 0
        def fail_second(path, content):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("simulated disk failure")
            real_write(path, content)
        with patch.object(installer, "atomic_write", side_effect=fail_second):
            with self.assertRaises(OSError):
                installer.install(self.source, self.target)
        self.assertFalse((self.dest / "SKILL.md").exists())
        self.assertFalse((self.target / "AGENTS.md").exists())


    def test_active_override_gets_pointer_not_inactive_agents(self):
        ordinary = self.target / "AGENTS.md"
        ordinary.write_bytes(b"# Ordinary instructions\n")
        override = self.target / "AGENTS.override.md"
        original = b"# Active instructions\r\nKeep this.\r\n"
        override.write_bytes(original)
        installer.install(self.source, self.target)
        self.assertEqual(b"# Ordinary instructions\n", ordinary.read_bytes())
        self.assertTrue(override.read_bytes().startswith(original))
        self.assertIn(installer.START.encode(), override.read_bytes())
        self.assertEqual([], installer.install(self.source, self.target))

    def test_software_route_uses_active_override_and_preserves_opt_in(self):
        ordinary = self.target / "AGENTS.md"
        ordinary.write_text("# Inactive instructions\n")
        override = self.target / "AGENTS.override.md"
        override.write_text("# Active project\n")
        installer.install(self.source, self.target, with_software=True)
        self.assertIn(installer.SOFTWARE_RULE, override.read_text())
        self.assertEqual("# Inactive instructions\n", ordinary.read_text())
        self.assertEqual([], installer.install(self.source, self.target))

    def test_software_opt_in_survives_new_override_and_return_to_fallback(self):
        installer.install(self.source, self.target, with_software=True)
        override = self.target / "AGENTS.override.md"
        override.write_text("# New active instructions\n")
        ordinary = self.target / "AGENTS.md"
        before = ordinary.read_bytes()
        planned = installer.install(self.source, self.target, check=True)
        self.assertIn(override, [p for p, _ in planned])
        installer.install(self.source, self.target)
        self.assertIn(installer.SOFTWARE_RULE, override.read_text())
        self.assertEqual(before, ordinary.read_bytes())
        self.assertEqual([], installer.install(self.source, self.target))
        override.write_text(" \n")
        self.assertEqual([], installer.install(self.source, self.target))

    def test_saved_opt_in_survives_replacement_of_root_instruction_file(self):
        installer.install(self.source, self.target, with_software=True)
        agents = self.target / "AGENTS.md"
        agents.write_text("# Replacement project instructions\n")
        installer.install(self.source, self.target)
        self.assertTrue(agents.read_text().startswith("# Replacement project instructions\n"))
        self.assertIn(installer.SOFTWARE_RULE, agents.read_text())
        self.assertEqual([], installer.install(self.source, self.target))

    def test_disabled_software_route_does_not_return_with_stale_fallback(self):
        installer.install(self.source, self.target, with_software=True)
        override = self.target / "AGENTS.override.md"
        override.write_text("# Override\n")
        installer.install(self.source, self.target, with_software=False)
        self.assertNotIn(installer.SOFTWARE_RULE, override.read_text())
        override.write_text(" \n")
        installer.install(self.source, self.target)
        self.assertNotIn(installer.SOFTWARE_RULE, (self.target / "AGENTS.md").read_text())
        self.assertEqual([], installer.install(self.source, self.target))

    def test_locally_edited_new_resource_blocks_update_before_pointer_change(self):
        installer.install(self.source, self.target)
        (self.dest / "SOFTWARE.md").write_text("My engineering rules")
        (self.source / "SKILL.md").write_text("New skill")
        before = {p: p.read_bytes() for p in self.target.rglob("*") if p.is_file()}
        with self.assertRaisesRegex(ValueError, "refusing overwrite"):
            installer.install(self.source, self.target, with_software=True)
        self.assertEqual(before, {p: p.read_bytes() for p in self.target.rglob("*") if p.is_file()})

    def test_empty_override_leaves_fallback_active(self):
        override = self.target / "AGENTS.override.md"
        override.write_bytes(b" \r\n")
        installer.install(self.source, self.target)
        self.assertEqual(b" \r\n", override.read_bytes())
        self.assertIn(installer.START, (self.target / "AGENTS.md").read_text())

    def test_new_override_is_detected_by_check_without_writes(self):
        installer.install(self.source, self.target)
        override = self.target / "AGENTS.override.md"
        override.write_bytes(b"# Added later\n")
        planned = installer.install(self.source, self.target, check=True)
        self.assertEqual([override], [path for path, _ in planned])
        self.assertEqual(b"# Added later\n", override.read_bytes())

    def test_malformed_override_is_rejected_before_writes(self):
        (self.target / "AGENTS.override.md").write_text(installer.START)
        with self.assertRaisesRegex(ValueError, "Malformed"):
            installer.install(self.source, self.target)
        self.assertFalse(self.dest.exists())

    def test_symlinked_override_is_not_modified(self):
        outside = self.source / "other-instructions.md"
        outside.write_text("Preserve")
        try:
            (self.target / "AGENTS.override.md").symlink_to(outside)
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks unavailable")
        with self.assertRaisesRegex(ValueError, "symlink"):
            installer.install(self.source, self.target)
        self.assertEqual("Preserve", outside.read_text())
        self.assertFalse(self.dest.exists())

    def test_symlinked_source_parent_is_rejected_before_writes(self):
        original = self.source / "agents"
        other = self.source / "external-agents"
        original.rename(other)
        try:
            original.symlink_to(other, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks unavailable")
        with self.assertRaisesRegex(ValueError, "symlink"):
            installer.install(self.source, self.target)
        self.assertEqual([], list(self.target.iterdir()))

    @unittest.skipUnless(os.name == "posix", "POSIX permission semantics")
    def test_replacing_instructions_preserves_permissions(self):
        path = self.target / "AGENTS.md"
        path.write_text("# Shared instructions\n")
        path.chmod(0o640)
        installer.install(self.source, self.target)
        self.assertEqual(0o640, stat.S_IMODE(path.stat().st_mode))

    def test_failed_update_restores_existing_files(self):
        installer.install(self.source, self.target)
        (self.source / "SKILL.md").write_text("Updated skill")
        (self.source / "TASTE.md").write_text("Updated taste")
        before = {p: p.read_bytes() for p in self.target.rglob("*") if p.is_file()}
        real_write = installer.atomic_write
        calls = 0
        def fail_second(path, content):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("simulated update failure")
            real_write(path, content)
        with patch.object(installer, "atomic_write", side_effect=fail_second):
            with self.assertRaises(OSError):
                installer.install(self.source, self.target)
        after = {p: p.read_bytes() for p in self.target.rglob("*") if p.is_file()}
        self.assertEqual(before, after)


class SkillContractTests(unittest.TestCase):
    def test_real_installed_bundle_has_resolvable_local_document_links(self):
        # Validate the actual exported package in a clean project. A valid link
        # in the checkout can still be broken if its resource is not packaged.
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder)
            installer.install(ROOT, target, with_software=True)
            bundle = target / ".agents/skills/design-kit"
            links_checked = 0
            for document in bundle.rglob("*.md"):
                text = document.read_text(encoding="utf-8")
                for href in re.findall(r"\[[^\]\n]+\]\(([^)\s]+)\)", text):
                    url = urlsplit(href)
                    if url.scheme or url.netloc or not url.path:
                        continue
                    resource = (document.parent / unquote(url.path)).resolve()
                    self.assertTrue(resource.is_relative_to(bundle.resolve()), (document, href))
                    self.assertTrue(resource.is_file(), (document, href))
                    links_checked += 1
            self.assertGreater(links_checked, 0)
            self.assertEqual([], installer.install(ROOT, target, check=True))

    def test_frontmatter_and_native_invocation(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\nname: design-kit\n"))
        self.assertIn("description:", text.split("---", 2)[1])
        meta = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
        self.assertIn("allow_implicit_invocation: true", meta)
        self.assertIn("$design-kit", meta)

    def test_metadata_strings_are_unambiguous_without_yaml_dependency(self):
        # Our authored metadata uses JSON-quoted strings, a valid YAML subset.
        # Unlike a substring check, this rejects an unquoted colon in description.
        lines = (ROOT / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[1].splitlines()
        raw = next(line.partition(": ")[2] for line in lines if line.startswith("description: "))
        description = json.loads(raw)
        self.assertIsInstance(description, str)
        self.assertTrue(0 < len(description) <= 1024)
        ui = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8").splitlines()
        for key in ("display_name", "short_description", "default_prompt"):
            raw = next(line.partition(": ")[2] for line in ui if line.startswith("  " + key + ": "))
            self.assertIsInstance(json.loads(raw), str)
        self.assertIn("policy:", ui)
        self.assertIn("  allow_implicit_invocation: true", ui)

    def test_reference_library_is_packaged_not_replaced(self):
        self.assertIn("REFERENCES.md", installer.PACKAGE)
        self.assertIn("[REFERENCES.md](REFERENCES.md)", (ROOT / "SKILL.md").read_text(encoding="utf-8"))
        self.assertIn("[SKILL.md](SKILL.md)", (ROOT / "WORKFLOW.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
