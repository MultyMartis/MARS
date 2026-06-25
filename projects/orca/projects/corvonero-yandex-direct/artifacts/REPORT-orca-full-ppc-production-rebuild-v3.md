# REPORT — КОРВО НЕРО — ORCA FULL PPC PRODUCTION REBUILD AND QA

**Date:** 2026-06-22  
**Project:** `projects/orca/projects/corvonero-yandex-direct`  
**Status:** GENERATED AND QA VALIDATED — manual Commander dry-run REQUIRED

---

## Summary

| Metric | v2 | v3 |
|--------|---:|---:|
| MIG phrases processed | 2384 | 2384 |
| Active keywords | 341 | **364** |
| Active groups | 48 | 48 |
| Held groups | 0 | 0 |
| Ads | 53 | 53 |
| Global negatives | 57 | **51** |
| Phrase inline negatives | 27 | **7** |
| Collision blocking (export) | 0* | **0** |
| Regression tests | partial | **PASSED** |
| XLSX data rows | 394 | **417** |

*v2 reported 0 collision errors but 26 warnings; v3 regression tests confirmed latent blocking on owner-group negatives.

**Gate:** OPERATOR REVIEW + COMMANDER DRY-RUN
