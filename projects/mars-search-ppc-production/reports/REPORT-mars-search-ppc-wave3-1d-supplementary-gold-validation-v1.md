# REPORT — MARS SEARCH PPC PRODUCTION — WAVE 3.1D SUPPLEMENTARY GOLD VALIDATION V1

**Date:** 2026-06-23  
**Branch:** `mars/post-cycle8-live-tests`  
**HEAD (live completion checkpoint):** `3d43c12`  
**Supplementary run ID:** `supplementary-pass-1782182564197`  
**Corvonero:** FROZEN

---

## 1. Preflight

| Check | Result |
|-------|--------|
| `2820b9f` in history | **CONFIRMED** |
| `7f7cb21` in history | **CONFIRMED** |
| Live completion uncommitted before checkpoint | **CONFIRMED** — now checkpointed at `3d43c12` |
| Wave 4 started | **NO** |
| Corvonero frozen | **YES** — E2E 9/9 |
| Unrelated WIP staged | **NO** |

### Regression suites (all PASS)

| Suite | Result |
|-------|--------|
| Lifecycle synthetic matrix | 20/20 |
| Wave 1 bypass | 15/15 |
| Wave 1 lockdown | 12/12 |
| Corvonero E2E | 9/9 |
| Wave 2 fixtures | 20/20 |
| Wave 2 bypass | 20/20 |
| Assisted capture | 12/12 |
| Wave 3 production matrix | 30/30 |
| Wave 3 bypass | 20/20 |
| Wave 3 scale | PASS |
| Wave 3.1 bypass | 20/20 |
| Wave 3.1D bypass | 10/10 |
| Secret loader tests | 22/22 |
| Lifecycle validator | READY |
| Cursor task linter | VALID |
| Under-admission regression | 5/5 |
| Ambiguous problem policy tests | 8/8 |

---

## 2. Operator Decisions W3.1D-D1–D7

| ID | Decision |
|----|----------|
| W3.1D-D1 | **APPROVED — REAL PROVIDER EXECUTED** |
| W3.1D-D2 | Original holdout **CLOSED** — no modification / full rerun |
| W3.1D-D3 | Supplementary blind strata **AUTHORIZED** |
| W3.1D-D4 | False rejects → systemic `commercial_under_admission` family |
| W3.1D-D5 | Ambiguous problem-query policy **RECORDED** |
| W3.1D-D6 | Wave 3 operational approval **BLOCKED** until D3 closure |
| W3.1D-D7 | Corvonero **FROZEN** |

Artifacts: `decisions/WAVE-3.1D-SUPPLEMENTARY-GOLD-DECISIONS-v1.md` (uncommitted)

---

## 3. Live Completion Approval and Checkpoint

| Item | Status |
|------|--------|
| Commit | `3d43c12` — `test(orca): validate live semantic provider execution wave 3.1` |
| Push | `mars/post-cycle8-live-tests` → origin |
| Scope | Loader, orchestrator, adapter sanitation, controls, readiness/blind integration, evidence index, REPORT v2 |
| Excluded | Secrets, raw completion folders, supplementary package |

---

## 4. Original Holdout Preservation

| Field | Value |
|-------|-------|
| Holdout ID | `orca-live-eval-holdout-v1` |
| Checksum | `1e76c9f4b94b9cc4288e2bbccd03b812a49d1af29fdf8e0ac9646c77b1e9b52a` |
| Records | 133 |
| Model | `openai/gpt-5-mini` |
| Prompt | `orca-semantic-assessment-prompt-v1` |
| Live run | `completion-pass-1782181300220` |

**Declaration:** `ORIGINAL HOLDOUT — CLOSED — NO FURTHER CALIBRATION OR FULL RERUN AUTHORIZED`

---

## 5. Supplementary Authority Contract

Contract: `supplementary/authority/SUPPLEMENTARY-BLIND-GOLD-AUTHORITY-CONTRACT-v1.md`  
`supplementary_blind_validation: true` — phrase/label separation enforced.

