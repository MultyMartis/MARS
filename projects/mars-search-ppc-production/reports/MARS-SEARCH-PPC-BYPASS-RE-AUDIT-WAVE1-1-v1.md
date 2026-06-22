# MARS Search PPC — Bypass Re-Audit After Wave 1.1 v1

**Date:** 2026-06-22  
**Baseline:** [MARS-SEARCH-PPC-BYPASS-FAILURE-AUDIT-v1.md](../reports/MARS-SEARCH-PPC-BYPASS-FAILURE-AUDIT-v1.md)  
**Wave 1:** [MARS-SEARCH-PPC-BYPASS-RE-AUDIT-WAVE1-v1.md](../reports/MARS-SEARCH-PPC-BYPASS-RE-AUDIT-WAVE1-v1.md)  
**Evidence:** bypass tests 15/15 PASS, Corvonero E2E 9/9 PASS

---

## Summary

| Disposition | Wave 1 | Wave 1.1 |
|-------------|-------:|---------:|
| CLOSED — EXECUTABLE PROOF | 4 | 11 |
| PARTIALLY CLOSED | 8 | 6 |
| OPEN | 6 | 1 |
| NOT TESTABLE — COMPONENT MISSING | 2 | 2 |

---

## Twenty-path comparison

| # | Bypass | Before | Wave 1 | Wave 1.1 | Evidence |
|---|--------|--------|--------|----------|----------|
| 1 | Strategy before analytical pack | HIGH | PARTIAL | **CLOSED** | Gate test #6; forbidden artifact check |
| 2 | Campaign before paid SERP | CRITICAL | PARTIAL | **CLOSED** | Gate + degraded-evidence; bypass #9 |
| 3 | Degraded mode absent | HIGH | PARTIAL | **CLOSED** | degraded-evidence.mjs + gate |
| 4 | Commander before QA | CRITICAL | CLOSED | **CLOSED** | Export gate test #9 |
| 5 | Clustering before admission | HIGH | PARTIAL | **CLOSED** | ORCA gate test #4 |
| 6 | Negatives before ownership | HIGH | PARTIAL | **CLOSED** | ORCA gate test #5 |
| 7 | Pilot replaces full corpus | CRITICAL | CLOSED | **CLOSED** | Gate test #3 |
| 8 | ABSTAIN wholesale to operator | MEDIUM | OPEN | **OPEN** | Wave 3 automation deferred |
| 9 | Web-GPT continues without artifacts | HIGH | PARTIAL | **PARTIAL** | Handoff validator; **no UI hook** |
| 10 | Manifest not consumed by runtime | CRITICAL | PARTIAL | **PARTIAL** | Gate wired; legacy CLIs quarantined not removed |
| 11 | Export changes semantic ownership | CRITICAL | PARTIAL | **CLOSED** | Gate test #10 |
| 12 | Strategy invents competitors | HIGH | OPEN | **NOT TESTABLE** | Strategist runtime MISSING |
| 13 | Frequency-only tiering | HIGH | OPEN | **NOT TESTABLE** | Tier CLI MISSING |
| 14 | Auto bidding without analytics | HIGH | PARTIAL | **CLOSED** | Synthetic #12 + gate |
| 15 | Launch inferred from export | CRITICAL | CLOSED | **CLOSED** | Synthetic #13 + gate |
| 16 | Post-launch silent SoT mutation | CRITICAL | PARTIAL | **CLOSED** | Gate policy flag |
| 17 | Missing source dates | HIGH | OPEN | **PARTIAL** | Artifact resolver; MIG uniform enforcement pending |
| 18 | Paid SERP outside business hours | CRITICAL | OPEN | **OPEN** | MIG mode MISSING |
| 19 | Human review primary engine | MEDIUM | CLOSED | **CLOSED** | Gate test #14 |
| 20 | Project-specific mistaken for universal | HIGH | PARTIAL | **PARTIAL** | Inventory + quarantine labels |

---

## Closure standard (W1.1-D6)

Wave 1.1 cannot mark CLOSED without executable proof. Documentation-only guards remain PARTIALLY CLOSED.
