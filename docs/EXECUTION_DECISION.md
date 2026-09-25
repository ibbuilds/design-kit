# Execution decision — 2026-09-25

## Decision for this kit

Keep Codex as the coding execution engine. Implement the repeatable frontend procedure as a native skill, with the existing reference library and target-owned decisions/assets. Do not build a new personal-agent runtime to address an unmeasured visual-quality problem.

A custom client is not the same as a custom execution engine: Codex SDK can run tasks programmatically; App Server supports clients with authentication, history, approvals, and streamed events. A small client can be evaluated later if a concrete need for budget enforcement, repeatable experiments, or visual annotation is not met by the existing interface. None is installed by this change.

## Video supplied by the user

Source: Ras Mic, video `i26XdSwoZ3g`, published 2026-09-11; the YouTube title surfaced as "I Stopped Using OpenClaw & Hermes. I Built My Own Agent Instead" and transcript mirrors retain "I'm Tired of OpenClaw & Hermes".

Reviewed the accessible timestamped transcript passages via two mirrors and compared the described architecture with the author's repository and Eve's public documentation. Did not inspect every moving frame or independently reproduce his deployment/performance claims. This is not a controlled comparison of coding agents or a first-pass design benchmark.

- Around 02:46–04:33 and 07:48–10:31, the author motivates Eve as a middle ground between a low-level SDK and a highly opinionated personal assistant. The file-based structure is an implementation convenience, not evidence of better design judgment.
- Around 04:33–06:29, a promotional Mobbin segment describes improving onboarding through real UI/UX references. Treat the claimed improvement as the author's demonstration, not a verified saving or proof that a paid MCP is required.
- Around 10:44–15:53, the examples concern personal-assistant interactions, tool use, and alternative deployments. They do not establish a replacement for Codex's coding workflow.
- Around 15:56–20:20, he emphasizes reusable tools and his preference for threads/voice. The transferable choice is to reuse tools and context rather than rebuild them each time the host changes.

The author's eve-agents README describes a hosted personal-assistant application and deployment through the owner's AI Gateway. Do not assume this consumes an existing Codex subscription or reduces inference costs. The official Codex App Server has its own documented managed ChatGPT authentication; a custom client over it remains Codex, with applicable account limits.

## Sources consulted

- Original video: https://www.youtube.com/watch?v=i26XdSwoZ3g
- Timestamped transcript mirror: https://lilys.ai/en/notes/openclaw-20260920/tired-openclaw-hermes
- Second transcript/coverage check: https://moderncreator.app/2026-09-11-ras-mic-i-replaced-openclaw-and-hermes-with-eve
- Author's implementation: https://github.com/michaelshimeles/eve-agents
- Eve: https://eve.dev/
- Native skills and discovery: https://developers.openai.com/codex/skills/
- Codex SDK: https://developers.openai.com/codex/sdk/
- Codex App Server and authentication: https://developers.openai.com/codex/app-server/

## What this revision proves

Unit tests cover the installer and package contract. Repository checks can establish that REFERENCES.md and the existing craft documents have not changed. Neither proves aesthetic quality, model obedience, or token savings. Test the skill in the actual target; distinguish activation, reference access, interpretation, implementation, and verification failures before adding mechanisms.
