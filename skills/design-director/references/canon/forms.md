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

## Dependencies, trust and a usable record

- **Principle / problem:** Explain prerequisites and information use, then distinguish completed, incomplete and blocked work.
- **Use:** Long, dependent or nonlinear services; choose the closer service context.
- **Do not use:** Treating a visited section as complete or adding a task list to a short linear form.
- **Alternatives:** Preserve answers between tasks, expose dependencies invalidated by changes, and provide a supported record of submission.
- **Exceptions:** Record/download, privacy and save/resume promises must match actual product support.
- **Accessibility:** Meaningful task status, clear dependency explanations, humane progression and reachable review/correction.
- **Source / scope:** `uswds-forms` emphasizes expectations/trust/progression/records; `gov-tasks` supplies completion/dependency guidance. Design-system patterns verified 2026-09-05, not universal journey templates or mandatory paired consultation.

## Booking and time-dependent availability

- **Principle / problem:** Separate finding an option, selection, review, commitment and confirmation.
- **Use:** Booking, scheduling and availability-dependent transactions.
- **Do not use:** Inventing reservation holds or treating submitted payment as confirmed success.
- **Alternatives:** Clear timezone/duration, availability freshness, cancellation terms and input-preserving recovery when an option changes.
- **Exceptions:** Domain scheduling, payment and reschedule rules require current project evidence; no specialized medical/travel research is implied.
- **Accessibility:** Explain date/time formats, retain valid input and provide meaningful status and keyboard paths.
- **Source / scope:** Original transferable heuristic from `nng-heuristics`, `gov-check` and review/error prevention; verified 2026-09-05.

## Recurrence and time-zone intent

- **Principle / problem:** A recurring local wall time in a named zone differs from a fixed interval or UTC offset. Offset alone cannot preserve future local intent across daylight-saving or rule changes.
- **Use:** Cross-zone scheduling, recurring meetings, availability windows and rescheduling.
- **Do not use:** Silently shift nonexistent/ambiguous local times, treat an all-day date as a universal midnight instant, or infer participant availability from a selected slot.
- **Alternatives:** Show governing zone and local date/time; distinguish one occurrence from a series edit and preview affected instances. Explain conflicts/partial availability, preserve inputs on stale-slot rejection, and separate proposed, pending and confirmed changes.
- **Exceptions:** Temporal distinctions come from draft guidance. Series edit/cancel scope, dependencies, notification, holds and multi-party acceptance are project rules to establish explicitly; they are not guaranteed by a calendar UI.
- **Accessibility:** Label time-zone context and date changes; offer keyboard-operable alternatives and understandable confirmation/recovery after interrupted booking.
- **Source / scope:** `w3c-timezone` is an informative Group Draft Note (2025-07-26), not a Recommendation or endorsed standard; read 2026-09-05. Temporal intent is its evidence. Availability/conflict/recovery UI is original heuristic synthesis with `nng-heuristics` and `gov-check`, not domain scheduling research.
