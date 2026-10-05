# Supported platforms and interfaces

The primary experience is **inside the agent interface**: questions, reference previews, system specimen, corrections, implementation and QA. Helper scripts are actions the agent can perform, not a terminal workflow the designer must follow. Support is limited to OpenAI, Anthropic and Google; the same design contract runs through their native adapters.

| Platform | Primary graphical surface | Native skill / project instructions | Additional surface |
| --- | --- | --- | --- |
| OpenAI | Codex desktop app | `.agents/skills/design-kit/SKILL.md`; active `AGENTS.override.md` or `AGENTS.md` | Codex CLI and IDE integration |
| Anthropic | Claude Desktop **Code** tab | `.claude/skills/design-kit/SKILL.md`; `CLAUDE.md` | Claude Code CLI and IDE integration |
| Google | Antigravity app / IDE | `.agents/skills/design-kit/SKILL.md`; `GEMINI.md` | Gemini CLI uses the same skill path/record, with a different MCP adapter |

This is a reusable **skill with supporting resources/scripts**. A plugin is host-specific packaging that can bundle skills and MCP definitions; that packaging alone does not improve design. This checkout and installer deliver the skill, not a marketplace plugin automatically installed in all accounts.

## Activate from the interface

Choose installation scope once: **user** makes the skill available across projects; **project** keeps a team/project-specific copy. User installation stores only the reusable kit; all project facts, references, approvals and generated work remain in the actual target. Do not edit global instruction files to impose design onboarding on unrelated tasks. When the skill applies, retain its workflow across follow-ups using the target checkpoint.

| Adapter | Global user skill directory |
| --- | --- |
| `codex` | `~/.agents/skills/design-kit/` |
| `claude-code` | `~/.claude/skills/design-kit/` |
| `gemini-cli` | `~/.agents/skills/design-kit/` (preferred alias) |
| `antigravity` | `~/.gemini/config/skills/design-kit/` (app/IDE) |

`~` is the selected user's home. OpenAI and Gemini CLI can share one managed global bundle; Antigravity app/IDE uses its own native global location. Antigravity CLI is a different surface and is not this adapter. Avoid duplicate global/project installations unless intentionally maintaining a project override: Codex may list both, whereas other hosts apply their own precedence. Existing unmanaged or customized copies require review rather than overwrite.

Open the actual project in the chosen local graphical surface. Once the skill is installed, explicitly select/invoke Design Kit from that surface's skill picker or ask it to use Design Kit. Codex supports `$design-kit`; Claude Code supports `/design-kit`; Antigravity supports native skill discovery/selection. Confirm it identified the project and current phase rather than assuming invocation proves compliance.

An initial setup request can be given in the interface:

> Install Design Kit from this checkout into the project we are working on, using this interface's adapter. Preserve existing instructions and work. Configure Awwwards and One Page Love if missing, show any concrete conflicts, and verify actual tool access. Then start Design Kit's supervised UI-to-frontend workflow.

For global installation, replace the destination with "globally for my user", and explicitly choose whether MCP configuration should also be global. This does not move project records into the shared skill. If the scope is unresolved, ask one user/project choice before writing; reuse an already explicit choice.

Resolve the checkout/project paths from actual context. The agent can use the installation and MCP helpers under existing authorization. Never install the kit into itself. If the interface cannot access local files or execute setup, state that capability gap and provide its native manual configuration; do not pretend installation succeeded.

Prefer native structured questions with contextual options and free text; use short chat questions when the host/mode lacks that tool. Prefer native previews, browser panels and annotations; otherwise show readable captures or a local artifact the host can open. At human checkpoints, stop dependent work until a response arrives. An asynchronous question submission alone is not an answer.

## Surface boundaries

- Codex app, CLI and IDE share MCP configuration, but project config requires the host's trust rules. Existing global/managed settings may affect the effective connection.
- Claude Code Desktop uses project skills/instructions and `.mcp.json` like its CLI. Account-synced skills and Desktop chat MCP settings can also affect local Code sessions. Inspect effective connections to avoid duplicates or conflicts. Chat/Cowork are distinct surfaces; this installer does not upload an account skill or configure their cloud runtime.
- Antigravity loads workspace skills and has graphical MCP management. Its remote field is `serverUrl`; Gemini CLI uses `httpUrl`. Sharing a skill does not make their MCP config formats identical. Gemini's consumer web chat/Gems are not verified native targets for this local skill-plus-MCP workflow.
- Cloud, SSH or WSL sessions need the kit and provider runtime in that environment. A local file path or stdio executable does not automatically become available remotely.

No host-independent custom question widget, browser bridge or model switch is necessary. Preserve the selected model/settings; capabilities and quality vary even with the same instructions. Report unavailable visual inspection, rendering or native setup honestly and use the scoped fallback.

## Adapter commands for the agent

```sh
python scripts/install.py "<target-project>" --host codex --check
python scripts/install.py "<target-project>" --host codex
```

For global user installation, omit the project argument:

```sh
python scripts/install.py --scope user --host codex --check
python scripts/install.py --scope user --host codex
```

`--user-home "<existing-profile-home>"` selects another explicit home for user scope, including an isolated test profile. Global installation adds no AGENTS.md, CLAUDE.md or GEMINI.md pointer; native discovery and the skill's task description supply activation. Project-only software pointer flags are rejected in user scope, but the skill still covers requested frontend work. Updates/checks use the same scope and host.

Use `claude-code` for Anthropic, `antigravity` for Google's graphical surface, or `gemini-cli` for Google's terminal surface. Installation copies the same resources and preserves project instructions. In project scope, shared `.agents/skills` paths allow OpenAI/Google to reuse one managed bundle; installing another adapter adds its instruction pointer without duplicating the skill. Setup performs no network requests or model calls. See [PROVIDERS.md](PROVIDERS.md) for separate project/user MCP configuration, dependency notices and verification.

Platform documentation checked October 5, 2026: [Codex skills](https://developers.openai.com/codex/skills), [Codex MCP](https://developers.openai.com/codex/mcp), [Claude Code Desktop](https://code.claude.com/docs/en/desktop), [Claude Code skills](https://code.claude.com/docs/en/skills), [Antigravity skills](https://www.antigravity.google/docs/skills), [Antigravity MCP](https://www.antigravity.google/docs/mcp), [Antigravity rules](https://www.antigravity.google/docs/rules), [Gemini CLI skills](https://geminicli.com/docs/cli/skills/), [Gemini CLI MCP](https://geminicli.com/docs/tools/mcp-server/). These support paths/contracts; offline package tests do not prove activation or identical behavior in those applications.
