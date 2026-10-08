# Building a reusable visual component library with images

This is an **image-based exploration library**, not a collection of coded components, Figma components or a final design system implementation. The library consists of selected **image specimens**, foundation decisions and relationships that can be reused when generating related components and eventual section images.

This is the **default route when designing a multi-part interface**, not a requirement for a single-element request. Each component/family can move through [PHASED_REFINEMENT.md](PHASED_REFINEMENT.md)'s foundational image, craft/detail, optional advanced finish and final user review. **Do not use Phase 3 gloss to hide a Phase 1 problem**. [SKILL.md](SKILL.md) controls the task scope and [IMAGE_WORKFLOW.md](IMAGE_WORKFLOW.md) governs each iteration.

## 1. Choose one high-leverage exemplar

Choose the **first visual unit** to settle important style questions: a typographic headline, a button/control, a content card, navigation or a component specified by the user. Its exact identity depends on the project; do not force every project to begin with a button.

If the foundation is missing, Design Kit may propose a **provisional** typography/color/surface direction using actual supplied or MCP reference imagery. Label it as proposed. Iterate substantially on the first exemplar's **image** through relevant phase-specific correction loops until the user selects or delegates a stable direction. This can require many rounds. Preserve the strongest image and record its visible relationships (the **style DNA**): text hierarchy, color/emphasis, geometry, spacing/density, icon/image treatment and exclusions.

A selected exemplar does not imply the whole library is done or that incidental generated artifacts are confirmed tokens.

## 2. Extend individually, then in groups

Build only the components the product actually needs; the user may name the set. Representative families include:

- **Typography / visual primitives:** headings, labels, body treatment, icons, badges, borders and surface treatments.
- **Actions / inputs:** buttons, links, text fields, selectors, toggles, filters, search and relevant states.
- **Content / navigation:** cards, list rows, tables, tabs, menus, nav bars, banners and overlays.
- **Product-specific elements:** charts, media frames, pricing blocks, progress, unusual controls or bespoke motifs.

First transfer the accepted style to one contrasting component and compare for visual coherence. If family relationships are no longer open, **generate a group of related components in one image batch/comparison sheet** rather than rerunning the full exploration for each sibling. A batch is still an image-generation round and requires a user feedback checkpoint afterward.

Keep variants truthful: default, selected, disabled, error, hover or dense examples are visual concepts, **not proof of working states**. A single image that depicts many components may be useful for comparison; preserve the individual accepted images or explicit version IDs when they exist. Do not infer exact pixel tokens from a generated composite.

## 3. Library consistency pass — user or Design Kit

After the user has enough component images, show a compact **visual library board** at comparable scale. Inspect the entire family for:

- Consistent typography, contrast, spacing density, material, corner/edge language and icon weight.
- Useful exceptions and distinct hierarchy across primary, secondary and tertiary components.
- Coherence between text-only details and complex controls; consistency across state examples.
- Obvious outliers that came from image-generation drift or unrelated references.

**The user may tweak every component; Design Kit can also propose and generate those refinements.** Treat the library as settled only to the extent the user actually accepts or delegates. Correct material inconsistencies in the relevant component images first. A technically consistent set can still be aesthetically weak: revisit the exemplar/foundation if the underlying style is wrong, rather than polishing dozens of descendants.

At the end of each image correction round, **ask whether to revise more, accept, generate related components, proceed to sections, or stop**.

## 4. Reuse the library for sections

Once the relevant components are visually consistent *enough for the user's chosen milestone*, construct **section images**, not a coded page. Include selected component images and foundation decisions as actual visual references in the next prompt when supported. The first section should feel quicker to resolve because repeated style questions were already settled; this is a hypothesis, **not guaranteed savings**.

Sections still need composition, storytelling and art direction of their own. Vary structure with purpose while maintaining accepted component proportions, materials and type relationships. Compare the new section against the component board; revisit specific image units if the scene contradicts an approved component.

Only assemble a page if requested. A user can stop at any component, at the library, at one section or with a whole page.

## 5. Compact library record

Use the target project record or [BRIEF.md](BRIEF.md). Track, for each relevant unit:

| Attribute | Record |
| --- | --- |
| Family and component | e.g. actions / primary button |
| Inputs | accepted foundation version, exemplar image and inspected source relationship |
| Output | actual image path/ID and version, including generated group where useful |
| Status | proposed, agent-selected, user-accepted, reopened |
| Style relationships | what is shared vs deliberately different |
| Open fixes | remaining image mismatches or states |
| Next action | iterate, batch siblings, section, or stop |

Preserve actual user decisions and strongest images; do not archive every failed prompt or invent files/approval. Reuse a short accepted style summary and actual reference images rather than copying the full research history into every generation.

## Example: moving from slow exploration to a batch

**Exploration:** "Generate a single primary-button visual specimen with the approved serif headline accent, deep neutral surface and quiet copper focus color. Keep the actual label. Explore a decisive, unusually wide silhouette versus a compact utility silhouette. Use the inspected control reference for border weight only. Show at 1:1 component scale."

**User-selected exemplar:** retain the chosen button image and concrete type/shape/contrast relationships.

**Batch after style is settled:** "Using the attached accepted primary-button specimen and confirmed foundation as the visual anchors, create one comparison image of secondary button, icon-only action, text link and disabled state. Preserve the same control weight, typography and accent role. Show meaningful priority differences without inventing a new visual language."

Review the resulting **images**, ask the user what to change or accept, and save only the selected versions. No final editable design or code is implied.
