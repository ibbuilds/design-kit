# Validation record

## 0.3.4 finalization — 2026-09-05

27 deterministic package, source-preference and retained-library tests passed,
including cross-session byte deduplication, indexed retrieval, legacy receipt
compatibility, scoped/paged search and exclusion of development machinery from
distribution. Official plugin and skill validators passed; the skill validator
required Python UTF-8 mode on Windows. PyYAML was supplied from a task-specific
temporary dependency directory, without modifying either validator.

A read-only search found all 33 existing retained images; Kudanil captures were
retrieved from legacy receipts without migration or re-download. No comparative
benchmarks or new Figma designs were run. The user's acceptance of the improved
prior design supports the consolidation direction; it does not prove every future
model/task will produce the same quality. Historical records below remain historical.

Installed `0.3.4+codex.20260905080553` through the existing personal marketplace.
All 36 non-manifest runtime files match repository content; installed Markdown links
resolve, and development-only files are excluded. The installed library helper
retrieves existing Kudanil captures. A new Codex task is required to load the refreshed
skill; no live design-quality claim is made by this packaging check.

Current as of 2026-09-04. Acceptance is defined in [acceptance.md](acceptance.md).

## Verified before the targeted restructuring

- Official plugin and skill validators passed for the working 0.2.0 package.
- Twenty-two deterministic Python tests passed, including manifest/link checks,
  reference-policy precedence and replacement behavior, and cleanup safety.
- Supported local installation exposed the primary skill in fresh Codex invocations.
- Activation, non-activation, narrow-edit, missing-tool, reference-authority, A1
  degradation, retention, and relevance behavior were exercised with read-only
  model probes. These are routing evidence, not visual-quality evidence.
- Official Figma 2.0.21 tools were authenticated and proved editable native create,
  revision, node inspection, and render access in the explicitly authorized
  `Test Plugin` draft. A/B/C remain unchanged historical mechanical specimens.
- A live approved-source reference exercise proved external retained storage,
  provenance, actual image inspection, and A1 query capability. Its first active
  set failed the stricter task-relevance standard; files remain retained and the
  affected visual conclusions are invalid.

## Targeted restructuring

Implemented from the audit evidence:

- artifact adequacy plus six optional archetype lenses;
- deeper on-demand typography, composition, rhythm, art-direction, and motion craft;
- stronger content/IA reasoning and reference coverage roles;
- artifact-based evaluation with material-defect/hypothesis/taste/intentional classes;
- same-state render/geometry rules and batched Figma call guidance;
- explicit specialist classifications; Impeccable 4.2.0 installed user-wide for a
  later development benchmark without project context, hooks, or repository files;
- a six-family representative benchmark plan and a reduced routing probe set.

No Figma tool was called during this restructuring. Post-change verification:

- official `validate_plugin.py`: passed against the repository root;
- official `quick_validate.py`: passed against `skills/design-director`;
- deterministic suite: all 23 tests passed, including the six-family benchmark contract;
- JSON parsing: manifest, source registry, four probes, and six benchmarks passed;
- local reinstall: `design-kit@personal` installed as
  `0.3.0+codex.20260904204718`;
- reduced read-only probes: all four completed. Complete-portfolio activated and
  loaded adequacy plus the portfolio archetype; typography-only activated without
  loading extra modules; unrelated backend engineering did not activate; missing
  Figma capability correctly withheld edit and visual-verification claims.

The host's configured `gpt-5.6-sol` required a newer CLI than the installed binary,
so probes used the CLI-supported `gpt-5.5` compatibility override. The first sandboxed
attempt also failed before model execution because Codex could not write its own state
database. Neither failed attempt produced behavioral evidence. Retained probe evidence
is stored outside the repository under
`%LOCALAPPDATA%/design-kit/benchmarks/legacy-cli-validation-2026-09-04/`.

## Representative quality benchmarks

Two of the six representative families in `evals/benchmarks.json` ran on
2026-09-04 as controlled comparisons: a complete multidisciplinary designer
portfolio and a dense analyst dashboard with comparison and drill-down. Each used
`gpt-5.5` at high reasoning, the same brief, the same retained reference images,
equivalent local Figma access, and separate blank authorized sections. The baseline
prompts prohibited Design Kit and other design skills; the treatment prompts invoked
Design Kit 0.3.1 only. Matching start renders had the same SHA-256. Outputs, prompts,
agent reports, fresh final renders, live node inventories, manifests, and blind
pairwise evaluations are retained under
`%LOCALAPPDATA%/design-kit/benchmarks/portfolio-controlled-2026-09-04/` and
`%LOCALAPPDATA%/design-kit/benchmarks/dashboard-controlled-2026-09-04/`.

