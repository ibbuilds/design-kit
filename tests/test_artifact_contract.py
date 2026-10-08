"""Image-first instruction contract checks, not model or aesthetic evaluations.

The package installer/provider tests cover operational safety. These assertions
make the new visual-only scope difficult to accidentally regress back into an
artifact-first/coded-design default.
"""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = (
    "SKILL.md", "IMAGE_WORKFLOW.md", "FOUNDATION.md", "BRIEF.md", "ONBOARDING.md",
    "DESIGN_DIRECTION.md", "REFERENCE_ROUTER.md", "EXECUTION.md", "PROMPT.md",
    "WORKFLOW.md", "README.md", "docs/GENERAL_GUIDE.txt",
    "docs/01_design_from_scratch.txt", "docs/02_improve_existing_design.txt",
    "docs/03_frontend_engineering.txt",
)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


class ImageFirstContractTests(unittest.TestCase):
    def test_skill_metadata_is_scoped_and_readable(self):
        skill = read("SKILL.md")
        self.assertTrue(skill.startswith("---\nname: design-kit\n"))
        header = skill.split("---", 2)[1]
        raw = next(line.partition(": ")[2] for line in header.splitlines()
                   if line.startswith("description: "))
        description = json.loads(raw)
        self.assertLessEqual(len(description), 240)
        self.assertIn("Image-first", description)
        self.assertIn("not frontend implementation", description)
        self.assertLessEqual(len(skill.split()), 1400)

    def test_invocation_governs_images_and_stops_before_implementation(self):
        metadata = read("agents/openai.yaml")
        raw = next(line.partition(": ")[2] for line in metadata.splitlines()
                   if line.startswith("  default_prompt: "))
        prompt = json.loads(raw)
        for phrase in ("$design-kit", "section images", "foundation",
                       "first section", "stop before actual design or code"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, prompt)
        self.assertIn('value: "onepagelove"', metadata)
        self.assertIn('value: "awwwards"', metadata)

    def test_actual_workflow_has_dependencies_and_stop_boundary(self):
        skill = read("SKILL.md")
        for phrase in ("user-owned foundation", "first section", "section by section",
                       "actual selected first-section image", "page order",
                       "**Stop at this visual specification.**",
                       "not human-accepted"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, skill)
        self.assertIn("not a coded section", read("IMAGE_WORKFLOW.md"))
        self.assertIn("not an implementation claim", read("BRIEF.md"))
        self.assertIn("User", read("FOUNDATION.md"))

    def test_image_prompt_is_specific_and_revisions_are_substantial(self):
        workflow = read("IMAGE_WORKFLOW.md")
        for phrase in ("Section job", "Actual copy and content", "aspect ratio",
                       "composition", "preserve / replace / expected visible difference",
                       "contact sheet", "third-party"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, workflow)
        self.assertIn("There is **no arbitrary two-pass cap**", read("SKILL.md"))
        self.assertIn("no universal two-pass cap", read("EXECUTION.md"))
        self.assertIn("small corrections", workflow)

    def test_user_owns_foundation_acceptance_and_actual_build(self):
        for relative in ("SKILL.md", "ONBOARDING.md", "README.md", "BRIEF.md"):
            with self.subTest(file=relative):
                text = read(relative)
                self.assertRegex(text, r"(?i)user")
                self.assertRegex(text, r"(?i)foundation")
        self.assertIn("agent-proposed", read("SKILL.md"))
        self.assertIn("not human approval", read("ONBOARDING.md"))
        self.assertIn("No component implementation", read("IMAGE_WORKFLOW.md"))
        self.assertIn("outside this skill", read("SKILL.md"))

    def test_reference_mcp_flow_survives_without_mandatory_browsing(self):
        router = read("REFERENCE_ROUTER.md")
        for phrase in ("Awwwards", "One Page Love", "no minimum reference count",
                       "not a replacement visual foundation", "reference_scope.py"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, router)
        self.assertIn("Skills.sh", read("IMAGE_WORKFLOW.md"))
        self.assertIn("matched", read("EXECUTION.md"))

    def test_old_default_is_not_reintroduced_by_active_guides(self):
        forbidden = (
            r"one candidate and at most two",
            r"author one coherent candidate in the existing medium",
            r"no additional approval gate before writing",
            r"system specimen before styled page",
            r"simulator loop until perfect",
        )
        for relative in ACTIVE:
            for pattern in forbidden:
                with self.subTest(file=relative, pattern=pattern):
                    self.assertIsNone(re.search(pattern, read(relative), re.I))

    def test_package_links_and_validation_are_honest(self):
        installer = read("scripts/install.py")
        for relative in ("IMAGE_WORKFLOW.md", "FOUNDATION.md"):
            self.assertIn('"' + relative + '"', installer)
            self.assertIn("[" + relative.split(".")[0].capitalize(), read("README.md"))
        self.assertIn("with/without-kit", read("README.md"))
        self.assertIn("do not prove", read("README.md"))
        self.assertIn("not frontend", read("SKILL.md"))
        self.assertIn("separate user", read("docs/03_frontend_engineering.txt"))


if __name__ == "__main__":
    unittest.main()
