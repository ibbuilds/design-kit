# Frontend QA

- Review the scoped result against the target's actual brief, accepted work, TASTE.md and active references; the packaged BRIEF.md is only a template.
- Apply relevant checks; add checks for actual risks. Keep evidence in the target.
- Follow target release requirements and user-reserved decisions. Review-only tasks report repairs without applying them or updating project records.

## Review depth

- **Concept:** inspect direction, mobile composition and interaction intent; identify unfinished behavior.
- **Interactive prototype:** exercise the main frontend flow, realistic states, keyboard and touch; label mocks.
- **Production frontend:** apply the experience checks, relevant production checks and target requirements.
- Recheck affected areas after repairs; repeat broader checks only when changes introduce broader risk.

## Early visual decision

Inspect the integrated sample at actual viewing sizes, with loaded fonts/media and honest content. Use the active references and product job, not a numeric self-score:

- Does the opening explain this product/task through a clear focal point and next action, rather than interchangeable copy and decoration?
- Do type, alignment, spacing, imagery and surfaces form one deliberate hierarchy? Judge wraps/crops in the render, not only token values.
- Does the deeper region add substance and appropriate density instead of repeating the same box pattern? Is mobile recomposed and usable?
- For an ambitious visual brief, which product-specific decisions carry the idea, and where does the render still fall short of the relevant strong reference in composition, type/image balance, rhythm, asset fidelity or finish? A clear but interchangeable page has not met that brief. For closed designs, judge fidelity to the supplied authority.

Name the actual mismatch before changing anything: repair execution, replace the weak element, or reconsider the premise only when necessary. Reuse this inspection in the final review; it is not another mandatory audit loop.

For an open direction, calibrate critique with relevant accepted examples: name what makes their hierarchy, density, identity and task usability strong, and what would not fit this product. Judge our live result against those relationships and the brief. Separate coherence, product-specific choices, craft and functionality rather than hiding tradeoffs in one score. Familiar controls are not a defect merely for being familiar. Preserve a stronger earlier candidate if later polishing reduces quality. In substantial work, a distinct review should inspect the brief, raw evidence and working states; the builder's positive summary is not verification. Independent review follows actual availability and authorization.

## Completion criteria

Judge the scoped result in the actual render, with the relevant reference/base beside it when comparison matters. A successful build or attractive hero alone is insufficient. Apply only criteria relevant to the requested fidelity and scope:

- **Product and authority:** the main job, content and next action are clear; closed structural/final-design decisions are respected. Claims and proof are real or explicitly labeled demo content.
- **Composition:** the intended focal point, reading/task order and density survive the render. The dominant visual is useful, legible and correctly cropped; its absence is not covered with decoration. Deeper regions have their own content-driven treatment instead of an interchangeable card grid.
- **Type and finish:** actual fonts/weights load; wraps, line lengths, alignment, spacing, borders and image quality form the intended hierarchy. No major clipping, placeholder assets or inconsistent controls remain within scope.
- **Reference impact:** each reference used to justify a material decision can be connected to the implementation. Compare the specific relationship (scale, rhythm, framing, density or behavior), not a checklist of copied colors. Reject irrelevant references instead of forcing them in. Record unobserved behavior as unknown.
- **Requested creative level:** an open direction expresses a coherent product-specific idea at the requested reference standard, with no material unresolved gaps in hierarchy, type/image relationships, rhythm, asset quality or finish. Compare observable relationships and preserve intended usability; do not certify an award, copy another brand or give the work a self-score. In faithful implementation, this criterion follows the supplied design rather than a new art direction.
- **Responsive and access:** the composition works at relevant mobile/desktop/container widths, including troublesome intermediate sizes. Content and actions remain available; required keyboard, focus, contrast and reduced-motion behavior work. Screenshots alone do not verify interaction.
- **Behavior and integration:** the scoped primary action and important failure/recovery states work at the requested fidelity. Mocks remain labeled. Required target checks pass and accepted work has no material regression.

