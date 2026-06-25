# Evidence Serialization Root Cause v2

## SER-01 — Object-to-string coercion in workbook metric row

- **Mechanism:** object_to_string_coercion
- **Fix:** formatMetricValue() / formatStatusValue() — never String(object)

## SER-02 — Shared-string index leak in regression error column (empty cell)

- **Mechanism:** shared_string_index_leak
- **Fix:** formatErrorDetails(passed, error) → PASS uses «Not applicable — test passed»

## SER-03 — Shared-string index leak in narrative column (empty cell)

- **Mechanism:** shared_string_index_leak
- **Fix:** formatNarrative() with explicit sentinels; forbid bare empty strings

## SER-04 — Legacy four-digit placeholder literal in narrative scan

- **Mechanism:** literal_placeholder
- **Fix:** isPlaceholderValue() rejects /^\d{4}$/
