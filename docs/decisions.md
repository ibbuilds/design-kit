# Architecture decisions

## 0.3.4 consolidation — 2026-09-05

The primary-session rule is unchanged and model-agnostic. The effective runtime now
centers reference mechanisms, essential assets, an internal art-direction lock,
primary-surface resolution and bounded visual correction. Canon/archetypes stay on
demand. Core/process/quality duplication and the historical specialist roster were
merged into shorter guidance; bridge configuration is unchanged.

Library ingestion accepts valid approved-source captures independently of today's
task relevance. Existing receipts serve as the index with optional reusable metadata,
paged search and cross-session image deduplication. No new store or automatic cleanup.
Packages ship manifest, skills and README only; source history, tests and evaluations
remain in this repository. The decisions below are the preserved development record.

Current official packaging and skill pages were opened on 2026-09-05:
https://developers.openai.com/plugins/build/plugins and
https://developers.openai.com/plugins/build/skills.
The installed creator/CLI still supports cachebuster + plugin add; use that verified
local installation path. No hooks were introduced; the documented validator discrepancy
does not affect this package.

Verified 2026-09-04. Official links and scoped UX authority are in the skill's
[source registry](../skills/design-director/references/sources.json).

1. **Native package, one primary skill.** Root `.codex-plugin/plugin.json` points
   to `./skills/`; `design-director` routes to normal Markdown. No custom agent
   framework, parallel agents, MCP server, embeddings, vector store or indexer.
   There is no demonstrated retrieval failure justifying them.
2. **Transport-neutral Figma access.** Reliable read, write, and current-render access
   is required; one hosted MCP is not. The separately installed, pinned local Desktop
   Plugin API bridge is primary after a live smoke test. Official Figma remains an
   optional fallback. `agents/openai.yaml` declares no mandatory MCP dependency because
   the local bridge is user-configured and must never be silently installed. No bridge
   source, credentials, connector IDs, or duplicate connection are bundled.
3. **Technical authority with explicit conflicts.** Current official docs lead,
   maintained source/runtime clarify disagreements. Official docs permit `hooks`
   but bundled plugin validator rejects it: hooks are unused, so omit them without
   weakening validation. Figma write limitations conflict with current image tools;
   inspect actual schema and test before claiming support. Current official
   Figma screen/library skills include codebase-oriented and large-library steps;
   user-authorized design-only scope prevails. Preserve API safety and native
   creation, record code mapping as inapplicable when no codebase is supplied, and
   avoid expanding a small test into a 20–100-call library build.
4. **Original scoped canon.** Distill principles, not manuals. Each pattern records
   use/non-use, alternatives, exceptions, accessibility, source scope/date. WCAG
   is normative for its conformance target; APG is informative. GOV one-question
   journeys and NN/g expert density differ by task. Apple point defaults/minima
   differ from WCAG CSS-pixel criteria. Baymard stays commerce-only. Fluent's
   older WCAG 2.1 baseline does not lower the 2.2 evaluation target.
5. **Single-agent ownership; specialists are optional in-session guidance.** See
   [comparison](research.md). The active primary Codex session and its selected model
   and reasoning configuration own reference interpretation, IA, art direction, Figma
   execution, visual critique, responsive work and final verification. Do not route
   those responsibilities through subagents, separate tasks, nested CLI sessions or
   custom agents. No upstream runtime or corpus is vendored. A compatible specialist
   may inform one bounded question inside the primary session; conflicting or
   delegation-only modes are not invoked.
6. **Retained references, no repository pollution.** User data location holds
   simple per-session files/receipts, not a custom memory service. Initial brief's
   automatic cleanup was superseded by explicit user-controlled retention. Completion,
   approval, uninstall and conversation end never clear references. Reuse first.
   Cleanup requires a real user request, inspected plan and digest; preserve foreign,
   modified and linked files. The helper handles local provenance/storage; browser
   tools and agent judgment handle lawful narrow acquisition and visual saturation.
7. **Request-driven design intelligence.** No plugin-owned process, stage assignment,
   compulsory brief/research/divergence/critique/gates or design-complete state.
   Preserve useful methods as conditional reasoning; work from current authorized
   Figma state and preserve human edits. Create no unrequested process artifacts.
   The named test draft is development authorization only, never runtime guidance.
8. **Verification has separate layers.** Schema/link checks, deterministic lifecycle
   tests, model workflow evaluations, live gallery evidence and actual Figma writes
   answer different questions. None can certify elite quality or human acceptance
   alone. Preserve failing cases and report unsupported behavior explicitly.

9. **Configurable source authority.** Explicit instructions and task references lead;
   user preferences replace built-in pools. Absent task references permits relevant
   default research; insufficient supplied references requires one supplementation
   choice. Exclusions win; no mandatory research and no bundled images. A read-only
   JSON resolver avoids silently merging replacements or falling back on malformed
   preferences. This is a plugin convention, not an invented Codex config feature.
10. **Optional A1 MCP.** Official A1/Codex documentation verified 2026-09-04 supports
    `https://www.a1.gallery/api/mcp` with HTTP/OAuth. Connect separately only on explicit
    request, not through a required dependency or bundled automatic connection.
    Runtime schemas/health determine availability; browser research remains viable.
    A1 metadata/measurements are evidence, not taste authority. Exclusive source
    restrictions prohibit broad corpus search even if results would be filtered later.
    See [integration contract](../skills/design-director/references/a1.md).

Versioning: 0.2.0 is the first working release after the 0.1.0 scaffold. Use semantic
versioning: fixes/source clarifications patch; compatible workflows minor; breaking
activation, storage or packaging contracts major (pre-1.0 minor may break with a
migration note). Use creator cachebuster helpers for local reinstall, not arbitrary
version bumps. Review upstream changes deliberately; do not auto-ingest new rules.
No automatic reference migration or deletion. Publish only completed, verified
work under the user's batching instructions; current work remains local.

11. **Adequacy before craft.** For broad work, infer the smallest complete artifact
    or connected set that satisfies the exact request. A compact general framework
    routes to six optional archetype lenses. This fixes shallow hero/index output
    without converting archetypes into required page sections or a workflow.
12. **Progressive craft depth.** Typography, composition, rhythm, art direction, and
    interaction/motion have separate on-demand modules. Core skill routing stays
    concise; no module establishes a universal aesthetic or loads automatically.
13. **Reference roles.** Curated references must cover specific experience, IA,
    composition, type, art-direction, interaction, or density questions. Connected
    experience claims require actual flow/page evidence; a first viewport is scoped
    to the decisions it visibly demonstrates.
14. **Current-state visual evidence.** A meaningful Figma write invalidates prior
    renders for verification of the changed target. Current geometry and pixels must
    refer to the same file/node/state; unavailable rendering blocks the claim rather
    than permitting stale substitution.
15. **Representative quality is the primary acceptance evidence.** Deterministic
    tests cover packaging, links, lifecycle safety, and obvious routing. Six live
    benchmark families test adequate artifacts and visual quality when explicitly
    authorized. Prompt-policy probes no longer stand in for designed outcomes.
