# REPORT — MARS SEARCH PPC PRODUCTION — WAVE 3.1E FINAL QUALITY REPAIR V1

**Date:** 2026-06-23  
**Branch:** `mars/post-cycle8-live-tests`  
**Wave 3.1D checkpoint:** `21d1f0f`  
**Wave 3.1E:** uncommitted — operator review  
**Corvonero:** FROZEN

---

## 1. Preflight

| Check | Result |
|-------|--------|
| `2820b9f` in history | **CONFIRMED** |
| `7f7cb21` in history | **CONFIRMED** |
| `3d43c12` in history | **CONFIRMED** |
| Wave 3.1D package uncommitted at task start | **CONFIRMED** — checkpointed `21d1f0f` |
| Wave 4 started | **NO** |
| Corvonero FROZEN | **YES** — E2E 9/9 |
| Unrelated WIP staged | **NO** |

### Regression suites (all PASS at preflight)

| Suite | Result |
|-------|--------|
| Lifecycle synthetic matrix | 20/20 |
| Wave 1 bypass | 15/15 |
| Wave 1 lockdown | 12/12 |
| Corvonero E2E | 9/9 |
| Wave 2 bypass | 20/20 |
| Assisted capture | 12/12 |
| Wave 3 production matrix | 30/30 |
| Wave 3 bypass | 20/20 |
| Wave 3.1 bypass | 20/20 |
| Wave 3.1D bypass | 10/10 |
| Wave 3.1E bypass | 10/10 |
| Secret loader | 22/22 |
| Lifecycle validator | READY |
| Under-admission + product regression | 11/11 |
| Ambiguous problem policy (structural) | 8/8 |

---

## 2. Operator Decisions W3.1E-D1–D7

| ID | Decision |
|----|----------|
| W3.1E-D1 | **APPROVED — QUALITY REPAIR REQUIRED** |
| W3.1E-D2 | Gold support **SUFFICIENT** |
| W3.1E-D3 | Original datasets **CLOSED** — regression only |
| W3.1E-D4 | One systemic product/service repair **AUTHORIZED** |
| W3.1E-D5 | Geo repair confirm via new blind set |
| W3.1E-D6 | Final PASS requires both confirmation gates |
| W3.1E-D7 | Corvonero **FROZEN** |

Artifacts: `decisions/WAVE-3.1E-FINAL-QUALITY-REPAIR-DECISIONS-v1.md` (uncommitted)

---

## 3. Wave 3.1D Approval and Checkpoint

| Item | Status |
|------|--------|
| Commit | `21d1f0f` — `test(orca): evaluate supplementary semantic gold strata wave 3.1d` |
| Push | `mars/post-cycle8-live-tests` → origin |
| Scope | Supplementary authority, strata, policies, prompt v1.1, adjudicator v1.1, runners, sanitized supplementary results, decisions, report, roadmap |

---

## 4. Product/Service Error Analysis

**Error family:** `PRODUCT ACQUISITION MISCLASSIFIED AS SERVICE PROCUREMENT`

| Record | Phrase | Primary | Secondary | Final (pre-repair) | Decisive defect |
|--------|--------|---------|-----------|-------------------|-----------------|
| SUP-PROD-BOX-02 | 1с бухгалтерия коробочная поставка | ACCEPT | REJECT | ACCEPT | «поставка» treated as service fulfillment |
| SUP-PROD-BOX-04 | 1с erp коробочная поставка | ACCEPT | REJECT | ACCEPT | product topic + supply → false commercial evidence |

Analysis artifact: `supplementary/regression/product-service-error-analysis-v1.json`

---

## 5. Product/Service Policy

Machine-readable: `supplementary/policies/product-service-disambiguation-policy-v1.json`  
Human-readable: `supplementary/policies/PRODUCT-SERVICE-DISAMBIGUATION-POLICY-v1.md`

Mandatory rule: **PRODUCT OBJECT + PURCHASE/SUPPLY MODIFIER does not imply provider-hire intent**

---

## 6. Bounded Product Repair

One systemic iteration (uncommitted, v1.2):

| Component | Change |
|-----------|--------|
| `prompt-contract.mjs` | v1.2 rules 14–16 product/service disambiguation |
| `semantic-adjudicator.mjs` | v1.2 `resolveProductServiceDisagreement` before geo resolver |
| `hard-rules.mjs` | product acquisition without service scope blocks ACCEPT |
| Regression | `product-service-regression-v1.json` + under-admission tests 11/11 |

No phrase-specific record IDs or exception lists.

---

## 7. Closed-Dataset Regression

**Run ID:** `closed-regression-1782193176896`  
**Mode:** regression evidence only — not blind PASS  
**Cost:** $0.083

| Check | Result |
|-------|--------|
| SUP-PROD-BOX-02 fixed | **YES** → REJECT |
| SUP-PROD-BOX-04 fixed | **YES** → REJECT |
| Product FPR (supplementary re-run) | **0.034** (2 remaining: product_update family) |
| Contrast false REJECT | 1 |
| Informational false ACCEPT | 1 (`SUP-INFO-ERR-04`) |
| Minimal pairs | 7/8 match (PSR-AMB-01: ACCEPT vs ABSTAIN) |
| Holdout | **Not re-run** — commercial precision 1.0 reference preserved |

