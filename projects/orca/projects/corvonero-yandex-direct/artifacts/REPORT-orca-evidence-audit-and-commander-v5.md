# REPORT — КОРВО НЕРО — ORCA EVIDENCE AUDIT AND COMMANDER V5

**Project:** `projects/orca/projects/corvonero-yandex-direct/`  
**Branch:** `mars/post-cycle8-live-tests` @ `bf313e4`  
**Generated:** 2026-06-22  
**ORCA status:** v5 **GENERATED AND EVIDENCE-QA VALIDATED** — operator dry-run required

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/post-cycle8-live-tests` |
| HEAD | `bf313e4` |
| v4 inputs present | Yes — dataset, semantic review, Commander/review XLSX, validation JSON |
| v4 operator approval | **Not approved** — treated as audit input |
| Campaign split | Deferred (operator decision preserved) |
| Import / launch / landing copy | **Not authorized** |
| Commit / push | **Not performed** |
| Unrelated WIP | Untouched (ocpilot, reports, `.recovery-temp/`) |

---

## 2. V4 Rejection Registered

`production/audit/v4-rejection-status.json`:

- Commander v4: **REJECTED BY OPERATOR — EVIDENCE QA FAILURE**
- Review workbook v4: **REJECTED BY OPERATOR — FORMAL QA EVIDENCE**
- v4 pipeline: **AUDIT INPUT**
- Launch readiness: **NOT ASSESSED**

v4 files preserved unchanged for comparison.

---

## 3. V4 Evidence Method Audit

Artifacts: `production/audit/v4-evidence-method-audit.md`, `production/audit/v4-evidence-method-audit.json`

Reviewed generation path: `semantic-human-review-v4.mjs` → `run-full-production-v4.mjs` → `collision-evidence-v4.mjs` → `generate-review-workbook-v4.cjs`.

---

## 4. Root Causes

| RC | Finding |
|----|---------|
| RC-01 | 324/341 active phrases received identical `clear_commercial_service_intent` + HIGH |
| RC-02 | Generic `inferLikelyIntent` fallback copied per group |
| RC-03 | Automatic `reviewer_status: REVIEWED` mislabeled as human-grade |
| RC-04 | No independent group-fit gate; stale v3 group_id retained |
| RC-05 | `advertisement_match: yes` without mismatch detection |
| RC-06 | 2451 unresolved stem warnings + PASS; `collisions_before=0` but `corrections_applied=13` |
| RC-07 | `negativeRegistryWithQA` formal PASS without per-token resolution |
| RC-08 | Collision findings exported with empty corrections for STEM_RISK rows |
| RC-09 | Ad changes sheet: PASS with empty `issues_found` |
| RC-10 | Regression gates ignored workbook integrity |

---

## 5. Semantic Review Method Correction

v5 module: `tools/lib/semantic-evidence-v5.mjs`

- Honest states: `SEMANTICALLY REVIEWED`, `RULE-SCREENED`, `NEEDS CONTENT REVIEW`, `OPERATOR HOLD`
- Prohibited template reasons enforced
- Phrase-specific `phrase_specific_reason` required for active phrases
- LOW commercial confidence cannot remain `ACTIVE COMMERCIAL`
- Separate commercial vs group-fit confidence

---

## 6. Phrase-Specific Semantic Audit

**Output:** `production/semantic-evidence-review-v5.json`, `.md`

| Metric | v4 | v5 |
|--------|----|----|
| Active keywords | 341 | **348** |
| Generic `clear_commercial_service_intent` | 324 | **0** |
| Phrase-specific active reasons | No | **Yes (100%)** |
| Exclusions / hold | partial | **17 excluded + controlled/regulatory** |

Regression anchors addressed:

- `вопрос программисту 1с` → **EXCLUDE INFORMATIONAL**
- `тс пиот 1с розница 2.3/3/3.0` → **CONTROLLED TEST** (retail config)
- `маркировка лекарств аптека` → **CONTROLLED TEST**
- `1с 3.0 внешние печатные формы` → retained with version curiosity handling

---

## 7. Excluded and Held Keywords

**17** phrases excluded from export (informational, regulatory, DIY, employment, hold).  
**0** held groups — all 48 architecture groups retain ≥1 commercial phrase.  
Full list: review workbook sheet **Exclusions**, `production/final-keyword-registry-v5.json` → `reject_log`.

---

## 8. Group Assignment Audit

**Output:** `production/group-assignment-audit-v5.json`, `.md`

Every active phrase scored for group fit (0–100) with candidate groups and ad/landing fit.

---

## 9. Group Reassignments

**10** reassignments logged in `production/group-reassignment-log-v5.md`:

| Phrase | From | To | Reason |
|--------|------|-----|--------|
| `1с маркировка в производстве` | CORV-G06-06 | CORV-G06-01 | General marking — not water (substring «вод» bug fixed) |
| `1с маркировка ввод в оборот` | CORV-G06-06 | CORV-G06-01 | Circulation / general marking — not water |
| TS PIOT retail variants | CORV-G08-02 | CORV-G08-01 | Setup vs integration group |
| External print forms | CORV-G03-03/04 | CORV-G03-05 | External forms owner |

---

## 10. Group Viability

48 groups **ACTIVE** or **ACTIVE NARROW**; **0** held groups in Commander export.  
Sheet **Group viability** in review workbook.

---

## 11. Negative Inventory Audit

Full inventory in review workbook sheets: Global, Direction, Group, Cross, Inline negatives.  
Each record includes collision result, semantic-risk result, final action, explanation (`final-negative-registry-v5.json`).

---

## 12. Stem and Broad-Negative Resolution

**Output:** `production/negative-risk-resolution-v5.json`, `.md`

| Metric | Value |
|--------|------:|
| Unique risky negatives | 363 |
| Total repeated warnings | 2491 |
| SAFE | 333 |
| REMOVED | 30 |
| REPLACED | 0 |
| HOLD | **0** |
| Unresolved | **0** |

---

## 13. Negative Rebuild

Negatives rebuilt from final phrase ownership after reassignment and risk resolution.  
Matrix: `production/final-conflict-negative-matrix-v5.md`.  
30 tokens removed (literal/regression collisions); cross-negatives recalculated per active group.

---

## 14. Collision Audit Method

v5 separates:

- **Literal blocking collision** — negative suppresses keyword in owner group
- **Semantic risk** — broad/stem token without literal hit
- **Preventive correction** — `semantic_risk_correction` (not mislabeled as collision correction)

Module: `tools/lib/collision-evidence-v5.mjs`

---

## 15. Literal Collisions Before and After

| Metric | Value |
|--------|------:|
| Pairs tested | 23 027 |
| Literal collisions before | **20** |
| Literal corrections | 30 |
| Literal collisions after | **0** |

(v4 falsely reported 0 before with 13 unexplained corrections.)

---

## 16. Semantic Risks Before and After

| Metric | Value |
|--------|------:|
| Semantic risk pairs before | 2046 |
| Preventive corrections | 30 |
| Unique negatives resolved | 363 |
| Unresolved risk decisions | **0** |
| QA PASS | **Yes** — all unique tokens classified |

Pair-level stem flags may remain in audit log; each unique token has SAFE/REMOVE decision in **Negative risk resolution** sheet.

---

## 17. Ad Evidence Audit

**Output:** `production/ad-evidence-audit-v5.json`, `production/ad-v4-to-v5-diff.md`

- 53 ads audited
- Certainty patterns scanned (гарант, восстановим, без потери, etc.)
- G07-02 h2 **Исправим** → **После обновления**
- Ad changes sheet documents original problem, risk, correction
- **Ad evidence QA: PASSED**

---

## 18. Operator Workbook Generator Fix

`tools/generate-review-workbook-v5.cjs` + `tools/lib/workbook-integrity-v5.cjs`

Integrity tests:

- No cell `1234`
- Semantic rows = active keyword count
- Risk resolution rows = unique risky negatives
- No blank correction for blocking findings
- Ad changes require evidence fields

**27 sheets** generated; integrity **PASS**.

---

## 19. Report-to-Export Consistency

`production/validation/report-export-consistency-v5.json` — **PASS**

- Keywords: 348 (dataset = workbook = Commander)
- Groups: 48 active
- Collision final_status: PASS
- Commander integrity: INTEGRITY_OK (401 fill rows)

---

## 20. Dataset V5

`production/direct-commander-production-dataset-v5.json` — canonical source for all v5 exports.

---

## 21. Commander XLSX V5

`exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v5.xlsx`

- Unified campaign, markers `[C01]`–`[C08]`
- 348 keywords, 53 ads, 48 groups
- Export integrity: **ok: true**
- v4 file **not overwritten**

---

## 22. Review Workbook V5

`exports/CORVONERO-CAMPAIGN-REVIEW-v5.xlsx`

27 sheets including Semantic evidence review, Group reassignments, Negative risk resolution, Collision summary/findings/samples, QA consistency.  
CSV mirror: `exports/review-v5-csv/`

---

## 23. Validation Gates

| Gate | Status |
|------|--------|
| semantic-evidence-validation-v5 | PASS |
| group-assignment-validation-v5 | PASS |
| negative-risk-validation-v5 | PASS |
| negative-collision-validation-v5 | PASS |
| ad-evidence-validation-v5 | PASS |
| review-workbook-validation-v5 | PASS |
| direct-commander-v5-validation | PASS |
| report-export-consistency-v5 | PASS |
| regression-tests-v5 | PASS |

---

## 24. ORCA Method Improvements

Documented: `production/orca-production-method-improvements-v5.md`

Reusable regression: `tools/regression-tests-v5.mjs` (pattern-based, not Corvonero-only literals).

---

## 25. Files Created or Changed

**Audit:** `production/audit/v4-*`  
**Production v5:** semantic/group/negative/ad registries, dataset, handoff  
**Validation v5:** all gate JSON/MD, collision-evidence-v5, export-run-result-v5  
**Tools v5:** `run-full-production-v5.mjs`, lib modules, workbook/export/regression scripts  
**Exports:** Commander v5 XLSX, Review v5 XLSX, import instructions v5, review-v5-csv/  
**Report:** this file

---

## 26. Git Status

Entire `projects/orca/projects/corvonero-yandex-direct/` tree is **untracked** in repo (pre-existing). No commit, no push.

---

## 27. Remaining Manual Checks

1. Operator opens **CORVONERO-YANDEX-DIRECT-COMMANDER-v5.xlsx** in Direct Commander — **dry-run only**
2. Operator reviews **CORVONERO-CAMPAIGN-REVIEW-v5.xlsx** evidence sheets (especially reassignments, exclusions, negative risk resolution)
3. Log Commander import warnings if any

---

## 28. Next Gate

**OPERATOR REVIEW OF V5 COMMANDER XLSX AND V5 EVIDENCE WORKBOOK**

---

## 29. Stop Condition

ORCA stopped after:

- v4 evidence audit complete
- v5 semantic + group assignment corrected
- All negative-risk warnings resolved (0 HOLD, 0 unresolved)
- Negatives rebuilt; honest collision evidence
- Ad evidence corrected
- Workbook generator fixed
- Reports/exports reconciled
- v5 generated with **all gates PASS**

**Not performed:** campaign split, Commander import, launch, landing copy, commit, push.

### Final status

| Artefact | Status |
|----------|--------|
| v4 Commander | REJECTED AND SUPERSEDED |
| v4 review workbook | REJECTED AND SUPERSEDED |
| v5 Commander | GENERATED AND EVIDENCE-QA VALIDATED |
| v5 review workbook | GENERATED AND EVIDENCE-QA VALIDATED |
| Unresolved negative risks | **0** |
| Blocking collisions | **0** |
| Manual Commander dry-run | **REQUIRED** |
| Launch | **NOT AUTHORIZED** |
