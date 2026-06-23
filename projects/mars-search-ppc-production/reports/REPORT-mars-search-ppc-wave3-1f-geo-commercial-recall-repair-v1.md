# REPORT — MARS SEARCH PPC PRODUCTION — WAVE 3.1F GEO-COMMERCIAL RECALL REPAIR V1

**Date:** 2026-06-23  
**Branch:** `mars/post-cycle8-live-tests`  
**Wave 3.1E checkpoint:** `fba8a97`  
**Wave 3.1F:** uncommitted — operator review  
**Corvonero:** FROZEN

---

## 1. Preflight

| Check | Result |
|-------|--------|
| `2820b9f` in history | **CONFIRMED** |
| `7f7cb21` in history | **CONFIRMED** |
| `3d43c12` in history | **CONFIRMED** |
| `21d1f0f` in history | **CONFIRMED** |
| Wave 3.1E uncommitted at task start | **CONFIRMED** — checkpointed `fba8a97` |
| Wave 4 started | **NO** |
| Corvonero FROZEN | **YES** |
| Unrelated WIP staged | **NO** |

### Regression suites (preflight)

| Suite | Result |
|-------|--------|
| Lifecycle synthetic matrix | 20/20 |
| Wave 3.1E bypass (pre-repair) | 9/10 — prompt v1.3 supersedes v1.2 check |
| Wave 3.1F bypass | **12/12** |
| Under-admission + product regression | **16/16** |
| Geo false-reject closed regression | **16/16** |

---

## 2. Operator Decisions W3.1F-D1–D7

| ID | Decision |
|----|----------|
| W3.1F-D1 | **APPROVED — QUALITY EVIDENCE ACCEPTED** (Wave 3.1E) |
| W3.1F-D2 | **VALIDATED — PROTECTED PRODUCT PASS** |
| W3.1F-D3 | Geo FPR 0.0 PASS; commercial recall 0.619 — **REPAIR AUTHORIZED** |
| W3.1F-D4 | One systemic geo-commercial repair — **EXECUTED** |
| W3.1F-D5 | Commercial intent / scope fit / ownership — **SEPARATED** |
| W3.1F-D6 | PQR-ABSTAIN-02 → **ABSTAIN** (fixed) |
| W3.1F-D7 | Corvonero **FROZEN** |

Artifacts: `decisions/WAVE-3.1F-GEO-COMMERCIAL-REPAIR-DECISIONS-v1.md`

---

## 3. Wave 3.1E Approval and Checkpoint

| Item | Status |
|------|--------|
| Commit | `fba8a97` — `test(orca): validate product disambiguation and geo quality wave 3.1e` |
| Push | `mars/post-cycle8-live-tests` → origin |
| Scope | Product/service policy v1.2, confirmation sets V1, runners, live results, decisions, report |

---

## 4. Geo False-Reject Forensics

**Source:** V1 run `confirmation-geo-pass-1782195340879`  
**Total false REJECT:** 16

| Family | Count | Decisive failure |
|--------|-------|------------------|
| Provider noun + geo (Bitrix) | 4 | reject_wins_on_disagreement; scope confusion |
| Price + service + geo (SAP) | 12 | assessor_agreement REJECT — out-of-scope → noncommercial |

Analysis: `supplementary/regression/geo-commercial-error-analysis-v1.json`

**Closed regression after repair:** **16/16 fixed** (structured evidence + scope-fit separation)

---

## 5. Commercial Intent vs Scope Fit

Contract: `contracts/commercial-scope-fit-contract-v1.json`

| Question | Field | Example outcome |
|----------|-------|-----------------|
| A. Commercial intent | `commercial_eligibility.decision` | ACCEPT |
| B. Scope fit | `scope_fit` | OUT_OF_SCOPE |
| C. Ownership | `ownership` | SERVICE_GAP |

Forbidden inference removed: registry absence no longer forces commercial REJECT.

---

## 6. Service-Noun Generalization

Layer: `evidence/service-intent-evidence.mjs` v1.0

Signal categories: provider professions, implementation tasks, procurement modifiers, urgent problem resolution, geography modifiers, product+service composition.

Extensible taxonomy — not 1С-only closed dictionary.

---

## 7. Product and Service Composition

Prompt v1.3 rules 14–19 preserved and extended. Product acquisition hard rule exempts price+service and product+explicit-service patterns.

Boxed-delivery regression: **PASS** (under-admission 16/16).

---

## 8. Geo Evidence Policy V2

`supplementary/policies/geo-evidence-policy-v2.json` + `GEO-EVIDENCE-POLICY-V2.md`

Mandatory: geography strengthens commercial evidence, never creates it alone.

---

## 9. Problem-Query Repair

Hard rule: bare error → ABSTAIN override. Adjudicator: `strong_commercial_problem` for explicit paid error resolution.

