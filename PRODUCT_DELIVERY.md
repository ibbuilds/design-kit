# Deliver a complete frontend capability

Use for substantial requested frontend features or integrations. Local changes use [SOFTWARE.md](SOFTWARE.md) directly. Design-only work stays in [SKILL.md](SKILL.md). This route connects outcomes to frontend evidence; it adds no backend, infrastructure or release scope.

## Establish the outcome and boundaries

Identify the user's task, starting state, successful result and important failure/recovery paths. Separate requested behavior from assumptions and proposed extras. Inspect the existing implementation, canonical components, API contracts and actual check commands. Probe an unfamiliar integration before expanding it.

Retain a small acceptance map in the target's existing issue/spec/record only when useful:

| Required outcome | Existing boundary | Evidence | Status |
| --- | --- | --- | --- |
| User submits a valid form | UI -> existing API client | Exercise valid/invalid input, pending feedback and the actual response when authorized | Planned / implemented / verified / blocked |
| Failed submission preserves input | Request/state/recovery | Controlled failure, retained work, useful retry without duplicate effects | Planned / implemented / verified / blocked |
| Interface follows the accepted system | Canonical tokens/components | Comparable desktop/mobile renders and affected interaction states | Planned / implemented / verified / pending human review |

These examples do not require forms or APIs in every project. If a needed service does not exist, disclose the missing contract and an explicitly labelled frontend mock; do not implement a backend under this kit.

## Complete the actual user path

Implement useful capabilities in dependency order, reusing accepted design and target conventions. Include connected navigation, task progression, feedback and recovery rather than isolated attractive screens. Keep the application runnable and preserve state across sessions with compact existing records.

Inspect the running result against the original brief, approved references/system and actual requirements. Challenge the outcome with relevant awkward content, failure, stale/slow responses, keyboard paths and responsive changes. Review the real diff and raw check evidence. A same-agent review is not independent; a separate reviewer is conditional on actual authorization.

For browser checks, use controlled data, stable accessible locators and condition-based assertions. Mock uncontrolled third parties when needed for reproducible failure checks; distinguish that evidence from live integration verification. Screenshots establish visible states, not successful service effects.

## Present the result and limits

Present the working interface, meaningful visual/behavior changes, affected checks and remaining gaps. Mark each important requirement implemented, verified, failed or untested with its evidence. Do not equate a build, success toast or a passing mock with production readiness.

Use relevant QA for responsive behavior, loaded assets/fonts, keyboard/focus, content hierarchy, state recovery and frontend performance. A marketing surface and a dense application need different evidence. Preserve closed design decisions and obtain review for material visual departures.

Continue requested frontend corrections without reauthorizing their existing scope. Deployment or publishing needs its own existing authorization; migrations, backend services and operational infrastructure remain outside this procedure. No automatic monitoring, additional agent team or mandatory process documents.
