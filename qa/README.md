# Frontend acceptance

Review the brief, taste and actual rendered experience. Keep evidence in the target,
not this skeleton. OpenDesign success, self-scores and passing tests do not prove
visual quality. Self-review is not independent release approval.
Agent walkthroughs are heuristic review, not evidence from representative users.

## Every handoff

- Inspect desktop/mobile with realistic content. Apply taste criteria to identity,
  hierarchy, typography/wrapping, composition, copy, meaningful assets and motion.
- Perform the primary job. Check orientation, findable actions, feedback and relevant
  failure/recovery states. Density must serve the task; polish covers behavior too.
- After integration, inspect the target app as well as the OpenDesign preview.
- Record each issue as **viewport/state + location + defect + impact + smallest
  repair + recheck**. Prioritize by user impact; preserve good
  work and verify repairs. Missing evidence stays open; a plateau cannot pass a blocker.

## Match the mode

| Mode | Required evidence |
| --- | --- |
| Concept | Visual hierarchy, mobile composition, interaction intent, honest labels |
| Interactive prototype | Working primary frontend flow, believable demo data/states, keyboard/touch; mocks explicit |
| Production frontend | All applicable checks below, real integrations and fresh release review |

## Production checks

- Visual/responsive: accepted targets, type/crops, section rhythm, assets and justified
  post-freeze changes. Use [baseline guidance](baselines/README.md) for comparisons.
- UX: relevant loading/empty/error/success/disabled/permission/destructive states;
  real action result, validation/input preservation, sign-in/recovery, deep links,
  refresh/back and slow/offline recovery where needed.
- Localization: required languages/locales, text expansion, formats and RTL where
  applicable. Do not invent extra locale scope.
- Accessibility: semantics, labels, contrast, keyboard/focus, touch, reduced motion,
  zoom/reflow, error identification and the critical screen-reader path. Automation
  covers only part of this; still images cannot prove interaction or motion.
- Performance: measure relevant bundle/network/media/render/memory against product
  budgets and recheck repairs. Lab results are not field Web Vitals.
- Integration/reliability: supplied contracts, session/permission UI, stale state,
  cancellation, recovery and required persistence. Protect client trust boundaries;
  secrets and privileged operations remain in services.
- Code: dependencies, dead/duplicate logic, fragile effects and needless abstractions.
- Release: use the authorized deployed preview; check routes/services, client error
  monitoring and recovery/rollback. A fresh reviewer/context must inspect the running
  result and decide SHIP / DO NOT SHIP; extra agents require authorization.

No invented backend requirements. Report unverified work. Release review does not
itself authorize publication. Research only the specific uncertainty that needs it.
