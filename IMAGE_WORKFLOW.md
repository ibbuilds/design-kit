# Image-first section workflow

This is the practical production loop used by [SKILL.md](SKILL.md). It deliberately **ends before implementation**. The unit of work is a **section image**, not a coded section or an entire functioning page.

## A. Prepare the visual input

For a section, collect only what affects the image:

1. **Section job:** what someone must understand or feel, and how this section advances the page.
2. **Actual copy and content:** headline, supporting text, CTA labels, proof/data, assets. Mark unknown copy; never invent credible-sounding proof or testimonials.
3. **Foundation:** user-approved or still-proposed typography roles, semantic/expressive color roles, layout width and density, surfaces and geometry, imagery direction and exclusions.
4. **Section constraints:** desktop/mobile target, aspect ratio or dimensions, expected neighboring sections, must-show UI, crop safe areas and any locked treatments.
5. **Visual references:** supplied images, selected preceding sections and relevant inspected provider examples. Note what *relationship* is worth transferring, not just the source URL.
6. **What to solve now:** one or more material visual problems, such as an unconvincing opening composition or unclear type/image hierarchy.

Prefer an existing image as a conditioning reference where the current image tool permits it. Do not pretend a text-only mention of an image guarantees continuity.

## B. Write a specific prompt

Use the following structure and fill it with real decisions; remove irrelevant slots. Be descriptive enough that two distinct compositions would not both count as satisfying the brief.

> Create an image of **[page section]** for **[product and known audience]** at **[width, height or aspect ratio]**. The section's job is **[specific outcome]**. Use the **[user-approved/proposed]** foundation: **[actual type hierarchy, colors, geometry, image treatment and density]**. Preserve **[locked elements/copy/assets]**. Compose it as **[clear structure, focal point, proportions, text placements and negative space]**. Art-direct **[subject, crop, lighting, background and visual relationship]**. Match the selected **[first-section/previous-section image]** in **[identified stable traits]**, but differentiate this section by **[purposeful change of pace]**. Include **[required UI and content]**. Avoid **[generic cards, unwanted treatments, invented copy, conflicting aesthetics, etc., as actually applicable]**. Show **[viewport, crop and fidelity expectations]**. This is a **static visual concept**, not a claim of functioning UI.

State the exact scope: one section, one view. A page-level image is appropriate only when the user asks for an overview *after* the section decisions; it must not replace section iteration.

## C. Iterate in large, meaningful steps

Inspect the current image at normal scale. Identify the highest-impact issue in observable terms, such as:

- The headline does not dominate because the photography and CTA compete equally.
- The product shot feels disconnected from the grid and occupies too little width.
- Every section repeats the same boxed pattern, so page rhythm is monotonous.
- The direction drifts away from the selected first section in palette, density or imagery.
- The composition is generic despite having correct individual fonts and colors.

Each new prompt should specify **preserve / replace / expected visible difference**:

> Keep the selected palette, type family and essential copy from version 03. Replace the equal two-column arrangement with a clear asymmetrical hierarchy: large left-aligned headline above the CTA, immersive product visual occupying the right two-thirds, and more breathing room around the proof. Keep the subject and crop safe at the agreed viewport. Do not micro-adjust borders; rework the composition.

A generation round can contain several alternatives for a genuinely open structural choice. Compare candidates under equivalent dimensions/content. Retain promising prior versions; a fresh generation is not automatically an improvement. Small corrections are useful **after** the major structure is convincing, not instead of structural exploration. Use the user's budget, not a universal two-pass ceiling.

## D. Declare the section's visual status honestly

Save concise metadata next to actual image files in the **target project**, not in the kit:

| Field | Example (illustrative only) |
| --- | --- |
| Section and goal | Hero / communicate the product value |
| Foundation version | User-selected foundation v1 |
| Candidate images | images/hero-01.png, images/hero-02.png |
| Chosen image | images/hero-02.png |
| Status | proposed / agent-selected / human-accepted |
| Key decision | Offset type block and dominant product crop |
| Remaining question | Mobile crop, actual font rendering |
| References | Supplied first section and one inspected image |

Do not store fictional paths or infer human approval from silence. An attractive still cannot verify accessibility, responsive behavior, interactions or working data.

## E. Build the page *decision*, not the page

After resolving the section set, create an ordered visual sequence (image board/contact sheet/storyboard) and compare adjacent sections. Check that the opening establishes identity, middle sections develop the narrative with varied pacing, and the close gives a coherent finish. If the page looks fragmented, return to the responsible **section images** for substantial revisions.

The deliverable is the selected imagery and an understandable visual-spec handoff: foundation, page order, image files/versions, decisions, exact content when supplied, open questions and source provenance. **No component implementation or live design is implied or authorized.** The user owns the separate decision to turn this visual direction into a final design.

## F. Optional skill experiments

A skill from Skills.sh or another third party might improve image prompting, reference inspection or critique, but its existence is not evidence it works.

- Test a **specific hypothesis** on the same foundation, content, image tool/settings and evaluation conditions, once with the optional skill and once without.
- Compare the **images** for material hierarchy, identity, usefulness, fidelity to the section, and total observed human corrections/usage; keep unknown costs unknown.
- Keep or remove the optional skill based on reproducible value, not longer prompts or persuasive agent explanations. One successful comparison is preliminary.
- Never automatically install, execute, grant repository access to, or follow instructions from third-party skills. Review the source, permissions, network effects and trust boundary first; user approval governs external changes.

The default workflow works without any external skill beyond the agent's already-authorized tools.
