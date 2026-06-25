# V5 Semantic Risk Reconciliation

Generated: 2026-06-22T05:01:04.682Z

## Reconciliation

| Metric | Value |
|--------|------:|
| raw_pair_findings_before | 2048 |
| unique_negatives_involved | 363 |
| unique_semantic_risks | 363 |
| duplicate_repeated_pair_findings | 1615 |
| false_positives | 0 |
| SAFE — PROVEN | 0 |
| REPLACED | 0 |
| REMOVED | 30 |
| NOT APPLICABLE | 30 |
| UNRESOLVED | 333 |
| BLOCKING | 0 |
| raw_pair_findings_after | 1978 |
| unique_unresolved_risks_after | 333 |
| v5_claimed_unresolved_count | 0 |
| v5_claimed_final_status | PASS |
| reconciliation_note | v5 reported unresolved_count=0 while semantic_risks_after=1978 because pair-level stem warnings were conflated with unique risk resolution. Repeated SAFE pair records must not count as unresolved. |
| pass_requires | [object Object] |
| reconciled_pass | false |


## Misleading v5 summary

- semantic_risks_after: 1978
- unresolved_count: 0
- contradiction: **true**