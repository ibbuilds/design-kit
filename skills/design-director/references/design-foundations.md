# Design Foundations

For substantial net-new interfaces, complete landings, apps, dashboards and product
surfaces. The deliverable includes a coherent local system that constructs the design.
Local edits inspect nearby tokens/components and change only the implicated relationship;
they do not trigger ramps, a board, new page or library. An explicit system request
can use the relevant capability directly. Reuse an existing approved system where it
fits; a new surface does not authorize replacing shared foundations or human edits.

Product/user/brand constraints and inspected visual evidence inform creative direction;
that direction informs foundations, semantic components and composition. Keep this
dependency inside normal design work. Start with enough real system objects to build
the governing surface, then extend and revise them as the artifact exposes needs.
The primary model authors every design choice; helpers only calculate.

## Principles in composition

Use the implicated relationships, not a checklist or universal style:

| Design decision | Practical judgment |
|---|---|
| Hierarchy, emphasis and visual flow | What is first, second and actionable? Position, scale/proportion, weight, space, depth and contrast should guide that order; color alone cannot carry it. |
| Balance and composition | Place visual mass against meaningful negative space. Choose symmetry, asymmetry or deliberate imbalance from the thesis; centering everything is not neutral. |
| Alignment, proximity and Gestalt | Use shared axes, closeness, similarity, continuity and figure/ground to explain relationships. Group related content before adding containers; optically correct geometry that looks misaligned. |
| Rhythm, repetition and unity | Repeat visual laws while varying scale, density and content mode. Whitespace groups, focuses and paces; more emptiness is not automatically better. Avoid monotonous equal-weight sections. |
| Legibility, readability and density | Judge glyph recognition, paragraph measure/leading and scanning with real content at intended size. Preserve useful information density and grouping through grid changes. |
| Affordance, feedback and states | Make interaction discoverable and its outcome visible. Distinguish focus, selection, errors and progress without color alone; touch cannot depend on hover. |
| Systemic coherence and local expression | Shared type, color and spatial grammar can support open canvas, editorial tension, dense data or immersive imagery. Do not make every expressive moment a card or component. |

Current high-end work applies these enduring principles through relevant mechanisms:
flexible type, strong type/image tension, adaptive layouts, controlled grid breaking,
layering/occlusion, material relationships, precise iconography, purposeful shape and
motion. Elite [visual evidence](visual-references.md) informs cultural/art-direction
choices; [Design Authorities](experience.md) inform UX truth. Neither fashionable
effects nor authority defaults choose the style. Connect [spatial storytelling and
anti-slide diagnosis](craft/composition.md), [Product Presentation / assets](craft/assets.md)
and [finish](craft/finish.md) when relevant; do not duplicate their workflows.

## Color: authored palette and usable system

Create two related artifacts. The **basic palette** is a concise, visible expression
of the direction: necessary brand/accent anchors, background/surface and foregrounds,
with neutral/support anchors as needed. Choose them together through hue/temperature,
lightness, chroma, imagery/materiality, domain and emotional tone. Allocate color mass
and accent scarcity to hierarchy. Do not force every category or an unrelated rainbow.

The **advanced system** derives primitive neutral, brand and major accent ramps plus
the semantic roles actually used: canvas/surface/layers, primary/secondary/inverse text,
borders, actions and relevant states, focus and needed statuses. Semantic aliases point
to primitives; not every shade needs its own semantic role. Modes exist only for an
actual product requirement, never to manufacture dark-mode coverage.

Aim for about **20 tonal stops on key ramps**, with intentional monotonic lightness,
controlled chroma and stable hue. Use OKLCH/LCH reasoning rather than arbitrary RGB/HSL
interpolation; LAB is another legitimate perceptual space. Keep fewer stops when gamut,
perceptual redundancy or real use makes that better. Inspect rendered ramps and their
actual relationships for muddy middles, accidental neon and indistinguishable steps.
Mathematical validity does not establish palette authorship or aesthetic quality.

Optional dependency-free calculation, from the skill directory:

```sh
python -B scripts/color.py ramp --anchor '#3856A6' --name brand --stops 20
python -B scripts/color.py contrast '#FFFFFF' '#3856A6' --minimum 4.5
python -B scripts/color.py convert --oklch 0.6 0.18 260
```

The model supplies anchors and can set lightness endpoints/chroma. The helper returns
token-ready sRGB/HEX and measured OKLCH, preserving the anchor within the range. It
reduces out-of-gamut chroma at fixed lightness/hue, tapers chroma toward endpoints and
reports removed redundant stops. This simple deterministic mapping is not Leonardo's
algorithm, CSS gamut-mapping conformance or a palette recommendation. Contrast uses
the emitted opaque sRGB values; inspect actual alpha compositing, gradients, images
and states separately. No helper runs automatically for a local edit.

Accessibility shapes role selection: WCAG 2.2 AA text requires **4.5:1**, or **3:1**
for large text (at least 18pt regular / 14pt bold, approximately 24 / 18.67 CSS px).
Necessary UI identification/state cues and meaningful graphical parts need **3:1**
against adjacent colors. Pure decoration, logotypes and inactive controls have scoped
exceptions, not a blanket waiver for essential content. Color cannot be the only
carrier of meaning. Design visible, unobscured focus, clear targets and responsive
readable text; a Figma file cannot certify implemented WCAG conformance.

## Type, space and visual language

Use [typography](craft/typography.md) to author families and roles, then encode them as
styles consumed by screens. A preset font and four sizes do not constitute a system.
Specimens should show actual roles, weights and reading behavior, not a font catalogue.

