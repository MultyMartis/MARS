# Sample run — Safe Sheet1 Data Row Removal v0

**Phase:** ORCA Safe Sheet1 Data Row Removal v0  
**NOT** production exporter · **NOT** Commander automation

---

## Prerequisites

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm install
```

Validation report: `export_allowed: true`.

---

## Command

```bash
npm run export:sheet1-patch:row-clean
```

Or:

```bash
node sheet1-patch-export.js \
  ../../schema/instances/triumph-s-tier-draft-v1.json \
  fixtures/validation-report.export-allowed.fixture.json \
  output/triumph-sheet1-patch-row-clean-v0.xlsx
```

**Legacy (no row removal):**

```bash
node sheet1-patch-export.js doc.json report.json output/legacy-neutralized.xlsx --no-row-removal
```

---

## Expected console output

- `ORCA Safe Sheet1 Data Row Removal v0 — SUCCESS`
- `Row removal mode: true`
- `Last export row: 30`
- `Stale rows removed: 103` (rows 31–133)
- `Dimension: A6:BZ133 → A6:BZ30`
- `Sheet1 rows after removal: 30 (max)`
- `ZIP preserve check: PASS`
- `Integrity: INTEGRITY_OK`

---

## Expected row range (triumph-s-tier fixture)

| Range | Count | Role |
|-------|-------|------|
| 1–15 | 15 | Preserved (metadata + headers) |
| 16–30 | 15 | ORCA export rows |
| 31–133 | 0 | **Removed** from sheet1.xml |

---

## Manual Excel checklist

- [ ] Open `output/triumph-sheet1-patch-row-clean-v0.xlsx` — **no repair dialog**
- [ ] Sheet **Тексты** — last populated data row ≈ **30**
- [ ] No scroll tail of 100+ empty/garbage rows
- [ ] Row 16 — ORCA group `01 — Манипулятор 5 тонн`
- [ ] Row 31 — **does not exist** (or no data row in sheet)
- [ ] Sheets **Регионы** / **Словарь** unchanged vs template

---

## Manual Commander checklist

- [ ] Import row-clean XLSX (human-operated test account)
- [ ] Confirm **no** stale «грузотакси» / autotarget tail entities
- [ ] Confirm **5** groups with full names
- [ ] Compare vs [commander-import-observations-v0.md](commander-import-observations-v0.md) — update notes after trial

---

## Exit codes

| Code | Meaning |
|------|---------|
| 0 | Patch + row removal + preserve + integrity passed |
| 1 | Blocked (safety check, patch, preserve, integrity) |
