# LEDGER RATE-LIMIT ROOT CAUSE v1

## Causal chain

1. Telegram send **succeeds** for each expanded recipient.
2. Google Sheets returns **quota / too many requests** on claim append, LEAD_DELIVERIES stamp, and/or LEAD_EVENTS.
3. `Upsert LEAD_DELIVERIES Claim` had `onError: continueRegularOutput` → pipeline continued as if claim persisted (**fake claimed**).
4. `Append LEAD_EVENTS` without continue-on-fail blocked Gmail PROCESSED and CONFIG `tg_delivered:*` fallback writes.
5. Next schedule/webhook poll: no durable `delivered` / no CONFIG guard → Expand treated lead as eligible → **blind resend**.

## Failure-model mapping (Task C)

| # | Scenario | Observed / modeled |
|---|----------|--------------------|
| 1 | LEAD_DELIVERIES read quota error | Can look like empty if errors filtered — **must fail closed** |
| 2 | Claim write fails before send | Must send **zero** cards |
| 3 | Claim ok, send ok, stamp fails | Must **not** resend; reconcile |
| 4 | Send ok, Gmail finalize fails | Must **not** resend delivered recipient |
| 5 | Stale read after write | Prefer fail closed / reconcile |
| 6 | Error item → “no row” | Root contributor — patched |
| 7 | `claimed` retryable blindly | Root contributor — patched |
| 8 | Telegram success loses delivery key | Must preserve key through Stamp |
| 9–11 | Ref / recipient churn | Deterministic key + per-recipient guards |
| 12 | Probable-test different finalize | Synthetic path lacked Gmail finalize |
| 13 | Direct-inject bypass | Synthetic webhook used; claim still required |
| 14 | Tab/range mismatch | Not primary for H |
| 15 | Sheets retries whole batch | Amplifies quota under load |

## Non-acceptable interpretation

Sheets quota ≠ “send again”.
