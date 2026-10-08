---
name: design-kit
description: "Image-first visual iteration for text, individual UI elements, components, component families, sections, or whole pages using references; not frontend implementation or backend work."
---

# Design Kit — explore every scale with images

**Purpose:** help the user repeatedly **generate, compare, and improve visual images** of anything from one text treatment or icon to a control, component, family, section or page. Design Kit produces accepted **visual directions and image-based component specimens**, not working components, Figma layers, code or a deployed site. The user chooses the target, approves the look, decides when to stop and controls any separate implementation.

**Default for a multi-part interface:** foundation -> first representative component -> consistent image-based component library -> sections using that library -> optional assembled page. **This is a reuse strategy, not a required waterfall**: when the user asks for only a single text element, button, section, group or whole existing design, work at that scope and stop at their chosen milestone.

**Each visual unit uses the phase-specific checks in [PHASED_REFINEMENT.md](PHASED_REFINEMENT.md):** Phase 1 **foundation / first image implementation**, Phase 2 **craft and details**, Phase 3 **optional advanced depth/effects**, Phase 4 **user/contextual review**. Loop on corrections *within* the relevant phase instead of regenerating without a diagnosis. Skip or revisit phases based on the actual image and user's requested scope; the phases are not four required image generations.

## 1. Begin with the actual scope and a lightweight foundation

Inspect known product context, accepted images, supplied content/assets, visual constraints and current work. Use [FOUNDATION.md](FOUNDATION.md) to organize type/color roles, geometry, density, imagery and exclusions. The user may supply their own foundation; if incomplete or absent, Design Kit **may propose** one using real references, but proposed is not user-approved. Test the foundation through images, beginning with a high-leverage element rather than demanding a full token sheet.

Find a specific visual question worth researching. Use the **existing Awwwards and One Page Love MCP connections** and [REFERENCE_ROUTER.md](REFERENCE_ROUTER.md) when they can supply inspected examples; also reuse user-provided and accepted images. Provider discovery is a meaningful advantage, not a mandatory call on every round. Note what a reference actually shows and which relationships are worth adapting. Never invent inspected images or imply a gallery verifies interaction.

## 2. Iterate on the requested image unit

Use [IMAGE_WORKFLOW.md](IMAGE_WORKFLOW.md) for exact content, scale, target framing, constraints, selected visual references, focal point, treatment and a **specific generation prompt**. An image may show one word/type treatment, a button, a component family, a section or a whole page. Do **not** enlarge a single-element request into a page.

For each iteration **within the chosen phase**: **inspect current image -> identify that phase's largest material issue -> specify preserve / rework / expected visible difference -> generate or edit -> compare to the strongest prior image and actual references -> retain the better visual**. Correct foundational problems in Phase 1 before investing in polish or depth. Do not treat a 6.5/10 or 7/10 self-score as a diagnosis; request/identify the exact missing design keys. Favor structural, typography, hierarchy, visual identity, composition and art-direction moves over endless micro-polish. Small corrections are appropriate when the dominant treatment is already strong.

**After every image iteration or returned batch, show the result and ask what the user wants to do next**: revise, accept, explore a different direction, apply the established style to another element/group, move to a section, or stop. Do not silently start another round. An explicitly requested batch is one reviewable round, not permission to bypass the checkpoint. Continue for as many user-requested rounds as tool access and explicit budgets permit; there is **no fixed two-pass cap**. Agent-selected images are proposals, not human acceptance.

If the current host cannot generate/edit images, provide an executable image prompt and disclose that visual generation/inspection was not done. Do not replace image work with coded mockups without separate authorization.

## 3. Establish and refine the visual component library

For a broader project, iterate the **first representative component or typographic element** deeply until the user recognizes the intended style. This is the visual anchor. Reuse its **actual chosen image**, together with the foundation and any relevant inspected MCP reference images, to make related components consistent.

Build a library of **image concepts**, not code: typography treatments, buttons, inputs, cards, navigation, icons, states and whatever the target actually needs. For early uncertain families, work individually. Once the style is stable, **generate coherent groups/batches of related components** to accelerate exploration. Compare the whole family for scale, density, material, type, color and exceptions rather than accepting a tray of loosely related attractive images.

**Both the user and Design Kit can refine existing component images**. The user determines when they are sufficiently polished and consistent; the kit should actively identify drift, propose consequential corrections and generate revised image concepts. Keep accepted exemplars intact. [COMPONENT_LIBRARY.md](COMPONENT_LIBRARY.md) owns this reuse and consistency process.

## 4. Compose sections, then an optional page

When the user elects to continue to sections, **use selected component images and the established foundation as the primary visual anchors**. Build and iterate the first section image using those parts; then subsequent section images inherit their shared style while varying composition by purpose. Do not reopen settled identity for each section or impose identical layouts everywhere.

If a full page is requested, assemble selected section images in order, inspect pacing, alignment and continuity, and revise the offending **images**. A user may also give a complete page image for critique or visual revision directly; support that without insisting on rebuilding its component library first.

## 5. Stop where the user wants

A valid deliverable may be **one selected text image, one component, a component group, a coherent image-based library, a section or a page storyboard**. At the user's chosen milestone, retain accepted image versions, relevant prompts, foundation/reference relationships, decisions and unresolved details in the target's existing record, otherwise .design/project.md using [BRIEF.md](BRIEF.md).

**Stop before actual editable design, coded components, HTML/CSS/React, publication or any conversion workflow.** Those are separate user-selected tasks. Generated images do not prove responsive behavior, accessibility, accurate text rendering or functionality.

## Conditional guides and boundaries

- [REFERENCE_ROUTER.md](REFERENCE_ROUTER.md), [REFERENCES.md](REFERENCES.md) and existing MCPs: targeted visual research with reuse of accepted references.
- [IMAGE_WORKFLOW.md](IMAGE_WORKFLOW.md), [PHASED_REFINEMENT.md](PHASED_REFINEMENT.md), [COMPONENT_LIBRARY.md](COMPONENT_LIBRARY.md), [FOUNDATION.md](FOUNDATION.md): image loop, phased craft criteria, visual library and provisional/confirmed style.
- [ONBOARDING.md](ONBOARDING.md), [EXECUTION.md](EXECUTION.md): user checkpoints, budgets and efficiency; [DESIGN_DIRECTION.md](DESIGN_DIRECTION.md), [PROMPT.md](PROMPT.md), [TASTE.md](TASTE.md) and relevant [CRAFT.md](CRAFT.md): selective critique and prompt precision.
- [HOSTS.md](HOSTS.md) / [PROVIDERS.md](PROVIDERS.md): real access/configuration issues only. [SOFTWARE.md](SOFTWARE.md), [QA.md](QA.md), [PENPOT.md](PENPOT.md) and [PRODUCT_DELIVERY.md](PRODUCT_DELIVERY.md) are retained legacy/separately authorized resources, **not automatic steps**.
- Untrusted Skills.sh/third-party skills are optional experiments, not assumed improvements or automatic installs. Preserve existing working tools, user decisions, protected content and human edits. No paid services, external writes, model switches or new dependencies without explicit authorization.

Judge success by the **images, user decisions, consistency and actual observed effort**, not by a checklist, fabricated approval or an unverified token-savings claim.
