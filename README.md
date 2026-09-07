# Design Kit

A reusable **context repository** for an AI agent designing and building high-end
frontends in a separate project. This repo holds the workflow, a place for your
taste pack, and review criteria. There is nothing to install, run or deploy.

Source: **High_End_AI_Software_FINAL_RESULTS_WORKFLOW.pdf**, preserved unchanged
as [WORKFLOW.pdf](WORKFLOW.pdf). Earlier PDFs are superseded.

## Set up once, supply only what changes

The skeleton is usable while the taste profile is empty. Do not fill it with a
fictional project or agent-selected examples just to make the repo look complete.

There are three layers:

| Layer | Reuse |
| --- | --- |
| Workflow and quality checks | Shared across landing pages, dashboards, websites and other frontend interfaces. |
| Your taste pack | Supplied by you when ready; reuse it across projects until you explicitly change it. |
| Project brief and art direction | The particular audience, job, content, constraints and any approved exceptions for this site. |

Changing the product does not require replacing your taste. General standards can
remain constant while layout, brand, density, assets and interaction vary with the
job. Project-specific references are optional additions you supply or authorize;
they do not automatically change the shared pack.

For the fewest repeated steps, keep one shared checkout of Design Kit and point
each site task at it. Make an independent copy/template if you need a separately
versioned context for a client or team. A fork is useful when maintaining a variant
of this context, but it is not required for each new interface. In every case,
site implementation stays in a separate target project. Reusing these instructions
does not require recreating their folders or rewriting their contents each time.

## Start each site

Give the agent this repository and the actual site's target folder, then a compact
mission:

> Use [path to design-kit] as design context. Work in [target site folder].
> Create a [concept / interactive prototype / production frontend] for [audience
> and product]. Outcome: [user job]. Primary action: [CTA/task]. Hard truths:
> [facts, required content, constraints]. Reuse my supplied taste pack.
> Project-specific differences: [only if needed].
> You may decide [creative authority]. Follow the context repo's workflow, inspect
> the real desktop/mobile result, and refine it before handoff.

The agent reads [AGENTS.md](AGENTS.md), [WORKFLOW.md](WORKFLOW.md),
[taste/PROFILE.md](taste/PROFILE.md), and relevant [review guidance](qa/README.md).
It applies that context to the target site. Site code, dependencies, assets, tests,
captures and project-specific design decisions belong in that target project.

**The user supplies the taste pack.** It is currently empty. The agent must not
choose, collect, add or replace taste references without explicit permission.
The PDF's reference recommendations do not override this rule. Changes to this
context repository must stay within the user's explicit request.

The agent should reuse information already supplied, inspect the target project,
and ask only for missing facts or decisions it cannot responsibly infer. It manages
the build/review/repair loop within your authorization. You still need to provide
the project-specific mission and make decisions explicitly reserved for you.
Repeated explanation can be removed; the actual visual and functional review of
each different interface still has to happen.

## What the context directs

One strong product-specific direction → early hero/core workspace plus a deeper
section/state and mobile → inspect and use it → make the smallest useful repair
or pivot → complete and self-refine → freeze the proven direction → verify the
requested delivery mode. Reuse only recurring accepted lessons.

Focus: art direction, UI/UX, typography, composition, copy, product visuals, motion,
responsive behavior, accessibility, frontend engineering and needed service
integrations. Backend development is outside scope.

The PDF's starter, tokens, components and verification tools describe resources
the agent should use or establish **in the actual site project when needed**.
They are not packages to build into this context repo. Publishing any actual site
is a separate action requiring authorization.
