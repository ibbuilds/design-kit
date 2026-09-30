# Deliver a real product capability

Read for a substantial product feature, integration, or release-readiness task. Local edits use [SOFTWARE.md](SOFTWARE.md) directly. Design-only work stays in SKILL.md/ONBOARDING.md and does not load this route. This complements SOFTWARE.md's engineering loop and SKILL.md's design procedure; it does not create a second implementation or authorize additional scope.

## Establish a checkable outcome

Identify the user, job, starting conditions, successful result and consequences of failure. Separate user requirements from agent assumptions and proposed extras. A planner must not invent features, AI integrations or infrastructure to make the product look ambitious. Resolve material unknowns; proceed on routine details within delegated authority.

For substantial work, retain a small acceptance map in the target's existing issue/spec/record:

| Required outcome | Contract or boundary | Evidence that could disprove it | Status |
| --- | --- | --- | --- |
| User saves an item and can recover it | UI -> authorized service -> durable store | Save, refresh/reopen, read back; reject another user's access where applicable | Planned / implemented / verified / blocked |
| Failed save preserves work | Request/state/recovery | Induce a controlled failure, inspect retained input, retry without unintended duplication | Planned / implemented / verified / blocked |

Use rows appropriate to the feature, not this example's database or login by default. Link substantial requirements to their checks; an implemented function, passing build or success toast cannot mark an unexercised outcome verified. Keep agent-selected and user-accepted design decisions separate.

## Plan against the repository and probe uncertainty

Inspect the affected path, callers, data model and canonical components. Identify boundaries, incompatible contracts, concurrent work, run commands and disposable fixtures. Use a small plan proportional to dependencies and risk. For an unfamiliar integration or irreversible technical choice, probe the uncertain boundary early before expanding the implementation.

A behavior-led feature starts with requirements; an existing technical constraint may require a feasibility probe first. Both must converge on the user's outcome. Requirements and technical design may evolve with evidence, but changes to closed decisions need the user's authority. Do not impose a complete specification framework on a local repair.

Make important invariants executable with existing types, schemas, constraints, lint or tests when warranted. Parse/validate untrusted data at the boundary; do not infer a service shape from a sample that never ran. Preserve maintainable dependency directions and the target's source of truth. Add custom architecture enforcement only for a demonstrated recurring need.

## Complete, then challenge the result

Implement complete capabilities in dependency order. Milestones help when the task needs them; fixed sprints, one-feature-per-session resets and mandatory extra agents are not required. Keep the environment runnable and the acceptance map current across long work.

Review the running result against requirements, not the builder's summary. For substantial or sensitive work, take a distinct review pass using the original brief, diff, application/host and raw check evidence. Try to disprove the important outcomes: exercise a fresh session, persistence, invalid input, permission failure and recovery as relevant. Report reproducible findings rather than congratulating the implementation or assigning a self-score. A same-agent pass is not independent review; use a separate reviewer only when available and authorized for the task/risk. Give that reviewer the requirements and raw artifacts without the builder's desired verdict.

For open visual work, calibrate critique against relevant accepted examples: explain which hierarchy, density, identity and interaction choices make an example strong or unsuitable. Evaluate coherence, product-specific decisions, craft and task usability separately. Weight them for the product; an expressive campaign and a dense work application have different needs. Visual originality cannot excuse a broken user task. Preserve a better earlier candidate; the last iteration is not automatically the best.

Tests need a useful oracle: derive expected results from the contract, known fixtures or another trusted source, not by rerunning the implementation inside its assertion. For a regression test, confirm it exposes the original defect when feasible and inspect why it fails; an import/configuration error is not evidence of the intended regression. Test-first is an option, not proof of superior architecture. Correct a demonstrably wrong test with justification; never weaken a valid requirement to pass. Consider targeted mutation/property checks for important pure logic only when they add confidence.

For browser E2E, use isolated controlled data, role/label or stable-contract locators and condition-based assertions rather than arbitrary sleeps. Exercise the real application path. Mock an uncontrolled third party for reproducible local failure tests, then separately verify the authorized real integration in its sandbox/staging environment where needed. A mocked E2E establishes frontend handling of that contract, not live provider compatibility. Inspect console/network/runtime evidence when it helps explain the failure; screenshots alone cannot verify behavior.

## Release evidence proportional to the product

For requested production readiness, identify applicable requirements and remaining gaps in:

- **User experience:** complete critical journeys, useful real content, responsive states, actual assets, keyboard/focus and relevant WCAG requirements.
- **Contracts/data:** validation, access at the trusted boundary, persistence, concurrency/retry behavior and compatibility; migration/recovery proof where applicable.
- **Build/runtime:** reproducible build and configuration, supported host, required checks and actual integration behavior. Record the tested revision/environment.
- **Operations:** observable failures, appropriate redacted diagnostics, deploy/rollback path and data restore where the product needs them; validate in an authorized disposable environment.
- **Performance:** realistic dataset/device/network and explicit budgets for important journeys; distinguish a local measurement from field performance.

Mark each applicable requirement verified, failed or untested with evidence and a concrete next action. A static site's profile differs from a SaaS or host plugin. Do not create irrelevant infrastructure or claim complete security/accessibility conformance from partial checks. Use the target's required review and release gates. Complete any already-authorized delivery; seek only missing authorization after preparing the concrete result.

After an authorized release, confirm the critical path and observable health within that authorization. Retain rollback/recovery information and unresolved issues. Product feedback and real defects can refine the next task; the kit does not schedule monitoring or background cleanup by itself.
