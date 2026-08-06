# FINAL SOAK ERROR SUMMARY T0 v1

## Ops (Operational.dev) since final T+0

| Metric | Value |
|---|---:|
| Listed executions | 106 |
| Success | 106 |
| Error | 0 |
| Stuck | 0 |
| OpenRouter node fires with items | 0 |
| Customer/Gmail-send path fires | 0 |

## Admin.dev since final T+0

| Metric | Value |
|---|---:|
| Reminder ticks | success (sampled) |
| Access upsert | success (invariant violation content, not transport error) |
| Spam callbacks | success ×2 on same lead alias (duplicate callback attention) |
| Active ERRORS tab rows | SAFE UNKNOWN (no Sheets mutation-free dump this checkpoint) |

## Classification notes

- Transport/capacity: **PASS** (no repeated quota, no poll failures).
- Production invariants: **STOP** (revoked reactivation + delivery) — see checkpoint verdict.
- Duplicate spam callback pair on PROD_LEAD_3: **ATTENTION** (bounded; same action).

## Active errors

No active workflow execution error storm observed. Invariant STOP is **not** an n8n crash; it is an access/delivery policy violation.
