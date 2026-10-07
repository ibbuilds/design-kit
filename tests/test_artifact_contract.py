"""Instruction-structure regression checks, not model or aesthetic evaluations.

These tests deliberately do not call a model, install tools, or infer quality from
word counts. The size bound is a maintenance guard against entrypoint growth.
The existing installation/configuration tests remain the package safety checks.
"""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = (
    "SKILL.md", "ONBOARDING.md", "DESIGN_DIRECTION.md", "REFERENCE_ROUTER.md",
    "EXECUTION.md", "SOFTWARE.md", "WORKFLOW.md", "README.md",
    "docs/GENERAL_GUIDE.txt", "docs/01_design_from_scratch.txt",
    "docs/02_improve_existing_design.txt", "docs/03_frontend_engineering.txt",
)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


class ArtifactContractTests(unittest.TestCase):
    def test_entrypoint_has_valid_scoped_metadata_and_a_size_guard(self):
        text = read("SKILL.md")
        self.assertTrue(text.startswith("---\nname: design-kit\n"))
        header = text.split("---", 2)[1]
        raw = next(line.partition(": ")[2] for line in header.splitlines()
                   if line.startswith("description: "))
        description = json.loads(raw)
        self.assertLessEqual(len(description), 240)
        self.assertIn("not backend", description)
        self.assertLessEqual(len(text.split()), 1400)

    def test_default_prompt_requests_a_candidate_not_a_guided_itinerary(self):
        metadata = read("agents/openai.yaml")
        raw = next(line.partition(": ")[2] for line in metadata.splitlines()
                   if line.startswith("  default_prompt: "))
        prompt = json.loads(raw)
        self.assertIn("$design-kit", prompt)
        self.assertIn("inspected candidate", prompt)
        self.assertIn("budget", prompt)
        self.assertNotIn("guide me through", prompt)
        self.assertIn('value: "onepagelove"', metadata)
        self.assertIn('value: "awwwards"', metadata)

    def test_active_guides_do_not_restore_known_research_or_waterfall_gates(self):
        forbidden = (
            r"curate\s+\*{0,2}4[–-]8",
            r"if fewer than four",
            r"wait before searching under a proposed vibe",
            r"system specimen before styled page construction",
            r"simulator loop until perfect",
        )
        for relative in ACTIVE:
            for pattern in forbidden:
                with self.subTest(file=relative, pattern=pattern):
                    self.assertIsNone(re.search(pattern, read(relative), re.I))

    def test_scope_and_truthfulness_protections_remain_explicit(self):
        skill = read("SKILL.md")
        for phrase in ("Review-only edits neither code nor project records",
                       "protected identity", "human edits", "paid access",
                       "No numerical self-score", "Never invent visual inspection"):
            with self.subTest(protection=phrase):
                self.assertIn(phrase, skill)
        self.assertIn("explicit user checkpoints", read("SOFTWARE.md"))
        self.assertIn("expressly rejected diagnosis", read("ONBOARDING.md"))

    def test_visual_contribution_is_not_replaced_by_technical_consistency(self):
        direction = read("DESIGN_DIRECTION.md")
        for phrase in ("expected visible difference", "quality anchor",
                       "A checklist pass is not visual uplift",
                       "Judge the result, not the explanation"):
            with self.subTest(criterion=phrase):
                self.assertIn(phrase, direction)
        self.assertIn("Inspect the actual render", read("SKILL.md"))
        self.assertIn("contrasting consumer", read("SKILL.md"))

    def test_budget_and_non_improvement_stop_are_shared(self):
        skill = read("SKILL.md")
        execution = read("EXECUTION.md")
        self.assertIn("at most two grouped visual refinement passes", skill)
        self.assertIn("does not reset it", skill)
        self.assertIn("User-specified budgets", execution)
        self.assertIn("no material improvement", execution)
        self.assertIn("report incomplete work and stop", read("SOFTWARE.md"))

    def test_optional_evidence_does_not_erase_required_source_fidelity(self):
        router = read("REFERENCE_ROUTER.md")
        self.assertIn("no minimum reference count", router)
        self.assertIn("one targeted discovery query", router)
        self.assertIn("fidelity to an inaccessible source", router)
        self.assertIn("do not claim alignment", router)
        self.assertIn("No automatic paid fallback", router)

    def test_no_claim_that_package_validation_proves_quality(self):
        for relative in ("README.md", "docs/ARTIFACT_FIRST_REVIEW.md"):
            with self.subTest(file=relative):
                text = read(relative)
                self.assertIn("with/without-kit", text)
                self.assertIn("not", text)
        self.assertIn("not a demonstrated visual-quality boost", read("README.md"))


if __name__ == "__main__":
    unittest.main()
