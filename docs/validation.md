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


## Reference and Experience Intelligence 0.4.0

Validated and installed on 2026-09-05 as `0.4.0+codex.20260905094650` through the
existing `design-kit@personal` marketplace using the installed plugin-creator
cachebuster helper and `codex plugin add`. Repository base version is `0.4.0`.
All 44 runtime files match the intended source package byte-for-byte except the
manifest's generated build suffix; the remaining manifest fields match exactly.
Fresh-default resolution knows 21 visual sources and 12 separate Design Authorities.
No installed MCP dependency or Figma transport configuration changed.

55 deterministic tests passed. Official plugin-creator `validate_plugin.py` and
skill-creator `quick_validate.py` passed for both repository and installed skill/package.
The optional Experience helper resolves 38 scoped sections without loading the whole
Canon; shadow/form/complex retrieval uses zero/one/three sections in the representative
checks. The 21 primary-authored problem decompositions and 16 visual source routes are
retrieval checks, not model activation or new Figma quality benchmarks.

All 264 retained images survived installation unchanged. The original 33 images plus
one note match baseline SHA-256 bytes; provenance was preserved while actual visual
observations were added. Current corpus: 49 analyzed, 208 uninspected, seven excluded
but preserved. No claim that the entire corpus is analyzed or that motion was verified.
Evidence lives outside the package in
`%LOCALAPPDATA%/design-kit/benchmarks/intelligence-2026-09-05/`.

See [coverage, source access and limitations](intelligence-validation.md). SAP/Fiori
and Baymard's product-list page loaded through normal browser navigation after HTTP
client 403 failures; the runtime now records method-specific failure and legitimate
fallback rather than treating 403 as source rejection. Paid/private material remains
restricted. A new task is required to pick up updated skills; no nested model session
or new visual benchmark was run, preserving primary-model continuity and the explicit
no-Figma-write constraint. No repository push was performed.

## Visual-memory enrichment 0.4.1

Installed 2026-09-05 as `0.4.1+codex.20260905102316` through the existing
`design-kit@personal` source, official cachebuster helper and `codex plugin add`.
All 44 runtime files match the repository byte-for-byte, except the expected
manifest build suffix; all other manifest fields match. Repository base is 0.4.1.

57 deterministic tests passed (55 existing plus two motion-evidence regressions;
existing bookmark coverage now checks note search and unrelated-query rejection).
Official plugin and skill validators passed for both repository and installed copy.
Initial validators lacked PyYAML; installing 6.0.3 into task scratch resolved the
missing dependency without changing either validator. `git diff --check` passed.
Installed motion filtering and clipboard-note retrieval passed. All 264 image hashes
still match baseline after installation; prior receipt fields were preserved.

Corpus: 250 useful analyses, zero pending, 14 excluded but preserved; four inspected
motion sequence notes remain link-only. Detailed source counts, relevance review,
limitations and audit location are in [intelligence-validation.md](intelligence-validation.md).
No Figma design or source approval changed, no new visual benchmark ran, and no push
was made. Fresh model activation and six live design benchmarks were not rerun for
this bounded retrieval/corpus change; no user acceptance or design-quality proof is claimed.
Use a new Codex task to load the updated installed skill.

## Optimization and hardening 0.4.2

Installed 2026-09-05 as `0.4.2+codex.20260905115121` through the existing personal
marketplace and official cachebuster/reinstall flow. All 46 installed package files
match source, apart from the expected manifest suffix. Both official validators and
the relevant deterministic suite passed. All retained references, receipt data, motion
bookmarks, 21 visual sources and 12 authority records survived unchanged.

Activated core measured 1,035 → 638 `o200k_base` tokens; six explicitly profiled paths
also shrank. Exact selected-model parity and live activation are unverified. See the
[measurement, gap review, Figma-default dry runs and limitations](optimization-validation.md).
No Figma mutation or new visual benchmark occurred during this optimization release.

## Asset semantics and finish hardening 0.4.3

Installed 2026-09-05 as `0.4.3+codex.20260905123124` through the existing personal
marketplace. All 48 installed files match source except the manifest build suffix.
68 deterministic tests passed; official plugin and skill validators passed for
source and installed cache. Installed detail retrieval/hydration and restriction
checks passed. Asset and finish intelligence are conditional resources; discovery
metadata is unchanged and the activated core adds 38 measured `o200k_base` tokens.

