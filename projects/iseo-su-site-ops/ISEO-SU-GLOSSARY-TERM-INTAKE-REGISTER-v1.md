# ISEO-SU GLOSSARY TERM INTAKE REGISTER v1

**Programme:** ISEO-SU-SITE-OPS
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-ARCHITECTURE-TEMPLATE-AND-CONTENT-INTAKE
**Date:** 2026-07-24

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

---

*Glossary term intake register v1 · 2026-07-24.*
