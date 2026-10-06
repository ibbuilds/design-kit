# Visual system craft

Read before developing or changing visual foundations, components or UI, and for a review of those concerns. Apply only the affected sections. [SKILL.md](SKILL.md) owns the procedure; [ONBOARDING.md](ONBOARDING.md) owns human checkpoints. This resource defines what to inspect and demonstrate inside their batches.

## Make the requested quality observable

Set the review lens from the user's complaint and accepted direction. In a UI-craft task, investigate type, colors, spacing, control families, assets and material treatment first; retain adequate behavior and accepted composition. Investigate navigation/content/flow when relevant evidence puts them in scope. A system-level cause can be a shared padding rule or missing color role, without any page-layout change.

Keep a compact visual contract in the target's existing record or working notes: `affected role/family -> expected relationship or explicit requirement -> source/rationale -> canonical owner -> actual view/measurement -> unresolved mismatch`. Reuse the accepted reference map and source paths. Separate mandatory requirements, protected source treatments and proposed aesthetic choices. Capture numerical rules and explicit exclusions accurately; a vague vibe summary must not replace them. Preserve scoped approvals and distinguish accepted originals from unreviewed additions.

For every requested defect, establish a concrete failure in the current view or source, then its expected result. If access is insufficient, mark that item unobserved. Do not infer that it passes from a design MD, successful build, matching token names or another component's capture. Propose necessary craft improvements beyond defects through the same scoped review, with their expected visible contribution.

## Color roles, not just swatches

Map the roles the actual interface needs to canonical tokens: canvas and layered surfaces; primary/secondary/supporting text; passive and interactive borders; filled/subtle actions and their foregrounds; selected/pressed/hover treatments; focus; disabled; and applicable status/feedback roles. Separate decorative/brand colors from operational semantics. A monochrome identity can have rich surface, border and state distinctions without acquiring unrelated hues.

Identify missing or overloaded roles from the rendered consumers. Reuse or derive the needed values within the approved palette and theme strategy; increasing shade count alone is not improvement. Document purpose, pairing, state and usage beside the existing definitions, with aliases when supported. Specify only required themes; new themes or a fixed palette size are not defaults.

Inspect actual text/background and control/background pairs in the applicable states and themes. Test readable hierarchy and distinguishability in context; measure required contrast using the effective background, including transparency/layers. A palette preview cannot establish contrast for its consumers. Check that intended state differences survive implementation and that arbitrary local hex values do not create competing role definitions.

## Typography as applied styles

Define the necessary styles by content role, such as display/title, section heading, body, control label, supporting text, metadata and numeric/code content. These are candidates, not a mandatory inventory. For each used role, specify its canonical family, loaded weight, size, line-height, tracking, case/features and responsive rule where relevant, plus when to use it. A font name and heading scale alone do not resolve a system.

Render real labels, paragraphs, mixed lengths and relevant numeric/code content. Verify the actual font and weight load; inspect fallback/synthetic-weight drift, baseline alignment, wrapping, measure and rhythm at the intended size/container. Compact labels and long-form copy may need different leading. Choose role relationships that express the confirmed aesthetic rather than imposing a universal font, ratio or tracking prescription. Keep repeated roles consistent and purposeful exceptions explicit.

## Spacing and geometry have owners

Reuse the project's required grid/scale. When the user requires strict multiples of a unit, check affected gaps, margins and paddings against it; propose a necessary exception explicitly instead of silently inventing an optical exemption. A grid for spacing does not automatically govern borders, font sizes or every geometry value.

Trace effective rendered values to the owning layer: intrinsic control padding; icon/label gap; field label/help/error spacing; row/stack gap; container inset; or page rhythm. Inspect cascade/variant overrides and actual bounds. Repair the shared owner when it causes repeated symptoms; avoid compensating local margins that leave the underlying rule inconsistent.

Compare text-only and icon-bearing controls of the same size. Verify logical leading/trailing insets, icon-to-label gap, text baseline, actual icon bounds and stable height. Reserve space for trailing adornments/chevrons so content cannot collide with them or the outer edge. Distinguish padding from border-box dimensions and visible glyph bounds. Inspect tight/long content and narrow containers; central alignment or a declared token does not prove adequate breathing room.

## Component families and states

Group affected variants by their shared visual rules. Check related controls together in the same theme, scale, content conditions and container, then in a real consumer. Preserve differences their jobs require; consistency means stable relationships, not making every control identical.

| Family in scope | Relationships to demonstrate |
| --- | --- |
| Actions | Height, label style, insets, icon gap/size, geometry and state feedback across needed sizes and text/icon variants. Introduce an icon-only action only when a real use requires it. |
| Text input, textarea, select and search | Shared label/text/border/surface language, appropriate height or line behavior, content/adornment clearance, and consistent focus/error/disabled rules. Preserve an approved search composition. |
| Checkbox, radio and other selection controls | Indicator geometry, mark treatment, label gap, baseline and selected/unselected/focus/disabled distinction. Preserve the correct selection and keyboard semantics when adapting appearance. |
| Field wrappers | Label, help/error, required indication and spacing around the actual input. Distinguish wrapper responsibilities from the input primitive; reconcile duplicate presentation/API roles without deleting meaningful semantics. |
| Repeated panels, rows and overlays | Shared surface/elevation, borders, insets and content hierarchy; inspect both isolated specimens and affected compositions. |

Use existing component APIs and state mechanisms. For each affected family, exercise the required default, hover/pressed, focus, selected, disabled, loading and invalid states as applicable. Inspect the visual outcome, not just prop coverage. A few static happy-path tiles cannot certify the family. Keep the inventory tied to current work rather than inventing unused variants or future controls.

## Icons, marks, assets and finish

Inventory relevant existing icon assets and their intended roles. Prefer that library's appropriate glyphs; keep stroke, weight, sizing and alignment coherent. Inspect the effective SVG/viewBox bounds and appearance at actual control sizes. Access to a broad icon set is not a requirement to display every icon.

Distinguish a base symbol, wordmark/lockup and approved contextual rendering. Compare the source asset and accepted in-product treatment before proposing changes. Preserve valued enhancements and identity relationships; possession of a raw asset does not establish the final appearance. New artwork or changes to the base mark require the actual scope/authorization. Check clipping, resolution, cropping, transparency, theme/background fit and consistency across needed uses.

Choose material, depth, texture and motion from accepted direction and reference achievements. Evaluate their role, intensity and coherence on real content. Useful finish can raise visual quality; adding every source effect or cloning its brand cannot. Inspect actual motion when it is part of the claim, including the relevant reduced-motion behavior.

## Evidence before the batch is presented

Use the existing preview and canonical implementation, with loaded fonts/assets. Batch inspection of affected families and their consumers; show readable actual captures in the user's preferred medium. Use the source and current/proposed views under equivalent states/content/viewport when comparison matters. For code, pair visual findings with computed styles, bounds and token/component ownership; for canvas, inspect actual properties and bindings. Retain useful evidence once rather than running a separate capture trip per rule.

Reconcile each visual-contract item with an observed result or explicit unresolved gap. A repaired example does not close unseen variants. Reinspect affected states/consumers after a shared repair. Update the affected canonical design documentation to describe the verified roles/usage, linking values/APIs instead of duplicating them. Present the visible contribution, protected treatments retained and remaining gaps for the normal human checkpoint. Mechanical consistency and aesthetic acceptance remain distinct; a positive summary certifies neither.
