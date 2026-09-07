# Review context

Use this guidance while reviewing the actual site in its target project. Run that
project's available tools and keep its tests, captures, baselines and review records
there. This context repo supplies no test harness and has no site-quality score.

## Review the actual result

Open the rendered desktop/mobile interface and perform the primary job. Inspect
the hero/core workspace, a deeper section/state, and relevant failure cases. Judge
product-specific identity, originality, hierarchy, type/wrapping, composition,
product meaning, copy/action clarity, assets, motion and responsive priorities.

For each issue, name viewport and section/control; describe the visible defect;
explain its effect on meaning, conversion, UX or craft; choose the smallest repair;
then render/use again and verify it improved without losing successful decisions.
Fix the two or three most important issues per pass. Preserve the best snapshot.

## Match the mode

| Mode | Evidence before handoff |
| --- | --- |
| Concept | Visual hierarchy, responsive composition, interaction intent and honest labels. |
| Interactive prototype | Working primary frontend flow, believable demo data/states, keyboard/touch; mocks explicit. |
| Production frontend | Real required integrations/state/persistence, failures, accessibility, measured performance, client security/reliability, deployed preview and fresh review. |

## Production frontend review

- Visual/responsive: accepted native-size targets, type/wrapping, crop/assets,
  section rhythm, mobile composition and justified post-freeze changes.
- UX: relevant loading/empty/error/success/disabled/permission/destructive states;
  actual CTA/task result, deep links, refresh/back, slow/offline recovery as needed.
- Accessibility: semantics, labels, contrast, keyboard/focus, touch, reduced motion
  and the critical screen-reader path. Automated checks cover only part of this.
- Performance: profile relevant bundle/network/media/rendering/memory, set product
  budgets and rerun after repairs. Lab checks are not field Web Vitals.
- Integrations/reliability: supplied service contracts, session/permission UI,
  request cancellation, stale state, failure recovery and required persistence.
  Keep secrets/privileged operations in services; backend implementation is separate.
- Code: client trust boundaries, dependencies, dead/duplicate logic, fragile effects
  and unnecessary abstractions. Evaluate the actual stack rather than imposing one.
- Release: use the authorized deployed preview, inspect routes/services and errors,
  and obtain a fresh reviewer/context's actual SHIP / DO NOT SHIP decision.

Still images do not prove motion or interactions. Test success does not prove taste.
Self-review is not independent approval. Missing evidence stays explicit, and a
plateau does not turn a blocker into a pass. A release decision is not authorization
to publish. Service-free sites need no invented backend requirements.
