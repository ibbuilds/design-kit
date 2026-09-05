# Reference retention and explicit cleanup

References belong to the human's continuing design process. Keep them across
iterations, design approval, task completion and conversation boundaries. Never
infer cleanup consent. Reuse relevant acquired references rather than downloading
them again. Resolve the current source policy before reuse; retained data cannot override new exclusions.

Use `scripts/session.py` relative to this skill with Python 3.10+. It performs no
network requests. Storage uses `%LOCALAPPDATA%/design-kit/references` on Windows and
`${XDG_DATA_HOME:-~/.local/share}/design-kit/references` elsewhere. This is ordinary
user-owned reference data, separate from plugin installation and the host repository.
There is no background process, expiry, automatic pruning or database. Check the
resolved location is outside the working repository; do not use a redirected data
directory inside it. Run the helper sequentially, not with concurrent writers.

## Search the persistent library

Session directories are storage partitions, not task boundaries. Existing schema-1
receipts remain valid; no migration or duplicate index file is required.

```sh
python -B <skill>/scripts/session.py search --query "hospitality horizon" --limit 12
python -B <skill>/scripts/session.py search --scope https://www.a1.gallery --offset 12 --limit 12
```

Search returns exact local image paths and provenance, using title, tags, description
and URLs across all retained sessions. All query terms must match; use a shorter
query or inspect other pages before declaring a coverage gap. Scope is one source
filter, not an authority resolver; apply all current restrictions before viewing.
Open returned images through available image tools. Results are metadata matches,
not proof of visual inspection. Old unannotated captures remain searchable by URL.

After inspecting a capture, enrich its receipt with compact, reusable observations:

```sh
python -B <skill>/scripts/session.py annotate --session <path> --file <asset-name> --title "Project / page" --tag hospitality --tag architecture --description "Wide image mass; display type occupies low-detail sky; compact secondary copy."
```

Use neutral visual vocabulary, not today's brief, an active-set decision or project
memory. The image is unchanged; metadata stays with existing provenance. No database,
daemon, expiry or capacity-based pruning. The library can grow independently of the
small visual subset used for a particular decision.

## Acquire and reuse

1. `python -B <skill>/scripts/session.py list` discovers retained sessions, source
   scopes and exact file receipts. Reuse an appropriate session and inspect the
   relevant images before acquiring more. `init` creates a fresh session only when
   one is needed and returns its path.
2. `approve --session <path> --scope https://approved.example/gallery` records a
   source **already allowed by the resolved reference policy** (explicit direction or
   an applicable configured pool). The command neither obtains consent nor expands policy.
3. `allow-asset --session <path> --page <approved-page> --asset-url <observed-url>
   --permission-checked` records exact provenance after checking access/terms.
   A CDN grant permits that image, not discovery on the CDN or a redirected site.
4. Download through available tools, rechecking redirects. `put --session <path>
   --input <download-path> --page <source-page> --asset-url <exact-url>` copies an
   image into managed storage; the helper itself never adopts or deletes the source. Identical
   image bytes are deduplicated across retained sessions. The returned path may belong
   to an earlier session; reuse it and do not clear that session as task cleanup.
   Inspect the returned image visually. Format sniffing
   excludes HTML/SVG; it is not a malware scanner or full image decoder.
5. Only user-requested notes or technically necessary compact runtime provenance use `put --session <path> --input <utf8-note> --note`. Keep it
   small and credential-free; do not persist briefs, plans or process/status reports. Do not overwrite the ownership receipt. Keep download
   intermediates outside the repository too. Once `put` and visual inspection confirm
   the retained managed copy, delete only a Design Kit-created temporary download as
   ephemeral scratch. Never delete or move a user-supplied original. The managed copy
   remains user-owned reference data and still requires explicit cleanup consent.

## Clean only when requested

When the user explicitly asks to clear Design Kit references, identify the requested
session(s), then run `plan --session <path>`. It lists owned unchanged files, files
that must be preserved, and a digest. Inspect it and run `cleanup --session <path>
--apply <digest> --user-requested`. The flag attests to a real user request; it is
not permission by itself. If the user meant one task, never clear all their sessions.

Cleanup rejects traversal, links/reparse points and hardlinks; preserves changed or
foreign files; never recursively deletes. It cannot delete Figma objects or imported
originals. Report preserved material and its reason without force-removing it.
A changed plan needs fresh inspection. Same-user malicious concurrent filesystem
changes are outside the trust model; do not share a live directory with other writers.

For user-scoped installation, references remain until explicitly cleared. For
repo-scoped installation, cleaning references and removing the plugin are separate
explicit choices. Uninstall must not implicitly delete reference data or any Figma
design. The README documents plugin removal; this helper handles reference cleanup.
