# Expert work, tables and visualization

Verified 2026-09-04; [sources](../sources.json). Load for real data/operational
complexity, not because a simple app could contain a metric card.

## Expert workspaces

- **Principle / problem:** Preserve task context across nonlinear work and large
  information sets; experienced people often need simultaneous comparison.
- **Use:** Dense operations, investigation, monitoring and repeated professional tasks.
- **Do not use:** Hide essential data behind repeated disclosure just to look minimal.
- **Alternatives:** List/detail panes, configurable views, progressive learning,
  shortcuts, contextual documentation and reversible exploration.
- **Exceptions:** Novice and expert roles can coexist; safety-critical actions need
  explicit safeguards and training rather than trial and error.
- **Accessibility:** Density must retain legibility, focus visibility and input
  alternatives; keyboard efficiency complements a discoverable path.
- **Source / scope:** `nng-complex`, `nng-heuristics`; complex applications only.

## Tables and grids

- **Principle / problem:** Align comparable attributes and expose useful ordering
  without turning every record into an oversized card.
- **Use:** Repeated records with comparable fields; show units, alignment and truncation rules.
- **Do not use:** Tables for a narrative sequence or an interactive ARIA grid merely
  because rows/columns look tabular.
- **Alternatives:** Lists, cards for rich heterogeneous content, detail panels,
  progressive columns, narrow-screen summaries with full detail access.
- **Exceptions:** True spreadsheet-like editing may justify a composite grid and
  its directional-key model; two-dimensional comparison can retain scrolling.
- **Accessibility:** Headers/relationships, sort state, named row actions; specify
  tab versus arrow behavior deliberately. Keep truncated information available.
- **Source / scope:** `carbon-table`, `apg-grid`, `wcag22`; product table usage and
  informative web grid behavior, with normative reflow exceptions.

## Selection and bulk action

- **Principle / problem:** Make the selected set and action scope explicit so people
  do not act on hidden, stale or unintended records.
- **Use:** Repeated actions across records with clear eligibility.
- **Do not use:** Imply “select all” spans all pages when it covers visible rows only.
- **Alternatives:** Per-row actions, explicit all-results selection, preview before
  applying, batch toolbar with count and clear selection.
- **Exceptions:** Mixed permissions and partial success need per-item results and
  retry of failed items only; destructive batches need stronger consequence clarity.
- **Accessibility:** Checkbox names/state, indeterminate state, keyboard reachability
  and selection announcements. Preserve context after batch completion.
- **Source / scope:** `carbon-table`, `nng-heuristics`; original scope/recovery
  synthesis for bulk operational tasks.

## Charts and decision support

- **Principle / problem:** Choose representation from the comparison/question, not
  empty dashboard space; explain units, time range, denominator and data freshness.
- **Use:** Trends, comparisons, distributions or relationships that graphics clarify.
- **Do not use:** Decorative fake data, unlabeled gauges or a chart when one number
  or table answers the question more accurately.
- **Alternatives:** Table for precise lookup, bars for comparison, line for temporal
  trends; choose more specialized plots only when the task warrants them.
- **Exceptions:** Uncertainty, incomplete data, unequal baselines and aggregation
  can change interpretation; disclose rather than polish them away.
- **Accessibility:** Color-independent series, legible direct labels, textual summary
  and accessible data alternative; tooltip-only values are insufficient.
- **Source / scope:** `carbon-charts`, `wcag22`; visualization selection and access,
  not endorsement of a particular metric, causal interpretation or business model.

## Live operations and command consequences

- **Principle / problem:** Distinguish observed state, timestamp/freshness, requested command and confirmed execution.
- **Use:** Live monitoring, alerts and consequential command surfaces.
- **Do not use:** Stale/missing readings shown as healthy zero, or silently reordering a target under the operator.
- **Alternatives:** Stable selection, freshness indicators, explicit command scope/eligibility and partial-failure results.
- **Exceptions:** Acknowledgment is not resolution. Alarm thresholds, escalation and safe operating procedures need actual domain evidence; matching screenshots cannot certify safety.
- **Accessibility:** Prioritize meaningful status changes without constant announcements; preserve focus and color-independent urgency.
- **Source / scope:** Original heuristic synthesis from `nng-complex`, `nng-heuristics` and state/recovery guidance; verified 2026-09-05. Preserve visual ambition through task-specific hierarchy/density/type instead of importing enterprise branding.

## Analytical structures and loaded selection

- **Principle / problem:** Choose a structure from whether users compare cells, work on complete records, aggregate measures or traverse a true hierarchy.
- **Use:** Large operational datasets, analytical comparison and aggregation.
- **Do not use:** Grouping as a substitute for parent/child data, or editable aggregate totals with no defined way to allocate the result to underlying records.
- **Alternatives:** Responsive records for line-item tasks, analytical tables for cell/aggregate work, tree structures for hierarchy, chart-to-detail for overview. Smartphone work may need a different presentation, not a scaled desktop grid.
- **Exceptions:** Fiori's row thresholds and component performance are implementation-specific, not universal limits. Distinguish loaded rows from all matching results when selecting across pages/ranges; state real limits rather than silently excluding unloaded items.
- **Accessibility:** Compact pointer-oriented density may fail touch use. Provide visible keyboard-operable alternatives to drag/context-menu actions, stable column widths and meaningful units; do not sum incompatible currencies/units into a misleading total.
- **Source / scope:** `sap-analytical`, Fiori 1.151 design-system pattern, browser verified 2026-09-05 after HTTP client 403. Transfer the behavioral distinctions; its styling, exact density values, component APIs and every local recommendation are not universal rules.
