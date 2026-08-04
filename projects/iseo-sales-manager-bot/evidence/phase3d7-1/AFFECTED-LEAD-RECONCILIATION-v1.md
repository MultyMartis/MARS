# AFFECTED LEAD RECONCILIATION v1

**Incident exec seed:** 20637 (representative of 20637–20652)  
**Stable lead hash:** `C3EF8E536C35E9CC`  
**Gmail message hash:** `FAE255BA5353022D`

## Actions (no Telegram sends)

1. Identified stable lead + four recipient delivery keys from Expand outputs.
2. Upserted **4** LEAD_DELIVERIES rows with `delivery_status=delivered` (appendOrUpdate by `delivery_key`).
3. Upserted CONFIG guards: `tg_delivered:<gmailId>`, `tg_attempts:<gmailId>=16`, runtime status keys.
4. Applied Gmail PROCESSED + removed incoming label via temporary Admin sidecar webhook.
5. Restored Admin.dev (57 nodes, active). Operational.dev remained inactive during reconcile.
6. **Did not delete** audit history; **did not** send additional cards; **did not** mass-delete Telegram messages.

## Webhook result

`{"ok":true,"reconciled":true}` (HTTP 200)

## Dry-run after reconcile

| Expectation | Result |
|---|---|
| Stable lead recognized | PASS |
| Four recipient states = delivered / skip | PASS |
| sends attempted | **0** |
| Gmail item finalized / excluded | PASS (webhook + dry-run) |

## Duplicate cards already in Telegram

Preserved. Count: **16 cards × 4 recipients = 64** historical duplicates. Lifecycle buttons on duplicates must remain idempotent (first transition wins) — Admin callback contract unchanged this wave unless proven broken.
