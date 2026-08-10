# COUNTER RECONCILIATION

```json
{
  "received_rows": 127,
  "tests_approx": 84,
  "statuses": {
    "pending": 111,
    "empty": 2,
    "processed": 7,
    "spam": 7
  },
  "pending_production_approx": 37,
  "pending_id_suffixes_sample": [
    "40e51e26",
    "40e51e26",
    "40e51e26",
    "40e51e26",
    "40e51e26",
    "40e51e26",
    "e937e0ad",
    "a2d7795c",
    "26678d71",
    "243530de",
    "80a6bd3d",
    "4c99394a",
    "eff6b455",
    "42028e45",
    "42028e45",
    "42028e45",
    "42028e45",
    "42028e45",
    "42028e45",
    "42028e45"
  ],
  "reopen_events_total": 9,
  "delivery_rows": 109,
  "resurface_delivery_rows_approx": 12,
  "ai_enabled": "false",
  "last_poll_state": "success",
  "last_poll_success_at": "2026-08-10T09:24:06.932Z",
  "pending_reminder_active_recipients_count": "4",
  "pending_reminders_enabled": "true",
  "gmail_poll_heartbeat": "{\"last_poll_started_at\":\"2026-08-10T09:24:06.884Z\",\"last_poll_completed_at\":\"2026-08-10T09:24:06.932Z\",\"last_poll_state\":\"success\",\"last_poll_source\":\"scheduled\",\"last_poll_matching_messages\":0,\"last_poll_error_code\":\"\",\"last_poll_execution"
}
```

Received lifetime rows unchanged by resurface (no new lead identities for REAL_REOPEN_*).
Pending increased for three reopened spam→pending leads.
