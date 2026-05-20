# Sample run — Sheet1 ZIP patch export v0

**Prototype:** ORCA XLSX Sheet1 Patch Export Prototype v0  
**NOT** production exporter · **NOT** Commander automation · **human review required**.

---

## Prerequisites

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm install
```

Validation report must allow export (`export_allowed: true`). Use fixture or validation-cli output.

---

## Example command

```bash
node sheet1-patch-export.js \
  ../../schema/instances/triumph-s-tier-draft-v1.json \
  fixtures/validation-report.export-allowed.fixture.json
```

**Output (default):** `output/triumph-sheet1-patch-draft.xlsx`

Custom path:

```bash
node sheet1-patch-export.js \
  ../../schema/instances/triumph-s-tier-draft-v1.json \
  fixtures/validation-report.export-allowed.fixture.json \
  output/my-sheet1-patch-draft.xlsx
```

**npm script (optional):**

```bash
npm run export:sheet1-patch
```

---

## Expected console output

- `SUCCESS` with mode `sheet1-zip-patch`
- `Rows patched (sheet1.xml):` (e.g. 15 for triumph-s-tier draft)
- `ZIP preserve check: PASS`
- `sheet1 changed: true`
- `sharedStrings introduced: false`
- Per-entry lines: `xl/worksheets/sheet2.xml: byte-identical`, `sheet3.xml: byte-identical`, etc.
- `Integrity: INTEGRITY_OK` (ExcelJS reopen)
- `OOXML forensics: sharedStrings added = false`
- sheet2/sheet3 cell counts **unchanged** (Δ 0)

---

## Integrity checks (automated)

| Check | Tool | Pass criterion |
|-------|------|----------------|
| Precheck gates | `precheck.js` | `export_allowed`, no blocking errors |
| ZIP entry preserve | `xlsx-zip-patch.js` | SHA-256 match template for sheet2, sheet3, rels, styles |
| No sharedStrings | `xlsx-zip-patch.js` | Entry absent in output |
| Reopen workbook | `xlsx-integrity-check.js` | Sheet **Тексты** readable; probe cells non-empty |
| OOXML comparison | inline in `sheet1-patch-export.js` | `sharedStringsAdded === false`; sheet2/3 cell Δ 0 |

---

## Forensic checks (manual follow-up)

```bash
node ooxml-forensics.js \
  ../../assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx \
  output/triumph-sheet1-patch-draft.xlsx
```

**Expect:**

- `sharedStrings added: false`
- `Only in generated: (none)` or no new parts
- `xl/worksheets/sheet2.xml` — cell count **unchanged**
- `xl/worksheets/sheet3.xml` — cell count **unchanged**
- `xl/worksheets/sheet1.xml` — size delta (patched data only)

Compare indexes: `xlsx-structure-index-v0.json` vs fresh generated index.

---

## Manual Excel validation checklist

Human operator only — **SAFE UNKNOWN** until performed:

- [ ] Open `triumph-sheet1-patch-draft.xlsx` in Microsoft Excel — **no repair dialog**
- [ ] Sheet **Тексты** — rows 16+ show draft phrases/headlines (Cyrillic OK)
- [ ] Sheet **Регионы** — region tree intact (spot-check vs template)
- [ ] Sheet **Словарь значений полей** — dictionary rows intact
- [ ] Save-as without Excel rewriting all sheets (optional control)
- [ ] Commander import trial on test account (if chartered) — compare to JSON source

---

## Compare with failed path (educational)

Template-fill (ExcelJS rewrite) for contrast:

```bash
node export.js \
  ../../schema/instances/triumph-s-tier-draft-v1.json \
  fixtures/validation-report.export-allowed.fixture.json \
  --template-fill
```

Then run `ooxml-forensics.js` against `triumph-commander-template-fill-draft.xlsx` — expect sheet2 collapse and sharedStrings addition.

---

## Exit codes

| Code | Meaning |
|------|---------|
| 0 | Patch + integrity + preserve checks passed |
| 1 | Blocked (precheck, patch, preserve, integrity) |
