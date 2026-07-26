# REGRESSION-RESULTS

Post-apply offline / repository validators (no production mutation by validators).

| Suite | Result |
|-------|--------|
| Python unittest (`tests/` discover) | **181/181 PASS** |
| Node harness (`n8n/harness/run-harness.mjs`) | **28/28 PASS** |
| Native auth binding payload validator | **23/23 PASS** |
| D0 documentation validator | **30/30 PASS** |
| D1 durable dedupe validator | **35/35 PASS** |
| D2 sequential producer validator | **47/47 PASS** |
| D3 controlled producer validator | **47/47 PASS** |
| D4 site002 adapter validator | **58/58 PASS** |
| D5 first manual real-source validator | **PASS** (failures=[]) |
| D5R site002 authority alignment validator | **PASS** (ok=true) |
| Telegram C1 sandbox evidence validator | **PASS** |
| Telegram semantics evidence validator | **14/14 PASS** |
| D6A delivery ledger harness | **11/11 PASS** |
| D6A delivery ledger validator | **48/48 PASS** |

Workstreams B/C/E/D: **not modified**.
