# Specific image prompts for any visual scale

Use [IMAGE_WORKFLOW.md](IMAGE_WORKFLOW.md) to expand **image-generation** prompts, never mandatory frontend instructions. Include the requested target, content, scale, provisional/confirmed foundation, actually inspected reference image, explicit style anchor, protected elements and visible expected change.

## Template

> Generate an **image** of [text / icon / component / component group / family / section / page] for [known product] at [scale or aspect]. The visual job is [specific purpose]. Use [accepted or explicitly proposed typography/color/geometry/density]. Match the selected [actual component/library/section image] in [stable relationships]. Adapt [actually inspected MCP reference] only for [observed useful trait]. Show [exact content, relevant components/states, crop/visual hierarchy]. **Keep** [locked style/content]. **Rework** [material weak relationship] so [expected visible difference]. Avoid [specific unwanted patterns]. This is a static image concept, not working UI.

## Write prompts for the active refinement phase

Use [PHASED_REFINEMENT.md](PHASED_REFINEMENT.md) alongside the component-first image process:

- **Phase 1 — foundation / visual implementation:** describe the underlying idea, exact copy, function, hierarchy, size, shape/radius, base color and proportions. When direction is unknown, offer meaningfully distinct approaches rather than fine polish.
- **Phase 2 — craft / surface details:** preserve the selected foundation; specify optical alignment, control stroke/outline, typographic spacing, surface transitions, gradients or states *only where appropriate*. Re-render and compare details at real scale.
- **Phase 3 — advanced finish (optional):** explain precisely what an effect would contribute (e.g., shallow elevation clarifying priority). Request an unadorned comparison if helpful; no automatic gloss, glow or elaborate gradient.
- **Phase 4 — user/contextual review:** show best image, previous accepted reference and related component/section context. **Ask** what is missing, which phase to revisit or whether to stop; this phase does not require a new image.

Corrections within *each* phase use a **keep / rework / expected difference** prompt; show every resulting image and wait for user feedback before another round. The same phase logic applies to typography, component groups, sections and page images without forcing extra scope.

## Examples

**Text only:** Generate a readable image specimen of the headline "Explore ideas" on the accepted neutral surface. Compare a compact modern geometric setting against a taller editorial setting. Preserve the exact words and don't add a hero section. Keep source copy outside the image, because generative imagery can misspell it.

**First component:** Generate images of one primary button labelled "Continue". Explore proportion, tactile edge/surface and typographic weight, using the inspected reference only for the observed control emphasis. Do not invent a whole website.

**Component batch after the first exemplar is selected:** Using the **attached accepted primary-button image** and the foundation, generate a coherent comparison sheet of secondary button, icon-only action, link and disabled state. Preserve accepted type, contrast, border/material and density while expressing distinct priority.

**Section after library:** Compose a pricing-section image using the selected typography, button and card specimen images. Preserve their style; improve relative emphasis and reading order for the real content.

A submitted full-page image can also be revised **directly**, without a compulsory component-by-component reconstruction.

After every image round, **show and ask the user** whether to refine, accept, switch direction, generate siblings, advance or stop. A reference URL alone is not evidence the model saw the image. [REFERENCE_ROUTER.md](REFERENCE_ROUTER.md) owns Awwwards/One Page Love discovery and provenance; third-party prompt skills are optional, unproven experiments.
