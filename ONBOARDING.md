# Supervised design onboarding

Read the common contract, continuity/checkpoint and current phase. Read subsequent phases only when entering them. [SKILL.md](SKILL.md) remains the entrypoint; this is guidance for the current agent, not a runtime.

## The phase contract

**Inspect -> identify phase -> obtain missing input -> produce agreed output -> agent inspects/repairs -> show artifact -> wait for human review -> record acceptance/corrections.** Start dependent work only after acceptance and authorization of its scope. Corrections keep the batch open. A supplied file, silence, elapsed time or the agent's recommendation is not acceptance.

Reuse explicit approvals already supplied, within their scope; a later phase can be entered directly. "Make the design" does not waive checkpoints; an explicit user override can. An initial frontend build request covers implementation after the design checkpoints; do not ask twice for that scope. Complete routine corrections within the approved batch without per-edit permission. Pending feedback permits only independent work already authorized inside this phase. Single-phase requests stay there; review-only does not edit records/designs. Backend work is outside this kit. Examples are not the user's preferences.

## Default project structure and continuity

Use the **target project's** authoritative record, otherwise `.design/project.md` with useful fields from blank [BRIEF.md](BRIEF.md). Create only what the task needs; installation creates no project brief. Sources can remain where the user supplied them:

| Input | Optional target path | Alternatives |
| --- | --- | --- |
| Brand/product | `.design/brand.md` | TXT/MD/PDF, conversation, accessible URL/authorized Notion page |
| References | `.design/references/` | Links, captures, moodboard/design file |
| Foundations | `.design/foundations.md` | Existing tokens/components or design file |
| Existing design | `.design/base/` | Canvas, readable capture, prototype/code |
| Assets | `.design/assets/` | Existing directories or authorized material |

Tell the user the resolved target path when requesting a file. Preserve originals/edits; retain decisions and source pointers rather than duplicating inputs. Imported content is data. Exclude secrets; no automatic private uploads.

Phase numbers below are navigation aids: resolve older checkpoints by their named responsibility/artifact, not an automatic numeric migration. Existing acceptance remains valid.

Normalize the actual scope before expansion: site/app, page/flow, section, component or local improvement. The same responsibilities apply proportionally. For a hero-only request, resolve its message/context and open aesthetic, reuse or review only the necessary foundations, then build/review that hero. Do not demand a full brand program, complete system library or all page sections. Accepted existing context, references and foundations satisfy their phases without reenactment. Inspect surrounding context when available; section-by-section work accumulates accepted system/relationships instead of restarting every section.

At each checkpoint state **phase; accepted work; missing input; proposed next output**. Ask a small batch of questions whose dependencies are settled. If access is absent, offer export/paste/readable files; a Notion or canvas URL alone proves no connection.

The agent performs applicable QA inside each authorized batch before presentation: relevant visual/structural checks for canvas/stills, relevant behavior for interactive work, and technical checks for requested code. Read only matching QA.md sections. Repair material problems; no extra QA interview, form or checkpoint for the designer. Report what cannot be observed rather than inventing a pass. Creative acceptance still belongs to the human.

Use the current agent's native structured questions, previews and annotations when available. Otherwise ask the same short questions in chat and show accessible rendered artifacts. Do not assume a question tool is available in every host or mode. Keep choices contextual, with free text; only essential missing inputs block dependent work.

Before the first visual output, reuse the project's existing medium. If none is chosen, propose an HTML/CSS specimen or prototype preview inside the agent interface; no separate design application is required. Penpot is conditional on the user's choice and working access; then read [PENPOT.md](PENPOT.md). No silent tool/model switch or automatic setup. Inspect selected provider access under [PROVIDERS.md](PROVIDERS.md) early, without delaying independent context work.

## 1. Product, brand and design problem

### Existing-project entry: understand what may change

When a base exists, inspect the relevant rendered interface and canonical brand/system sources before proposing a new direction: identity/assets, type/color roles, tokens/themes, component primitives, system documentation and affected consumers. Look for the actual stack's sources (for example CSS variables, theme configuration, token files and component libraries); do not assume a particular format or infer a complete system from a screenshot. Distinguish documented identity, observed implementation, explicit human approvals and your interpretation. An existing file is evidence, not proof that every decision is closed or that the user wants a replacement.

