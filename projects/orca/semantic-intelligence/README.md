# ORCA Semantic Intelligence — Implementation-Neutral Specification Locus

**Locus:** `projects/orca/semantic-intelligence/`  
**Status:** `P0-I — APPROVED — IMPLEMENTATION AUTHORIZED`  
**P0-B checkpoint:** `3151953`  
**P0-C checkpoint:** `78b0557`  
**Audit checkpoint:** `a09380d`

Implementation-neutral semantic specification for ORCA Semantic Intelligence v1. Not runtime. Not classifier. Benchmark rows not created.

## Authority

- Approved ADR v1 (`projects/orca/architecture/semantic-intelligence/`)
- Operator approval A1–A7, B1–B7, C1–C7, J1–J7 (P0-I)
- Capability recovery audit v1 — APPROVED (`a09380d`)

## Structure

| Path | Role |
|------|------|
| `taxonomy/` | Controlled vocabularies |
| `schemas/` | Canonical semantic record schema |
| `contracts/` | Record invariants |
| `validation/` | Taxonomy and schema validation |
| `fixtures/` | Schema shape tests only — not gold labels |
| `decisions/` | P0-B decision and operator approval records |
| `annotation/` | P0-C annotation guideline — **APPROVED — CHECKPOINTED** (`78b0557`) |
| `integration/` | **P0-I admission integration — APPROVED — CHECKPOINTED** |
| `benchmark/` | P0-D benchmark charter — **ON HOLD UNTIL P0-I PASS** |

## Gates

| Item | Status |
|------|--------|
| P0-A ADR | APPROVED — CHECKPOINTED |
| P0-B Taxonomy & Schema | APPROVED — CHECKPOINTED (`3151953`) |
| P0-C Annotation Guideline | APPROVED — CHECKPOINTED (`78b0557`) |
| Capability recovery audit v1 | APPROVED — CHECKPOINTED (`a09380d`) |
| **P0-I Integration Charter** | **APPROVED — CHECKPOINTED** |
| P0-D Benchmark Charter | ON HOLD UNTIL P0-I PASS |
| B0 | BLOCKED |
| P0-E Corvonero Pilot | BLOCKED |
| Benchmark rows / gold labels | NOT CREATED |
| Classifier | NOT STARTED |
| Corvonero | FROZEN |
| Campaign production | BLOCKED |

## Reading order

1. P0-B taxonomy and schema
2. P0-C annotation locus — [`annotation/README.md`](annotation/README.md)
3. P0-I integration locus — [`integration/README.md`](integration/README.md)
4. P0-D benchmark locus — [`benchmark/README.md`](benchmark/README.md) (on hold)
