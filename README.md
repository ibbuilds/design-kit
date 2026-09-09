# Design Kit

Reusable AI guidance for high-quality frontend design and engineering, from components to complete apps.

## Use

1. Copy the files into an unused `.design-kit/` folder in your project, without this repo's `.git`. An accessible external checkout also works.
2. Append the pointer below to the target's root `AGENTS.md`. Preserve existing instructions; create the file only if absent. For another agent, use its recognized project-instruction file.
3. Fill relevant fields in [BRIEF.md](BRIEF.md) in the project copy, or ask the agent to fill them from your chat/specs. This is the only project-specific kit file.
4. Work from the target project and request the site, feature, section, component or review you need.

```md
For frontend design, implementation or review, read `.design-kit/AGENTS.md`
as supplemental guidance and follow its selective reading routes.
Preserve this project's instructions, stack and conventions.
```

- The folder alone does not activate the kit: nested instructions do not automatically guide sibling application files. Use the root pointer, or explicitly request reading `.design-kit/AGENTS.md` in the task.
- If the kit is external or named `design-kit/`, adjust the pointer to its actual path. Use a project copy when recording a brief; keep the reusable source blank.
- Check first use by asking the agent to identify the kit/target roots and guidance applied. Reading guidance supports consistency; it does not guarantee compliance or output quality.
- Keep the kit out of application build/public output.
- Use the current agent. No external design runtime or new dependencies required.
- Project references define direction. General references provide knowledge and examples when needed.

## Files

| File | Read for |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Entry instructions and reading routes |
| [BRIEF.md](BRIEF.md) | Project-specific facts and direction |
| [TASTE.md](TASTE.md) | Shared quality standards |
| [WORKFLOW.md](WORKFLOW.md) | Design/build steps, reference lookup and learning |
| [GUIDELINES.md](GUIDELINES.md) | Relevant work-type priorities |
| [QA.md](QA.md) | Verification and accepted-baseline comparison |
| [REFERENCES.md](REFERENCES.md) | Free design, UX and implementation references |
| [RESEARCH.md](RESEARCH.md) | Historical evidence; audits only |

## Maintain

- Leave BRIEF.md blank upstream. Keep implementation and evidence in target projects.
- Propose transferable improvements through [the learning loop](WORKFLOW.md#learn).
- Apply approved updates deliberately to project copies.
- Check links, reading paths, blank fields and source integrity before committing.
- Keep the flat layout. Read only relevant sections; Markdown supports headings and links without a separate format or loader.
- Document checks verify consistency. Real output quality requires building and reviewing interfaces.
- REFERENCES.md combines user-supplied and researched free resources for frontend craft, UX and implementation.
