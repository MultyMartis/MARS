# CORVONERO RUN 002 — SPPC-05 FAILURE ACCEPTANCE v1

**Run ID:** `corv-semantic-v2-20260626-002`  
**Status:** `BLOCKED_AT_SPPC_05`  
**Decision date:** 2026-06-26  
**Authority:** Operator review of CORVONERO NEW CONTROLLED SEMANTIC RUN PHASE 0/1/2 V1

## Operator decision

The operator **accepts** the SPPC-05 fail-closed result for run `corv-semantic-v2-20260626-002`.

## Immutable run boundary

| Property | Value |
|----------|-------|
| Run ID | `corv-semantic-v2-20260626-002` |
| Final validation attempt | **YES — non-resumable** |
| Lifecycle | `BLOCKED_AT_SPPC_05` |
| Lock | `RELEASED` |
| Full corpus calls | `0` |
| Canary calls | `0` |
| Resume | **PROHIBITED** |
| Run ID reuse | **PROHIBITED** |
| Evidence mutation | **PROHIBITED** |

## Confirmed failure causes

1. **Product confirmation adversarial FPR 0.0125** — false accept `CFM-PROD-UPD-02` («обновление sap business one до новой версии»).
2. **Problem query policy 9/10** — `PQR-ABSTAIN-03` expected ABSTAIN, received REJECT.

## Next validation gate

- ORCA Wave 3.1F targeted repair (separate task) must complete before any new SPPC-05 attempt.
- Next Corvonero validation attempt **must** use a **new run ID**: `corv-semantic-v2-20260626-003`.
- Phase 3 (canary / full corpus) remains **blocked** until operator authorizes a new controlled run after successful ORCA repair and SPPC-05 pass.

## Evidence preservation

The following artefacts are frozen read-only:

- `projects/mars-search-ppc-production/pilots/corvonero/runs/corv-semantic-v2-20260626-002/run-manifest-v1.json`
- `projects/mars-search-ppc-production/pilots/corvonero/runs/corv-semantic-v2-20260626-002/reports/sppc-05-sanitized-report-v1.json`
- `projects/mars-search-ppc-production/pilots/corvonero/runs/corv-semantic-v2-20260626-002/sanitized-execution-receipt-v1.json`
- `projects/mars-search-ppc-production/pilots/corvonero/runs/corv-semantic-v2-20260626-002/lifecycle-decision-v1.json`
- STORAGE: `C:\MARS Phenix\AI MARS STORAGE\mig\corvonero\semantic-runs\corv-semantic-v2-20260626-002\`
- Review package: `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-SPPC-05-REVIEW-PACKAGE-v1.md`
