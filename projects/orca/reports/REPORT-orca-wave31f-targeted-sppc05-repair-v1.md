# REPORT — ORCA Wave 3.1F Targeted SPPC-05 Repair v1

**Task:** ORCA WAVE 3.1F TARGETED SPPC-05 REPAIR  
**Date:** 2026-06-26  
**Verdict:** `ORCA_WAVE_3_1F_TARGETED_REPAIR — PASS` / `READY_FOR_NEW_SPPC_05_ATTEMPT`

---

## 1. Safety and Scope

- Repair limited to ORCA Wave 3.1F semantic layer (prompt, evidence, hard-rules, adjudicator) + focused tests/reports.
- Run `corv-semantic-v2-20260626-002` evidence **not modified**.
- Run `003` **not created**.
- `projects/projects/` **not deleted** (inventory only).
- No commit/push.

## 2. Git Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/canonical-post-recovery` ✓ |
| HEAD | `f5a9ecd7` (ahead of stated anchor `ebc65acd` — fp-0002 commits; ORCA paths present) |
| Run 002 evidence | Present under canonical `projects/mars-search-ppc-production/pilots/corvonero/runs/corv-semantic-v2-20260626-002/` |
| Lock | `RELEASED` (STORAGE receipt verified) |
| Full corpus | Never started (`full_corpus_started: false`) |
| Unrelated WIP | Untouched (fp-0002, ocpilot backups remain separate) |

## 3. Failed Run 002 Freeze

Created `CORVONERO-RUN-002-SPPC-05-FAILURE-ACCEPTANCE-v1.md/json`. Confirmed:

- `run_id`: corv-semantic-v2-20260626-002  
- `status`: BLOCKED_AT_SPPC_05  
- `lock`: RELEASED  
- `full_corpus_calls`: 0  
- `canary_calls`: 0  

## 4. Defect Reproduction

Pre-repair failures confirmed from run 002 artefacts and local regression (PQR-ABSTAIN-03 9/10).

Post-repair live repro (`run-sppc05-defect-repro.mjs`, openrouter / gpt-5-mini):

| Record | Expected | Final | Match |
|--------|----------|-------|-------|
| CFM-PROD-UPD-02 | REJECT | REJECT | ✓ |
| PQR-ABSTAIN-03 | ABSTAIN | ABSTAIN | ✓ |

## 5. SAP Product Boundary Root Cause

- Missing `product_version_update` semantic class; «обновление … до новой версии» treated as potential service/commercial.
- Hard-rules lacked version-update enforcement (regex only in adjudicator disambiguation).
- Wave 3.1F prompt rules 17–19 encouraged commercial ACCEPT for foreign platforms when task-like wording appeared.

## 6. DIY Error ABSTAIN Root Cause

- `исправить` inside «как исправить» triggered `EXPLICIT_ERROR_RESOLUTION`, blocking abstain paths.
- Model classified as DIY → REJECT.
- Adjudicator `SINGLE_ASSESSOR` branch overwrote hard-rule ABSTAIN.

## 7. Files Modified

**Production:**

- `prompt-contract.mjs` (v1.3 → v1.4)
- `service-intent-evidence.mjs` (v1.0 → v1.1)
- `platform-compatibility.mjs` (new)
- `hard-rules.mjs` (v1.1)
- `semantic-adjudicator.mjs` (v1.3 → v1.4)

**Tests:** `run-under-admission-regression.mjs`, `run-wave31f-bypass-audit.mjs`, `run-confirmation-validation.mjs`, `run-problem-query-policy-regression.mjs`, plus new focused runners.

## 8. Policy Changes

- **Product version maintenance** without service scope → REJECT (protected product).
- **Ambiguous DIY-framed technical errors** → ABSTAIN (not REJECT).
- **Platform compatibility** compares detected platform to project-approved platforms (eval: 1C-only).
- Direct commercial error resolution (without «как …» framing) unchanged → ACCEPT when signals present.

## 9. Focused Regression Matrix

