# REPORT — КОРВО НЕРО — ORCA V5 QA REPAIR GATE

**Project:** `projects/orca/projects/corvonero-yandex-direct/`  
**Branch:** `mars/post-cycle8-live-tests` @ `bf313e4`  
**Generated:** 2026-06-22  
**Package:** QA REPAIR DECISION PACKAGE (not Commander v6)

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/post-cycle8-live-tests` |
| HEAD | `bf313e4` |
| v5 Commander XLSX | Present — **not operator-approved** |
| v5 review workbook | Present — **rejected input** |
| v5 production JSON/validation | Present |
| v6 production | **NOT AUTHORIZED** |
| Import / launch / split / landing copy | **NOT AUTHORIZED** |
| Commit / push | **NOT performed** |
| Unrelated WIP | Untouched |

---

## 2. V5 Rejection Registered

`production/audit/v5-rejection-status.json`:

- Commander v5: **REJECTED BY OPERATOR — QA EVIDENCE INTEGRITY FAILURE**
- Review workbook v5: **REJECTED BY OPERATOR — PLACEHOLDER AND UNRESOLVED RISK FAILURE**
- Commander dry-run: **BLOCKED**
- v6 production: **NOT AUTHORIZED**
- Launch: **NOT AUTHORIZED**

v5 production files preserved unchanged.

---

## 3. Placeholder Root Cause

**Defect:** Operator-visible `2464` in narrative evidence fields (`replacement`, `representative_phrases`, QA `detail`, etc.).

**Root cause (confirmed via XLSX forensics):**

| Item | Value |
|------|-------|
| Source file | `tools/generate-review-workbook-v5.cjs` |
| Function | `main` → Negative risk resolution / QA consistency mapping |
| Mechanism | Empty string `""` written to narrative columns |
| ExcelJS behaviour | Empty strings deduplicated to `sharedStrings[2464]` |
| Cells referencing index 2464 | **613** (sheet17 — Negative risk resolution, columns F/H) |
| Operator display | Raw shared-string index `2464` shown instead of blank |

**Why validation failed:** `workbook-integrity-v5` checked only literal `1234`, not four-digit shared-string indices or empty narrative fields in XLSX output.

**Reusable correction:** `tools/lib/evidence-format-v5.mjs` — explicit sentinels (`Not required — negative retained`, etc.); forbid bare empty strings in narrative columns; post-generation scan for `/^\d{4}$/`.

Artifacts: `production/audit/v5-placeholder-root-cause.json`, `.md`

---

## 4. Evidence Integrity Scan

`production/audit/v5-evidence-integrity-scan.json` — **696+ findings**

| Category | Severity | Examples |
|----------|----------|----------|
| XLSX 2464 index leak | CRITICAL | 613+ cells in review workbook v5 |
| Generic SAFE template | HIGH | 333 negatives with identical explanation |
| Prohibited correction token | HIGH | 20× `blocks_own_group_keyword` in collision evidence |
| Empty replacement → 2464 | CRITICAL | All SAFE negatives with null replacement |
| Collision summary contradiction | HIGH | `semantic_risks_after=1978`, `unresolved_count=0` |

---

## 5. Career and Education Query Audit

**348 active phrases checked; 4 matched career/education patterns; 4 active leakage.**

| Phrase | Group | v5 | Corrected |
|--------|-------|-----|-----------|
| `1с программист без образования` | CORV-G01-08 | ACTIVE COMMERCIAL | **EXCLUDE EDUCATIONAL** |
| `образование программист 1с` | CORV-G01-08 | ACTIVE COMMERCIAL | **EXCLUDE EDUCATIONAL** |
| `программист 1с без высшего образования` | CORV-G01-08 | ACTIVE COMMERCIAL | **EXCLUDE EDUCATIONAL** |
| `программист 1с высшее образование` | CORV-G01-08 | ACTIVE COMMERCIAL | **EXCLUDE EDUCATIONAL** |

**Required v6 action:** `EXCLUDE_KEYWORD` for all four before export.

Semantic module updated for future runs: `tools/lib/semantic-evidence-v5.mjs` — `EXCLUDE EDUCATIONAL` patterns added.

---

## 6. Controlled Test Audit

Explicit anchors reviewed plus all active phrases with CONTROLLED TEST / LOW|MEDIUM confidence / short noun-only wording.

Regression anchors (`маркировка лекарств аптека`, TS PIOT retail versions, `модуль тс пиот 1с`, `тс пиот 1с атол`) documented with commercial hypothesis, noise risk, and post-launch evaluation rules.

**149 phrases** flagged where v5 lacks concrete commercial hypothesis (gate G-04).

Artifact: `production/audit/v5-controlled-test-audit.json`

---

## 7. Unique Negative Risk Audit

**363 unique negatives audited.**

| Final state | Count |
|-------------|------:|
| SAFE — PROVEN | 0 |
| REMOVED | 30 |
| REPLACED | 0 |
| UNRESOLVED | **333** |
| BLOCKING | 0 |

333 SAFE decisions retain generic template without phrase-specific proof — cannot be classified `SAFE — PROVEN`.

---

## 8. Semantic-Risk Reconciliation

| Metric | Value |
|--------|------:|
| raw_pair_findings_before | 2048 |
| raw_pair_findings_after | 1978 |
| unique_negatives_involved | 363 |
| duplicate_repeated_pair_findings | 1615 |
| UNRESOLVED (unique) | **333** |
| v5 claimed unresolved_count | 0 (**contradiction**) |
| v5 claimed final_status | PASS (**invalid**) |

**Conclusion:** v5 PASS is invalid. Pair-level `semantic_risks_after` was conflated with unique risk resolution; `unresolved_count=0` is not evidence-backed.

---

## 9. Literal Collision Correction Audit

**20 blocking findings** in v5 collision evidence.

| Metric | Value |
|--------|------:|
| Valid exact actions (derived from removal_log) | 20 |
| v5 correction field valid | **0** |
| v5 correction value | `blocks_own_group_keyword` (problem type, not action) |

**Correct action format (example):**  
`DELETE NEGATIVE: removed «честный знак» (group_cross) from scope CORV-G08-01 — literal collision with active keyword «тс пиот честный знак 1с розница»`

Repaired generator now emits exact actions via `formatCollisionCorrection()`.

---

## 10. Review Workbook Generator Repair

**Modified files:**

- `tools/lib/evidence-format-v5.mjs` / `.cjs` — type-safe narrative formatting, sentinels
- `tools/lib/workbook-integrity-v5.mjs` / `.cjs` — 2464/four-digit scan, generic SAFE detection, collision summary contradiction check
- `tools/generate-review-workbook-v5.cjs` — uses formatters for risk resolution, collision corrections, QA detail

**Regression tests:** `production/validation/workbook-integrity-regression-v5.json` — **8/8 PASS**

---

## 11. QA Repair Evidence Workbook

**Generated:** `exports/CORVONERO-V5-QA-REPAIR-AUDIT.xlsx`

12 sheets: Audit summary, V5 rejection, Placeholder findings, Placeholder root causes, Career/education audit, Controlled tests, Unique negative risks, Semantic-risk reconciliation, Literal collision corrections, Evidence integrity findings, Generator regression tests, QA gate decision.

**Not for Commander import.** No campaign production rows.

---

## 12. Independent QA Gate

`production/validation/v5-qa-repair-gate.json`

**Result: BLOCKED — QA REPAIR INCOMPLETE**

| Check | Result |
|-------|--------|
| G-01 Repair package placeholders | PASS |
| G-02 Root cause documented | PASS |
| G-03 Career/education leakage | **FAIL** (4 active) |
| G-04 Controlled test hypothesis | **FAIL** (149) |
| G-05 Unique negative final states | **FAIL** (333 UNRESOLVED) |
| G-06 SAFE evidence specific | **FAIL** |
| G-07 Semantic risks reconciled | **FAIL** |
| G-08 Collision exact actions in v5 source | **FAIL** |
| G-09 Summary reconciliation | **FAIL** |
| G-10 Generator regression | PASS |

---

## 13. ORCA Method Improvements

Documented: `production/orca-qa-repair-method-v1.md`

10 reusable rules + workbook integrity discipline + negative risk state model + gate outcomes.

---

## 14. V6 Production Authorization or Blocker

**Blocker issued:** `production/approvals/v6-production-blocker.md`

v6 production is **NOT AUTHORIZED** until:

1. Career/education exclusions applied to semantic registry
2. 333 generic SAFE negatives upgraded to `SAFE — PROVEN` or REMOVED/REPLACED
3. Collision evidence regenerated with exact correction strings
4. Semantic pair vs unique unresolved metrics reconciled
5. Review workbook regenerated with repaired generator
6. Independent QA Repair Gate re-run → PASS

---

## 15. Files Created or Changed

**Created (audit package):**

- `production/audit/v5-rejection-status.json`
- `production/audit/v5-placeholder-root-cause.json` / `.md`
- `production/audit/v5-evidence-integrity-scan.json` / `.md`
- `production/audit/v5-career-education-query-audit.json` / `.md`
- `production/audit/v5-controlled-test-audit.json` / `.md`
- `production/audit/v5-unique-negative-risk-audit.json` / `.md`
- `production/audit/v5-semantic-risk-reconciliation.json` / `.md`
- `production/audit/v5-exact-collision-correction-log.json` / `.md`
- `production/validation/v5-qa-repair-gate.json` / `.md`
- `production/validation/workbook-integrity-regression-v5.json`
- `production/approvals/v6-production-blocker.md`
- `production/orca-qa-repair-method-v1.md`
- `exports/CORVONERO-V5-QA-REPAIR-AUDIT.xlsx`
- `artifacts/REPORT-orca-v5-qa-repair-gate.md`

**Changed (reusable tooling):**

- `tools/lib/evidence-format-v5.mjs` / `.cjs` (new)
- `tools/lib/qa-repair-audits.mjs` (new)
- `tools/lib/workbook-integrity-v5.mjs` / `.cjs`
- `tools/generate-review-workbook-v5.cjs`
- `tools/lib/semantic-evidence-v5.mjs`
- `tools/run-v5-qa-repair-gate.mjs` (new)

**Not changed:** v5 Commander XLSX, v5 review workbook, v5 production JSON datasets.

---

## 16. Git Status

Corvonero project tree: untracked (`?? projects/orca/projects/corvonero-yandex-direct/`). No commit. No push.

---

## 17. Remaining Issues

1. **2464 placeholder** in existing v5 review workbook (613 cells) — generator fixed; v5 workbook not regenerated per scope.
2. **4 education/career phrases** still ACTIVE in v5 export.
3. **333 UNRESOLVED** unique negative risks (generic SAFE template).
4. **20 collision corrections** in v5 JSON use problem-type token, not action.
5. **1978 vs 0** semantic risk reporting contradiction in v5 summary.
6. **149 controlled-test phrases** need explicit hypothesis before paid traffic.

---

## 18. Next Gate

**V6 PRODUCTION ONLY AFTER QA REPAIR GATE PASSES.**

Follow-up task (when authorized): rebuild semantic registry → apply exclusions → resolve negatives → dataset v6 → Commander v6 + review v6 → dry-run validation.

---

## 19. Stop Condition

**STOPPED** as instructed.

| Status | Value |
|--------|-------|
| v5 Commander | REJECTED |
| v5 review workbook | REJECTED |
| v5 QA Repair Gate | **BLOCKED** |
| placeholder root cause | FIXED in generator |
| placeholder in v5 workbook | 613 remaining (artefact not regenerated) |
| career/education leakage | **4 remaining** |
| unresolved unique negative risks | **333** |
| blocking collisions (invalid corrections) | **20** |
| exact correction evidence in v5 source | INCOMPLETE |
| v6 production | **NOT AUTHORIZED** |
| Commander dry-run | BLOCKED UNTIL V6 |
| launch | NOT AUTHORIZED |

**Did not execute:** Commander XLSX v6, campaign review v6, split, import, launch, landing copy, commit, push.
