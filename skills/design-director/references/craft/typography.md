# Typography craft

Use when type carries hierarchy, reading, identity, density, or a diagnosed defect.
Typography is a relationship among content, roles, measures, spacing, and rendering;
a font name or scale alone is not a system.

## Build the hierarchy

- Start from content roles and reading order. Give distinct treatment only to roles
  that need distinct recognition; repeated roles should behave consistently.
- Establish a body setting that works with realistic content, then place display,
  title, heading, label, metadata, code, and numeric roles around it as needed.
- Use size, weight, width, case, color, position, and space deliberately. Do not ask
  every variable to signal the same distinction.
- Make hierarchy legible in grayscale and at a glance before relying on accent color.
- In data work, align comparable numbers, preserve signs/units, and consider tabular
  figures when the available font and task support them.

## Set and inspect

- Judge type in the actual frame at intended scale. Check family/face availability,
  line breaking, truncation, text resizing, localization risk, and fallback behavior.
- Tune measure and leading together. Short labels, long-form prose, dense tables, and
  expressive headlines need different relationships; no universal character count,
  modular scale, or line-height ratio governs all of them.
- Check rag, widows/orphans where controllable, awkward proper-name breaks, heading
  attachment to following content, and the visual weight of punctuation and numerals.
- Use tracking sparingly and optically. All-caps labels may need it; body text rarely
  benefits from broad tracking. Use manual line breaks only when content stability
  and editorial intent justify them.
- Preserve semantic emphasis and accessible text alternatives. A Figma specimen
  cannot prove platform text scaling, font loading, or assistive-technology output.

## Diagnose

| Observed failure | Targeted intervention → check |
|---|---|
| Heading, label and body read as peers | Separate roles through one or two meaningful contrasts; inspect the reading order before adding more sizes. |
| Headline wraps into an accidental shape on mobile | Recompose measure, size and editorial breaks at mobile width; check both rag and the image/CTA relationship. |
| An impressive face makes long copy tiring | Reserve expression for display and tune the reading face/measure/leading; inspect real paragraphs, not sample words. |
| Tiny uppercase labels carry essential decisions | Promote functional information to readable type; verify at actual viewport scale and contrast. |

Name the relationship that fails: two levels read as peers, a label overwhelms its
value, a headline shape damages composition, a measure slows reading, or a typeface
contradicts the intended voice. Change the smallest set of related roles, then inspect
the full hierarchy and representative extremes. Do not replace an approved typeface
because another font is fashionable, or call conventional typography unoriginal
when convention serves the task.

Guidance synthesized from `wcag22`, `apple-accessibility`, and the current Carbon
typography guidance recorded in `sources.json`; platform examples are scoped evidence,
not universal aesthetic rules.
