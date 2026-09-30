# Design Kit

A native skill for product-specific frontend design with Codex or another compatible coding agent, with optional programming guidance. Connects curated references to concrete implementation decisions and inspected results. Quality closes on observable criteria; unnecessary discovery, context and rework are reduced. No custom agent server, paid MCP, extra model, or agent team is required.

## Install once into a target project

Keep this repository as a separate checkout (or the existing `.design-kit/` checkout). From a terminal with Python 3.9+:

```sh
python /path/to/design-kit/scripts/install.py /path/to/project
```

The installer copies the skill and its canonical reference documents into `.agents/skills/design-kit/` and adds one marked pointer to the active root instruction file: non-empty `AGENTS.override.md` when present, otherwise `AGENTS.md`. It preserves unrelated instructions and existing file permissions, refuses to overwrite edited managed files, and performs no network requests, model calls, dependency installs, or application changes. Run it again to update an unmodified installation. Review local edits before updating; there is deliberately no force-overwrite option.

For a project where you both design and program, activate both entrypoints:

```sh
python /path/to/design-kit/scripts/install.py /path/to/project --with-software
```

This adds a pointer to SOFTWARE.md for programming. It does not broaden the design skill's discovery metadata to backend work. Mixed features apply engineering guidance to contracts/behavior and Design Kit to the frontend. A normal reinstall preserves this choice; `--design-only` explicitly removes the engineering pointer while preserving other project instructions. The supporting documents remain packaged but are read only for relevant work.

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

## Choose the task's input and acceptance

- **From scratch / moodboard:** ask for one product-specific direction. The agent inspects an integrated desktop/mobile sample before expanding. If you want to approve that direction first, explicitly request a stop at the sample; otherwise it continues within delegated scope.
- **Wireframe / structural composition:** state what is closed, open and illustrative. Preserve the closed structure while resolving finish and responsive behavior.
- **Final design / accepted system:** implement or extend faithfully. No new identity-discovery phase.
- **Programming:** state the observable behavior, important constraints and recovery paths. SOFTWARE.md scales the process to a local change, feature or sensitive operation.
- **Review only:** request findings; code and project records remain unchanged.

For example:

```text
$design-kit Implement this wireframe for [product/user].
Closed: hierarchy, section order and primary action. Open: typography,
spacing, image treatment and mobile composition. References: [URL/capture].
Deliver working UI, compare the important regions and verify affected states.
```

```text
Implement [capability] in this project. Success: [observable behavior].
Preserve [contracts/data/accepted UI]. Verify [important failures/recovery].
Complete the capability, inspect the diff and report actual evidence.
```

The second prompt uses the installed engineering pointer; it does not invoke `$design-kit` for backend-only work. High reasoning on GPT-6.1 Sol with Standard speed is a recommended starting point for demanding tasks, not a setting changed by the installer. See EXECUTION.md for focused escalation and context reuse.

## What lives where

- **SKILL.md:** one procedure for create/redesign, extend, refine, and review.
- **REFERENCE_ROUTER.md:** choose one eligible source for a named gap, inspect it, apply the relationship and compare the render. Preserves the curated catalog while excluding incompatible access from automatic discovery.
- **DESIGN_DIRECTION.md:** resolve an open composition through product/task, type/content, dominant asset, density and responsive behavior; skip for final designs and accepted-system repairs.
- **SOFTWARE.md:** one engineering procedure for programming; optional root activation through `--with-software`.
- **EXECUTION.md:** quality-oriented effort, context reuse, budgets and handoff; read when relevant, not every turn.
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

One primary coding agent, code-first in the existing target, real visual inspection, and no automatic full-page variant tournament. Complete necessary implementation, functional debugging, and required checks. Resolve material requirement, craft, responsive and behavior gaps against QA.md's scoped completion criteria. Batch justified repairs; stop when the criteria are met, an explicit user budget is exhausted or essential evidence/access blocks progress. There is no fixed two-round ceiling and no endless “make it perfect” loop. Repeated identical failures change the hypothesis or expose a blocker. Review-only requests skip construction and do not update code or project records.

These limits are instructions, **not a hard token/money cap**. No 8/10 score, first-pass success rate, token savings, browser availability, or production readiness is guaranteed. Package tests establish install behavior only. Validate quality on an actual project before treating this as a proven workflow.

Optional MCPs or specialist skills may supply a missing capability. Do not activate several complete design workflows for the same task, upload private captures by default, or replace the agent runtime merely to obtain a different instruction format.

Reference tools are documented options, not installed integrations. User links/files and the existing browser come first. Hosted free services with limits require the user's acceptance; paid/metered catalog services are excluded from automatic discovery. The router cannot guarantee provider availability or terms.

## Maintain and test

```sh
python -m unittest discover -s tests -v
```

Tests exercise deterministic installation behavior and static package contracts, not an LLM or browser. For a real quality comparison, keep the task, input references, starting code and model fixed; record the first handoff, regressions, human corrections and observed cost. Unmeasured quality/cost remains unknown.

GitHub Actions runs the offline suite on Linux and Windows with supported Python versions. Tests verify both entrypoint installation/update, opt-in preservation, conflict/rollback behavior and local Markdown link integrity. They do not certify visual quality or runtime activation.

Preserve source URLs and keep shared BRIEF.md blank. Add reusable examples/checks only after recurring accepted corrections justify them. See [the execution decision](docs/EXECUTION_DECISION.md) for Codex versus a custom runtime and the video analysis.

The [quality evidence record](docs/QUALITY_EVIDENCE.md) connects the September 29 update to current GPT-6 guidance and identifies which frontend/prompt principles come from earlier-model examples. It is research history, not extra default context. The full Spanish human guide is in `docs/GUIA_GENERAL.txt`; it is deliberately not installed into the active skill package.
