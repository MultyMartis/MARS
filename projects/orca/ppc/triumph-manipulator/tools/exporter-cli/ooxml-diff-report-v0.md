# OOXML Diff Report v0

**Phase:** ORCA OOXML Workbook Forensics v0  
**Compared:**

| Role | File |
|------|------|
| Original template | `assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx` |
| Generated export | `tools/exporter-cli/output/triumph-commander-template-fill-draft.xlsx` |

**Generated:** `node ooxml-forensics.js` (local, 2026-05-20)  
**Machine indexes:** [xlsx-structure-index-v0.json](xlsx-structure-index-v0.json), [generated-xlsx-structure-index-v0.json](generated-xlsx-structure-index-v0.json), [ooxml-comparison-v0.json](ooxml-comparison-v0.json)

**NOT:** exporter fix · NOT Direct API · NOT runtime

---

## Executive summary

Microsoft Excel reports XML corruption in **all three worksheets** after ExcelJS `readFile` + `writeFile`, while ExcelJS reopens the generated file successfully.

Forensics show **full-workbook rewrite** by ExcelJS:

1. New **`xl/sharedStrings.xml`** part (~850 KB) — template used **inline strings** only.
2. **Massive cell loss** on reference sheets, especially **sheet2** (Регионы): **102 170 → 17 344** `<c>` elements with **unchanged row count** (17 344).
3. **Dimension ref drift** on sheet2/sheet3 (column **A** dropped from `dimension`).
4. **`ignoredErrors`** blocks removed from every worksheet.
5. **`workbook.xml.rels`** reordered — styles/theme/sharedStrings/worksheets relationship IDs changed.

**Conclusion (likely):** Excel rejects **semantic / sparse-grid inconsistency**, not necessarily **ill-formed XML** (all extracted parts pass basic XML parse).

---

## ZIP container comparison

| Metric | Template | Generated |
|--------|----------|-----------|
| ZIP entries (files) | 11 | 18 |
| Total uncompressed (indexed parts) | ~5.28 MB | ~3.05 MB |
| `xl/sharedStrings.xml` | **absent** | **present** (849 971 B) |

**Only in generated (real parts):** `xl/sharedStrings.xml`

**Note:** Generated ZIP lists directory placeholder entries (`xl/`, `docProps/`, …) from the writer — template pack is flatter (11 files only).

---

## Critical part deltas (uncompressed bytes)

| Part | Template | Generated | Δ |
|------|----------|-----------|---|
| `xl/worksheets/sheet2.xml` | 4 325 781 | 1 561 786 | **−2 763 995** |
| `xl/worksheets/sheet1.xml` | 934 922 | 610 694 | −324 228 |
| `xl/worksheets/sheet3.xml` | 6 345 | 4 631 | −1 714 |
| `[Content_Types].xml` | 2 210 | 1 536 | −674 |
| `xl/styles.xml` | 1 199 | 1 742 | +543 |
| `xl/workbook.xml` | 464 | 799 | +335 |
| `xl/_rels/workbook.xml.rels` | 839 | 979 | +140 |
| `xl/theme/theme1.xml` | 7 646 | 7 646 | 0 |

---

## Worksheet XML forensics

### sheet1.xml — Тексты (primary transport)

| Field | Template | Generated |
|-------|----------|-----------|
| `dimension` | `A6:BZ133` | `A6:BZ133` (unchanged) |
| `<row>` count | 128 | 128 |
| `<c>` count | 9 402 | 5 665 (**−3 737**) |
| String model | inline `t="str"` (7 868) | shared `t="s"` (2 872) |
| `ignoredErrors` | 2 | **0** |

ExcelJS rewrote the data grid while keeping row skeleton; many template cells outside the 15 mapped export columns were **dropped** from OOXML.

### sheet2.xml — Регионы (reference tree) — **highest severity**

| Field | Template | Generated |
|-------|----------|-----------|
| `dimension` | `A3:G17461` | `B3:G17461` (**A column removed**) |
| `<row>` count | 17 344 | 17 344 |
| `<c>` count | 102 170 | 17 344 (**−84 826**, ~83% loss) |
| String model | inline `t="str"` (all cells) | shared `t="s"` (one index per row, sparse) |

**Observation:** Row count preserved but multi-column region tree collapsed to ~**one shared-string cell per row**. Dimension still claims thousands of rows — Excel likely flags inconsistent `sheetData` vs `dimension`.

### sheet3.xml — Словарь значений полей

| Field | Template | Generated |
|-------|----------|-----------|
| `dimension` | `A2:E32` | `B2:E32` |
| `<row>` count | 31 | 31 |
| `<c>` count | 155 | 70 |
| `ignoredErrors` | 2 | 0 |

---

## workbook.xml / relationships

**Template `workbook.xml.rels`:** worksheets rId1–3, theme, styles — **no sharedStrings**.

**Generated `workbook.xml.rels`:** adds `sharedStrings` relationship; worksheet rIds shifted (rId4–6).

Generated `workbook.xml` adds `fileVersion`, `calcPr`, `filterPrivacy`, `mc:Ignorable` namespaces — ExcelJS default workbook metadata.

---

## XML parse validation

| Package | XML parts tested | Parse OK | Parse fail |
|---------|------------------|----------|------------|
| Template | 9 | 9 | 0 |
| Generated | 10 | 10 | 0 |

**Important:** Well-formed XML per DOM parser **does not** imply Excel acceptance. Excel applies stricter spreadsheet semantics.

---

## What ExcelJS changed (rewrite observations)

| Behavior | Evidence |
|----------|----------|
| Full workbook load into model | All 3 sheets rewritten on save |
| Inline → shared string migration | New `sharedStrings.xml`; `t="s"` indices in sheets |
| Sparse sheet serialization | sheet2 cell count collapse |
| Removed `ignoredErrors` | 2 → 0 per sheet |
| Namespace / `mc:Ignorable` injection | Generated sheet roots include `x14ac` attributes |
| Untouched sheets not preserved at XML level | sheet2/sheet3 massive deltas despite no exporter writes |

---

## Cross-reference

- Risk framing: [ooxml-risk-analysis-v0.md](ooxml-risk-analysis-v0.md)  
- Operator runbook: [sample-ooxml-analysis.md](sample-ooxml-analysis.md)  
- Prior integrity phase: [xlsx-integrity-notes-v0.md](xlsx-integrity-notes-v0.md)

**Human remains final investigator.** No runtime, no Direct API, no autonomous export claimed.
