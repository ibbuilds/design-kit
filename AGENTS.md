# Design Kit repository — maintainer guidance

This repository packages an **image-first visual-iteration skill at any scale**. It does **not** create working designs, UI components, code or a custom runtime.

- [SKILL.md](SKILL.md) is canonical. For broad work, default to foundation -> **first representative component image** -> **image-based component library** -> sections -> optional page. For a text/icon/button/section-only request, respect that smaller scope. Support direct full-page image revision.
- The user controls foundation approval, image acceptance, iteration count and stopping point. Kit-proposed foundations are clearly provisional. **After every image iteration or returned batch**, show images and ask what the user wants next; never silently advance.
- First component image establishes style DNA. Use accepted exemplar images to generate related components, then coherent **groups/batches** when style is stable. The user or Design Kit can refine inconsistent visual component images. Reuse those actual images for section exploration.
- Preserve **Awwwards and One Page Love MCPs**, [REFERENCES.md](REFERENCES.md), [REFERENCE_ROUTER.md](REFERENCE_ROUTER.md), HOSTS/PROVIDERS access guidance and existing installer safeguards. Inspect actual sources; don't impose gratuitous repeated gallery research.
- Keep SKILL, IMAGE_WORKFLOW, COMPONENT_LIBRARY, FOUNDATION, README, BRIEF, PROMPT, ONBOARDING, EXECUTION, DESIGN_DIRECTION, WORKFLOW and docs usage guides aligned. Historical material is background.
- External skills are optional experiments. No automatic installs, paid calls, model switches, private uploads, external product writes, implementation, conversion, merge or force-push.
- Keep authored documentation in English and product-specific material in the target project. Run python -m unittest discover -s tests -v after package changes. Passing tests cannot establish image quality, model obedience or token savings.
