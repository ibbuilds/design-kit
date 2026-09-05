# Artifact adequacy and surface completeness

Use this only when the requested design unit or its necessary connected surfaces
are unclear. It is an internal reasoning layer, not a workflow, deliverables list,
or permission to broaden scope.

Ask: **What complete artifact or connected set of artifacts would adequately
satisfy this exact request?** Resolve five things from the user's words and current
Figma state:

1. **Requested unit:** a region, one screen, a page, a flow, a system view, or an
   experience spanning overview and detail.
2. **User jobs:** what someone must understand, decide, find, create, compare, or
   complete within that unit.
3. **Content and relationships:** the objects, questions, evidence, ordering,
   actions, and transitions needed for those jobs to be credible.
4. **Connected expectations:** only the adjacent view or state without which the
   requested artifact would be misleading or impossible to judge.
5. **Enough:** the observable condition that makes this scope coherent and useful,
   while leaving unrelated product territory alone.

Do not equate visual resolution with adequacy. A polished hero can be adequate for
"design this hero" and structurally shallow for "design a portfolio experience."
A dashboard overview may be adequate when the request is only an overview; a
drill-down is needed when the brief asks people to diagnose and act. A narrow type,
spacing, color, or component edit remains narrow. Preserve the surrounding system.

## Content and IA questions

Use only the questions that change the requested artifact:

- What must be understood first, and what can be progressively disclosed?
- Which content types are peers, and which are evidence, metadata, detail, or action?
- How do people move from overview to selection, detail, comparison, or completion?
- What proof, orientation, next action, feedback, or recovery is inherent in the job?
- Which states materially change meaning: empty, loading, error, permission,
  selection, success, return, or resumption?
- Does realistic content expose a missing level of hierarchy or a false assumption?

Use realistic placeholders when the user asked for a concept and real content is
unavailable. Label invented facts as placeholders; never fabricate requirements,
research, customers, metrics, testimonials, or product behavior. Ask the user only
when a missing answer represents a material product decision that cannot be safely
and reversibly assumed.

## Conditional archetypes

Load at most the archetype matching the current artifact, plus another only when
the requested experience genuinely crosses both:

- [Portfolio / showcase](archetypes/portfolio.md)
- [Marketing / product / persuasion](archetypes/persuasion.md)
- [Application / workspace](archetypes/application.md)
- [Dashboard / data](archetypes/dashboard.md)
- [Editorial / reading](archetypes/editorial.md)
- [Form / service / transaction](archetypes/transaction.md)

These are diagnostic lenses. They do not require sections, screens, artifacts, or
stages. The user's exact request remains the boundary.
