# Legacy frontend reference — outside Design Kit's default scope

This document is retained for separately user-authorized frontend tasks and the explicit legacy installer software pointer. **Design Kit itself stops at selected section images and the complete page's visual decision. It never auto-implements these images.** Read [SKILL.md](SKILL.md) for the current purpose. The implementation advice below applies only after a separate user instruction chooses that work.

# Frontend implementation and QA

Use for requested frontend code and behavior. [SKILL.md](SKILL.md) governs scope and review. Work from accepted design or the currently authorized coded candidate; there is no additional approval gate before authoring that candidate. Preserve explicit user checkpoints. Scope ends at the frontend: consume existing APIs, but do not create backend endpoints, databases, migrations or infrastructure. Review-only inspects and reports without edits.

## Work from the target and actual implementation

Inspect target instructions, relevant stack and canonical tokens/components, affected callers, current changes and required checks. Locate the closest accepted component variant or composed pattern in source, stories/examples and real usage. Import or extend that implementation within the target's architecture; do not reconstruct it from screenshots or documentation when working code is available.

Preserve protected structure/assets and useful prototype code, hardening behavior for the requested fidelity. Where reuse across products is incompatible, port the scoped pattern deliberately and verify its inherited relationships. Ask only for material missing contracts or reserved decisions; routine implementation follows existing conventions. For open design, the assigned agent still owns the visual decisions rather than requiring a second model or exhaustive specification.

Keep the implementation proportional. A local repair needs reproduction, a scoped fix and relevant verification. A substantial frontend feature uses [PRODUCT_DELIVERY.md](PRODUCT_DELIVERY.md) for outcome, states and evidence. No new framework, architecture document or exhaustive test suite by default.

## Define observable behavior

Identify relevant UI inputs, outputs, state transitions, existing service contracts and important errors. Include loading, empty, populated, invalid, disabled, slow/failed and successful states where needed. Preserve work on failure and provide recovery. Label mocks, illustrative data and untested services; a toast is not evidence of persistence.

For a bug, reproduce its symptom in the actual application or supported host. Separate candidate causes with the smallest useful evidence. If reproduction is unavailable, name the unknown. Repeated speculative patches require a changed hypothesis or targeted instrumentation.

## Implement and inspect in the same assignment

Use the target's existing types, state patterns and API clients. Validate untrusted input at frontend boundaries; do not claim client-side checks provide server authorization. Handle cancellation, stale responses and retries where relevant. Keep secrets out of browser code, records and logs. Preserve project contracts and concurrent human edits.

Use semantic elements, useful labels, keyboard behavior, visible focus and relevant accessibility requirements. Apply [CRAFT.md's responsive criteria](CRAFT.md#responsive-in-every-ui-batch) to affected containers, breakpoint transitions, content/states, asset/font loading and reduced motion. Compare actual results under equivalent content, state, viewport and loaded assets. A necessary departure from a protected visual decision requires the proposed alternative and human acceptance.

For host plugins, inspect the actual host's UI/lifecycle when that integration is in scope. A browser mock does not verify host behavior. Use the existing application/preview path; do not change the runtime or install dependencies without authorization.

## Verify the relevant risks

Choose checks capable of exposing incorrect implementation. Unit tests suit meaningful pure logic; integration checks suit contract boundaries; browser tests suit critical paths. Existing checks/direct inspection can suffice for reversible low-impact changes. Do not add tests that merely restate implementation or weaken valid assertions to pass.

Derive expected results from requirements or trusted fixtures. A setup/import error does not demonstrate the intended regression. Controlled mocks can exercise failure handling; separately report whether the actual authorized service was exercised. Use stable accessible locators and condition-based assertions, not arbitrary sleeps.

Measure suspected performance problems before optimizing. Inspect excessive rendering, oversized assets, font loading and layout instability when affected. Do not introduce an observability platform for a local diagnostic.

## Finish without an unbounded second loop

Verification and repair use the same task budget as the visual assignment. Group checks and corrections; do not reset the allowance at frontend or QA handoff. Required checks still matter. At an explicit limit, report incomplete work and stop rather than hiding defects or claiming readiness. [EXECUTION.md](EXECUTION.md) governs stopping and continuity.

Present the actual frontend, visible contribution, checked states/containers and limits. Preserve the strongest accepted baseline. Passing tests does not certify beauty, complete accessibility, security or live backend compatibility. Keep implemented, verified and human-accepted states separate. Publication follows separate authorization; no automatic backend extension, extra agents or background monitoring.
