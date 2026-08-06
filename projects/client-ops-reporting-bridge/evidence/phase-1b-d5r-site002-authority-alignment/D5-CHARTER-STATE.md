# D5-CHARTER-STATE

| Field | Value |
|-------|-------|
| D5 charter | UNUSED |
| `charter_consumed` | `false` |
| `real_http_requests` | `0` |
| Live POST | not performed |
| D5R consumed D5 charter? | **NO** |

## Rebuild decision

`D5_CHARTER_REQUIRES_REBUILD_FOR_RETRY` — **YES (for any future live retry)**

Reasons:

1. Source authority root cause requires SITE-002 monitor/runner repair before any truthful fresh candidate can be trusted from the scheduled path.
2. No safe existing candidate remains for a controlled D5 retry.
3. Event interpretation was not remapped in D5R, but the operational precondition for live retry changed (emitter must be fixed first).
4. Preserve current unused local charter metadata; do **not** consume it; do **not** enable POST. A future live phase must issue a new explicit one-time charter after monitor repair + fresh safe source acquisition.

D3 charter remains **CONSUMED**.
