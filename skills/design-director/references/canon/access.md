# Onboarding, authentication and permissions

Verified 2026-09-04; [sources](../sources.json).

## Onboarding at the point of need

- **Principle / problem:** Help people reach a first useful outcome without requiring
  them to memorize a tour before understanding the task.
- **Use:** Unfamiliar workflows, first use, features whose consequences need explanation.
- **Do not use:** Compulsory multi-screen tours for self-evident controls or promotional
  tips that obstruct recurring work.
- **Alternatives:** Meaningful empty state, sample with clear labeling, contextual
  instruction, optional tour, discoverable help and safe exploration.
- **Exceptions:** Regulated or safety-critical operations may need explicit training
  and acknowledgment. A sample is never actual user data.
- **Accessibility:** Help is reachable by keyboard and not dependent on transient
  overlays; onboarding can be skipped/resumed where appropriate.
- **Source / scope:** `nng-complex`, `nng-heuristics`; learning and recognition,
  not proof of a particular activation/conversion metric.

## Authentication and account recovery

- **Principle / problem:** Permit secure access and recovery without unnecessary
  memory or transcription barriers.
- **Use:** Actual authentication requirements; distinguish sign-in, enrollment,
  recovery and reauthentication states.
- **Do not use:** Ban paste/password managers, impose arbitrary password rotation,
  require an account without reason or expose account existence in sensitive errors.
- **Alternatives:** Supported passwordless/passkey/SSO paths, reveal password control,
  recovery links and alternative accessible verification methods.
- **Exceptions:** Never invent a supported identity method or backend security policy;
  annotate intended behaviors and verify feasibility separately.
- **Accessibility:** Accessible Authentication (Minimum), redundant entry, labels,
  predictable focus and adequate time. Explain how recovery returns to the task.
- **Source / scope:** `gov-passwords`, `wcag22` 3.3.7–3.3.8; service and web access.

## Permission and denied access

- **Principle / problem:** Explain why access is needed and what happens if denied;
  unavailable work should not look like absent data.
- **Use:** Device permissions, role-limited actions, revoked access and sharing.
- **Do not use:** Ask for all permissions on first launch without context, or offer
  a disabled control with no explanation when users need a recovery path.
- **Alternatives:** Just-in-time request, partial workflow, settings/help link,
  request-access action when actually supported.
- **Exceptions:** Avoid disclosing sensitive resource existence; platform permission
  dialogs are system-owned and their wording/layout should not be fabricated.
- **Accessibility:** Explain state in text, keep denial/retry paths operable and
  return focus to context. Permission is not conveyed by low opacity alone.
- **Source / scope:** Original synthesis from `nng-heuristics`, `apple-accessibility`,
  `wcag22`; inspect target platform's current permission rules when implementing design.

## Accessible outbound contact

- **Principle / problem:** People may need alternatives to standard letters or
  telephone calls; capture communication needs without making them diagnose themselves.
- **Use:** Services that send outbound communications, especially public services.
- **Do not use:** Confuse preferences for receiving communications with how to contact
  support, or copy DWP's complete application journey into unrelated products.
- **Alternatives:** Accessible format selection, assisted support, editable contact
  preferences with options the service can actually fulfill.
- **Exceptions:** Updating an existing need may require a different flow from initial
  collection. Needs can change; do not make choices irreversible.
- **Accessibility:** Include written and spoken alternatives, plain language and
  an accessible way to request a format not listed.
- **Source / scope:** `dwp-formats` (source updated 2026-01-20); outbound benefit/service
  communication, not universal onboarding.
