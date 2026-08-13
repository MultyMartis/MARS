# REMINDER OBSERVABILITY — Phase 3H.8

Contract: `iseo-reminder-observability-v1.1` (see architecture doc).

`/reminder_status` now includes:
- last evaluation timestamp
- pending count at last evaluation
- last decision (SENT / SKIPPED_ZERO_PENDING / SKIPPED_ALREADY_SENT / ERROR / …)
- last successful send + recipient count
- active error if present

No secrets / PII in command text.