---

## 8. Product Confirmation Dataset

**Set:** PROTECTED PRODUCT BLIND CONFIRMATION SET V1  
**Records:** 106 (gold)  
**Checksum frozen:** `confirmation/strata/protected_product_confirmation/manifest-v1.json`  
**Lexical surface:** diverse products (Bitrix, SAP, AutoCAD, Office, SQL Server, etc.) — not 1С-only

---

## 9. Geo-Commercial Confirmation Dataset

**Set:** GEO COMMERCIAL BLIND CONFIRMATION SET V1  
**Records:** 100 (gold)  
**Families:** service+geo, provider noun+geo, price+geo, adversarial noncommercial strata  
**Authority:** `confirmation/authority/confirmation-blind-gold-authority-contract-v1.json`

---

## 10. Gold Authority and Blindness

| Control | Status |
|---------|--------|
| `confirmation_blind_validation: true` | **PASS** |
| Labels sealed separately | **PASS** |
| Assessor label access blocked | **PASS** |
| Post-run calibration forbidden | **PASS** |
| Freeze timestamps recorded | **PASS** |

---

## 11. Product Live Confirmation

**Run ID:** `confirmation-product-pass-1782194366760`  
**Provider:** OpenRouter / `openai/gpt-5-mini`  
**Cost:** $0.061

| Metric | Value | Gate |
|--------|-------|------|
| Total gold | 106 | — |
| False ACCEPT (protected negatives) | **0** | — |
| FPR | **0.0** | ≤ 0.01 **PASS** |
| Product-only ACCEPT on negatives | 0 | — |
| Contrast false REJECT | 2 | non-blocking |
| Gate | **PASS** | |

False REJECT examples: `CFM-PROD-SVC-04` (adobe photoshop), `CFM-PROD-SVC-05` (microsoft office) — consumer software «внедрение» edge cases.

---

## 12. Geo Live Confirmation

**Run ID:** `confirmation-geo-pass-1782195340879`  
**Cost:** $0.056

| Metric | Value | Gate |
|--------|-------|------|
| Commercial recall | **0.619** | ≥ 0.85 **FAIL** |
| Commercial false REJECT | **16** | — |
| Adversarial false ACCEPT rate | **0.0** | ≤ 0.01 **PASS** |
| High-confidence geo-commercial precision | **1.0** | ≥ 0.95 **PASS** |
| Geography-alone ACCEPT | **0** | **PASS** |
| Gate | **FAIL** | |

Primary failure pattern: `программист bitrix <город>` and `цена настройки sap <город>` false REJECTs — geo-commercial under-admission on non-1С service nouns.

---

## 13. Ambiguous Problem Policy Validation

**Run:** `problem-policy-regression-1782194369962`  
**Result:** **6/7 PASS**

| Case | Expected | Got |
|------|----------|-----|
| PQR-ABSTAIN-02 (ошибка 0x80004005 1с) | ABSTAIN | REJECT **FAIL** |

Urgent specialist, DIY, informational, service-object problem cases pass.

---

## 14. Cross-Regression

Post-repair deterministic suites: synthetic 20/20, Wave 3 matrix 30/30, Wave 3.1 bypass 20/20, Wave 3.1D 10/10, Wave 3.1E 10/10. **No critical bypass regression.**

Closed supplementary re-run shows minor informational drift (`SUP-INFO-ERR-04`) — not used as new blind PASS.

---

## 15. Combined D3 Decision

| Input | Result |
|-------|--------|
| Original holdout commercial precision | 1.0 (closed, not re-run) |
| Supplementary informational (original blind) | PASS preserved (FPR 0.0 at 3.1D) |
| New product confirmation | **PASS** FPR 0.0 |
| New geo-commercial confirmation | **FAIL** recall 0.619 |
| Problem-query validation | **6/7** |
| Cross-regression bypass | PASS |
| Bounded human review | preserved |

**Combined verdict:** `WAVE 3.1 — QUALITY REPAIR REQUIRED`

Not: `LIVE MODEL VALIDATED — D3 QUALITY EVIDENCE COMPLETE`

**Blocker:** geo-commercial confirmation gate — commercial under-admission on provider-noun + geography and price + geography patterns outside original 1С holdout repair scope.

---

## 16. Operator Review Package

`live-model/reports/wave-3.1e-operator-review-package-v1.json` — bounded sample (not full sets).

---

## 17. Bypass Audit

