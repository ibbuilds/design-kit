# Experience knowledge on demand

Retrieve only knowledge that changes the current decision. Project evidence and valid
established behavior lead; behavioral authorities do not choose palette, typography
or art direction. No task classification, consultation, external fetch or report is
mandatory. General research is not this product's user research.

Python 3.10+, relative to this skill:

```sh
python -B <skill>/scripts/experience.py --need validation
python -B <skill>/scripts/experience.py --need batch-selection --need live-status --need keyboard-access --platform web
python -B <skill>/scripts/experience.py --search --need inspector-selection --context tool
python -B <skill>/scripts/experience.py --read tool-modes --context tool
```

A precise `--need` returns only applicable complete sections. For exploration, `--search`
returns compact titles, matched needs, applicability and citations; select IDs, then
`--read` only useful sections. Known IDs bypass discovery. `--catalog` is optional;
never read the whole registry to perform a lookup. Full selected authority access/scope
records: `--authority-info <id>`. They remain in [experience.json](experience.json);
article provenance is in [sources.json](sources.json).

Default bounds: three sections / 10,000 serialized knowledge characters; explicitly
increase only for complementary questions (`--limit` <=6, `--max-chars` <=20,000).
Unknown needs add no knowledge. Platform-specific entries require `--platform`;
`--context` filters incompatible contexts. `--authority` restricts sources; mixed-source
sections require all listed authorities. Never silently widen restrictions.

Choose the interaction problem: an essay table may need reading hierarchy; an editable
grid needs record, selection and keyboard behavior. A shadow needs no UX lookup.
Stop when current knowledge suffices. Stable retrieved sections can be reused; fresh
Figma renders are still needed after relevant mutations.

The Canon remains directly readable by question: [foundations](canon/foundations.md),
[navigation](canon/navigation.md), [forms](canon/forms.md), [data work](canon/data-work.md),
[states](canon/states.md), [content](canon/content.md), [accessibility](canon/accessibility.md),
[platform](canon/platform.md), [access](canon/access.md), [commerce](canon/commerce.md),
[professional tools](canon/productivity.md). Do not load whole chapters by default.

Normative requirements, informative APG guidance, platform conventions, research,
design-system patterns and original heuristics retain their distinct evidence types,
exceptions and dates. Resolve conflicting advice by applicability, not votes.
Visual observation belongs to inspected references; task judgment stays in the task.
Figma verifies visual/structural intent, not keyboard execution or backend guarantees.

For voice, spatial/XR, deep script behavior or safety-critical/domain requirements,
retrieve current relevant platform/domain guidance only when the task requires it;
general UI heuristics cannot establish domain rules, safe thresholds or compliance.
Preserve supplied domain evidence. Paid authorities remain approved; never invent
inaccessible findings or replace them merely for free access. An HTTP 403 calls for
normal browser navigation to the same official resource or a canonical equivalent;
use legitimate available access, never spoof/bypass controls. Report any remaining
specific gap; it does not require more research when current context is sufficient.
