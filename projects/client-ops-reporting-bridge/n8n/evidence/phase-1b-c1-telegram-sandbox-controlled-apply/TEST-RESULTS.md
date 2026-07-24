# Test Results — Phase 1B-C1

## Pre-apply

| Suite | Result |
|-------|--------|
| Python unittest | 59/59 PASS |
| Node harness | 28/28 PASS |
| Template validator | 18/18 PASS |
| Native auth PUT validator | 23/23 PASS |
| B2 evidence (prior) | PASS |
| Telegram intake evidence | PASS |
| Semantics evidence | 14/14 PASS |
| Telegram secret boundary | PASS |
| Telegram target boundary | PASS |
| Message contract | 15/15 PASS |
| Proposed integration | 24/24 PASS |
| Composed PUT payload | 27/27 PASS |
| Apply runner dry-run | READY |
| Activation dry-run phrases | READY |
| Authenticated POST dry-run | BLOCKED_MATRIX_REPLAY (expected) |
| Authenticated POST `--c1-sandbox-test` dry-run | READY_C1_OVERRIDE |
| Security scan | CLEAN |
| Token leakage | 0 |
| URL leakage | 0 |
| Rollback validator/snapshot | PASS |

## Live

| Gate | Result |
|------|--------|
| Workflow PUT | 1 |
| Structural verification | PASS |
| Activation | 1 |
| Authenticated synthetic POST | 1 → HTTP 202 ACCEPTED |
| Execution added | 1 (24→25) |
| Telegram attempts/delivered | 1/1 |
| Duplicates | 0 |
| Deactivation | 1 |
| Final active=false | PASS |

## Post-operation

| Suite | Result |
|-------|--------|
| Python unittest | 59/59 PASS |
| Node harness | 28/28 PASS |
| Template | 18/18 PASS |
| Native auth | 23/23 PASS |
| Apply runner dry-run | BLOCKED_REAPPLY |
| POST matrix dry-run | BLOCKED_MATRIX_REPLAY |
| Security scan | CLEAN |
| Token leakage | 0 |
| URL leakage | 0 |
