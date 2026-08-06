# Phase 1B-D6D2 — Unattended Producer Controlled Runtime Deployment and Dry-Run Verification

## Scope

Controlled dedicated producer runtime deployment + one bounded manual DRY_RUN against real SITE-002 completed monitor artifacts.

Not unattended production enablement. Not scheduler creation. Not live delivery proof.

## Results (sanitized)

| Item | Value |
|------|-------|
| Producer runtime | `X:\AI MARS STORAGE\runtime-checkouts\client-ops-site-002-producer\repo` |
| Pin | `e1d2a1786fd7d778957b74fb213cf5656231a256` |
| Kill switch | `DRY_RUN` (not ENABLED) |
| Marker deployment | **DEFERRED** (OPTION A — producer-only) |
| Artifact root | `...\scheduled-monitors\post-1c` |
| Complete candidates inventoried | 39 (46 run dirs; marker absent on all) |
| Selected candidate | `2026-07-10_13-27-20` (oldest by committed ordering) |
| Classification | `ONBOARDING_REQUIRED` → source_status `ATTENTION` |
| Age | 1692975s (> 93600) |
| Policy | `BLOCKED_STALE` / `STALE_REVIEW_REQUIRED` |
| Event ID | `7493aaa9-dd5b-5fb9-a317-b413adcb8426` |
| Request authorized | false |
| Activation / webhook / Telegram / DT mutations | 0 |
| n8n executions | 34 → 34 |
| Data Table rows | 4 → 4 |
| Workflow active | false → false |
| Producer scheduler created | false |
| Monitor scheduler modified | false |
| MAIN index mutations | 0 |
| Git commit/push | 0 |

## Evidence

`evidence/phase-1b-d6d2-unattended-producer-controlled-runtime-deployment-and-dry-run-verification/`

## Readiness

`READY_FOR_D6D2_RUNTIME_EVIDENCE_BASELINE_COMMIT`

## Production readiness (unchanged)

```
CLIENT_OPS_UNATTENDED_PRODUCTION_READY=NO
CLIENT_OPS_AUTOMATIC_SITE002_CONNECTION_AUTHORIZED=NO
D6D_UNATTENDED_PRODUCTION_ENABLED=NO
D6D2_PRODUCER_RUNTIME_DEPLOYED=YES
D6D2_MANUAL_DRY_RUN_VERIFIED=YES
D6D2_SCHEDULER_CREATION_AUTHORIZED=NO
D6D2_ENABLED_MODE_AUTHORIZED=NO
AUTOMATIC_RETRIES_ENABLED=NO
MAX_AUTOMATIC_RETRIES=0
MAX_SAFE_CONCURRENCY=1
HISTORICAL_D5R2A_ROW_RECONCILIATION_AUTHORIZED=NO
```

## Next (not started)

Phase 1B-D6D2B — Controlled Producer Runtime and Manual Dry-Run Evidence Baseline Commit

REPORT is chat-only for this phase. No commit/push in D6D2.
