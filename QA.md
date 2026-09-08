# Frontend acceptance

Review the scoped result against BRIEF.md, [TASTE.md](TASTE.md) and relevant selected
references. This is a quality floor, not an aesthetic formula. Use applicable checks;
add checks for actual risks. Keep evidence in the target. Passing tests, agent scores
and OpenDesign success do not prove excellent design or independent approval.

## Inspect every handoff

- **Craft:** compare actual hierarchy, type relationships, composition, assets and
  motion with the selected reference intent. Identify the gap, not just "needs polish."
  Check deeper content as carefully as the opening; repetition must serve the content.
- **Comprehension:** can a new user identify where they are, the value/task, next action
  and result? Test concrete labels and believable content; remove contradictory cues.
- **Behavior:** complete the primary job and consequential recovery states. Inspect
  input preservation, feedback and continuity. Match the fidelity promised in the brief.
- **Adaptation:** inspect desktop and small screens plus intermediate widths where the
  layout changes. Try long content and realistic data density; check wrapping, crops,
  overflow, sticky layers and touch access. A scaled-down desktop is not mobile design.
- **Integration:** when delivered, inspect the target application as well as the
  OpenDesign preview. Compare fonts, assets, layout, interactions and state behavior.

Record issues as **viewport/state + location + defect + impact + repair + recheck**.
Prioritize blocked tasks, misleading behavior and major craft gaps before micro-polish.
Attach a capture for visual defects or reproduction steps for behavior. Preserve good
work; a plateau cannot pass a blocker. Keep unobserved behavior marked unverified.

## Match the mode

| Mode | Evidence required |
| --- | --- |
| Concept | Visual direction, mobile composition, interaction intent; unfinished behavior explicit |
| Interactive prototype | Usable primary frontend flow, credible demo data/states, keyboard/touch; mocks explicit |
| Production frontend | Applicable checks below, real integrations and fresh release review |

## Production checks

- **Accessibility:** semantic controls and names; logical keyboard order, visible and
  restored focus; contrast, zoom/reflow, touch, reduced motion and critical screen-reader
  path. Check custom widgets against APG and applicable WCAG requirements. Automated
  checks supplement manual use; decorative originality does not excuse inaccessible controls.
- **Forms and navigation:** useful validation timing, actionable errors, preserved input,
  clear success, recoverable destructive actions where appropriate; deep links, refresh,
  back and permission/session recovery. Test actual results, not just click handlers.
- **Relevant product risks:** search/filter/sort preserve orientation; charts communicate
  units, scales and comparisons honestly; AI flows expose limitations, progress, correction
  and recovery. Apply only to features in scope; use the relevant library section for gaps.
- **Localization:** test required locales, expansion, formats and bidirectional content.
  Do not invent additional locale scope.
- **Performance:** measure loading, interaction responsiveness and layout stability;
  investigate costly fonts, media, effects and requests. Compare with product budgets.
  Smooth animation alone is not responsiveness; lab measurements are not field Web Vitals.
- **Integration/code:** verify supplied contracts, persistence, stale/slow/failed requests,
  cancellation and session/permission UI. Keep privileged operations in services. Run
  existing required checks and relevant regression tests; inspect duplicate logic, fragile
  effects, unused dependencies and unnecessary abstractions.
- **Release:** a fresh reviewer/context checks the authorized deployed preview, routes,
  services and applicable monitoring/recovery, then decides SHIP / DO NOT SHIP. Extra
  agents require authorization. Self-review is not independent release approval.

Use [BASELINES.md](BASELINES.md) to detect drift. Agent walkthroughs are heuristic review,
not representative-user research. Report missing evidence; do not invent backend scope
or claim accessibility conformance from partial checks. Release review does not publish.
