# E-commerce

Verified 2026-09-04; [sources](../sources.json). Load only for shopping, cart or
checkout. Baymard findings are domain research, not rules for every conversion UI.

## Checkout without avoidable burden

- **Principle / problem:** Let shoppers complete an intended purchase without
  unnecessary registration, confusing fields or hidden costs.
- **Use:** Actual consumer checkout and cart-to-purchase transitions.
- **Do not use:** Force accounts by default, import checkout assumptions into a
  public-service form, or claim generic abandonment percentages predict this product.
- **Alternatives:** Clear guest path, supported express checkout, concise inputs,
  accurate order summary, transparent delivery/fees and editable purchase details.
- **Exceptions:** Some regulated or account-bound purchases require identification;
  explain why. Payment and fulfillment options depend on actual business support.
- **Accessibility:** Field labels, autofill intent, understandable errors, keyboard
  payment paths, review before financial commitment and preserved valid data.
- **Source / scope:** `baymard-checkout`, `wcag22`; consumer checkout research and
  financial error prevention, not a guaranteed conversion uplift.

## Purchase confidence and fulfillment

- **Principle / problem:** Shoppers need to compare what matters and understand
  when/what they receive, including the final cost and constraints.
- **Use:** Product selection, order summary, delivery choice and purchase review.
- **Do not use:** Fake reviews, unverifiable trust marks, ambiguous shipping speed
  in place of useful arrival information or undisclosed mandatory charges.
- **Alternatives:** Supported delivery dates/ranges, plain return conditions,
  attribute comparisons, clear variants and honest stock information.
- **Exceptions:** Unknown delivery estimates must stay uncertain; don't invent a
  date for a prettier prototype. Synthetic testing content must be labeled.
- **Accessibility:** Legible prices/units, distinguish options beyond color,
  announce cart changes and preserve context during quantity/variant edits.
- **Source / scope:** `baymard-checkout`, `nng-heuristics`, `wcag22`; commerce only.

## Product finding and comparison

- **Principle / problem:** Choose search, facets, sorting and comparison from actual shopping criteria.
- **Use:** Consumer product discovery and attribute/variant comparison.
- **Do not use:** Transferring internal database filters unchanged into shopping or treating gallery pixels as usability evidence.
- **Alternatives:** Visible applied criteria, no-result recovery, comparable price basis/variants and relevant fulfillment constraints.
- **Exceptions:** Baymard product-list HTTP client access returned 403, but the normal browser loaded its public research overview. Full reports remain paid; do not invent restricted findings or conversion uplift.
- **Accessibility:** Preserve focus, label filters, expose selection and explain changed results without announcing every keystroke.
- **Source / scope:** `baymard-product-lists` reports that product presentation, filtering and sorting work together to support finding and evaluating relevant products. Public commerce research, verified in browser 2026-09-05; recovery details are original synthesis with `nng-heuristics`. Study outcomes are not forecasts for this product.
