# Developing Design Kit

Build a reusable, project-agnostic Codex plugin whose sole goal is final UI/UX
design quality: authoritative UX knowledge, exceptional visual references,
Figma-native creation, critique, and repeated human feedback. These instructions
govern plugin development; installed workflow guidance belongs in the skills.

## Scope and architecture

- The repository root is the plugin root. Keep `.codex-plugin/plugin.json` and
  primary skill `skills/design-director/SKILL.md`; manifest paths are relative to the
  plugin root and start with `./`.
- Current milestone: complete request-driven design intelligence with demonstrated acceptance.
- Design Kit influences execution; it never owns the user's process. Keep methods
  conditional, preserve current Figma edits, and create no unrequested process artifacts.
  The named test draft below is development-only authorization, never a runtime default.
- Design Kit is single-agent by default. The active primary Codex session and its
  selected model/reasoning configuration own every substantive design decision and
  Figma action end to end. Never hand reference interpretation, IA, art direction,
  composition, Figma construction, visual critique, responsive work or final verification
  to a subagent, separate Codex task or nested CLI session. Use a subagent only for
  explicitly useful peripheral mechanics that cannot influence design decisions.
- Preserve existing Figma projects/drafts. Live development tests may write only
  to the newly created `Test Plugin` draft; never delete it. Keep test file keys
  outside the reusable package.
- Keep completed-work commits local while fewer than 50 are ahead of the upstream
  branch. At 50 or more, push the pending commits together in one normal batch after
  refreshing upstream state. Never push each commit individually or manufacture
  commits to reach the threshold. Uncommitted files do not count as pending commits.
- Keep customer, brand, product, and project knowledge out of the reusable
  package. Add no frontend production code or bundled reference images.
- Retain acquired references outside repositories until an explicit user cleanup
  request. Never infer cleanup consent from completion, approval or session end.
- Classify generated material as source, persistent dependency, user-owned retained
  reference, explicit benchmark evidence or ephemeral scratch. Keep ordinary renders
  and download intermediates in managed temporary storage only as long as needed;
  never delete user-supplied originals or retained reference copies implicitly.
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
- Verify affected Figma artifacts; use critique only when it serves the current
  request. Incorporate human feedback and recheck authorized revisions. Respect the user's stopping
  decision; never claim user acceptance or visual verification without evidence.
- After manifest or skill changes, run the installed `plugin-creator` helper
  `scripts/validate_plugin.py` against the repository root and `skill-creator`
  helper `scripts/quick_validate.py` against each changed skill. Resolve helper
  paths from the installed skills; do not copy validators into this package.
- For implemented workflows, test representative activation, non-activation,
  incomplete inputs, missing tools, and revision behavior. Judge observable
  outputs and design quality, not wording matches. Report checks run, failures,
  and untested behavior; schema validation does not prove installation or quality.
- Treat the six representative live Figma benchmarks as the primary quality gate.
  Cheap policy probes cover only activation and obvious safety/routing boundaries.
  A meaningful write invalidates earlier renders for verification of that target.
- Judge editable construction as well as pixels. For substantial work, inspect whether
  content-driven regions use appropriate Auto Layout, repeated/stateful UI uses
  components when warranted, and long content or resizing exposes collisions.
- Classify failures as SPEC, CONTEXT, TOOL, VERIFIER, ARCH, EXTERNAL or MODEL.
  Correct one concrete cause, verify, and keep or revise the smallest useful fix.
  Never weaken acceptance, drop failing cases, or add infrastructure to hide a gap.
- Promote permanent guidance only for general, important or recurring problems,
  after checking overlap and regressions. Preserve working behavior; no taste rewrites.

## Architecture baseline

Verified 2026-09-04; recheck before relying on this baseline:

- [Plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [Skill authoring](https://developers.openai.com/plugins/build/skills)
- [AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

At verification, official docs support a `hooks` manifest field while the bundled
plugin validator rejects it. Omit unused hooks; resolve conflicts explicitly.
Installation, workflow evidence and limitations belong in `docs/validation.md`.
