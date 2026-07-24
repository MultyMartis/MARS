# ISEO-SU GLOSSARY SOURCE MATERIAL REGISTER v1

**Programme:** ISEO-SU-SITE-OPS
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-SOURCE-MATERIAL-CANONICALIZATION
**Date:** 2026-07-24
**Classification:** SOURCE / IMMUTABLE / NIKITA v1

---

## 1. Source Status

| Field | Value |
|-------|-------|
| Status | **CANONICALIZED** |
| Version | v1 |
| Mutability | **IMMUTABLE** — never overwrite |
| Production upload | **forbidden** |
| Publication from workbook | **forbidden** |

---

## 2. Provider and Provenance

| Field | Value |
|-------|-------|
| Provider | Никита |
| Project | i-seo.su Glossary |
| Original filename | `ГЛОССАРИЙ РАБОЧИЙ САЙТ.xlsx` |
| Prior operator location (intake-era) | Operator Desktop → project working copy under `data/glossary-intake/` |
| Chat upload mount `/mnt/data/…` | **not available** in this Cursor environment |
| Accessible binary used for canonicalization | `data/glossary-intake/glossary-rabochiy-sait.xlsx` (documented copy of the original workbook; same bytes as production-import source) |
| Version mismatch vs import inventory | **none** — structure and 241 valid-term accounting match intake registers |

---

## 3. Canonical File

| Field | Value |
|-------|-------|
| Canonical path | `projects/iseo-su-site-ops/materials/glossary/ISEO-SU-GLOSSARY-SOURCE-NIKITA-v1.xlsx` |
| Canonical filename | `ISEO-SU-GLOSSARY-SOURCE-NIKITA-v1.xlsx` |
| Provenance README | `materials/glossary/README.md` |
| Copy method | Direct binary `Copy-Item` (no Excel/LibreOffice/Python rewrite) |

---

## 4. Hash and Integrity

| Field | Value |
|-------|-------|
| SHA-256 | `f7651cffc5d03c497062ac6ee5b6288d9397ae5abede43fbd19f1a3ea26699de` |
| Byte size | `23820` |
| Source↔destination match | **exact** (SHA-256 and size) |
| Format | Office Open XML `.xlsx` (ZIP package) |

---

## 5. Workbook Structure

| Field | Value |
|-------|-------|
| Sheet | `Лист1` |
| Columns (4) | Термин · Ключевые слова · LSI-фразы · Синонимы |
| Extra definition columns | **none** |
| VBA / macro package (`vbaProject.bin` etc.) | **absent** |
| Raw rows | 266 |
| Header repeats | 13 |
| Blank separators | 12 |
| Valid unique terms | **241** |
| Duplicate terms | 0 |

---

## 6. Content Coverage

| Content | Present? |
|---------|----------|
| Term titles | yes (241) |
| Keywords | yes (where provided) |
| LSI phrases | yes (where provided) |
| Synonyms | yes (where provided) |
| Publishable definitions / long-form body copy | **no** |

---

## 7. Relation to WordPress Drafts

| Field | Value |
|-------|-------|
| Related implementation commit | `2e7f150c` |
| Related intake REPORT | `reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-ARCHITECTURE-TEMPLATE-AND-CONTENT-INTAKE.md` |
| Draft count | **241** |
| Post status | draft only |
| Definitions written at import | **none** |
| Runtime content store | WordPress CPT `glossary` |
| Workbook role | Provenance source for terms / keywords / LSI / synonyms — **not** the runtime store |

---

## 8. Derived Artifacts

| Artifact | Path | Notes |
|----------|------|-------|
| Sanitized JSON inventory | `data/glossary-intake/glossary-terms-inventory-v1.json` | Must stay tied to parent source hash above |
| Sanitized CSV inventory | `data/glossary-intake/glossary-terms-inventory-v1.csv` | Same |
| Theme inventory copy | `wordpress/iseoblog-glossary/inc/data/glossary-terms-inventory-v1.json` | Deployed with foundation |
| Working intake xlsx | `data/glossary-intake/glossary-rabochiy-sait.xlsx` | Local working copy; canonical locus is `materials/glossary/` |

---

## 9. Versioning Rules

1. **Never overwrite** `ISEO-SU-GLOSSARY-SOURCE-NIKITA-v1.xlsx`.
2. Future operator workbooks become `…-v2.xlsx`, `…-v3.xlsx`, etc.
3. Do not edit the original workbook in place.
4. Normalized import files are **derived** artifacts and must record the parent source SHA-256.
5. WordPress remains the runtime content store.
6. Definitions are prepared in a **separate editorial workflow**.
7. The workbook must **not** be copied to production.

---

## 10. Editorial Limitations

- Keywords and LSI phrases are **not** definitions.
- Empty draft bodies must not be published as finished glossary pages.
- Public exposure remains closed until operator-authorized editorial and publication gates.

### Editorial audit linkage (2026-07-24)

| Artifact | Path |
|----------|------|
| Editorial standard | `ISEO-SU-GLOSSARY-EDITORIAL-STANDARD-v1.md` |
| Term audit summary | `ISEO-SU-GLOSSARY-TERM-AUDIT-v1.md` |
| Term audit CSV | `data/glossary-editorial/ISEO-SU-GLOSSARY-TERM-AUDIT-v1.csv` |
| Pilot batch | `ISEO-SU-GLOSSARY-PILOT-BATCH-v1.md` |
| SEO / linking model | `ISEO-SU-GLOSSARY-SEO-AND-INTERNAL-LINKING-MODEL-v1.md` |
| Parent source SHA-256 | `f7651cffc5d03c497062ac6ee5b6288d9397ae5abede43fbd19f1a3ea26699de` (unchanged) |

Workbook v1 remains **immutable**; audit/pilot artifacts are derived editorial work, not a new source version.

---

## 11. Security and Privacy Review

| Check | Result |
|-------|--------|
| Executable macros | none detected |
| Email-like strings in shared strings | 0 |
| Phone-like strings in shared strings | 0 |
| Password / API-key-like markers | 0 |
| Obvious personal customer data | none observed (SEO glossary metadata only) |
| Threaded-comments person list | empty stub XML only |

---

## 12. Future Updates

1. Operator supplies a new workbook revision if terms/metadata change.
2. Store as `ISEO-SU-GLOSSARY-SOURCE-NIKITA-vN.xlsx` with new provenance notes.
3. Recompute SHA-256; do not mutate v1.
4. Refresh derived inventories only under an explicit charter.
5. Definition writing and publication remain separate tasks.

---

*Glossary source material register v1 · 2026-07-24.*
