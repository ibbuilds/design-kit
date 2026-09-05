# Reading, microcopy and expression

Verified 2026-09-04; [sources](../sources.json). Craft judgments below are original
synthesis, not experimentally established universal style rules.

## Reading hierarchy and rhythm

- **Principle / problem:** Give readers an intelligible hierarchy and sustained
  comfortable reading rather than a series of unrelated promotional blocks.
- **Use:** Editorial, documentation, knowledge and long-form content.
- **Do not use:** Display typography, tight measures or decorative interruptions
  that impair the actual reading task merely to look distinctive.
- **Alternatives:** Clear headings, summaries, tables of contents when useful,
  inline explanations, appropriate text measure and paragraph rhythm.
- **Exceptions:** Poetry, portfolios and art direction may deliberately break
  conventions when the intended experience remains understandable and accessible.
- **Accessibility:** Semantic heading intent, logical order, resize/reflow, meaningful
  links and image alternatives. No type scale or line length fits every script.
- **Source / scope:** `fluent-accessibility`, `wcag22`, `nng-heuristics`; structure
  and access, with type rhythm assessed by actual render and brief.

## Microcopy and feedback language

- **Principle / problem:** Labels and messages should describe the action, object
  and consequence in the audience's vocabulary.
- **Use:** Commands, errors, help, permissions and consequential choices.
- **Do not use:** Vague “Submit” when the consequence matters, humorous blame,
  unsupported promises, or expert terminology for an unfamiliar audience.
- **Alternatives:** Specific action labels, brief explanation near uncertainty,
  progressive help and consistent domain terms.
- **Exceptions:** Experts may need precise technical terms. Brevity must not remove
  essential information; translation may change length and grammatical structure.
- **Accessibility:** Visible text and accessible names align; links make sense in
  context, errors identify correction, critical messages persist long enough.
- **Source / scope:** `nng-heuristics`, `gov-errors`, `fluent-wait`, `wcag22`.

## Persuasion with credible evidence

- **Principle / problem:** Make the offer, relevance, proof and next step clear
  without replacing comprehension with visual spectacle.
- **Use:** Landing pages, pricing explanations, campaigns and other Persuade surfaces.
- **Do not use:** Invent testimonials, usage metrics, urgency, logos or outcomes;
  enforce a mandatory hero/cards/testimonials template.
- **Alternatives:** Product demonstration, meaningful examples, transparent comparison,
  narrative sequence or an evidence-led concise page.
- **Exceptions:** Brand-led expression may lead when the brief warrants it; commerce
  evidence is applicable only when a purchase/checkout problem exists.
- **Accessibility:** Readable hierarchy, descriptive CTAs, disclosed costs/conditions,
  motion alternatives and no meaning conveyed solely by imagery.
- **Source / scope:** Original design synthesis grounded in `nng-heuristics` and
  `wcag22`; no claim that a particular layout increases conversion.

## Coherent expressive systems

- **Principle / problem:** A distinctive visual thesis must shape composition,
  type, imagery and interaction together rather than decorate a generic template.
- **Use:** Experience surfaces and brief-supported expressive directions elsewhere.
- **Do not use:** Force novelty onto a constrained operational system or adopt a
  reference's brand assets, signature layout or copy.
- **Alternatives:** More restrained interpretation, domain-specific composition,
  distinctive content treatment, contrasting visual territories before selection.
- **Exceptions:** Deliberately familiar conventions may be the best expression of
  trust; gradients, cards, common fonts and single-family type are not defects alone.
- **Accessibility:** Expression must preserve navigation, readability, input access
  and alternatives to motion/gesture-only interaction.
- **Source / scope:** Original aesthetic methodology; constraints from `wcag22`
  and `nng-heuristics`, visual evidence from session-approved references only.

## Language and formatting context

- **Principle / problem:** Keep language choice findable and preserve understandable task context across languages.
- **Use:** Multilingual services and locale-dependent names, dates, units and currency.
- **Do not use:** Assuming nationality predicts language or one text expansion percentage fits every script.
- **Alternatives:** Recognizable language names, supported context preservation, explicit incomplete translation and representative long/bidirectional content.
- **Exceptions:** This is not a complete internationalization specification; retrieve scoped W3C guidance when script direction or semantics affect the decision.
- **Accessibility:** Test actual reading/focus order and meaningful labels, not blanket visual mirroring.
- **Source / scope:** `uswds-language` public-service pattern; formatting/layout resilience is original heuristic synthesis verified 2026-09-05.

## Mixed-direction content and layout

- **Principle / problem:** Language, base direction and alignment are different decisions. RTL text can contain LTR names, URLs and numbers; blanket reversal corrupts meaning.
- **Use:** Multiscript interfaces, user-entered names, identifiers and mixed-direction labels.
- **Do not use:** Reverse stored text, infer direction from language alone, or mirror every object.
- **Alternatives:** Direction-aware start/end alignment; isolate opposite-direction phrases from adjacent punctuation/numbers. In web handoff, explicit direction for known phrases and `dir=auto`/`bdi` for unknown inserted text preserve isolation; automatic first-strong detection has exceptions.
- **Exceptions:** Physical/spatial arrangements may remain fixed. Script-specific line breaking, shaping and font metrics require relevant language guidance and representative text, not a universal expansion percentage.
- **Accessibility:** Check actual reading/focus order, caret/selection and punctuation around mixed names/numbers; Figma appearance alone cannot verify browser text behavior.
- **Source / scope:** `w3c-bidi-structure`, `w3c-bidi-inline`, informative internationalization guidance read 2026-09-05. Original design translation; not a normative universal layout rule.

## Directional controls and imagery

- **Principle / problem:** Mirror by meaning. Reading/navigation direction can reverse while physical direction, identity and imagery retain meaning.
- **Use:** RTL localization of navigation, progress, ordered content and custom icons.
- **Do not use:** Flip logos, digits within a number, photographs or an arrow meaning physical right merely because the interface is RTL.
- **Alternatives:** Reverse reading-order navigation and associated progress endpoints where the platform expects it; use localized directional symbols. Reorder meaningfully ordered images without flipping their pixels.
- **Exceptions:** Complex icons need component-level judgment; script-specific artwork may need a localized version. These are Apple conventions; transfer to another platform only after checking its context.
- **Accessibility:** Preserve understandable control names, numeric values and reading order; inspect actual mixed-script size balance without prescribing a universal font adjustment.
- **Source / scope:** `apple-rtl`, platform guidance read 2026-09-05. No Apple visual-style mandate.
