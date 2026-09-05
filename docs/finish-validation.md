# Asset semantics and finish hardening — 0.4.3

Implemented and installed 2026-09-05 as **0.4.3+codex.20260905123124** through
the existing `design-kit@personal` source. Repository base version: 0.4.3.
The installed cache contains 48 package files, verified equal to repository source
except the expected manifest build suffix. No marketplace entry, bridge configuration,
model setting, Figma artifact or approved source pool changed in this task.

## What changed

1. **Asset Intelligence:** new on-demand [asset guidance](../skills/design-director/references/craft/assets.md)
   makes section meaning and intended placement precede generation. Creating an
   asset activates it; ordinary revisions do not acquire an asset-planning phase.
2. **Semantic fidelity:** a few internal clauses describe depiction/purpose,
   viewer message, section relationship, metaphor and recognizable cues,
   material/form, composition role, integration and failure conditions. There is
   no persistent contract schema, mandatory report or planning tool.
3. **Rejection:** the primary model must describe visible output before comparing
   with the intended concept. Semantic/contextual failure vetoes acceptance;
   beauty, matching color/material and generation success cannot outweigh it.
   Correct the failed cue, edit/regenerate, change metaphor or omit. Removal from
   a design never implies deleting retained references.
4. **Generation/editing preparation:** prompts encode consequential subject cues,
   construction, scale/perspective, region/aspect/crop, light, occlusion and
   negative constraints. They must not suppress the cues needed for recognition.
   Existing image tools/skills govern execution; unavailable capabilities are
   reported without invented generation or extraction success.
5. **Transparency/masking/compositing:** isolate subjects only where independent
   positioning helps. Inspect real alpha, halos, matte fringes, fine edges and
   translucent interiors against intended backgrounds. Separate image, environment,
   shadow and graphic layers only when useful; align light/perspective/occlusion.
   Keep meaningful product text, controls and data native in Figma. Recheck meaning
   after cropping/shading and inspect the actual placed composition.
6. **Finish Intelligence:** new on-demand [finish guidance](../skills/design-director/references/craft/finish.md)
   addresses ambitious or credibly under-finished work. Correctness, coherent
   resolution and exceptional expression are different judgments, not scores or
   compulsory stages. Flat, monochrome and image-free work remain valid.
7. **Depth/shadow/materiality:** reason about plane relationships, contact,
   ambient separation, cast-light direction/distance, inset depth, highlights,
   occlusion and neighboring surfaces. Minimum coherent cues replace generic
   multi-shadow recipes. Intentional suspension is distinguished from accidental
   floating in a resting-object brief.
8. **Micro-craft:** examine thin-edge hierarchy, opacity, seams, nested radii,
   texture frequency, optical type/baseline/punctuation relationships, label
   readability, icon weight/size, arrows, control padding and relevant states.
   Existing typography/interaction guidance supplies detail without duplication.
   Responsive crops and small-scale shadow/texture behavior must be reconsidered.
9. **Detail retrieval:** `--role` can match the observed cause/effect inside a
   mechanism, not only its broad role label. Compact results prioritize that
   mechanism. Lexical variants cover shadow, layering, translucency, edge, masking
   and related terms. Texture, tactility, material and depth are no longer one
   interchangeable synonym group. Provider metadata cannot satisfy a role filter.
10. **Complementary selection:** guidance checks what references actually teach,
    rather than assuming different projects/sources or role names are complementary.
    A lighting reference cannot establish subject recognition. Missing mechanisms
    trigger targeted permitted retrieval only when needed; no reference quota or
    new research requirement. The existing diversity tie-break remains unchanged.
11. **Memory representation:** existing hash-bound observations and
    `role / visible / effect` mechanisms were sufficient; no schema migration,
    new semantic index or model-powered runtime was added. One inspected reference
    was enriched; all other receipts and all image bytes were preserved.
12. **Context:** discovery metadata is unchanged; activated core adds 38 tokens.
    Asset and finish resources add 1,138 and 911 tokens respectively only when read.