One actually inspected button reference gained an edge-detail mechanism; all prior
observations, other receipts, 264 image bytes, motion bookmarks and 21 sources were
preserved. No Figma edit or new live benchmark occurred. Primary scenario walkthroughs
and a non-blind pixel re-review do not certify independent semantic judgment or
general design quality. See [implementation, measurements, exact checks and remaining
limitations](finish-validation.md). A new task loads the updated installed skill.

## Product consolidation 0.5.0

Installed 2026-09-05 as **0.5.0+codex.20260905125453** through the existing
`design-kit@personal` marketplace, official cachebuster helper and `codex plugin add`.
The actual starting installed runtime was 0.4.3. All 48 installed files match intended
source bytes except the expected manifest suffix; all other manifest fields match.
73 deterministic tests, official source/package/installed validators, installed retrieval,
hydration, source-scope, static-motion and Experience deferral checks passed.
`git diff --check` passed. All 269 retained reference files (264 images plus metadata)
and all source/authority/Canon data survived unchanged; no data migration occurred.

The original asset master was generated and visually inspected. Its attempted isolated
variant failed exact geometry preservation and returned RGB with a painted checkerboard;
it was rejected. Current MARGEN pixels and structure were inspected read-only. No existing
Figma design changed, no new Figma benchmark ran, and no nested model/evaluator or Git push
was used. Fresh automatic activation and the six representative live quality gates remain
unverified for this release. The core stays 675 tokens; narrow text routes save 53 tokens,
while the explicit expressive-assets route adds 831. These are profiler measurements,
not active-model token parity or proof of design quality.

See [architecture, concrete capability checks, context measurements and weaknesses](consolidation.md).
Explicit evidence is retained under `%LOCALAPPDATA%/design-kit/audits/consolidation-0.5.0-20260905/`;
ordinary task scratch was removed after retaining those records. Start a new Codex task
to load the installed skill; an existing task does not hot-reload its catalogue.

## Targeted contribution and finish update 0.5.1

Installed 2026-09-05 as **0.5.1+codex.20260905213034** through the existing personal
marketplace and official cachebuster/reinstall flow. Task relevance and mechanism evidence
are now separate; partial creative matches remain gaps. Existing conditional craft routes
support visible-gap retrieval, reference-relative finish and one credible material opportunity.
The 675-token core, narrow routes and mandatory-read count are unchanged.

80 deterministic tests, official source/distribution/installed validators and installed
retrieval checks pass. All 48 installed package files match intended source (manifest build
suffix excepted). Eight actually inspected visual-memory records were selectively enriched;
all 264 retained image hashes, prior analysis content, provenance, other records, 21 sources
and 12 authorities were preserved. No Figma modification, live benchmark, new source, nested
model, dependency or Git push occurred. Fresh activation and improved live output remain
unverified. See [changes, actual capability evidence, costs and limits](contribution-validation.md).

## Source/reference correction, included in 0.6.0

Installed 2026-09-05 as **0.6.0+codex.20260905220333** using the official packaging,
cachebuster and `codex plugin add design-kit@personal` flow. This includes the concurrent
foundation task's 0.6.0 changes without overwriting them. All **50 installed files** match
the source, except the expected manifest build suffix. Source, packaged and installed
plugin validation and source/installed skill validation pass. The correction's 96-test
suite passes; the combined checkout passes **106 tests**. Installed probes confirm Recent
retirement/provenance behavior, macro/specialist ranking, high-ambition scope filtering and
static-only motion rejection. `git diff --check` passes.

All **269 original non-SQLite reference files**, including 264 images and their provenance,
remain byte-for-byte unchanged. Source review covered representative visible material from
all 23 approved sources. No new source images were bundled, no retained item was blindly
upgraded to elite, and this correction made no Figma edits. High-ambition page retrieval
currently returns an honest gap until eligible mechanisms are actually assessed.

The isolated source correction adds 19 tokens to the 675-token core. The subsequently
combined 0.6.0 core measures 798 o200k_base tokens. Scripted broad routes load more optional
guidance; these measurements exclude image/tool costs and do not certify model activation.
The six live Figma benchmarks, complete playback across sources, device compositing and
human acceptance remain unverified. See [source review, A–P checks, nine capability cases
and limits](source-intelligence-validation.md). Explicit measurement and installation evidence
is retained under `%LOCALAPPDATA%/design-kit/audits/source-correction-20260905/`.
Start a new task to load the updated skill.

## Design Foundations 0.6.0

