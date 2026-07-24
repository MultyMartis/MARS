# Test results — Phase 1B-C0S

## Pre-apply gates

| Gate | Result |
|------|--------|
| Python unittest | 59/59 PASS |
| Node harness | 28/28 PASS |
| Template validator | 18/18 PASS |
| Native auth PUT validator | 23/23 PASS |
| Phase 1B-B2 evidence | PASS |
| Telegram secret file present (ignored) | PASS |
| Telegram target file present (ignored) | PASS |
| Target chat ID | 499423375 match |
| Message contract | PASS |
| Proposed integration (pre) | PASS |
| Semantics runner dry-run | PASS |
| Security scan | CLEAN |

## Live semantics

| Test | Result |
|------|--------|
| Level 1 structural | `PATTERN_B_STRUCTURALLY_SUPPORTED` — HTTP 202; exec `3407`; marker after Respond |
| Level 2 Telegram | `PATTERN_B_TELEGRAM_AFTER_RESPOND_CONFIRMED` — HTTP 202; exec `3408`; 1 Telegram run; 1 delivered |
| Pattern A | NOT RUN (Pattern B Level 2 consumed the one authorized message) |
| Async branch live | NOT RUN (doc evaluation only; message cap) |
| Final decision | `PATTERN_B_CONFIRMED` |

## Telegram external delivery

| Field | Value |
|-------|-------|
| Max authorized | 1 |
| Attempted | 1 |
| Delivered | 1 |
| Chat ID | 499423375 |
| Credential ID | `2bIC5376l7ElXb4B` |
| Content class | synthetic semantics test |
| Production data | NO |
| Secrets | NO |

## Post-apply

| Gate | Result |
|------|--------|
| Real workflow unchanged | PASS |
| Temp exact-name count | 0 |
| Proposed integration updated (ignored local) | PASS — not applied |
| Evidence validator | (run after pack complete) |
| Security / leakage | (run after pack complete) |

## Readiness

`READY_FOR_TELEGRAM_SANDBOX_INTEGRATION_APPLY`
