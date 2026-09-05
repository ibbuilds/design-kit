# Accessibility and keyboard

Verified 2026-09-04. Sources: [registry](../sources.json). Apply requirements at the
intended conformance level and platform; record design evidence and runtime gaps.

## Perceivable contrast and meaning

- **Principle / problem:** People must distinguish text, controls and status without
  relying on color alone.
- **Use:** Text, interactive boundaries, charts, focus and error states. WCAG 2.2 AA
  text contrast is 4.5:1; large text is 3:1 (18pt regular or 14pt bold). Relevant
  non-text UI/graphical contrast is 3:1 against adjacent colors.
- **Do not use:** Apply text ratios indiscriminately to decorative artwork; declare
  success from a screenshot sampled without knowing the actual background/state.
- **Alternatives:** Labels, shape, pattern, icons with meaning and stronger contrast.
- **Exceptions:** Normative exemptions include inactive controls, incidental text
  and logotypes; absence of a requirement does not mean low contrast is desirable.
- **Accessibility:** Check all meaningful states, transparency, image backgrounds
  and color-vision differences. Record measured pairs rather than “looks accessible.”
- **Source / scope:** `wcag22` 1.4.1, 1.4.3, 1.4.11; normative web criteria.

## Reflow and readable content

- **Principle / problem:** Enlarging text or narrowing the viewport must not lose
  content or functionality.
- **Use:** Web designs: text resize to 200%; reflow at 320 CSS px width (horizontal
  writing) without two-dimensional scrolling; inspect meaningful long content.
- **Do not use:** Shrink text to make a fixed artboard fit or equate device pixels
  with CSS pixels. A Figma frame resize is evidence of layout intent, not browser proof.
- **Alternatives:** Stack/reprioritize panes, wrap labels, disclose secondary details.
- **Exceptions:** Content requiring two-dimensional layout (some tables/maps) has
  reflow exceptions; surrounding navigation and controls still need accommodation.
- **Accessibility:** Specify text-spacing resilience, orientation and logical order;
  annotate alt text/captions/transcripts for meaningful media.
- **Source / scope:** `wcag22` 1.4.4, 1.4.10, 1.4.12, 1.3.4; `fluent-accessibility`.

## Keyboard, focus and targets

- **Principle / problem:** Complete tasks without precise pointing or a mouse, and
  make the currently operated control evident.
- **Use:** Interactive web designs: logical focus order, visible focus, no keyboard
  traps. WCAG 2.2 AA minimum target is 24×24 CSS px or its spacing/other exceptions;
  focus must not be entirely obscured by author-created content.
- **Do not use:** Claim 44px is the universal AA target minimum, or impose left-to-right
  “Z order” on RTL or a different meaningful task sequence.
- **Alternatives:** Larger targets, spacing, keyboard shortcuts with discovery,
  single-pointer alternatives to dragging and multipoint gestures.
- **Exceptions:** Inline targets, equivalent controls and essential/user-agent
  presentation have specific target exceptions; check normative text. 44×44 is
  WCAG AAA target guidance; native platform sizing uses its own units/conventions.
- **Accessibility:** Annotate focus entry/return, keyboard actions, names/roles and
  state announcements. Test assistive technology later in implementation.
- **Source / scope:** `wcag22` 2.1, 2.4.3, 2.4.7, 2.4.11, 2.5.7, 2.5.8;
  `apg-patterns` for interaction conventions, informative rather than normative.

## Motion and time

- **Principle / problem:** Motion, flashing or expiring input can obstruct perception
  and completion.
- **Use:** Animated/immersive surfaces, carousels, live updates, timed sessions.
- **Do not use:** Require gestures or motion as the only way to understand content;
  equate a reduced-motion annotation with tested implementation.
- **Alternatives:** Static equivalent, pause/stop/hide where required, extend time,
  stable layout, restrained progress updates.
- **Exceptions:** Essential timing/motion and real-time events have narrowly scoped
  normative exceptions. Security needs require explicit design of recovery.
- **Accessibility:** Avoid unsafe flashing; communicate changes without constant
  announcements. Reduced-motion accommodation is good design beyond individual AA rules.
- **Source / scope:** `wcag22` 2.2, 2.3; `apple-accessibility`; see states for timeouts.