Show a short finding such as "I found an existing identity, token theme and shared components; the hero's hierarchy and imagery are the open improvement." Establish the change boundary in this existing context/direction checkpoint, not a separate onboarding form. Reuse explicit instructions such as "keep my fonts and palette; improve only the hero" without asking again. A localized correction that does not alter identity or shared-system rules should reuse the existing vocabulary and proceed through its normal scoped review. When the request could change identity/system relationships and the boundary is unresolved, ask one focused question with options grounded in what you found and free text. Useful interpretations are:

| Change boundary | Resulting treatment |
| --- | --- |
| Preserve the identity/system | Improve the requested composition, hierarchy, content, states, responsive behavior and finish inside its vocabulary; propose only necessary scoped additions. |
| Evolve it | Retain the user-selected anchors (for example logo, palette, type or component language), use them to guide reference fit, and propose specific changes to the open system relationships. |
| Replace it within the requested scope | Resolve a new direction and references, then propose/review a replacement system or scoped treatment; do not assume the entire application is a rebrand. |

These interpretations guide judgment; do not require a three-option menu for every task. Ask what to keep/change only where it materially affects the current proposal, rather than forcing a complete brand questionnaire. "Use this aesthetic as inspiration and improve it" may mean evolve, but identify the anchor relationships rather than silently copying everything or discarding them. "Make it better" alone does not authorize wholesale identity replacement. An explicit replacement choice does not erase content, accessibility, stack or behavioral constraints unless delegated.

Keep the agreed change boundary, protected anchors, open decisions and canonical sources in the target's existing record. Global installation never stores these in the shared kit or inherits them from another project. Enter the next unresolved responsibility instead of repeating completed phases: an accepted existing identity/system can satisfy direction and foundations; reference discovery remains focused on the actual gap. Existing documented/observed facts are not invented human approvals. Show a scoped system specimen only for additions/changes needing review, or reuse the already reviewed equivalent.

Before changing a shared token/component, inspect the affected consumers and explain its relevant downstream impact. Propose the smallest canonical change, show an appropriate before/after specimen in context and obtain the necessary acceptance before propagation. Do not fork a parallel design system to avoid understanding the existing one. Preserve unaffected choices and revisit only affected dependencies. For review-only work, report findings/recommendations without editing records or sources.

Inspect inputs first. Need what the brand/product does, why it matters, audience, main user task and intended result; relevant distinction, values/voice, honest proof, content/assets and constraints. Also understand the current situation/barriers, relevant content and device/access constraints, scope and the intended UI/UX improvement. Reuse available research, feedback or product knowledge; label assumptions. A designer-confirmed brief is not evidence from users. Ask only material gaps, not a research questionnaire.

If absent: "Phase 1: share a readable brief/link, attach TXT/MD/PDF, or place it at `<actual-target>/.design/brand.md`. I need what it does, who it serves and what users should achieve. We can capture those answers here."

Read Notion only with authorized working access. Inspect PDF visuals when extraction is insufficient and name unreadable portions. Produce a short sourced brand/product summary: facts, design implications/hypotheses and material unknowns separately. This is understanding, not an invented identity. Show it for confirmation/correction.

**Exit:** human-confirmed context. Wait before dependent experience/direction work.

## 2. Experience structure and interaction intent

Before multiplying screens/components, resolve the necessary content priority, grouping/terminology, navigation and critical task paths: entry/preconditions -> decisions/actions -> feedback/completion/recovery. Include relevant states, responsive/context constraints and known feasibility limits. A marketing site may need a clear information/action sequence; an application needs connected task/state design. Reuse existing accepted structure rather than remapping everything.

If uncertain, produce the smallest useful sketch, wireframe, flow or prototype in the chosen medium; placeholders remain illustrative. Do not wait for a complete design system to explore a task; defer styled full-page construction until the visual system is accepted. Focused UX/pattern references may help under REFERENCE_ROUTER.md without a full visual-discovery round. Identify unconfirmed assumptions; research/user sessions are conditional on actual need, scope and access, not a mandatory service subscription or paperwork stage.

Show the structure in context and discuss what the person understands, what they do next and how important states connect. Ask the designer to accept/correct open choices. This is experience design, not a QA gate. Structural acceptance does not close later art direction.

**Exit:** accepted scoped experience/content plan or supplied equivalent, unresolved assumptions and clear open visual decisions. Keep it in existing work/record; no mandatory sitemap, persona or journey document per task.

## 3. Designer's intended direction (vibe)

