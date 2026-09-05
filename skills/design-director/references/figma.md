# Figma execution

Keep the existing healthy local Desktop Plugin API bridge as primary transport.
Official Figma MCP is optional fallback. Design Kit supplies intelligence; the bridge
supplies transport. Discover actual available tools/schemas, never invent capabilities,
hard-code hosted quotas, silently install/change connections or substitute a model.
If tools are missing, restore/explain access in the primary session.

## Target and bounded writes

Confirm the authorized file, page and target subtree before writes; pin the file when
the available bridge supports it. Inspect relevant current pixels, structure, variables
and components. Preserve human edits and unrelated nodes. A new file requires explicit
authorization; never delete files. Reuse known unchanged context and inspect changed
regions before continuing.

Create native editable Figma content. Load fonts before text mutation; append children
before assigning dependent layout sizing. Use Auto Layout inside content-driven regions,
repeated rows, controls and navigation; root-only stacking is not a substitute for
responsive internals. Use components where repetition/states justify them, not a
mandatory library. Absolute positioning is appropriate for intentional spatial
composition, imagery and data marks. Name meaningful layers.

Group related changes into bounded writes; resolve the primary surface before broad
expansion as described in [creative runtime](process.md). An execution error may follow
partial mutations: inspect live state before retrying, avoid duplicate artifacts and
repair only known in-scope changes. Respect dynamic-page API requirements when exposed;
use current schemas and official skill prerequisites for the chosen integration.

## Fresh visual evidence

A meaningful write invalidates earlier renders for the changed target. Obtain a fresh
current-runtime render of the same file/node/state and inspect it before claiming the
change worked. Current node data alone cannot certify pixels. Use region-level images
at readable scale: a downscaled full-page export cannot prove small text or mobile fixes.

Inspect → diagnose → bounded write → fresh render → compare. Check material defects,
nearby regressions, relevant states and construction. For substantial content-driven
work, verify a representative long-content or resize condition within authorized nodes;
do not alter unrelated human artifacts as a test. Keep/revert changes from evidence,
not from successful tool responses.

If no available transport can write or render, do useful scoped reasoning and report
the exact limitation. Do not claim visual verification or switch to frontend delivery.
Reuse a healthy bridge process; don't launch duplicate listeners. Close only processes
started solely for a bounded task, never a shared healthy transport. No process manager.

## Output

The editable Figma page/frame is the deliverable. Keep ordinary renders in tool memory
when possible; if a file is necessary, use managed temporary storage outside the repo
and remove only Design Kit-created transient copies when no longer needed. User exports,
explicit retained benchmark evidence and reference-library assets have different
lifecycles; never treat them as temporary screenshots. No QA boards or PNG finals by default.

Transport baseline verified 2026-09-04; official Plugin API documentation rechecked
2026-09-05: https://developers.figma.com/docs/plugins/api/figma/.
Source records: `figma-console-local`, `figma-remote`, `figma-tools`, `figma-write`
and `codex-mcp` in [sources.json](sources.json). These are provenance, not a guarantee
that a tool is present in the current session.