13. **Narrow scope:** the entrypoint routes conditionally, and finish explicitly
    sends narrow shadow/control tasks to affected craft. A minor shadow edit does
    not require assets, whole-page finish critique or new reference discovery.
14. **Capability checks:** five asset cases, six finish cases and four scope/tool
    boundaries are recorded in [bounded fixtures](../evals/asset-finish.json).
    These are primary decision walkthroughs, not an automated visual judge or a
    new benchmark runner. Actual pixel inspection was limited as described below.
15. **Exact validation results:** 68 deterministic tests passed, including all 62
    prior tests and six new retrieval/evidence regressions. Official plugin and
    skill validators passed against both repository and installed cache.
    `git diff --check` passed. Installed retrieval, hydration, empty-scope denial
    and static-motion exclusion passed; all 48 installed files matched source.
16. **Preservation:** 264 retained images remain byte-identical: 250 analyzed,
    14 excluded but preserved. All 21 source identities/configuration, authority
    records and four motion bookmarks are unchanged. No broad re-analysis or
    additional approved-source research occurred. No generated replacement asset,
    Figma edit, nested model session, new task or live benchmark was run.
17. **Remaining weakness:** semantic and finish judgment still depends on the
    primary model honestly inspecting pixels and following the guidance. Lexical
    retrieval is not visual understanding, and structured attestations cannot
    prove cognition. No blind independent semantic test, new image-generation/
    alpha-extraction test or live Figma composition test was performed this release.
    The six live design benchmarks remain a separate quality gate; this bounded
    hardening does not establish general design-quality acceptance.

## Retrieval and one targeted enrichment

Identical analyzed-only queries with a matching detail role, against the same corpus:

| Query / role | 0.4.2 candidates | 0.4.3 candidates |
|---|---:|---:|
| shadow | 0 | 5 |
| edge | 0 | 19 |
| transparency | 0 | 4 |
| layering | 0 | 17 |
| masking | 0 | 7 |
| compositing | 0 | 0 |
| texture | 44 | 13 |
| microinteraction | 0 | 0 |

Counts measure retrievability, not relevance or quality. The smaller texture result
set is intentional: unobserved depth/material assumptions no longer count as texture.
An edge-position observation may still match a broad `edge` query. Likewise, a
visible cutout is a candidate for composition research, not proof of extraction
quality or actual alpha. Specific questions and primary inspection remain necessary.
Empty compositing/motion results remain honest gaps, not a reason to fabricate evidence.
Existing permitted discovery still routes tactile-control motion to Design Spells/
60fps, navigation detail to Details.so and scroll interaction to Codrops.

The primary inspected the retained Aather image: its hand-supported candle and
directional cast shadow support a narrow light/contact lesson; its preview does not
certify fine anatomy. The retained AI-generated macro-pad image shows translucent
keys against opaque caps/dark bases, supporting material contrast, not control behavior.
These existing annotations were left unchanged.

