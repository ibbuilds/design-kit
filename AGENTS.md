# Design Kit repository — maintainer instructions

This repository packages a **visual image-iteration skill**, not an autonomous product builder, code generator, or agent runtime. The canonical procedure is SKILL.md: user-owned foundation -> first section image explorations -> subsequent section images -> whole-page visual decision -> stop. The user, **not Design Kit**, decides whether and how to implement a completed direction.

- Preserve useful Awwwards and One Page Love MCP integrations, the curated REFERENCES.md catalog, HOSTS.md / PROVIDERS.md access guidance, safe installer/manifest behavior and existing user-edited work.
- Keep canonical image workflow instructions consistent across README.md, SKILL.md, IMAGE_WORKFLOW.md, FOUNDATION.md, BRIEF.md, ONBOARDING.md, EXECUTION.md, PROMPT.md and the docs/ entrypoints. WORKFLOW.md is only a compatibility pointer.
- When a product asks for images, do not substitute frontend implementation. When a product asks for code, acknowledge that implementation is outside this skill and requires a separately user-selected task. Preserve historical SOFTWARE.md and QA guidance without routing users to them automatically.
- The user owns the design foundation and visual acceptances. Proposals/agent selections are not human approval; generated static images do not verify functioning responsive UI.
- Make image prompts highly specific. Iterate section by section with meaningful visual changes; reuse the actual selected first-section image as an anchor. Do not impose a fixed two-pass cap. Use existing reference providers for concrete gaps, not as a mandatory waterfall.
- Third-party skills are optional and should be evaluated against image outcomes under matched inputs. No automatic skill installs or unreviewed external instructions.
- Keep authored docs/instructions/code in English. Product facts, actual captures and design decisions belong to target projects; do not put them in this kit.
- Do not change external application code or make paid calls as part of kit maintenance. Preserve concurrent work; no force push/merge by default.
- Run the existing unittest suite after package changes. Passing tests establish structural/package behavior only, not improved design quality.
- Historical research/evaluation files remain archived context and do not override SKILL.md.
