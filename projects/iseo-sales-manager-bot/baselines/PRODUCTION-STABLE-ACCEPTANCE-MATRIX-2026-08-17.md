# Acceptance Matrix — Sales Manager v2 Production Stable Baseline 2026-08-17

**Designation:** Sales Manager v2 — Production Stable Baseline 2026-08-17  
**STATUS:** PRODUCTION STABLE  
**Evidence:** [../evidence/stable-baseline-20260817/](../evidence/stable-baseline-20260817/)  
**Note:** No synthetic production tests or reminder triggers were sent to fill this matrix.

| Area | Result |
|------|--------|
| Gmail intake | **PASS** |
| Full-source preservation | **PASS** |
| Line-break preservation | **PASS** |
| RAW/CLEAN separation | **PASS** |
| Literal raw callback | **PASS** |
| Legacy Gmail fallback | **PASS** |
| Telegram card delivery | **PASS** |
| Processed action | **PASS** |
| Spam action | **PASS** |
| Raw source action | **PASS** |
| Lifecycle preservation on raw click | **PASS** |
| Dedupe | **PASS** |
| Delivery retry guard | **PASS** |
| AI OFF | **PASS** |
| Reminder configuration | **PASS** |
| Reminder weekday gate | **PASS** |
| Monday weekend-backlog logic | **PASS** |
| Natural Monday reminder live acceptance | **PENDING OBSERVATION — NOT YET A FAILURE** |

### Pending observation detail

At freeze capture, Europe/Moscow was still **2026-08-16 Sunday**; first natural window **2026-08-17 10:00 Europe/Moscow** had not occurred. Label:

`STABLE_BASELINE_WITH_PENDING_NATURAL_REMINDER_OBSERVATION`

Gate: `SM_STABLE_ACCEPTANCE_MATRIX_COMPLETE`
