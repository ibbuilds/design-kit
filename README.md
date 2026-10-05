# Design Kit

A supervised **UI -> frontend -> QA skill**, designed primarily for the graphical interfaces of OpenAI, Anthropic and Google. It guides the current agent through product/vibe clarification, inspected references, a rendered design system, components, interface refinement and requested frontend code. No backend work, paid inspiration subscription or separate design runtime is required.

## The experience

1. Inspect the actual project and reuse its brief, base, system and accepted decisions. Detect an existing identity/system and clarify only an unresolved material change boundary; local improvements reuse its vocabulary. Retain protected anchors and update canonical sources instead of introducing a competing system.
2. Ask only missing product/experience and vibe questions, using contextual options, surprise me and free text. Expand the user's words into a detailed brief/prompt under [PROMPT.md](PROMPT.md), preserving requirements and negatives, marking proposed interpretation/unknowns, and reviewing it in the same vibe checkpoint.
3. Search **Awwwards and One Page Love** primarily by the agreed aesthetic, allowing cross-industry inspiration; business/genre terms are optional filters for a specific need. Use matching curated references/user material as fallback. Show readable evidence, explain transfer to this product and contributions, then correct the selection until accepted.
4. Reuse or develop the scoped design system: real typography, semantic tokens, spacing, geometry, assets and behavior. Show a **rendered specimen** before styled page construction; revise it until accepted.
5. Build scoped base/composite components and interfaces from that accepted system and reference map. Inspect the actual result, show it, apply feedback and preserve the stronger baseline.
6. If frontend code was requested, continue through implementation and relevant QA without asking for that same permission again. Design-only stops at design.

Every dependent design phase waits for explicit human acceptance. Existing approvals remain valid within scope; local corrections do not restart the whole workflow. A supplied file, agent self-score or elapsed time is not acceptance. An existing base enters at its actual open question.

The same flow serves a full site/app, a page, a hero/other section, a component or a local improvement. Reuse resolved phases; review only necessary system additions and the requested region. User-supplied references can be used directly or guide discovery of matching visual relationships. Section-by-section work retains prior acceptance without expanding into a whole site automatically.

For section work, find the requested pattern first and match its aesthetic there. If connected MCPs lack usable matches, continue through relevant catalog sites with ordinary browser/search, including readable public Refero evidence. Try subsequent relevant sources; if usable coverage is exhausted, explain the gap and invite user references/clarification. Missing MCP access does not disable the fallback library.

[SKILL.md](SKILL.md) is the entrypoint; [ONBOARDING.md](ONBOARDING.md) supplies phase guidance. This is **one skill with supporting resources and scripts**, not a custom model/runtime or an automatically installed marketplace plugin. Plugins are host-specific bundles; the skill is the reusable design procedure.

## Supported interfaces

| Platform | Primary interface | Adapter |
| --- | --- | --- |
| OpenAI | Codex desktop app | `codex` (also CLI/IDE) |
| Anthropic | Claude Desktop, Code tab | `claude-code` (also CLI/IDE) |
| Google | Antigravity app/IDE | `antigravity`; `gemini-cli` for Gemini CLI |

Use it from the agent's prompt/skill picker; the designer does not need to operate a terminal. Native questions, previews and annotations are preferred, with chat/readable artifacts as fallback. [HOSTS.md](HOSTS.md) explains activation, project paths and surface boundaries. Consumer web chats, cloud environments and local coding interfaces do not automatically share skill files or stdio runtimes.

Keep the current model, mode and settings. The same contract does not guarantee identical tools, compliance or visual quality across platforms.

## Setup from the interface

Give the agent access to this checkout. For installation across your projects, ask:

> Install Design Kit globally for my user in this interface. Preserve my existing skills and settings. Configure Awwwards and One Page Love globally if missing, verify actual tools and readable results, and guide any required installation or native consent step. Keep each project's brief and design decisions in that project.

For a team/project-local installation, open the real target project and ask:

> Install Design Kit into this project for the interface I am using. Preserve existing instructions and work. Configure Awwwards and One Page Love if missing, verify actual tools and readable results, then start the supervised design workflow.

The agent can perform setup with the helpers under that explicit authorization. It should report concrete conflicts or missing prerequisites, not ask again for already-authorized steps. This repository is the kit, never the target application.

For the agent or manual installation, from this checkout:

```sh
python scripts/install.py --scope user --host codex --check
python scripts/install.py --scope user --host codex
python scripts/setup_mcp.py --scope user --host codex
python scripts/setup_mcp.py --scope user --host codex --apply
```

For one project instead:

```sh
python scripts/install.py "<target-project>" --host codex --check
python scripts/install.py "<target-project>" --host codex
python scripts/setup_mcp.py "<target-project>" --host codex
python scripts/setup_mcp.py "<target-project>" --host codex --apply
```

Choose the appropriate adapter from the table. `--scope user` installs globally for this user; omit the project argument. Project scope remains the default and requires a target directory. `--user-home "<existing-profile-home>"` explicitly selects another home for user scope. Global native paths are listed in [HOSTS.md](HOSTS.md). Avoid installing the same skill globally and locally unless a project needs its own version; hosts differ in duplicate precedence.

