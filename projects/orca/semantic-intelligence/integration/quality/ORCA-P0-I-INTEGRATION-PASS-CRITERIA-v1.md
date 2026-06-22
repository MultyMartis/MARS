# ORCA P0-I Integration Pass Criteria v1

**Criteria ID:** `orca-p0-i-integration-pass-criteria-v1`  
**Date:** 2026-06-22

---

## P0-I PASS definition

P0-I PASS proves **integration and enforcement** — not production classifier accuracy. D3 quality thresholds do **not** apply.

---

## Required evidence

| # | Criterion | Evidence artifact |
|---|-----------|-------------------|
| 1 | All required contracts loaded | Contract-consumption report — 100% required `INTEGRATED` |
| 2 | Version checks pass | No `VERSION MISMATCH` fatals |
| 3 | Schema validation passes | Pilot records validate against P0-B schema |
| 4 | All three decisions emitted | Pilot contains ≥1 ACCEPT, ≥1 REJECT, ≥1 ABSTAIN |
| 5 | ABSTAIN route demonstrated | Review router queue entries |
| 6 | Blocking invariants demonstrated | Known violation phrases blocked with SI-INV codes |
| 7 | No direct service mapping before ACCEPT | `service_candidate.mapping_status` rules enforced |
| 8 | No cluster/negative/campaign output | Schema SI-INV-010 zero violations |
| 9 | Legacy regex has no final authority | Comparison report — authority = tri-state only |
| 10 | Decision trace complete | `versioning` + `audit` populated per record |
| 11 | Contract-consumption proves actual use | Each contract has `fields_consumed[]` non-empty |

---

## FAIL conditions

- Any required contract `REGISTERED — NOT INTEGRATED`
- Legacy `ELIGIBLE COMMERCIAL` in authority field
- ACCEPT on career/edu/DIY leakage phrases without block
- Pilot triggers downstream clustering or export
- Missing operator approval of P0-I charter before PASS claim

---

## After PASS

1. Operator approves P0-I result  
2. Amend and release P0-D hold  
3. Plan B0 qualification (not execution in same gate)
