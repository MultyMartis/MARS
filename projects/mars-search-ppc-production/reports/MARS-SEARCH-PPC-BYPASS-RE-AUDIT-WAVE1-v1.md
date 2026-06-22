# MARS Search PPC — Bypass Re-Audit After Wave 1 v1

**Date:** 2026-06-22  
**Baseline:** [MARS-SEARCH-PPC-BYPASS-FAILURE-AUDIT-v1.md](../reports/MARS-SEARCH-PPC-BYPASS-FAILURE-AUDIT-v1.md)  
**Wave 1 evidence:** `runtime/tests/run-synthetic-matrix.mjs` (20/20 PASS), Corvonero manifest validation

---

## Summary

| Disposition | Count |
|-------------|------:|
| CLOSED | 4 |
| PARTIALLY CLOSED | 8 |
| OPEN | 6 |
| NOT TESTED | 2 |

---

## Before/after matrix

| # | Bypass | Before | After Wave 1 | Evidence |
|---|--------|--------|--------------|----------|
| 1 | Strategy before analytical pack | HIGH / partial validator | **PARTIALLY CLOSED** | Synthetic #5; `FORBIDDEN_BEFORE` in runtime |
| 2 | Campaign before paid SERP | CRITICAL | **PARTIALLY CLOSED** | Synthetic #6; `checkPaidSerpDegradation` when manifest used |
| 3 | Degraded mode absent | HIGH / partial | **PARTIALLY CLOSED** | Synthetic #7; `degraded-evidence.mjs` schema validation |
| 4 | Commander before QA | CRITICAL | **CLOSED** | Synthetic #10; runtime `FORBIDDEN_BEFORE['SPPC-19']` |
| 5 | Clustering before admission | HIGH | **PARTIALLY CLOSED** | Synthetic #8; prerequisite + ownership artifact check |
| 6 | Negatives before ownership | HIGH | **PARTIALLY CLOSED** | Synthetic #9 |
| 7 | Pilot replaces full corpus | CRITICAL | **CLOSED** | Synthetic #4; `corpus-enforcement.mjs` |
| 8 | ABSTAIN wholesale to operator | MEDIUM | **OPEN** | Human-review boundary detects policy flags; I-09 automation deferred Wave 3 |
| 9 | Web-GPT continues without artifacts | HIGH | **PARTIALLY CLOSED** | Execution contract + sync pack; **no Web-GPT runtime** |
| 10 | Manifest not consumed by runtime | CRITICAL | **PARTIALLY CLOSED** | Validator CLI + Cursor/Web-GPT contracts; MIG/ORCA CLIs not wired (Wave 1 W1-04 partial) |
| 11 | Export changes semantic ownership | CRITICAL | **PARTIALLY CLOSED** | Synthetic #11; export mutation flag blocked |
| 12 | Strategy invents competitors | HIGH | **OPEN** | No strategist output schema (Wave 4) |
| 13 | Frequency-only tiering | HIGH | **OPEN** | No tier registry validator (Wave 3) |
| 14 | Auto bidding without analytics | HIGH | **PARTIALLY CLOSED** | Synthetic #12 |
| 15 | Launch inferred from export | CRITICAL | **CLOSED** | Synthetic #13; `final_launch_authority` check |
| 16 | Post-launch silent SoT mutation | CRITICAL | **PARTIALLY CLOSED** | Synthetic #14; policy flag blocked |
| 17 | Missing source dates | HIGH | **OPEN** | Artifact resolver checks `collection_date` when flagged; MIG uniform enforcement Wave 2 |
| 18 | Paid SERP outside business hours | CRITICAL | **OPEN** | MIG mode still MISSING (Wave 2) |
| 19 | Human review primary engine | MEDIUM | **CLOSED** | Synthetic #15; `human-review-boundary.mjs` |
| 20 | Project-specific mistaken for universal | HIGH | **PARTIALLY CLOSED** | Corvonero manifest + operational indexes; capability matrix still partial |

---

## Wave 1 closure notes

Wave 1 **does not** mark bypasses CLOSED unless executable proof exists. Documentation-only updates are **PARTIALLY CLOSED** at best.

**Remaining top unblockers (Wave 2–3):** MIG paid SERP mode (#18), subsystem CLI manifest wiring (#10), ABSTAIN automation (#8), strategist schema (#12).

---

## Related

- [REPORT-mars-search-ppc-wave1-state-enforcement-v1.md](./REPORT-mars-search-ppc-wave1-state-enforcement-v1.md)
- [../runtime/reports/synthetic-matrix-results-v1.json](../runtime/reports/synthetic-matrix-results-v1.json)
