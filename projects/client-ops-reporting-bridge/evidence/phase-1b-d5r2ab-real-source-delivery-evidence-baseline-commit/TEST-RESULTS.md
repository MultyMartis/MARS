# TEST-RESULTS — D5R2AB (pre-commit offline)

All suites offline. No live requests. No n8n mutations. No Telegram. No monitor.

| Suite | Result |
|-------|--------|
| Python unittest (`tests/`) | **181/181 PASS** |
| D5R authority (`test_producer_d5r_authority.py`) | **20/20 PASS** |
| Node harness offline (`n8n/harness/run-harness.mjs`) | **28/28 PASS** |
| Native auth binding validator | **23/23 PASS** |
| D0 charter validator | **30/30 PASS** |
| D1 durable dedupe validator | **35/35 PASS** |
| D2 sequential producer validator | **47/47 PASS** |
| D3 controlled producer validator | **PASS** (gates ok / fail_count=0) |
| D4 site002 adapter validator | **58/58 PASS** |
| D5 first manual real-source validator | **PASS** |
| D5R authority alignment validator | **PASS** |
| Template validator | **18/18 PASS** |
| Telegram message/sandbox validators | **PASS** |
| Activation client syntax (`node --check`) | **PASS** |
| JSON syntax (D5R2/D5R2A/D5R2AB packs) | **0 failures** |
| Secret-value scan (accepted loci) | **0 hits** (`D5R2AB_SECURITY_CLEAN`) |

D5R2 / D5R2A dedicated evidence validators: not present as separate runners; factual evidence reviewed against accepted charter + security scan.
