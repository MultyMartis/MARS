# TEST-RESULTS (D5R)

## Suites (post-D5R)

| Suite | Result |
|-------|--------|
| Python unittest (`tests/`) | **181/181 PASS** (includes 20 D5R authority tests) |
| D5R module tests (`test_producer_d5r_authority.py`) | **20/20 PASS** |
| Node harness offline | **28/28 PASS** |
| Native auth binding validator | **23/23 PASS** |
| D0 runtime charter validator | **30/30 PASS** |
| D1 durable dedupe validator | **35/35 PASS** |
| D2 sequential producer validator | **PASS** (`passed=47`, `failed=0`, `network=false`) |
| D3 controlled producer validator | **PASS** (`passed=47`, `failed=0`) |
| D4 SITE-002 adapter validator | **PASS** |
| D5 first manual real-source validator | **PASS** (`ok: true`, failures=[]) |
| D5R authority alignment validator | **PASS** (`ok: true`, failures=[]) |
| Security / path leak scan (D5R evidence via validator) | **CLEAN / 0** |

## Caps verified

- Network / live POST: **0**
- Monitor executions: **0**
- SITE-002 repo edits by D5R: **0**
- D5 charter consumed: **false**
- D5 real_http_requests: **0**
