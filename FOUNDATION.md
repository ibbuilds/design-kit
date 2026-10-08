# Visual foundation — proposed by Design Kit or supplied by the user

The foundation is the **user-controlled style baseline for image iterations**. The user can provide it directly, edit it, or ask Design Kit to **propose and improve it using actual visual references**. A proposal is not automatically approved. The foundation starts lightweight; the first selected component image helps refine it before similar components and sections inherit the look.

## Minimum decisions worth capturing

| Dimension | Status: user-confirmed / kit-proposed / unknown | Value, source or selected image |
| --- | --- | --- |
| Intended brand character and overall visual impression | | |
| Typography roles: headline, label, body and emphasis | | |
| Color roles: dominant surfaces, text, accents, contrast | | |
| Geometry, border and depth/surface language | | |
| Component density, proportions and spacing rhythm | | |
| Iconography and imagery treatment, if relevant | | |
| Content/assets that must remain exact | | |
| Exclusions and protected prior visual choices | | |
| Framing and dimensions for the requested unit(s) | | |

Don't invent an authoritative font file, set of tokens or trademark identity from a generated screenshot. Label inferred relationships and actual user-selected values separately. An image can demonstrate style without resolving exact type metrics or browser CSS.

## Foundation grows with the first component

1. Reuse the user's decisions and inspected **Awwwards / One Page Love or other relevant source images** when a visual question remains open.
2. Propose only enough styling to generate a **first high-leverage element/component image**.
3. After each image round, review the result and ask the user what to change, keep or stop.
4. Once a component is selected, write down the visually meaningful stable relationships and use its **actual image** as the anchor for related components.
5. As the component library is tuned by the user or Design Kit, record **confirmed** revisions to the foundation before propagating them into group generations and sections.

The foundation is not a prerequisite to finishing an entire system before visual exploration, nor is an agent's first image a completed design system. Working component, section and page images should consistently inherit confirmed decisions while allowing task-appropriate variety.

## What remains outside Design Kit

A foundation is not a working component library, design token package, Figma document, React components or validated responsive behavior. The **visual component library** described in [COMPONENT_LIBRARY.md](COMPONENT_LIBRARY.md) consists of images and accepted relationships only. A separate implementation is entirely user-controlled and never initiated as a side effect.
