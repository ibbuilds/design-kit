# Penpot design medium

Read only for chosen Penpot design/handoff. Design Kit supplies supervision; the MCP supplies canvas tools. No second workflow, self-score or automatic autofix policy.

## Documentation versus connection

Reviewed September 29, 2026: [official help](https://help.penpot.app/mcp/), [pricing](https://penpot.app/pricing), [AI Kit tools](https://github.com/penpot/penpot-ai-kit/blob/main/shared/penpot-mcp-tool-reference.md), [token-aware prompting](https://help.penpot.app/mcp/prompting-token-aware/) and [file structure](https://help.penpot.app/mcp/design-file-structure-best-practices/).

The MCP is described as free/open, remote or local; Professional cloud is $0 with listed storage/team/history limits. The model/client retains its own usage limits. No Figma subscription/API-model purchase is required by this route. Documentation and published efficiency claims do not prove this account/version works or quantify our savings. The kit installs no connection/runtime.

## Connect only if needed

Reuse a working connection. Otherwise ask for remote, existing self-hosted/local setup, or readable files; a URL alone is not MCP access. Continue independent brand/direction work when possible; never silently change the medium.

Current official help recommends remote for most users:

1. Penpot **Your account -> Integrations -> MCP Server**: verify availability and enable it.
2. Generate the private key if needed; use the account-provided URL (`https://<domain>/mcp/stream?userToken=<private-key>`), never a guessed deployment. Configure through the actual host's supported private settings. No keys/credential URLs in logs, project files, commits or public artifacts.
3. Open the intended file, **File -> MCP Server -> Connect**. Keep the connected tab active; only one owns MCP and a focused-page change can alter the target.
4. Inspect live schemas and verify read-only access to the intended file/page before writes.

Local, only when chosen: official help uses `npx @penpot/mcp@stable`, running server/plugin, manifest `http://localhost:4400/manifest.json`, MCP normally `http://localhost:4401/mcp`. Check current prerequisites/version/config before starting or installing. Kit invocation does not authorize global settings or dependency installation. Use supported browser network settings, not blanket security disabling. A disconnected bridge needs connection repair, not repeated design operations.

## Work locally within the accepted batch

Live schemas govern. Reviewed core tools: `high_level_overview`, `penpot_api_info`, `execute_code`, `export_shape`; local also documents `import_image`. Never invent `get_file`, `get_object_tree` or a design-to-code command.

1. **Orient once.** Read `high_level_overview` guidance; it is not the document tree. Check unfamiliar API types/members with `penpot_api_info`; reuse that verified knowledge for this connection/version. Refresh relevant signatures after a version change or API failure, not before every known call. No guessed token/variant support.
2. **Resolve the target.** Before each meaningful mutation, confirm file/page IDs and the agreed objects from the checkpoint. Accepted target IDs win over incidental selection. If no explicit target exists, inspect selection and clarify scope. A shallow page probe can locate objects when necessary: documented example `return penpotUtils.shapeStructure(penpot.currentPage.root, 1);`, only after confirming live APIs.
3. **Read enough, not everything.** For a local edit, inspect its subtree, relevant parent/layout, used tokens/components and affected shared consumers. Reuse known IDs; expand inspection only to answer an actual dependency question. Whole-page/system changes justify broader reads; neither full-tree dumps nor a blind selection-only policy is the default.
4. **One logical operation per call.** Batch related edits to an agreed region/component when supported and reversible. Return compact IDs/names/counts and important exceptions, not the canvas tree or redundant prose. Never batch an entire screen/library into a giant call or impose an arbitrary operation count. Preserve human edits and accepted shared objects; use a proposal board/duplicate when appropriate. Track only canonical IDs and meaningful changes in the existing checkpoint.
5. **Recover from actual state.** A failed/timed-out mutation may have partially applied. Reread the affected objects/bindings before retrying; reuse valid work, correct the cause, avoid duplicates. Repeated failures need a changed hypothesis or blocker. No delete-and-rebuild of accepted libraries to hide API failures.
6. **Verify structure and appearance separately.** Check actual token bindings, component instances, required variants and layout behavior after writes. Then inspect the affected region/states through `export_shape` or a supported browser/capture, and related in-context composition. Remote exports may be limited. JSON success does not prove appearance; a pretty image does not prove reuse. If either check is unavailable, report exactly what remains unverified and obtain usable access/evidence before claiming it complete.
7. **Show and wait.** Present the actual phase/batch, relevant states, material differences and gaps. Wait for human acceptance/corrections before dependent writes; local routine fixes inside that batch need no per-call approval. Record the reviewed revision/capture with IDs so a mutable canvas is not mistaken for the accepted version.

## Reuse and code handoff

Keep a readable map of foundations, base components, patterns, pages/proposals within the existing file; no duplicated library per page. Use accepted semantic tokens, functional naming, meaningful variants and supported Flex/Grid/responsive constraints. Numeric nesting examples are guidance, not universal rules. Check the live [token API/applicability](https://help.penpot.app/user-guide/design-tokens/) instead of claiming unsupported bindings.

For requested code, retrieve only needed accepted structure/styles/tokens, component IDs, assets, states and responsive intent. Map them to target canonical tokens/components and reuse accepted prototype code. Verify the actual browser against the reviewed design and task; export/code snippets alone do not establish fidelity or production readiness. Reference discovery stays in [REFERENCE_ROUTER.md](REFERENCE_ROUTER.md); canvas access authorizes neither extra inspiration sources nor private uploads.