The retained [Realistic Button](https://recent.design/i/s6uqxg7-realistic-button-interaction)
was inspected at 970 × 720. A pale rounded upper rim, dark violet lower band and
diffuse shadow are visible. One `surface edge` mechanism was appended to its existing
analysis, plus a limitation about dense-workspace, mobile and accessible-state
suitability. Prior observations and mechanisms were preserved; the inspection
attestation was refreshed to this actual view. Its prior resting-only limitation
remains. No hover/press/timing evidence was invented.

Before this targeted enrichment, `edge highlight` mainly returned page-edge
composition examples. Afterward, the button is first with both terms observed.
Receipt fingerprint comparison found exactly one changed reference. The disposable
SQLite index rebuilt that change without rewriting other receipts. Existing
complementary retrieval produced composition, shadow and transparency candidates
from distinct projects and an explicit missing motion candidate; this is useful
coverage assistance, not automatic proof of visual complementarity.

## Bounded primary walkthroughs

These were reasoning/application checks performed by the same primary session that
implemented the fix. They are not blind or independent model evaluations. Only the
document case included re-viewing the actual rejected generated image; the other
asset defects are supplied scenario evidence, not newly verified pixels.

| Case | Decision under revised guidance |
|---|---|
| Document/research asset | Rejected for the intended evidence role. The actual asset shows stepped, fibrous planes and a colored rule, without passages, annotations, documentary proportions or provenance. Material resemblance cannot establish research meaning. Prefer explicit readable-document cues in native layers, a clearer asset, or omission; no benchmark mutation performed. |
| Human subject | Supplied waxy skin/fused-finger/light defects block acceptance. Repair the actual anatomical and integration cause with identity preserved, or choose another asset. No new human image was generated/tested. |
| Product object | Supplied broken geometry and absent support contradict the resting-object brief; repair construction and contact/light rather than add a generic shadow. A different intentional-suspension brief remains valid. |
| Illustration | Supplied inconsistent shapes/outlines/perspective fail the established brand language. Reject the mismatch; illustration as a medium remains permitted. |
| Abstract asset | With no useful association or composition role, omit it. Intentional atmosphere can justify abstraction when it has a specific job. |
| Elite flat editorial | Preserve flatness. Inspect measure, rag, optical alignment, spacing/rhythm and signature; no mandatory shadow, image or 3D. |
| Layered hero | Load finish; diagnose touching/lifted planes, shared light and occlusion, then compare the specific intervention in context. |
| Tactile control | Load relevant interaction/edge craft only; maintain label/icon/focus clarity. No asset contract or page-level research. |
| High-end branded landing | Preserve useful macro references, identify the unsupported detail mechanism and retrieve only for that gap. Distinct project names are not enough. |
| Dense workspace | Prioritize comparison alignment, muted labels, meaningful border/state hierarchy and density. Do not place ornamental layers over information. |
| Mobile | Reframe an asset if its meaning is cropped away; reduce muddy shadows/texture and verify mobile separately. Desktop acceptance does not transfer automatically. |
| Narrow shadow edit | Inspect current control, adjust bounded shadow relationship, verify affected render. Neither new on-demand resource is required. |
| Incomplete context | Recover section/meaning/placement from existing material; ask only a material unresolved question. Do not invent a subject to satisfy “premium.” |
| Missing tools | State unavailable generation/editing/inspection and use an authorized native/usable fallback. Do not claim masking or acceptance. |
| Revision restrictions | Keep supplied references, approved direction and target. Recheck the revised crop's identifying cues and surrounding composition without widening research. |

## Context measurements

Method: existing development profiler with `tiktoken 0.14.0`, `o200k_base`, identical
scripted route inputs. These are exact counts for that tokenizer, not established
parity with the selected model. Routes are explicit replays, not observed model
activation. Host/tool schemas, live payloads and image tokens are excluded.

| Loaded text | Before | After | Difference |
|---|---:|---:|---:|
| Always-visible discovery metadata | 63 | 63 | 0 |
| Full activated SKILL.md | 638 | 676 | +38 |
| Activated body alone | 573 | 611 | +38 |
| Minimal shadow route | 1,191 | 1,229 | +38 |
| Button + affected interaction craft | 1,722 | 1,760 | +38 |
| Form route | 2,299 | 2,337 | +38 |
| Table route | 3,593 | 3,631 | +38 |
| Substantial operations route | 8,872 | 9,081 | +209 |
| Landing route | 8,109 | 8,318 | +209 |

The full activated skill grows by 166 characters to 3,506. The 38-token routing
increase is about 6% of that small core; narrow route totals grow about 1–3%.
The two substantial routes also read revised process/quality/reference guidance.
They do not automatically open the new asset or finish files.

Conditional payloads: **finish 911 tokens**, **assets 1,138 tokens**, **both 2,049**.
For the measured landing path, deliberately adding finish yields 9,229 tokens;
adding custom-asset guidance too yields 10,367. This cost buys the new capability
only when relevant. No new runtime dependency, prompt-wide examples, mandatory
contract file or extra helper call was added. The existing narrow interaction guide
remains 531 tokens and unchanged by this release.

## Verification details and failures corrected

- New deterministic regressions cover broad-label detail retrieval, provider-only
  claims, texture/depth separation, compact detail prioritization with full hydration,
  static motion attestation/query exclusion, and targeted enrichment cache refresh.
  Synthetic fixture pixels test storage/ranking boundaries, not visual quality.
- Initial profiler run could not reach the tokenizer download endpoint in the
  restricted shell. Reused the already cached tokenizer file; no network workaround
  or runtime dependency was introduced. Classification: EXTERNAL/tool setup.
- The initial enrichment regression expected no `edge highlight` result, but its
  pre-existing fixture already described edge anchors and search intentionally uses
  OR terms. The probe now asks for the absent `highlight` before enrichment and both
  terms afterward. Ranking semantics and acceptance were not weakened.
  Classification: VERIFIER fixture mismatch. Final suite: **68/68 passed**.
- Official installed validator paths: `plugin-creator/scripts/validate_plugin.py`
  and `skill-creator/scripts/quick_validate.py` under the installed system skills.
  Both passed on source and installed cache; temporary PyYAML supplies the validator
  dependency, with neither validator modified.
- Installed smoke checks used the installed helper: the enriched edge detail ranked
  first, hydration preserved both mechanisms, empty scope returned no references,
  and static images did not satisfy a microinteraction query.

Current official documentation was opened on 2026-09-05:
[skill authoring](https://developers.openai.com/plugins/build/skills),
[plugin packaging](https://developers.openai.com/plugins/build/plugins), and
[Figma image integration](https://developers.figma.com/docs/plugins/working-with-images/).
Supporting references and explicit load conditions follow official progressive
disclosure guidance. The actual local bridge passed a read-only roundtrip; current
schemas expose execution, screenshots and image fills. The built-in generation/edit
tool is available. No image/Figma write was necessary to verify those tool boundaries.
Official plugin docs include hooks, whereas the bundled validator rejects that
unused field; no hooks were added. Official surface-dependent manual installation
guidance differs from the local helper's CLI flow; actual `codex plugin add --help`
and successful reinstall confirmed the CLI flow here.

Audit evidence is retained outside the package at
`%LOCALAPPDATA%/design-kit/audits/finish-0.4.3-20260905/`: baseline package snapshot,
before/after profiles, retrieval results, original enriched receipt, receipt
fingerprints and test log. Development fixtures/reports are excluded from the
48-file installed package. Existing accumulated repository changes were preserved;
the batch remains below the approximately 50-file push threshold and was not pushed.
Start a new Codex task to pick up the updated installed skill normally.

## Answers to the three central questions

**A. Why is the translucent-research-sheets failure more likely to be rejected?**
The contract now requires recognizable cues and a likely wrong reading before
generation. The primary then judges actual pixels without crediting the prompt's
nouns. Document meaning and section relevance are veto conditions. A second check
after placement catches crops/overlays that destroy otherwise valid meaning. The
explicit fallback is correction, a clearer metaphor or omission, not rationalization.
This raises the likelihood of rejection; it is not a deterministic semantic guarantee.

**B. How does solid differ from exceptionally finished without more effects?**
Correctness and coherence establish a foundation. Finish asks whether the chosen
language is fully expressed through focal emphasis, signature, asset quality and
optical/material/control relationships across the real composition and mobile.
Only a credible, visible improvement justifies another intervention; removing an
asset, weakening a shadow or improving type may be the better move.

**C. Why is this contextual judgment rather than a premium template?**
Neither asset nor finish guidance activates a fixed aesthetic sequence. The brief,
section role, current visual language and observed reference mechanism determine
the intervention. Flatness and density are protected, references are complementary
only by actual evidence, and a fresh in-context comparison decides what stays.
