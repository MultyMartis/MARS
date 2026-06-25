# REPORT — КОРВО НЕРО — COMMANDER V7 PRODUCTION

**Generated:** 2026-06-22  
**Project:** `projects/orca/projects/corvonero-yandex-direct/`  
**Branch:** `mars/post-cycle8-live-tests` @ `bf313e4`

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/post-cycle8-live-tests` ✓ |
| HEAD | `bf313e4` ✓ |
| Production Scope Recovery Gate | `PASS — V7 PRODUCTION AUTHORIZED` ✓ |
| `v7-production-input-package.json` | readable ✓ |
| v6 source files | unchanged (read-only inputs) ✓ |
| Import / split / landing copy / commit / push | **not authorized** ✓ |

---

## 2. V7 Authorization

- Scope Recovery Gate: **PASSED**
- v7 production status: **IN PRODUCTION**
- Commander dry-run: **AUTHORIZED**
- Moderation / launch: **NOT AUTHORIZED**

---

## 3. Scope Recovery Package Applied

Applied `production/recovery/v7-production-input-package.json` via `tools/lib/v7-scope-recovery-apply.mjs`:

- 41 commercial phrases restored
- 4 informational phrases excluded
- 8 groups reactivated
- 27 controlled-test decisions from `controlled-test-registry-v2.json`
- Cross-negative «перенос данных» narrowed on CORV-G05-01
- v5 ads restored for 8 reactivated groups

---

## 4. Operator Service Coverage

- Service families: **31/31** represented in export
- Commercial seed loss: **0**
- Gate: `production/validation/operator-scope-coverage-v7.json` → **PASS**
- Anchor «обслуживание 1с» satisfied via approved variant «обслуживание 1с для организации»

---

## 5. Commercial Phrases Restored

**41** phrases restored from v6 exclusion (see `production/keyword-v6-to-v7-diff.md`).

Key anchors verified:

| Anchor | Group | Status |
|--------|-------|--------|
| расчет себестоимости 1с | CORV-G04-01 | ACTIVE NARROW |
| перенос данных в 1с | CORV-G05-06 | ACTIVE NARROW |
| внедрение 1с | CORV-G01-04 | ACTIVE NARROW |
| программист 1с новосибирск | CORV-G01-02 | ACTIVE NARROW |
| восстановление работы 1с | CORV-G07-04 | ACTIVE NARROW |
| срочно программист 1с | CORV-G07-01 | ACTIVE COMMERCIAL |

---

## 6. Informational Phrases Excluded

Hard excludes removed from export:

1. маркировка лекарств проверить  
2. маркировка автозапчастей 2026  
3. маркировка автозапчастей честный знак 2026  
4. 1с программист 2026  

Active informational leakage: **0**

---

## 7. Groups Restored

Eight groups reactivated (40 → **48** active export groups):

| Group | Service |
|-------|---------|
| CORV-G07-04 | Восстановление работы 1С |
| CORV-G05-06 | Перенос данных |
| CORV-G04-01 | Расчёт себестоимости |
| CORV-G04-02 | Планирование закупок |
| CORV-G04-03 | Платёжный календарь |
| CORV-G01-02 | Программист 1С Новосибирск |
| CORV-G01-06 | Обслуживание 1С |
| CORV-G01-04 | Внедрение 1С |

Each restored group: keywords ✓, ads ✓, URL ✓, bid ✓, negatives safe ✓

---

## 8. Controlled Tests

- **27** controlled tests with phrase-specific hypotheses (`controlled-test-registry-v2.json`)
- Hypothesis mismatches: **0**
- Generic TS PIOT template removed from unrelated services

---

## 9. Status/Reason Consistency

- Gate: `production/validation/status-reason-consistency-v7.json` → **PASS**
- EXCLUDE with commercial ACTIVE reasons: **0**
- ACTIVE with informational reasons: **0**
- Controlled tests without hypotheses: **0**

---

## 10. Negative Rebuild

- Base: v6 negatives + `negative-impact-plan-v7.json`
- Cross-negative narrow: CORV-G05-01 «перенос данных»
- Full stack recalculated for v7 phrase ownership
- Registry: `production/final-negative-registry-v7.json`

---

## 11. Collision QA

| Metric | Value |
|--------|------:|
| Blocking collisions | 0 |
| Unresolved unique negative risks | 0 |
| Unresolved semantic risks (unique) | 0 |
| Final status | **PASS** |

Evidence: `production/validation/negative-collision-validation-v7.json`

---

## 12. Ads

- **48** ads (one per exported group)
- **8** ads restored from v5 for reactivated groups
- Factual claims within operator-confirmed scope
- Registry: `production/final-ad-registry-v7.json`

---

## 13. Bids

| Tier | Count |
|------|------:|
| T1 | per `bid_summary.by_tier` in dataset |
| Controlled tests | T3 with capped starting bids |

- Zero bids: **0**
- Narrow restored groups: non-negligible bids assigned

---

## 14. URLs and UTM

- Domain: `https://lk.corvonero.ru/`
- `utm_campaign=corvonero_1c_search_nsk`
- Group ID in `utm_content`; `{keyword}` in `utm_term`
- All restored groups use approved landing IDs
- Status: **PLANNED — NOT PUBLISHED**

---

## 15. Dataset V7

Canonical source: `production/direct-commander-production-dataset-v7.json`

