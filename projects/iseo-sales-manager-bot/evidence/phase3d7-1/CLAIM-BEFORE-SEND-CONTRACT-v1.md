# CLAIM-BEFORE-SEND CONTRACT v1

## States

| State | Meaning | Terminal? | Resend? |
|---|---|---|---|
| `planned` | Expand selected recipient for this poll | no | yes (becomes claimed) |
| `claimed` | Persisted before Telegram API call | no | **blocked** while fresh; stale (>10m) → reclaim |
| `delivered` | Telegram success recorded | **yes** | **never** |
| `failed_retryable` | Send failed; attempts &lt; max | no | yes (bounded) |
| `failed_terminal` | Attempts exhausted / hard fail | **yes** | no |
| `skipped_ineligible` | Recipient not eligible | **yes** | no |

## Sequence

1. Derive deterministic `delivery_key = lead_delivery:<stable_lead_ref>:<opaque_recipient_ref>`.
2. Read LEAD_DELIVERIES; skip if `delivered` / terminal / fresh `claimed`.
3. **Prepare Delivery Claims** sets `claimed` for send candidates.
4. **Upsert LEAD_DELIVERIES Claim** persists claim (Sheets `appendOrUpdate` by `delivery_key`).
5. **Restore Claimed Delivery Items** reloads full payload (Sheets output is sparse).
6. Telegram send only when `__expect_telegram_send=true` and `skip_telegram≠true`.
7. **Stamp Delivery Result** (`runOnceForAllItems`) classifies delivered/failed.
8. **Append LEAD_DELIVERIES** upserts final status.
9. Aggregate finalizes Gmail on Admin-anchor delivered.

## Sheets limitation (documented)

Google Sheets is **not** a true atomic compare-and-set store. Guard is the safest serialized pattern available:

- n8n schedule executions are effectively single-flight for this workflow;
- claim row blocks concurrent polls for 10 minutes;
- stale `claimed` reconciles to bounded retry (not blind infinite resend);
- `delivered` is always terminal regardless of Gmail label outcomes.

## Forbidden key contents

execution id · timestamp · username · display name · row number · Telegram message id · mutable role labels
