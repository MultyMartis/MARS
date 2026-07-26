# Test Results (D5)

## Recorded post-Part-A offline suite (2026-07-26)

| Suite | Result |
|-------|--------|
| Python unittest (`tests/`) | **161/161 PASS** |
| Node harness offline | **28/28 PASS** |
| Native auth binding validator | **23/23 PASS** |
| D0 runtime charter validator | **30/30 PASS** |
| D1 durable dedupe validator | **35/35 PASS** |
| D2 sequential producer validator | PASS (network=false) |
| D3 controlled producer validator | PASS |
| D4 SITE-002 adapter validator | **PASS** |
| D5 first manual real-source validator | **PASS** (`ok: true`, failures=[]) |
| D5 Python module tests | included in 161 (test_producer_d5 categories A–AC coverage) |
| Absolute Storage path leak scan (D5 evidence) | **0** |
| Telegram-token-like scan (D5 evidence) | **0** |

## Part B

- Live POST: **NOT EXECUTED**
- Real producer HTTP: **0**
- No live integration test evidence

## Notes

- Prior documented baseline entering D5: Python 140/140; delta is D5 gate/CLI tests.
- Native Header Auth binding validator filename not re-run in this wave if absent as a separate runner; D3/D4 regressions and harness cover auth interface offline.
- Generic live (`push-webhook`) remains blocked; D4 `--apply` remains blocked; D5 missing `--apply` blocked with `network_calls=0`.
