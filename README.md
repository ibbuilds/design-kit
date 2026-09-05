# Design Kit

Version 0.6.1. A native, model-agnostic Codex plugin that improves design through
reusable visual context, reference mechanisms, art direction, appropriate assets,
native Figma creation and visual refinement. One primary session owns the work.

## Normal use

Ask for the current design task with `$design-director`, or let the skill activate
for relevant Figma work. Specify the authorized file and any constraints. Narrow edits
stay narrow. For substantial creation, Design Kit retrieves and inspects references,
synthesizes an internal direction, resolves essential assets, materializes a local
design system, then composes and inspects the governing surface from it. The system
and design evolve together; mobile reuses the same foundations and component sources
when in scope. UX Canon and archetypes support real content/usability needs;
they do not prescribe aesthetics.
New substantial designs with no destination use a dedicated professionally named page
in the clearly authorized active file. Explicit edits stay in their specified target;
real iterations remain organized together, without manufactured alternatives.

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

All 23 approved visual sources (8 Tier 1, 13 Tier 2, 2 Tier 3) ship in the source registry
with independent acquisition modes and dated access evidence. A source remains approved when bulk downloading is
restricted: use targeted research, in-source visual inspection or a retained bookmark.
No unapproved gallery, outbound website or sponsor becomes a discovery source.

Storage is outside repositories: Windows `%LOCALAPPDATA%/design-kit/references`;
elsewhere `${XDG_DATA_HOME:-~/.local/share}/design-kit/references`. Original receipts
and images remain authoritative. Separate source metadata and hash-bound visual
analysis feed a rebuildable SQLite FTS index. Search returns four compact candidates;
hydrate selected references for complete observations, with acquisition receipts on demand.
Complementary roles and source-specific gap routes remain available. Actual visual opening
is required before design use; evidence attestations do not prove model cognition.

See [source policy](skills/design-director/references/visual-references.md),
[intelligence and acquisition](skills/design-director/references/intelligence.md), and
[retention and explicit cleanup](skills/design-director/references/session.md).
Only explicit user cleanup deletes references. Upgrades and uninstall never do.

## Experience knowledge

Twelve permanent authorities complement visual intelligence: Apple HIG, Material 3,
Fluent 2, W3C/WAI, NN/g, GOV.UK, USWDS, Baymard, Carbon, SAP/Fiori, Spectrum and
Atlassian. The existing Canon remains the local knowledge library; an optional
read-only helper returns bounded, relevant sections with classified provenance. Discovery
can return metadata only; precise needs/selected IDs read their sections directly. The
42 selectively available sections include bidi, recurrence and editing-history guidance.
No authority is a mandatory consultation or a default aesthetic. Narrow edits need
no new lookup. See [experience knowledge](skills/design-director/references/experience.md).

## Creative capability, without a prescribed aesthetic

One small skill routes only relevant intelligence to the primary model: Experience,
visual references, creative direction, asset direction, and finish/craft. Project truth
and human edits govern their use. Internal Task Design DNA connects observed visual
relationships to a precise thesis and, when useful, one meaningful signature moment.
No planning report, reference quota, evaluator or fixed creative sequence is required.

Reference candidates separate task fit from observed creative contribution and its
evidence strength. Specific visible gaps can drive lateral mechanism retrieval; partial
matches and limited evidence remain unresolved. No role list certifies creative coverage.
Important custom imagery uses visual anchors,
prompt-independent semantic inspection, and a verified master for related variants.
Preparation and placed Figma inspection remain separate checks. High ambition can justify
one specific material investigation before native content closes the direction. Finish
seeks consequential opportunities and checks that selected reference relationships survive
into the artifact; flat, dense and restrained work are valid. Stop when no material defect
or supported high-leverage improvement remains, not merely when geometry is correct.
Narrow edits load neither asset direction nor the substantial creative route by default.

## Design Foundations

Substantial net-new designs include an authored basic palette, perceptual color ramps
and semantic variables, reusable typography styles, rational spacing/layout language
and product-derived components. Components follow semantic reuse, even with one current
instance; primary and responsive screens consume the same system. A compact working
Foundations / Components area makes those definitions inspectable alongside the design.
Existing systems and human edits lead; small button, spacing and shadow edits do not
generate a new system, board or page. Systemization preserves expressive composition.

The optional dependency-free `skills/design-director/scripts/color.py` calculates
OKLCH ramps (20 stops by default, fewer when quantized values become redundant), maps
to sRGB and measures WCAG contrast. The primary model chooses the anchors and roles.
See [Design Foundations](skills/design-director/references/design-foundations.md) for
construction, proportionality and iteration; no new workflow engine or evaluator.

## Install, connect and update

Requires a Codex client supporting native plugins. Python 3.10+ is needed for reference
helpers and development tooling. Pillow is required for image decoding, analysis
validation and inspection sheets; SQLite FTS5 ships with standard Python. A separately configured healthy local Figma bridge is
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
