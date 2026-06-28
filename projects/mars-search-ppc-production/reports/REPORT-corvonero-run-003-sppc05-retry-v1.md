# REPORT — CORVONERO RUN 003 SPPC-05 RETRY V1

**Task:** CORVONERO NEW CONTROLLED SEMANTIC RUN 003 — SPPC-05 RETRY  
**Date:** 2026-06-26  
**Run ID:** `corv-semantic-v2-20260626-003`

---

## 1. Safety and Authorization

Authorized scope: Phase 0 authority verification, Phase 1 run registration, Phase 2 SPPC-05 validation retry only.

| Decision | Status |
|----------|--------|
| ORCA repair | APPROVED |
| Run 002 | BLOCKED_AT_SPPC_05 — NON-RESUMABLE |
| Run 003 | AUTHORIZED SPPC-05 RETRY ONLY |
| Provider / model | openrouter / openai/gpt-5-mini |
| Hard cost cap | $3.00 |
| Old forensic cache / lock | PROHIBITED |
| Missing TS PIOT SERP | NON-BLOCKING |
| PSR-AMB-01 | KNOWN AMBIGUITY — NON-BLOCKING |
| Phase 3 / Wave 5 | NOT AUTHORIZED |

No ORCA brain edits during this task. No commit/push.

## 2. Git Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/canonical-post-recovery` ✓ |
| HEAD | `48fbb38ff3050e79269f2ded90e21c271ecaf21a` |
| Recovery ancestor `ebc65acd` | ✓ (exit 0) |
| Run 002 evidence | Immutable — untouched |
| Run 003 pre-existence | Absent at start ✓ |
| FP-0002 WIP | Untouched (separate workspace changes only) |

## 3. ORCA Repair Authority

**Verdict:** `APPROVED ORCA REPAIR AUTHORITY — FROZEN` (no drift)

| Component | Version |
|-----------|---------|
| prompt-contract.mjs | orca-semantic-assessment-prompt-v1.4 |
| service-intent-evidence.mjs | v1.1 |
| platform-compatibility.mjs | v1.0 |
| hard-rules.mjs | v1.1 |
| semantic-adjudicator.mjs | v1.4 |

Semantic classes verified: `product_version_update`, `ambiguous_diy_problem`; platform compatibility via `evaluatePlatformCompatibility`.

Snapshot: `runs/corv-semantic-v2-20260626-003/repair-authority-freeze-v1.json`  
STORAGE: `manifests/repair-authority-freeze-v1.json`

## 4. Run 002 Boundary

- `corv-semantic-v2-20260626-002` — BLOCKED_AT_SPPC_05, lock RELEASED  
- Not reopened, not resumed, receipts unchanged  
- Failure acceptance: `CORVONERO-RUN-002-SPPC-05-FAILURE-ACCEPTANCE-v1.json`

## 5. Run 003 Identity

- **Run ID:** `corv-semantic-v2-20260626-003`  
- **Project:** PRJ-0013  
- **MIG session:** `session-mig-20260622-corv01`  
- **Initial lifecycle:** `REGISTERED_FOR_SPPC_05_RETRY`  
- **Final lifecycle:** `BLOCKED_AT_SPPC_05`

## 6. STORAGE Root

