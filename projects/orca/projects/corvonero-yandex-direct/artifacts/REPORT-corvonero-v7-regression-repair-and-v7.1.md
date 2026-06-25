# REPORT — КОРВО НЕРО — V7 REGRESSION REPAIR AND V7.1 XLSX INTEGRITY GATE

## 1. Preflight
- Branch: mars/post-cycle8-live-tests @ 96050ec
- v7 artefacts preserved; v7.1 repair authorized

## 2. V7 Actual Export Rejection
- Commander v7: REJECTED — REGRESSION KEYWORD LEAKAGE
- Review v7: REJECTED — XLSX SERIALIZATION PLACEHOLDER

## 3. Repair Boundary
- 48 groups / 31/31 services unchanged
- Export regression + exclusion authority + narrative serialization only

## 4. Regression Root Cause
- Pattern: SCOPE_RECOVERY_WITHOUT_EXCLUSION_AUTHORITY
- v7 scope recovery restored v5 educational exclusions without exclusion authority gate

## 5. Semantic Exclusion Authority
- Registry: production/operator-semantic-exclusion-registry-v1.json (10 records)

## 6. Four Suspect Phrase Decisions
- EXCLUDE EDUCATIONAL: 1с программист без образования; программист 1с без высшего образования
- EXCLUDE AMBIGUOUS: задание программисту 1с
- EXCLUDE UNNATURAL: часа программиста 1с

## 7. Full Active Keyword Regression Scan
- Scanned: 311; removed: 6 (includes 2 additional v5 education restores)

## 8. Inline-Minus Contract Rule
- Extended validate-campaign-production-contract.mjs: INV-EXCL-01, INV-INLINE-02

## 9. Placeholder 272 Root Cause
- Empty hypothesis strings; Keywords sheet skipped narrative validation in v6 integrity module

## 10. Serialization Repair
- Sentinel: «Не применимо — ключевое слово не является контролируемым тестом»

## 11. Validator Improvements
- workbook-integrity-v7.1.cjs; validate-review-xlsx-v7.1.cjs; commander exclusion registry checks

## 12. Regression Tests
- Contract invariants INV-EXCL-01 / INV-INLINE-02 / INV-SEM-EDU-01

## 13. Dataset V7.1
- Active keywords: **305** (was 311)
- Groups: 48

## 14. Keyword and Negative Delta
- See production/keyword-v7-to-v7.1-diff.md

## 15. Collision and Semantic-Risk Summary
- pair_level_semantic_risk_records = SAFE resolved pairs; unique_unresolved_risks = 0

## 16. Commander XLSX V7.1
- exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v7.1.xlsx

## 17. Review XLSX V7.1
- exports/CORVONERO-CAMPAIGN-REVIEW-v7.1.xlsx

## 18. Independent Actual XLSX Inspection
- Commander: STRUCTURALLY_VALIDATED
- Review: PASS

## 19. Production Contract Re-run
- Critical: 0; High: 0

## 20. Import Instructions
- Issued v7.1 (local preview only)

## 21. Project Status Updates
- v7 exports superseded; v7.1 candidate generated

## 22. Files Created or Changed
- production/direct-commander-production-dataset-v7.1.json
- production/operator-semantic-exclusion-registry-v1.json
- exports/*-v7.1.*
- tools/lib/workbook-integrity-v7.1.cjs
- projects/orca/tools/validate-campaign-production-contract.mjs

## 23. Git Status
- No commit (per task)

## 24. Remaining Manual Checks
- Operator open actual v7.1 XLSX in Excel/Desktop Commander preview

## 25. Next Gate
- UPLOAD AND OPERATOR REVIEW OF ACTUAL V7.1 COMMANDER AND REVIEW XLSX FILES

## 26. Stop Condition
- **PASS — V7.1 READY FOR OPERATOR ACTUAL XLSX REVIEW**
