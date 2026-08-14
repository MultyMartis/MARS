# REAL ACCEPTANCE LEAD PREP v1

**Alias:** `REMINDER_ACCEPTANCE_LEAD_2`  
**Sanitized id hash:** `LEAD_A6A0FB0DBFF6`  
**Action:** existing reopen contract `spam → pending`  
**Actor:** `PHASE_3H82_OPERATOR`  
**When:** 2026-08-14 (after technical repair)

## Proof (no PII)

| Check | Result |
|---|---|
| Same lead ID | yes (`same_lead=true`) |
| Prior status | spam |
| Current status | pending |
| Spam history preserved | `spam_at` still present |
| Event | one `manager_reopened` |
| New lead row | no (CLEAN still 129 rows) |
| Automatic new-card resurface | false (no Telegram send in reopen TMP) |
| pending_count | 31 (was 30 before reopen; tests excluded) |

`REMINDER_ACCEPTANCE_LEAD_1` / `LEAD_3990BF2451B7` remains pending from Phase 3H.8 (not closed). Only **one** additional genuine spam lead was reopened this phase.

Lead left untouched after prep: do not mark Spam/Processed; do not send a manual production reminder.
