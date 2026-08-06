# ROLLBACK-PLAN

**Token:** D6B2_ROLLBACK_READY

## Method

Producer-only rollback (no n8n PUT):

1. Restore allowlisted modified files from 
ollback-baseline/ (exact HEAD pre-D6B content captured before apply declare).
2. Delete delivery_eligibility.py (absent at HEAD).
3. Re-run D6B harness expecting FAIL / pre-D6B stale→BLOCKED behavior.
4. No Data Table / workflow rollback required (untouched).

## Caps

- Rollback operations: max 1
- Actual rollback performed: **0** (validation passed)

Secrets are not stored in rollback baseline.
