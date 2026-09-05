# Optimization and hardening 0.4.2

Installed 2026-09-05 as `0.4.2+codex.20260905115121` from the existing
`design-kit@personal` source. This is a backward-compatible disclosure/retrieval
and default-placement patch. The primary model remains the designer; the healthy
local Figma bridge remains transport. No vector database, new model, evaluator,
background service, mandatory phase or workflow engine was added.

## Measurement and reproducibility

Baseline is the actual installed `0.4.1+codex.20260905102316`, not Git HEAD (the
repository already contained its uncommitted development). Before editing runtime,
captured its text and real corpus retrieval. The final reproducible scripted routes
are in [profile_context.py](../scripts/profile_context.py). Profiling is development
only and excluded from the package. It writes a temporary SQLite cache, not receipts.

Method: tiktoken 0.14.0, `o200k_base`, exact counts of normalized LF text and emitted
JSON. **Selected-model tokenizer parity is unavailable.** These are plausible explicit
route replays, not measured model activation or end-to-end production traces. Host
instructions, unrelated installed skills, tool schemas, Figma state/render payloads,
image tokens, reasoning and transport latency are excluded. No hidden-cost savings
are claimed for those. Counts are reproducible for the preserved corpus and routes.

| Context | 0.4.1 chars / tokens | 0.4.2 chars / tokens |
|---|---:|---:|
| Discovery frontmatter contents | 311 / 63 | 311 / 63 |
| Activated SKILL.md, including frontmatter | 5,328 / 1,035 | 3,340 / 638 |
| Body only | 5,007 / 970 | 3,019 / 573 |

Discovery metadata is already precise and remains unchanged. The activated core is
not loaded for unrelated tasks. The route table counts the full activated file once.

| Route | Before tokens | After tokens | Helper calls before → after |
|---|---:|---:|---:|
| Slight shadow revision | 1,728 | 1,191 | 0 → 0 |
| Button dimensionality | 2,145 | 1,722 | 0 → 0 |
| Form validation | 4,094 | 2,299 | 1 → 1 |
| Complex editable table | 6,109 | 3,593 | 1 → 1 |
| Operations workspace | 13,085 | 8,872 | 2 → 3 |
| Full marketing landing | 10,513 | 8,109 | 1 → 2 |

Shadow uses core + Figma; button additionally reads interaction/motion craft (now
including specific surface-depth heuristics). Form reads the validation section.
Table reads comparison, selection, filtering and keyboard knowledge. Operations
reads selection, live/stale/command state, filtering and keyboard knowledge plus
creation, quality and composition. Landing retains art direction, typography,
composition, quality, credible-content guidance and asset guidance in creative runtime.
Creation routes include the **new** placement document; its cost is not hidden.

Operations and landing replay six old versus four new reference candidates, selecting
the same first two. The new path hydrates both in one extra call. The first four
candidate identities and selected full observations are preserved. Exact selected
UX section texts and source IDs match the baseline. This verifies availability and
selection consistency, not relevance precision or aesthetic acceptance. The user can
expand results, use complementary retrieval or request `--full`; four is a starting
count, not an adequacy rule. No external browsing is triggered by these routes.

The extra hydration call is a real tradeoff. Fewer tokens do not guarantee lower
end-to-end latency. All-selected requests can use `--full`; already selected references
and stable knowledge can be reused without repeating discovery. No forced two-stage
lookup was imposed on a precise UX need.

## What became smaller or faster

- Core: removed the long design-ownership enumeration, repeated synthesis/retention
  statements and the Canon link catalogue. The essential scope/evidence rules remain.
- Visual retrieval: acquisition schemas/procedures moved to a conditional document;
  it is absent from sufficient-corpus paths. Source lists/modes are resolved by the
  existing policy helper instead of rereading registries. Numeric exploration ranges
  that could anchor unnecessary research were replaced by evidence sufficiency.
- Experience: removed the repeated 12-authority table and complete authority records
  on every result. Full selected records remain available through `--authority-info`.
  `--search` returns candidate metadata; `--read` hydrates selected sections. A precise
  `--need` directly returns its complete applicable section. Provenance retains source
  identity, URL, type, scope and date; no authority is relabeled as visual intelligence.
- Figma: kept transport, scope, fonts, Auto Layout, native editability, partial-failure
  recovery and fresh render requirements. Naming/iteration details load only for new
  creation. Repeated stopping prose now points to the existing quality rule.
