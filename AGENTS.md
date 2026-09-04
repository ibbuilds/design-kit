# Developing Design Kit

Build a reusable, project-agnostic Codex plugin whose sole goal is final UI/UX
design quality: authoritative UX knowledge, exceptional visual references,
Figma-native creation, critique, and repeated human feedback. These instructions
govern plugin development; installed workflow guidance belongs in the skills.

## Scope and architecture

- The repository root is the plugin root. Keep `.codex-plugin/plugin.json` and
  primary skill `skills/design-kit/SKILL.md`; manifest paths are relative to the
  plugin root and start with `./`.
- Current milestone: minimum valid scaffold only. Implement workflows and
  integrations when the user requests the next milestone.
- Keep customer, brand, product, and project knowledge out of the reusable
  package. Add no frontend production code or bundled reference images.
- Use `plugin-creator` for packaging and `skill-creator` for skill changes. Keep
  instructions concise; add supporting resources only for a demonstrated need.
- Declare integrations only after verifying their supported configuration and
  actual tools. Never invent capability names, connector IDs, dependencies,
  permissions, or successful Figma actions.

## Research and freshness

- Before changing architecture or tool behavior, open current official Codex
  plugin/skill documentation and relevant official Figma documentation. Verify
  available tools and permissions in the target environment. Memory, old examples,
  and local helper scripts are not proof of current support.
- Record source URLs and verification dates with consequential technical or UX
  guidance. Distinguish research evidence, standards, observations, and aesthetic
  judgment; disclose uncertainty. If verification is unavailable, report the gap
  and defer changes that depend on it.
- Resolve documentation/runtime/validator conflicts explicitly; never silently
  weaken validation or turn an outdated limitation into a permanent rule.

## Quality and verification

- Optimize for usability, accessibility, visual hierarchy, typography, spacing,
  coherent interaction states, and context-appropriate originality. Visual polish
  alone is insufficient; references must inform reasoned choices.
- Future workflows must inspect actual Figma artifacts, critique concrete issues,
  incorporate human feedback, and recheck revisions. Respect the user's stopping
  decision; never claim user acceptance or visual verification without evidence.
- After manifest or skill changes, run the installed `plugin-creator` helper
  `scripts/validate_plugin.py` against the repository root and `skill-creator`
  helper `scripts/quick_validate.py` against each changed skill. Resolve helper
  paths from the installed skills; do not copy validators into this package.
- For implemented workflows, test representative activation, non-activation,
  incomplete inputs, missing tools, and revision behavior. Judge observable
  outputs and design quality, not wording matches. Report checks run, failures,
  and untested behavior; schema validation does not prove installation or quality.

## Architecture baseline

Verified 2026-09-04; recheck before relying on this baseline:

- [Plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [Skill authoring](https://developers.openai.com/plugins/build/skills)
- [AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

At verification, official docs support a `hooks` manifest field while the bundled
plugin validator rejects it. This scaffold omits hooks and needs no integration
configuration. Marketplace registration and installation are separate from the
source scaffold and have not been performed.
