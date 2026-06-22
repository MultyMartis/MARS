# Operator Review Package — P0-I Real Integration Pilot v1

**Status:** `HUMAN REVIEW PENDING`  
**Pilot run:** `p0-i-real-slice-v1`  
**Mandatory review rows (queued):** 293 (with overlap across queues)

## Review queues

| Queue | Count | Location |
|-------|------:|----------|
| 01 All ABSTAIN | 70 | `review/01_all_abstain.json` |
| 02 Blocked ACCEPT | 0 | `review/02_blocked_accept.json` (none) |
| 03 HIGH/CRITICAL risk | 0 | (none at admission stage) |
| 04 Protected strata conflicts | 0 | routed via other queues |
| 05 Short-head cases | 2 | `review/05_short_head_cases.json` |
| 06 Problem-query ambiguity | 66 | `review/06_problem_query_ambiguity.json` |
| 07 Product/service ambiguity | 2 | `review/07_product_service_ambiguity.json` |
| 08 Career/provider ambiguity | 14 | `review/08_career_provider_ambiguity.json` |
| 09 Provider/DIY ambiguity | 19 | `review/09_provider_diy_ambiguity.json` |
| 10 Legacy/new disagreement | 108 | `review/10_legacy_new_disagreement.json` |
| 11 Random ACCEPT audit | 7 | `review/11_random_accept_audit.json` |
| 12 Random REJECT audit | 6 | `review/12_random_reject_audit.json` |

## Operator fields (blank by design)

Each queue entry includes:

- `operator_decision`: **null** — awaiting adjudicator
- `operator_notes`: **null**
- `adjudicator`: **null**

## Outputs for inspection

- Semantic records: `output/p0-i-pilot-semantic-records-v1.json`
- Integration metrics: `reports/p0-i-integration-metrics-v1.json`
- Legacy diagnostic summary: `diagnostics/p0-i-legacy-diagnostic-comparison-v1.json`

## Not in scope of this review

- D3 threshold compliance
- Commercial Precision claims
- P0-D / B0 release
- Campaign production authorization