- Helpers: compact JSON serialization, per-operation receipt reuse, one index sync and
  one policy resolution across complementary roles. Each separate search/hydration
  still rechecks current restrictions and bytes. No persistent freshness shortcut.
- Bookmark retrieval now enforces optional path scopes and resolves policy once;
  this closes a concrete restriction gap in the motion/source-context route.

Five warm in-process samples on the same machine/corpus, median elapsed milliseconds:

| Operation | Before | After |
|---|---:|---:|
| Precise Experience lookup | 22.32 | 1.21 |
| Visual search | 1,136.01 | 178.02 |
| Three-role complementary retrieval | 1,180.88 | 197.72 |

These exclude process startup and network/model latency. Experience discovery now
reads no Canon sections; a precise form lookup reads one rather than validating all
38 first. Full `--validate` still checks every section. Receipt reuse removes repeated
parsing within a call; hashes and permission checks were not removed. Timing samples
and per-file/output token accounting are retained with the raw profiles.

## Gaps reviewed and bounded changes

- **Multilingual/bidi:** added W3C base direction, phrase isolation, mixed numbers/URLs,
  caret/reading-order limitations; Apple-specific mirroring separates navigation from
  physical direction, digits, photographs and logos. These are two scoped sections.
- **Scheduling:** one scoped section distinguishes wall time, named zones, offsets,
  recurrence, floating dates and DST ambiguity. W3C's time-zone publication is explicitly
  an informative Group Draft Note, not an endorsed Recommendation. Series scope,
  conflicts, participant acceptance and recovery are labeled heuristic/project contracts.
- **Professional tools:** one scoped section adds predictable named undo, visible
  results, meaningful grouping and distinctions among preview, commit, selection,
  saving and collaborative conflict. No unsupported history/backend guarantee or
  Apple shortcut is imposed on other platforms.
- **Mobile/responsive:** strengthened existing craft around priority/order, crop,
  detail routes, navigation, sticky controls, measure and touch reach. Paired real
  states versus an inferred recomposition are explicitly distinguished. No new
  mobile screenshot or empirical responsive behavior is claimed.
- **Motion:** existing four inspected link-only sequence notes remain searchable and
  unchanged; their discovery is explicit in the compact retrieval path, and path
  restrictions now apply. No new motion clip was acquired/inspected in this iteration.
  Static images still cannot satisfy motion searches; no video platform was introduced.
- **Small desktop previews:** retained limitations and full-image/crop inspection;
  did not upscale evidence claims or erase weak-but-preserved records.
- **Spatial/voice/XR, deep script shaping/line breaking, safety-critical/domain rules
  and unavailable paid research:** remain current, scoped authority/project retrieval
  questions. No generic substitute can establish those requirements. No authority or
  approved visual source was replaced to make coverage look complete.

All 38 original Experience entries **and complete section text** remain unchanged;
four additions bring the selective library to 42. Every original provenance record
and all 12 authority records remain identical as data. The 21-source visual registry
is byte-identical. All 264 retained assets and receipt records are unchanged: 250 useful
analyses, 14 excluded/preserved, zero pending. Motion bookmarks are byte-identical.
No data migration or retained-reference cleanup occurred.

## Figma default: safe primary-session dry runs

The following are primary-session policy applications against supplied synthetic state,
not an independent evaluator, new model session or live Figma test. No page/frame was
created or modified. They establish reviewed decisions; they do not prove future model
activation or API execution. A runtime decision engine was deliberately not added.

| Case / fixture | Reviewed decision |
|---|---|
| A: New landing, authorized product file, no destination | Dedicated `Product · Landing` page; preserve current page. |
| B: Redesign explicitly identified frame | Edit that frame; no new page, even if the change is substantial. |
| C: New dashboard, one clearly authorized active file | New concise page derived from the actual product/surface. Selection alone is not permission to overwrite. |
| D: Real second iteration, existing task page | Keep it on that page; align iterations with consistent scale-appropriate gaps and grouped desktop/mobile frames. |
| E: One solution, no iteration | Only its actual design frame/group; no invented alternatives or iteration copies. |
| F: Existing `Atlas / Checkout`, `Atlas / Research` convention | New workspace uses `Atlas / Workspace`; equivalent state naming within the page. |
| G: Only placeholder page names, no product branding supplied | Use `Operations workspace`; do not invent branding or use `Test`/`Output`. |
| Explicit page supplied for a new surface | Honor it; no dedicated-page fallback. |
| Two equally plausible files or no authorized file | Resolve context/tools first; ask only if still genuinely unresolved. |
| Retry after partial creation failure | Inspect for the already-created task page; do not create duplicates. |
| Plan/page limit prevents creation | Preserve existing pages; resolve an authorized alternative, without silent spillover. |
| No writer/render tool | Useful scoped reasoning and exact limitation; no claimed edits or visual verification. |

