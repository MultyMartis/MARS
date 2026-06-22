# MARS Search PPC — Bypass Re-Audit After Wave 1.2 v1

**Date:** 2026-06-23  
**Baseline:** [MARS-SEARCH-PPC-BYPASS-RE-AUDIT-WAVE1-1-v1.md](MARS-SEARCH-PPC-BYPASS-RE-AUDIT-WAVE1-1-v1.md)  
**Evidence:** lockdown tests 12/12 PASS, bypass tests 15/15 PASS, synthetic matrix 20/20 PASS

---

## Summary

| Disposition | Wave 1.1 | Wave 1.2 |
|-------------|--------:|---------:|
| CLOSED — EXECUTABLE PROOF | 11 | 14 |
| PARTIALLY CLOSED | 6 | 2 |
| OPEN | 1 | 1 |
| NOT TESTABLE — COMPONENT MISSING | 2 | 2 |
| PLATFORM BOUNDARY — CONTROLLED | 0 | 1 |

---

## Twenty-path comparison

| # | Bypass | Wave 1.1 | Wave 1.2 | Evidence |
|---|--------|----------|----------|----------|
| 1 | Strategy before analytical pack | **CLOSED** | **CLOSED** | Gate test #6 |
| 2 | Campaign before paid SERP | **CLOSED** | **CLOSED** | Gate + degraded-evidence |
| 3 | Degraded mode absent | **CLOSED** | **CLOSED** | degraded-evidence.mjs |
| 4 | Commander before QA | **CLOSED** | **CLOSED** | Export gate + lockdown #7 |
| 5 | Clustering before admission | **CLOSED** | **CLOSED** | ORCA gate test #4 |
| 6 | Negatives before ownership | **CLOSED** | **CLOSED** | ORCA gate test #5 |
| 7 | Pilot replaces full corpus | **CLOSED** | **CLOSED** | Gate test #3 |
| 8 | ABSTAIN wholesale to operator | **OPEN** | **OPEN** | Wave 3 automation deferred |
| 9 | Web-GPT continues without artifacts | **PARTIAL** | **PLATFORM BOUNDARY — CONTROLLED** | Repository validator mandatory; UI unavailable |
| 10 | Manifest not consumed by runtime | **PARTIAL** | **CLOSED** | Legacy CLIs physically locked; lockdown tests #1,#4,#6 |
| 11 | Export changes semantic ownership | **CLOSED** | **CLOSED** | Gate test #10 |
| 12 | Strategy invents competitors | **NOT TESTABLE** | **NOT TESTABLE** | Strategist runtime MISSING |
| 13 | Frequency-only tiering | **NOT TESTABLE** | **NOT TESTABLE** | Tier CLI MISSING |
| 14 | Auto bidding without analytics | **CLOSED** | **CLOSED** | Synthetic + gate |
| 15 | Launch inferred from export | **CLOSED** | **CLOSED** | Synthetic #13 + gate |
| 16 | Post-launch silent SoT mutation | **CLOSED** | **CLOSED** | Gate policy flag |
| 17 | Missing source dates | **PARTIAL** | **PARTIAL** | Artifact resolver; MIG uniform enforcement Wave 2 |
| 18 | Paid SERP outside business hours | **OPEN** | **NOT TESTABLE — COMPONENT MISSING** | MIG mode MISSING; lifecycle blocks downstream |
| 19 | Human review primary engine | **CLOSED** | **CLOSED** | Gate test #14 |
| 20 | Project-specific mistaken for universal | **PARTIAL** | **CLOSED** | Inventory LOCKED labels + output path guard |

---

## Critical executable bypasses (Wave 1.2 closure)

| Bypass | Status |
|--------|--------|
| Subsystem execution without manifest | **CLOSED** — lockdown tests #1, #4, #6 |
| Full corpus substitution | **CLOSED** — gate test #3 |
| Campaign/export before QA | **CLOSED** — gate tests #9, lockdown #7 |
| Semantic mutation during export | **CLOSED** — gate test #10 |
| Bulk manual review as primary classifier | **CLOSED** — gate test #14 |

No open **critical executable** bypass remains.
