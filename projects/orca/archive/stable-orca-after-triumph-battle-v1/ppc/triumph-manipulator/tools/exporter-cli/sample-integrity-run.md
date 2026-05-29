# Sample Integrity Run — Operator Runbook

**Phase:** ORCA XLSX Integrity Hardening v0  
**NOT:** Direct API · auto-import · runtime · launch approval

---

## Command example

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm install

node export.js \
  ../../schema/instances/triumph-s-tier-draft-v1.json \
  fixtures/validation-report.export-allowed.fixture.json \
  --template-fill
```

npm script:

```bash
npm run export:template-fill
```

Output default: `output/triumph-commander-template-fill-draft.xlsx`

---

## Integrity success example

Expected console tail:

```text
--- ORCA Exporter Prototype v0 — SUCCESS (template-fill draft) ---
Document:  ...\triumph-s-tier-draft-v1.json
Report:    ...\validation-report.export-allowed.fixture.json
Output:    ...\output\triumph-commander-template-fill-draft.xlsx
Mode:      template-fill
Sheet:     Тексты (header row 14)
Rows written: <N>
Template source unmodified: true
Extension join delimiter: "||" (fastlinks/callouts)
Integrity:   INTEGRITY_OK — Workbook reopened successfully; required sheet and mapped columns readable
  Reopen: 3 sheets, <N> data rows verified
Write discipline: exact cells only (row 16+), no range clear

NOT production-safe · NOT guaranteed Commander import · Human review required.
```

Operator checks after success:

1. Open output in Excel — **no recovery/repair dialog** expected.  
2. Confirm `assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx` mtime/size unchanged.  
3. Sheet **Тексты** row 14 headers match template.  
4. Rows 16+ contain ORCA data in mapped columns only.

---

## Integrity fail example

Simulated failure modes (block codes):

| Condition | Block code |
|-----------|------------|
| ExcelJS cannot reopen saved file | `INTEGRITY_CHECK_FAILED` / `WORKBOOK_LOAD_FAILED` |
| Sheet **Тексты** missing after reopen | `INTEGRITY_CHECK_FAILED` / `SHEET_MISSING` |
| Written rows not readable in mapped cols | `INTEGRITY_CHECK_FAILED` / `WRITTEN_ROWS_MISSING` |
| Write to merged slave cell | `MERGED_CELL_WRITE` |
| Write before row 16 | `METADATA_ROW_TOUCH` |

Example console (integrity):

```text
--- ORCA Exporter Prototype v0 — TEMPLATE-FILL BLOCKED ---
Block code:  INTEGRITY_CHECK_FAILED
Reason:      ExcelJS could not reopen workbook: <detail>
Details:
  - ...
```

Corrupt output is **removed** when integrity fails (best-effort `unlink` on output path).

---

## Standalone integrity mindset

Integrity runs **inside** `export.js --template-fill` after save. There is no separate daemon — single human-triggered run.

To debug without export (advanced): require a saved XLSX and call `runIntegrityCheck()` from `xlsx-integrity-check.js` in a one-off Node snippet — **not** shipped as a separate CLI in v0.

---

## Operator checklist before Commander import

1. Export succeeded with `INTEGRITY_OK`.  
2. Excel opens output **without** XML recovery prompt.  
3. Original template asset untouched.  
4. Review metadata block rows 7–12 (still template defaults in v0).  
5. Scan fastlink/callout `\|\|` cells — adjust manually if needed.  
6. Import in **test** Commander account only.  
7. Log UI errors in pack notes — not governance.

---

## Related

- [xlsx-integrity-notes-v0.md](xlsx-integrity-notes-v0.md) — root cause and risks  
- [sample-template-fill-run.md](sample-template-fill-run.md) — template-fill runbook  
- [template-fill-notes-v0.md](template-fill-notes-v0.md) — fidelity scope
