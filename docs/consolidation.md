# Product consolidation — 0.5.0

Implemented 2026-09-05 against the actual installed baseline
`0.4.3+codex.20260905123124`, whose 48 files matched the starting repository except
the generated manifest suffix. The user's older 0.4.1 baseline was not substituted
for the actual runtime. Existing uncommitted work and historical evidence were preserved.
Installation evidence is recorded in [validation](validation.md).

## Architecture and material changes

One primary skill routes relevant intelligence to the user's selected primary model:
project truth → Experience / visual references / creative direction / asset direction /
finish and craft → editable Figma → actual visual feedback. These are capabilities,
not phases. No extra runtime file, service, provider abstraction, agent or data schema
was introduced. Fourteen of the 48 distributed files changed from the installed baseline.

- **Merged/replaced:** the duplicated art-direction packet in `process.md` and broad
  thesis/underdesign guidance now have one owner in `craft/art-direction.md`. Creation
  is a smaller conditional connection between context, material, governing surface and
  expansion. It no longer implies a separate direction-lock ceremony.
- **Strengthened in place:** Task Design DNA carries observed relationship → adaptation
  → uncertainty, with specific mass, focal, type/image, plane, rhythm and omission
  examples. The visual thesis makes a causal choice. An optional signature must serve
  content and usable behavior; ordinary controls need no showpiece.
- **Assets:** existing semantic veto remains. Visual anchors identify exactly what
  they establish. A verified master supplies actual image input for related edits;
  crop/angle/scene changes have explicit invariants. Family and placed-crop comparisons
  can reject individually attractive but incompatible results. Preparation covers
  editing, isolation, masks, real alpha, relighting/grading and purposeful compositing;
  exact UI and type stay native. No asset inventory or contract file is mandatory.
- **Finish:** existing microtypography, control, surface, edge and composition craft
  remains. Plane count, perspective, occlusion, scale, material and light determine
  depth; shadows are one cue. Flatness, density and restraint remain valid. Inspect
  macro, relevant section and implicated detail, including responsive expression.
- **Removed:** complementary retrieval's one-image-per-role exclusion. It had forced
  a real edge query away from a relevant control toward incidental page-edge content.
  Results now expose the matching mechanism, partial role terms, reuse and exact
  cause/effect repeats. Declared observed roles help disambiguate incidental words;
  task context precedes source diversity. Semantic complementarity remains human/model
  judgment. Cause/effect paraphrases are not algorithmically understood.
- **Removed:** the two-major-attempt stopping cutoff. A failed intervention calls for
  new diagnosis/evidence or a simpler direction; stop when no credible next improvement
  remains, a material user preference is unresolved, or the user stops. This permits
  justified correction without rewarding blind retries.
- **Other end-to-end fixes:** explicit Experience reads omitted by result limits are
  now reported as deferred. Supplementation already authorized is not asked again.
  Figma guidance distinguishes local instance edits from shared-source changes, restores
  live human context on resumption, and explains section capture when export caps make
  tall pages unreadable. Redundant Figma scope/delivery prose was consolidated.
- **Placement:** dedicated pages for substantial new work, explicit edits in place,
  meaningful desktop/mobile/iteration organization. Benchmark mode requires explicit
  intent or strong comparative file evidence; preserve runs and follow the actual naming
  convention without invented model identity. No test naming enters normal designs.
- **Demoted:** legacy nested-model evaluation instructions are explicitly historical
  in `evals/README.md`; no evaluator ran. Development machinery remains excluded from
  the installed plugin. Canon, typography, composition, rhythm, interaction, platform
  distinctions and source authorities were preserved rather than taste-rewritten.

## Concrete checks and outcomes

**73 deterministic tests pass** (68 baseline + five regressions). Three selected new
regressions fail against 0.4.3: wrong distinct edge candidate, missing coverage/reuse
information, and silently omitted direct Experience reads. They pass with 0.5.0.
Additional regressions cover input/scope bounds and task relevance before diversity.
Whole-suite tests retain hashes, source restrictions, provenance, motion exclusion,
selective reads, package boundaries and lifecycle safety. Schema success is not design
quality or automatic skill activation.

Real-corpus complementary retrieval now reuses Realistic Button for shadow and edge,
with distinct mechanisms and explicit reuse. Product presentation exposes only a
partial `product` match. Motion remains a real missing retained-image candidate.
Source-specific discovery remains available; missing evidence is not filled with tags.

Read-only current Figma inspection covered the existing MARGEN hero, reasoning section,
its raster and relevant structure in the authorized test file. The visible raster has
fibrous stepped sheets and a line: it supports material atmosphere, but cannot by itself
establish research/evidence-document meaning. Under an explanatory document contract it
is insufficient. The surrounding native decision record supplies the actual semantic
information. No claim that these existing pixels are a new 0.5.0 result; no Figma edit
was performed. A still cannot establish the throughline's motion.

A new built-in image-generation check produced an original ceramic desk-lamp master.
The primary inspected actual pixels: illuminated underside, stem, base and cord make
the lamp legible; material, light and quiet type space are coherent. It is adequate as
a product-material test master, not a certified elite design or engineering model.
The inspected macro-pad reference informed only material separation, without copying
its identity or geometry. The master was then supplied as the actual edit input.

**The isolated variant failed and was rejected.** It preserved a broadly related visual
world but changed the shade/geometry and returned an RGB PNG containing a painted
checkerboard. Pillow inspection confirms no alpha channel. Neither family resemblance
nor an image tool's successful response satisfies exact preservation or transparency.
The runtime already required rejection; guidance now also names checking file alpha
when available. No external provider, silent CLI fallback, manual pixel workaround or
false extraction claim was introduced. The usable rectangular master remains available.
Both generated outputs are retained as explicit development evidence outside the package.

