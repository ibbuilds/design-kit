# Design Kit

Version 0.3.4. A native, model-agnostic Codex plugin that improves design through
reusable visual context, reference mechanisms, art direction, appropriate assets,
native Figma creation and visual refinement. One primary session owns the work.

## Normal use

Ask for the current design task with `$design-director`, or let the skill activate
for relevant Figma work. Specify the authorized file and any constraints. Narrow edits
stay narrow. For substantial creation, Design Kit retrieves and inspects references,
synthesizes an internal direction, resolves essential assets, builds and inspects the
primary surface, then expands and recomposes mobile when in scope. UX Canon and
archetypes support real content/usability needs; they do not prescribe aesthetics.

The normal deliverable is editable Figma. No frontend code, project memory, automatic
draft, QA board or workflow document. Verification renders are transient internal
evidence; user-requested exports are retained. The user's current model/reasoning
configuration performs all substantive work, including Figma and critique, without
nested sessions or model substitution.

## Reference library

Reuse current user references first, then project/user material, configured preferences,
and the permitted persistent library. Discover only genuine coverage gaps. User
exclusivity always wins; insufficient supplied references get one supplementation
question. No reference images ship with the plugin.

Valid discovered captures from approved sources are retained even if not selected for
today's task. Only duplicates, broken/inaccessible or invalid/non-design material are
excluded from ingestion. Task selection is stricter: actual images must reveal useful
mechanisms for the current brief. Library size can grow; visual context stays focused.

Storage is outside repositories: Windows `%LOCALAPPDATA%/design-kit/references`;
elsewhere `${XDG_DATA_HOME:-~/.local/share}/design-kit/references`. Existing receipts
are a lightweight searchable index, with optional titles, tags and visual descriptions.
No vector database or background service. See
[reference policy](skills/design-director/references/visual-references.md) and
[search, import and explicit cleanup](skills/design-director/references/session.md).
Only explicit user cleanup deletes references. Completion and uninstall never do.

## Install, connect and update

Requires a Codex client supporting native plugins. Python 3.10+ is needed for reference
helpers and development tooling. A separately configured healthy local Figma bridge is
the primary transport; official Figma MCP is optional fallback. Design Kit neither
bundles nor silently installs/changes the bridge. Use the bridge's documented setup,
confirm current tools, and authorize the target file. No transport source or credentials
are included. See [Figma guidance](skills/design-director/references/figma.md).
[A1](skills/design-director/references/a1.md) is optional discovery acceleration.

A personal marketplace at `~/.agents/plugins/marketplace.json` can point to
`./plugins/design-kit` relative to the user's home. Use the installed plugin-creator
helpers to create/manage the catalogue. For an existing local source, validate its
marketplace name, update its cachebuster and reinstall:

```sh
python -B <plugin-creator>/scripts/read_marketplace_name.py
python -B <plugin-creator>/scripts/update_plugin_cachebuster.py <actual-marketplace-source>
codex plugin add design-kit@<validated-marketplace-name>
```

Start a new Codex task to load the refreshed cached skill. Editing a source directory
does not reload an already-running task. Follow the installed client/creator when
commands differ; do not hand-edit catalogue or account configuration.

A non-default marketplace root must first be registered with
`codex plugin marketplace add <root>`. Remove with
`codex plugin remove design-kit@<name>`; leave shared catalogues and retained data intact.

## Development and distribution

The source repository is the plugin root. Run the installed creator's
`scripts/validate_plugin.py` against it and the skill creator's
`scripts/quick_validate.py` against `skills/design-director`, plus
`python -B -m unittest discover -s tests -v` for package/lifecycle integrity.
These checks establish structure and deterministic behavior, not visual quality.

`scripts/package.py --output <new-path> --creator-skill <installed-plugin-creator>`
builds a local marketplace and zip using official helpers. It ships only the manifest,
skills and this README. Development instructions, tests, historical docs and benchmark
machinery remain in the source repository; they do not enter the installed runtime.
The exporter does not overwrite, install, publish or push automatically.

Historical evidence and source comparisons remain under `docs/`; explicit development
evaluations remain under `evals/`. They are not normal design workflows.
No open-source license has been selected for this private plugin. Referenced third-party
material retains its own rights. Publishing and Git pushes follow the user's authority.
