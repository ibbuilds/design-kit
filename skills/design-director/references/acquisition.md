# Acquisition and persistent analysis

Read only when acquiring or recording reusable evidence. For retrieval see
[intelligence](intelligence.md).

Commands below use `python -B <skill>/scripts/intelligence.py` for analysis/metadata,
`acquire.py` for acquisition/bookmarks and `reference_policy.py` for source lookup.
Do not load this file for an ordinary search of sufficient retained evidence.

## Persist only observed reusable intelligence

`analyze --path <retained-image> --input <temporary-analysis.json>` accepts:

```json
{
  "inspection": {
    "sha256": "exact retained image hash from retrieval",
    "method": "primary-image-view",
    "evidence": "actual image-view tool result identifier or description",
    "region": "region and readable scale actually inspected",
    "observed_at": "2026-09-05T12:00:00+00:00"
  },
  "observations": ["Visible composition, type or imagery relationship."],
  "mechanisms": [{"role": "composition", "visible": "Specific visible cause.", "effect": "Reasoned transferable benefit."}],
  "families": ["architecture"],
  "surfaces": ["hero"],
  "limitations": ["Static crop; unobserved states and small text remain uncertain."],
  "confidence": "medium"
}
```

These fields require real observations, not the example strings. Date, exact hash,
viewing method and image integrity are checked. The caller attests truthfully to seeing
pixels; software cannot independently prove cognition. Static shots cannot support
motion/hover/scroll claims. `primary-motion-view` needs an actually viewed retained
animated image **and** the sequence receipt below. First-frame-only stays static.
No inferred motion from source tags or a successful file decode.

A mechanism may additionally carry `"evidence": {"strength": "clear", "basis":
"Observed region/scale that supports this relationship."}`. Use `limited` when a crop,
overlay, resolution or missing state prevents reliable transfer of that mechanism.
Judge strength per relationship: macro composition can be clear while subtle edges are
unresolved in the same image. No automatic pixel-size threshold or reference-wide quality
score. Missing evidence assessment remains `unassessed`; old analyses need no migration.
Evidence limitations are disclosed, never indexed as positive contributions. Enrich only
useful records after inspecting their retained pixels; preserve existing observations,
mechanisms and provenance. Keep task adaptation out of reusable memory.

`metadata --path ... --input ...` separately preserves source title, tags, description,
creator, date, project, `typefaces` (list), `medium`, `editorial_context` and
`evidence_url`. Font names/editorial claims are provider facts, never pixel-derived
identification or model observation. Legacy `index` remains unverified metadata.
`exclude --path ... --reason ...` preserves non-design/broken/redundant material while
removing it from normal retrieval. Never delete an old reference to improve statistics.

Optional per-mechanism `scope` lists only observed extents: `full-site`, `page`, `hero`,
`section`, `component`, `detail`, `motion-sequence`, `typography`, `brand`, `mobile`.
For reusable quality assessment, add `quality: {"ambition":"high", "basis":"Observed
reason this mechanism meets the strongest reference standard for this scope."}`.
`ordinary` is useful but not elite. High eligibility requires clear evidence and scope;
missing assessments remain unassessed. Judge each sibling independently. Source tier,
confidence, file size and provider tags cannot supply this judgment. Task-specific
novelty/adaptation stays in the conversation, not in permanent source records.

For an actually inspected animation, `analysis.sequence` (or bookmark `--sequence`
JSON) has this shape; replace every illustrative value with the real observation:

```json
{
  "method": "representative-frames",
  "states": [
    {"position": 0, "visible": "Observed start state."},
    {"position": 0.5, "visible": "Observed transition or progression."},
    {"position": 1, "visible": "Observed end state."}
  ],
  "trigger": "Observed trigger, or unknown from the recording.",
  "continuity": "What stays anchored.",
  "spatial_relationship": "What moves relative to what.",
  "purpose": "What the change communicates.",
  "transferable_mechanism": "The concrete reusable principle.",
  "repetition": "Observed repeat behavior, or unknown.",
  "timing_basis": "Sparse frames; exact timing/easing not established."
}
```

Prefer `method: playback` when actually viewed. Positions are normalized within the
inspected start-to-end sequence, not invented milliseconds. Inspect enough intermediate
states to understand choreography; three points are a validation minimum, not a visual
sufficiency guarantee. A two-frame retained animation permits both states. Use `frames`
to expose GIF/WebP samples; view the output before recording. Video uses source playback
and permitted link-only observations, never a first-frame motion analysis.

