# Regression D6G1

| ID | Result | Note |
|----|--------|------|
| R1 | PASS | Wrapper calls server dispatcher after terminal |
| R2 | PASS | Scheduled + admin share same dispatcher |
| R3 | PASS | Exact run_id dispatched |
| R4 | PASS | Re-dispatch → ALREADY_DISPATCHED |
| R5 | PASS | Later manual run independently reportable |
| R6 | PASS | Missing offers → ATTENTION |
| R7 | PASS | FAILED path still dispatch-capable (code path) |
| R8 | PASS | Delivery with Windows poller disabled |
| R9 | PASS | Poller task disabled / cannot trigger |
| R10 | PARTIAL | Poller+watchdog disabled/hidden; monitor Hidden change access-denied (daily only) |
| R11 | PASS | Server watchdog logic detects absent scheduled import |
| R12 | PASS | Watchdog skips when today’s terminal exists |
| R13 | PASS | Marker per reporting date |
| R14 | PASS | No stale producer candidate selection on server path |
| R15 | PASS | Admin launch permission/token preserved |
| R16 | PASS | Admin async enqueue (~233–300ms class) |
| R17 | PASS | Webhook auth HTTP 202 |
| R18 | PASS | No secret values in committed evidence |
| R19 | PASS | Workflow active (20 nodes) |
| R20 | PASS | Data Table FIRST_SEEN / dedupe event_id |
| R21 | PASS | Russian UX preserved |
| R22 | PASS | Deployed hashes verified against worktree sources |

`D6G1_REGRESSION_PASS` with R10 residual noted for catalog monitor window style.
