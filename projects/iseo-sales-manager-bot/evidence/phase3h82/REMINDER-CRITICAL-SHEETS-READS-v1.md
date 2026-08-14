# REMINDER-CRITICAL SHEETS READS v1

Traced reminder evaluation path only (Admin.dev). Per-execution reads are already unique: each sheet/range is read **once** per evaluation. No long-lived cache.

| Node | API | Range | Requests / eval | Retry (post 3H.8.2) | Can 429? | Failure aborts decision? | Per-run reuse |
|---|---|---|---|---|---|---|---|
| Read Reminder CONFIG | Sheets read | CONFIG default/all | 1 | native 4×15s | yes | yes (gate never runs) | once |
| Read CLEAN for Reminder | Sheets read | `lead_clean_v2` A1:ZZ500 | 1 | native 4×30s | yes | yes (pending never computed) | once |
| Read ACCESS_CONTROL for Reminder | Sheets read | ACCESS_CONTROL default/all | 1 + up to 3 Wait-loop retries | explicit 5s/15s/30s, max 4 | **yes — proven 10:00/10:15** | yes → `ERROR_SHEETS_429_ACCESS` | once; retries same node |
| Read REMINDER_DELIVERIES | Sheets read | A1:Z500 | 1 | native 4×30s | yes | yes (claims not built) | once |
| Upsert REMINDER_DELIVERIES Claim | appendOrUpdate | default | 1 per recipient **after** decision | native 3×30s (pre-existing) | yes | post-decision; not wrapped this phase | n/a |
| Upsert REMINDER_DELIVERIES Delivered | appendOrUpdate | default | 1 per recipient after send | native 3×30s | yes | post-decision | n/a |
| Apply Reminder Window CONFIG Write | appendOrUpdate | CONFIG | 1+extras | native 4×15s | yes | observability only; ERRORS fallback | n/a |

Recipient set is resolved from ACCESS_CONTROL **once** per evaluation (`Reminder Build Claims`). Expected recipients=4.

Mutations are not retried as a restarted workflow.
