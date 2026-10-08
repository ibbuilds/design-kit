# Phase-led image refinement — choose the right kind of improvement

This is the **3–4-phase visual-image protocol** for [SKILL.md](SKILL.md). It works on a text treatment, symbol, button, any component, an image-based component family, a section, or a whole page. The word **implementation** in Phase 1 means *establishing the concept in an image*, not writing working UI or exporting editable Figma components.

For a multi-part project, use it on the first high-leverage component, reuse that accepted style in related component images, and then apply it to each requested section. For an existing nearly-finished image, **start at the phase with the real deficit**; never force the user through earlier phases if those decisions are already accepted.

## Four phases, not four automatic generations

| Phase | Focus / question | What is in scope | Evidence to move on |
| --- | --- | --- | --- |
| **1. Foundation & first visual implementation** | *Is this the right fundamental design?* | Exact content and purpose, essential composition, dimensions, typographic roles and scale, base color roles, shape/radius, spacing/density, hierarchy, required elements, intended style. Explore substantially different approaches if direction is open. | Strong concept with accurate source content, legible basic hierarchy, consistent foundation and no major structural or aesthetic mismatch |
| **2. Craft & surface details** | *Does the chosen concept feel deliberate and refined?* | Optical spacing/alignment, text wraps and weight, border width/outline, icons, control proportions, color tuning, gradients and materials where appropriate, coherent visual states, crop quality and family consistency. | The details visibly reinforce hierarchy, identity and consistency rather than disguising a weak foundation |
| **3. Advanced depth & expressive finish (optional)** | *Would a higher-order treatment actually add value?* | Purposeful lighting, shadow hierarchy, material layering, subtle texture, atmospheric gradients, reflections and glow where justified; image variants can **depict** hover/pressed/focus or motion intent. | An observable contribution at normal viewing size with intact legibility and accepted visual identity; **skip if the look is deliberately flat, minimal or already strong** |
| **4. User decision & contextual review** | *Does the user want to accept, change or stop?* | Compare accepted references and strongest retained variants; look at actual intended scale and context, related components, adjacent sections or page sequence if requested; resolve drift, record acceptance, or point to the phase needing rework. | User accepts/delegates the result, selects another improvement round or stops at their chosen milestone |

**Phase 4 is not an excuse to wait until the end for feedback.** At the end of **every generated image round or returned batch in Phases 1–3**, show the image(s), state the relevant phase-specific change and **ask the user** whether to revise, accept this phase/direction, try an alternative, revisit a prior phase, proceed or stop. Phase 4 is a distinct **final/contextual** user review, not an automatic fourth image generation.

**Phases are lenses, not gates that manufacture work.** The default progression for a new unit is 1 -> 2 -> optional 3 -> 4. If requested by the user, a single text treatment may finish at Phase 1 or 2; an existing visually strong image may enter Phase 2 or 3; a component group may be reviewed together. Avoid mandatory full-page work for a small item. User-approved decisions can carry across phases, but an obvious structural problem discovered during polish sends the work **back to Phase 1**, not into more effects.

## The correction loop inside each phase

1. **Name the phase and one visual problem.** Ground it in the actual image, actual content, selected exemplar(s), and, when helpful, the **inspected Awwwards / One Page Love reference image**. Don't use a generated 7/10 score as diagnosis.
2. **Identify the missing design keys.** Specify *keep / change / expected visible difference*, choosing the **2–4 consequential variables** appropriate to this phase. Do not merely ask to "make it premium" or "add more detail".
3. **Generate/edit one visual round**, or a user-requested group of alternatives. Keep exact words separately; image generation may distort them. Use the actual chosen exemplar as an image input if the host supports it.
4. **Compare with a relevant previous version** at equivalent content, crop and scale. Check the current phase's criteria *and* that earlier accepted decisions did not regress. A newly added gradient can reduce contrast, and a beautiful shadow can muddy hierarchy.
5. **Show, assess briefly and ask the user what next.** Repeat the same phase with a different *testable* change, accept it and move on, reopen an earlier phase, or stop. Never silently start another image round. The user can request any number within real tool and cost limits.

