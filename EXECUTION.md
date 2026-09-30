# Quality and efficient execution

Read when selecting effort, managing a long task, or handling a budget. This is a working recommendation for design and programming, not a benchmark or runtime configuration. The user's current model, effort, speed and explicit choices win.

Keep the task contract small: outcome, relevant evidence, closed decisions, success criteria and actual side-effect boundaries. Remove repeated instructions and unnecessary tool/process scaffolding before adding more reasoning. Preserve the user's authorization across turns; a requested build/fix continues through implementation, checks and the requested delivery destination. Do not substitute a plan, sample or PR for a requested complete result or direct branch/main update.

## Spend effort on decisions that affect the result

Optimize total consumption to reach the requested quality, including failed attempts, review and rework. Use GPT-6.1 Sol as the normal model when available. **Medium + Standard** is a practical starting proposal for bounded work with clear criteria; Low fits simple, easily checked edits. Use High for consequential ambiguity, coupled architecture or difficult diagnosis where deeper reasoning can resolve a named problem. Substantial scope alone does not require High for every action. These are working proposals, not measured Sol optima; the user's explicit choices win. Do not lower effort halfway through a hard task just to shorten a response.

High is not mandatory for all frontend work. OpenAI's GPT-5.4 frontend article recommends Low/Medium for simpler websites; it is useful counterevidence to “more reasoning always looks better,” not a measured Sol recommendation. For a straightforward visual task, start at the user's selected effort or Medium and inspect the result before paying for escalation. Preserve any explicit user choice. See [workflow research](docs/WORKFLOW_RESEARCH.md) for alternatives and model-specific limits.

Raise effort to Xhigh/Max for a named unresolved problem when better reasoning could change the answer. Reserve Astra for a problem Sol cannot resolve reliably or an explicit user choice. Do not automatically switch models, escalate every action, or assume maximum effort guarantees better visual judgment. A failed render needs inspection or code repair, not necessarily a stronger model.

Standard is the default recommendation for quota efficiency. Fast trades more consumption for speed where supported. Brief visible output does not bound hidden reasoning. API prices cannot be converted directly into hours or a subscription percentage. When usage is observable, compare representative completed tasks with equivalent input and quality requirements; record actual consumption, rework and limitations. Otherwise leave cost unknown.

Official references: [GPT-6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [reasoning effort](https://developers.openai.com/api/docs/guides/reasoning), [Codex usage](https://developers.openai.com/codex/pricing). Availability and rates can change.

When building an API harness, use Responses for Sol tool calling, preserve compatible response/reasoning state and stable prompt prefixes, and evaluate cache/compaction behavior on that runtime. The desktop client manages those mechanisms; an instruction file does not activate explicit caching, async tools, pro reasoning mode or a larger subscription allowance. Subscription Pro and API pro reasoning mode are different concepts. See the [evidence record](docs/QUALITY_EVIDENCE.md) for source scope and transferred recommendations.

## Preserve useful context

- Work in the real target with its existing commands and environment. Read the entrypoint and only relevant supporting documents, code and reference regions.
- Keep a coherent task in its current chat while the context remains useful. For an unrelated task or an overloaded session, preserve a compact handoff rather than replaying the whole history.
- Keep logs and broad search results outside active context; surface errors, conclusions and paths for deeper inspection. Retain evidence needed for diagnosis.
- Reuse accepted code, assets and comparisons. A local cache saves retrieval, not necessarily model context; do not re-send every stored image.
- For a recurring problem, retain the verified cause, relevant revision/conditions, source evidence and smallest successful repair in an existing project record. Retrieve that narrow record when useful; treat an old diagnosis as a hypothesis until its conditions still match. Do not accumulate unverified conclusions, secrets, whole logs or each run's narrative in permanent instructions. No automatic memory service or background observer is required.
- Batch related repairs. Repeat tests and reference discovery only when a change, failure or new scope justifies them.

Before another expensive iteration, identify the unmet criterion, the new evidence or changed hypothesis, and the smallest action that can resolve it. Compare concise concepts or the uncertain region before building additional complete variants. Reuse the accepted sample for expansion; do not rebuild the system, generate a suite of project skills or migrate tools without a demonstrated need. Keep required verification even when it adds consumption: preventing a material defect can save more rework than skipping the check.

Do not sacrifice acceptance criteria to a token target. Close on verified scope and concrete quality criteria, not a self-score or a fixed number of rounds. Continue substantive repairs while progress is possible; stop preference churn when there is no defect or supported improvement. A repeated failure calls for a changed hypothesis, missing evidence, or a clear blocker. Explicit user budgets always win; report incomplete work honestly.

## Long work and handoff

Preserve the objective, closed/open decisions, accepted code/token paths, selected evidence, run/check commands, verification results, remaining defects and next action. Distinguish implemented, verified, agent-selected and user-accepted work. Use existing project records; create a new document only when it improves continuity. No mandatory PRD, ceremony, agent team, full-page variant tournament or extra server.

Tools and dependencies enter for a demonstrated need and authorized scope. Do not install the reference catalog, change runtime settings, activate background jobs, or create additional agents by default. Complete the authorized work with the available capabilities; request approval only where the actual action requires it and prior authorization does not cover it.
