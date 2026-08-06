# Rollback Architecture — Phase 1B-D0

**Status:** ARCHITECTURE (not executed)

| Area | Snapshot requirements | Rollback unit | Trigger | Who | Evidence | Historical executions | Telegram undo | Duplicate risk after rollback |
|------|----------------------|---------------|---------|-----|----------|----------------------|---------------|-------------------------------|
| Dedupe implementation | Pre-change workflow export + Data Table schema/row export if any | Workflow version + table drop/disable under charter | Failed D1 apply / bad uniqueness | Operator + programmer | Sanitized structural diff | Remain | N/A | May re-allow duplicates — stop producer |
| Exporter/adapter change | Git commit / allowlisted paths before change | Revert allowlisted code only | Regressions | Operator | Test results | N/A | N/A | Pause POST mode |
| Monitor integration | None expected (monitor unchanged) | Disconnect adapter only | Accidental coupling | Operator | Prove monitor untouched | Remain | N/A | Stop adapter |
| Endpoint/secret config | Local ignored file backup outside Git | Restore ignored files; rotate credential if leaked | Misconfig | Operator | Rotation note (no values) | Remain | N/A | Invalidate old secret |
| Scheduler connection | Task XML export / disabled state proof | Disable task | Unexpected runs | Operator | Task state screenshot/log sanitized | Remain | N/A | Disable immediately |
| Workflow activation | Pre-active versionId + inactive proof | Deactivate allowlisted workflow | Any anomaly | Operator / activation client | GET active=false | Remain | Cannot unsend | Deactivate + dedupe |
| Telegram delivery config | Pre-change node credential binding | Revert workflow PUT / unbind under charter | Wrong chat/bot | Operator | Structural diff | Remain | **Cannot undo sent messages** | Suppress via dedupe SENT |

## Hard truths

- Delivered Telegram messages **cannot** be undone.
- n8n historical executions remain after rollback.
- After rollback that removes dedupe, **stop producer** until duplicate risk is re-controlled.
