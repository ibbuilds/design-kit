# Supervised design onboarding

Read the common contract, continuity/checkpoint and current phase. Read subsequent phases only when entering them. [SKILL.md](SKILL.md) remains the entrypoint; this is guidance for the current agent, not a runtime.

## The phase contract

**Inspect -> identify phase -> obtain missing input -> produce agreed output -> show artifact -> wait for human review -> record acceptance/corrections.** Start dependent work only after acceptance and authorization of its scope. Corrections keep the batch open. A supplied file, silence, elapsed time or the agent's recommendation is not acceptance.

Reuse explicit approvals already supplied, within their scope; a later phase can be entered directly. "Make the design" does not waive checkpoints; an explicit user override can. Complete routine corrections within the approved batch without per-edit permission. Pending feedback permits only independent work already authorized inside this phase. Single-phase requests stay there; review-only does not edit records/designs. Backend-only uses SOFTWARE.md. Examples are not the user's preferences.

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

At each checkpoint state **phase; accepted work; missing input; proposed next output**. Ask a small batch of questions whose dependencies are settled. If access is absent, offer export/paste/readable files; a Notion or canvas URL alone proves no connection.

## 1. Brand/product information and summary

Inspect inputs first. Need what the brand/product does, why it matters, audience, main user task and intended result; relevant distinction, values/voice, honest proof, content/assets and constraints. Ask only material gaps; no full branding questionnaire for a new project.

If absent: "Phase 1: share a readable brief/link, attach TXT/MD/PDF, or place it at `<actual-target>/.design/brand.md`. I need what it does, who it serves and what users should achieve. We can capture those answers here."

Read Notion only with authorized working access. Inspect PDF visuals when extraction is insufficient and name unreadable portions. Produce a short sourced brand/product summary: facts, design implications/hypotheses and material unknowns separately. This is understanding, not an invented identity. Show it for confirmation/correction.

**Exit:** human-confirmed context. Wait before direction/reference work.

## 2. Designer's intended direction (vibe)

Ask for the designer's ideas, character, wanted/avoided qualities, sketches or uncertainty. Reflect their words with hard constraints versus interpretations; no industry stereotype or default kit aesthetic. If undecided, offer a few concise product-grounded options for discussion, not complete variant builds.

**Exit:** human-confirmed direction and search question. Wait before searching under a proposed vibe.

## 3. References and human interpretation

If not settled: "Do you have links/captures or files at `<actual-target>/.design/references/`, or should I search the curated Design Kit sources for our agreed direction?"

Reuse supplied examples. Delegated discovery follows [REFERENCE_ROUTER.md](REFERENCE_ROUTER.md): relevant curated families or expressly human-added sources; inspect visuals and verify original-link provenance. Existing browser/search suffices; an MCP is optional.

Default: **eight clear, distinct, relevant inspected references**, supplied/retrieved/combined. Eight is a working default, not a proven optimum. If access/fit falls short, show valid evidence and ask whether to search other eligible sources, accept user additions or waive the count. No padding or silent waiver.

Show preview when possible, exact source/verified original, region/relationship, fit, differences and unknowns. Include relevant task/state evidence for UX; label unseen behavior. Ask which to retain/reject and **what to take from each**. Synthesize that feedback into `chosen relationship -> product application -> constraints/exclusions -> evidence`; resolve conflicts rather than blending every identity. Keep only chosen contributions/useful rejection reasons.

**Exit:** human-reviewed references and accepted interpretation. Wait before foundations/components.

## 4. Designer's foundations and system development

Request the supplied base at `<actual-target>/.design/foundations.md` or an existing document/tokens/design file: type roles, primary/semantic colors, sizing/spacing/density, geometry, shadows and relevant behavior. Only needed categories apply. For a material missing foundation, ask or offer focused assistance; proposed additions need acceptance.

**Choose/reuse the design medium before the first visual system output.** Penpot is the preferred editable-canvas candidate when chosen; then read [PENPOT.md](PENPOT.md). Existing media or explicitly chosen HTML/CSS previews work. Verify capability; no silent switch or automatic setup. Do not block brand/direction work on canvas setup.

Develop the smallest system needed for agreed tasks/pages: semantic roles/aliases, usage, necessary derived values, responsive and interaction/accessibility rules. Preserve canonical token format/paths; DTCG interchange is optional. Distinguish supplied values from proposals. Show additions and a visual application in the chosen medium; explain consequential differences.

**Exit:** accepted foundations/scoped rules. Correct locally; wait before base-component generation.

## 5. Base components

Derive the inventory and review batches from agreed tasks/content/pages; obtain acceptance if not established. No exhaustive framework library. Build only the current batch from accepted foundations, including required focus/disabled/loading/error and awkward-content states. Use actual canonical components/instances and token bindings where supported; matching rectangles do not establish reuse, and drawings do not prove keyboard behavior.

Inspect the result and show location, relevant states, changes and unknowns. Iterate corrections within the batch; do not generate another batch/composites while its review is pending.

**Exit:** accepted scoped base components, states, usage and paths/IDs.

## 6. Composite components and task patterns

Build approved batches of actual forms/navigation/listings/panels from accepted base components. Reuse instances. Include task sequence, feedback/recovery, representative content and in-context layouts so isolation cannot hide hierarchy/density/responsive problems.

Parts and screens inform each other: if context exposes a shared-system problem, propose the smallest correction and obtain acceptance before changing approved shared design. Invalidate only affected downstream work, not the whole product.

**Exit:** accepted scoped patterns and usable page/flow structure. Wait at each meaningful batch.

## 7. Page composition, flow and polish

Agree the whole-page/flow outline if missing. Produce the authorized batch using accepted context, reference map, system/components and representative real content. Inspect integrated hierarchy/rhythm, deeper regions, mobile, primary task and important states. Components do not automatically settle layout or UX.

Show the result; wait, correct locally, present again. One accepted batch does not authorize every remaining page. A hero-only preview is not a completed product; decoration does not repair a weak concept. When scoped pages are accepted, let the user choose manual polish, AI polish or implementation.

**Exit:** human-accepted requested pages/flows. Wait for the next choice; no automatic production code.

## 8. Authorized implementation and verification

After code is requested, implement accepted design in the target stack. Use real structure/tokens/component data with captures; pixels alone cannot disclose hidden values/behavior. Reuse accepted HTML/CSS rather than regenerate. Apply SKILL.md's verification guidance and SOFTWARE.md for required engineering; no unsolicited backend/deployment.

Verify actual render, relevant widths/states, task/recovery and target checks. Present for review. A needed change to a closed design requires the proposed alternative and human acceptance, not a silent "improvement".

**Exit:** requested implementation, actual evidence/limits and human review status. Package tests do not certify generated quality or savings.

## Checkpoint format

Keep one short current record: `phase/scope; artifact paths/IDs; accepted revision + human decision reference; pending revision/feedback; next authorized action`. A revision can be a commit, existing version ID or dated capture linked to the reviewed artifact; no new tracking system. For mutable canvas/code, reread relevant state before using it. A path/ID is not proof that its current contents were accepted. Preserve later human edits; if they materially diverge, clarify affected decisions rather than restoring an old baseline or treating all changes as accepted.

Update on meaningful decisions, not each tool call. Record what was implemented, verified and accepted separately. After corrections, only changed/dependent work needs review; retain unrelated approvals. Missing essential input/access/review requires an exact gap and usable alternative. Guidance cannot technically compel every agent or guarantee aesthetics.
