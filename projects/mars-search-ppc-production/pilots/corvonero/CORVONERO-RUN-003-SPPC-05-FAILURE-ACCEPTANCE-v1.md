# CORVONERO RUN 003 — SPPC-05 FAILURE ACCEPTANCE v1

**Run ID:** `corv-semantic-v2-20260626-003`  
**Status:** `BLOCKED_AT_SPPC_05`  
**Decision date:** 2026-06-26  
**Authority:** Operator review of CORVONERO RUN 003 SPPC-05 RETRY V1

## Operator decision

The operator **accepts** the SPPC-05 fail-closed result for run `corv-semantic-v2-20260626-003`.

## Immutable run boundary

| Property | Value |
|----------|-------|
| Run ID | `corv-semantic-v2-20260626-003` |
| Final validation attempt | **YES — non-resumable** |
| Lifecycle | `BLOCKED_AT_SPPC_05` |
| Lock | `RELEASED` |
| Full corpus calls | `0` |
| Canary calls | `0` |
| Resume | **PROHIBITED** |
| Run ID reuse | **PROHIBITED** |
| Checkpoint/receipt mutation | **PROHIBITED** |
| Evidence mutation | **PROHIBITED** |

## Confirmed failure causes (Run 003)

1. **Adjudicator ordering defect** — `PQR-ABSTAIN-03` expected ABSTAIN, received REJECT; `ambiguous_diy_problem` invariant applied before `SINGLE_ASSESSOR` branch.
2. **Generic ERP over-rejection** — `PC-ABSTAIN-01` expected ABSTAIN, received REJECT; generic `ERP` treated as explicit foreign platform / product-only reject.

## Phase 3 status

Phase 3 (canary / full 2368 corpus) remains **blocked**.

## Next validation gate

- ORCA Wave 3.1F targeted repair **v2** (this task family) must complete before any new SPPC-05 attempt.
- Next Corvonero validation attempt **must** use a **new run ID**: `corv-semantic-v2-20260626-004`.
- Run 004 is **not yet authorized** by this acceptance document.

## Co-frozen runs (immutable evidence)

| Run ID | Status |
|--------|--------|
| `corv-semantic-v2-20260626-002` | `BLOCKED_AT_SPPC_05` — immutable failed evidence |
| `corv-semantic-v2-20260626-003` | `BLOCKED_AT_SPPC_05` — immutable failed evidence |

## Evidence preservation

Frozen read-only artefacts under:

- `projects/mars-search-ppc-production/pilots/corvonero/runs/corv-semantic-v2-20260626-003/`
- `CORVONERO-RUN-003-SPPC-05-RESULT-v1.md/json`
- `CORVONERO-RUN-003-SPPC-05-REVIEW-PACKAGE-v1.md/json`
