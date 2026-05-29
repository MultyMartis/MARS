# XLSX Integrity Notes v0

**Phase:** ORCA XLSX Integrity Hardening v0  
**Scope:** Workbook structural integrity stabilization only · **NOT** Commander import automation · **NOT** Direct API · **NOT** runtime

---

## Observed symptom (pre-hardening)

**Excel recovery mode** was observed when opening generated `triumph-commander-template-fill-draft.xlsx`: Excel reported XML problems and offered to repair the workbook before display.

This is a **workbook survivability** failure — transport output must open cleanly without repair prompts.

---

## Likely XML corruption causes (root cause analysis)

| Cause | Mechanism | Hardening response |
|-------|-----------|-------------------|
| **Broad range clears** | `clearDataRows()` set `cell.value = null` across all mapped columns from row 16 through `worksheet.rowCount` (~133 rows) | **Removed** — no mass nulling of template example rows |
| **Merge / validation drift** | Nulling cells inside or adjacent to merged regions or validated ranges can invalidate OOXML | **Exact-cell overwrite only** on verified mapped columns |
| **ExcelJS rewrite side effects** | Full-sheet touch increases chance of dropping hidden metadata Excel expects | **Minimize touched cells** — preserve untouched template cells |
| **Formula / rich-text overwrite** | Blind assignment to complex cell types | **Fail-closed** on formula cells; sanitize scalars only |
| **Invalid scalar values** | `NaN`, objects, broken refs written as strings | `sanitizeCellValue()` skips or rejects |

**SAFE UNKNOWN:** Full inventory of template merges, data validations, and hidden XML parts was **not** exhaustively parsed in v0. Hardening follows **survivability-first** discipline, not proven Commander roundtrip.

---

## What was changed (v0)

| Area | Change |
|------|--------|
| `template-fill-writer.js` | Removed `clearDataRows()` and all broad row/column clearing on **Тексты** |
| `workbook-writer.js` | Added `safeSetCell`, `sanitizeCellValue`, merge-slave guard, metadata row guard |
| `xlsx-integrity-check.js` | Post-save ExcelJS reopen validation (fail-closed) |
| `export.js` | Reports integrity result on template-fill success |
| Docs | This file, [sample-integrity-run.md](sample-integrity-run.md), [future-expansion-notes-v0.md](future-expansion-notes-v0.md) |

---

## Safe-write protections

- **Row 16+ only** — rows 1–15 (metadata, headers) never written  
- **Verified mapped columns only** — column set from `commander-header-map-v0.json` `status: "verified"`  
- **No range clears** — template example data in unmapped columns may remain below written rows  
- **Merged slave cells** — write attempt → `MERGED_CELL_WRITE` (fail loud)  
- **Formula cells** — overwrite attempt → `FORMULA_CELL_TOUCH`  
- **Integrity gate** — if reopen check fails, output file removed and export exits 1  

---

## Workbook survivability discipline

1. Clone template (source never modified).  
2. Touch only necessary scalars in mapped cells.  
3. Save once.  
4. Reopen with fresh `ExcelJS.Workbook` — success required before operator handoff.  
5. Human opens in Excel **without recovery dialog** — still operator-verified (**SAFE UNKNOWN** until confirmed on your Excel build).

---

## What remains risky

| Risk | Status |
|------|--------|
| Commander import acceptance | **NOT claimed** — integrity ≠ import fidelity |
| Stale template rows below export row count | Example rows in unmapped columns may persist |
| `\|\|` fastlink/callout encoding | **SAFE UNKNOWN** for Commander |
| Status literal language (Draft vs Russian) | **SAFE UNKNOWN** |
| Excel version-specific repair heuristics | Human must confirm on target Excel |

---

## Remaining SAFE UNKNOWN

- Complete merge map for **Тексты** (only runtime merge-slave detection on write targets)  
- Whether Excel recovery dialog is **fully eliminated** on every operator Excel version (local reopen test required)  
- Hidden macros, VBA, external links in template  
- Binary OOXML diff vs golden template checksum  

---

## Distinction (required)

| Category | This phase |
|----------|------------|
| **Verified** | Code removes range clear; adds reopen check via ExcelJS |
| **Assumption** | Recovery mode was caused primarily by mass null clears |
| **Human remains** | Final reviewer and Commander importer |

**NOT:** runtime · orchestration · Direct API · autonomous export.
