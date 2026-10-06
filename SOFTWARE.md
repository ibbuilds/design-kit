# Frontend implementation and QA

Use for requested frontend code and behavior. [SKILL.md](SKILL.md) governs design checkpoints; this is the implementation procedure after relevant design acceptance. Scope ends at the frontend: consume existing APIs, but do not create backend endpoints, databases, migrations or infrastructure. Review-only inspects and reports without edits.

## Work from the target and accepted design

Inspect target instructions, stack, canonical tokens/components, affected callers, current changes and required checks. Reuse accepted structure, assets and useful prototype code. Harden prototype behavior rather than blindly copying it or rebuilding its visual vocabulary. Ask only for material missing contracts or reserved decisions; routine implementation follows existing conventions.

Keep the implementation proportional. A local repair needs reproduction, a scoped fix and relevant verification. A substantial frontend feature uses [PRODUCT_DELIVERY.md](PRODUCT_DELIVERY.md) to connect the user outcome, states and evidence. No new framework, architecture document or exhaustive test suite by default.

## Define observable behavior

Identify the relevant UI inputs, outputs, state transitions, existing service contract and important errors. Include loading, empty, populated, invalid, disabled, slow/failed and success states where the feature needs them. Preserve work on failure and provide meaningful recovery. Label mocks, illustrative data and untested services; a toast is not evidence of persistence.

For a bug, reproduce its symptom in the actual application or supported host. Separate candidate causes with the smallest useful evidence. If reproduction is unavailable, name the unknown. Repeated speculative patches require a changed hypothesis or targeted instrumentation.

## Implement and inspect

Loop: **inspect/reproduce -> choose evidence -> implement -> run affected checks -> inspect render/diff/behavior -> repair concrete gaps.**

Use the target's existing types, state patterns and API clients. Validate untrusted input at frontend boundaries; do not claim client-side checks provide server authorization. Handle cancellation, stale responses and retries where relevant. Keep secrets out of browser code, records and logs. Preserve project contracts and concurrent human edits.

Use semantic elements, useful labels, keyboard behavior, visible focus and relevant accessibility requirements. Apply [CRAFT.md's responsive criteria](CRAFT.md#responsive-in-every-ui-batch) in every UI implementation batch, checking actual containers, affected breakpoint transitions, content/states, asset/font loading and reduced motion. Compare accepted design and actual result under equivalent content, state, viewport and loaded assets. A needed departure from a closed visual decision requires the proposed alternative and human acceptance.

For host plugins, inspect the actual host's UI and lifecycle when that integration is in scope. A standalone browser mock does not verify host behavior. Run the existing application/preview path when possible; do not change the user's runtime or install dependencies without applicable authorization.

## Verify the relevant risks

Choose checks that could reveal an incorrect implementation. Unit tests suit meaningful pure logic; integration checks suit existing contract boundaries; browser tests suit critical user paths. Existing checks/direct inspection can suffice for reversible low-impact changes. Do not add tests that restate implementation or weaken valid assertions to pass.

Derive expected results from requirements or trusted fixtures. A setup/import error does not demonstrate the intended regression. Controlled mocks can exercise frontend failure handling; separately report whether the actual authorized service was exercised. Use stable accessible locators and condition-based assertions, not arbitrary sleeps.

Measure a suspected performance problem before optimizing, with relevant content, device/network conditions and the project's budget. Check excessive rendering, oversized assets, font loading and layout instability when affected. No new observability platform for a local diagnostic.

## Finish the requested scope

Complete relevant required checks and resolve material regressions. Present the working frontend, affected visuals/states, verification and actual limits. Preserve the strongest accepted baseline. Passing tests does not certify beauty, complete accessibility, security or live backend compatibility.

Keep implemented, verified and human-accepted statuses separate in the existing project record. Continue authorized corrections through the result; only changed/dependent work needs review. Publishing/deployment follows separate existing authorization. No automatic backend extension, extra agents or background monitoring. [EXECUTION.md](EXECUTION.md) covers continuity and effort.
