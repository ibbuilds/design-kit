# Design Kit

[![Validate kit](https://github.com/ibbuilds/design-kit/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/ibbuilds/design-kit/actions/workflows/validate.yml)

[Setup](#setup-from-the-interface) · [Supported platforms](HOSTS.md) · [Reference access](PROVIDERS.md) · [General guide](docs/GENERAL_GUIDE.txt)

A UI/frontend skill centered on **one visible improvement at a time**: inspect the relevant target, author a coherent candidate, compare its actual render, refine within a budget, and preserve the code that succeeds. It uses the current agent and existing tools. No additional paid service, custom runtime, reference database or required second model.

This revision is a workflow proposal, not a demonstrated visual-quality boost. Package tests do not establish aesthetics, model compliance or token savings.

## Use it

In the real project, ask:

> Use $design-kit to improve this UI. Preserve the behavior and treatments I have already accepted. Own the remaining visual decisions. Deliver one inspected candidate with at most two grouped visual refinement passes. Use our existing references and tools only for concrete gaps; do not install anything.

Name the target and product goal when not already clear. A finished Figma file, wireframe, exact token system or exhaustive defect list is not required. The agent must resolve the open design, not return that work to you.

The default is **artifact-first**, not a sequence of approvals for an expanded prompt, reference board, token sheet and component specimen. Existing explicit user checkpoints remain binding; ask for guided/supervised work when that is useful. A broad new direction is reviewed on a representative candidate before new shared choices propagate across the application. Authorized consistency repairs can update their shared owner and agreed consumers without per-component permission.

[SKILL.md](SKILL.md) owns the procedure. [ONBOARDING.md](ONBOARDING.md) handles missing inputs and review boundaries. [WORKFLOW.md](WORKFLOW.md) is only a compatibility pointer.

## What should change the output

The agent identifies a concrete visual gap/opportunity and a coherent intervention, rather than merely auditing tokens. Craft complaints start with applied typography/color, effective spacing, control families and assets; they do not automatically become navigation redesigns. Composition work examines attention order, proportion, enclosure and density.

Affected foundations are resolved inside a real composition. The candidate is compared both with its baseline and a relevant accepted example/reference where available. A technically valid or less inconsistent result is not automatically good enough. Shared changes are verified in consumers, not only isolated tiles. Accepted implementation is reused rather than recreated from aesthetic prose.

[TASTE.md](TASTE.md), [DESIGN_DIRECTION.md](DESIGN_DIRECTION.md), affected [CRAFT.md](CRAFT.md) sections and relevant [GUIDELINES.md](GUIDELINES.md) sections remain available. They are selective resources, not a stack to load before every edit. [SOFTWARE.md](SOFTWARE.md), [PRODUCT_DELIVERY.md](PRODUCT_DELIVERY.md) and relevant [QA.md](QA.md) sections cover requested frontend integration and checks.

## Budget and evidence

Default for one bounded unit: one candidate and at most two grouped visual refinement passes. A pass groups consequential fixes; phases, components and context handoffs do not reset it. Stop repeating a hypothesis when it produces no material gain. Preserve the stronger version and report unresolved gaps. User budgets override defaults; necessary verification is not waived when the budget is exhausted.

There is no minimum reference count. Reuse supplied/accepted evidence. Default discovery is one targeted query and one narrower query or relevant fallback when needed; inspecting selected results remains scoped. These are proposed spending guardrails, not optimal counts proved by research. Explicit user research requests take precedence. [EXECUTION.md](EXECUTION.md) and [REFERENCE_ROUTER.md](REFERENCE_ROUTER.md) give details.

Keep the two selected integrations, Awwwards and One Page Love, where already configured. Use whichever actually fits the decision; do not call both or repair working setup by routine. The curated [REFERENCES.md](REFERENCES.md) catalog is unchanged. The [reference helper](scripts/reference_scope.py) plans scopes/checks membership, not visual quality or source provenance. Missing optional inspiration permits an honest original proposal when authorized; missing required fidelity evidence does not permit a claimed match.

Provider access is conditional on current availability and limits. Free provider access does not make model/image usage free. Do not add paid providers, registration, uploads or dependencies because discovery failed. [PROVIDERS.md](PROVIDERS.md) is for actual access and authorized setup problems, not a mandatory startup step.

## Supported interfaces

The existing adapters and native paths are retained:

| Platform | Interface | Adapter |
| --- | --- | --- |
| OpenAI | Codex desktop app, CLI/IDE | `codex` |
| Anthropic | Claude Desktop Code tab, Claude Code CLI/IDE | `claude-code` |
| Google | Antigravity app/IDE; Gemini CLI | `antigravity`; `gemini-cli` |

[HOSTS.md](HOSTS.md) covers the existing integration boundaries. Keep the current model/settings; different hosts do not guarantee identical tool access or output. Native questions/previews are useful when available; readable chat artifacts are the fallback. [PENPOT.md](PENPOT.md) applies only to explicitly chosen, accessible Penpot. No automatic app switch.

## Setup from the interface

Use the current installation first. To install/update, give the agent access to this checkout and ask:

> Install or update Design Kit for this interface using its existing installer. Preserve my instructions, local changes, selected model and working MCP connections. Do not configure additional tools. Use the artifact-first procedure in the actual target project.

Specify global/user or project scope when installation is needed; reuse an already-known scope. From the checkout, the existing installer supports:

```sh
# One project; --check reports drift without changing files.
python scripts/install.py "<target-project>" --host codex --check
python scripts/install.py "<target-project>" --host codex

# Or global installation for this user; no project argument.
python scripts/install.py --scope user --host codex --check
python scripts/install.py --scope user --host codex
```

Choose the existing host adapter from the table. `--user-home "<existing-profile-home>"` selects another profile for user scope. Avoid duplicate global/project copies unless intentionally needed. Updating the checkout does not automatically update copied installations; run the existing installer against the selected target/scope. Do not bypass a locally edited-file conflict.

The installer copies every `PACKAGE` resource, preserves unrelated files, refuses unmanaged/local-edit overwrites and writes a marked project instruction pointer only in project scope. Global installation does not modify global instruction files or create project facts. `--check` exits 1 when drift exists. `--with-software` adds the existing direct frontend pointer for project scope; ordinary updates preserve that choice and `--design-only` removes only that extra pointer. Do not copy SKILL.md alone.

MCP configuration remains separate and requires actual authorization. The existing helper plans by default; `--apply` writes the selected config with its conflict/backup protections. It does not itself install dependencies or launch servers. Provider metadata declarations are retained for the user's existing integrations; they are not a claim that every host skips its own setup prompts. The design assignment does not require discovery/setup when relevant tools and evidence already work.

Preserve the documented One Page Love decimal-priority compatibility path when genuinely needed; see [compatibility details](PROVIDERS.md#codex-decimal-priority-compatibility). Do not introduce it into an unaffected working connection by routine. Installation/provider scripts and supported paths are not changed by this revision.

## Verification and honest status

```sh
python -m unittest discover -s tests -v
```

Existing tests cover installation/update safety, exported resource links, provider configuration and scoped reference queries. Added instruction lint catches known routing regressions; it does not exercise an AI model. A green suite is not a beauty test.

Use one necessary real product task before investing in broader evaluation. Record model/settings, base/content, reference access, task budget, actual renders, human intervention and observable total consumption including preparation and repairs. Mark unknown consumption unknown. A baseline-to-candidate gain is not proof the kit caused it: a matched with/without-kit comparison is needed for that inference. One pair remains preliminary, not reproducibility.

The maintainer-only `docs/ARTIFACT_FIRST_REVIEW.md` records this revision's recent primary sources and limits; it is not installed or loaded for design tasks. Historical [research](RESEARCH.md), [workflow research](docs/WORKFLOW_RESEARCH.md), [quality evidence](docs/QUALITY_EVIDENCE.md) and [evaluation scenarios](docs/WORKFLOW_EVALUATION.md) preserve prior decisions. Their older supervised/default-count policies do not override SKILL.md. No model comparison or visual uplift is implied by their existence.

Keep accepted code/assets/captures and relevant source relationships in the target's existing record, otherwise `.design/project.md` using [BRIEF.md](BRIEF.md). Do not duplicate token values or add a transcript archive. Design-only, review-only, backend, private uploads and publication retain their explicit scope boundaries.
