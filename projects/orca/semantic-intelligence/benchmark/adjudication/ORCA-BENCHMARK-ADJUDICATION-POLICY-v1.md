# ORCA Benchmark Adjudication Policy v1

**Policy ID:** `orca-benchmark-adjudication-policy`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-benchmark-adjudication-policy-v1.json`](orca-benchmark-adjudication-policy-v1.json)

---

## Purpose

Define adjudication for benchmark gold label formation. Aligns with P0-C disagreement policy; adds benchmark metadata requirements.

---

## Mandatory adjudication triggers

- Eligibility mismatch (ACCEPT / REJECT / ABSTAIN)
- ACCEPT on either side of disagreement
- Protected vs commercial intent conflict
- Rationale quality failure on ACCEPT or borderline ABSTAIN
- Service-candidate conflict on ACCEPT-bound record

---

## Gold fields

Adjudicator sets authoritative values for:

`commercial_eligibility`, `primary_intent`, `ambiguity`, `risk`, and `benchmark.adjudication` block.

---

## Operator escalation

Protected-strata ACCEPT, pilot go/no-go edge cases, contamination suspicion.

---

## Old Corvonero labels

**FORBIDDEN** as adjudication input or tie-breaker.