Choose a rational spacing progression from grouping, content density and optical
relationships; 4/8-based scales are useful options, not laws. Distinguish internal
component spacing from layout gaps. Establish the used margins, columns/gutters,
content/max widths and section rhythm, with rules for reflow and priority at narrow
widths. Bind reusable spacing values where supported. A grid coordinates composition;
it does not force identical section geometry or suppress optical adjustments.

Systematize used shape/material relationships: corner and nested-radius logic, border
weights/treatments, surface/layer hierarchy, opacity and any real blur/shadow/elevation.
A flat design needs few such decisions. No unused radius/effect catalogue. Encode
relevant [asset direction](craft/assets.md) as icon geometry/stroke/fill/optical sizes,
image treatment/crops/masks and illustration language. Use [motion](craft/interaction-motion.md)
for needed duration/easing/physics and feedback character; foundations record the
chosen language without inventing motion or claiming that a still proves it.

## Semantic components

**Componentization follows semantic/systemic reuse, not current duplicate count.**
A recognizable UI entity whose content, state or size can change, which could serve
another surface, or whose central definition a future designer would reasonably
expect must be a component in substantial interface work, even with exactly one use.
This covers product-relevant controls, navigation, cards/rows, tables, panels, feedback
and overlays, plus meaningful editorial/marketing modules. Derive the inventory from
the actual product; do not prebuild a generic kit. Pure layout wrappers, unique hero
compositions and one-off artwork need no component unless they acquire system identity.

Construct flexible Auto Layout and text behavior, meaningful properties and necessary
states. Separate axes such as Type, Size, State, Emphasis or Selection when useful;
do not bury every combination in one Style name or create an exhaustive Cartesian
product. Expose text, optional content and swaps where appropriate. Include only states
the interaction needs (e.g. focus, disabled, loading, error), with clear distinctions.
Slots may help composable content only when current API/bridge support is verified;
they are not a prerequisite or a reason to invent methods.

Once the main component exists, **screens use instances**, including single-use
controls. Desktop and mobile share semantic component sources, tokens and type roles.
Adapt layout, density, navigation, hierarchy, type settings, interaction and crops;
use responsive variants/properties where needed, not raw mobile redraws. Inspect long
labels/content and resizing for clipping, collisions and broken nested layout.

## Figma system objects

Use the existing [transport and authorization](figma.md), preserving [placement and
benchmark conventions](figma-create.md). Organize a compact Foundations / Components
area separately from Design, with palette, ramps/semantic swatches, type specimens and
used layout/visual-language samples. Main components belong in a named section/frame.
This is a working system, not a prose board or case study. Variables/styles are
file-scoped: inspect existing definitions, namespace task-local additions and avoid
altering unrelated consumers. Swatches alone never substitute for definitions.

Through the supported Plugin API, create variables in collections with
`figma.variables.createVariable(name, collection, type)`; set primitive mode values
with `setValueForMode`, and semantic values using `createVariableAlias(primitive)`.
Use the returned bound paint from `setBoundVariableForPaint` in the node's fills/strokes;
bind supported scalar fields with `node.setBoundVariable`. Preserve semantic names
(e.g. `color/brand/01` versus `action/primary`) and relevant mode mapping.

Create text styles with `figma.createTextStyle()` and effect styles when used with
`figma.createEffectStyle()`; load the actual font first and apply styles through
`setTextStyleIdAsync` / `setEffectStyleIdAsync` on supported nodes. Use component
creation, `combineAsVariants`, component properties and `createInstance()` for reusable
UI. Batch bounded related writes; inspect definitions and bindings after mutation.
Do not infer successful binding from equal rendered colors. Discover actual schemas;
if a capability is unavailable, use an appropriate supported style/property fallback
and state the missing propagation behavior instead of pretending swatches are tokens.

## Refine the system and artifact

Inspect fresh real renders of composed primary/responsive surfaces and the relevant
system specimens. Trace representative semantic controls to main components, paints
to variables/aliases and text to styles. Catch raw recreated controls, unnecessary
desktop/mobile forks and local overrides that silently sever shared decisions. When
an authorized brand, type, padding or radius revision is needed, change its definition
and verify affected uses actually update. Do not perturb unrelated work to demonstrate
propagation. Correct a weak foundation and propagate; no early token is immutable.

Judge whether systemization made the design generic or removed an expressive moment.
Refine the system and composition together until no material gap remains, subject to
[human feedback and stopping](quality.md). This is normal design judgment, not an
evaluator, component quota or user-visible approval sequence.

## Evidence and scope

Verified 2026-09-05. Principles, palette authorship, ramp targets and family limits
above are contextual design judgments, not standards or proven quality guarantees.
Existing visual sources and Design Authorities keep their separate scopes.

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): normative 1.4.1, 1.4.3, 1.4.11 and
  applicable focus/resize/reflow requirements; role exceptions must be respected.
- [CSS Color 4](https://www.w3.org/TR/css-color-4/): color-space/conversion reference
  (Candidate Recommendation Draft), not evidence that a ramp is attractive.
- [Original Oklab derivation](https://bottosson.github.io/posts/oklab/): D65 conversion
  matrices used by the helper; original technical work, not a visual-style authority.
- [Figma variables](https://developers.figma.com/docs/plugins/api/figma-variables/),
  [Plugin API](https://developers.figma.com/docs/plugins/api/figma/) and
  [shared node properties](https://developers.figma.com/docs/plugins/api/node-properties/)
  / [text nodes](https://developers.figma.com/docs/plugins/api/TextNode/):
  system-object capabilities; document/runtime presence does not prove a particular
  write succeeded. Read-only local bridge capability checks are recorded in development
  validation; file access, fonts and optional API fields remain environment-dependent.
