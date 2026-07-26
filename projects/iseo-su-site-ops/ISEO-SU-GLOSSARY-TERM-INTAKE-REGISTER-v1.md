# ISEO-SU GLOSSARY TERM INTAKE REGISTER v1

**Programme:** ISEO-SU-SITE-OPS
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-ARCHITECTURE-TEMPLATE-AND-CONTENT-INTAKE
**Date:** 2026-07-25 (updated after Batch 02 drafts; Batch 03 2026-07-26)

## Source

| Field | Value |
|-------|-------|
| Original workbook | `ГЛОССАРИЙ РАБОЧИЙ САЙТ.xlsx` (Никита) |
| Canonical immutable source | `materials/glossary/ISEO-SU-GLOSSARY-SOURCE-NIKITA-v1.xlsx` |
| SHA-256 | `f7651cffc5d03c497062ac6ee5b6288d9397ae5abede43fbd19f1a3ea26699de` |
| Source register | `ISEO-SU-GLOSSARY-SOURCE-MATERIAL-REGISTER-v1.md` |
| Intake-era working copy | Operator Desktop → `data/glossary-intake/glossary-rabochiy-sait.xlsx` |
| Sanitized inventory | `data/glossary-intake/glossary-terms-inventory-v1.json` / `.csv` |

## Row accounting

| Metric | Count |
|--------|-------|
| Total workbook rows | 266 |
| Repeated header rows | 13 |
| Blank separator rows | 12 |
| Malformed rows | 0 |
| Duplicate term names | 0 |
| Valid unique terms | **241** |

## Import result

| Metric | Value |
|--------|-------|
| Dry-run would_create | 241 |
| Imported | **241** |
| Skipped on import | 0 |
| Errors | 0 |
| Post status | **draft** only |
| Definitions / excerpts written | **none** (absent in source; not invented) |
| ACF populated | synonyms, keywords, LSI phrases where present in workbook |
| Sample first IDs | 2444… (АГС and following) |

## Notes

- Full 241-term list is in the sanitized JSON/CSV inventory — not duplicated here.
- Re-run is idempotent by normalized title (existing drafts are skipped).
- Admin import UI disabled after successful intake.

## Editorial audit follow-up (2026-07-24)

| Field | Value |
|-------|-------|
| Editorial task | ISEO-SU-SITE-OPS-GLOSSARY-EDITORIAL-AUDIT-AND-PILOT-CONTENT-STANDARD |
| Audit summary | `ISEO-SU-GLOSSARY-TERM-AUDIT-v1.md` |
| Full audit matrix | `data/glossary-editorial/ISEO-SU-GLOSSARY-TERM-AUDIT-v1.csv` |
| Status counts (provisional) | KEEP 146 · RENAME 48 · MERGE 26 · REVIEW 8 · EXCLUDE 13 |
| Pilot definitions | `ISEO-SU-GLOSSARY-PILOT-BATCH-v1.md` (12 terms, MARS-only) |
| WP drafts mutated | **no** (audit/pilot wave) |
| Public exposure | **still closed** |

## Final corpus + Batch 01 (2026-07-25)

| Field | Value |
|-------|-------|
| Task | ISEO-SU-SITE-OPS-GLOSSARY-FINAL-CORPUS-AND-BATCH-01-CONTENT |
| Final corpus | APPROVED 146 · APPROVED_RENAME 48 · MERGED 26 · DEFERRED 8 · EXCLUDED 13 |
| Corpus artifacts | `ISEO-SU-GLOSSARY-FINAL-CORPUS-v1.md` + CSV |
| Batch 01 size | **30** draft definitions applied to existing posts |
| Batch 01 manifest | `ISEO-SU-GLOSSARY-BATCH-01-MANIFEST-v1.md` |
| Content sources | `content/glossary/batch-01/` |
| WP mutation scope | Batch 01 glossary drafts only (title/content/excerpt/ACF/Yoast); status remains draft |
| Public exposure | **still closed** |
| Publication | **not performed** |

## Batch 01 refinement + Batch 02 (2026-07-25)

| Field | Value |
|-------|-------|
| Task | ISEO-SU-SITE-OPS-GLOSSARY-BATCH-01-REFINEMENT-AND-BATCH-02 |
| Batch 01 refine | 4 MINOR_EDIT applied; 26 PASS_AS_IS; 0 MATERIAL_EDIT |
| Batch 02 size | **45** draft definitions applied to existing posts |
| Populated drafts (approx.) | **75** (30 + 45) |
| Remaining empty drafts | **166** (241 − 75) |
| Batch 02 manifest | `ISEO-SU-GLOSSARY-BATCH-02-MANIFEST-v1.md` |
| Content sources | `content/glossary/batch-02/` |
| Public exposure | **still closed** |
| Publication | **not performed** |

## Batch 03 (2026-07-26)

| Field | Value |
|-------|-------|
| Task | ISEO-SU-SITE-OPS-GLOSSARY-BATCH-03 |
| Batch 03 size | **55** draft definitions applied to existing posts |
| Populated drafts | **130** (30 + 45 + 55) |
| Remaining empty drafts | **111** (241 − 130) |
| Remaining publication-pool | **63** (APPROVED 54 + APPROVED_RENAME 9) |
| Batch 03 manifest | `ISEO-SU-GLOSSARY-BATCH-03-MANIFEST-v1.md` |
| Content sources | `content/glossary/batch-03/` |
| Public exposure | **still closed** |
| Publication | **not performed** |

---

*Glossary term intake register v1 · updated Batch 03 2026-07-26.*
