# Sample run — Display URL + Sitelink Routing v0.3

**Date:** 2026-05-21  
**Fixture:** `schema/instances/triumph-s-tier-draft-v1.json`  
**Report:** `fixtures/validation-report.export-allowed.fixture.json`

---

## Command

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm run export:sheet1-patch:v0.3
```

---

## Expected transport signals

| Check | Expected |
|-------|----------|
| `meta.exporter_version` | `orca-exporter-cli-display-url-routing-v0.3` |
| Display URL col 49 | `manip-5-tonn`, `perevozka-byt`, `dostavka-stroy`, `manip-dlya-b2b`, `vezdehod-6x6` |
| No domain in display cells | No `manipulator-triumph.ru` in col 49 |
| Landing URL col 48 | Full HTTPS URLs with trailing slash |
| Fastlinks per ad | 5 unique production slugs (no root `/`, no duplicate URL) |
| Row removal | Stale rows 31+ removed; dimension `A6:BZ30` |
| ZIP fidelity | sheet2/sheet3 byte-identical to template |

---

## Post-run verification (local)

1. Open `output/triumph-sheet1-patch-display-url-routing-v0.3.xlsx` in Excel  
2. Spot-check row for group `01 — Манипулятор 5 тонн`: display `manip-5-tonn`, landing `.../manipulyator-5-tonn/`  
3. Confirm fastlink URL column has 5 distinct slugs joined with `||`  
4. Re-run `npm run forensics:ooxml` if integrity regression suspected — **optional**

---

## Not verified in this sample

- Commander UI import of display path field semantics  
- Live Direct API upload  
- Automated validation CLI re-run against updated fixture
