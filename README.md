# Design Kit

A repo-scoped skill that guides the agent you already use through design: brand/product information, curated visual/UX references, designer's foundations, base and composite components, coherent pages, and authorized implementation. It provides onboarding, missing-input questions and continuity between phases. No custom agent, server, paid MCP or extra model is required.

## Start and let your agent guide the phases

```text
$design-kit Start the design workflow for this project. Inspect what I already
provided, tell me the current phase and ask for the information or decisions
needed next. Use the curated sources for reference discovery. I will make the
design decisions unless I explicitly delegate one.
```

If no brand context exists, the agent requests a readable link, attachment or `<project>/.design/brand.md`. Next it asks whether you have references or want it to search the curated library, clarifies the intended direction and shows useful inspected candidates. You select/refine the direction, provide or develop foundations with focused help, then choose how much expansion to delegate. The agent does not assume a style from examples in this repository.

The agent reads [ONBOARDING.md](ONBOARDING.md)'s shared contract and current phase, then only the routes needed for that operation. The checkpoint identifies the reviewed revision/capture and your decision, separately from pending changes; a mutable path alone is not approval. The default project record is `.design/project.md`; existing records remain valid. Reference review uses eight clear candidates by default and captures what you want to take from each; a shortage is discussed, never hidden. Suggested input paths are `.design/brand.md`, `.design/references/`, `.design/foundations.md`, `.design/base/` and `.design/assets/`. These are relative to your project, never the installed skill. They are created only when needed. Attachments, existing files and accessible links are equally valid; Notion is optional and requires available authorized access.

You can enter any phase directly: "references only", "help choose typography", "extend my accepted system" or "implement this final design". The agent skips resolved phases, asks only for material missing inputs and preserves prior decisions. Every phase and meaningful design batch is supervised: the agent shows the output and waits for your acceptance/correction before dependent work. A broad build request does not waive that. Previously supplied explicit approval is reused within its scope. A brief and palette need representative composition/flow evidence before reliable expansion.

The catalog is the discovery allowlist. [REFERENCE_ROUTER.md](REFERENCE_ROUTER.md) describes vibe interpretation, scoped search, visual inspection, shortlists and provenance. [scripts/reference_scope.py](scripts/reference_scope.py) generates optional catalog-scoped queries and checks candidate source membership without network/model calls. Queries with only `--source-url` generate only those human-added sources; adding `--section` combines the chosen scopes. It is not a browser firewall or visual ranking engine. External originals are inspected only through verified curated links or user-supplied material. Preserve the curated catalog; do not automatically broaden to the web.

[BRIEF.md](BRIEF.md) is a blank handoff you can copy into Notion or an existing project record. The agent can capture your answers there; you do not have to complete the entire template before starting. Choose or reuse the design medium before the first visual system output. The designer can work in their current design medium. If an HTML/CSS prototype is chosen, reuse its code through integration rather than rebuilding it from screenshots.

## Use with your chosen agent

The workflow is Markdown instructions and local resources. An agent with repo/file access and a browser or search capability can follow it. Use the host's supported skill location and invocation mechanism, or tell it to read `/actual/path/to/design-kit/SKILL.md` and follow its links. A folder being present does not make every host discover it automatically. `$design-kit` below is Codex's invocation syntax; other hosts may use a different selector or explicit file request. `agents/openai.yaml` is optional Codex UI metadata, not a runtime requirement. No universal compatibility claim replaces checking that the actual host loaded the entrypoint and can read the project inputs.

## Editable design in Penpot

Penpot is the preferred canvas candidate for this workflow. [PENPOT.md](PENPOT.md) documents the official MCP route, actual setup requirements, supervised writes and validation. Penpot's MCP is free/open; the existing AI subscription still supplies the model. Remote setup needs account availability, a private MCP key and an active connected design tab. Local setup needs its server/plugin. The kit does not install either or claim a live connection. Reference discovery remains separate and can use the existing browser without an extra MCP.

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

`--check` performs no writes and reports whether installation/update is needed. This checks files, including a newly added root override, not model activation or visual capability. It does not inspect user-global instructions, custom fallbacks, or nested overrides; verify the active context from the actual working directory. If Codex does not list the skill after installation, restart it and select `$design-kit` explicitly. Do not install a second copy under the same name. The target can be a design workspace before application code exists; reference-only work does not require a running app.

Run Codex **inside the target project**, not this library. A short task is enough to start:

```text
$design-kit Start the supervised design workflow for [product and audience].
Primary outcome: [job/action]. Use [existing brief/files] when available.
Ask for missing phase inputs, develop my supplied base, present each phase's
output and wait for my review before dependent work.
```

When you ask it to discover references, the agent selects and inspects relevant examples from REFERENCES.md. You do not need to annotate the entire library first; you review the candidates and say what to take from each useful example. Existing project references and accepted work come first. A new direction needs concrete visual evidence; a small refinement need not research again.

## Choose the task's input and acceptance

- **From scratch / moodboard:** start the guided phases. Confirm the brand summary and intended direction, review eight references, supply foundations, then review system/component/page batches. The agent waits before dependent expansion.
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

The second prompt uses the installed engineering pointer; it does not invoke `$design-kit` for backend-only work. Medium + Standard on GPT-6.1 Sol is a practical proposal for bounded work; High addresses named consequential ambiguity or difficult diagnosis. The user's chosen settings win, and the installer changes none of them. See EXECUTION.md for escalation and total cost through an accepted result.