Classify gaps before repairing: **requirement violation**, **material craft/usability defect**, or **optional preference**. Resolve the first two in authorized edit work while a justified repair is possible. Do not reopen accepted identity for an unrequested preference. Batch related changes and recheck their effects. Stop after criteria are met; do not add effects, variants or audits solely to keep improving. If a user budget or missing capability prevents completion, preserve the result and name the unmet criterion rather than claiming readiness.

For a short local change, reuse existing evidence and inspect the affected region/states; do not turn these criteria into a full-site audit. Review-only tasks report gaps without applying repairs. User acceptance remains separate from the agent's verification.

## Experience

- **Craft:** identify concrete gaps in hierarchy, composition, type, imagery and detail, including deeper screens.
- **Clarity:** verify the user can identify the value/job, available action and expected result.
- **Copy:** check audience fit, meaningful benefits, relevant objections and accurate CTA promises. Remove filler and unsupported proof.
- **Behavior:** in an authorized local/test state, exercise the primary task and relevant recovery paths. Check feedback, input preservation and continuity.
- **Responsive:** inspect mobile, tablet, desktop and intermediate widths with realistic content. Test components within their actual containers.
- **Layout:** check wrapping, crops, overflow, sticky layers and touch access; preserve useful information and actions.
- **Code:** follow target conventions; use semantics, clear names, cohesive components, predictable state and appropriate types.
- **Integration:** inspect the actual application. Preserve accepted prototype design and behavior when integrating.
- **System adherence:** check actual component reuse, semantic token roles, required variants/states and affected consumers. Similar colors or detached shapes do not establish system adherence. Keep inferred style foundations distinct from a verified reusable system.

## Production

- **Accessibility:** check names, semantics, keyboard order, visible/restored focus, contrast, zoom/reflow, touch and reduced motion. Check critical screen-reader paths and custom widgets against relevant APG/WCAG guidance.
- **Forms/navigation:** test validation, actionable errors, preserved input, success, destructive-action recovery, deep links, refresh and back behavior.
- **Product-specific risks:** check relevant search/filter context, honest chart scales/units, and AI progress, limits and correction.
- **Localization:** test required locales, text expansion, formats and bidirectional content.
- **Performance:** measure loading, interaction responsiveness and layout stability against product budgets. Investigate costly fonts, media, effects and requests.
- **Data/integrations:** verify contracts, persistence, stale/slow/failed requests, cancellation and session/permission states. Keep privileged operations in services.
- **Maintainability:** inspect duplicated logic, fragile effects, unused dependencies and unnecessary abstractions. Run required format, lint, type and relevant regression checks.
- **Release:** when authorized, follow target release checks for routes, services and recovery. Obtain additional review when required or material risk remains.

## Accepted baselines

- Keep accepted baselines in the target using its existing tools.
- Capture baselines when comparison will help; no new baseline files are required for every task.
- Record acceptance, revision, content/state, viewport, browser, fonts and assets.
- Capture important responsive and interaction states in context, including focus, input, motion and task completion.
- Compare equivalent conditions for hierarchy, wrapping, crops, density, behavior and perceived speed; separate rendering noise from regressions.
- Update a baseline only for an accepted improvement and keep before/after evidence.

## Close the review

- Record useful issues as **location + viewport/state + defect + impact + repair + recheck**.
- In an authorized edit task, fix blocked tasks, misleading behavior and major craft gaps before micro-polish; in review-only mode, report them.
- Preserve accepted work; use baseline comparison when it helps.
- Report unobserved behavior and missing evidence. Keep captures/reproduction steps when useful.
- Distinguish directly exercised keyboard/focus behavior, DOM/accessibility-tree observations and inferred screen-reader behavior. Name the method and evidence for a reported defect; do not present a planned check or an inferred reading order as an actual assistive-technology test. Reuse existing captures/annotations for precise feedback; a separate HTML/PDF audit artifact is optional.
- Tests do not prove design excellence; walkthroughs do not replace user research.
- Synthetic personas can suggest hypotheses and edge cases, not establish actual user needs or usability findings. Validate consequential assumptions with real evidence when available.
- Partial checks do not establish accessibility conformance. Lab metrics are not field Web Vitals.
- Review does not authorize publication.
