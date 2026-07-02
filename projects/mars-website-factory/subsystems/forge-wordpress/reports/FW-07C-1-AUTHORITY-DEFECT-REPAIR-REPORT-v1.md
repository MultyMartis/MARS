# FW-07C-1 Authority Defect Repair Report

**Date:** 2026-07-02  
**Phase:** FW-07C-1  
**Task:** FW-07C-1 X-RUNTIME AUTHORITY DEFECT REPAIR AND REVALIDATION  
**Verdict:** REPAIRED

---

## Defect summary

Previous X-runtime revalidation failed closed with `RT_AUTHORITY_PATH_MISMATCH` because executable runtime authority still referenced legacy `E:\MARS-Localhost` while the binding registry and frozen baseline manifest already declared canonical `X:\MARS-Localhost`.

---

## Obsolete references identified

| File | Obsolete reference | Classification | Correction |
| ---- | ------------------ | -------------- | ---------- |
| `runtime/src/runtime-authority.mjs` | `RUNTIME_PARENT = E:\MARS-Localhost` | ACTIVE_EXECUTABLE_DRIFT | Aligned to `X:\MARS-Localhost` |
| `runtime/src/runtime-authority.mjs` | `allowed_root` under `E:\...fws-0001` | ACTIVE_EXECUTABLE_DRIFT | Aligned to `X:\...fws-0001` |
| `runtime/tests/run-runtime-preflight.mjs` | `FWS_ROOT` on `E:\` | ACTIVE_EXECUTABLE_DRIFT | Aligned to `X:\` |
| `runtime/tests/run-runtime-preflight.mjs` | `RECEIPT_ROOT` on `C:\MARS Phenix\...` | ACTIVE_EXECUTABLE_DRIFT | Moved to repo path `runtime/reports/fw07c1-x-runtime-preflight/` |
| `runtime/tests/run-runtime-binding-tests.mjs` | `FWS_ROOT` on `E:\` | ACTIVE_TEST_DRIFT | Aligned to `X:\`; added E/D/Shpigovsky regression cases |
| `runtime/tests/run-reparse-boundary-tests.mjs` | `FWS_ROOT` on `E:\` | ACTIVE_TEST_DRIFT | Aligned to `X:\`; parent test uses `X:\MARS-Localhost` |
| `runtime/README.md` | Phoenix receipt path | COMMENT_OR_EXAMPLE | Updated active receipt path |
| `FW-07C-1-VALIDATED-BASELINE-FREEZE-v1.md` | `E:\` / `C:\MARS Phenix\` paths | HISTORICAL_EVIDENCE | **UNCHANGED** |
| `runtime/FW-07C-1-VALIDATED-BASELINE-v1.json` | historical freeze metadata | HISTORICAL_EVIDENCE | **UNCHANGED** (manifest `allowed_root` already `X:\`) |
| `enforcement/README.md` denylist examples | `D:\` / `E:\` / `C:\MARS Phenix\` | COMMENT_OR_EXAMPLE | **UNCHANGED** |
| `FW-07C-SAFETY-ENFORCEMENT-PREFLIGHT-v1.md` | legacy path table | HISTORICAL_EVIDENCE | **UNCHANGED** |

---

## Repair scope

- Smallest executable authority alignment only.
- No operation definitions, schemas, failure taxonomy, risk classes, kill-switch semantics, mutation detector, four-operation allowlist, or Shpigovsky admission changes.
- No FP-0002 admission or capability expansion.

---

## Post-repair authority

| Field | Value |
|-------|-------|
| Runtime parent | `X:\MARS-Localhost` |
| Allowed root | `X:\MARS-Localhost\sites\wordpress\synthetic\fws-0001` |
| Receipt root | `projects/mars-website-factory/subsystems/forge-wordpress/runtime/reports/fw07c1-x-runtime-preflight/` |
| E root accepted | **NO** |
| D root accepted | **NO** |
| Shpigovsky accepted | **NO** |

---

## Regression tests added

1. Canonical X root admitted when path exists
2. Legacy E root rejected (`RT_AUTHORITY_PATH_MISMATCH`)
3. Legacy D root rejected (`RT_AUTHORITY_PATH_MISMATCH`)
4. Shpigovsky root rejected for `fws-0001`
5. Four-operation allowlist unchanged
6. Reparse parent denial updated to canonical `X:\MARS-Localhost`

---

## Revalidation linkage

- Receipt: [FW-07C-1-X-RUNTIME-REVALIDATION-RECEIPT-v1.md](FW-07C-1-X-RUNTIME-REVALIDATION-RECEIPT-v1.md)
- Artefact: [runtime/FW-07C-1-X-RUNTIME-REVALIDATION-v1.json](../runtime/FW-07C-1-X-RUNTIME-REVALIDATION-v1.json)
- Harness evidence: [runtime/reports/fw07c1-x-runtime-preflight/](../runtime/reports/fw07c1-x-runtime-preflight/)

---

*FW-07C-1 authority defect repair — canonical X runtime authority restored.*
