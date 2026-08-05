# REPORTING «27» ROOT CAUSE v1

## Class

Positional / index-leakage mapping defect.

## Mechanism

Phase 3F.2 reporting seed and HTTP fix helpers mixed:

1. Positional `values: [[ ... ]]` arrays without an explicit header→field contract.
2. Header `indexOf(...)` integers used in the same pipeline as cell writers (`tokenIdx`, `statusIdx`, `rowNumber`).
3. Empty optional fields lacked a keyed empty-fallback policy, allowing numeric indices / metadata to be writable as cell values.

Live workbook after 3F.2.1 targeted resync: **erroneous `27` count = 0**. Remaining pre-repair human defects (`gmail_form`, `true`, `lifecycle_reconciled`) confirmed the mapper was still non-keyed.