- 1 campaign, 8 directions, 48 groups, 311 keywords, 48 ads

---

## 16. Commander XLSX V7

- File: `exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v7.xlsx`
- Fill rows: **359** (48 ads + 311 keywords)
- Integrity: **INTEGRITY_OK**
- Independent validation: **STRUCTURALLY_VALIDATED**

---

## 17. Review Workbook V7

- File: `exports/CORVONERO-CAMPAIGN-REVIEW-v7.xlsx`
- Sheets: **30**
- Integrity: **PASS** (no placeholders 1234/2464/970)
- CSV mirror: `exports/review-v7-csv/`

---

## 18. Independent Validation

| Artefact | Status |
|----------|--------|
| Commander XLSX | PASS |
| Review XLSX | PASS |
| semantic-validation-v7 | PASS |
| operator-scope-coverage-v7 | PASS |
| group-validation-v7 | PASS |
| controlled-test-validation-v7 | PASS |
| negative-validation-v7 | PASS |
| negative-collision-validation-v7 | PASS |
| ad-validation-v7 | PASS |
| status-reason-consistency-v7 | PASS |
| report-export-consistency-v7 | PASS |
| direct-commander-v7-validation | PASS |

---

## 19. Import Instructions

- `exports/CORVONERO-COMMANDER-IMPORT-INSTRUCTIONS-v7.md`
- `exports/CORVONERO-COMMANDER-DRY-RUN-RESULT-TEMPLATE-v7.md`
- **Dry-run only** — no server send, no moderation, no launch

---

## 20. Landing Handoff

- `production/landing-copy-handoff-v7.json`
- Includes all 48 active groups + 8 restored
- Landing copy: **NOT STARTED**

---

## 21. Production Counts

| Entity | v6 | v7 |
|--------|---:|---:|
| Active groups | 40 | **48** |
| Held groups | 8 | **0** |
| Keywords | 274 | **311** |
| Ads | 40 | **48** |
| Controlled tests | 27 | **27** |
| Exclusions (active) | — | **4** informational |

---

## 22. V6→V7 Differences

- +41 commercial phrase restorations
- −4 informational phrases
- +8 group reactivations
- 27 controlled-test hypotheses rebuilt (phrase-specific)
- Cross-negative narrow for data-transfer group
- v6 Commander/Review: **REJECTED** (preserved as evidence)

---

## 23. Files Created or Changed

**New tools:**

- `tools/lib/v7-scope-recovery-apply.mjs`
- `tools/run-full-production-v7.mjs`
- `tools/export-commander-xlsx-v7.cjs`
- `tools/generate-review-workbook-v7.cjs`
- `tools/validate-commander-xlsx-v7.cjs`

**New production v7:**

- `production/direct-commander-production-dataset-v7.json`
- `production/final-keyword-registry-v7.json/.md`
- `production/final-group-registry-v7.json/.md`
- `production/final-negative-registry-v7.json`
- `production/final-ad-registry-v7.json/.md`
- `production/final-controlled-test-registry-v7.json/.md`
- `production/landing-copy-handoff-v7.json`
- `production/*-v6-to-v7-diff.md` (keyword, group, negative, ad)
- `production/validation/*-v7.json/.md` (full validation suite)

**New exports:**

- `exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v7.xlsx`
- `exports/CORVONERO-CAMPAIGN-REVIEW-v7.xlsx`
- `exports/CORVONERO-COMMANDER-IMPORT-INSTRUCTIONS-v7.md`
- `exports/CORVONERO-COMMANDER-DRY-RUN-RESULT-TEMPLATE-v7.md`

**Updated:**

- `production/audit/version-lifecycle-status.json`

**Preserved unchanged:** all v1–v6 artefacts

---

## 24. Git Status

- Entire `projects/orca/projects/corvonero-yandex-direct/` tree: **untracked** (`??`) relative to repo HEAD
- **No commit, no push** (per task)

---

## 25. Remaining Manual Checks

1. Operator review of actual v7 XLSX files
2. Commander desktop dry-run (fill template v7)
3. Manual post-import: strategy, budget, Metrika, goals, business card
4. Landing page publication before launch

---

## 26. Next Gate

**OPERATOR REVIEW OF ACTUAL V7 FILES AND COMMANDER DRY-RUN**

---

## 27. Stop Condition

Task complete. Stopped after:

- ✓ v7 input package applied  
- ✓ operator scope restored  
- ✓ registries rebuilt  
- ✓ dataset v7 + Commander + Review generated  
- ✓ independent validation PASS  
- ✓ dry-run instructions + landing handoff  

**Not performed:** split, import, moderation, launch, landing copy, commit, push

---

## FINAL STATUS

| Item | Status |
|------|--------|
| v6 Commander / Review | REJECTED |
| Scope Recovery Gate | PASSED |
| v7 operator coverage | COMPLETE |
| Commercial seed loss | 0 |
| Informational leakage | 0 |
| Controlled-test hypotheses | VALIDATED |
| Status/reason contradictions | 0 |
| Blocking collisions | 0 |
| Unresolved negative risks | 0 |
| Commander XLSX v7 | GENERATED AND VALIDATED |
| Review XLSX v7 | GENERATED AND VALIDATED |
| Commander dry-run | **AUTHORIZED** |
| Moderation | NOT AUTHORIZED |
| Split | DEFERRED |
| Landing copy | NOT STARTED |
| Launch | NOT AUTHORIZED |
