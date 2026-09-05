# Adaptive layouts and platform conventions

Verified 2026-09-04; [sources](../sources.json). Load only the target platform's
guidance. Do not adopt a framework or generate implementation code.

## Adapt structure, preserve task

- **Principle / problem:** Resizing changes available space and sometimes which
  panes can be visible; simply scaling a desktop composition loses usability.
- **Use:** Requested responsive/multi-window surfaces and content enlargement.
- **Do not use:** Assume phone equals touch-only or desktop equals pointer-only;
  force mobile-first onto a desktop-only expert task.
- **Alternatives:** Pane show/hide, stacking/reflow, alternate navigation, retained
  selection and explicit detail routes, content-based breakpoints.
- **Exceptions:** Material renamed window size classes to breakpoints in May 2026;
  use current target terminology. Essential spatial content may retain pan/zoom.
- **Accessibility:** Keyboard/pointer/touch alternatives, coherent focus after
  reflow, orientation and text-size resilience.
- **Source / scope:** `material-adaptive`, `wcag22`; adaptive design and web access.

## Touch and native sizing

- **Principle / problem:** Interactive areas must fit the platform, input precision,
  spacing and motor needs; visual icon size is not the hit area.
- **Use:** Mobile/touch interfaces and mixed-input devices.
- **Do not use:** Treat WCAG CSS pixels, Apple points and Material units as identical
  or claim one numeric minimum applies everywhere.
- **Alternatives:** Larger hit areas, greater separation, redundant visible controls,
  single-pointer actions instead of gesture-only shortcuts.
- **Exceptions:** Current Apple accessibility table distinguishes default and minimum:
  iOS/iPadOS default 44×44pt, minimum 28×28pt; this is platform guidance, not WCAG AA.
  Check the current table for the actual platform instead of generalizing these numbers.
- **Accessibility:** Prefer comfortable target size over squeezing to a minimum;
  consider reach, enlarged text, VoiceOver and accessible alternatives.
- **Source / scope:** `apple-accessibility`, `wcag22` 2.5.8; platform guidance versus web standard.

## Follow the approved platform system

- **Principle / problem:** Familiar system behaviors reduce relearning and support
  user settings; arbitrary cross-platform copying can break expectations.
- **Use:** Apple native, Material-based or Fluent-based experiences when specified
  or established by the approved Figma system.
- **Do not use:** Apply all three systems at once, import their branding into a
  different product, or claim a component library alone guarantees accessibility.
- **Alternatives:** Approved local components/variables, native controls, or a
  coherent custom system validated against the task and platform.
- **Exceptions:** Brand expression may differ while interaction conventions persist.
  Fluent's published accessibility baseline mentions WCAG 2.1; evaluate requested
  work against current WCAG 2.2 rather than silently lowering the standard.
- **Accessibility:** Specify Dynamic Type/text scaling, semantic colors, high-contrast
  and reduced-motion behavior where relevant; verify actual available fonts/components.
- **Source / scope:** `apple-accessibility`, `material-adaptive`, `fluent-accessibility`.
