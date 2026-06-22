# ORCA P0-I Operator Decisions v1

**Date:** 2026-06-22  
**Status:** `APPROVED — IMPLEMENTATION AUTHORIZED`  
**Machine-readable:** [`orca-p0-i-operator-decisions-v1.json`](orca-p0-i-operator-decisions-v1.json)  
**Approval record:** [`ORCA-P0-I-ADMISSION-INTEGRATION-OPERATOR-APPROVAL-v1.md`](ORCA-P0-I-ADMISSION-INTEGRATION-OPERATOR-APPROVAL-v1.md)

---

## I1 — Audit

**TRIUMPH-TO-ORCA CAPABILITY RECOVERY AUDIT V1 — APPROVED**

Checkpointed: commit `a09380d`. See [`../../../audits/triumph-to-orca-capability-recovery-v1/decisions/TRIUMPH-TO-ORCA-CAPABILITY-RECOVERY-AUDIT-APPROVAL-v1.md`](../../../audits/triumph-to-orca-capability-recovery-v1/decisions/TRIUMPH-TO-ORCA-CAPABILITY-RECOVERY-AUDIT-APPROVAL-v1.md).

## I2 — Roadmap

**OPTION D — HYBRID CORRECTION**

Insert P0-I integration stage between P0-C and P0-D. Selective merge of invariant duplicates. Amend P0-D prerequisites. Do not approve P0-D unchanged.

## I3 — P0-D

**ON HOLD UNTIL P0-I INTEGRATION PASS**

P0-D benchmark charter remains documentation-only. B0 blocked until P0-I core integration pass, pilot execution, and operator approves amended P0-D.

## I4 — P0-I

**APPROVED — IMPLEMENTATION AUTHORIZED**

Operator approves P0-I integration and enforcement charter v1. Authorizes bounded core implementation I-01–I-07. Does not authorize P0-I PASS without pilot evidence.

## I5 — Legacy admission

**REGEX-BASED `classifyIntent` / `commercialEligibility` IS NOT SEMANTIC AUTHORITY**

Legacy logic may remain only as:

- diagnostic baseline;
- candidate signal generator;
- comparison baseline.

Target state: `DIAGNOSTIC BASELINE / SIGNAL GENERATOR ONLY`.

## I6 — Contract enforcement

A contract is considered **integrated** only if:

1. an explicit consumer loads it;
2. required versions are checked;
3. outputs conform to schema;
4. violations are blocking;
5. evidence is recorded.

Documents referenced in a manifest but not loaded by a consumer: **`REGISTERED — NOT INTEGRATED`**.

## I7 — Historical examples

Triumph and Corvonero phrases may be reused only as:

- diagnostic examples;
- regression candidates;
- freshly annotated cases.

Old labels (Corvonero ELIGIBLE COMMERCIAL, Triumph export rows, v1–v7.1 classifications) are **not ground truth**.

---

## Operator approval J1–J7 (2026-06-22)

| ID | Decision |
|----|----------|
| J1 | P0-I Charter — `APPROVED — IMPLEMENTATION AUTHORIZED` |
| J2 | Core implementation I-01–I-07 — authorized |
| J3 | Pilot execution — not yet authorized |
| J4 | P0-D — `ON HOLD UNTIL P0-I INTEGRATION PASS` |
| J5 | Legacy regex — diagnostic only; not authoritative eligibility |
| J6 | I-09 — `PLANNED — DEFERRED` |
| J7 | Runtime proof boundary — loading/blocking/routing only; no accuracy claim |