Default frame naming is `Desktop · 01` / `Mobile · 01`, then meaningful actual
iterations and clearly named intended final frames. Existing professional conventions
override this fallback. Consistent whitespace/alignment makes prior iterations
subordinate; no QA/process boards or giant visible FINAL label is required.

## Verification and limits

All relevant deterministic checks passed: existing source/authority boundaries,
retrieval decompositions, compact-to-full round trips, scope/exclusion/hash changes,
bounded result counts, per-call freshness, selective section reads, draft provenance,
platform/context restrictions, empty inputs, unknown inputs, missing sections, revision
behavior, package inclusion and local links. The suite ran 62 tests; their purpose is
regression prevention, not a quality score. Official plugin and skill validators passed
for repository and installed package. `git diff --check` passed.

Installed package: 46 files match intended source bytes, except the generated manifest
build suffix; all other manifest fields match. Installed compact search, batched selected
hydration, direct/deferred Experience retrieval and full registry validation passed.
Asset/receipt/bookmark preservation was rechecked after installation. No transport
configuration, plugin dependency or marketplace entry changed. A new task is needed
to discover the updated skill automatically; this running task's initial catalogue
does not refresh itself.

Observed development failures: **TOOL** optional legacy citation titles were initially
treated as required; corrected without rewriting old records. **VERIFIER** a receipt
read-count fixture included the non-session SQLite file; session enumeration now skips
non-session names before attempting receipt validation. **TOOL** Windows CRLF writes
caused diff whitespace failures; normalized only edited files to LF. All reruns passed.

Rejected: weaker generic craft wording; removing reference hashes/limitations; persistent
cache shortcuts that hide changed evidence; flattening mechanisms into tags; mandatory
discovery before a known section; automatic authority browsing; broader source expansion;
visual-quality claims from structural tests; and a destination workflow engine solely to
produce test counts. Craft and aesthetic synthesis retain their freedom and specificity.

Remaining limitations: lexical ranking is not semantic relevance or a quality judgment;
some redundant selected-candidate information and citation overlap remain; rich hydration
adds a call; full receipts still scan each request; small desktop previews and narrow
motion/mobile coverage remain. No post-intelligence 0.4.1 design-benchmark evidence was
present in repository docs. No new visual benchmark, Figma mutation, model delegation or
Git push was performed. The six live quality gates and fresh automatic activation are
not claimed as rerun or accepted.

Technical/authority pages actually opened on 2026-09-05:
[OpenAI plugins](https://developers.openai.com/plugins/build/plugins),
[skills](https://developers.openai.com/plugins/build/skills),
[Figma API](https://developers.figma.com/docs/plugins/api/figma/),
[createPage](https://developers.figma.com/docs/plugins/api/properties/figma-createpage/),
[W3C direction](https://www.w3.org/International/questions/qa-html-dir),
[inline bidi](https://www.w3.org/International/articles/inline-bidi-markup/),
[time zones](https://www.w3.org/TR/timezone/),
[Apple undo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo),
[Apple RTL](https://developer.apple.com/design/human-interface-guidelines/right-to-left).
Official docs retain hooks support while the installed validator rejects unused hooks;
none were added. Docs emphasize desktop local installation while this installed CLI
explicitly supports `plugin add`; its help and successful install resolve that surface
difference without changing validation or configuration.

Retained development evidence: `%LOCALAPPDATA%/design-kit/audits/optimization-0.4.2-20260905/`
contains original/final profiles, baseline package archive and profiler. It is explicit
development evidence, outside the reusable package. Tokenizer/validator dependencies and
ordinary caches are temporary development scratch, not installed runtime dependencies.

**Why does this version cost less model attention/tokens than 0.4.1?** Smaller activated
instructions, no acquisition/authority catalogues on ordinary retrieval, fewer candidate
annotations, selected hydration, compact machine output and session-local knowledge reuse.
Mechanical validation/filtering and receipt parsing stay in code.

**Why should that reduction not make UI/UX judgment worse?** Original knowledge, evidence,
sources, mechanisms and craft remain accessible and unchanged where decisions depend on
them. Selected details retain provenance and actual visual inspection. New knowledge is
scoped; the primary model still chooses meaning, synthesis and aesthetics. This is a
preservation argument supported by checks, not a claim of proven visual non-regression.
