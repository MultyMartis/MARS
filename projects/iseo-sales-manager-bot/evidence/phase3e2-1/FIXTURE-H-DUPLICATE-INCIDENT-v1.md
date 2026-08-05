# FIXTURE H DUPLICATE INCIDENT v1

**Marker (synthetic):** `ISEO_SM_FR2_H_PROBABLE_TEST`  
**Phase:** 3E.2.1  
**Date (UTC day):** 2026-08-05  

## Summary

Probable-test fixture H was correctly suppressed for customer reply, but the **same stable lead** was delivered to Telegram managers repeatedly (~four waves). This was a **duplicate-delivery regression**, not four unique fixtures.

## Containment

- Operational.dev deactivated while H remained eligible / looping.
- Admin.dev remained active.
- Sales-Manager-v2 remained inactive.
- No new Gmail intake activated.
- Already-delivered Telegram cards not deleted.
- ACCESS_CONTROL / roles unchanged.

## Duplicate scale (sanitized)

| Metric | Value |
|--------|------:|
| Send waves (approx.) | 4 |
| Cards per wave (two recipients) | ~2 |
| Estimated duplicate cards | **8** |
| Related executions inspected | 6 |

## Operator-facing impact

Managers received repeated identical test-suppression cards for the same marker/contact/site content.

## Related evidence

- [FIXTURE-H-EXECUTION-MATRIX-v1.md](FIXTURE-H-EXECUTION-MATRIX-v1.md)
- [LEDGER-RATE-LIMIT-ROOT-CAUSE-v1.md](LEDGER-RATE-LIMIT-ROOT-CAUSE-v1.md)
- [AFFECTED-H-RECONCILIATION-v1.md](AFFECTED-H-RECONCILIATION-v1.md)
