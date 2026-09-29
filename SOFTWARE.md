# Software workflow

Use for programming and behavior. This is the canonical engineering procedure; [SKILL.md](SKILL.md) governs visual/frontend decisions only when the task has them. A backend-only change does not load the visual library. Review-only requests inspect and report without changing code or project records.

## Match depth to the change

- **Local change:** inspect relevant code, reproduce the failure or state the observable acceptance criterion, implement, run focused checks and inspect the diff. No new architecture/specification by default.
- **Substantial feature:** define the user outcome, contracts, state and failure paths, affected boundaries and verification; implement a complete useful capability before expanding.
- **Long work:** use scoped milestones and preserve a compact handoff in existing records. See [EXECUTION.md](EXECUTION.md) for effort and continuity.
- **Sensitive change:** add relevant negative cases and recovery evidence for permissions, money, sensitive data, deletion, migrations or external side effects, even if the diff is small.

Work in the target project. Preserve its stack, instructions, uncommitted work and public contracts. Inspect callers and conventions before replacing a component. Clarify material ambiguity early while continuing independent authorized work; infer routine details from the available context.

## Define evidence before significant implementation

Identify inputs/outputs, source of truth, states, invariants, important errors and the expected user-visible result. Keep the contract as small as the task allows. Use the host's architecture: a plugin has a host lifecycle and files; a static site need not gain authentication or a database; a service may need transactions. Add abstractions, queues, caches or infrastructure for an identified requirement, not an enterprise appearance.

Choose checks that could reveal a wrong implementation. Unit tests cover logic; integration checks cover real boundaries; E2E covers important user paths. A mock that always succeeds does not verify a real service. For a reversible low-impact edit, an existing check or direct verification can be sufficient; do not add tests that simply restate the implementation.

## Implement and verify one complete capability

Follow the relevant path from input/UI through logic, effects or persistence to success, error and recovery. Include authorization at the trusted boundary where applicable. For a plugin, exercise the actual host when verifying its integration; a browser demo alone is insufficient.

Loop: **inspect/reproduce -> specify useful evidence -> implement -> run affected checks -> inspect diff and behavior -> repair concrete gaps.** Use test-first when it helps specify behavior. Finish necessary debugging and required checks; do not remove tests or weaken contracts to get a passing result. Broaden verification when changes create broader risk, not automatically after every small repair.

Preserve accepted frontend design while integrating real behavior; use Design Kit for changed UI states. Verify loading, empty, populated, invalid, slow/failed and success states where they belong to the feature. Do not call a visual mock a working backend or infer persistence from a success toast.

## Data, security and performance

Select controls by actual risk. Verify access across users/tenants where relevant; validate untrusted input; keep secrets out of code, chat and logs; preserve session and file boundaries. External URL fetches need appropriate network/redirect controls; file mutations need bounded paths and conflict handling. Select relevant [OWASP ASVS](https://owasp.org/projects/asvs) requirements for web applications without claiming certification.

For schema/data changes, verify constraints, migration compatibility, repeat/retry behavior and rollback or recovery where needed. Protect the originals and account for concurrent edits. For host integrations, check load/unload, reopen, compatibility and resource cleanup as applicable.

Measure the suspected performance bottleneck before optimizing. Use realistic data and the product's budgets; record the conditions and limits. Avoid building a new observability platform for a local diagnostic. Preserve maintainable boundaries, clear naming and a canonical source of truth.

## Completion and release

Close when the requested behavior and important recovery paths work, required checks pass, the diff preserves scoped contracts/data, and material regressions are resolved. Report any untested host/service, missing credentials or environment limitations. Passing tests is evidence for the tested behavior, not complete security or production readiness.

Review substantial/sensitive work against requirements, diff and evidence. Use independent review only when requested, required, or available and authorized for the risk; no automatic agent committee. A repeated failure must change the hypothesis or identify the blocker. Explicit user budgets take precedence; never mark incomplete work complete.

Deploy, merge, publish or perform consequential data operations within existing user authorization and project requirements. Prepare the concrete diff, checks and recovery plan before requesting any missing approval. Report what changed, why, actual verification and material limitations. Preserve only the state the next task needs.
