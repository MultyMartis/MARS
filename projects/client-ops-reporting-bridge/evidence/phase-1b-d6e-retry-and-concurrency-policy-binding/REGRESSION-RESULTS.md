# REGRESSION-RESULTS

**Token:** `D6E_REGRESSION_PASS`

All suites offline except GET-only live baseline/postcheck. No production mutations.

| Suite | Result |
|-------|--------|
| Python unittest (`tests/` discover) | **211/211 PASS** (was 201; +10 D6E binding) |
| D6B freshness semantics harness | **20/20 PASS** |
| D6A delivery ledger harness | **11/11 PASS** |
| D6A delivery ledger validator | **48/48 PASS** |
| D6C activation lifecycle harness | **30/30 PASS** |
| D6E retry/concurrency policy harness | **54/54 PASS** (E40+EC10+INV4) |
| Node harness (`run-harness.mjs`) | **28/28 PASS** |
| Native auth binding validator | **23/23 PASS** |
| D0 documentation validator | **30/30 PASS** |
| D1 durable dedupe validator | **35/35 PASS** |
| D2 sequential producer validator | **47/47 PASS** |
| D3 controlled producer validator | **47/47 PASS** |
| D4 site002 adapter validator | **58/58 PASS** |
| Telegram semantics evidence validator | **14/14 PASS** |
| D6E artifact secret scan | **PASS** (`D6E_SECURITY_GATE_PASS`) |
| Extension security-scan (pre-existing chat_id_numeric REVIEW) | REVIEW (no new D6E findings) |

Workstream A ledger: unchanged.
Workstream B freshness: unchanged.
Workstream C lifecycle: unchanged.
Workstream D unattended: not started.
Automatic retries: 0.
Max safe concurrency: 1.
