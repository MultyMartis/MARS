# TEST-RESULTS — D6B2B

All suites offline. No live requests. No n8n mutations. No Telegram. No monitor.

| Suite | Result |
|-------|--------|
| Python unittest (`tests/` discover) | **201/201 PASS** |
| D6B freshness semantics harness | **20/20 PASS** (B1–B15) |
| Node harness (`n8n/harness/run-harness.mjs`) | **28/28 PASS** |
| Native auth binding payload validator | **23/23 PASS** |
| D0 documentation validator | **30/30 PASS** |
| D1 durable dedupe validator | **35/35 PASS** |
| D2 sequential producer validator | **47/47 PASS** |
| D3 controlled producer validator | **47/47 PASS** |
| D4 site002 adapter validator | **58/58 PASS** |
| D5 first manual real-source validator | **PASS** |
| D5R site002 authority alignment validator | **PASS** |
| Telegram C1 sandbox evidence validator | **PASS** |
| Telegram semantics evidence validator | **14/14 PASS** |
| D6A delivery ledger harness | **11/11 PASS** |
| D6A delivery ledger validator | **48/48 PASS** |
| Secret-value scan (accepted loci) | **0 disallowed hits** (`D6B2B_SECURITY_CLEAN`) |

Tokens: `D6B2B_SEMANTIC_CLAIMS_CLEAN`, `D6B2B_PRODUCTION_SURFACE_CLAIMS_ACCURATE`.
