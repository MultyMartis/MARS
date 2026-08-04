# DELIVERY KEY ROOT CAUSE v1

## Checklist (Task C)

| # | Hypothesis | Result |
|---|---|---|
| 1 | Read LEAD_DELIVERIES before stable lead key exists | **Partial** — Format runs first; Expand uses `lead.lead_id`. Stable key existed. Not primary. |
| 2 | Expand builds different recipient ref each poll | **Rejected** — opaque refs identical across 16 polls |
| 3 | Delivery key includes timestamp/exec/row/display | **Rejected** — keys were `lead_delivery:<stable>:<u:HASH>` |
| 4 | LEAD_DELIVERIES upsert after Telegram skipped by later error | **CONFIRMED PRIMARY** — Stamp threw → Append LEAD_DELIVERIES never ran |
| 5 | Write node uses append instead of upsert | **Rejected as primary** — node was already `appendOrUpdate` by `delivery_key`; it never executed |
| 6 | Sheets read stale / wrong tab | **Secondary** — read returned empty/header only because nothing written |
| 7 | Delivery status value not recognized by skip | **N/A** — no prior status rows |
| 8 | Telegram success loses delivery key | **Contributing** — Stamp pairing via `.item` failed; fallback used `$input.first()` and threw |
| 9 | Merge/branch re-enters send | **Rejected** — no cycle; Skip→Stamp only |
| 10 | Gmail finalization does not run after fan-out | **CONFIRMED** — Aggregate/IF Success never reached |
| 11 | Telegram Skip Pass reconnects into send | **Rejected** — Skip→Stamp only |
| 12 | Business `tg_delivered:*` guard bypassed | **CONFIRMED secondary** — Update Last Success never ran → CONFIG guard never set; Classify stayed `new` |
| 13 | Moderator failure retries all including Admin | **N/A this incident** — all four TG sends succeeded each poll; failure was post-send stamp |
| 14 | Code returns all recipients after each send | **Rejected** |
| 15 | One recipient item replays whole batch | **Rejected** — each poll independently expanded 4 |
| 16 | LEAD_DELIVERIES key normalization differs read/write | **N/A** — no writes |
| 17 | Sheets numeric/text coercion changes key | **N/A** |
| 18 | Stable lead identity differs between polls | **Rejected** — identical hash |

## Exact root cause

1. **Primary:** `Stamp Delivery Result` mode `runOnceForEachItem` + `$input.first()` → hard fail after 4 successful Telegram sends.
2. **Cascade:** no LEAD_DELIVERIES persistence → no Aggregate → no Gmail PROCESSED/remove incoming → message remains intake-eligible.
3. **Amplifier:** business-level `tg_delivered:<gmailId>` never written; Classify Duplicate kept `duplicate_status=new`.

## Delivery key contract (unchanged shape; now enforced end-to-end)

`lead_delivery:<stable_lead_ref>:<opaque_recipient_ref>`

Forbidden in key: execution id, timestamp, username, display name, row number, Telegram message id, mutable role labels.
