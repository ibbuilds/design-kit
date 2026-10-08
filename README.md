# Design Kit — image-first visual iteration

[![Validate kit](https://github.com/ibbuilds/design-kit/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/ibbuilds/design-kit/actions/workflows/validate.yml)

[Workflow](SKILL.md) · [Image iteration](IMAGE_WORKFLOW.md) · [Component library](COMPONENT_LIBRARY.md) · [Foundation](FOUNDATION.md) · [Reference MCPs](REFERENCE_ROUTER.md)

**Iterate with generated images, at any scale:** a word or type treatment, icon, individual control, component group, section or entire page. Design Kit is not a website/code generator.

## Component-first by default, not compulsory

For a multi-part interface:

1. **Foundation:** reuse your choices or let the kit propose a starting direction from inspected references. You control acceptance.
2. **First component:** iterate its images as many rounds as you want, making meaningful changes until its style is chosen.
3. **Visual component library:** reuse the accepted image to style related components. Once the shared direction stabilizes, generate **groups of related component images**. You or Design Kit can continue refining outliers.
4. **Sections, if requested:** compose section images using the chosen component imagery and foundation. Reuse their style across further sections.
5. **Page, if requested:** view selected section images together and refine the weakest relationships.
6. **Stop at any milestone:** one text image, component, group, visual library, section or page.

**After each image iteration or returned batch**, the kit shows the result, briefly compares it, and **asks what you want next**: revise, accept, change direction, make related components, move on or stop. There is no fixed two-pass limit, and no requirement to create a page for a smaller task. A user can also submit an existing full design image for direct visual refinement.

These are **image concepts**, not working or editable UI components. Final implementation/conversion is separate, user-authorized work.

## Example prompts

**One component:**

> Use $design-kit to explore images of my primary button. Use my foundation or suggest a provisional one from relevant inspected Awwwards/One Page Love references. Iterate with substantial visual changes and ask what I want after each image round. Do not build code.

**Extend the library:**

> Take my selected button image and generate consistent visual images of a secondary button, text link and filter chip. Batch related images once the style is established. Review the family with me.

**Any other size:**

> Improve only this headline / icon / card / section / full-page image by generating and comparing images. Preserve my accepted references and stop when I say.

[IMAGE_WORKFLOW.md](IMAGE_WORKFLOW.md) explains prompts and the feedback loop. [COMPONENT_LIBRARY.md](COMPONENT_LIBRARY.md) explains reuse, family consistency and batching. [BRIEF.md](BRIEF.md) is a blank project record.

## Reference advantage and efficiency

Existing Awwwards and One Page Love MCP integrations, the curated [REFERENCES.md](REFERENCES.md) catalog and [REFERENCE_ROUTER.md](REFERENCE_ROUTER.md) remain available for **actual inspected images** that settle a visual question. Reuse the accepted reference relationships and first component images across later components and sections rather than researching the same style repeatedly. The intended savings come from that reuse and from coherent group generations; **token savings are not yet measured or guaranteed**.

Optional third-party Skills.sh-style skills may be compared on actual image results when authorized; do not automatically install them or assume they help.

## Installation

Existing supported host flags: codex, claude-code, gemini-cli, antigravity. For project installation from this checkout:

~~~sh
python scripts/install.py "<target-project>" --host codex --check
python scripts/install.py "<target-project>" --host codex
~~~

For user scope:

~~~sh
python scripts/install.py --scope user --host codex --check
python scripts/install.py --scope user --host codex
~~~

The installer preserves managed file safety, local edits and working MCP configuration. A merged PR **does not automatically update existing installed copies**. See [HOSTS.md](HOSTS.md) and [PROVIDERS.md](PROVIDERS.md). Legacy --with-software routing remains an opt-in for a separately authorized frontend task.

## Verification and limits

~~~sh
python -m unittest discover -s tests -v
~~~

Tests verify packaging, installation safety, helper tools and instruction contracts. They **do not prove** visual quality, image-model compliance or savings. Real image outcomes and observable user effort are the measure; attributing improvement requires a matched **with/without-kit** task comparison. Historical implementation-first research is background, not an active default.
