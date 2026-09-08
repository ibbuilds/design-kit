# Workflow evidence and decision

Reviewed 2026-09-07. Read for provenance or a workflow decision, not routine design
prompts. This records research sources, not additions to the user's taste library.

## Decision and confidence

Use the PDF-derived process with Codex and OpenDesign as the current candidate.
OpenDesign offers an existing design workspace, configurable context, live preview
and source access through MCP. That fits the user's requested workflow and avoids
building those facilities ourselves. This is a reasoned fit assessment, **not a
demonstrated quality win** over direct Codex or competing tools.

The skeleton preserves the user's standards, project boundaries and acceptance
criteria. OpenDesign supplies execution facilities; its generated result still
needs inspection and integration. More orchestration can also introduce context
conflicts, latency and integration work. Keep it only if results justify those costs.

## What backs each decision

| Decision | Source and supported conclusion | Limit |
| --- | --- | --- |
| Follow the supplied process | User-supplied `High_End_AI_Software_FINAL_RESULTS_WORKFLOW.pdf` (not bundled), pp. 1–6: short mission, one direction, early render, repair/pivot, self-refinement, earned freeze, mode-specific release and accepted lessons. Implemented in [WORKFLOW.md](WORKFLOW.md) and [QA](QA.md). | The user's specification, not independent evidence that this exact sequence is optimal. The context-only scope moves its illustrative starter, primitives and captures into frontend projects. |
| Reuse durable instructions | [OpenAI: AGENTS.md](https://developers.openai.com/codex/guides/agents-md/) documents instruction discovery and scope. [OpenAI: skills](https://developers.openai.com/codex/skills/) documents progressive disclosure. | Supports the context architecture. Phase-based reading here is an instruction convention, not an enforced loader or measured token saving. |
| Use and customize OpenDesign | [OpenDesign README][od-readme] documents Codex integration, filesystem-based skills/design systems, preview and MCP source access. [Prompt composition][od-prompts] and [instruction inputs][od-inputs] expose design-system, skill, user and project context. | First-party documentation/source establish capabilities, not better outputs. Runtime versions and selected execution paths matter; supplied instructions are not guaranteed compliance. |
| Keep modification possible | [OpenDesign license][od-license] permits modification under Apache-2.0 terms; the README identifies separately licensed bundled material. | Open source does not make model inference, hosted services or every bundled asset free. No runtime fork is required by this kit. |
| Render, inspect, repair and recheck | [NN/g: Iterative User Interface Design](https://www.nngroup.com/articles/iterative-design/) describes testing, local redesign and retesting to expose regressions. | This 1993 research concerns user testing, not AI self-critique. It supports iteration, not our exact pass size, an AI quality score or guaranteed first-pass quality. |
| Evaluate accessibility throughout | [W3C evaluation guidance](https://www.w3.org/WAI/test-evaluate/) requires knowledgeable human evaluation; [WCAG 2.2](https://www.w3.org/TR/WCAG22/) supplies testable accessibility criteria. | Automated checks alone cannot establish accessibility; accessibility conformance alone cannot establish excellent UX or visual craft. |
| Measure experienced performance | [Google: Web Vitals](https://web.dev/articles/vitals) defines loading, responsiveness and stability metrics and distinguishes lab from field measurement. | A lab score is neither field evidence nor a complete experience assessment. |

OpenDesign links above pin source revision
`d82385309f5f76466313b020ed8cd8e53e22938a`; this is the inspected upstream source,
not a claim about the locally installed version. Other web sources can change.

## Practitioner comparison: targeted refinements

The user's September 7 clarification prioritizes minimal, surgical context and
freedom of method while preserving quality. WORKFLOW.md now treats phases as
adaptive checkpoints, permits inexpensive exploration when direction is uncertain,
and checks the critical experience before freezing. These refine the PDF-derived
process; they are not claims of literal PDF equivalence or measured token savings.

- [Linear, August 12](https://designerfund.substack.com/p/ai-design-linear): named
  designers describe problem framing, customer context and selective AI use. Supports
  challenging assumptions; does not establish that AI critique replaces judgment.
- [Sierra, July 20](https://designerfund.substack.com/p/ai-design-sierra) and
  [Shopify, August 24](https://designerfund.substack.com/p/ai-design-shopify): designers
  describe prototypes using real data and existing product code. Supports exposing
  constraints early, not importing their organizational tooling wholesale.
- [Interfere, September 1](https://interfere.com/blog/how-we-built-interferes-new-website):
  the credited authors document visual exploration and implementation tradeoffs.
  Supports exploration before commitment; the article does not establish an AI build.

Dates are publication dates, not verified recording dates. These are qualitative
practitioner accounts, not controlled comparisons or user-approved taste additions.
They justify small process changes, not a ranking of tools or guaranteed outcomes.

## Alternatives remain credible

These are documentation comparisons, not completed trials or an exhaustive ranking.

| Approach | Documented distinction | Implication for this project |
| --- | --- | --- |
| Direct Codex + this kit | Uses the same durable context with fewer execution boundaries; see OpenAI documentation above. | Essential baseline. OpenDesign must demonstrate enough added quality to justify its overhead. |
| [Impeccable](https://github.com/pbakaus/impeccable/blob/main/README.md) | Design guidance, product-context setup, craft/audit commands, live browser iteration and deterministic detectors. | Calling it "just a skill" understates its current scope. A credible lighter alternative; its aesthetic defaults still need checking against user taste. |
| [Superdesign](https://github.com/superdesigndev/superdesign/blob/main/README.md) | Original IDE extension is explicitly no longer maintained; its README points to the current web app and coding-agent skill. | Evaluate the current offering, not old extension demos. No superiority conclusion from the historical repository. |
| [Onlook](https://github.com/onlook-dev/onlook/blob/main/README.md) | Open-source visual editing of Next.js/Tailwind code; the next hosted product is described separately as early access. | Relevant when direct visual manipulation matters. Its editor and stack assumptions differ from this context repo's general frontend scope. |

## What would establish a winner

No comparative output evaluation has been completed for this kit. Vendor demos,
feature counts, self-scores and the user's high-quality reference library cannot
substitute for it. Nor do the cited sources prove code-first always beats Figma.

When a trial is authorized, compare direct Codex + this kit against the same kit
with OpenDesign. Use the same model/settings where supported, brief, references,
assets, target stack and time/correction budget. Record versions and any mismatch.
Repeat across a landing page, a dense workspace and a multi-step interface; retain
first handoffs and final results, including failures.

Review outputs without tool labels where practical. Judge the supplied taste,
real task completion, mobile/states, accessibility and maintainability. Distinguish
expert/agent walkthroughs from representative-user testing. Record corrections,
elapsed time and actual usage where available. Quality comes first; efficiency
breaks ties between results that meet the quality bar. Keep evidence in trial
projects and promote only approved, transferable findings into this kit.

Revisit this decision when repeated results favor another approach, a runtime
change breaks the handoff, or a different product requires a different workflow.

[od-readme]: https://github.com/nexu-io/open-design/blob/d82385309f5f76466313b020ed8cd8e53e22938a/README.md
[od-prompts]: https://github.com/nexu-io/open-design/blob/d82385309f5f76466313b020ed8cd8e53e22938a/apps/daemon/src/prompts/system.ts
[od-inputs]: https://github.com/nexu-io/open-design/blob/d82385309f5f76466313b020ed8cd8e53e22938a/apps/daemon/src/prompts/stable-sections.ts
[od-license]: https://github.com/nexu-io/open-design/blob/d82385309f5f76466313b020ed8cd8e53e22938a/LICENSE
