# Design Kit repository

This repository distributes reusable UI/frontend guidance. It is not the target application or a custom agent runtime.

## Maintaining the kit

- Read affected files. Preserve the curated REFERENCES.md and blank BRIEF.md unless changing them is explicitly requested. Product identity, captures and accepted code belong in target projects.
- Write authored documentation, instructions, prompts and code in English. Preserve original source names, URLs and user evidence.
- SKILL.md is the canonical artifact-first procedure. WORKFLOW.md is a compatibility pointer. ONBOARDING.md resolves delegation and explicit human checkpoints, not a mandatory phase itinerary. Keep active guides consistent with that boundary.
- CRAFT.md, TASTE.md and GUIDELINES.md provide selective visual guidance. SOFTWARE.md owns frontend implementation/QA; backend remains outside scope. REFERENCE_ROUTER.md and EXECUTION.md are conditional support.
- HOSTS.md and PROVIDERS.md retain platform/access/setup details. Preserve installed integrations and compatibility helpers; do not require new setup for ordinary design work.
- Keep changes reversible and preserve concurrent work. External writes need authorization; never force-push or merge by default. Kit maintenance does not authorize application changes, paid services, new dependencies, model-credit experiments or runtime-setting changes.
- Run `python -m unittest discover -s tests -v` for package changes. Keep installer/configuration safety tests intact. Instruction lint and passing package tests do not establish model compliance, visual uplift or savings.
- Maintainer rationale and comparison criteria for the artifact-first revision are in docs/ARTIFACT_FIRST_REVIEW.md. It is not routine model context or an installed design prerequisite. Historical research records prior decisions, not the current operating contract.

## Using the kit

Install into the actual target using scripts/install.py and follow SKILL.md. Resolve skill guidance from the installed kit and application paths from the target. Reuse existing target instructions and briefs, including legacy `.design-kit/BRIEF.md`. Do not run a product-design workflow while maintaining this repository.