The blind portfolio comparison selected Design Kit with 78% confidence. It improved
positioning, typography, information architecture, and cross-page visual coherence;
the baseline's first viewport had a severe monogram/body collision. The Design Kit
case-study header still clipped its introductory copy beneath the metadata strip,
so the treatment is materially stronger but not correction-free.

The blind dashboard comparison selected Design Kit with 82% confidence. It improved
workflow depth, selected-row continuity, evidence/provenance structure, state coverage,
and product character. Its main defect was a discontinuous-looking trend line built
from separated line segments; one alert and the close control also remained cramped.
The baseline had cleaner chart continuity but weaker prioritization, more generic card
treatment, and unused drill-down space.

Live structure inspection found zero Auto Layout nodes, components, or instances in
all ten root benchmark frames across both conditions. The frames contain editable
native text and shape nodes, but this is a repeated Figma-construction weakness and
limits the construction-quality claim. The two results support a causal hypothesis
that Design Kit improves design reasoning and system coherence while its current
guidance does not reliably convert that advantage into robust responsive Figma
structure or prevent local overlap/chart defects. No Design Kit change was made from
these first two results; the remaining four benchmark families and specialist benefit
remain unverified.

A1 MCP is configured and previously queried, but is optional. Checklist Design and
Interface Design are not installed in the current runtime. Impeccable is installed
for a future task/runtime refresh but has not been invoked; its normal mandatory
project setup remains incompatible with Design Kit's user workflow.

## Local Figma transport migration

Validated on 2026-09-04 against `southleft/figma-console-mcp` release `v1.40.0`,
pinned to commit `e4d5605e6108cd0b21a950f6f57fc189749bd2eb`. Practical due
diligence confirmed an MIT license, active maintenance, substantial public usage,
documented local operation, and a successful source build. The local transport runs
through the Figma Desktop Plugin API over loopback; no Figma personal access token
was configured. Cloud, remote SSE, filesystem-scanning, comments, version history,
FigJam, Slides, design-system automation, cross-file arbitrary execution, and code
accessibility scanning tools are excluded from the Codex allowlist. Arbitrary
single-file `figma_execute` remains available but approval-gated.

The local bridge connected to the explicitly authorized `Test Plugin` file and
passed a real smoke test: file/status/selection reads, current screenshot capture,
native frame and Auto Layout creation, text creation and editing, component and
instance creation, variable creation and binding, structured property writes,
batched changes, structural reinspection, and fresh post-write screenshot evidence.
All work was isolated in section `32:11`, with root frame `32:12`. Baseline specimens
A/B/C (`5:7`, `5:8`, `5:9`) retained their names, geometry, layout values, and child
counts.

The migrated `design-kit@personal` build was installed as
`0.3.1+codex.20260904220514`. A fresh Codex invocation loaded `$design-director`,
routed exclusively through `figma_console_local`, inspected frame `32:12`, captured
current evidence, and made bounded structured edits to the Component Zone. Its
first resize fixed clipping but harmed the composition, so it restored the original
height. A final bounded Auto Layout correction set node `32:21` to 8 px item spacing
and 16 px vertical padding. Fresh plugin-rendered evidence confirmed all three
component rows are visible with balanced spacing; structural reinspection again
confirmed A/B/C unchanged. This verifies transport selection, guarded write access,
same-state inspection, visual checking, and corrective iteration. It remains a
small integration specimen, not a representative Design Kit quality benchmark.
Its manifest and image evidence are retained outside the repository under
`%LOCALAPPDATA%/design-kit/benchmarks/transport-smoke-2026-09-04/`; no validation
record depends on Windows Temp.

## Runtime lifecycle cleanup

A bounded cleanup on 2026-09-04 classified Design Kit-created artifacts under
`%LOCALAPPDATA%/design-kit/`: user-controlled `references/`, retained
`benchmarks/`, minimal `sessions/`, bounded `logs/`, disposable `temp/`, and the
single required `tooling/` dependency. Historical development/probe evidence and
the transport screenshots moved into managed benchmark directories with manifests.
Confirmed scratch downloads, duplicate temporary validator dependencies, the stopped
MCP driver, empty test directories, and Python bytecode caches were removed. The
reference session was unchanged. The pinned bridge build remains in `tooling/`
because the active Codex MCP configuration executes its `dist/local.js`; the Figma
Desktop plugin counterpart remains under `%USERPROFILE%/.figma-console-mcp/plugin/`.
