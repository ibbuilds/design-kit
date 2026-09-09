# Frontend QA

- Review the scoped result against BRIEF.md, TASTE.md and supplied project references.
- Apply relevant checks; add checks for actual risks. Keep evidence in the target.
- Follow target release requirements and user-reserved decisions.

## Review depth

- **Concept:** inspect direction, mobile composition and interaction intent; identify unfinished behavior.
- **Interactive prototype:** exercise the main frontend flow, realistic states, keyboard and touch; label mocks.
- **Production frontend:** apply the experience checks, relevant production checks and target requirements.
- Recheck affected areas after repairs; repeat broader checks only when changes introduce broader risk.

## Experience

- **Craft:** identify concrete gaps in hierarchy, composition, type, imagery and detail, including deeper screens.
- **Clarity:** verify the user can identify the value/job, available action and expected result.
- **Copy:** check audience fit, meaningful benefits, relevant objections and accurate CTA promises. Remove filler and unsupported proof.
- **Behavior:** complete the primary task and relevant recovery paths. Check feedback, input preservation and continuity.
- **Responsive:** inspect mobile, tablet, desktop and intermediate widths with realistic content. Test components within their actual containers.
- **Layout:** check wrapping, crops, overflow, sticky layers and touch access; preserve useful information and actions.
- **Code:** follow target conventions; use semantics, clear names, cohesive components, predictable state and appropriate types.
- **Integration:** inspect the actual application. Preserve accepted prototype design and behavior when integrating.

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
- Fix blocked tasks, misleading behavior and major craft gaps before micro-polish.
- Preserve accepted work; use baseline comparison when it helps.
- Report unobserved behavior and missing evidence. Keep captures/reproduction steps when useful.
- Tests do not prove design excellence; walkthroughs do not replace user research.
- Partial checks do not establish accessibility conformance. Lab metrics are not field Web Vitals.
- Review does not authorize publication.
