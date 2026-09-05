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
