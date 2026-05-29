# XLSX NO-DUPLICATE-ADS QA v1

**Label:** `orca-xlsx-no-duplicate-ads-qa-v1`  
**Date:** 2026-05-29  
**Script:** `tools/exporter-cli/_validate-no-duplicate-ads-v1.js`  
**Target:** `output/triumph-sheet1-patch-full-cycle-v1.2.xlsx`

---

## Checklist (automated)

| # | Check | Result |
|---|-------|--------|
| 1 | Groups = 12 | PASS |
| 2 | Ad rows = 20 | PASS |
| 3 | Keyword rows = 64 | PASS |
| 4 | Total export rows = 84 | PASS |
| 5 | Duplicate ad signatures = 0 | PASS |
| 6 | Keyword rows: no headline/body/URL | PASS |
| 7 | Ad rows: empty phrase column | PASS |
| 8 | Legacy domain (`gruzotaxi-triumph.ru`) = 0 | PASS |
| 9 | Landing URLs canonical | PASS |
| 10 | Fastlink URLs canonical | PASS |
| 11 | No `direct.yandex.ru/images` URLs | PASS |
| 12 | Region = Краснодарский край (all rows) | PASS |
| 13 | Ad type valid on ad rows | PASS |
| 14 | Display path: no domain in col 49 | PASS |
| 15 | No stale rows after last export row | PASS |
| 16 | XLSX integrity (ExcelJS reopen) | PASS |
| 17 | ZIP preserve (sheet2/3, rels, styles) | PASS |

---

## Ad duplicate signature rule

```
group_name + headline_1 + headline_2 + description + landing_url
```

Evaluated only on rows with non-empty `headline_1` (ad rows).

---

## Commander readiness (transport)

**READY** — all automated gates PASS.

**Not proven:** Commander UI ad/phrase counts after import.

---

## Commands

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm run export:sheet1-patch:full-cycle-v1.2
npm run validate:no-duplicate-ads-v1.2
```
