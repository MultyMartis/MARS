# TEST-RESULTS — D6DB (pre-commit, offline)

| Suite | Result |
|-------|--------|
| D6D harness D1–D60 | **60/60 PASS** |
| D6D scheduler/runtime DS1–DS10 | **10/10 PASS** |
| D6D combined | **70/70 PASS** |
| Python `test_unattended_d6d` | **5/5 PASS** |
| Python unittest discover | **216/216 PASS** |
| D6A delivery-ledger harness | **11/11 PASS** |
| D6A validator | **48/48 PASS** |
| D6B freshness harness | **20/20 PASS** |
| D6C lifecycle harness | **30/30 PASS** |
| D6E harness | **54/54 PASS** |
| D6E concurrency | within D6E harness PASS |
| Python `test_retry_policy_d6e` | **10/10 PASS** |
| Node harness | **28/28 PASS** |
| Native auth | **23/23 PASS** |
| D0 | **30/30 PASS** |
| D1 | **35/35 PASS** |
| D2 | **47/47 PASS** |
| D3 | **47/47 PASS** |
| D4 | **58/58 PASS** |
| Telegram semantics | **14/14 PASS** |
| SITE-002 marker `py_compile` / PS parse | PASS |
| D6D `node --check` | PASS |
| Scoped security scan | PASS (`D6DB_SECURITY_CLEAN`) |

No live producer or monitor execution.
