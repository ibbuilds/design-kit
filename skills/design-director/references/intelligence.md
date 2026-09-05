# Retrieve visual memory

Optional Python 3.10+ helpers, relative to this skill; SQLite FTS5 is built in.
Only image operations require Pillow. Writers are sequential; retained data lives
outside repositories as described in [session](session.md).

```sh
python -B <skill>/scripts/intelligence.py search --query "asymmetric photography" --analyzed-only
python -B <skill>/scripts/intelligence.py search --query "comparison density" --surface table
python -B <skill>/scripts/intelligence.py search --query software --role layering --analyzed-only
python -B <skill>/scripts/intelligence.py complementary --query software --role "surface edge" --role framing
python -B <skill>/scripts/intelligence.py hydrate --path <selected-path> --sha256 <selected-hash>
python -B <skill>/scripts/intelligence.py search --query "spatial storytelling" --ambition high --evidence-scope page
```

Search defaults to four candidates, maximum 24 per page (`--limit`, `--offset`).
For consequential high-ambition direction, `--ambition high` selects only mechanisms
with primary-assessed high quality, clear evidence and explicit scope. Add
`--evidence-scope` for the decision's extent; section evidence never implies page/full-site.
These filters also work on `gap` and `complementary`. Legacy observations stay useful
and retrievable with ordinary search, but do not silently become elite evidence.
If assessment is missing, inspect only promising ordinary candidates and judge them
for this task; no corpus-wide regrading or mandatory persistence. A recorded pass is
still a role-specific observation, not automatic acceptance for a new task.
Each separates `task_match` (observed terms vs provider-only labels) from two concrete
cause/effect `mechanisms`. Per-mechanism evidence is `clear`, `limited`, or `unassessed`,
with a primary-observed basis when recorded; image size, viewing method and limitations
expose what the retained visual can support. These are attestations, not quality scores.
Hydrate only selected references for complete observations, mechanisms,
provider metadata and hash-bound inspection. Add `--receipt` only for complete acquisition
or legacy provenance. `--full` retains the richer legacy
search output when all candidates' details are useful. No information is deleted.
Batch up to six selections in one hydration call by repeating `--path` and matching
`--sha256` arguments in the same order.

Use `--query` for task context and `--role` for an unresolved visible relationship.
Role retrieval ranks support within one mechanism and its assessed strength before task
similarity; a cross-domain example can lead. `--surface`/`--family` deliberately restrict
scope, so omit them for lateral transfer. Matching uses roles/causes/effects, never provider
tags or evidence limitations. “Product” does not imply commerce. Specify the relationship
behind ambiguous “product presentation”: UI framing, physical imagery or storytelling.
Partial matches remain candidates with unmatched terms; they leave `gap: true` in
complementary retrieval, as does limited evidence. `gap: false` only means a candidate exists.
No combined relevance score, label set or lexical match certifies creative coverage.

Complementary retrieval is optional for actual decision gaps, not a reference-role checklist.
It returns one mechanism per requested relationship, reference reuse and exact cause/effect
repeats; paraphrased repetition still needs judgment. One image may support several decisions.
After inspecting a governing render, turn a consequential visible gap into a mechanism query
(e.g. under-integrated product frame → framing/layering), inspect the useful detail, then apply
or reject it. Keep task research and resolved decisions; no need to restart domain discovery.

Current source restrictions apply on search AND hydration. `--scope` restricts allowed
paths; `--specialist` enables conditional identity sources when relevant. An empty
scope set means no references. Reuse stable selections; recheck changed restrictions.
Never browse merely because query terms remain unmatched when evidence is sufficient.

Open the selected actual `path` with the image-view tool. For multiple images,
`view --path <image> --output <temporary-sheet.png>` makes a sheet, but **open the
returned sheet** before claiming inspection. Use originals/crops when details are small.
Static evidence cannot establish motion, hidden interaction or responsive states.
`view` labels animated images **first-frame-only**. Prefer source playback; for a
retained GIF/animated WebP use `frames --path <image> --output <temporary-sequence.png>`
and actually open the sequence sheet. Inspect additional frames when sampling misses
the mechanism. Neither generating a sheet nor an animated flag proves observation.

For motion or source-context material, `acquire.py links --query "motion"` searches
retained link-only notes, including dated primary sequence observations. Open the
source to inspect the relevant sequence; pass the same `--scope` restrictions to links.
Distinguish ordered observed states from
provider claims. `intelligence.py` motion queries require actual motion inspection,
not a static section described as a transition. A sequence receipt is required, including
ordered states, trigger, continuity, relative movement, purpose and transferable mechanism.
Retained video decoding is not implemented; inspect source playback and save permitted
link-only observations through `acquire.py bookmark --sequence <observations.json>`.
Legacy motion notes remain preserved but are not structured sequence attestations.

If local evidence is insufficient, `intelligence.py gap --query "specific need"`
returns a bounded approved source shortlist with access modes. Read
[acquisition](acquisition.md) only for discovery, retention or new analysis, and
[A1](a1.md) only for its optional integration. No automatic browsing or source expansion.
