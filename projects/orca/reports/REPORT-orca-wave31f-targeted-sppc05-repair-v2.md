# REPORT — ORCA WAVE 3.1F TARGETED SPPC-05 REPAIR V2

**Task:** ORCA WAVE 3.1F TARGETED SPPC-05 REPAIR V2  
**Date:** 2026-06-26  
**Verdict:** `ORCA_WAVE_3_1F_TARGETED_SPPC05_REPAIR_V2 — PASS` / `READY_FOR_RUN_004_SPPC_05_ATTEMPT`

---

## 1. Safety and Scope

- Repair limited to ORCA Wave 3.1F semantic layer (adjudicator ordering + generic ERP platform policy) and focused tests/reports.
- Runs `corv-semantic-v2-20260626-002` and `003` evidence **not modified**.
- Run `004` **not created**.
- `projects/projects/` **not modified** (inventory reference only).
- No commit/push.

## 2. Git Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/canonical-post-recovery` ✓ |
| HEAD at task close | `0eb2f279` (advanced during session; recovery ancestor confirmed at task start) |
| Recovery ancestor `ebc65acd` | ✓ confirmed at preflight |
| Run 002 evidence | Present under `pilots/corvonero/runs/corv-semantic-v2-20260626-002/` |
| Run 003 evidence | Present under `pilots/corvonero/runs/corv-semantic-v2-20260626-003/` |
| Locks | RELEASED (both runs) |
| Full corpus | `0 / 2368` |
| Unrelated WIP | Not staged; fp-0002 workspace files show separate activity |

## 3. Run 002 and Run 003 Freeze

- Run 002 acceptance: `CORVONERO-RUN-002-SPPC-05-FAILURE-ACCEPTANCE-v1.*` (pre-existing).
- Run 003 acceptance **created:** `CORVONERO-RUN-003-SPPC-05-FAILURE-ACCEPTANCE-v1.md/json`.
- Both runs: `BLOCKED_AT_SPPC_05`, non-resumable, immutable evidence.

## 4. Defect Reproduction

Pre-repair (artefact `sppc05-defect-repro-1782467510540`, authority v1.4):

| Record | Expected | Final | Match |
|--------|----------|-------|-------|
| CFM-PROD-UPD-02 | REJECT | REJECT | ✓ |
| PQR-ABSTAIN-03 | ABSTAIN | REJECT | ✗ |
| PC-ABSTAIN-01 | ABSTAIN | REJECT | ✗ (platform regression) |

Post-repair (`sppc05-defect-repro-1782478143382`, openrouter / gpt-5-mini):

| Record | Expected | Final | Match |
|--------|----------|-------|-------|
| CFM-PROD-UPD-02 | REJECT | REJECT | ✓ |
| PQR-ABSTAIN-03 | ABSTAIN | ABSTAIN | ✓ |
| PC-ABSTAIN-01 | ABSTAIN | ABSTAIN | ✓ |

## 5. Adjudicator Ordering Root Cause

`ambiguous_diy_problem` downgrade (lines 69–74 in v1.4) ran while default outcome was `FINAL ABSTAIN`, **before** `SINGLE_ASSESSOR` set `FINAL REJECT`. Hard-rule emitted `reinforce_abstain` (deterministic assessor input ≠ model REJECT) but adjudicator never re-applied invariant.

## 6. Generic ERP Root Cause

Generic `erp` matched no specific platform → `platform_unspecified: true`, but `product_version_update` + `product_only` drove model/hard-rule `REJECT`. Missing `GENERIC_PLATFORM_FAMILY` classification allowed treating unspecified ERP like explicit foreign product maintenance.

## 7. Files Modified

