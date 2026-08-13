# REAL REMINDER ACCEPTANCE LEAD — Phase 3H.8

| Field | Value |
|---|---|
| Alias | `REMINDER_PROD_LEAD_A` |
| Action | spam → pending |
| Same lead ID | yes |
| Spam history preserved | yes (`spam_at`/`spam_by`/`spam_reason` retained) |
| Event | `manager_reopened` appended |
| Automatic resurface | **no** |
| Alternate `REMINDER_PROD_LEAD_B` | not reopened |

Verify payload: current_status=pending, ok=true.