---

## 6. Protected Product Dataset

| Metric | Value |
|--------|-------|
| Gold records | **70** |
| Families | buy, download, license, price, version, boxed, compare, update, official site, self-install, ambiguity pairs, provider contrast |
| Phrase checksum | `5e2b8d74f9b60f6431321438fbb34eb1ca2d969fae307d931bb198b0c955b0b6` |

---

## 7. Protected Informational Dataset

| Metric | Value |
|--------|-------|
| Gold records | **66** |
| Families | what/how/instruction/docs/term/overview/regulatory/news/error/problem/urgent/ambiguity/contrast |
| Phrase checksum | `9f4bf990abd648f0fff20ffe015e2b2d763ef298f1a1a2ec45bc82cde33a537a` |

---

## 8. Dataset Balance and Gold Authority

| Class | Count | Min target | Authority |
|-------|-------|------------|-----------|
| protected_product | 70 | 50 | gold — expert label + policy |
| protected_informational | 66 | 50 | gold — expert label + policy |

Contrast positives, hard borderline, and adversarial minimal pairs included. **Not** an easy-only set.

---

## 9. Blindness Proof

| Control | Status |
|---------|--------|
| Phrase files lack `expected_decision` | **PASS** |
| Labels sealed separately | **PASS** |
| Manifest `calibration_forbidden` | **PASS** |
| Holdout checksum unchanged | **PASS** |
| Assessor label access | **BLOCKED** |

---

## 10. Commercial Under-Admission Analysis

**Family:** `commercial_under_admission` — 4 holdout false rejects  
**Pattern:** `программист 1с <город>` misread as career  
**Hypothesis:** Assessors default to career without vacancy markers; adjudicator reject-wins amplifies disagreement  
**Repair applied (uncommitted):** prompt v1.1 geo-service rules + adjudicator geo-commercial disagreement resolver  
**Forbidden:** phrase-specific exceptions

---

## 11. Bounded Repair

One systemic iteration (uncommitted):

- `prompt-contract.mjs` → v1.1 rules 11–13
- `semantic-adjudicator.mjs` → `resolveGeoCommercialDisagreement`
- Regression: under-admission 5/5, Wave 3/3.1 matrix unchanged

Holdout **not** re-run for tuning.

---

## 12. Ambiguous Problem-Query Policy

Machine-readable: `supplementary/policies/ambiguous-problem-query-policy-v1.json`  
Classes: ACCEPT / ABSTAIN / REJECT with regression tests 8/8 PASS.

---

## 13. Supplementary Live Execution

| Field | Value |
|-------|--------|
| Provider | OpenRouter |
| Model | `openai/gpt-5-mini` |
| Records | 136 |
| Cost | **$0.073** |
| Cap | $50 (shared config) |

Pipeline: blind A → independent B → hard rules → adjudication → D3 metrics.

---

## 14. Product Stratum Metrics

| Metric | Value |
|--------|-------|
| Total gold | 70 |
| ACCEPT / REJECT / ABSTAIN | 14 / 56 / 0 |
| False ACCEPT (protected negatives) | **2** |
| False positive rate | **0.034** (gate ≤ 0.01) |
| False REJECT (contrast) | 0 |
| Assessor agreement | 0.97 |
| Gate | **FAIL** |

High-risk false ACCEPT: boxed delivery queries (`SUP-PROD-BOX-02`, `SUP-PROD-BOX-04`).

---

## 15. Informational Stratum Metrics

| Metric | Value |
|--------|-------|
| Total gold | 66 |
| ACCEPT / REJECT / ABSTAIN | 11 / 55 / 0 |
| False ACCEPT | **0** |
| False positive rate | **0.0** |
| False REJECT (contrast) | **1** (`SUP-INFO-CTR-03`) |
| Assessor agreement | 0.98 |
| Gate | **PASS** |

---

## 16. Cross-Regression

Post-repair: Wave 3 matrix 30/30, bypass 20/20, Wave 3.1 bypass 20/20, scale PASS. **No critical regression** on deterministic strata.

