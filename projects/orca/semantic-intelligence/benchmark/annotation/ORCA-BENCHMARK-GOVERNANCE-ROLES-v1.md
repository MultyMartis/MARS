# ORCA Benchmark Governance Roles v1

**Document ID:** `orca-benchmark-governance-roles`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Define **roles and authority boundaries** for benchmark construction. Extends P0-C role model with benchmark-specific duties.

---

## Roles

| Role | Benchmark duties | Cannot |
|------|------------------|--------|
| **Operator** | Approve charter, B0 pass, blind seal, contamination calls | Delegate D3 threshold changes |
| **QA owner** | Sampling frame audit, quality gates, agreement reports | Adjudicate alone on ACCEPT disputes |
| **Annotator** | First-pass annotation per P0-C | Access peer labels during pass |
| **Second annotator** | Independent second pass | See first-pass eligibility |
| **Adjudicator** | Resolve disagreements; provisional gold | Change D3 thresholds |
| **Domain expert** | Stratum/domain candidate review | Final gold without adjudicator |
| **PPC specialist** | Commercial evidence review on borderline | Override protected-strata REJECT without audit |
| **ML engineer** | Consume **released** dev/calibration splits | Access blind labels pre-gate |
| **LLM assistant** | Draft rationale suggestions | Authoritative labels |

---

## Escalation

Protected-strata ACCEPT disputes, pilot go/no-go edge cases, contamination → **operator**.

---

## Corvonero boundary

No role may use Corvonero v1 labels as adjudication evidence. Corpus **FROZEN**; campaign **BLOCKED**.
