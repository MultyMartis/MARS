# ORCA Semantic Intelligence — Implementation-Neutral Specification Locus

**Locus:** `projects/orca/semantic-intelligence/`  
**Status:** `P0-B — SEMANTIC TAXONOMY AND RECORD SCHEMA`  
**Package status:** `APPROVED — IMPLEMENTATION NOT STARTED`  
**Checkpoint:** selective commit after operator approval B1–B7

Implementation-neutral semantic specification for ORCA Semantic Intelligence v1. Not runtime. Not classifier. Not benchmark.

## Authority

- Approved ADR v1 (`projects/orca/architecture/semantic-intelligence/`)
- Operator approval A1–A7
- Operator decisions D1–D7
- Operator approval B1–B7 ([`decisions/ORCA-P0-B-TAXONOMY-AND-SCHEMA-OPERATOR-APPROVAL-v1.md`](decisions/ORCA-P0-B-TAXONOMY-AND-SCHEMA-OPERATOR-APPROVAL-v1.md))

## Structure

| Path | Role |
|------|------|
| `taxonomy/` | Controlled vocabularies — intent, goal, signal, ambiguity, eligibility, risk, review |
| `schemas/` | Canonical semantic record schema, null policy, decision trace |
| `contracts/` | Record invariants |
| `validation/` | Taxonomy and schema validation plan |
| `fixtures/` | Schema shape and invariant test cases only — not gold labels |
| `decisions/` | P0-B decision and operator approval records |
| `reports/` | Task reports |

## Gates

| Item | Status |
|------|--------|
| P0-A ADR | APPROVED — CHECKPOINTED |
| P0-B Taxonomy & Schema | APPROVED — CHECKPOINTED |
| P0-C Annotation Guideline | AUTHORIZED (B7) — drafting in progress |
| Classifier | NOT STARTED |
| Benchmark | NOT STARTED |
| Corvonero | FROZEN |
| Campaign production | BLOCKED |

## Reading order

1. Taxonomy principles
2. Primary intent taxonomy
3. User goal taxonomy
4. Signal taxonomy
5. Ambiguity taxonomy
6. Commercial eligibility taxonomy
7. Risk taxonomy
8. Review status taxonomy
9. Semantic record schema
10. Null/unknown policy
11. Invariants
12. Decision trace model
13. Fixtures
14. Validation plan
15. P0-B decision record
16. P0-B operator approval record (B1–B7)