Record source-established editorial membership as `source_metadata.curated_subset`
(e.g. `Selected`), with its actual evidence URL. Siteinspire items without Selected
membership evidence cannot enter library design retrieval; root access is not membership.

## Discover according to the source's mode

`reference_policy.py` resolves built-in sources and explicit user preferences. Its
registry includes canonical identity, aliases, conditional editorial role, acquisition
mode, retention policy, discovery mechanisms, verified evidence and limitations.
Fresh installs need no source configuration. Preference overrides retain their existing
replace-pool behavior; old records without acquisition policy default to research with
unverified individual retention, never automatic bulk permission.

Use `gap` output for a bounded, specialty-matched source shortlist when local results
are inadequate. `reference_policy.py --query "font pairing"` exposes the same optional
selection independently; empty user source pools stay empty. No request automatically
queries all 23 sources. Curated subset links retain their editorial distinction.
Check current terms/robots and use the source's visible navigation/search or a verified
source-specific MCP. No guessed endpoints, CDN search, outbound site browsing, sponsor
ingestion, authentication bypass or source expansion. A1 tools remain optional.

`acquire.py discover --page <approved-page> --html <temporary-observed-html>` extracts
candidate images and approved links from supported public HTML. This is mechanical
discovery, not proof of curation or visual analysis. Inspect candidates; an unsupported
page should use ordinary browser/provider research rather than guessed scraping rules.

```sh
python -B <skill>/scripts/acquire.py enqueue --page <approved-page> --html <observed-html> --intent task --need "specific current visual need" --asset <exact-observed-asset> --rights "dated terms/robots evidence and permitted use"
python -B <skill>/scripts/acquire.py run --limit 12
python -B <skill>/scripts/acquire.py bookmark --page <approved-item-page> --title "Source title" --note "Access/retention limitation"
```

- `seed` intent is allowed only for broad/bounded modes. No configured source currently
  has established unrestricted broad-mirroring permission; bounded is not wholesale.
- Targeted/research image acquisition requires explicit observed asset selection and a
  stated need. Per-item retention additionally requires `--retention-permission` with
  actual specific evidence. These arguments record checks; they do not grant rights.
- Link-only retention rejects image enqueue; preserve a bookmark instead. Research
  may still inspect the source's own visual when the actual use is permitted.
- A queue records provenance and completion atomically. Resume skips retained assets;
  `--retry` retries ordinary failures, not access restrictions. HTTP 401/403/429 stop the
  automatic method for the failed resource; rate limiting also pauses same-source
  automated requests. For a 403, try normal browser navigation to the same official
  resource, a canonical/versioned equivalent or legitimately available official API/MCP.
  Use successful legitimate access; report a remaining resource/method gap. Failure
  does not revoke source approval. No account or user-agent
  workaround, and no automatic retry of the failed resource.
- Redirects require explicit review, not silent follow-through. Decoding rejects
  broken/nonimage/tiny previews; exact SHA-256 deduplicates retained bytes. Advisory
  `duplicates` reports perceptual candidates without deleting or merging anything.

After acquisition, open actual images, record reusable observations, then retrieve
again. Only that closes the gap path. Uninspected references remain explicitly marked.
`coverage` reports analysis coverage separately from file count. Index refresh is
transactional and rebuildable; receipts and retained pixels survive upgrades. Keep all
retained data until explicit user cleanup; temporary sheets/downloads are disposable.

Documented A1, 60fps and Details MCPs are optional; none is a mandatory dependency.
Discover actual connected tools before use and respect account/plan permissions.
Provider video availability or a motion breakdown is not inspected motion evidence.
View actual sequences through available tools when motion matters; if unavailable,
report the gap. Do not replace evidence with motion tags or static frames.
For browser-viewed sequences without retention permission, use bookmark `--sequence`
for structured primary observations. Existing dated access notes remain searchable;
`acquire.py links --query` searches both structured sequences and legacy notes;
they remain link-only observations, separate from hash-bound retained-image analyses.
Explicit motion/interaction searches in `intelligence.py` require primary motion
inspection, so a static section “transition” cannot stand in for temporal evidence.