| Case | Expected | Result |
|------|----------|--------|
| PQR-ABSTAIN-02 | ABSTAIN | **ABSTAIN** |
| PQR-ABSTAIN-03 | ABSTAIN | **ABSTAIN** |
| PQR-ACCEPT-03 | ACCEPT | **ACCEPT** |
| PQR-ACCEPT-04 | ACCEPT | **ACCEPT** |

**Problem policy live:** **10/10 PASS**

---

## 10. Bounded Geo Repair

One iteration (v1.3):

| Component | Change |
|-----------|--------|
| `prompt-contract.mjs` | v1.3 rules 17–22; scope_fit output |
| `semantic-adjudicator.mjs` | v1.3 structured evidence; scope-fit separation |
| `hard-rules.mjs` | bare error ABSTAIN; price+service exempt |
| `service-intent-evidence.mjs` | new universal evidence layer |
| `geo-evidence-policy-v2` | machine-readable policy |

No phrase-specific or brand-specific exceptions.

---

## 11. Closed-Dataset Regression

| Check | Result |
|-------|--------|
| 16 V1 geo false REJECT fixed | **16/16** |
| New false ACCEPT (closed) | **0** |
| Boxed-delivery PASS | **YES** |
| PQR-ABSTAIN-02 | **ABSTAIN** |
| Review ratio (geo V2 live) | **0.017** |

---

## 12. Geo Confirmation Dataset V2

**Set:** GEO COMMERCIAL BLIND CONFIRMATION SET V2  
**Records:** 120  
**Stratum:** `geo_commercial_confirmation_v2`  
**Builder:** `confirmation/build-confirmation-geo-v2-strata.mjs`

Strata: provider+geo, task+geo, price+geo, product+service+geo, urgent+geo, out-of-scope commercial, service noun+geo, career/education/product/navigation/informational/ambiguous adversarial.

No V1 false-reject phrases copied.

---

## 13. Gold Authority and Blindness

| Control | Status |
|---------|--------|
| `confirmation_blind_validation: true` | **PASS** |
| `commercial_intent_label_separate_from_scope_fit: true` | **PASS** |
| Post-run calibration forbidden | **PASS** |
| Freeze timestamp recorded | **PASS** |

---

## 14. Live Geo V2 Execution

**Run ID:** `confirmation-geo-v2-pass-1782223272398`  
**Provider:** OpenRouter / `openai/gpt-5-mini`  
**Cost:** $0.080

Pipeline: blind A → independent B → hard evidence → adjudication → metrics.

---

## 15. Commercial Admission Metrics

| Metric | Value | Gate |
|--------|-------|------|
| Commercial recall | **0.960** | ≥ 0.90 **PASS** |
| Commercial false REJECT | 4 | — |
| High-confidence geo precision | **1.0** | ≥ 0.95 **PASS** |
| Adversarial false ACCEPT rate | **0.0** | ≤ 0.01 **PASS** |
| Provider-noun recall | 0.969 | — |
| Service-task recall | 0.952 | — |
| Product+service recall | 0.833 | — |
| Gate | **PASS** | |

---

## 16. Scope-Fit Metrics

| Metric | Value |
|--------|-------|
| Out-of-scope commercial-intent recall | **0.982** |
| Scope-fit accuracy (labeled subset) | **0.857** |
| In-scope commercial recall | N/A (eval registry is 1C-only) |

Out-of-scope commercial queries correctly ACCEPT at admission with `scope_fit: OUT_OF_SCOPE`.

---

## 17. Problem-Policy Validation

**Run:** `problem-policy-regression-1782223046785` (latest)  
**Result:** **10/10 PASS**

---

## 18. Cross-Regression

| Check | Result |
|-------|--------|
| Product FPR (3.1E closed) | **0.0** preserved |
| Boxed-delivery | **PASS** |
| Synthetic matrix | 20/20 |
| Wave 3.1F bypass | 12/12 |
| Holdout checksum | unchanged |
| No new critical error family | **YES** |

---

## 19. Combined D3 Closure

| Input | Result |
|-------|--------|
| Original holdout | closed — precision 1.0 reference preserved |
| Supplementary informational | PASS preserved |
| Product confirmation (3.1E) | PASS FPR 0.0 |
| Geo V2 | **PASS** recall 0.96 |
| Problem policy | **10/10** |
| Cross-regression | PASS |
| Bypass audit (3.1F) | 12/12 |

**Combined verdict:** `LIVE MODEL VALIDATED — D3 QUALITY EVIDENCE COMPLETE`

---

## 20. Operator Review Package

`live-model/reports/wave-3.1f-operator-review-package-v1.json`

4 remaining V2 commercial false REJECTs (borderline provider/product+service+geo) — gate still passes.

---

## 21. Bypass Audit

