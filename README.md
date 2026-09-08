# Design Kit

Reusable context for polished frontend design, UI and UX: whole sites and apps,
flows, features, sections or components. OpenDesign with Local Codex generates and
refines the design; your coding agent integrates and verifies it. The kit carries
your quality criteria and reference intent through both stages.

## Use with an existing or new project

Copy this kit's files into one unused `.design-kit/` folder inside your project.
Copy the contents, not the kit's `.git` history. Keep your application's existing
instructions and structure. If that folder already exists, choose another name;
do not overwrite it. A separate shared checkout also works when accessible.

```text
your-project/
  .design-kit/     All kit documents, flat
  ...             Your existing application and agent configuration
```

Continue your coding task in the application and send:

> Read .design-kit/AGENTS.md as supplemental frontend guidance. Use it to [task]
> in [target work area], preserving this project's instructions and existing work.
> Use OpenDesign with Local Codex and our BRIEF.md. Integrate and verify the result.
> Keep shared kit guidance unchanged. Do not publish.

Use the actual kit path if different. Explicit reading avoids relying on nested
instruction discovery. To reuse it in future tasks, add a short frontend-only pointer
to your existing agent instructions; do not replace them with the kit's contract.

**Edit only [BRIEF.md](BRIEF.md) for each project.** It holds scope, project references,
design direction, constraints and execution choice. Link existing specs instead of
duplicating them; the agent can fill supplied facts from chat. All other kit files
stay reusable. No new skill, agent, dependencies or folder layout is required.
Exclude the kit from application build/public output if your tooling would otherwise
include it; keep it accessible to the agent.

Follow the [OpenDesign handoff](OPENDESIGN.md): verify access, commission a focused
preview, refine against the references, integrate into the target, then review there.
For review before integration, reserve that boundary in BRIEF.md. The preview itself
is code; preview acceptance does not establish production readiness. A different
execution path requires an explicit user choice.

## Files and reading cost

| File | Purpose / when to read |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Short entry contract and reading routes |
| [TASTE.md](TASTE.md) | Shared quality criteria |
| [WORKFLOW.md](WORKFLOW.md) | Adaptive design/build checkpoints and learning loop |
| [BRIEF.md](BRIEF.md) | The only project-specific file |
| [QA.md](QA.md) | Review the scoped result |
| [BASELINES.md](BASELINES.md) | Preserve/compare an accepted state |
| [OPENDESIGN.md](OPENDESIGN.md) | Selected runtime and integration handoff only |
| [REFERENCES.md](REFERENCES.md) | User library; search relevant sections on demand |
| [RESEARCH.md](RESEARCH.md) | Evidence, alternatives and limits; reassessment only |

Markdown is plain text with searchable headings and links. Renaming it to `.txt`
does not reduce the content the model reads. Keep guidance concise and load it on
demand; do not inject this entire repo. Selective reading is an instruction, not an
enforced context loader or a measured token-saving guarantee.

## Maintain

Leave BRIEF.md blank in the reusable source; fill it only in project copies.
Preserve shared user taste and references. Keep project evidence outside the kit;
propose small transferable changes through the
[learning loop](WORKFLOW.md#08---learn), replacing redundant rules after approval.
Copies receive updates deliberately, never automatically.

Check local links, reading paths, blank fields and source integrity before committing.
This kit has no executable app tests. Document checks establish consistency;
actual UI/UX quality requires building and reviewing a real interface.

The workflow derives from the user-supplied
**High_End_AI_Software_FINAL_RESULTS_WORKFLOW.pdf** and subsequent approved refinements.
[WORKFLOW.pdf](WORKFLOW.pdf) is optional source provenance, read only for audits;
it is not required at runtime.
[REFERENCES.md](REFERENCES.md) preserves **product-references-elite.md** verbatim.
