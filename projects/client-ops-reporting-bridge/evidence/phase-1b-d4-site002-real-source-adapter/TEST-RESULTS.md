# Test Results (D4)

## Baseline before edits

| Suite | Result |
|-------|--------|
| Python unittest | 112/112 PASS |
| Node harness | 28/28 PASS |
| Native auth binding | 23/23 PASS |
| D0 | 30/30 PASS |
| D1 | 35/35 PASS |
| D2 | 47/47 PASS |
| D3 | 47/47 PASS |

## After D4

| Suite | Result |
|-------|--------|
| Python unittest | 140/140 PASS (112 + 28 D4) |
| Node harness | 28/28 PASS |
| Native auth binding | 23/23 PASS |
| D0 | 30/30 PASS |
| D1 | 35/35 PASS |
| D2 | 47/47 PASS |
| D3 | 47/47 PASS |
| D4 validator | 58/58 PASS |
| Security/secret scan (D4 loci) | CLEAN / 0 |
| D3 regression | 27/27 PASS |
| D4 categories A-AA | tests/test_site002_adapter_d4.py |