| # | Check | Result |
|---|-------|--------|
| 1 | Commercial intent ≠ scope fit | PASS |
| 2 | Out-of-scope not forced noncommercial | PASS |
| 3 | Geography alone no ACCEPT | PASS (0 adversarial FA) |
| 4 | Product+geo without service | PASS |
| 5–6 | Career/education+geo | PASS |
| 7 | Product repair regressed | PASS |
| 8–9 | Brand/phrase exceptions | PASS — none |
| 10 | V1 copied to V2 | PASS |
| 11 | V2 calibration | PASS — forbidden |
| 12 | Label leakage | PASS |
| 13 | Insufficient sample | PASS — 120 records |
| 14 | Bare error forced REJECT | PASS — ABSTAIN |
| 15 | Deterministic fallback promoted | PASS |
| 16 | Secret leak | PASS |
| 17 | Cost cap bypass | PASS |
| 18 | Corvonero classified | PASS |
| 19 | Wave 4 started | PASS |
| 20 | Output reconciliation | PASS |

---

## 22. Actual Cost

| Run | USD |
|-----|-----|
| Problem policy (10 cases) | ~0.008 |
| Geo V2 confirmation (120) | 0.080 |
| **Total Wave 3.1F live** | **~$0.088** |

---

## 23. Wave 3 Final Status

```text
Wave 3.1 — LIVE MODEL VALIDATED — OPERATOR REVIEW REQUIRED
Wave 3 Overall — READY FOR SEMANTIC QUALITY APPROVAL
Wave 4 — BLOCKED UNTIL OPERATOR APPROVAL
Corvonero — FROZEN
```

---

## 24. Wave 4 Readiness

**BLOCKED UNTIL OPERATOR APPROVAL** of Wave 3.1F geo quality results.

---

## 25. Corvonero Boundary

**FROZEN** — no classification, Semantic Core, or campaign work.

---

## 26. Files Changed

### Checkpointed (Wave 3.1E — `fba8a97`)

39 files — product repair, confirmation V1, runners, reports.

### Uncommitted (Wave 3.1F)

| Path | Role |
|------|------|
| `decisions/WAVE-3.1F-GEO-COMMERCIAL-REPAIR-DECISIONS-v1.*` | Operator decisions |
| `evidence/service-intent-evidence.mjs` | Universal evidence layer |
| `contracts/commercial-scope-fit-contract-v1.json` | Intent/scope separation |
| `contracts/prompt-contract.mjs` | v1.3 |
| `adjudication/semantic-adjudicator.mjs` | v1.3 |
| `production/assessors/hard-rules.mjs` | bare error + price+service |
| `supplementary/policies/geo-evidence-policy-v2.*` | Geo policy V2 |
| `supplementary/regression/geo-commercial-error-analysis-v1.json` | Forensics |
| `confirmation/build-confirmation-geo-v2-strata.mjs` | V2 builder |
| `confirmation/strata/geo_commercial_confirmation_v2/**` | V2 blind set |
| `tests/run-geo-false-reject-regression.mjs` | 16-case regression |
| `tests/run-wave31f-bypass-audit.mjs` | Bypass audit |
| `tests/run-confirmation-validation.mjs` | V2 stratum support |
| `tests/run-problem-query-policy-regression.mjs` | Extended minimal pairs |
| `tests/run-under-admission-regression.mjs` | v1.3 unit tests |
| `reports/confirmation-geo-v2-pass-*` | Geo V2 live results |
| `reports/problem-policy-regression-1782223046785/` | Problem policy |
| `reports/geo-false-reject-regression-*` | Closed regression |
| `reports/wave-3.1f-operator-review-package-v1.json` | Operator package |
| `reports/REPORT-mars-search-ppc-wave3-1f-geo-commercial-recall-repair-v1.md` | This report |

---

## 27. Git Status

- **HEAD (3.1E):** `fba8a97` pushed  
- **Wave 3.1F:** local uncommitted per operator review instruction  
- **Secrets / raw provider payloads:** not committed

---

## 28. SAFE UNKNOWN

- Full-corpus live cost at production scale — extrapolated from confirmation runs only.
- Long-term stability of 4 remaining V2 borderline false REJECTs under model updates — not proven beyond single blind run.
- In-scope commercial recall on 1C-only eval registry — not separately measured in V2 (no IN_SCOPE gold labels).

---

## 29. Operator Approval Items

1. Accept **geo V2 PASS** (recall 0.96, FPR 0.0) as sufficient geo-commercial repair evidence?
2. Review **4 remaining V2 false REJECTs** (engineer/figma/mysql edge cases)?
3. Approve **commercial intent vs scope-fit separation** for production admission?
4. Authorize **Wave 3.1F commit** after review?

---

## 30. Recommended Next Action

**OPERATOR REVIEW OF WAVE 3.1F FINAL GEO QUALITY RESULTS**

---

## 31. Stop Condition

Stopped after: 3.1E checkpoint, forensics, scope-fit separation, one bounded geo repair, closed regression, V2 set, live V2 run, problem validation, cross-regression, D3 decision, operator package, bypass audit.

**Not performed:** second repair iteration, holdout re-run, Wave 4, Corvonero, 3.1F commit.
