# Operator Scope Authority Sync — Corvonero v7

**Audit ID:** `operator-scope-authority-sync-v7`  
**Generated:** 2026-06-22

---

## Count reconciliation

| Expected stale records | Identified | Reconciled |
|------------------------|----------:|-----------:|
| 6 | 6 | **YES** |

Previous contract audit (`orca-production-contract-audit-v7.json`, 2026-06-22T06:41:14Z) reported **6** HIGH violations under `INV-SCOPE-02`. Independent comparison confirms exactly six authority/production mismatches. No discrepancy.

---

## Stale authority records

| Service ID | Service | Authority (before) | v7 production | Group | Corrected authority |
|------------|---------|-------------------|---------------|-------|---------------------|
| SVC-04 | внедрение 1С | HOLD | ACTIVE NARROW | CORV-G01-04 | ACTIVE NARROW |
| SVC-06 | обслуживание 1С | HOLD | ACTIVE | CORV-G01-06 | ACTIVE |
| SVC-20 | расчёт себестоимости | HOLD | ACTIVE NARROW | CORV-G04-01 | ACTIVE NARROW |
| SVC-21 | планирование закупок | HOLD | ACTIVE NARROW | CORV-G04-02 | ACTIVE NARROW |
| SVC-22 | платёжный календарь | HOLD | ACTIVE NARROW | CORV-G04-03 | ACTIVE NARROW |
| SVC-28 | перенос данных / миграция | HOLD | ACTIVE NARROW | CORV-G05-06 | ACTIVE NARROW |

---

## Root cause

- v7 production dataset and group registry correctly represent operator-approved scope after Production Scope Recovery Gate **PASS**.
- `operator-service-scope-v1.json` retained pre-recovery `HOLD — NO VALID COMMERCIAL DEMAND` and `recovery_required: true` for these six services.
- No commercial or architectural defect in v7 production data.
- Technical authority-registry drift only.

---

## Evidence basis

- `production/recovery/hold-group-review-v1.json` — commercial recovery decisions per group
- `production/recovery/commercial-scope-recovery-registry.json` — protected seed anchors
- `production/recovery/v7-production-input-package.json` — v7 reactivation package
- `production/validation/production-scope-recovery-gate.json` — gate PASS
- `production/final-group-registry-v7.json` — active group statuses
- `production/direct-commander-production-dataset-v7.json` — unchanged production truth (read-only)

---

## Synchronization applied

Updated **only** `production/operator-service-scope-v1.json`:

- `current_group_status`: HOLD → ACTIVE / ACTIVE NARROW (matching v7 group registry)
- `recovery_required`: true → false
- `protected_seed_refs` and `last_authority_sync` added per service
- Registry-level `last_authority_sync` metadata added

**Production dataset v7 was not modified.**
