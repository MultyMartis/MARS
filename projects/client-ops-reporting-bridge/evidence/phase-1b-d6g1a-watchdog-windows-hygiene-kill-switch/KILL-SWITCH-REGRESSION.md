# Kill Switch Regression

Server PHP 8.3 offline + brief production flip:

| Case | Result |
|------|--------|
| enabled true helper | PASS |
| enabled false helper | PASS |
| alias server_dispatch_enabled | PASS |
| false → BLOCKED_BY_KILL_SWITCH no HTTP | PASS |
| terminal remains | PASS |
| true not blocked by kill switch | PASS |
| delivered marker idempotent | PASS |
| watchdog false → BLOCKED_BY_KILL_SWITCH | PASS |
| restore true | PASS (`CLIENT_OPS_DISPATCH_ENABLED`: true) |
