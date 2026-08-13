# REMINDER OBSERVABILITY CONTRACT v1.1

**Product:** i-SEO Sales Manager Bot  
**Contract id:** `iseo-reminder-observability-v1.1`  
**Phase:** 3H.8

`/reminder_status` must expose (no secrets/PII):

- enabled
- schedule time
- timezone
- minimum pending
- eligible recipients count
- last evaluation timestamp
- pending count at last evaluation
- last decision: `SENT` | `SKIPPED_ZERO_PENDING` | `SKIPPED_ALREADY_SENT` | `ERROR` (plus explicit skip classes if recorded)
- last successful send timestamp
- last successful send recipient count
- current active error if any

CONFIG keys (observability/cache only; evaluation must use live CLEAN):
- `pending_reminder_last_evaluation_at`
- `pending_reminder_last_decision`
- `pending_reminder_last_pending_count`
- `pending_reminder_last_success_at`
- `pending_reminder_last_recipient_count`
- `pending_reminder_last_window` (only after successful window completion)
- `pending_reminder_last_error_safe`
