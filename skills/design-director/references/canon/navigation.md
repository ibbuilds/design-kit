# IA, navigation, search and filtering

Verified 2026-09-04; [sources](../sources.json). Apply to collections/tasks needing
wayfinding; do not add app navigation to every persuasive or expressive page.

## Wayfinding and hierarchy

- **Principle / problem:** Show where the person is, what belongs together and how
  to return; don't make every destination equally prominent.
- **Use:** Multi-area products, content collections, nested services.
- **Do not use:** Deep menus for a short linear task; tabs that secretly navigate
  unrelated destinations or reset work without warning.
- **Alternatives:** Clear headings, breadcrumbs for hierarchy, contextual back,
  task navigation, search for known-item retrieval.
- **Exceptions:** A linear transaction may minimize global navigation while retaining
  exit/recovery. Expert tools may need persistent multi-area access.
- **Accessibility:** Meaningful labels and sequence; selected state beyond color;
  annotate focus behavior using the relevant APG pattern, not visual analogy alone.
- **Source / scope:** `nng-heuristics`, `apg-patterns`, `gov-questions`; general,
  web widget behavior and transactional public-service journeys respectively.

## Search and result recovery

- **Principle / problem:** Support known-item and exploratory retrieval without
  concealing query, scope or the reason results changed.
- **Use:** Collections large/varied enough that direct navigation is inefficient.
- **Do not use:** Add search to a tiny stable set because a template has a search bar.
- **Alternatives:** Browse by meaningful categories, recent items, guided choices.
- **Exceptions:** Sensitive results must obey access rules; fuzzy matching needs
  transparent correction, not silent query replacement.
- **Accessibility:** Label input and submit, show query/result count and empty/error
  states, preserve focus, avoid announcing every keystroke. Keyboard-operable suggestions.
- **Source / scope:** Original synthesis from `nng-heuristics`, `apg-patterns`,
  `carbon-filter`; retrieval design, not a claim of search algorithm performance.

## Filters and sorting

- **Principle / problem:** Make applied criteria and ordering visible; users should
  understand why records disappear and recover without resetting everything.
- **Use:** Meaningful subsets, multi-attribute comparison, repeated retrieval.
- **Do not use:** Facets without useful data distribution or controls that change
  order while implying they change membership.
- **Alternatives:** Instant results for cheap queries; Apply for expensive/multiple
  criteria; saved views for recurring expert tasks; clear one/all actions.
- **Exceptions:** Expensive async results need progress and stale-result handling;
  disabled facets should explain unavailable combinations where useful.
- **Accessibility:** Named groups, selection states, result status, stable focus and
  keyboard controls. Don't make removable chips the only way to understand criteria.
- **Source / scope:** `carbon-filter`, `carbon-table`; data-heavy product patterns,
  not universal commerce taxonomy or fixed latency thresholds.