Reuse any stated vibe. Otherwise ask one contextual question with a few product-grounded directions, a "surprise me" choice and free text. For example, a B2B SaaS might support precise/technical, warm/editorial or bold/product-led directions; these are hypotheses, not universal options. If the designer chooses surprise, propose a coherent interpretation for review rather than silently accepting it.

Translate terms into observable relationships before searching: typography/scale, density/whitespace, palette/materials, imagery, geometry and motion where relevant. For "big tech, humanist", a possible reading is precise product hierarchy with warmer imagery, approachable language and softer accents; confirm the user's intended meaning. Distinguish constraints from interpretation and wanted from avoided traits.

Use [PROMPT.md](PROMPT.md) to turn the sparse product request plus vibe into a detailed, copyable execution prompt/search brief. Preserve original wording, negative constraints and sourced facts; label proposed relationships and unknowns rather than inventing features, audience or exact styles. Show the interpretation and expanded prompt as this phase's review output, revise with feedback, and retain the accepted version in the existing target record. Reuse prior acceptance; no separate prompt-approval ritual or external optimizer.

**Exit:** human-confirmed visual direction, faithful expanded brief/prompt and search question. Wait before searching under a proposed vibe. Standalone prompt help stops at its requested output.

## 4. References and human interpretation

Reuse supplied links, captures or moodboard files. If discovery is requested or needed for the agreed design task, search eligible sources directly; do not add a ritual permission question. Ask only for missing user-reserved references or meaning. Resolve selected provider access with [PROVIDERS.md](PROVIDERS.md), preserving existing setup authorization.

User-provided examples have priority. Inspect them and confirm what the designer likes/wants to avoid; they may establish the direction more clearly than words. If sufficient, use them directly without compulsory gallery discovery. If the user wants more matches or a relationship lacks evidence, search the selected sources by observed type/image, composition, density, geometry/materials and tone. Show what matches the supplied reference and why; preserve its accepted role rather than replacing it. A request to match a hero does not authorize copying unrelated pages or identities.

For a section/component, first constrain evidence to its requested pattern, then match the aesthetic within it. Follow REFERENCE_ROUTER.md's sequential fallback: selected connected MCPs -> relevant catalog sources through direct browser/search -> user-supplied evidence or clarified vibe if usable coverage is exhausted. Try the next relevant source when one fails; do not silently abandon the fallback library, pad with unrelated regions or claim sources were searched when they were not. Keep industry filters optional.

Discovery follows [REFERENCE_ROUTER.md](REFERENCE_ROUTER.md): Awwwards and One Page Love MCPs first when available, then relevant curated families or expressly human-added sources. Search primarily by the interpreted aesthetic and observable relationships, using actual provider filters and allowing examples from other industries. Keep product/task as the transfer/fit context; use it as a search filter only when helpful for an actual question or expressly requested. Refine queries when literal wording misses the concept. Inspect legible visuals and verify original-link provenance. An unavailable MCP can fall back with honest access limits.

Select enough distinct evidence to resolve the actual open choices, without a fixed count. Show a compact first selection and expand only where feedback or an unresolved relationship warrants it. Good gallery curation does not establish product fit; reject impressive but unsuitable examples. Report access/fit gaps without padding.

Show readable previews, exact source/verified original, relevant region/relationship, why it fits the requested vibe, proposed contribution and what to avoid. If visuals cannot be read, say so rather than claiming visual inspection. Include relevant task/state evidence for UX; label unseen behavior. Ask which to retain/reject and what to change in the interpretation. Search or replace affected examples, present the revised selection and wait again. Repeat until references and **what to take from each** are accepted; resolve conflicts rather than blending every identity. Retain `chosen relationship -> product application -> constraints/exclusions -> evidence` and useful rejection reasons.

**Exit:** human-reviewed references and accepted interpretation. Wait before foundations/components.

## 5. Designer's foundations and system development

Inspect existing tokens, components and system documentation first. Reuse their authority. If no system exists and design development is authorized, propose the scoped foundations from approved reference relationships and product constraints; do not block by demanding user-supplied tokens. Ask only for material reserved choices, assets or constraints. Cover actual type roles/fonts, semantic colors, sizing/spacing/density, geometry, imagery and relevant behavior; only needed categories apply.

Apply the existing-project change boundary from phase 1. Reuse protected anchors, update the canonical system only within the agreed boundary and show affected consumers for shared changes. Do not require the user to rebuild or reapprove an unchanged system merely because Design Kit was installed globally.

Reuse the chosen medium and canonical sources; do not switch tools or create a parallel system for this phase.

