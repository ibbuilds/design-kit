---
name: design-kit
description: "Design, improve, or review interfaces in their existing medium. Use for visual UI work and requested frontend QA, not backend work or kit maintenance."
---

# Design Kit

Make the actual interface better, not merely more consistent with a checklist. Own the open visual decisions and deliver a rendered result. Preserve the user's constraints, behavior, content, valued source treatments, and later human edits. Existing code is an implementation baseline, not automatic aesthetic approval.

## Working agreement

Default to an **artifact-first** assignment: inspect the relevant context, choose a coherent treatment, implement, inspect and refine, then show the result. Do not require approval of a rewritten prompt, reference board, token sheet, or intermediate diagnosis unless the user requested that supervision. [ONBOARDING.md](ONBOARDING.md) handles missing inputs and explicit checkpoints; it is not a mandatory sequence of phases.

A design request delegates open aesthetic choices within its scope. It does not authorize replacing protected identity, changing product behavior, expanding scope, installing dependencies, paid access, private uploads, external writes, or publication. Ask only when a material reserved choice or necessary permission is genuinely unresolved; reuse answers already given. Review-only edits neither code nor project records.

Keep the current agent, model, settings, tools, and working medium. No automatic model handoffs, extra agents, runtime, or MCP setup. For broad visual evolution, work on a representative unit first and obtain acceptance before application-wide propagation. An authorized consistency repair may update its shared owner and affected consumers in the agreed batch without per-component permission.

## 1. Find the visual problem

Inspect the actual render, relevant source files and accepted examples. Locate the canonical style/component owners and enough consumers to understand the proposed change. Do not begin with an exhaustive repository or catalog audit.

Choose the appropriate treatment:

| Task | Starting point |
| --- | --- |
| Faithful implementation / consistency | Reuse the closest accepted code, component, source control or composition. Restore its relationships; do not redesign valued originals. |
| Existing UI, appearance unapproved | Preserve engineering and protected anchors. Resolve the visual relationships that remain open; do not treat the whole library as approved. |
| New design | Use product goals, real content, assets and constraints to author one representative composition in the chosen medium. |
| Review | Compare evidence and report prioritized findings; no edits. |

For craft complaints, inspect applied typography, color roles, effective spacing, control families and assets before assuming that navigation or layout needs replacement. For composition complaints, inspect attention order, grouping, proportions, enclosure and density. The user supplies direction, not an exhaustive defect inventory. Read only the affected [CRAFT.md](CRAFT.md) sections; use [DESIGN_DIRECTION.md](DESIGN_DIRECTION.md) for unresolved visual choices.

## 2. Choose changes that can actually improve the render

Use the user's strongest accepted example or an inspected, relevant reference as a quality anchor when available. A baseline that is merely less broken is not necessarily good enough.

Form a short working note, not a new specification document: **visible gap or opportunity -> proposed mechanism -> expected visible difference -> protected relationships**. Usually one to three coordinated moves suffice; this is a prioritization aid, not a cap on required fixes. Own the choices instead of asking the user to prescribe their pixels. Separate observed violations, intent mismatches and aesthetic proposals.

The moves must address the requested quality: for example, coordinate control weight and label rhythm across a family rather than adjusting one convenient margin. Do not substitute generic decoration or an unrelated layout overhaul for the actual complaint. When references conflict, select a dominant treatment and bound secondary contributions instead of averaging their identities.

Use supplied evidence first. Additional research is conditional on a named decision it can resolve, not a required reference count. [REFERENCE_ROUTER.md](REFERENCE_ROUTER.md) uses existing MCPs or the curated [REFERENCES.md](REFERENCES.md) catalog selectively. Missing optional inspiration does not block an authorized original proposal; missing a required fidelity source does block a fidelity claim. Never invent visual inspection.

## 3. Author one coherent candidate

Design directly in the target's existing code or chosen editable medium. Resolve affected foundations in a real composition; a separate specimen, complete token system or component library is not a prerequisite. Use an existing preview or isolated disposable artifact when necessary, not a new production review route.

Change canonical owners where they explain repeated symptoms. Preserve correct source controls and semantic behavior. A proposed treatment may need coordinated type, spacing, asset and composition changes; do not mistake a tiny diff for a high-value design. Conversely, do not rebuild adequate structure merely to make the change look substantial.

Use real or explicitly representative content and loaded fonts/assets. Keep the full composition visible while refining details. For a family change, include an affected consumer and a meaningful variant/state; for a screen, include a contrasting state or narrow container where it challenges the design. Retain accepted implementation, not just prose about it. Requested frontend integration follows [SOFTWARE.md](SOFTWARE.md) inside this assignment.

## 4. Compare and correct within the budget

Inspect the actual render at intended viewing size, then the discrepant region closely. Compare baseline/candidate under equivalent content, state, viewport and loaded assets. Compare the anchor's relevant relationships too, without assuming identical pixels suit different content. Judge the images before relying on your explanation of the changes.

Check visual contribution separately from functional/responsive correctness. Repair affected states, widths, content stress and relevant failures using CRAFT.md and matching [QA.md](QA.md) sections. Numerical consistency, screenshot counts and passing tests do not certify visual quality.

Default budget for one bounded unit: **one candidate and at most two grouped visual refinement passes**. A pass addresses the highest-impact remaining gaps together; another phase, component or context handoff does not reset it. [EXECUTION.md](EXECUTION.md) defines the stopping rules. User-specified budgets override this default. Do not weaken correctness checks or hide incomplete work to fit the budget.

If a pass produces no material improvement, do not repeat the same hypothesis. Distinguish execution drift from a weak treatment or missing evidence. Preserve the stronger version. An alternative must fit the remaining scope/budget; otherwise report the unresolved gap and stop, without declaring victory.

## 5. Deliver evidence and preserve the gain

Lead with the actual result and a useful before/after comparison. Briefly state the visible contribution, important tradeoffs, checked scope and remaining limits. No numerical self-score or unsupported quality claim. Human acceptance belongs to the user; agent-selected work is not human-approved.

For broad evolution, wait here before propagating new shared visual choices. Once accepted, reuse their actual code/assets/tokens and verify a contrasting consumer. Keep a small coverage record for a whole-library request; a single attractive example does not close uninspected families.

Retain paths, accepted revision/captures, protected choices, pending defects and next authorized action in the target's existing record, otherwise `.design/project.md`. Do not duplicate token values, archive the transcript, or update the shared kit during a design task.

## Conditional resources

[TASTE.md](TASTE.md) and [GUIDELINES.md](GUIDELINES.md): a relevant unresolved craft/experience question, not compulsory extra reading. [PROMPT.md](PROMPT.md): requested prompt help. [HOSTS.md](HOSTS.md) / [PROVIDERS.md](PROVIDERS.md): actual activation/access/setup problems. [PENPOT.md](PENPOT.md): user-selected Penpot only. Historical research is not build context. This file owns the current procedure; supporting documents do not add unrequested research quotas or approval phases.
