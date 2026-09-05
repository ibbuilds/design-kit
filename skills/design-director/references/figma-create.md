# Placement for new design work

Apply only to a new artifact/substantial surface whose page/frame/subtree was not
specified. In the clearly active authorized file, create a dedicated page instead of
putting unrelated design into existing pages. An explicit edit, redesign of an existing
frame, named destination or user instruction overrides this default. A current selection
alone is not an instruction to modify it. No authorized file or equally plausible files:
resolve with available context/tools, asking only if ambiguity remains.

Inspect existing page names without loading all page contents. Follow a clear professional
file convention. Otherwise use concise product/project + surface, e.g. `Atlas · Workspace`.
With no supplied product name, `Checkout` or `Operations workspace` suffices; do not invent
branding. Avoid placeholder/process names (`New Page`, `Test`, `Output`, `AI Design`).
Disambiguate an existing name with a meaningful qualifier or the file's suffix convention;
never overwrite an existing page based on its name.

Benchmark mode applies when explicitly requested, or strongly evidenced by several
isolated prior runs with a clear comparative convention in the current file. A page
called “Test” alone is insufficient. For a new benchmark run, preserve prior runs and
create a new page unless the user specifies otherwise. Follow the established page
naming convention exactly. Include active model/version/time/run metadata only when
that convention calls for it and the values are actually known; never infer model
identity from old page names. Use a truthful run qualifier if required information is
unavailable. Explicit edits stay in their target even inside a benchmark file.

Keep meaningful iterations from this task on that dedicated page. Preserve useful prior
states with consistent alignment, scale-appropriate separation and predictable reading
order; group related desktop/mobile frames. Follow the file's frame convention, or use
`Desktop · 01`, `Mobile · 01`, then `Desktop · 02` / `Mobile · 02` as real iterations occur.
Name the intended final frames clearly (`Desktop · Final` / `Mobile · Final`); distinct
concepts may use meaningful concept names. One solution needs one frame/group, not invented
iterations. Do not duplicate a frame for every micro-edit or manufacture comparison work.

Prior work is subordinate through canvas organization, never through QA labels inside the
actual design. Substantial net-new work includes a compact, separated working
Foundations / Components area alongside Design on the appropriate task page; reuse
existing file organization and preserve benchmark names. It contains real system
objects and concise specimens, not a giant presentation board, research dump,
process diagram or plugin explanation. User organization/preservation instructions lead.

Use native `figma.createPage()` and `page.name` through the available local bridge schema;
use `await figma.setCurrentPageAsync(page)` for dynamic-page access. Read page identity/names
from `figma.root.children`; do not load every subtree to determine naming conventions.
After a partial failure, inspect whether the task page already exists before retrying.
If the file's plan/page limit prevents creation, preserve existing pages and resolve an
authorized alternative destination; do not silently mix work into another page.
These API capabilities were verified 2026-09-05 in the
[official reference](https://developers.figma.com/docs/plugins/api/figma/).