| File | Version | SHA256 prefix | Rationale |
|------|---------|---------------|-----------|
| `semantic-adjudicator.mjs` | v1.4 → **v1.5** | `9618364947BA812C` | Post-branch `applyMandatorySemanticInvariants` |
| `platform-compatibility.mjs` | v1.0 → **v1.1** | `49B8C4D604EE732F` | Platform classification enum + generic ERP family |
| `hard-rules.mjs` | v1.1 → **v1.2** | `E6CD74CCCA6ED453` | `generic_platform_family_abstain_rule` |
| `prompt-contract.mjs` | v1.4 (unchanged) | `481075E55A827404` | Not required |
| `service-intent-evidence.mjs` | v1.1 (unchanged) | `5BFFF7AE2ED3B854` | Evidence already correct |

**Tests:** `run-sppc05-defect-repro.mjs`, `run-platform-compatibility-regression.mjs`, `run-under-admission-regression.mjs`, `run-sppc05-variance-check.mjs`, `run-wave31f-bypass-audit.mjs`

## 8. Adjudication Invariant

After all primary branches:

```text
if ambiguous_diy_problem confirmed
and no direct commercial override (strong_commercial_problem / provider+task)
then final verdict ∉ {REJECT, ACCEPT} → ABSTAIN
```

Recorded in `invariant_applications[]`. `PQR-ABSTAIN-03`: prior `FINAL REJECT` → `FINAL ABSTAIN` via `ambiguous_diy_problem_abstain`.

## 9. Platform Compatibility Policy

| Class | Example | 1C-only project outcome |
|-------|---------|-------------------------|
| EXPLICIT_COMPATIBLE | `1с`, `обновление 1с специалистом` | Normal service evaluation |
| EXPLICIT_INCOMPATIBLE | `sap business one`, `microsoft dynamics`, `oracle erp` | REJECT (foreign) |
| GENERIC_PLATFORM_FAMILY | `erp`, `erp система` | ABSTAIN |
| PLATFORM_UNKNOWN | no platform token | Existing product/service rules |

No `contains "erp" → REJECT` global rule. Approved platforms read from `businessScope` / registry.

## 10. Focused Regression Matrix

| Case | Expected | Post-repair |
|------|----------|-------------|
| `как исправить ошибку 0x80004005 1с` | ABSTAIN | ABSTAIN (PQR-ABSTAIN-03) |
| `обновление erp до новой версии` | ABSTAIN | ABSTAIN (PC-ABSTAIN-01) |
| `обновить erp систему` | ABSTAIN | ABSTAIN (PC-ABSTAIN-02) |
| `обновление sap business one до новой версии` | REJECT | REJECT |
| `обновление 1с специалистом` | ACCEPT | ACCEPT (PC-ACCEPT-03) |
| `инструкция как исправить ошибку 1с` | REJECT | (policy structural; not live-rerun) |
| `нужен специалист исправить ошибку 1с` | ACCEPT | (covered by PQR-ACCEPT-04 suite) |

Platform matrix live run: **9/9 PASS** (`platform-compatibility-regression-1782478501903`).

## 11. Problem Query Result

`problem-policy-regression-1782478317421`: **10/10 PASS**

## 12. Platform Compatibility Result

**9/9 PASS** (expanded matrix incl. `PC-ABSTAIN-02`, `PC-ACCEPT-03`).

## 13. Product Confirmation

`confirmation-sppc05-repair-v2-product-pass-pass-1782481444825`:

- Gold records: 106
- **FPR: 0.0** (gate ≤ 0.01) ✓
- False accepts: []

## 14. Under-Admission

**23/23 PASS** (includes generic ERP + ambiguous DIY unit cases).

## 15. Geo Confirmation

`confirmation-sppc05-repair-v2-geo-pass-pass-1782485788024`:

- Commercial recall: **1.0** (gate ≥ 0.90) ✓
- Adversarial FPR: **0** ✓
- `gate_pass`: true

## 16. Bypass Audit

**16/16 PASS** (v1.5 invariant + generic platform checks).

## 17. Closed Dataset Result

`closed-regression-1782485791111`: **exit 0**

- Product FPR: 0
- Boxed delivery: fixed
- `PSR-AMB-01`: ACCEPT vs expected ABSTAIN (pre-existing contrast; non-blocking)