## What lives where

- **SKILL.md:** the canonical entrypoint for supervised design, extend, refine and review.
- **ONBOARDING.md:** default phase inputs, outputs, concrete file/link questions, human checkpoints and resume behavior.
- **PENPOT.md:** conditional official canvas/MCP connection, target verification, supervised batches and handoff; no bundled runtime or automatic installation.
- **REFERENCE_ROUTER.md:** interpret a vibe, search inside eligible curated sources, inspect candidate evidence, report fit/mismatches and preserve designer selection; implementation follows only the requested scope.
- **scripts/reference_scope.py:** dependency-free catalog search planning and deterministic source-membership checks; no network, ranking model or browser enforcement.
- **DESIGN_DIRECTION.md:** resolve an open composition through product/task, type/content, dominant asset, density and responsive behavior; skip for final designs and accepted-system repairs.
- **SOFTWARE.md:** one engineering procedure for programming; optional root activation through `--with-software`.
- **PRODUCT_DELIVERY.md:** conditional requirements, evidence and release guidance for substantial capabilities or readiness work.
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

Your chosen agent, supervised design-first phases, real visual inspection and no automatic full-page variant tournament. The designer supplies the base; the agent develops it and presents each meaningful review batch before advancing. Code starts when requested after accepted design. Complete necessary implementation, functional debugging, and required checks. Resolve material requirement, craft, responsive and behavior gaps against QA.md's scoped completion criteria. Batch justified repairs; stop when the criteria are met, an explicit user budget is exhausted or essential evidence/access blocks progress. There is no fixed two-round ceiling and no endless “make it perfect” loop. Repeated identical failures change the hypothesis or expose a blocker. Review-only requests skip construction and do not update code or project records.

These limits are instructions, **not a hard token/money cap**. No 8/10 score, first-pass success rate, token savings, browser availability, or production readiness is guaranteed. Package tests establish install behavior only. Validate quality on an actual project before treating this as a proven workflow.

Optional MCPs or specialist skills may supply a missing capability. Do not activate several complete design workflows for the same task, upload private captures by default, or replace the agent runtime merely to obtain a different instruction format.

Reference tools are documented options, not installed integrations. User links/files and the existing browser come first. Hosted free services with limits require the user's acceptance; paid/metered catalog services are excluded from automatic discovery. The router cannot guarantee provider availability or terms.

## Maintain and test

```sh
python -m unittest discover -s tests -v
```

Tests exercise deterministic installation, source-scope regressions and static package contracts, not an LLM or browser. Both test files ship in the installed bundle; the same offline suite can run there. For a real quality comparison, keep the task, input references, starting code and model fixed; record the first handoff, regressions, human corrections and observed cost. Unmeasured quality/cost remains unknown.

GitHub Actions runs the offline suite on Linux and Windows with supported Python versions. Tests verify both entrypoint installation/update, opt-in preservation, conflict/rollback behavior and local Markdown link integrity. They do not certify visual quality or runtime activation.

Preserve source URLs and keep shared BRIEF.md blank. Add reusable examples/checks only after recurring accepted corrections justify them. See [the execution decision](docs/EXECUTION_DECISION.md) for Codex versus a custom runtime and the video analysis.

The [quality evidence record](docs/QUALITY_EVIDENCE.md) connects the September 29 update to current GPT-6 guidance and identifies which frontend/prompt principles come from earlier-model examples. It is research history, not extra default context.

## Spanish manuals for learning and applying the workflows

These are standalone human learning manuals. Each begins with the user's decisions and a guided pass, explains the detailed procedure, provides examples and prompts, and includes the setup, efficiency guidance and relevant research sources. They are not installed into the active skill package or new procedures to inject into every turn.

- [Design from scratch](https://github.com/ibbuilds/design-kit/blob/main/docs/01_diseno_desde_cero.txt): use guided onboarding, select direction and develop foundations before delegated expansion.
- [Iterate on your design base](https://github.com/ibbuilds/design-kit/blob/main/docs/02_diseno_sobre_tu_base.txt): enter with existing work, resolve only missing inputs and preserve authorship.
- [Professional programming](https://github.com/ibbuilds/design-kit/blob/main/docs/03_programacion_profesional.txt): define observable behavior, judge contracts and evidence, and complete appropriate verification and recovery.

The prior combined `docs/GUIA_GENERAL.txt` remains a consolidated reference/catalog and research record. The three manuals are the current human-facing workflow guides; SKILL.md and SOFTWARE.md remain the canonical agent procedures.

The [broader workflow comparison](docs/WORKFLOW_RESEARCH.md) documents alternatives from Codex/Figma, Spec Kit, Kiro, Anthropic, Cursor and Google, the supplied videos and the failed prior runbook, including costs and limits that prevent blindly adopting heavier processes. The Spanish guide presents three workflows: design from scratch, iteration on the user's design base, and programming. For substantial features, [PRODUCT_DELIVERY.md](PRODUCT_DELIVERY.md) connects requirements to evidence, challenges the working result and records applicable release readiness. It is loaded conditionally; a local refinement stays local. The research record includes a real-task comparison protocol, but no measured improvement in generated product quality is claimed.
