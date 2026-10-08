# Design Kit — image-first visual exploration

[![Validate kit](https://github.com/ibbuilds/design-kit/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/ibbuilds/design-kit/actions/workflows/validate.yml)

[Install](#installation) · [Workflow](SKILL.md) · [Image iteration](IMAGE_WORKFLOW.md) · [Foundation](FOUNDATION.md) · [Reference tools](PROVIDERS.md)

**Design Kit is now for deciding an interface visually through generated images, section by section—not for building the final interface.**

The user defines or selects a starting design-system foundation. Design Kit helps explore the first representative section through **multiple specific image generations** and significant revisions. The selected first image and foundation become the anchors for subsequent sections. After the requested sections are visually resolved, the output is an ordered page storyboard/contact sheet and the image-based design decisions. **The user separately decides whether and how the actual design, components or code will be created.**

The existing reference-discovery knowledge is retained: [Awwwards and One Page Love integrations](PROVIDERS.md), the curated [REFERENCES.md](REFERENCES.md) catalog, visual craft principles and scoped research. Existing installer hosts and safe update behavior remain intact. Third-party skills are optional experiments, not dependencies.

## How to use

In the actual product project, request:

> Use $design-kit to explore the visual direction with **images only**. Begin from my existing design foundation and supplied references. Start with the hero section, generate and compare substantially different image directions, and refine the strongest one in meaningful chunks until I select it. Reuse that visual anchor for each subsequent section. After all sections are visually decided, present the ordered image storyboard and stop. Do not build the site, components or code.

Replace “hero” with the section you want to start with; you may request only a single section. Provide your foundation, original imagery/copy and known page sections where available. The kit should organize known constraints and propose missing visual choices clearly, **not invent an approved brand system**.

### What you get

| Stage | Deliverable | Owner |
| --- | --- | --- |
| Foundation | User-authored or user-selected visual rules, with unknowns labelled | User |
| First section | Candidate images, explicit major changes, strongest selected visual anchor | Design Kit explores; user accepts |
| Remaining sections | Section images that inherit the anchor, with purposeful variation | Design Kit explores; user accepts |
| Whole page | Ordered selected image set, storyboard/contact sheet, source decisions and unresolved gaps | Design Kit prepares visual handoff |
| Actual design and implementation | Figma/components/code/live pages, **only in a separate user-selected workflow** | User decides next action |

There is **no automatic two-iteration ceiling**. The desired number of image rounds depends on visible progress and the user's actual budget. Prefer large changes to composition, type/image hierarchy, density and art direction before small details. Images are visual hypotheses, **not functioning or responsive UIs**.

[SKILL.md](SKILL.md) owns the operating rules; [IMAGE_WORKFLOW.md](IMAGE_WORKFLOW.md) has concrete prompt/iteration examples. [ONBOARDING.md](ONBOARDING.md) and [BRIEF.md](BRIEF.md) preserve user decision rights and visual evidence. [WORKFLOW.md](WORKFLOW.md) is a compatibility pointer. Historical workflow/research records are not current defaults.

## Research and optional skills

Reuse user-supplied images first; inspect selected examples through the existing MCP connections when a particular section decision needs references. Do not force an Awwwards/One Page Love search for every round, crawl entire sites, or add services when existing references suffice. The useful MCP/reference flows stay part of the skill.

Skills from Skills.sh or other sources might assist image prompts or critique. Do not assume they improve output. Run comparable image tasks with and without an optional skill, assess the **resulting images** and human effort, review permissions/security, and keep only proven contributors. The kit does not automatically install them.

## Installation

The supported hosts and bundle paths are unchanged:

| Platform | Host flag |
| --- | --- |
| OpenAI Codex desktop/CLI/IDE | codex |
| Anthropic Claude Code | claude-code |
| Google Gemini CLI | gemini-cli |
| Google Antigravity | antigravity |

From a checkout, install or update into the real project (not this kit checkout):

~~~sh
python scripts/install.py "<target-project>" --host codex --check
python scripts/install.py "<target-project>" --host codex
~~~

For an existing global installation:

~~~sh
python scripts/install.py --scope user --host codex --check
python scripts/install.py --scope user --host codex
~~~

Select your actual host/scope. The installer copies the complete managed bundle, checks conflicts before writing, and preserves unrelated instructions, human changes and working MCP configuration. Updating this GitHub repository **does not automatically update previously installed copies**. See [HOSTS.md](HOSTS.md) and [PROVIDERS.md](PROVIDERS.md) for host-specific access issues. A legacy explicit `--with-software` routing option remains for compatibility; it does **not** turn the image-first skill into an autonomous implementation workflow.

## Verification

~~~sh
python -m unittest discover -s tests -v
~~~

Tests validate installation safety, packaging, helper behavior and instruction contracts. They **do not prove** that image generation tools are available, that the model will follow instructions, or that images are beautiful. Assess quality using actual comparable section images, user selection and realistic usage. A matched with/without-kit comparison is needed before attributing any uplift to the kit.

Older research and evaluations are preserved for provenance, but their previous artifact-first or implementation-first defaults no longer govern Design Kit.