If several rounds do not produce a *material visible gain*, diagnose the missing evidence or wrong-level intervention; do **not** assume additional generations inherently raise quality. Retain the stronger earlier image. No arbitrary numeric score, round quota or compulsory effects threshold defines success.

## Adapt the phase checks to the unit

| Unit | Phase 1: core | Phase 2: craft | Phase 3: advanced (only if relevant) | Phase 4: context |
| --- | --- | --- | --- | --- |
| **Word / text** | Exact words, reading hierarchy, type role, basic scale | Tracking, kerning/optical spacing, wraps, baseline and contrast | Optional lettering/texture treatment; don't make text illegible with 3D/depth | Legibility at real use size and user's decision |
| **Button / control** | Label, purpose, size, shape/radius, color roles and priority | Stroke, padding, corner consistency, icon-label balance, precise fill/gradient, visible state concepts | Purposeful shadow/elevation, highlight, restrained material; depict pressed/hover states only as stills | Compare with sibling controls and user's desired feel |
| **Card / component family** | Content anatomy, grouping, size/density, shared foundation | Alignment, borders/surfaces, hierarchy, state variation, family coherence | Deliberate layering/visual emphasis for priority | Inspect comparison board; user selects or revises |
| **Section** | Content, layout/composition, focal point, selected component imagery | Pacing, type/image crops, spacing transitions and surface consistency | Optional depth/atmosphere serving the story | Compare with neighboring sections; accept/return |
| **Page** | Narrative order, large-scale hierarchy, component/style continuity | Rhythm, transitions, detail consistency and content density | Only purposeful page-level material/art direction effects | Review visual sequence at intended widths; user decides |

### Example: one button

- **Phase 1, option A vs B:** "Generate a static visual of the 'Continue' button at component scale using the user-proposed warm-neutral palette. Compare a broad pill versus a more restrained rounded rectangle. Keep the exact label and clear primary-action priority; don't add gloss yet."
- **Correct Phase 1:** "Keep the rounded-rectangle direction, make its label less timid and correct width-to-height proportion. Preserve neutral fill and accent role; re-generate and compare." Ask the user after the image result.
- **Phase 2:** "Keep the accepted silhouette and hierarchy. Adjust the border weight, inner padding, optical label position and subtle warm-to-cool surface transition together. Render the actual image and compare against the previous accepted version." Ask again.
- **Phase 3, only if useful:** "Try a shallow contact shadow and slight edge highlight to communicate a raised primary control without gloss or neon. Provide a flat alternative for comparison. These are still images, not interactive behavior." Ask again.
- **Phase 4:** "Show the best candidate at intended scale alongside the accepted sibling controls; ask the user to accept, rework a named phase or stop." Don't claim that user approval alone proves functional accessibility.

## Reference use and guardrails

Use the current Awwwards and One Page Love MCP workflow in [REFERENCE_ROUTER.md](REFERENCE_ROUTER.md) **selectively by phase**: Phase 1 usually benefits from overall style/composition; Phase 2 from real surface/type/crop exemplars; Phase 3 from actual inspected material/effect treatments. If accepted images already resolve that question, **reuse rather than re-search**. A provider screenshot is visual evidence, not proof of interaction, exact CSS, conversion or usability.

Apple's [design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles) emphasize purpose, clarity and craft rather than decoration; its [materials guidance](https://developer.apple.com/design/human-interface-guidelines/materials) says visual depth should strengthen hierarchy without obscuring content. The [Nielsen Norman Group iterative design discussion](https://www.nngroup.com/articles/parallel-and-iterative-design/) grounds revisions in evaluation rather than repetition alone. These are **informative design principles**, not evidence this specific workflow improves aesthetic quality.

Treat visual legibility and contrast seriously; the [WCAG 2.2 contrast criterion](https://www.w3.org/TR/WCAG22/#contrast-minimum) is relevant to implemented UIs, but **a static generated image cannot demonstrate WCAG conformance** or functioning hover, focus, motion or click behavior. If source text or color values are unavailable, mark checks unverified rather than fabricating measurements.

Store only useful phase, image IDs, inspected source relationship, strongest version, user feedback and next authorized action in the target's existing design record ([BRIEF.md](BRIEF.md)). **Design Kit stops at the user's chosen visual-image milestone.**
