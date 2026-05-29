# Sheet1 ZIP Patch Export — notes v0

**Phase:** ORCA XLSX Sheet1 Patch Export Prototype v0  
**Status:** Local human-operated transport prototype · **NOT** production-safe · **NOT** Commander import automation.

---

## Why full workbook rewrite failed

Forensic evidence ([ooxml-risk-analysis-v0.md](ooxml-risk-analysis-v0.md), [ooxml-diff-report-v0.md](ooxml-diff-report-v0.md)) shows that `template-fill-writer.js` path (`ExcelJS` `readFile` + `writeFile`) **re-serializes the entire workbook**, even when only sheet **Тексты** cells are edited.

**Proven side effects:**

| Part | Template → ExcelJS export |
|------|---------------------------|
| `sheet2.xml` (Регионы) | ~102k cells → ~17k cells; dimension `A3:…` → `B3:…` |
| `sheet3.xml` (Словарь) | Same sparse-collapse pattern |
| `xl/sharedStrings.xml` | Absent → added (~850 KB) |
| `ignoredErrors` | Present → removed on all sheets |
| `workbook.xml.rels` | Rewritten by library |

**Root cause:** ExcelJS is not a byte-fidelity OOXML roundtrip engine for this Commander template.

**Survivability implication:** Integrity hardening (exact-cell writes, no range clear) **cannot** fix Commander fidelity while the save path rewrites all sheets.

---

## Why sheet1-only patching exists

This phase introduces a **ZIP-level transport strategy**:

1. Binary-clone the Commander template XLSX (ZIP archive).
2. Read **only** `xl/worksheets/sheet1.xml` from the clone.
3. Surgically patch **target row/cell `<v>` values** (rows 16+, verified columns only).
4. Replace **only** that ZIP entry in the output archive.
5. Leave `sheet2`, `sheet3`, `workbook.xml`, `styles.xml`, `rels`, etc. **untouched**.

ExcelJS is still used for:

- JSON → row mapping (`mapping.js`)
- Reopen integrity gate (`xlsx-integrity-check.js`)
- Optional diagnostics

ExcelJS is **not** used for full workbook serialization in this path.

---

## Byte-preservation strategy

| Layer | v0 behavior |
|-------|-------------|
| Non-sheet1 ZIP entries | SHA-256 verified **byte-identical** to template (`sheet2`, `sheet3`, rels, styles, Content_Types) |
| `sheet1.xml` | Surgical row patch; entry recompressed on replace (expected) |
| `sharedStrings.xml` | Must **not** appear — fail-closed if introduced |
| String model | Preserve `t="str"` + `<v>` cells; no shared string index migration |

**SAFE UNKNOWN:** Whether Excel/Commander accepts **only** sheet1 entry recompression while other entries stay byte-identical — requires human Excel open + Commander import trial.

---

## Patch scope (sheet1)

**Preserved (not regenerated):**

- Worksheet root, namespaces, `dimension`, `sheetViews`, `sheetPr`
- `mergeCells`, `conditionalFormatting`, `hyperlinks`, `ignoredErrors`, `extLst`
- `pageMargins`, `pageSetup`, `cols`
- Row/cell structure outside patched `<v>` nodes

**Modified:**

- Rows **16+** only
- Verified mapped columns per [commander-header-map-v0.json](commander-header-map-v0.json)
- Metadata rows **1–15** never touched

---

## Remaining risks

| Risk | Level |
|------|-------|
| Sheet1 XML regex patch misses unusual cell shapes | Likely (low) — unpatched cell logged |
| `dimension` ref stale after many new rows | SAFE UNKNOWN — v0 uses existing template rows |
| ZIP central directory rewrite on Update | Likely — non-sheet1 **content** still byte-identical in v0 runs |
| Commander import acceptance | **SAFE UNKNOWN** — experimental; human review mandatory |
| Cyrillic / special chars in `<v>` | Mitigated via XML escape; Excel display not verified here |

---

## Commander compatibility

**Experimental only.** This prototype proves **transport discipline** (isolate sheet1 mutation), not Commander import success.

**Human remains:** final reviewer and importer. No Direct API, no daemon, no orchestration.

---

## Related artifacts

| File | Role |
|------|------|
| [sheet1-patch-export.js](sheet1-patch-export.js) | CLI orchestrator |
| [sheet1-xml-builder.js](sheet1-xml-builder.js) | Row/cell XML patch |
| [xlsx-zip-patch.js](xlsx-zip-patch.js) | ZIP clone + entry replace |
| [sample-sheet1-patch-run.md](sample-sheet1-patch-run.md) | Operator runbook |
