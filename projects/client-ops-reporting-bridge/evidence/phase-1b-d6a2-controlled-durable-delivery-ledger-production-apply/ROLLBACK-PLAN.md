# ROLLBACK-PLAN

**Token:** `D6A2_ROLLBACK_SNAPSHOT_READY`

| Item | Value |
|------|-------|
| Pre versionId | `3d2fd6fc-bc17-4e0f-b9e5-086c959afd29` |
| Pre nodes | 17 |
| Fingerprint sha16 | `39278d6adb2edb75` |
| Fingerprint sha256 | `39278d6adb2edb75f81386e16e46a03431f16e6bbc929ebdae171ea3fbf90932` |
| Local snapshot | `local/client-ops-reporting-bridge/bzpm.ru/rollback/phase-1b-d6a2/pre-apply-workflow.put-payload.json` |
| Rollback phrase | `ROLL BACK CLIENT OPS D6A2 DELIVERY LEDGER BZPM` |
| Runner | `n8n/runners/run-client-ops-d6a2-delivery-ledger-production-apply.mjs --rollback` |

Rollback was **not** required: apply + static validation passed.
