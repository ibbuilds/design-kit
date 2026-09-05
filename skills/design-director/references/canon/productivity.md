# Professional tools and shared work

Original scoped synthesis, verified 2026-09-05; [sources](../sources.json).
Use only for actual tool/workspace behavior. Source systems supply behavioral
alternatives; the project's art direction determines visual expression.

## Commands, modes and selection

- **Principle / problem:** Distinguish an immediate command from a persistent mode or toggle; make scope and current selection apparent.
- **Use:** Professional tools, inspectors and contextual command surfaces.
- **Do not use:** Ambiguous icon-only mode changes or hidden essential commands.
- **Alternatives:** Single/multiple/empty selection, contextual tools, wrapping or overflow chosen by task. Keep frequent actions discoverable.
- **Exceptions:** Moving focus into an inspector should not silently change selection. Mixed values differ from empty values; actual editing semantics depend on the product.
- **Accessibility:** Named controls and visible selected state; keyboard access complements discoverable commands. Verify detailed keyboard behavior in the applicable standard/platform.
- **Source / scope:** `spectrum-actions` distinguishes commands/toggles, selection and overflow (design-system pattern, verified 2026-09-05). Inspector scope is original synthesis with `nng-complex`. No Spectrum palette, radius, blue emphasis or fixed density is implied.

## Resume nonlinear work

- **Principle / problem:** Preserve task context so people can resume after interruption without reconstructing their reasoning.
- **Use:** Long professional work, investigations and multi-pane editing.
- **Do not use:** Stacking panels by convention or promising unsupported history/undo.
- **Alternatives:** Persistent comparison panes, deep-work routes, saved selection/filter context and previews of reversible effects.
- **Exceptions:** External irreversible commands may have no undo. Spectrum 2 is a preview direction, not proof of completed component behavior.
- **Accessibility:** Keyboard accelerators supplement visible learnable paths; restore focus meaningfully after context changes.
- **Source / scope:** `nng-complex` general complex-application research synthesis; `spectrum2` adaptability direction. Original scoped synthesis verified 2026-09-05.

## Shared context and conflicts

- **Principle / problem:** Make workspace, object and access scope understandable before actions cross a boundary.
- **Use:** Collaborative workspaces, shared objects and concurrent changes.
- **Do not use:** Treating presence as permission or a remote cursor as proof that edits are saved.
- **Alternatives:** Distinguish local draft, saving, saved, conflicting and disconnected states; preserve effort with supported comparison/reconciliation.
- **Exceptions:** Never invent merge behavior or backend guarantees. Not every collaboration surface needs cursors, presence or locks.
- **Accessibility:** Consistent terminology and important announcements without continuous focus interruption; accessible components do not certify the whole workflow.
- **Source / scope:** `atlassian-accessibility` supports consistency/control and end-to-end access; `nng-complex`, `nng-heuristics` support continuity. Conflict behavior is heuristic synthesis, not a tested product claim; verified 2026-09-05.

## Predictable editing history

- **Principle / problem:** People need to predict what undo changes and see its result, especially when an inspector or canvas obscures the affected object.
- **Use:** Creative editors, direct manipulation and repeated property adjustment.
- **Do not use:** Promise unlimited history, universal shortcuts or undo for unsupported external irreversible effects.
- **Alternatives:** Name the affected operation, reveal its result, and group related incremental adjustments into meaningful undo steps where supported. Keep temporary preview distinct from committed change and selection scope distinct from focus.
- **Exceptions:** Undo boundary, save/version history and collaboration conflict behavior are different contracts; inspect project support. Applying Apple principles outside Apple platforms is reasoned transfer, not a platform requirement.
- **Accessibility:** Keyboard shortcuts complement discoverable commands; keep focus and selection understandable after reversal without forcing pointer-only manipulation.
- **Source / scope:** `apple-undo` platform guidance read 2026-09-05 supports predictability, visible results and grouping. `spectrum-actions` supports command/selection distinction. Preview/commit and cross-platform transfer are original heuristic synthesis; no creative-app visual style is implied.
