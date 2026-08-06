# RETRY-BUDGET

**Token:** `D6E_RETRY_BUDGET_MODEL_DEFINED` · `D6E_NO_AUTOMATIC_RETRY_LOOP`

| Budget | Value |
|--------|-------|
| Automatic retry budget | **0** |
| Manual bounded retry budget (future) | **1** |
| Max safe concurrency | **1** |

`AUTOMATIC_RETRIES_ENABLED=NO`. Exhausted budget → reject (`RETRY_BUDGET_EXHAUSTED`). No retry queue worker / poller.
