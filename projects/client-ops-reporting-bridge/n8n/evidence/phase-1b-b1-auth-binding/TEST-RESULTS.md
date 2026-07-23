# Test Results — Phase 1B-B1

## Pre-apply

| Suite | Result |
|-------|--------|
| Python unittest | 59/59 PASS |
| Node harness | 28/28 PASS |
| Template gates | 18/18 PASS |
| Credential dry-run | PASS (collision=0, schema_ok) |
| Proposed PUT validation | 23/23 PASS |
| Security scan (extension) | CLEAN |
| Secret length class | gte32 |
| Drift gate | PASS |

## Post-apply

| Suite | Result |
|-------|--------|
| Python unittest | 59/59 PASS |
| Node harness | 28/28 PASS |
| Template gates | 18/18 PASS |
| Secret leakage scan (authorized trees + live WF) | 0 matches |
| Live GET reconfirm | active=false; nodes=9; headerAuth; credential ref; executions=0 |
| Credential create dry-run | NAME_COLLISION (exact count=1) — expected |
| Auth binding PUT dry-run | versionId_drift vs pre-apply snapshot — expected safety abort |

## Not run

- Authenticated webhook POST
- Unauthorized webhook POST
- Workflow execution
- Telegram send
- Activation
