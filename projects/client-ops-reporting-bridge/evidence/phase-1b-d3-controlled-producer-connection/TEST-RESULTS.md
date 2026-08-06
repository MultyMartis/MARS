# TEST-RESULTS

| Suite | Result |
|-------|--------|
| Python unittest | 112/112 PASS (85 baseline + 27 D3) |
| Node harness | 28/28 PASS |
| Native auth PUT validator | 23/23 PASS |
| D0 validator | 30/30 PASS |
| D1 validator | 35/35 PASS |
| D2 validator | 47/47 PASS |
| D3 validator | PASS (post-live) |
| Live transport mocked tests | PASS |
| Network allowlist tests | PASS |
| Sequential / retry / event-id / source firewall | PASS |
| Security / secret / URL leakage scans | CLEAN (0) |
| Push-webhook generic block | NETWORK_DISPATCH_NOT_AUTHORIZED_D2 |
| D3 live without phrase | BLOCKED network_calls=0 |
| Third real POST after charter consumed | BLOCKED |
| Producer dry-run | offline READY / network_calls=0 |

## Live

| Path | Result |
|------|--------|
| FIRST_SEEN producer | HTTP 202 INTAKE_ACCEPTED / FIRST_SEEN / network_calls=1 |
| FIRST_SEEN n8n | execution 3414; executions 29→30 |
| FIRST_SEEN Data Table | rows 1→2; D3 event row=1 |
| FIRST_SEEN Telegram | attempts=1 delivered=1 message_id=6 |
| Exact replay producer | HTTP 200 DUPLICATE_SUPPRESSED / network_calls=1 |
| Exact replay n8n | execution 3415; executions 30→31; telegram_runs=0 |
| Exact replay Data Table | rows remain 2 |
| Final workflow | active=false running=0 |
