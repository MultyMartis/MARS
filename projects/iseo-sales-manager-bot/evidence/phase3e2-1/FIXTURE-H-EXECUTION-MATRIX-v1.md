# FIXTURE H EXECUTION MATRIX v1

Sanitized matrix for Operational.dev executions tied to marker `ISEO_SM_FR2_H_PROBABLE_TEST`.  
No raw Gmail IDs, Telegram IDs, chat IDs, or workbook IDs.

| Wave | Time (UTC, approx.) | Claim before send | Recipients expanded | Sends attempted | Sends successful | Ledger durable? | Gmail finalize | Error class |
|------|---------------------|-------------------|--------------------:|----------------:|-----------------:|-----------------|----------------|-------------|
| 1 | ~00:04 | absent / fake-claimed | 2 | 2 | 2 | no (quota after) | no | Sheets quota after Telegram success |
| 2 | ~00:07 | absent | 2 | 2 | 2 | no | no | resend — no durable delivered |
| 3 | ~00:10 | absent | 2 | 2 | 2 | no | no | resend |
| 4 | ~00:13 | absent | 2 | 2 | 2 | no | no | resend |
| later | ~00:16–00:21 | n/a / failed | 0–1 | 0 | 0 | noisy | no | rate-limit / failed_terminal |

## Findings

- **Total repeated send waves:** 4
- **Cards per recipient per wave:** 1 (both recipients each wave when expansion=2)
- **Estimated cards:** 8
- Claims were **not** trustworthy before every resend (`Upsert LEAD_DELIVERIES Claim` used continue-on-error → fake claimed).
- Delivery key remained stable across polls for the same synthetic lead.
- CONFIG `tg_delivered:*` fallback was **absent** during the storm (blocked by LEAD_EVENTS quota path).
- Sheets quota after Telegram success was **incorrectly** treated as permission to resend on next poll.

Rate-limit is **not** an acceptable reason for duplicate Telegram sends.
