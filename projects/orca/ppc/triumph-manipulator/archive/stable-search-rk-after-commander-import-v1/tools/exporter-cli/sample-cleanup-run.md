# Sample run — Template cleanup + new entity mode v0

**Phase:** ORCA Commander Template Cleanup + New Entity Mode v0  
**NOT** production exporter · **NOT** Commander automation · **human review required**

---

## Prerequisites

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm install
```

Validation report must allow export (`export_allowed: true`).

---

## Example command (default: cleanup + new-entity)

```bash
node sheet1-patch-export.js \
  ../../schema/instances/triumph-s-tier-draft-v1.json \
  fixtures/validation-report.export-allowed.fixture.json
```

**Default output:** `output/triumph-sheet1-patch-cleanup-draft.xlsx`

Custom path:

```bash
node sheet1-patch-export.js \
  ../../schema/instances/triumph-s-tier-draft-v1.json \
  fixtures/validation-report.export-allowed.fixture.json \
  output/my-cleanup-draft.xlsx
```

**npm script:**

```bash
npm run export:sheet1-patch:cleanup
```

---

## Expected console output

- `SUCCESS` — mode `sheet1-zip-patch`
- `New campaign mode: true`
- `Stale-row cleanup: true`
- `Rows patched` — e.g. **15** for triumph-s-tier draft
- `Entity ID columns cleared` — cells cleared on exported rows (typically 3 cols × N rows)
- `Stale rows neutralized` — e.g. **103** rows if template has 118 data rows (16–133) and export writes 15
- `ZIP preserve check: PASS` — sheet2/sheet3 byte-identical
- `sharedStrings introduced: false`
- `Integrity: INTEGRITY_OK`

---

## Expected cleanup behavior

| Row range | Behavior |
|-----------|----------|
| 1–15 | Unchanged (headers + campaign metadata) |
| 16 – (15+N) | ORCA draft content written; **ID cols empty** |
| (16+N) – 133 | Writable PPC + ID cols **blanked**; row XML preserved |

For triumph-s-tier draft (N≈15): stale neutralization from **row 31** through last template data row.

---

## Expected blanked rows (spot-check)

Open output in Excel (or ExcelJS probe):

| Cell | Row 16 (exported) | Row 31 (stale) |
|------|-------------------|----------------|
| D — ID группы | empty | empty |
| G — ID фразы | empty | empty |
| I — ID объявления | empty | empty |
| H — Фраза | ORCA phrase text | empty |
| J — Заголовок 1 | ORCA headline | empty |

Row 16 should show **new** Cyrillic copy from JSON; row 31 should **not** show old «грузотакси краснодар» transport text.

---

## Manual review checklist (before Commander import)

- [ ] Excel opens `triumph-sheet1-patch-cleanup-draft.xlsx` — **no repair dialog**
- [ ] Sheet **Тексты** — export block has intended draft copy
- [ ] ID columns empty on rows 16–20 (sample)
- [ ] Row 31+ has no leftover campaign phrases/URLs from template
- [ ] Sheet **Регионы** — tree intact vs template
- [ ] Sheet **Словарь значений полей** — dictionary intact
- [ ] Metadata rows 7–12 — campaign type/negatives/URL still correct for operator intent
- [ ] Commander test import (if chartered) — compare entity creation vs update behavior

---

## Debug flags (non-default)

```bash
# Legacy: keep template IDs, skip stale cleanup
node sheet1-patch-export.js doc.json report.json out.xlsx --preserve-commander-ids --no-cleanup
```

---

## Forensics (optional)

```bash
node ooxml-forensics.js \
  ../../assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx \
  output/triumph-sheet1-patch-cleanup-draft.xlsx
```

Expect: `sharedStrings added: false`; sheet2/sheet3 cell Δ **0**.

---

## Exit codes

| Code | Meaning |
|------|---------|
| 0 | Patch + cleanup + preserve + integrity passed |
| 1 | Blocked (precheck, patch, preserve, integrity) |
