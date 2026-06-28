# ORCA Wave 3.1F — Targeted SPPC-05 Repair Decisions v2

**Date:** 2026-06-26  
**Verdict:** `ORCA_WAVE_3_1F_TARGETED_SPPC05_REPAIR_V2 — PASS`  
**Run 004:** not authorized by this package

## Defect A — Adjudicator ordering (`PQR-ABSTAIN-03`)

**Observed (Run 003):** `ambiguous_diy_problem` evidence + hard-rule `reinforce_abstain`, but `SINGLE_ASSESSOR` assigned `FINAL REJECT` after early downgrade check (when outcome was not yet `FINAL REJECT`).

**Repair:** Refactor adjudication into ordered phases; export `applyMandatorySemanticInvariants()` applied **after** agreement, disagreement, and single-assessor branches. Invariant downgrades `REJECT`/`ACCEPT` → `ABSTAIN` when `ambiguous_diy_problem` unless direct commercial error override (`strong_commercial_problem`).

**Version:** `semantic-adjudicator.mjs` v1.4 → **v1.5**

## Defect B — Generic ERP over-rejection (`PC-ABSTAIN-01`)

**Observed:** Generic `erp` without platform identity triggered `product_version_update` → `REJECT`.

**Repair:** `platform-compatibility.mjs` v1.1 introduces `PLATFORM_CLASSIFICATION` (`EXPLICIT_COMPATIBLE`, `EXPLICIT_INCOMPATIBLE`, `GENERIC_PLATFORM_FAMILY`, `PLATFORM_UNKNOWN`). Hard-rules v1.2 adds `generic_platform_family_abstain_rule` before product-version reject reinforcement. Adjudicator invariant reinforces abstain for generic family + product update.

**Preserved:** SAP / Dynamics / Oracle explicit foreign platforms → `REJECT`.

## Unchanged authority

- `prompt-contract.mjs` — v1.4 (no change)
- `service-intent-evidence.mjs` — v1.1 (no change)

## Focused tests added/updated

- `run-sppc05-defect-repro.mjs` — adds `PC-ABSTAIN-01`, decision-path fields
- `run-platform-compatibility-regression.mjs` — 9 cases incl. generic ERP + 1C specialist update
- `run-under-admission-regression.mjs` — generic ERP unit cases
- `run-sppc05-variance-check.mjs` — `PC-ABSTAIN-01`, `PSR-AMB-01`
- `run-wave31f-bypass-audit.mjs` — v1.5 invariant + generic platform checks

## Known non-blocking ambiguity

`PSR-AMB-01` («купить 1с с настройкой»): expected ABSTAIN, stable ACCEPT×3 — pre-existing; not introduced by v2 repair.

## Corvonero boundary

Runs 002 and 003 frozen immutable. No Run 004 artefacts created.
