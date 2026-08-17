# CONFIG RECIPIENT RECONCILIATION — Phase 3H.9.2

CONFIG is cache/observability. ACCESS_CONTROL is authority.

| Field | Before | After |
|---|---|---|
| ACCESS live staff | 3 | **4** |
| `pending_reminder_active_recipients_count` | 4 | **4** |
| `active_recipients_count` | 4 (cached) | **4** |
| `/reminder_status` recipients (ACCESS-preferring) | would show 3 | **4** |

No CONFIG write was required: the cache already said 4. After restore, cache matches live ACCESS. CONFIG was not used to override ACCESS.