---

## 17. Combined D3 Closure

| Input | Result |
|-------|--------|
| Original holdout | Valid; insufficient gold for product/informational (0 gold each) |
| Supplementary product | **FAIL** FPR |
| Supplementary informational | **PASS** FPR |
| Cross-regression | PASS |
| Under-admission repair | Applied; holdout geo cases not re-evaluated |

**Combined verdict:** `WAVE 3.1 — QUALITY REPAIR REQUIRED`

Not: `LIVE MODEL VALIDATED — D3 QUALITY EVIDENCE COMPLETE`  
Not: `GOLD SUPPORT STILL INSUFFICIENT` (supplementary gold now adequate)

---

## 18. Human Review Package

`reports/supplementary-pass-1782182564197/operator-review-package-v1.json` — small curated set only.

---

## 19. Bypass Audit

Wave 3.1D bypass: **10/10 PASS** — no label leak, no holdout mutation, no calibration on supplementary set, min record counts met, no secret leak in tree.

---

## 20. Wave 3 Final Assessment

```
Wave 3 Overall — NOT OPERATIONAL
Wave 4 — BLOCKED
Corvonero — FROZEN
```

Wave 3.1 quality: supplementary product stratum requires repair before semantic quality approval.

---

## 21. Wave 4 Readiness

**BLOCKED** — combined D3 not complete.

---

## 22. Corvonero Boundary

**FROZEN** — no classification, Semantic Core, or strategy.

---

## 23. Actual Cost

| Phase | USD |
|-------|-----|
| Original live completion | ~0.152 |
| Supplementary run | 0.073 |
| **Session total** | **~0.225** |

Under configured cap.

---

## 24. Files Changed

### Committed (checkpoint `3d43c12`)

- `local-secret-loader.mjs`, loader tests, completion orchestrator
- Adapter/controls/blind/readiness integration
- `.cursorignore`, `.gitignore` (`.secrets/`)
- `live-completion-evidence-index-v1.json`, REPORT v2, roadmap

### Uncommitted (operator review)

- `WAVE-3.1D-SUPPLEMENTARY-GOLD-DECISIONS-v1.*`
- `supplementary/` strata, contracts, policies, regression
- Bounded repair (prompt v1.1, adjudicator v1.1)
- Supplementary test runners + results
- This REPORT

---

## 25. Git Status

Live completion **pushed** at `3d43c12`. Supplementary package and repair remain **local uncommitted**.

---

## 26. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Live geo false-reject fix without holdout re-run | Repair logic unit-tested; live effect on 4 holdout cases **UNKNOWN** |
| Operator acceptance of boxed-delivery gold labels | Pending review |
| Production cost at full corpus scale | Estimated only |

---

## 27. Operator Approval Items

1. Accept or revise supplementary product false ACCEPT cases (boxed delivery).
2. Review `SUP-INFO-CTR-03` geo provider contrast false REJECT.
3. Approve ambiguous problem-query policy for production.
4. Decide on second bounded repair iteration vs gold label revision.
5. Sign off combined D3 only after product stratum gate PASS.

---

## 28. Recommended Next Action

**OPERATOR REVIEW OF WAVE 3.1D COMBINED D3 QUALITY RESULTS**

Review operator package; authorize product-stratum repair or gold adjudication; do not start Wave 4.

---

## 29. Stop Condition

**STOPPED** per task:

- [x] Live completion checkpoint committed and pushed
- [x] Original holdout preserved
- [x] Two supplementary blind gold strata created
- [x] Bounded under-admission repair (uncommitted)
- [x] Ambiguous problem-query policy
- [x] One supplementary live run
- [x] Cross-regression
- [x] Combined D3 decision recorded
- [x] Operator package + bypass audit

**Not done (by design):** holdout re-tuning, Wave 4, Corvonero work, supplementary commit.

**Next gate:** OPERATOR REVIEW OF WAVE 3.1D COMBINED D3 QUALITY RESULTS.