Implemented 2026-09-05 against the actual **0.5.1 source working tree**, already
containing source-tier, evidence-scope, spatial-composition, Product Presentation,
Asset Direction and Finish changes beyond the 0.5.0 baseline. Those capabilities
were inspected and preserved. This is a repository implementation record, not an
installation or visual-acceptance claim.

The architectural addition is one conditional reference, an optional deterministic
color calculator and focused tests. The primary skill now makes substantial net-new
creation foundation-first: product/evidence/direction inform real system objects;
semantic components and their instances construct the primary/responsive design.
Local edits remain local. Foundations and composition co-evolve through fresh renders
and feedback; no workflow engine, evaluator, subagent or approval phase was added.

Files changed by this request (excluding concurrent source-intelligence edits):

- Added `skills/design-director/references/design-foundations.md`,
  `skills/design-director/scripts/color.py`, and `tests/test_color.py`.
- Updated `.codex-plugin/plugin.json`, `README.md`, and
  `skills/design-director/SKILL.md`.
- Updated existing references `process.md`, `figma.md`, `figma-create.md`,
  `quality.md`, `craft/typography.md`, and `craft/finish.md`.
- Updated the existing development-only `scripts/profile_context.py` to include
  Foundations/type in complete-design routes, and this validation record.

The color helper implements 20-stop OKLCH ramps from a supplied anchor, configurable
endpoints/count/chroma, simple fixed-lightness/hue gamut reduction, canonical opaque
8-bit sRGB/HEX values and WCAG contrast. It preserves the anchor and reports removal
of redundant/nonascending quantized stops. It neither authors palettes nor creates
semantic roles, promises perceptual uniformity after quantization, or implements the
CSS gamut-mapping algorithm. Ten deterministic tests cover independent primary-color
vectors, round trips, gamut limits, anchor preservation, neutral ramps, custom counts,
serialization, duplicate removal, invalid/alpha input and CLI output. The 4.478:1
boundary remains below 4.5:1; comparison is not rounded into a pass.

Typography now selects one/two families by role, permits three only with a structural
reason, checks available faces and distinguishes reading/display/data needs. Real
text styles carry role properties; responsive roles preserve hierarchy. Components
are required by semantic reuse even at one instance, with relevant states/properties,
content-driven layout and actual instances on screens. System organization remains
compact within the established task page and benchmark naming conventions.

### Checks and limits

The first baseline run had 95 passes and one failure in the pre-existing animated
GIF/WebP test: its WebP subcase expected an empty search although the preceding GIF
had acquired valid motion evidence. A concurrent source-intelligence edit corrected
the assertion to exclude the specific unverified reference; this task did not modify
that test or weaken motion admission. The combined suite then passed **106 tests**
(96 existing plus 10 color tests), using `python -B -m unittest discover -s tests`.

Both installed official helpers passed against source:
`plugin-creator/scripts/validate_plugin.py` and
`skill-creator/scripts/quick_validate.py`. Their first invocation lacked PyYAML;
PyYAML 6.0.3 in task-local temporary storage resolved this EXTERNAL environment gap
without changing validators or plugin dependencies. `git diff --check` passed.

The existing route profiler ran with tiktoken installed only in task scratch. Its
scripted shadow/button/form/table routes omit Foundations, with zero extra color
helper or network calls. Complete operations/landing routes include Foundations.
The core measured 798 o200k_base tokens (694 in the concurrently corrected source
baseline); the new reference is 2,664 tokens and is conditionally loaded.
These are emitted-text measurements, not selected-model parity, observed automatic
activation, wall-clock design cost or image/tool payload cost.

Primary instruction walkthroughs, not live design benchmarks:

| Input or condition | Result of scope/dependency review |
|---|---|
| Complete SaaS landing / new dashboard | Direction before foundations; palette/ramps, real styles/variables and product-derived components before full composition. No generic kit or mandatory aesthetic. |
| Improve one button / fix card spacing / change shadow | Existing target/system inspected; no full ramps, type system, new page or foundation area. |
| Single search field in a new interface | Semantic control becomes a component despite one current use; screen consumes its instance. A unique hero arrangement can remain native one-off composition. |
| Missing product facts / unavailable font | Resolve material gaps or label reversible assumptions; verify an available fallback. Do not invent product evidence or silently claim unavailable faces. |
| Missing variable/write support | Use a suitable supported style fallback where possible and disclose lost propagation; no fake token claim. Missing write access does not authorize transport changes. |
| Palette or padding revision after composition | Update the authorized system source, preserve unrelated reuse/human edits and inspect affected instances and fresh renders. |
| Mobile adaptation / critique only | Shared semantic sources with responsive composition; critique still grants no write authorization. |

