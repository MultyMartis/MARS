# ORCA Semantic Intelligence — Implementation-Neutral Specification Locus

**Locus:** `projects/orca/semantic-intelligence/`  
**Status:** `P0-C — ANNOTATION GUIDELINE — APPROVED`  
**Package status:** `APPROVED — IMPLEMENTATION NOT STARTED`  
**P0-B checkpoint:** `3151953`

Implementation-neutral semantic specification for ORCA Semantic Intelligence v1. Not runtime. Not classifier. Not benchmark.

## Authority

- Approved ADR v1 (`projects/orca/architecture/semantic-intelligence/`)
- Operator approval A1–A7
- Operator decisions D1–D7
- Operator approval B1–B7 ([`decisions/ORCA-P0-B-TAXONOMY-AND-SCHEMA-OPERATOR-APPROVAL-v1.md`](decisions/ORCA-P0-B-TAXONOMY-AND-SCHEMA-OPERATOR-APPROVAL-v1.md))
- Operator approval C1–C7 ([`annotation/decisions/ORCA-P0-C-ANNOTATION-GUIDELINE-OPERATOR-APPROVAL-v1.md`](annotation/decisions/ORCA-P0-C-ANNOTATION-GUIDELINE-OPERATOR-APPROVAL-v1.md))

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
| `annotation/` | P0-C annotation guideline locus — **APPROVED — IMPLEMENTATION NOT STARTED** |

## Gates

| Item | Status |
|------|--------|
| P0-A ADR | APPROVED — CHECKPOINTED |
| P0-B Taxonomy & Schema | APPROVED — CHECKPOINTED (`3151953`) |
| P0-C Annotation Guideline | APPROVED — IMPLEMENTATION NOT STARTED (C1–C7) |
| P0-D Benchmark Charter | AUTHORIZED — NOT STARTED |
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
17. P0-C annotation locus — [`annotation/README.md`](annotation/README.md)
18. P0-C operator approval record (C1–C7)