`run-platform-compatibility-regression.mjs`: **7/7 PASS** (1C service update accept, SAP/Dynamics/Oracle product update reject, self-update reject, generic ERP abstain, etc.)

## 10. Product Confirmation

`confirmation-sppc05-repair-product-pass-1782434048184`: **FPR 0.0** (gate ≤ 0.01), 106 gold records.

## 11. Problem Query Regression

`problem-policy-regression-1782433971781`: **10/10 PASS**

## 12. Under-Admission

**21/21 PASS** (includes new product-version and ambiguous-DIY unit tests)

## 13. Geo Confirmation

`confirmation-sppc05-repair-geo-pass-1782434729512`: **commercial recall 0.96** (gate ≥ 0.90), adversarial FPR 0.

## 14. Bypass Audit

**15/15 PASS** (12 original + 3 repair checks)

## 15. Model Variance

`run-sppc05-variance-check.mjs` — **3 repetitions** per case:

| Record | Distribution | Stable |
|--------|--------------|--------|
| CFM-PROD-UPD-02 | REJECT×3 | ✓ |
| PQR-ABSTAIN-03 | ABSTAIN×3 | ✓ |
| PQR-ACCEPT-03 | ACCEPT×3 | ✓ |
| PC-ACCEPT-02 | ACCEPT×3 | ✓ |

## 16. Full Regression Summary

| Suite | Status |
|-------|--------|
| SPPC-05 defect repro | PASS |
| Problem query | 10/10 |
| Platform matrix | 7/7 |
| Under-admission | 21/21 |
| Bypass audit | 15/15 |
| Ambiguous problem policy (structural) | 8/8 |
| Product confirmation | PASS (FPR 0) |
| Geo confirmation v2 | PASS (recall 0.96) |
| Closed dataset regression | **PASS** (exit 0, ~16 min) — product FPR 0, boxed delivery fixed; 1 contrast false-reject on PSR-AMB-01 (pre-existing ambiguous pair) |

## 17. Corvonero Boundary

Run 002 frozen. No checkpoint reopen. No lock recreate. No run 003 artefacts.

## 18. Run 003 Eligibility

ORCA repair **PASS** → operator may schedule new SPPC-05 with run ID `corv-semantic-v2-20260626-003` after review. **Not authorized in this task.**

## 19. `projects/projects/` Inventory

7 files: 1 EXACT_DUPLICATE, 6 DIVERGENT_DUPLICATE (Corvonero run 002 artefacts duplicated with hash drift). See `REPORT-projects-projects-duplicate-tree-inventory-v1.md`. **No cleanup performed.**

## 20. Files Created or Changed

See sections 7 and decision package `ORCA-WAVE-3.1F-TARGETED-SPPC05-REPAIR-DECISIONS-v1.*`, Corvonero acceptance/repair summaries, inventory report, live-model report artefacts under `projects/orca/semantic-intelligence/live-model/reports/`.

## 21. Git Status

ORCA repair files modified/untracked; no staging. Unrelated workspace WIP unchanged.

## 22. SAFE UNKNOWN

- **PSR-AMB-01** («купить 1с с настройкой»): expected ABSTAIN, got ACCEPT — pre-existing ambiguous minimal-pair behaviour; not introduced by SPPC-05 repair.
- **HEAD vs expected anchor** `ebc65acd`: branch correct; HEAD advanced by unrelated fp-0002 commits.

## 23. Operator Decisions Required

1. Review ORCA Wave 3.1F targeted repair artefacts.  
2. Confirm closed-dataset regression completion.  
3. Authorize new controlled run `corv-semantic-v2-20260626-003` if satisfied.  
4. Resolve `projects/projects/` divergent duplicates (separate cleanup task).

## 24. Recommended Next Action

`OPERATOR REVIEW OF ORCA WAVE 3.1F TARGETED REPAIR`

## 25. Stop Condition

All authorized repair steps completed. Corvonero remains blocked until operator approves new SPPC-05 attempt.
