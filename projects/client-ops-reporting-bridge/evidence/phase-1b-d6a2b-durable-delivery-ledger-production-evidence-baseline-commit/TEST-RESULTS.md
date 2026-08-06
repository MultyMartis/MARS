# TEST-RESULTS — D6A2B (pre-commit offline)

All suites offline. No live requests. No n8n mutations. No Telegram. No monitor.

| Suite | Result |
|-------|--------|
| Python unittest (`tests/` discover) | **181/181 PASS** |
| Node harness (`n8n/harness/run-harness.mjs`) | **28/28 PASS** |
| Native auth binding payload validator | **23/23 PASS** |
| D0 documentation validator | **30/30 PASS** |
| D1 durable dedupe validator | **35/35 PASS** |
| D2 sequential producer validator | **PASS** (fail_count=0) |
| D3 controlled producer validator | **PASS** (fail_count=0) |
| D4 site002 adapter validator | **PASS** |
| D5 first manual real-source validator | **PASS** (failures=[]) |
| D5R site002 authority alignment validator | **PASS** (ok=true) |
| Telegram C1 sandbox evidence validator | **PASS** |
| Telegram semantics evidence validator | **14/14 PASS** |
| D6A delivery ledger harness | **11/11 PASS** |
| D6A delivery ledger validator | **48/48 PASS** |
| Activation / ledger / D6A2 runner `node --check` | **PASS** |
| Secret-value scan (accepted loci) | **0 disallowed hits** (`D6A2B_SECURITY_CLEAN`) |

Static workflow structural validation for the D6A2 deployed ledger remains recorded under D6A2 pack token `D6A2_DEPLOYED_LEDGER_STATIC_VALIDATION_PASS`.
