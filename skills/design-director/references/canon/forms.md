# Forms and service journeys

Verified 2026-09-04; [sources](../sources.json). GOV.UK patterns are strongest for
transactional services. Do not force their page granularity onto expert tools.

## Ask only what is needed

- **Principle / problem:** Unnecessary questions and repeated entry increase burden
  and errors; people need to understand what a field asks and why.
- **Use:** Registration, applications, settings, data entry and search inputs.
- **Do not use:** Placeholder-only labels, unexplained formats or compulsory answers
  when “unknown/not applicable” is legitimate.
- **Alternatives:** Reuse previously supplied information with review, sensible
  defaults, optional fields, conditional questions and contextual hints.
- **Exceptions:** Re-entry can be essential for security or invalid data; don't
  prefill sensitive or uncertain answers as if confirmed.
- **Accessibility:** Persistent labels, associated instructions, input purpose and
  clear optional/required state. Support paste and accessible input methods.
- **Source / scope:** `gov-questions`, `wcag22` 3.3.2, 3.3.7; services and web input.

## Group or sequence by task

- **Principle / problem:** A manageable sequence reduces perceived complexity, while
  related information may need to remain visible for comparison.
- **Use:** One question/topic at a time for unfamiliar service journeys; grouped
  fields for short familiar tasks or expert cross-field comparison.
- **Do not use:** Split every field into a page regardless of task, or cram a long
  unfamiliar application onto one dense screen.
- **Alternatives:** Sections, conditional steps, save/resume, review summaries.
- **Exceptions:** Branching flows cannot honestly show a fixed total step count;
  sensitive save/resume needs privacy and expiry decisions.
- **Accessibility:** Clear headings, labels, back behavior that preserves input,
  meaningful progress and no unexpected automatic navigation.
- **Source / scope:** `gov-questions`, `nng-complex`; resolve the service/expert
  tension using audience expertise and actual dependencies.

## Validation and recovery

- **Principle / problem:** Explain the specific problem and the correction while
  preserving valid input; errors should not punish an unfinished answer.
- **Use:** Invalid or missing submission data; summary plus field messages for long
  forms where users need to locate several errors.
- **Do not use:** Generic “invalid,” color alone, premature errors during typing,
  or silently clear valid entries after failure.
- **Alternatives:** Forgiving formats, validation on appropriate completion events,
  inline guidance, linked error summary after submit.
- **Exceptions:** Cross-field or server errors may belong to a group/page; sensitive
  login responses must not reveal account existence.
- **Accessibility:** Focus the summary appropriately; link errors to fields and
  associate messages. Distinguish asynchronous status from intrusive alerts.
- **Source / scope:** `gov-errors`, `wcag22` 3.3.1–3.3.3; accessible service forms.

## Review before commitment

- **Principle / problem:** Let people verify important information and understand
  consequences before submission.
- **Use:** High-impact, legal, financial or long multi-step transactions.
- **Do not use:** Add a heavy review page to every low-risk reversible edit.
- **Alternatives:** Inline preview, confirmation at the consequential action, undo.
- **Exceptions:** Very large journeys may use section reviews; changed answers can
  invalidate dependent fields and must trigger a clear recheck.
- **Accessibility:** Change links have contextual names; return users to review
  without repeating the whole journey; place related labels and values together.
- **Source / scope:** `gov-check`, `wcag22` 3.3.4; public-service review and error
  prevention for consequential web submissions.