Python 3.9+ supports skill installation and JSON MCP config; validating Codex TOML requires Python 3.11+. The installer copies the full bundle, adds a marked pointer to project instructions only in project scope, preserves unrelated content and refuses locally edited managed files. Global installation does not edit global instruction files or create a project brief. `--check` reports drift without writes (exit 1 when changes are needed); rerun installation to update an unmodified copy. Existing unmanaged resources remain intact. There is no force-overwrite option.

The MCP helper **plans by default**; `--apply` writes the explicitly selected project or user config after conflict checks and backs up an existing config. It installs no dependencies and launches no servers. The host may download/launch the documented Awwwards npm package when connecting. Inspect effective connections across scopes before applying to avoid duplicate providers; reload/trust may be required by the host. Codex metadata declares the reference MCP dependencies for native integration; it does not install Node or launch local Awwwards by itself. The skill detects missing access/prerequisites, presents the concrete setup and uses native questions/consent controls when available, otherwise chat. [PROVIDERS.md](PROVIDERS.md) documents setup and verification.

In project scope, `--with-software` optionally adds a direct pointer for requested frontend programming/QA. Ordinary updates preserve that choice; `--design-only` removes that extra pointer. These pointer options do not apply to global installation. The skill itself loads frontend implementation when requested in either scope; backend work remains excluded.

Manual installation copies every file in `scripts/install.py`'s `PACKAGE` to the selected native skill directory, with a project instruction pointer only for project scope. Copying only SKILL.md is incomplete. Legacy target briefs under `.design-kit/BRIEF.md` remain usable; [WORKFLOW.md](WORKFLOW.md) redirects to the canonical skill.

## Evidence and reusable work

[REFERENCES.md](REFERENCES.md) remains the curated fallback library. [REFERENCE_ROUTER.md](REFERENCE_ROUTER.md) scopes discovery, original-link provenance and visual inspection. The helper [scripts/reference_scope.py](scripts/reference_scope.py) plans scoped queries/checks membership; it does not rank visual quality, verify gallery outbound links or enforce browser requests.

Selected MCPs supply reference evidence, not taste by themselves. One Page Love currently documents free beta access with IP limits and possible future paid caps; Awwwards is an unofficial open-source server dependent on the public site. No unlimited/free-forever claim. Inspo and paid providers are not added automatically. A hero thumbnail is not a complete page or proof of interaction.

MCP use is scoped to open decisions: plan filters before calls, reuse schemas/results/captures, retrieve only the useful shortlist, and refresh only affected evidence. The agent chooses the provider by capability and falls back for a named gap instead of duplicating every search. PROVIDERS.md covers batching, payloads, rate limits and explicit budgets.

Keep reference relationships, exclusions and accepted revisions in the target's existing record, otherwise `.design/project.md` using relevant [BRIEF.md](BRIEF.md) fields. Preserve the canonical token format and system document, or use target DESIGN.md for intent when absent. Do not duplicate token values into competing sources. Public extracted styles are partial evidence.

Reuse the existing medium; otherwise propose an HTML/CSS specimen/preview inside the agent interface. [PENPOT.md](PENPOT.md) is conditional on user choice and actual access. No canvas app switch, Obsidian crawler or reference database is required. A future capture/index pipeline is separate scope.

[TASTE.md](TASTE.md), [DESIGN_DIRECTION.md](DESIGN_DIRECTION.md) and relevant [GUIDELINES.md](GUIDELINES.md) sections guide visible improvement. [SOFTWARE.md](SOFTWARE.md), [PRODUCT_DELIVERY.md](PRODUCT_DELIVERY.md) and relevant [QA.md](QA.md) sections cover frontend implementation, existing API integration and verification. [EXECUTION.md](EXECUTION.md) covers continuity and effort without choosing a model.

## Verification and the next real trial

```sh
python -m unittest discover -s tests -v
```

Offline tests verify installation/update safety, exported resources, provider config schemas and scoped reference queries. They do not evaluate an LLM following human checkpoints, working connections inside every GUI, aesthetic uplift or token savings. Platform paths are checked against primary documentation linked in HOSTS.md; provider limits/source behavior are linked in PROVIDERS.md.

The next useful design trial compares the **same brief, model, base, references and budget**, with and without the kit. Review actual renders for hierarchy, identity, coherence, responsive behavior and task usability; retain human choices, repair count and observable consumption. Do not claim a 9/10 result or success probability before those comparisons.

Historical research and the previously attempted mechanisms remain in [RESEARCH.md](RESEARCH.md), [workflow research](docs/WORKFLOW_RESEARCH.md) and [quality evidence](docs/QUALITY_EVIDENCE.md). They inform choices and state their limits; they are not routine build context or extra mandatory phases. English usage guides live at `docs/GENERAL_GUIDE.txt`, `docs/01_design_from_scratch.txt`, `docs/02_improve_existing_design.txt` and `docs/03_frontend_engineering.txt`.
