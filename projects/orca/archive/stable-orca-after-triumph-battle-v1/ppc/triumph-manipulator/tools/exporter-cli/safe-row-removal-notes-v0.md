# Safe Sheet1 Data Row Removal v0

**Phase:** ORCA Safe Sheet1 Data Row Removal v0  
**Scope:** ZIP-level `sheet1.xml` only · human-supervised · **NOT** import automation

---

## Why neutralization was not enough

v0.1 **neutralized** stale template rows (cleared cells, masked visible fields with `-`). Commander still:

- Listed structural `<row>` elements as importable objects  
- Showed empty/masked rows in the UI  
- Treated leftover rows as campaign artifacts  

**Evidence:** [commander-import-observations-v0.md](commander-import-observations-v0.md) — import succeeded but garbage rows remained.

**Principle shift:** For stale **data** rows after the ORCA export block, **physical `<row>` removal** is now the default. Rows 1–15 (metadata + headers) are never removed.

---

## Row removal strategy

| Region | Rows (triumph-s-tier fixture) | Action |
|--------|------------------------------|--------|
| Metadata + headers | 1–15 | **Preserve** |
| ORCA export block | 16–30 (15 rows) | **Preserve** + patch content |
| Stale template tail | 31–133 | **Remove** `<row>` nodes |

`lastExportRow = dataStartRow + fillRows.length - 1` → **30** for current fixture.

Implementation: [sheet1-xml-builder.js](sheet1-xml-builder.js) — `removeStaleSheetDataRows`, `buildRowRemovalPlan`.

**NOT:** row deletion on sheet2/sheet3 · NOT sharedStrings · NOT workbook rels rewrite.

---

## Dimension handling

Template dimension: `A6:BZ133`  
After removal: `A6:BZ30` (end row = `lastExportRow`)

Updated when ref matches `START:COLROW` pattern. Other formats → **SAFE UNKNOWN** (left unchanged, export may still succeed).

---

## Safety checks (fail-closed)

| Check | On failure |
|-------|------------|
| Duplicate `<row r="N">` | `DUPLICATE_ROW_REFS` |
| Exported rows missing before removal | `EXPORT_ROWS_MISSING_BEFORE_REMOVAL` |
| Removal touches rows &lt; 16 | `PROTECTED_ROWS_IN_REMOVAL_PLAN` |
| `mergeCells` refs beyond `lastExportRow` | `MERGE_REF_BEYOND_LAST_EXPORT_ROW` |
| Planned rows not removed | `ROW_REMOVAL_FAILED` / `PARTIAL_ROW_REMOVAL` |
| Exported row accidentally removed | `EXPORT_ROW_REMOVED` |
| Max row still &gt; `lastExportRow` after removal | `STALE_ROWS_REMAIN` |

Template v0 merge cells: only rows 14–15 — **verified safe** for removal 31–133.

---

## Operator flags

| Flag | Effect |
|------|--------|
| *(default)* | `rowRemovalMode: true` |
| `--no-row-removal` | Legacy neutralization only (v0.1 behavior) |
| `--keep-template-tail` | Alias for `--no-row-removal` |

---

## Risks and SAFE UNKNOWN

| Risk | Marking |
|------|---------|
| Conditional formatting anchors on removed rows | **SAFE UNKNOWN** — not scanned in v0 |
| `ignoredErrors` / extLst row refs | **SAFE UNKNOWN** |
| Commander import after row delete | **Human verify** required |
| Non-standard dimension ref shapes | Dimension skipped (`DIMENSION_REF_UNPARSED`) |

---

## Output artifact

`output/triumph-sheet1-patch-row-clean-v0.xlsx` — does **not** overwrite [triumph-sheet1-patch-feedback-v0.1.xlsx](output/triumph-sheet1-patch-feedback-v0.1.xlsx).

---

## Distinction (required)

| Layer | Status |
|-------|--------|
| XML row cleanup in sheet1 | **Implemented** (this phase) |
| Commander import quality | **Human-verified** per session |
| Direct API / runtime | **Not claimed** |
