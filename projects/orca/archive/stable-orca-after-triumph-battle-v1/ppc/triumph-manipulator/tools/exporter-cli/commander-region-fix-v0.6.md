# Commander region import fix v0.6

**Phase:** ORCA Commander Region Import Fix v0.6  
**Scope:** Column **52** / **AZ** «Регион» on sheet **Тексты** · Triumph search-only fixture · **no** region ID API

---

## Commander symptom (post–v0.5)

*«Неуказанные и некорректные регионы заменены значением "Все"»* — still observed after v0.4 multi-line geo export.

---

## Operator evidence (direct.xlsx)

Human operator set correct region for group **01 — Манипулятор 5 тонн** and re-exported `direct.xlsx`:

| Field | Correct value | Incorrect (v0.4) |
|-------|---------------|------------------|
| Col **AZ** / «Регион» | `Краснодарский край` | `Краснодарский край` + newline + `Краснодар` |
| | | `Краснодар` alone |
| | | `Все` (Commander fallback) |
| | | empty / blank rows |

Commander accepts the **parent krai label only** for this campaign — not city child line, not multi-line cell.

---

## Root cause

| Issue | v0.4 behavior | Effect |
|-------|---------------|--------|
| Multi-line col 52 | `Краснодарский край\nКраснодар` | Commander treats as invalid → **Все** |
| Stale tail rows | Rows 25–30 blank region before row removal | Fallback **Все** on partial import |
| JSON `primary_region` | `Краснодар` (city) | Mapped to two-line transport |

Row removal (v0) fixed tail blanks; **region label shape** still wrong until v0.6.

---

## Transport rule (v0.6)

`buildGeoRegionForTransport()` in [mapping.js](mapping.js):

- Returns constant **`Краснодарский край`** for every `templateFillRows` row.
- **No** newline join · **no** city child · **no** empty string · **no** `Все`.

`sheet1-xml-builder.js` writes `fillRow.geo_region` to col **52** on rows **16–lastExportRow** (15 rows → row 30).

Stale rows **31+** removed (row removal mode) — not left with template **Все** / empty.

---

## Preserved from v0.2–v0.5

| Feature | Status |
|---------|--------|
| Ad type col 2 | `Текстово-графическое` (v0.5) |
| Display URL col 49 | Short paths (v0.3) |
| Fastlinks | v0.2 routing |
| Image cols 64–66 | Empty (v0.4) |
| Row removal | ON — tail rows deleted |
| ZIP patch | sheet1 only · sheet2/sheet3 byte-preserve |

---

## Human re-import checklist

- [ ] Import `output/triumph-sheet1-patch-region-v0.6.xlsx`
- [ ] No warning about regions replaced with **Все**
- [ ] Col 52 rows 16–30 = **Краснодарский край** (single line)
- [ ] Five groups, ad type, display paths, fastlinks unchanged
- [ ] No image/creative popup

---

## Limitations (SAFE UNKNOWN)

| Topic | Status |
|-------|--------|
| Per-group geo | **Not implemented** — one krai for whole fixture |
| Other cities / campaigns | Constant override — not driven by JSON yet |
| Region IDs | **Not implemented** |
| Sheet **Регионы** mutation | **Forbidden** — ZIP byte-preserve |

---

## Sample run

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm run export:sheet1-patch:v0.6
node _validate-v06.js
```

**Output:** `output/triumph-sheet1-patch-region-v0.6.xlsx`
