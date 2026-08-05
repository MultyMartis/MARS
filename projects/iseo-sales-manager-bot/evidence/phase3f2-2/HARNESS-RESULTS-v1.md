# HARNESS RESULTS v1 — Phase 3F.2.2

Offline harness over patched Help + Lead History Handler code.

**Result: 33/33 PASS** (see `HARNESS-RESULTS-RAW.json`).

## Event labels (1–10 + extras)

| ID | Check | Result |
|---|---|---|
| 1 | `telegram_sent` mapped | PASS |
| 2 | `delivered_to_employee` mapped | PASS |
| 3 | `lifecycle_reconciled` mapped | PASS |
| 4 | `lead_received` mapped | PASS |
| 5 | `reply_generated` mapped | PASS |
| 6 | unknown → `техническое событие` | PASS |
| 7–10 | timestamp/actor/order invariants | PASS |
| lc_* / delivery_failed / archive / manual | required phrases | PASS |

## Help (11–27)

| ID | Check | Result |
|---|---|---|
| 11–13 | templates selected | PASS |
| 14–18 | `/lead_history` placeholder + `/ai_on` integrity | PASS |
| 19–22 | pending / reminder_status / status / users | PASS |
| 23–24 | admin-only labelled; moderator safe | PASS |
| 25–27 | length / HTML balance / no duplicate sections | PASS |
