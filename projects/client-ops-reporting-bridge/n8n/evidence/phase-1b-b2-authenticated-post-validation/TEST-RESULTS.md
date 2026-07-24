# Test results — Phase 1B-B2

## Pre-test gates

| Gate | Result |
|------|--------|
| Python unittest | 59/59 PASS |
| Node harness | 28/28 PASS |
| Template validator | 18/18 PASS |
| Native auth PUT validator | 23/23 PASS |
| Live graph verification | PASS (`active=false`, nodes=9, headerAuth bound) |
| Credential metadata | PASS (id/name/type; no secret value) |
| Security scan extension | CLEAN |
| Runner dry-run | READY |
| Executions baseline | 0 |

## Matrix

| Metric | Value |
|--------|-------|
| Requests attempted | 28 |
| Requests completed | 28 |
| Diagnostic retries | 0 |
| Activation changes | 2 (activate + deactivate) |
| Executions final | 24 |
| Class matches | 27/28 (T26 documented native 422 discrepancy) |
| Critical auth/accept gates | PASS (T01/T02 reject; T05 accept) |
| Post-matrix dry-run | BLOCKED on `executions_baseline_zero` (intentional re-run guard) |

## Post-test

| Gate | Result |
|------|--------|
| Final `active` | `false` |
| Credential bound | YES |
| Telegram | absent |

## Verdict

**COMPLETE** — authenticated sandbox POST matrix passed; workflow returned inactive.
