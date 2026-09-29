# Design Kit repository

This repository distributes reusable frontend guidance. It is not the target application and is not a custom agent runtime.

## Maintaining the kit

- Read only the affected files. Preserve the curated sources in REFERENCES.md unless changing them is explicitly requested.
- SKILL.md is the single canonical design procedure. WORKFLOW.md is a compatibility pointer, not a second workflow.
- SOFTWARE.md is the canonical programming procedure; REFERENCE_ROUTER.md and EXECUTION.md are conditional supporting guidance. Keep installed pointers aligned with those sources rather than duplicating their procedures.
- Keep BRIEF.md a blank template. Product facts, active captures, assets, accepted examples, and implementation live in target projects, not in the shared library.
- Keep TASTE.md and GUIDELINES.md general; no project's identity becomes a universal rule without approval.
- Changes to installation must pass `python -m unittest discover -s tests -v`. Document actual limits; passing package tests does not establish visual output quality.
- Kit maintenance does not authorize building a demo app, installing dependencies, consuming model credits, changing runtime settings, publishing, or modifying other repositories.
- Honor explicit user authorization for commits and other external writes. Preserve reversibility and concurrent changes; never force-push by default.

## Using the kit for frontend work

Install into the target with scripts/install.py as described in README.md, then use `$design-kit`. Read and apply SKILL.md. Resolve kit resources from the skill's directory and application resources from the target root.

Legacy users explicitly routed here from a target's AGENTS.md should follow SKILL.md instead of starting the old workflow. Preserve the target's own instructions and use its existing brief, including `.design-kit/BRIEF.md` when relevant. Merely storing this checkout beside application files does not activate its instructions for them.