Official OpenAI [packaging](https://developers.openai.com/plugins/build/plugins) and
[skill authoring](https://developers.openai.com/plugins/build/skills), Figma
[variables](https://developers.figma.com/docs/plugins/api/figma-variables/),
[Plugin API](https://developers.figma.com/docs/plugins/api/figma/),
[node properties](https://developers.figma.com/docs/plugins/api/node-properties/) and
[text nodes](https://developers.figma.com/docs/plugins/api/TextNode/),
[WCAG 2.2](https://www.w3.org/TR/WCAG22/),
[CSS Color 4](https://www.w3.org/TR/css-color-4/) and
[original Oklab matrices](https://bottosson.github.io/posts/oklab/) were opened/read on
2026-09-05. Figma's HTTP response was empty; normal browser documentation succeeded.
An attempted Carbon typography URL was unavailable and supplies no new verified
claim. Existing scoped authority knowledge is preserved. The known unused-hooks
validator/documentation conflict is not implicated; no hooks or integrations changed.

The existing local Desktop bridge passed a live read-only health probe. A read-only
Plugin API query confirmed callable variable collections/creation/aliases/paint
binding, text/effect style creation, component creation, variants and font listing.
Thus semantic variables and typography styles are supported by the documented and
currently exposed transport. No system objects were created or edited to test
propagation: capability presence is not a successful-write or end-to-end proof.
No existing Figma benchmark was run, altered or overwritten. Fresh automatic
activation, live system binding/propagation, responsive construction, actual visual
quality and human acceptance remain for the explicitly requested future benchmark.

All **270 retained reference files**, including images, receipts/bookmarks and the
existing index file, matched the captured baseline byte-for-byte after tests. No
source/corpus/provenance asset was deleted. The visual source registry, retrieval,
acquisition and motion-test files received concurrent changes outside this request;
those edits were preserved, not reverted or attributed to Foundations. Existing
Figma transport, source hierarchies, UX authorities and single-primary ownership
remain intact. No frontend production code or bundled raster asset was added.

## Reconciled runtime 0.6.1

Verified and installed 2026-09-05. This record supersedes the ambiguous 0.6.0
installation status; historical workstream reports remain evidence of their own times.

| State | Exact version |
|---|---|
| Source tree | `0.6.1` |
| Distribution package | `0.6.1` |
| Installed and enabled | `0.6.1+codex.20260905221320` |

Starting checkout: 0.6.0 with 50 accumulated modified/new files. Starting installed
cache: `0.6.0+codex.20260905220333`. Direct comparison showed that this cache already
contained both Source Intelligence and Foundation-First, including the color helper.
Only later README wrapping and Foundation citation additions differed, apart from
the expected manifest suffix. The earlier “not reinstalled” Foundation report did
not account for the concurrent Source task's combined installation.

### Semantic reconciliation

Compared the shared runtime files with the archived 0.5.1 distribution, current
checkout and installed 0.6.0 snapshot. Reviewed `SKILL.md`, creation/process, Figma
transport/placement, quality, typography, Finish and README, plus their source/asset/
foundation references. Both additions coexist: scoped visual evidence informs the
direction; conditional foundations construct it; fresh visual and structural judgment
refines both. Single-primary ownership, existing transport, narrow revisions and
user stopping/authorization remain intact. No conflict markers, duplicated phase
sequence or contradictory activation contract required an instruction rewrite.

Three repository files changed semantically during reconciliation:
`.codex-plugin/plugin.json` (patch version), `README.md` (version and stale 21-source
count corrected to 23 with exact tier totals), and this record. Retained the late
citation additions. No skill/core, helper, source registry, test or architecture
change was needed; the core remains 798 o200k_base tokens. No new capability was added.
Staging the previously untracked development files exposed CRLF trailing-whitespace
diagnostics in `docs/intelligence-validation.md` and `evals/experience-retrieval.json`.
Normalized only their line endings to LF; content and test cases are unchanged.
This brings reconciliation to five changed files, with two formatting-only changes.

Source Intelligence is preserved: Recent canonical, Godly discovery inactive,
8 Tier 1 / 13 Tier 2 / 2 Tier 3 sources, Awwwards Tier 1, Landingfolio and Httpster
Tier 3, authority-before-similarity discovery, role-correct specialist priority,
individual/per-mechanism quality and scope, independent sibling qualification,
sequence evidence and first-frame-static limits, cross-domain mechanism retrieval,
anti-slide/spatial storytelling and accurate editable product presentation.

Foundation-First is preserved: substantial-only activation; principles; authored
basic palette and advanced perceptual ramps; deterministic 20-stop OKLCH/gamut/contrast;
semantic Figma variables; selected typography and reusable styles; spacing/layout and
used visual-language foundations; semantic components even at one instance; relevant
variants/properties and instances in screens; shared desktop/mobile system with
responsive adaptation; iterative system/artifact refinement; proportionate local edits.
Figma API/bridge support remains as previously verified; this integration made no
Figma calls or writes and does not claim a new end-to-end propagation test.

### Retained-file count reconciliation

The exact difference is `references/intelligence.sqlite3`. The Source workstream's
baseline explicitly excluded SQLite; the Foundation snapshot counted every file.
There was no new retained reference. The 269 original files comprise 264 images and
five provenance/support files. Every SHA-256 still matches the Source workstream's
`corpus-before.json`, after normalizing Windows path separators.

The index is intentional, rebuildable SQLite FTS cache maintained by the existing
`intelligence.py` `connect()` / `sync()` functions, not authoritative source material.
Its filesystem creation timestamp is **2026-09-05 09:44:27.206193 UTC**; last write
**10:21:01.494544 UTC**. These filesystem observations establish that it predates both
current workstreams, not the identity of the process that first created it. It holds
264 cached records in 1,470,464 bytes. Its hash also remains unchanged:
`65c064db5a954a29bab1f4e70d38aee1bca37f81e5bde43990551f9d1fb484ec`.
Nothing was deleted or moved to make the counts agree. Runtime probes rebuilt an
independent index in managed task scratch, leaving all 270 existing files untouched.

### Executed verification

- Complete source suite: **106 tests passed**, including all 10 focused color tests.
- Installed runtime: **100 existing runtime tests passed**, loading the six helper
  modules from the exact installed cache. Test adapters redirected existing explicit
  source-module references and the color CLI to that cache; six repository-only
  package tests remained in the source suite. No assertions or cases were weakened.
- Official plugin and skill validators passed for source, package and installed copy.
  The installed creator helpers were used unchanged, with their existing temporary
  PyYAML dependency. Working-tree and staged `git diff --check` passed after the
  two development-file newline corrections; validation rules were not weakened.
- Installed discovery probes: macro queries led with Tier 1; button motion returned
  60fps/Design Spells; typography returned Typewolf/Fonts In Use; branding returned
  appropriate Tier 2 sources; spatial storytelling returned Recent/Awwwards.
- Actual retained retrieval: 161 ordinary photography candidates, successful hash-bound
  hydration of two selected records, zero candidates for an empty allowed scope.
  High-ambition page and motion queries returned honest gaps (zero), without upgrading
  legacy observations. Positive/negative quality, scope, authority and sequence cases
  are covered by the installed synthetic tests.
- Installed Experience retrieval returned `form-recovery`; the color helper produced
  20 stops and kept `#777777` on white at 4.478089453577214:1, below 4.5:1.

Built with `scripts/package.py` and the installed official creator, copied the verified
50-file package to the existing `design-kit@personal` source, ran the official
cachebuster helper there, then `codex plugin add design-kit@personal`. The CLI reports
the exact installed build enabled. All 50 archive/package files match the repository
byte-for-byte. All 49 non-manifest installed files match source byte-for-byte; every
manifest field matches except the intentional `+codex.20260905221320` version metadata.
The marketplace source and installed cache match byte-for-byte with no extra runtime
files. Package SHA-256:
`683a204242c7b9fcf8854e033ce504f3ee6d12ca8e854801e0db10eb2cebb5a6`.

Explicit integration evidence and the distribution archive are retained outside the
repository under `%LOCALAPPDATA%/design-kit/audits/integration-0.6.1-20260905/`.
No benchmark, MARGEN edit, ASTER creation or other design occurred. Fresh automatic
activation, actual Figma propagation, rendered design quality and human acceptance
remain unproven. The next fresh benchmark task should load
**`0.6.1+codex.20260905221320`**; an already-running task does not hot-reload its skill.
