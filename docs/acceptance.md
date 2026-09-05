# Acceptance contract

Established 2026-09-04 and revised after the first live design audit. Evidence and
gaps live in [validation.md](validation.md). Missing or stale evidence is unverified.

## Primary gate: representative design quality

Design Kit is ready for a quality claim only after authorized live Figma benchmarks
cover the six families in `evals/benchmarks.json`: portfolio/showcase,
marketing/product, dense dashboard, productivity application, mobile flow, and
editorial reading.

Each benchmark must demonstrate:

- the designed artifact or connected set adequately satisfies the exact request;
- content and IA support the user jobs with realistic depth and relevant states;
- references, when useful, are relevant to named decisions and visually inspected;
- the editable Figma result is judged from current renders and matching structure;
- construction uses appropriate Auto Layout, components/states and resilient text
  behavior where the artifact's repetition or content flow warrants them;
- composition, typography, hierarchy, proportion, rhythm, spacing, art direction,
  interaction, coherence, originality, restraint, detail, and applicable
  accessibility are evaluated against the brief and reference evidence;
- revisions target material defects or credible hypotheses, preserve strengths and
  human edits, and stop when remaining differences are predominantly taste;
- tool and specialist use is reported from actual calls, not configuration or docs.

A successful write, complete frame tree, policy-compliant response, or schema pass
does not satisfy this gate. Static Figma cannot certify production accessibility,
runtime behavior, performance, or user acceptance.

## Supporting gates

| Gate | Required evidence |
|---|---|
| Native package | Official plugin and skill validators pass; local links resolve; one primary skill is discoverable after supported installation. |
| Activation | A representative design request selects Design Director; unrelated engineering does not; a narrow request stays narrow. |
| Knowledge routing | Adequacy and only the relevant archetype/canon/craft modules are available without loading the entire library. |
| Source integrity | Consequential technical/UX guidance has scoped sources and dates; uncertain or conflicting evidence remains explicit. |
| References | Source authority, exclusions, configurable pools, role coverage, visual inspection, task relevance, broad-pool/working-set distinction, saturation, and user-controlled retention behave as specified. |
| Optional integrations | Figma capability is checked at runtime; A1 and specialists degrade gracefully and are never silently installed or falsely reported as used. |
| Lifecycle safety | Only explicit cleanup can remove Design Kit-owned unchanged runtime data; traversal, links/reparse points, changed/foreign files, originals, Figma artifacts, and repository files remain protected. |
| Figma evidence | Writes stay in the authorized target; related changes are batched; prior renders become stale after meaningful writes; fresh targeted renders verify current claims. |
| Simplicity | No production frontend, bundled reference images, project memory, mandatory workflow, copied specialist corpus, server, database, or analytics layer. |

Cheap deterministic checks should cover manifests, links, frontmatter, safety helpers,
source configuration, obvious activation/non-activation, and a few high-value routing
boundaries. Do not expand wording probes to compensate for missing live visual evidence.

For a failed gate, record the evidence, consequence, correction hypothesis, smallest
change, and retest needed. Never weaken a gate, hardcode benchmark answers, or claim
quality from historical specimens known to be shallow.
