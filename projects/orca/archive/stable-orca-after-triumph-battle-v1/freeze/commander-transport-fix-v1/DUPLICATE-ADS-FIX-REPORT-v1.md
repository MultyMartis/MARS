# DUPLICATE ADS FIX REPORT v1

**Label:** `orca-commander-duplicate-ads-fix-v1`  
**Date:** 2026-05-29  
**Artifact:** `triumph-sheet1-patch-full-cycle-v1.2.xlsx`

---

## Root cause (confirmed)

`mapTemplateFillRows()` nested `for (ad) { for (kw) { push } }` — **Source C** in [DUPLICATE-ADS-AUDIT-v1.md](../commander-url-sync-v1/DUPLICATE-ADS-AUDIT-v1.md).

---

## Fix applied

**Transport split v1.2** — separate AD rows and KEYWORD rows; no keyword×ad multiplication.

---

## Counts

| Metric | v1.1 (before) | v1.2 (after) |
|--------|---------------|--------------|
| Sheet1 data rows | 108 | **84** |
| Commander-equivalent ads | 108 (duplicate) | **20** |
| Keyword phrase rows | 0 (merged) | **64** |
| Groups | 12 | **12** |
| Duplicate ad signatures | 20 | **0** |

---

## Preserved transport discipline

- Canonical `manipulator-triumph.ru` URLs (`.html` slugs + root for `grp_fc12_zakaz`)
- Display paths (short, no domain)
- Fastlinks / callouts (`||` join)
- Region: `Краснодарский край`
- Ad type: `Текстово-графическое` on ad rows only
- Image/creative cols cleared
- Stale template rows removed (last export row 99)

---

## Validation

`npm run validate:no-duplicate-ads-v1.2` — **PASS** (transport QA).

**Commander import:** **SAFE UNKNOWN** — human test account required.
