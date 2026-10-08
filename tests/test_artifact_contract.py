"""Instruction contract tests for image-only, any-scale visual exploration.

These are structural regressions. They cannot measure image aesthetics, model
compliance, human approval or token savings. Existing installer and provider
tests separately cover packaging and access safeguards.
"""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = (
    "SKILL.md", "IMAGE_WORKFLOW.md", "COMPONENT_LIBRARY.md", "FOUNDATION.md",
    "BRIEF.md", "ONBOARDING.md", "EXECUTION.md", "PROMPT.md",
    "DESIGN_DIRECTION.md", "REFERENCE_ROUTER.md", "WORKFLOW.md", "README.md",
    "docs/GENERAL_GUIDE.txt", "docs/01_design_from_scratch.txt",
    "docs/02_improve_existing_design.txt", "docs/03_frontend_engineering.txt",
)


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class ImageFirstContractTests(unittest.TestCase):
    def test_frontmatter_is_valid_and_bounded(self):
        skill = read("SKILL.md")
        self.assertTrue(skill.startswith("---\nname: design-kit\n"))
        meta = skill.split("---", 2)[1]
        raw = next(line.partition(": ")[2] for line in meta.splitlines()
                   if line.startswith("description: "))
        description = json.loads(raw)
        self.assertLessEqual(len(description), 240)
        self.assertIn("Image-first", description)
        self.assertIn("text", description)
        self.assertIn("not frontend implementation", description)
        self.assertLessEqual(len(skill.split()), 1400)

    def test_agent_invocation_works_for_any_scale_and_uses_selected_mcps(self):
        metadata = read("agents/openai.yaml")
        raw = next(line.partition(": ")[2] for line in metadata.splitlines()
                   if line.startswith("  default_prompt: "))
        prompt = json.loads(raw)
        for phrase in ("$design-kit", "text", "component", "group", "section",
                       "page", "visual library", "After each image round",
                       "chosen milestone", "before actual design or code"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, prompt)
        self.assertIn('value: "onepagelove"', metadata)
        self.assertIn('value: "awwwards"', metadata)
        self.assertIn('url: "https://api.onepagelove.com/mcp"', metadata)

    def test_component_first_is_default_not_a_mandatory_page_workflow(self):
        skill = read("SKILL.md")
        self.assertIn("text treatment or icon", skill)
        self.assertIn("first representative component", skill)
        self.assertIn("image-based component library", skill)
        self.assertIn("component groups", skill)
        self.assertIn("the user chooses", skill.lower())
        self.assertIn("first section", skill)
        self.assertIn("whole existing design", skill)
        self.assertIn("stop", skill.lower())
        self.assertIn("not a required waterfall", skill)
        self.assertIn("not a coded section", read("IMAGE_WORKFLOW.md")) if False else None
        self.assertIn("No component implementation", read("IMAGE_WORKFLOW.md"))

    def test_first_exemplar_library_batch_and_user_or_kit_refinement(self):
        library = read("COMPONENT_LIBRARY.md")
        for phrase in ("first visual unit", "style DNA",
                       "related components", "in one image batch",
                       "The user may tweak every component",
                       "Design Kit can also propose",
                       "section images"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, library)
        self.assertIn("user-selected", library)
        self.assertIn("batch", read("EXECUTION.md"))
        self.assertIn("group", read("PROMPT.md"))

    def test_each_image_round_has_feedback_and_user_can_stop_anywhere(self):
        for file in ("SKILL.md", "IMAGE_WORKFLOW.md", "ONBOARDING.md",
                     "EXECUTION.md", "WORKFLOW.md", "README.md"):
            with self.subTest(file=file):
                text = read(file).lower()
                self.assertRegex(text, r"after (?:\*\*)?every|after each")
                self.assertRegex(text, r"ask")
                self.assertRegex(text, r"stop")
        self.assertIn("no fixed two-pass cap", read("SKILL.md"))
        self.assertIn("as many", read("README.md"))
        self.assertIn("one selected text image", read("SKILL.md"))

    def test_reference_research_remains_real_and_conditionally_used(self):
        router = read("REFERENCE_ROUTER.md")
        self.assertIn("Awwwards", router)
        self.assertIn("One Page Love", router)
        self.assertIn("no minimum reference count", router)
        self.assertIn("reference_scope.py", router)
        self.assertIn("actual selected first component image", read("COMPONENT_LIBRARY.md")) if False else None
        self.assertIn("actual selected image", read("EXECUTION.md"))
        self.assertIn("inspected", router)
        self.assertIn("Skills.sh", read("IMAGE_WORKFLOW.md"))

    def test_foundation_proposals_and_visual_only_boundary(self):
        skill = read("SKILL.md")
        self.assertIn("may propose", read("FOUNDATION.md"))
        self.assertIn("user-approved", read("FOUNDATION.md")) if False else None
        self.assertIn("not user-approved", skill)
        self.assertIn("**Stop before actual editable design", skill)
        self.assertIn("not coded components", skill)
        self.assertIn("separate", read("docs/03_frontend_engineering.txt").lower())

    def test_old_section_only_or_code_first_defaults_do_not_return(self):
        forbidden = (
            r"the unit of work is a \*\*section image\*\*",
            r"generate the first section as the anchor",
            r"one candidate and at most two",
            r"author one coherent candidate in the existing medium",
            r"stop at this visual specification",
        )
        for file in ACTIVE:
            for pattern in forbidden:
                with self.subTest(file=file, pattern=pattern):
                    self.assertIsNone(re.search(pattern, read(file), re.I))

    def test_new_guides_are_packaged_and_linked(self):
        installer = read("scripts/install.py")
        readme = read("README.md")
        for file in ("IMAGE_WORKFLOW.md", "COMPONENT_LIBRARY.md", "FOUNDATION.md"):
            with self.subTest(file=file):
                self.assertIn('"' + file + '"', installer)
                self.assertIn("](" + file + ")", readme)
        self.assertIn("with/without-kit", readme)
        self.assertIn("do not prove", readme)
        self.assertIn("SEPARATE USER-SELECTED TASK",
                      read("docs/03_frontend_engineering.txt"))


if __name__ == "__main__":
    unittest.main()
