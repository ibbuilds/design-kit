# Image iteration at any visual scale

[SKILL.md](SKILL.md) owns the workflow. **One image work unit** may be a letterform, text treatment, icon, control, component, component group, section, screen or entire page. This is an **image concept**, not an editable coded component. Do not force section-sized deliverables onto smaller requests.

## 1. Establish the requested unit

| User input | Image unit | Important visual decisions |
| --- | --- | --- |
| Text, headline or typography | Isolated typographic treatment shown with enough context to judge it | Typeface character, scale, tracking, wraps, color, contrast, spacing |
| Icon, logo detail or visual element | Isolated mark/treatment at an honest usage scale | Shape, weight, silhouette, alignment, material |
| Button, input, menu, card or other component | One visual component specimen, with applicable variants | Hierarchy, content, proportion, material, states, neighbors |
| Related components | Cohesive comparison sheet or grouped image variants | Shared style, useful differences, family consistency |
| Page section | One section image composed from established visual components | Composition, type/image hierarchy, focal point, narrative and responsive crop |
| Whole design or page | Existing image revision or assembled page image if requested | Global hierarchy, pacing, components, sections and consistency |

For a large project, prefer **component-first** work and build a visual library before designing sections. For a one-off target, begin and end at its actual size. Never demand a finished library for a user who asked to refine only a button or text treatment.

At *any* scope, use [PHASED_REFINEMENT.md](PHASED_REFINEMENT.md) to choose the current improvement lens: **1 foundational visual implementation -> 2 craft/details -> 3 advanced depth/effects only if justified -> 4 user/contextual review**. A unit that is already strong can enter a later phase. Each phase has its own image corrections and after-round user checkpoint; phases do **not** imply separate implementation or four mandatory generations.

## 2. Gather enough real evidence

Use known product purpose and **exact supplied copy**, the current user-confirmed or proposed foundation, images already selected by the user, and relevant *actually inspected* examples from the existing reference MCPs. Ask a focused question when vital input is missing; do not invent logos, metrics, testimonials, fonts or approved tokens.

References serve different roles: a selected first component establishes **style DNA**; a selected related component establishes family rules; a selected section informs composition; a provider example can resolve a fresh visual question. Use actual image inputs when the image tool supports them. A link or text description alone does not guarantee the model saw the image.

Choose a suitable framing for the requested unit (component crop, type specimen, comparison sheet, viewport or page). Specify output dimensions/aspect ratio, real content, important states, protected treatment and negative constraints. Image models can misspell or alter text: compare visually and keep the source copy outside the image as ground truth.

## 3. Write a specific image prompt

> Generate an **image** showing [exact visual unit] for [known product and context] at [aspect ratio/dimensions]. Its purpose is [concrete job]. Base the look on [confirmed/proposed foundation: type, color, spacing, geometry, image treatment]. Use the selected [first component/related family/section image] to preserve [specific relationships]. Apply the inspected [MCP/source image] only for [named visual relationship]. Show [required copy, subject, composition and relevant states]. Prioritize [focal point, proportions and hierarchy]. Avoid [specific unwanted patterns]. **Keep** [locked decisions]. This is a static visual exploration of [one component / group / section / page], not coded UI.

Make the prompt as concrete as the unit requires: a typographic treatment should not invent unrelated navigation; a button does not need page-level art direction; a section should include its composition and the reused family traits. [PROMPT.md](PROMPT.md) has examples by scale.

## 4. Iteration = image result + feedback

For **each image-generation/editing round inside the active phase** (Phase 1, 2 or optional 3 of [PHASED_REFINEMENT.md](PHASED_REFINEMENT.md)):

1. Inspect the actual image at useful scale, with relevant reference/previous images.
2. Name the highest-impact visible mismatch **at this phase's level** and propose a **meaningful revision**: keep / rework / expected visible difference. If the weakness belongs to an earlier phase, go back rather than masking it with effects. Change several connected traits when they express one clearer direction.
3. Generate or edit the image; a round may include multiple alternatives or an explicitly requested group.
4. Compare equivalent content, dimensions and style anchors. Preserve the strongest version, even if the newest is worse.
5. **Show the image(s), give a brief phase-specific assessment and ask what the user wants next.** Offer revision, acceptance, another direction, related components/group, the next section, or stop as relevant. Wait for their decision before another round.

There is no universal pass count. A difficult first component can take many rounds. Once its style is chosen, reuse its image/foundation rather than reexploring the same identity for each sibling. Prioritize substantial redesign before micro-tweaks; **small corrections** matter once the large relationships are right. Do not equate user silence with approval.

## 5. Scale by reusing agreed images

In a multi-part design, the usual path is:

**first high-leverage component** -> visually accepted exemplar and compact style decisions -> similar components -> related components generated in batches -> consistent image-based library -> first section composed with component images -> remaining sections -> optional page sequence.

[COMPONENT_LIBRARY.md](COMPONENT_LIBRARY.md) explains the point at which batch generation is useful, how the user/kit can tune the library and how to avoid inconsistent families. Individual-component or section-only assignments stop earlier as requested. Do not introduce a new mandatory phase just to increase output volume.

## 6. Save only useful provenance

In the **target project**, record actual image references/version IDs, scope (text/component/group/section/page), concise prompt or revision delta, selected reference images or MCP source and observed relationship, foundation status, user-selected vs agent-proposed state, open issues and requested next action. Keep images themselves when output storage is authorized; never make up paths or human acceptance.

A storyboard, comparison sheet or component tray is still **static image evidence**. It does not verify accessibility, responsive implementation, interaction, accurate embedded text or browser behavior. **No component implementation is performed by this skill.** Actual editable design/conversion/code requires a separately authorized workflow.

## 7. Optional outside skills

Skills from Skills.sh or third parties may help prompting or visual critique, but are not prerequisites. When the user authorizes a trial, compare the same image task/foundation/tool settings **with and without** the skill, judging the actual images, accepted decisions, intervention and observable consumption. Review security and permissions before any installation. A persuasive explanation or longer prompt is not proof of benefit.
