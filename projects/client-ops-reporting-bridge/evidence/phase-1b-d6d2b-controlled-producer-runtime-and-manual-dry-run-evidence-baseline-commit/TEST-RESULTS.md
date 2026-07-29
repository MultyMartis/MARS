# TEST-RESULTS — D6D2B

## Pre-commit (MAIN working tree; offline)

| Suite | Result |
|-------|--------|
| D6D harness | **70/70 PASS** (d_pass=60, ds_pass=10) |
| Python `test_unattended_d6d` | **5/5 PASS** |
| D6A delivery-ledger harness | **11/11 PASS** |
| D6A validator | **48/48 PASS** |
| D6B freshness harness | **20/20 PASS** |
| D6C lifecycle harness | **PASS** (`D6C_OFFLINE_LIFECYCLE_HARNESS_PASS`) |
| D6E retry/concurrency harness | **PASS** (`D6E_OFFLINE_POLICY_HARNESS_PASS` + `D6E_CONCURRENCY_HARNESS_PASS`) |
| Python `test_retry_policy_d6e` | **10/10 PASS** |
| JSON parse D6D2+D6D2B evidence | **18/18 PASS** |
| Claim hygiene | **PASS** (0 overclaim hits) |
| Scoped security scan | **PASS** (0 secret hits) |

Manual producer DRY_RUN: **not rerun** (authorized evidence already accepted).

Post-commit results: filled after commit wave.
