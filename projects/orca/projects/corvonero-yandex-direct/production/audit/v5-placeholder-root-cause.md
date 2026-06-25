# V5 Placeholder Root Cause — 2464

**Defect:** Operator-visible `2464` in narrative evidence fields.

## Root cause

Empty string "" written to narrative evidence columns. ExcelJS deduplicates empty strings to sharedStrings index 2464. Operator tools and Excel display the raw shared-string index "2464" instead of blank.

## Source

- File: `tools/generate-review-workbook-v5.cjs`
- Function: `main → Negative risk resolution sheet mapping`
- Fields: replacement, representative_phrases, QA consistency detail

## Affected scope

- Estimated cells: 613
- Sheets: Negative risk resolution, QA consistency, Collision findings (empty corrections)

## Why validation failed

workbook-integrity-v5 only checked literal "1234", not four-digit shared-string indices or empty narrative fields in XLSX output.

## Reusable correction

Use evidence-format-v5.formatNarrative() with explicit sentinels; forbid bare empty strings in narrative columns; scan for /^\d{4}$/ in narrative fields post-generation.