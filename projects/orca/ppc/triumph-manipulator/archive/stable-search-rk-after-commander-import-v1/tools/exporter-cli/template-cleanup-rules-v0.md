# Commander template cleanup rules v0

**Phase:** ORCA Commander Template Cleanup + New Entity Mode v0  
**Scope:** ZIP-level `sheet1.xml` surgical patch · human-supervised · **NOT** import automation

---

## Cleanup philosophy

The Commander transport template (`triumph-manipulator-commander-template-v0.xlsx`) ships with **leftover rows** from a prior live campaign export. If the exporter writes only the new ORCA draft rows (e.g. 15 rows from row 16), **rows 31–133** still carry old phrases, URLs, and Commander entity IDs.

**Goal:** produce a workbook safe for **new campaign import intent** without breaking OOXML fidelity.

**Principle:** *neutralize content, preserve structure.*

---

## Why rows are not deleted

| Approach | Risk |
|----------|------|
| Delete `<row>` nodes from `sheet1.xml` | Breaks `dimension`, merge refs, conditional formatting anchors, row-index formulas — **high Excel recovery risk** |
| Clear only existing cell `<v>` values | Preserves row/cell refs, merges, formulas, hidden technical cells — **survivability-first** |

This phase **never** removes `<row>` elements. Stale rows remain as structural placeholders with **blanked writable PPC cells**.

---

## Writable vs protected columns

### Cleared on stale rows (rows after export block)

Verified **writable PPC / transport** columns from [commander-header-map-v0.json](commander-header-map-v0.json):

- Required fill keys: group name, phrase, headlines, description, URLs, statuses, extensions  
- Extra: group negatives, geo region  
- Entity IDs: group ID, phrase ID, ad ID  

### Cleared on exported rows (new-campaign mode only)

- Entity ID columns only (`ID группы`, `ID фразы`, `ID объявления`)  
- ORCA content still written from JSON mapping  

### Never touched

| Category | Examples |
|----------|----------|
| Rows 1–15 | Metadata block, headers, sub-header row 15 |
| Formulas | Cells with `<f>` — patch only `<v>` when present; no formula rewrite |
| Merges / `mergeCells` | Unmodified |
| Workbook metadata | `workbook.xml`, `styles.xml`, `rels` |
| Non-sheet1 sheets | **Регионы**, **Словарь значений полей** — byte-preserved via ZIP clone |
| Unsupported / unmapped columns | Combinatorics cols 16–47, RSYA, bids, etc. |
| `ads.ad_type` and structural markers | Col 2 «Тип объявления» — left as template default on stale rows (**probable** transport marker) |

---

## Stale-row neutralization

After export rows `N = fillRows.length`:

1. List all `<row r="…">` with `r >= 16` in template `sheet1.xml`.  
2. For each row `>= 16 + N`, clear writable columns to empty `<v></v>`.  
3. If cell node absent for a column, **skip** (no new cells invented).

**Status columns** (`Статус объявления`, `Статус фразы`) are cleared to empty on stale rows. Exact Commander “inactive” literals are **SAFE UNKNOWN** until human import trial.

---

## Survivability strategy

1. **ZIP-level patch** — only `xl/worksheets/sheet1.xml` replaced.  
2. **No sharedStrings** — fail-closed if introduced.  
3. **SHA verify** sheet2/sheet3/rels unchanged.  
4. **ExcelJS reopen** integrity gate on output.  
5. **Human review** before Commander import — mandatory.

---

## Implementation reference

| Module | Role |
|--------|------|
| [sheet1-xml-builder.js](sheet1-xml-builder.js) | `neutralizeStaleDataRows`, `clearEntityIdsOnExportedRows` |
| [sheet1-patch-export.js](sheet1-patch-export.js) | Orchestrates patch + cleanup + ZIP write |

**NOT:** production importer, Direct API, runtime sync, auto-import.
