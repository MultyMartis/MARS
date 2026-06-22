# ORCA Semantic Intelligence — Admission Integration and Enforcement (P0-I)

**Locus:** `projects/orca/semantic-intelligence/integration/`  
**Status:** `P0-I — APPROVED — IMPLEMENTATION AUTHORIZED`  
**Date:** 2026-06-22  
**Audit input:** [triumph-to-orca capability recovery audit v1](../../audits/triumph-to-orca-capability-recovery-v1/) — **APPROVED — CHECKPOINTED** (`a09380d`)

## Purpose

Integration and enforcement architecture that makes approved semantic contracts, taxonomy, annotation rules, and invariants **mandatory consumers** of the admission pipeline — not manifest registrations.

## Boundary

| In scope | Out of scope |
|----------|--------------|
| Consumer architecture | Full P0-I PASS without pilot |
| Contract loading manifest | Corvonero full rerun |
| Blocking invariant validator | B0 benchmark rows |
| Legacy regex migration plan | Gold labels |
| Integration pilot slice design (~200 phrases) | Campaign production |
| P0-D prerequisite amendment | Commander export / import |

## Structure

| Path | Role |
|------|------|
| `charters/` | P0-I integration charter |
| `architecture/` | Consumer architecture overview |
| `consumers/` | Explicit consumer specifications (7) |
| `contracts/` | Contract loading manifest |
| `validators/` | Blocking invariant validator |
| `enforcement/` | Enforcement model and severity |
| `pilot-slice/` | Integration pilot design |
| `migration/` | Legacy regex migration |
| `quality/` | Integration pass criteria |
| `validation/` | Charter validation checklist |
| `decisions/` | Operator decisions I2–I7, approval J1–J7 |
| `reports/` | Task reports |

## Gates

| Item | Status |
|------|--------|
| Capability recovery audit v1 | APPROVED — CHECKPOINTED |
| P0-A ADR | APPROVED — CHECKPOINTED |
| P0-B Taxonomy & Schema | APPROVED — CHECKPOINTED (`3151953`) |
| P0-C Annotation Guideline | APPROVED — CHECKPOINTED (`78b0557`) |
| **P0-I Integration Charter** | **APPROVED — CHECKPOINTED** |
| P0-D Benchmark Charter | ON HOLD UNTIL P0-I INTEGRATION PASS |
| B0 | BLOCKED |
| Corvonero | FROZEN |
| Campaign Production | BLOCKED |

## Reading order

1. [`charters/ORCA-SEMANTIC-ADMISSION-INTEGRATION-CHARTER-v1.md`](charters/ORCA-SEMANTIC-ADMISSION-INTEGRATION-CHARTER-v1.md)
2. [`decisions/ORCA-P0-I-ADMISSION-INTEGRATION-OPERATOR-APPROVAL-v1.md`](decisions/ORCA-P0-I-ADMISSION-INTEGRATION-OPERATOR-APPROVAL-v1.md)
3. [`architecture/ORCA-SEMANTIC-ADMISSION-CONSUMER-ARCHITECTURE-v1.md`](architecture/ORCA-SEMANTIC-ADMISSION-CONSUMER-ARCHITECTURE-v1.md)
4. [`contracts/ORCA-SEMANTIC-CONTRACT-LOADING-MANIFEST-v1.md`](contracts/ORCA-SEMANTIC-CONTRACT-LOADING-MANIFEST-v1.md)
5. [`consumers/README.md`](consumers/README.md)

## Next gate

**IMPLEMENTATION OF I-01–I-07** → operator review → pilot phrase-selection.
