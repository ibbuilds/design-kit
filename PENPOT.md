# Penpot design medium

Read only when Penpot is chosen for design or handoff. Design Kit supplies the supervised workflow; Penpot's official MCP supplies canvas tools. They are different responsibilities. Do not import a second full design workflow, numeric self-score or automatic canvas-fix policy merely because another kit includes one.

## Verified documentation, not a verified connection

Reviewed September 29, 2026: [official MCP guide](https://help.penpot.app/mcp/), [server/product page](https://penpot.app/ai/mcp-server), [pricing](https://penpot.app/pricing), [official server source](https://github.com/penpot/penpot/tree/develop/mcp) and [Penpot AI Kit tool reference](https://github.com/penpot/penpot-ai-kit/blob/main/shared/penpot-mcp-tool-reference.md).

Penpot describes its MCP server as free/open, with remote and local options. Its Professional cloud plan is $0 with listed storage/team/history limits; open source does not mean hosting/storage/support are universally unlimited. The connected AI client/model still has its own usage cost or subscription limits. There is no Figma subscription or API-model purchase required by this route. An MCP-compatible host is required; not every agent exposes the same capabilities.

No Penpot connection, runtime or canvas was installed/modified as part of this kit revision. These instructions are not evidence that a particular account, server version or tool call works. Read the live tools and verify access before claiming integration.

## Connect the actual agent to the actual design file

First check for an existing working connection. If none, ask whether the user wants **remote Penpot / existing self-hosted or local setup / continue supplying readable files**. A Penpot URL alone does not establish MCP access. Complete brand/direction work independently of canvas setup when possible; do not silently switch the user's chosen design medium.

The current [official help guide](https://help.penpot.app/mcp/) recommends remote for most users:

1. In Penpot, open **Your account -> Integrations -> MCP Server** and check that the feature is available; enable it.
2. Generate the private MCP key if required and copy the server URL from that account. Its form is `https://<penpot-domain>/mcp/stream?userToken=<private-key>`; use the account-provided URL, not a guessed deployment.
3. Connect the user's actual MCP client through its supported private/user configuration. Do not print the key or credential-bearing URL, store it in `.design/`, commit it or ask the user to paste it in a public artifact. Prefer the host's credential/configuration UI. Configuration is separate from a phase's design write.
4. Open the intended design file and use **File -> MCP Server -> Connect**. Keep the connected tab active while using the bridge. Only one tab owns MCP at a time; focused-page changes can change the operation target.
5. Inspect exposed tools and perform read-only verification. Confirm the actual file/page and selected objects before any mutation.

Local is an alternative when chosen, not the default installation payload: official help uses `npx @penpot/mcp@stable`, a running server/plugin and the plugin manifest at `http://localhost:4400/manifest.json`, with MCP normally at `http://localhost:4401/mcp`. It requires Node and an available local environment. Check the current official instructions/version and existing configuration before starting/installing anything; do not bootstrap Penpot or alter global host settings merely because the kit was invoked. Browsers may restrict local network access; use supported configuration, not blanket disabling of browser security.

Some product/AI-kit pages differ in how they label remote/local setup. Prefer current official help and the live deployment's instructions over copied examples. A disconnected bridge needs setup repair, not repeated large design operations.

## Tools and supervised operations

The reviewed AI Kit documents four core tools: `high_level_overview`, `penpot_api_info`, `execute_code`, `export_shape`; local mode additionally documents `import_image`. This is a discovery hint, not a hardcoded schema for every future version. Inspect the connected tool schemas and current official documentation. Do not invent `get_file`, `get_object_tree` or a design-to-code command that the actual server does not expose.

- Start with the connected server's `high_level_overview` guidance, then a read-only structure probe. The documented example uses `execute_code` with `return penpotUtils.shapeStructure(penpot.currentPage.root, 1);`. Use it only after confirming those live APIs.
- For unfamiliar operations, query `penpot_api_info` with the documented type/member. No guessed method names, signatures or token/variant support. Read-only calls and mutations both can use `execute_code`; the name alone does not make an operation safe or a write authorized.
- Before each meaningful write batch, confirm the current file/page IDs match the accepted target. Work only on the objects in that approved phase/batch. Preserve human edits, originals and approved shared components; use a separate proposal board/duplicate when appropriate and supported.
- Use small reversible operations and return compact IDs/counts/names, not the entire canvas tree. Keep canonical IDs/path mappings in the project's existing checkpoint so the next batch reuses actual objects.
- Bind accepted tokens and real reusable components/instances where the live API supports them. Verify the bindings after writes; identical-looking shapes are not proof of reuse. Report missing API support and ask how to handle it instead of claiming a complete system.
- Inspect the resulting design using `export_shape` when available; remote export can be limited. A supported browser view/capture can supply visual evidence. If no legible visual inspection is possible, show the limitation and request a usable view/capture; never claim visual validation from an object-tree JSON response.
- Present the concrete phase/batch, important states, differences and unresolved gaps. **Wait for the designer's acceptance/corrections before the next dependent write batch.** Do not use an external kit's autofix/default scoring to override Design Kit's supervision.

## System structure and handoff

Use functional names and a readable canvas map: foundations, base components, composites/patterns, pages and proposals can be grouped as needed in the existing file. Do not duplicate the library on every page. Use the designer's accepted type/color/spacing values and semantic roles; document usage. Use supported Flex/Grid or responsive rules instead of treating every board as a fixed screenshot.

Official [design-file guidance](https://help.penpot.app/mcp/design-file-structure-best-practices/) supports semantic tokens, reusable components, meaningful variants and layout constraints. Treat its numeric nesting examples as guidance, not universal requirements. The [token guide](https://help.penpot.app/user-guide/design-tokens/) documents import/export and applicability limits; verify actual token API and binding support in the connected version.

For code, obtain the accepted canvas structure, styles/tokens, component IDs, assets, states and responsive intent; export only needed regions. Map them to the existing frontend's canonical tokens/components and retain a short mapping. Penpot inspection/code examples are inputs to implementation, not a guarantee of faithful production code. Verify the real browser result against the accepted design and user task before presenting it for human review.

Reference discovery remains in [REFERENCE_ROUTER.md](REFERENCE_ROUTER.md). Penpot is a canvas bridge, not permission to search outside the curated catalog or upload third-party/private captures without authorization.
