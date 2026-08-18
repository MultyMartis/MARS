# ISEO-SU Glossary Source Materials

## Canonical Source

| Field | Value |
|-------|-------|
| Canonical filename | `ISEO-SU-GLOSSARY-SOURCE-NIKITA-v1.xlsx` |
| Original filename | `ГЛОССАРИЙ РАБОЧИЙ САЙТ.xlsx` |
| Provider | Никита |
| Project | i-seo.su Glossary |
| Version | v1 |
| Classification | **SOURCE / IMMUTABLE** |
| SHA-256 | `f7651cffc5d03c497062ac6ee5b6288d9397ae5abede43fbd19f1a3ea26699de` |
| Byte size | `23820` |
| Intake date | 2026-07-24 |
| Valid term count | **241** |
| Definitions | **absent** |
| Production import relation | Same binary used for sanitized inventory and WordPress draft import (241 drafts) |
| Related implementation commit | `2e7f150c` (`feat(iseo-su): add wordpress glossary foundation and draft intake`) |
| Related REPORT | `reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-ARCHITECTURE-TEMPLATE-AND-CONTENT-INTAKE.md` |

Canonical path:

`projects/iseo-su-site-ops/materials/glossary/ISEO-SU-GLOSSARY-SOURCE-NIKITA-v1.xlsx`

## Workbook Fields

| Column | Role |
|--------|------|
| **Термин** | Canonical term title (unique publishable label once editorial definitions exist) |
| **Ключевые слова** | Primary keyword phrases for the term |
| **LSI-фразы** | Related / LSI phrases (editorial metadata, not definitions) |
| **Синонимы** | Synonym phrases |

Sheet used for intake: `Лист1`. No fifth column of publishable definitions exists in this workbook.

## Usage Rules

- The original v1 workbook is **not edited** in place.
- New source revisions receive a **new version** filename (`…-v2.xlsx`, `…-v3.xlsx`, …).
- Derived CSV/JSON (or other normalized) files **must identify the parent source SHA-256**.
- **No** workbook upload to production.
- **No** automatic publication from this workbook.
- **No** definitions may be inferred solely from keywords and LSI phrases.

## Derived Artifacts

| Artifact | Path | Parent source |
|----------|------|---------------|
| Sanitized term inventory (JSON) | `data/glossary-intake/glossary-terms-inventory-v1.json` | original name `ГЛОССАРИЙ РАБОЧИЙ САЙТ.xlsx`; working intake basename `glossary-rabochiy-sait.xlsx` |
| Sanitized term inventory (CSV) | `data/glossary-intake/glossary-terms-inventory-v1.csv` | same |
| Theme-bundled inventory copy | `wordpress/iseoblog-glossary/inc/data/glossary-terms-inventory-v1.json` | same (deployed with foundation commit `2e7f150c`) |
| Local working workbook copy | `data/glossary-intake/glossary-rabochiy-sait.xlsx` | byte-identical to canonical v1 at intake; not the immutable locus |

Derived inventories list 241 valid terms and do not invent definitions.

## Editorial Status

- **241** WordPress `glossary` drafts exist (imported under commit `2e7f150c`).
- Definitions are **not** ready in WordPress.
- Editorial standard + full term audit + 12-term pilot prepared in MARS (2026-07-24).
- Public exposure remains **closed** (`ISEO_GLOSSARY_PUBLIC_EXPOSURE = false`).
- Operator / Nikita review required before bulk definition generation or WP content upload.

### Derived editorial artifacts

| Artifact | Path |
|----------|------|
| Editorial standard | `ISEO-SU-GLOSSARY-EDITORIAL-STANDARD-v1.md` |
| Term audit CSV | `data/glossary-editorial/ISEO-SU-GLOSSARY-TERM-AUDIT-v1.csv` |
| Pilot batch | `ISEO-SU-GLOSSARY-PILOT-BATCH-v1.md` |

Parent source SHA-256 remains `f7651cffc5d03c497062ac6ee5b6288d9397ae5abede43fbd19f1a3ea26699de`.

---

*SOURCE / IMMUTABLE / NIKITA v1 · editorial audit linked 2026-07-24*
