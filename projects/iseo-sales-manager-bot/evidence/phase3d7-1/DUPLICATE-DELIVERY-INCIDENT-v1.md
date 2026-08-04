# DUPLICATE DELIVERY INCIDENT v1

**Phase:** 3D.7.1 Emergency Duplicate Delivery Containment  
**Date:** 2026-08-04  
**Workflow:** Operational.dev `xSnXPy8cEHoZw6xG`  
**Verdict at discovery:** `STOP — PRODUCTION DUPLICATE LEAD DELIVERY LOOP`

## Operator observation

Around 2026-08-04 20:05–20:08 +07, one synthetic test lead was delivered repeatedly to all eligible recipients (1 Admin + 3 moderators). Cards continued arriving on every ~30s Gmail poll.

## Immediate containment

| Check | Result |
|---|---|
| Operational.dev deactivated | YES (was active → inactive @ 13:13 UTC) |
| Admin.dev kept active | YES |
| Sales-Manager-v2 kept inactive | YES |
| Active Gmail intake during containment | **0** |
| Further test leads sent | **0** |
| Client contact | **0** |
| AI | **OFF** (OpenRouter disabled) |

## Exact duplicate counts (sanitized)

| Metric | Value |
|---|---:|
| Unique business leads | **1** (`stable_lead_ref` hash `C3EF8E536C35E9CC`) |
| Operational executions processing that lead | **16** (ids 20637–20652) |
| Telegram cards attempted | **64** (16 × 4) |
| Cards per recipient | **16** |
| Telegram API successes (message created) | **64** |
| LEAD_DELIVERIES rows written during incident | **0** (stamp crashed before upsert) |
| Gmail PROCESSED during incident | **0** (never reached) |
| Execution terminal error | `Can't use .first() here [line 9, for item 0]` on **Stamp Delivery Result** |

## Root cause (one line)

`Stamp Delivery Result` ran in `runOnceForEachItem` and called `$input.first()`, threw after successful multi-recipient Telegram sends → LEAD_DELIVERIES never persisted → Gmail never finalized → every poll re-fetched the same message and resent to all four recipients.

## Repair summary

1. Stamp rewritten to `runOnceForAllItems` (no `$input.first()`).
2. Claim-before-send path added (`Prepare Delivery Claims` → upsert claim → restore items → send).
3. Aggregate Gmail finalize bound to **Admin-anchor delivered** (does not wait for all moderators).
4. Affected lead reconciled to `delivered` in LEAD_DELIVERIES + CONFIG `tg_delivered:*` + Gmail finalize.
5. Operational.dev reactivated; natural polls showed **0** further sends across ≥3 intervals.

## Residual

Operator live confirmation of a **new** unique synthetic lead (exactly one card per recipient) remains pending — see acceptance receipt.
