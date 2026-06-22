# P0-D Prerequisite Amendment v1

**Amendment ID:** `p0-d-prerequisite-amendment-v1`  
**Date:** 2026-06-22  
**Status:** `PROPOSED — P0-D REMAINS ON HOLD`

---

## P0-D status change

| Before | After |
|--------|-------|
| `PROPOSED — ON HOLD PENDING AUDIT` | `PROPOSED — ON HOLD UNTIL P0-I INTEGRATION PASS` |

Hold record updated by reference: [`../../../audits/triumph-to-orca-capability-recovery-v1/decisions/ORCA-P0-D-BENCHMARK-CHARTER-HOLD-v1.md`](../../../audits/triumph-to-orca-capability-recovery-v1/decisions/ORCA-P0-D-BENCHMARK-CHARTER-HOLD-v1.md)

---

## New prerequisites — P0-D cannot proceed to B0 until

| # | Prerequisite | Verification |
|---|--------------|--------------|
| 1 | P0-I consumer architecture approved | Operator sign-off on P0-I charter |
| 2 | Required contracts have explicit consumers | Contract-consumption report |
| 3 | Integration pilot slice executed | Pilot artifacts I-08 |
| 4 | Contract-consumption audit passes | 100% required INTEGRATED |
| 5 | Semantic invariant validator blocks violations | SI-INV demonstration |
| 6 | ABSTAIN routing demonstrated | Review router samples |
| 7 | Legacy regex authority removed | Migration state DIAGNOSTIC BASELINE |
| 8 | Operator approves P0-I result | P0-I PASS record |

---

## Unchanged P0-D scope

This amendment does **not** redesign:

- Benchmark size phases (B0/B1/B2)
- Stratification model
- Gold label authority
- Adjudication policy
- Corvonero pilot boundary document
- D3 quality thresholds (apply after integration, not as P0-I proof)

---

## Release sequence

```text
P0-I PASS → operator approves amended P0-D → B0 qualification planning → B0 execution (separate gate)
```

Corvonero rerun remains **BLOCKED** until B0 + integration evidence per roadmap Option D.