`C:\MARS Phenix\AI MARS STORAGE\mig\corvonero\semantic-runs\corv-semantic-v2-20260626-003\`

Structure created: manifests, runtime, checkpoints, locks, batches, cache, raw-responses, receipts, reports, quarantine.

No copy from runs 001/002. No forensic cache.

## 7. Immutable Input Verification

| Check | Result |
|-------|--------|
| Record count | 2368 ✓ |
| Duplicate IDs | 0 ✓ |
| Missing IDs | 0 ✓ |
| SHA-256 prefix | `eaa09b8450f82738` ✓ |
| Lineage | 2399 → 31 clusters → 2368 ✓ |

Corpus not processed (processed = 0).

## 8. Old Run Isolation

**OLD_RUN_ISOLATION — PASS**

No forbidden run ID references, no old cache/checkpoint reuse in Run 003 root.

## 9. Model and Provider

| Item | Value |
|------|-------|
| Provider | openrouter |
| Model | openai/gpt-5-mini |
| Secret | SET (not printed) |
| Fallback | None |

## 10. Cost Projection

Pre-run projection: ~980 calls, ~$0.85 estimated, within $3.00 hard cap.

## 11. Lock Authority

- Atomic lock acquired: `locks/run.lock.json`  
- Owner: `execute-run-003-sppc05-retry-v1.mjs`  
- Status: **RELEASED** with failure outcome  
- Receipt: `receipts/lock-release-receipt-v1.json`

## 12. Checkpoint Authority

Initial: phase `SPPC-05_VALIDATION`, processed `0`, total `2368`, complete `false`.

Final: phase `BLOCKED_AT_SPPC_05`, processed `0`, gate_b `FAILED`.

## 13. Closed Dataset Inventory

| Suite | Fixtures |
|-------|----------|
| Product confirmation | 106 |
| Geo confirmation v2 | 120 |
| Closed supplementary | 136 |
| Problem query | 10 |
| Wave 3.1F bypass | 15 |
| Under-admission | 21 |
| Platform compatibility | 7 |
| Variance (repair focus) | CFM-PROD-UPD-02, PQR-ABSTAIN-03, + controls |

Explicit fixtures: CFM-PROD-UPD-02, PQR-ABSTAIN-03, PSR-AMB-01 (documented).

## 14. SPPC-05 Criteria

| Gate | Required | Run 003 |
|------|----------|---------|
| Product FPR ≤ 0.01 | ✓ | **PASS** (0.0) |
| Geo recall ≥ 0.90 | ✓ | **PASS** (1.0) |
| Geo adversarial FPR = 0 | ✓ | **PASS** |
| Problem query 10/10 | ✓ | **PASS** |
| Under-admission | full | **PASS** |
| Bypass audit | full | **PASS** |
| Platform compatibility | full | **FAIL** (6/7) |
| Repair fixtures stable | ✓ | **FAIL** |
| Closed dataset | pass | **NOT EXECUTED** |

## 15. SPPC-05 Execution

Provider live calls executed for platform, defect repro, problem query, product/geo confirmation, variance. Closed dataset not reached after critical failures.

**Gate B:** `FAILED`

## 16. Product Confirmation

Run artefact: `confirmation-product-pass-1782467771260`

- False positive rate: **0.0**  
- Gate pass: **true**  
- CFM-PROD-UPD-02: not in false_accepts

## 17. Platform Compatibility

Run artefact: `platform-compatibility-regression-1782467386966`

- Score: **6/7**  
- Failure: **PC-ABSTAIN-01** — «обновление erp до новой версии» expected ABSTAIN, got REJECT (`product_version_update` signal, platform unspecified)

## 18. Problem Query Regression

Run artefact: `problem-policy-regression-1782467593637`

- Score: **10/10** including PQR-ABSTAIN-03 → ABSTAIN in batch run  
- Note: defect-repro and variance runs on same fixture still show REJECT when model returns REJECT primary

## 19. Under-Admission

**21/21 PASS** (unit tests, no live model)

## 20. Geo Confirmation

Run artefact: `confirmation-geo-pass-1782471125933`

- Commercial recall: **1.0** (gate ≥ 0.90)  
- Adversarial FPR: **0**  
- Gate pass: **true**

## 21. Bypass Audit

**15/15 PASS** — includes repair checks (platform layer, product_version_update_hard_rule, ambiguous_diy_problem_abstain_rule)

## 22. Closed Dataset Result

**NOT EXECUTED** in Run 003. Repair-run reference only (not Run 003 evidence): `closed-regression-1782434738344` documented PSR-AMB-01 contrast false-reject under ORCA v1.4 repair.

## 23. Variance Check

Run artefact: `sppc05-variance-1782466708542` — 3 repetitions

| Record | Distribution | Stable |
|--------|--------------|--------|
| CFM-PROD-UPD-02 | REJECT×3 | ✓ |
| PQR-ABSTAIN-03 | REJECT×3 | ✗ |
| PQR-ACCEPT-03 | ACCEPT×3 | ✓ |
| PC-ACCEPT-02 | ACCEPT×3 | ✓ |

`repair_cases_stable`: **false**

## 24. PSR-AMB-01 Status

- Expected: ABSTAIN  
- Historically observed: ACCEPT  
- Run 003: not re-run in variance suite; known pre-existing ambiguity  
- **Non-blocking** — isolated; no product FPR breach  
- Must remain in operator review

## 25. Cost and Runtime

| Item | Value |
|------|-------|
| Cumulative cost | ~**$0.62** USD |
| Hard cap | $3.00 — not exceeded |
| Soft warning | $2.00 — not exceeded |
| Full corpus calls | 0 |
| Canary calls | 0 |

## 26. Gate B Verdict

```text
SPPC-05: FAILED
Run 003: BLOCKED_AT_SPPC_05
```

## 27. Project Lifecycle

```text
BLOCKED_AT_SPPC_05
```

Not `FROZEN_PENDING_CANARY_AUTHORIZATION`. Phase 3 blocked.

## 28. Runtime Cleanup

- Lock released with failure receipt  
- Checkpoint preserved  
- No canary, no corpus batch, no Wave 5

## 29. Outputs Created

**Git (sanitized):**

- `pilots/corvonero/CORVONERO-RUN-003-SPPC-05-RESULT-v1.md/json`
- `pilots/corvonero/CORVONERO-RUN-003-SPPC-05-REVIEW-PACKAGE-v1.md/json`
- `pilots/corvonero/CORVONERO-RUN-003-PHASE-3-NEXT-TASK-v1.md`
- `pilots/corvonero/runs/corv-semantic-v2-20260626-003/` (manifest, repair freeze, receipt, report)
- `reports/REPORT-corvonero-run-003-sppc05-retry-v1.md`

**STORAGE (mutable):** locks, checkpoints, receipts, execution reports

**Tools added:** `execute-run-003-sppc05-retry-v1.mjs`, `finalize-run-003-sppc05-retry-v1.mjs`, `compile-run-003-report-v1.mjs`

## 30. Git and STORAGE Placement

- Git run authority: `projects/mars-search-ppc-production/pilots/corvonero/runs/corv-semantic-v2-20260626-003/`  
- STORAGE root: `C:\MARS Phenix\AI MARS STORAGE\mig\corvonero\semantic-runs\corv-semantic-v2-20260626-003\`  
- `projects/projects/` — not modified (inventory reference only)

## 31. Tests

| Suite | Result |
|-------|--------|
| wave31f_bypass | PASS |
| under_admission | PASS |
| platform_compatibility | FAIL |
| focused_repair_repro | FAIL |
| problem_query_policy | PASS |
| confirmation_product | PASS |
| confirmation_geo_v2 | PASS |
| closed_dataset_regression | NOT RUN |
| variance_check | FAIL (repair cases) |

## 32. Files Changed

**Created (Corvonero Run 003):**

- `projects/mars-search-ppc-production/pilots/corvonero/tools/execute-run-003-sppc05-retry-v1.mjs`
- `projects/mars-search-ppc-production/pilots/corvonero/tools/finalize-run-003-sppc05-retry-v1.mjs`
- `projects/mars-search-ppc-production/pilots/corvonero/tools/compile-run-003-report-v1.mjs`
- `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-RUN-003-*`
- `projects/mars-search-ppc-production/pilots/corvonero/runs/corv-semantic-v2-20260626-003/*`
- `projects/mars-search-ppc-production/reports/REPORT-corvonero-run-003-sppc05-retry-v1.md`

**STORAGE:** full Run 003 tree under semantic-runs.

**Not modified:** ORCA brain (read-only verification), Run 002 evidence, `projects/projects/`.

## 33. Git Status

Branch `mars/canonical-post-recovery`. Run 003 pilot files untracked/uncommitted for operator review. Pre-existing ORCA repair and FP-0002 WIP unchanged by this task scope.

## 34. SAFE UNKNOWN

- Exact OpenRouter billing total vs calculated token estimate — reconcile against provider dashboard if needed  
- Closed dataset outcome under Run 003 live provider — **not executed**; repair-run closed regression is ORCA-only reference, not Run 003 gate evidence  
- Whether problem-query 10/10 and variance REJECT×3 on PQR-ABSTAIN-03 reflect model sampling only vs deterministic adjudicator ordering — code review indicates ordering issue when primary=REJECT on SINGLE_ASSESSOR path

## 35. Operator Decisions Required

1. Accept Run 003 **FAILED** / **BLOCKED_AT_SPPC_05** as immutable evidence  
2. Decide adjudicator fix for `ambiguous_diy_problem` downgrade after SINGLE_ASSESSOR branch (new ORCA repair — **not** in this task)  
3. Decide PC-ABSTAIN-01 generic ERP abstain policy  
4. Whether to authorize new SPPC-05 attempt (new run ID) after repair  
5. PSR-AMB-01 — acknowledge known ambiguity; no policy change in this task

## 36. Exact Phase 3 Task

**Blocked.** See `CORVONERO-RUN-003-PHASE-3-NEXT-TASK-v1.md`.

Prerequisite not met:

```text
SPPC-05: PASS — OPERATOR REVIEW REQUIRED
```

## 37. Stop Condition

**Stopped after SPPC-05 result.**

Not started: canary, full 2368 corpus, semantic production, assembly, strategy, Campaign Architecture, Commander, import, launch, Wave 5.

**Next gate:** `OPERATOR REVIEW OF CORVONERO RUN 003 SPPC-05 RESULT`