## 18. Model Variance

`sppc05-variance-1782485788046` — 3 repetitions:

| Record | Distribution | Stable |
|--------|--------------|--------|
| CFM-PROD-UPD-02 | REJECT×3 | ✓ |
| PQR-ABSTAIN-03 | ABSTAIN×3 | ✓ |
| PC-ABSTAIN-01 | ABSTAIN×3 | ✓ |
| PSR-AMB-01 | ACCEPT×3 | known ambiguity |

`repair_cases_stable`: **true**

## 19. PSR-AMB-01 Status

«купить 1с с настройкой»: expected ABSTAIN, observed **ACCEPT×3** (stable). Pre-existing ambiguous minimal-pair; **non-blocking**; unchanged by v2 repair.

## 20. Full Regression Summary

| Suite | Status |
|-------|--------|
| SPPC-05 defect repro | 3/3 PASS |
| Problem query | 10/10 |
| Platform matrix | 9/9 |
| Under-admission | 23/23 |
| Bypass audit | 16/16 |
| Ambiguous problem policy (structural) | 8/8 |
| Product confirmation | PASS (FPR 0) |
| Geo confirmation v2 | PASS (recall 1.0) |
| Closed dataset | **exit 0** |
| Variance (repair cases) | stable |

## 21. Corvonero Boundary

- Runs 002/003 frozen; no checkpoint/receipt mutation.
- No Run 004 lock/checkpoint/STORAGE.
- Corpus **0 / 2368**.
- No canary.

## 22. Run 004 Eligibility

ORCA repair v2 **PASS** → operator may schedule `corv-semantic-v2-20260626-004` after review. **Not authorized in this task.**

## 23. Files Created or Changed

**Production:** `semantic-adjudicator.mjs`, `platform-compatibility.mjs`, `hard-rules.mjs`

**Tests:** `run-sppc05-defect-repro.mjs`, `run-platform-compatibility-regression.mjs`, `run-under-admission-regression.mjs`, `run-sppc05-variance-check.mjs`, `run-wave31f-bypass-audit.mjs`

**Reports/decisions:**

- `projects/orca/reports/REPORT-orca-wave31f-targeted-sppc05-repair-v2.md`
- `projects/orca/semantic-intelligence/ORCA-WAVE-3.1F-TARGETED-SPPC05-REPAIR-DECISIONS-v2.*`
- `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-RUN-003-SPPC-05-FAILURE-ACCEPTANCE-v1.*`
- `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-SPPC-05-ORCA-REPAIR-RESULT-v2.*`

**Live-model report dirs:** defect repro, variance, problem/platform regression, confirmation (product+geo), closed regression (timestamps above).

## 24. Git Status

ORCA repair files modified/untracked; **not staged**. Unrelated fp-0002 WIP present separately. No commit/push.

## 25. SAFE UNKNOWN

- **HEAD drift:** Task stated `48fbb38f`; closeout HEAD `0eb2f279` from unrelated fp-0002 commits during long test window — ORCA paths unaffected.
- **PSR-AMB-01** resolution strategy not defined — remains documented ambiguity.

## 26. Operator Decisions Required

1. Review ORCA Wave 3.1F targeted repair **v2** artefacts.
2. Confirm acceptance of Run 003 freeze document.
3. Authorize Run `corv-semantic-v2-20260626-004` if satisfied.
4. Resolve `projects/projects/` divergent duplicates (separate cleanup task).

## 27. Recommended Next Action

```text
OPERATOR REVIEW OF ORCA WAVE 3.1F TARGETED REPAIR V2
```

## 28. Stop Condition

All authorized repair steps completed:

- Failures reproduced (pre-repair artefacts cited)
- Adjudicator ordering fixed
- Generic ERP policy fixed
- Focused tests added/updated
- Required suites finished; closed dataset **exit 0**
- Bounded variance completed
- Repair verdict issued

Corvonero remains `BLOCKED_AT_SPPC_05` until operator authorizes Run 004.