Primary-session scenario applications (not independent or automatic activation tests):

| Situation | Applied decision |
|---|---|
| Research visual reads as slabs, without documentary cues | Reject for that meaning; clearer cues/metaphor, native document material or omission. Do not rationalize with the prompt. |
| Related assets drift in geometry/light | Compare with master and reject violated invariants; do not regenerate unrelated pictures independently. Actual isolate test exposed this. |
| Flat elite editorial | Type, optical spacing, pacing and signature carry finish; no compulsory 3D, shadow or image. |
| Spatial product composition | Establish supporting/overlapping planes and light; judge specific separation/contact in pixels. |
| People with fused fingers/waxy skin | Reject supplied defects when realism is intended; no fresh people-generation test claimed. |
| Illustration with mixed outlines/perspective | Judge authored shape language and context; no photorealism requirement or fresh illustration test claimed. |
| Narrow button edit | Core + target/affected craft and fresh render; no DNA/asset/finish route by default. |
| Mobile loses focal crop or signature | Recompose meaning, scale and interaction benefit; desktop approval cannot verify mobile. No new mobile design was built. |
| Incomplete product/asset brief | Recover existing context; make reversible design assumptions, ask only a material missing fact. |
| Missing image/Figma tool | State the exact gap and use a scoped authorized alternative; no invented writes, masks or verification. |
| Supplied-reference revision | Preserve target, approved direction and restrictions; no research restart or new page. |
| New substantial surface / explicit frame edit | Dedicated professional page / existing frame respectively. Current comparative file supports benchmark inference, but no naming write was executed. |
| Backend-only request | Design Director is inapplicable; no design resources. This is a reviewed routing decision, not fresh automatic activation evidence. |

## Attention cost and preservation

Measured with tiktoken 0.14.0 `o200k_base`, LF-normalized text and actual helper output.
These are scripted explicit routes, not model traces or tokenizer parity with the active
model. Excludes host/tool schemas, image tokens, Figma payloads, reasoning and network.
The profiler now includes creative direction on both operations routes and an explicit
asset/finish route on both baselines; historical 0.4.3 operations used a smaller route.

| Text route | Installed 0.4.3 | Consolidated 0.5.0 |
|---|---:|---:|
| Discovery metadata | 63 | 63 |
| Activated core | 676 | 675 |
| Shadow | 1,229 | 1,176 |
| Control with interaction craft | 1,760 | 1,707 |
| Form validation | 2,337 | 2,284 |
| Complex table | 3,631 | 3,578 |
| New operations direction | 9,789 | 9,987 |
| Landing direction | 8,318 | 8,516 |
| Expressive landing with custom assets + finish | 10,367 | 11,198 |

The core stays 3,506 characters. Conditional creative direction is 809 tokens, assets
1,691 and finish 991. Narrow paths save 53 tokens through Figma consolidation; substantial
paths pay for consequential direction, family and benchmark information. No claim that
every route is cheaper. Deferred hydration, exact-need UX retrieval, bounded narrowing
and session-local reuse remain. Runtime file count stays 48.

All 264 retained images, 250 useful analyses, 14 excluded-but-preserved records, four
motion bookmarks and other reference files remain byte-identical: 269 retained files
checked, excluding only rebuildable databases. All 21 source configurations, 12 authorities,
42 Experience entries, provenance registry and Canon remain unchanged. No migration,
reference deletion, production code, bundled image, new dependency or Git push occurred.

## Remaining quality gates and evidence basis

The six representative live design benchmarks were **not rerun**; no general elite-quality
or user-acceptance claim is justified. Current automatic activation requires a user-owned
fresh task. Real transparent editing and exact asset preservation failed this bounded test;
the architecture catches failure but cannot guarantee a tool will produce the desired asset.
Native responsive construction, people, illustration and motion were not newly exercised.

The corpus is heavily biased toward hero previews (196), with one mobile-labeled surface,
few operational/detail views and no retained inspected motion image. Four link-only motion
notes are useful but do not close every behavior gap. Better retrieval exposes this;
it cannot manufacture missing evidence or make low-resolution images prove micro-craft.
Honest primary visual judgment remains essential and cannot be proved by an attestation.

Technical sources actually opened 2026-09-05:
[OpenAI packaging](https://developers.openai.com/plugins/build/plugins),
[skills](https://developers.openai.com/plugins/build/skills),
[Figma page creation](https://developers.figma.com/docs/plugins/api/properties/figma-createpage/),
[image integration](https://developers.figma.com/docs/plugins/working-with-images/).
Built-in image tool schemas/installed imagegen skill and the live local bridge were also
inspected. Official docs support hooks while the validator rejects them: none is used.
Docs emphasize desktop installation, while this CLI's inspected help supports `plugin add`;
the established creator/cachebuster flow is retained. No validation was weakened.

Workflow lessons about visual anchors and authored moments are user-supplied direction
and original synthesis, not independently verified claims about named creators; see the
preserved [research record](research.md). New aesthetic guidance is labeled heuristic.
Failures addressed: ARCH (duplicate direction guidance, forced reference diversity, retry
cutoff), TOOL (silent UX deferral, missing alpha), CONTEXT (shared edits/resumption), and
MODEL (semantic/identity drift). A generation failure remains a recorded failure.
