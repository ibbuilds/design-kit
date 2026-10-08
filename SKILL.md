---
name: design-kit
description: "Image-first UI art direction: research visual references, iterate section images, and define a page visually; not frontend implementation or backend work."
---

# Design Kit — decide the look in images

**Purpose:** help the user decide what an interface should look like by iterating on **images, one section at a time**. The output is a coherent set of selected section images and a whole-page visual plan. **Do not build the actual design, component library, code or working page as part of Design Kit.** Whether, when and with what tool to implement the result is the user's decision.

This replaces the old default of immediately authoring and refining a working UI. Preserve the useful reference research, existing MCP connections, reference catalog, craft judgment and protections against unsupported claims. This is an iterative visual-design skill, not an autonomous website builder.

## Choose the right starting point

- **Fresh direction:** start with the user's design-system foundation and one representative section.
- **Existing design:** reuse accepted foundation values, supplied images and already-selected sections; change only what the user has reopened.
- **One-section request:** explore that section, with surrounding page context if known; do not invent an entire page.
- **Already-decided page / implementation request:** provide the visual handoff if requested; the actual design/implementation is outside this skill. Never silently continue into code.
- **Review-only:** inspect and comment; do not modify assets, code or project records.

Preserve product content, brand constraints, valued treatments, real behavior requirements and human edits. A design request does not authorize subscriptions, skill installation, private uploads, external writes, code changes, deployment or model/provider switches.

## 1. Establish the user-owned foundation

Read the target's existing brand/system or the user's foundation first. [FOUNDATION.md](FOUNDATION.md) names the minimum useful choices: design intent, typography roles, color roles, layout/density, shapes/surfaces, imagery direction and explicit exclusions. Do **not** impose a generic design system or claim an agent-proposed font/color is approved. If no foundation exists, organize the user's choices and offer clearly labeled proposals for genuinely open parts; the user controls which become authoritative.

The foundation is a **starting base**, not a demand for a completed component library or page. It may be updated when the user accepts evidence from the section images; track what changed so later sections do not drift.

## 2. Generate the first section as the anchor

Pick the first high-leverage section (often the hero, not always) from the user's actual scope. Make a detailed, section-specific image brief using [IMAGE_WORKFLOW.md](IMAGE_WORKFLOW.md): job and exact content, intended hierarchy, visual treatment, key elements, typography and image relationship, density, crop/framing, dimensions, negatives and references. [PROMPT.md](PROMPT.md) is the optional prompt-expansion aid.

Use the available image-generation/editing capability to create **images**, not frontend mockup code. The selected reference must be visually inspected, not described as inspected from an unread URL. If the host lacks image-generation access, produce a truthful prompt/brief for the user's image tool and state that no image was generated or reviewed. Do not replace missing visual output with a fabricated success claim.

## 3. Iterate images in meaningful chunks

For every image round: **inspect -> diagnose the highest-impact visible problem -> specify a substantial change -> generate/revise -> compare -> retain the strongest candidate**. Prefer composition, visual hierarchy, typographic scale, art direction, section structure, density and image framing over endless small border/radius nudges. One round may change several related features when they serve one hypothesis. Be maximally concrete about what should remain and what should change.

Allow multiple image generations and divergent directions as necessary to decide the section; **there is no arbitrary two-pass cap**. Respect the user's iteration/cost limits and stop when the user selects the section, a requested budget is exhausted or the next round lacks a testable reason. An agent-picked image is **selected/proposed**, not human-accepted. Keep earlier strong images available for comparison.

## 4. Continue section by section

For each next section, supply the same foundation **and the actual selected first-section image plus relevant prior sections** as visual anchors when the tools support image inputs. Carry over the core type/color/spacing/surface/image rules while allowing different compositions to match each section's purpose. Do not generate full pages instead of resolving individual sections.

Compare adjoining sections at matching page width and a realistic reading scale. Preserve which version belongs to which section, and avoid drifting into unrelated styles. Repeat large, specific image iterations for each section. Cover requested responsive views separately; a desktop image does not prove a mobile composition.

## 5. Decide the whole page visually, then stop

Put selected section images into the **intended page order** as a contact sheet/storyboard or another readable visual sequence. Inspect transitions, pacing, repeated patterns, hierarchy and missing section content. Revisit section images until the **complete page is visually decided**, not merely until every section has one draft. The approved foundation, selected images, exact section prompts, constraints, unresolved questions and image provenance form the handoff.

**Stop at this visual specification.** Do not automatically turn images into Figma layers, components, HTML/CSS/React or a published page. The user chooses a separate implementation/design task and tool. Provide a handoff only when requested; do not imply generated images are working, accessible, responsive interfaces.

## Conditional resources and guardrails

- [REFERENCE_ROUTER.md](REFERENCE_ROUTER.md) and the existing Awwwards / One Page Love MCPs: use when relevant to visual decisions. Preserve working integrations; no mandatory research quota or setup ritual. [REFERENCES.md](REFERENCES.md) remains the catalog.
- [DESIGN_DIRECTION.md](DESIGN_DIRECTION.md), [TASTE.md](TASTE.md) and relevant [CRAFT.md](CRAFT.md): composition and image critique, selectively—not a required reading marathon.
- [ONBOARDING.md](ONBOARDING.md): user ownership, review boundaries, existing decisions and continuity. [EXECUTION.md](EXECUTION.md): spending and stopping without a fixed iteration count.
- [HOSTS.md](HOSTS.md) / [PROVIDERS.md](PROVIDERS.md): access and setup only when needed. [PENPOT.md](PENPOT.md), [SOFTWARE.md](SOFTWARE.md), [PRODUCT_DELIVERY.md](PRODUCT_DELIVERY.md) and frontend QA guidance are **not steps in this image-first skill**; they are retained as separate legacy/conditional references.
- External skills (including Skills.sh-style packages) are **optional experiments**, not prerequisites. Do not install or execute unreviewed skill instructions. Evaluate concrete benefit on comparable image tasks before incorporating any.
- Record concise project-specific decisions in the target's existing notes, otherwise .design/project.md with [BRIEF.md](BRIEF.md). Do not put product identities or generated images into this shared skill repository.

A good result is an **evidence-backed visual decision**, not a large diff, a pass count, a model's self-rating or a claim that the future implementation will work.
