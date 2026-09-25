# Design Kit

A native skill for product-specific frontend design with Codex or another compatible coding agent. Reuses the curated reference library, keeps creative decisions close to real implementation, and bounds refinement. No custom agent server, paid MCP, extra model, or agent team is required.

## Install once into a target project

Keep this repository as a separate checkout (or the existing `.design-kit/` checkout). From a terminal with Python 3.9+:

```sh
python /path/to/design-kit/scripts/install.py /path/to/project
```

The installer copies the skill and its canonical reference documents into `.agents/skills/design-kit/` and adds one marked pointer to the active root instruction file: non-empty `AGENTS.override.md` when present, otherwise `AGENTS.md`. It preserves unrelated instructions and existing file permissions, refuses to overwrite edited managed files, and performs no network requests, model calls, dependency installs, or application changes. Run it again to update an unmodified installation. Review local edits before updating; there is deliberately no force-overwrite option.

```sh
python /path/to/design-kit/scripts/install.py /path/to/project --check
```

`--check` performs no writes and reports whether installation/update is needed. This checks files, including a newly added root override, not model activation or visual capability. It does not inspect user-global instructions, custom fallbacks, or nested overrides; verify the active context from the actual working directory. If Codex does not list the skill after installation, restart it and select `$design-kit` explicitly. Do not install a second copy under the same name.

Run Codex **inside the target project**, not this library. A short task is enough to start:

```text
$design-kit Build the landing page for [product and audience].
Primary outcome: [job/action]. Preserve [facts and constraints].
Choose suitable visual references from the existing library and make
one coherent direction. Complete and inspect the result before handoff.
```

The agent selects and inspects relevant examples from REFERENCES.md itself. You do not need to annotate the entire library first. Existing project references and accepted work win over generic examples. A new direction needs concrete visual evidence; a small refinement need not research again.

## What lives where

- **SKILL.md:** one procedure for create/redesign, extend, refine, and review.
- **TASTE.md / GUIDELINES.md / QA.md:** craft and work-specific checks, read selectively.
- **REFERENCES.md:** the original curated sources, unchanged by this migration.
- **BRIEF.md:** blank template; actual facts, selected captures, decisions and code stay in the target. Reuse existing records instead of multiplying documents.
- **agents/openai.yaml:** Codex discovery metadata with implicit invocation enabled.
- **AGENTS.md:** maintenance contract and compatibility entry for this library.
- **WORKFLOW.md:** compatibility pointer to SKILL.md.
- **RESEARCH.md / docs/:** history and rationale, not routine build context.

The installed package is generated from these canonical source files. Do not maintain another copy of the workflow manually.

## Migrating the old layout

The installer removes only the exact historical three-line `.design-kit/AGENTS.md` activation snippet documented by the previous README, then inserts the native pointer. Other instructions and any `.design-kit/BRIEF.md` are untouched. If you wrote a different legacy pointer, review it manually to avoid two entry paths. The skill can reuse the old project brief; no source-library reconstruction is required.

Manual installation is also possible: copy the files listed in `scripts/install.py` into `.agents/skills/design-kit/`, and point the target's active root instruction file to that SKILL.md. Copying only SKILL.md without its reference documents is not a complete installation. Symlinked skill folders are supported by Codex, but this installer deliberately writes ordinary files for portability.

## Execution defaults and limits

One primary coding agent, code-first in the existing target, real visual inspection, and no automatic full-page variant tournament. Complete necessary implementation, functional debugging, and required checks. Discretionary visual refinement has a default ceiling of two edit-and-inspect rounds for the whole task, including early-sample polish, followed by final confirmation. This is not a two-code-fix limit. User-set overall budgets override it; repeated identical failures stop that attempt. Review-only requests skip construction and do not update code or project records.

These limits are instructions, **not a hard token/money cap**. No 8/10 score, first-pass success rate, token savings, browser availability, or production readiness is guaranteed. Package tests establish install behavior only. Validate quality on an actual project before treating this as a proven workflow.

Optional MCPs or specialist skills may supply a missing capability. Do not activate several complete design workflows for the same task, upload private captures by default, or replace the agent runtime merely to obtain a different instruction format.

## Maintain and test

```sh
python -m unittest discover -s tests -v
```

Tests exercise deterministic installation behavior and static package contracts, not an LLM or browser. For a real quality comparison, keep the task, input references, starting code and model fixed; record the first handoff, regressions, human corrections and observed cost. Unmeasured quality/cost remains unknown.

Preserve source URLs and keep shared BRIEF.md blank. Add reusable examples/checks only after recurring accepted corrections justify them. See [the execution decision](docs/EXECUTION_DECISION.md) for Codex versus a custom runtime and the video analysis.