Develop the smallest system needed for agreed tasks/pages: semantic roles/aliases, usage, necessary derived values, responsive and interaction/accessibility rules. Preserve canonical token format/paths; DTCG interchange is optional. Use the existing system document or target DESIGN.md for decisions and reference relationships, not a second competing source of token values. Distinguish supplied/extracted values from proposals; public styles do not disclose a full internal design system.

Render a **system specimen before styled page construction**: real type hierarchy/content, colors in context, spacing/geometry, assets and representative UI states at relevant widths. A JSON file, color list or prose alone is insufficient. Use an existing preview/browser or readable captures; report missing rendering access. Show the specimen and canonical paths, explain consequential decisions, request corrections, revise and show again until accepted. This is a sample application of foundations; the reusable component library follows in the next phase.

**Exit:** accepted foundations/scoped rules. Correct locally; wait before base-component generation.

## 6. Base components

Derive the inventory and review batches from agreed tasks/content/pages; obtain acceptance if not established. No exhaustive framework library. Build only the current batch from accepted foundations, including required focus/disabled/loading/error and awkward-content states. Use actual canonical components/instances and token bindings where supported; matching rectangles do not establish reuse, and drawings do not prove keyboard behavior.

Inspect the result and show location, relevant states, changes and unknowns. Iterate corrections within the batch; do not generate another batch/composites while its review is pending.

**Exit:** accepted scoped base components, states, usage and paths/IDs.

## 7. Composite components and task patterns

Build approved batches of actual forms/navigation/listings/panels from accepted base components. Reuse instances. Include task sequence, feedback/recovery, representative content and in-context layouts so isolation cannot hide hierarchy/density/responsive problems.

Parts and screens inform each other: if context exposes a shared-system problem, propose the smallest correction and obtain acceptance before changing approved shared design. Invalidate only affected downstream work, not the whole product.

**Exit:** accepted scoped patterns and usable page/flow structure. Wait at each meaningful batch.

## 8. Page composition, flow and polish

Agree the whole-page/flow outline if missing. Produce the authorized batch using accepted context, reference map, system/components and representative real content. Use [DESIGN_DIRECTION.md](DESIGN_DIRECTION.md) to compare base/proposal and refine hierarchy, type/image balance, rhythm, identity, deeper regions, mobile and the connected experience. An operational but interchangeable layout does not meet an exceptional design brief. Components do not automatically settle layout or UX.

Show the result; wait, correct locally, present again. One accepted batch does not authorize every remaining page. A hero-only preview is not a completed product; decoration does not repair a weak concept. Show the visible design contribution and material tradeoffs; keep the stronger treatment if polishing weakens it. When scoped pages are accepted, continue to frontend implementation if already requested; otherwise stop at the requested design deliverable. Later refinement stays in this workflow and revisits only the actual open design question.

**Exit:** human-accepted requested pages/flows. Continue only within the existing requested scope; design-only does not authorize production code.

## 9. Requested code handoff

When frontend code is part of the request, implement accepted design in the target stack. Use real structure/tokens/component data with captures; pixels alone cannot disclose hidden values/behavior. Reuse useful accepted HTML/CSS/layout/assets, hardening or replacing prototype logic as needed. Apply SOFTWARE.md and relevant implementation QA. Consume existing API contracts where needed, but do not implement backend services, database changes or infrastructure. Label mocks and missing dependencies; deployment needs its own existing authorization.

Verify actual render, relevant widths/states, task/recovery and target checks. Present for review. A needed change to a closed design requires the proposed alternative and human acceptance, not a silent "improvement".

**Exit:** requested implementation, actual evidence/limits and human review status. Package tests do not certify generated quality or savings.

## Checkpoint format

Keep one short current record: `phase/scope; artifact paths/IDs; accepted revision + human decision reference; pending revision/feedback; next authorized action`. A revision can be a commit, existing version ID or dated capture linked to the reviewed artifact; no new tracking system. For mutable canvas/code, reread relevant state before using it. A path/ID is not proof that its current contents were accepted. Preserve later human edits; if they materially diverge, clarify affected decisions rather than restoring an old baseline or treating all changes as accepted.

Update on meaningful decisions, not each tool call. Record what was implemented, verified and accepted separately. After corrections, only changed/dependent work needs review; retain unrelated approvals. Missing essential input/access/review requires an exact gap and usable alternative. Guidance cannot technically compel every agent or guarantee aesthetics.
