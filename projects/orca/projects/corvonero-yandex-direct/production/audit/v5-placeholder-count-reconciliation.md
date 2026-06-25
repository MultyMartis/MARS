# V5 Placeholder Count Reconciliation

# Metrics

Generated: 2026-06-22T05:15:48.290Z

## Metrics

| Metric | Value |
|--------|------:|
| total_affected_cells | 613 |
| total_finding_rows | 334 |
| unique_workbook_sheets | 3 |
| unique_columns | replacement; representative_phrases; detail |
| unique_entities | 363 |
| unique_bad_values | 1 |
| duplicate_occurrences | 280 |
| root_causes | 1 |

## Explanation

613 counts physical XLSX cells storing sharedStrings index 2464 across 3 sheets (602 on Negative risk resolution + 11 elsewhere). 334 counts deduplicated audit finding rows at entity level (333 per-resolution replacement defects + 1 workbook summary). Cell instances vs entity findings — different layers, not interchangeable.

280 extra cell-level occurrences beyond entity finding rows (second column leaks + cross-sheet cells).