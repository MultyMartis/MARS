# ORCA P0-I Operator Review Import Plan v1

**Workbook:** `ORCA-P0-I-OPERATOR-REVIEW-WORKBOOK-v1.xlsx`  
**Template:** `orca-p0-i-operator-review-template-v1.json`  
**Overlay model:** review decisions imported as overlay — **no mutation** of `p0-i-pilot-semantic-records-v1.json`

## 1. Workbook identity verification

- Filename must be `ORCA-P0-I-OPERATOR-REVIEW-WORKBOOK-v1.xlsx`
- Sheet names unchanged (10 visible sheets + hidden `_Enums` for dropdown validation)
- Column headers match generator v1

## 2. Checksum verification

- Compare SHA-256 of returned workbook against operator-submitted manifest entry
- Reject import if sheets/columns renamed

## 3. Allowed editable columns

Only operator columns on data sheets:

- Operator decision
- Corrected eligibility
- Corrected primary intent
- Primary error type
- Secondary error types
- Operator comment
- Needs domain expert
- Reviewed by
- Review date

## 4. Query-ID matching

- Match on `Source query ID` (CR2-PHR-*)
- Secondary key: `Pilot row ID` (P0I-*)
- Unmatched rows → import error report

## 5. Duplicate detection

- One decision per query_id
- Duplicate operator rows → reject import

## 6. Controlled-value validation

- Operator decision ∈ approved enum
- Corrected eligibility ∈ ACCEPT|REJECT|ABSTAIN|blank
- Corrected primary intent ∈ P0-B taxonomy|blank
- Error types ∈ approved enum

## 7. Mandatory-completion validation

Required before P0-I human gate:

- All P0 + P1 rows on `Обязательная проверка`
- All workbook random ACCEPT audit rows
- All workbook random REJECT audit rows

Per completed row:

- operator_decision required
- corrected_eligibility when decision is CHANGE_*
- corrected_primary_intent when intent correction applicable
- primary_error_type when decision is CHANGE_* or INVALID_RECORD
- comment for CHANGE_*, NEEDS_DOMAIN_EXPERT, INVALID_RECORD

## 8. Preservation

- Automated fields copied from source records, not overwritten
- Import creates `review/p0-i-operator-review-overlay-v1.json` (future)

## 9. Disagreement analysis

- Compare operator_decision vs automated_decision
- Aggregate error types and legacy disagreement resolution

## 10. P0-I decision gate

Full P0-I PASS requires operator completion + analysis — **not** granted by import alone.

**Importer:** not implemented in workbook v1 task — reuse only if safe generic importer exists.
