# Reference library and visual intelligence

Use references when requested or materially useful. No-reference instructions prohibit
acquisition and use, including A1/aggregate research. Research is not a mandatory stage.

## Authority and retrieval order

Current explicit direction wins. Retrieve in this order: current user references →
project/user references → configured preferences → permitted persistent library →
new discovery for genuine coverage gaps. Current source restrictions apply to retained
material too; storage is not permission to reuse against an exclusion.

- User references are primary. If sufficient, do not supplement from lower tiers.
- If materially insufficient, ask once: "I can work only from your references, or
  supplement them with Design Kit's default curated sources. Which do you prefer?"
  Honor that answer throughout the task; while unanswered stay within their material.
- If the user supplied none, use the configured pool automatically when helpful,
  reusing permitted library material first. Do not ask the supplementation question.
- “Only these,” “no external references,” and “no defaults” override fallback paths.
  Do not query unapproved sources through A1 and filter results afterward.

Read `python -B <skill>/scripts/reference_policy.py` when policy matters. Built-in
URLs are in [reference-sources.json](reference-sources.json): Godly, Siteinspire Selected,
Minimal Gallery, Httpster, Site of Sites, A1 Gallery and Refs.Gallery. Rebrand Gallery
is conditional on identity/visual-system needs. No source is immutable aesthetic doctrine.

User preferences: Windows `%LOCALAPPDATA%/design-kit/preferences.json`; elsewhere
`${XDG_CONFIG_HOME:-~/.config}/design-kit/preferences.json`. This is a plugin data
convention, not a Codex configuration key. Edit only when the user requests configuration.
Version 1 accepts `sources` and `specialist_sources` arrays of `{name, url, when?}`.
Present arrays replace that pool; omitted arrays inherit; `[]` disables a pool.
Malformed/unreadable preferences never silently broaden to defaults. Task overrides
and supplementation choices stay in the conversation, not project files.

## Library ingestion is broader than task curation

Approved sources → broad discovery → persist valid references → lightweight index →
reuse across tasks. Keep every newly discovered accessible, valid design capture from
permitted sources unless truly duplicate, broken/inaccessible or non-design content.
Today's relevance is NOT an ingestion filter. A library can grow to hundreds or
thousands over time without a quota, expiry, whole-gallery scrape or vector database.
Search results without obtainable visual material are not acquired visual references.

Use [session.py storage and index](session.md). Preserve existing sessions and A1
captures; no migration or re-download is required. Receipts are the lightweight index.
Search title, tags, reusable visual observations and provenance; open the returned
files. Metadata only retrieves candidates—it never substitutes for visual inspection.
Add compact neutral descriptions after viewing; don't store task briefs or project memory.

Prefer gallery-supplied images/captures. Browser screenshots are a fallback when no
usable capture exists and access permits. Obtain exact asset URLs from observed pages
or authorized provider results. Record page and asset provenance; CDN access authorizes
that asset, not discovery across its host. Respect access restrictions and terms,
recheck redirects, never bypass access controls or silently follow unapproved sites.
[A1](a1.md) is optional acceleration, not source authority or a taste engine.
Use available tools; do not scrape entire galleries.

## Task curation and mechanism extraction

Open actual screenshots/pages/sections at readable resolution in the primary session.
For each task candidate evaluate surface/task similarity, information/content similarity,
interaction/structural relevance, visual-direction fit and exact transferable decisions.
Gallery prestige and broad tags such as minimal/light/showcase are insufficient.
Ask: **What specific problem in this design does this reference help solve?**
Reject weak answers from the active task set, while retaining the library image.

Reason: reference → what exactly works → why → relevant mechanism → original synthesis.
For a selected reference, identify the visible region, mechanism, task benefit,
adaptation, what must not transfer, and unobserved behavior. Useful observations include:

- image mass occupies roughly two-thirds of a hero and leads the eye before copy;
- lower-left display type and secondary right copy counterbalance around a quiet center;
- serif display plus neutral sans creates role contrast without proliferating sizes;
- architecture crops preserve planes, apertures and scale rather than lifestyle mood;
- overview/detail transitions change scale while keeping a stable navigation anchor;
- stable row alignment preserves dense comparison; disclosure isolates secondary detail.

Approximate measurements are observations, not universal rules. A still cannot establish
hover, keyboard behavior, motion or full experience architecture. Inspect actual adjacent
pages/states before making those claims. Cross-domain mechanisms may transfer narrowly;
they do not make a stylistic neighbor a whole-surface benchmark. Never clone identity,
copy or proprietary imagery; reference access does not license production reuse.

## Broad exploration, focused context

Research as many candidates as materially useful, curate a rich relevant task set,
then inspect the subset for the current decision. Substantial work may warrant roughly
20–80+ candidates, 10–25 task references and 3–8 for one decision. These are neither
quotas nor caps; don't supplement sufficient user references to hit counts, and don't
stop at three simply because context is limited. Reuse library coverage before discovery.

Stop at relevance saturation: important decisions have credible visual evidence and
additional candidates mostly repeat useful signal. Repeated poor matches or access
failures are not saturation. When a later gap appears, search specifically for it;
do not restart the research. A rejected task reference stays retained. Revisit decisions
based on it without invalidating unrelated work.

Feed selected mechanisms into the [art-direction lock](process.md). Compare current
Figma regions with relevant reference regions at comparable scale/density during
[refinement](quality.md). Keep reasoning internal unless asked. Only explicit user
cleanup removes library data; completion, approval, session end or uninstall never do.
