# REGRESSION-RESULTS

**Token:** `D6D_REGRESSION_PASS`

All suites offline except GET-only live baseline/postcheck. No production mutations.

| Suite | Result |
|-------|--------|
| Python unittest (`tests/` discover) | **216/216 PASS** (211 prior + 5 D6D language-boundary) |
| D6B freshness semantics harness | **20/20 PASS** |
| D6A delivery ledger harness | **11/11 PASS** |
| D6A delivery ledger validator | **48/48 PASS** |
| D6C activation lifecycle harness | **30/30 PASS** |
| D6E retry/concurrency policy harness | **54/54 PASS** |
| D6D unattended integration harness | **70/70 PASS** (D60+DS10) |
| Node harness (`run-harness.mjs`) | **28/28 PASS** |
| Native auth binding validator | **23/23 PASS** |
| D0 documentation validator | **30/30 PASS** |
| D1 durable dedupe validator | **35/35 PASS** |
| D2 sequential producer validator | **47/47 PASS** |
| D3 controlled producer validator | **47/47 PASS** |
| D4 site002 adapter validator | **58/58 PASS** |
| Telegram semantics evidence validator | **14/14 PASS** |

Workstream A ledger: UNCHANGED
Workstream B freshness: UNCHANGED
Workstream C lifecycle: UNCHANGED
Workstream E retry/reconciliation: UNCHANGED
Workstream D unattended integration: OFFLINE IMPLEMENTED

Automatic retries: 0
Max safe concurrency: 1
Unattended production enabled: NO
