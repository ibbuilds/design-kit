# States, feedback and recovery

Verified 2026-09-04; [sources](../sources.json).

## Empty, loading and asynchronous work

- **Principle / problem:** Explain whether nothing exists, nothing matches, access
  is limited or work is underway; those states imply different next actions.
- **Use:** First use, search/filter emptiness, delayed content, submission and background jobs.
- **Do not use:** Treat failure as empty data, show fake percentages or use many
  competing spinners. Avoid flashing a loader for near-instant operations.
- **Alternatives:** Actionable first-use message, reset-filter link, retained content
  with local busy status, skeleton for known layout, real progress for measurable work.
- **Exceptions:** Latency and task risk determine thresholds; Fluent's short-wait
  numbers and Copilot animations are contextual, not universal UI rules.
- **Accessibility:** Status announcement without focus theft, reduced motion,
  labeled progress; preserve focus and valid input. Disable only conflicting actions.
- **Source / scope:** `carbon-loading`, `fluent-wait`, `nng-heuristics`; product
  waiting patterns with Microsoft-specific expression excluded.

## Feedback, errors and undo

- **Principle / problem:** Distinguish action received, completed and failed so
  people know whether to wait, retry, correct or continue.
- **Use:** Saves, uploads, async commands and recoverable changes.
- **Do not use:** Toast-only critical errors, silent partial success or retry buttons
  that can duplicate an irreversible action without reconciliation.
- **Alternatives:** Inline confirmation/error, persistent results, undo, retry failed
  items, saved draft, conflict resolution showing current versus proposed value.
- **Exceptions:** Optimistic UI suits recoverable low-risk actions only when rollback
  and conflict behavior are clear; don't invent backend guarantees in a design.
- **Accessibility:** Announce important changes with appropriate urgency, provide
  actionable text and reachable controls, retain keyboard focus context.
- **Source / scope:** `nng-heuristics`, `gov-errors`, `fluent-wait`; original synthesis
  for feedback/recovery, not a claim that Figma prototypes implement server behavior.

## Dialog or page

- **Principle / problem:** Use interruption only for a bounded decision that needs
  attention; modal layers create navigation and focus obligations.
- **Use:** Relevant confirmations, short contextual tasks and justified warnings.
- **Do not use:** Long complex flows, routine announcements or stacked dialogs.
- **Alternatives:** Inline disclosure, nonmodal panel, separate page, reversible undo.
- **Exceptions:** Home Office discourages general modals in its service context;
  APG defines how a necessary modal behaves, not a requirement to use one.
- **Accessibility:** Focus enters appropriately, remains within a true modal, Escape
  normally closes and focus returns meaningfully. Background is inert; do not mark
  a visually nonmodal panel as modal. Long content may need initial heading focus.
- **Source / scope:** `apg-dialog`, `home-timeout`; web interaction and scoped
  Home Office research respectively.

## Timeout and interrupted sessions

- **Principle / problem:** Give people time to react and a clear recovery path;
  unexpected expiry can erase effort and trust.
- **Use:** Services that actually expire for inactivity/security requirements.
- **Do not use:** Invent session limits as a design default or promise progress
  retention that the service cannot provide.
- **Alternatives:** Extend time, save/resume where permitted, reauthentication with
  restored context, explicit expiry page explaining what remains.
- **Exceptions:** Home Office's at-least-two-minute warning and observed countdown
  intervals derive from its service research; choose and validate local timing
  against security needs and WCAG's actual timing requirements/exceptions.
- **Accessibility:** Accessible warning, meaningful focus return, restrained time
  announcements, keyboard extension and enough time to respond.
- **Source / scope:** `home-timeout`, `wcag22` 2.2.1; don't generalize an operational
  service's limited assistive-technology study to every user population.