| # | Check | Result |
|---|-------|--------|
| 1 | Old supplementary set as blind proof | PASS — not claimed |
| 2 | Confirmation set used for calibration | PASS — forbidden post-run |
| 3 | Expected label leakage | PASS |
| 4 | Boxed delivery by topic match | PASS — repaired |
| 5 | Implementation rejected as product-only | PASS — contrast positives mostly pass |
| 6 | Geography alone forces ACCEPT | PASS — 0 adversarial FA |
| 7 | Career + geography accepted | PASS |
| 8 | Education + geography accepted | PASS |
| 9 | Product + geography as service | PASS |
| 10 | Phrase-specific exception | PASS — none |
| 11 | Confirmation copied from prior sets | PASS — new IDs/surface |
| 12 | Insufficient sample reported PASS | PASS — 106/100 records |
| 13 | Secret leak | PASS |
| 14 | Cost cap bypass | PASS |
| 15 | Deterministic fallback promoted | PASS |
| 16 | Human review becomes primary | PASS |
| 17 | Original holdout modified | PASS |
| 18 | Corvonero classified | PASS — not run |
| 19 | Wave 4 started | PASS |
| 20 | Output reconciliation failure | PASS |

---

## 18. Actual Cost

| Run | USD |
|-----|-----|
| Closed-dataset regression | 0.083 |
| Product confirmation | 0.061 |
| Geo confirmation | 0.056 |
| Problem policy (7 records) | ~0.005 |
| **Total Wave 3.1E live** | **~$0.205** |

---

## 19. Wave 3 Final Status

```text
Wave 3.1 — QUALITY REPAIR REQUIRED
Wave 3 Overall — NOT OPERATIONAL
Wave 4 — BLOCKED
Corvonero — FROZEN
```

Product/service repair **validated on new blind product confirmation**. Geo-commercial repair **not validated** on new blind geo set.

---

## 20. Wave 4 Readiness

**BLOCKED** — D3 quality evidence incomplete (geo confirmation FAIL).

---

## 21. Corvonero Boundary

**FROZEN** — no semantic core, no production classification, no campaign work.

---

## 22. Files Changed

### Checkpointed (Wave 3.1D — `21d1f0f`)

33 files — supplementary package, prompt v1.1, adjudicator v1.1, runners, report.

### Uncommitted (Wave 3.1E)

| Path | Role |
|------|------|
| `decisions/WAVE-3.1E-FINAL-QUALITY-REPAIR-DECISIONS-v1.*` | Operator decisions |
| `contracts/prompt-contract.mjs` | v1.2 product rules |
| `adjudication/semantic-adjudicator.mjs` | v1.2 product resolver |
| `production/assessors/hard-rules.mjs` | product acquisition hard rule |
| `supplementary/policies/product-service-*` | Policy |
| `supplementary/regression/product-service-*` | Analysis + regression |
| `confirmation/**` | Blind confirmation sets + authority |
| `tests/run-confirmation-validation.mjs` | Live confirmation runner |
| `tests/run-closed-dataset-regression.mjs` | Closed regression |
| `tests/run-problem-query-policy-regression.mjs` | Problem policy live |
| `tests/run-wave31e-bypass-audit.mjs` | Bypass audit |
| `tests/run-under-admission-regression.mjs` | Extended unit tests |
| `reports/closed-regression-*` | Regression evidence |
| `reports/confirmation-product-pass-*` | Product live results |
| `reports/confirmation-geo-pass-*` | Geo live results |
| `reports/problem-policy-regression-*` | Problem policy |
| `reports/wave-3.1e-operator-review-package-v1.json` | Operator package |
| `reports/REPORT-mars-search-ppc-wave3-1e-final-quality-repair-v1.md` | This report |

---

## 23. Git Status

- **HEAD (3.1D):** `21d1f0f` pushed  
- **Wave 3.1E:** local uncommitted per operator review instruction  
- **Secrets / raw provider payloads:** not committed

---

## 24. SAFE UNKNOWN

- Effect of v1.2 product repair on **closed holdout** geo false-rejects — not re-evaluated (holdout closed).
- Whether geo false REJECTs on Bitrix/SAP phrases share the same root cause as 1С holdout under-admission — hypothesized but not isolated in this task (no third repair iteration authorized).
- Long-run cost at full corpus scale — extrapolated from confirmation runs only.

---

## 25. Operator Approval Items

1. Accept **product confirmation PASS** (FPR 0.0) as sufficient product/service repair evidence?
2. Authorize **follow-up geo-commercial repair** (second wave) or expand service registry scope for Bitrix/SAP geo patterns?
3. Review **2 service contrast false REJECTs** on consumer software (Photoshop/Office «внедрение»).
4. Review **PQR-ABSTAIN-02** error-code query over-rejection.
5. Approve or reject **Wave 3.1E commit** after review.

---

## 26. Recommended Next Action

**OPERATOR REVIEW OF WAVE 3.1E FINAL D3 QUALITY RESULTS**

If geo repair is chartered: bounded geo-commercial v1.3 iteration on **new** confirmation holdout (current geo set closed post-run) — not a third product repair.

---

## 27. Stop Condition

Stopped after: 3.1D checkpoint, product error analysis, one bounded product repair, closed regression, confirmation sets, live runs (product + geo), problem validation, cross-regression, combined D3 decision, operator package, bypass audit.

**Not performed:** second repair iteration, holdout re-run, Wave 4, Corvonero, Semantic Core, 3.1E commit.
