# ORCA Semantic Taxonomy and Schema Decision v1

**Decision ID:** `orca-semantic-taxonomy-and-schema-decision`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `APPROVED — IMPLEMENTATION NOT STARTED`  
**Machine reference:** [`orca-semantic-taxonomy-and-schema-decision-v1.json`](orca-semantic-taxonomy-and-schema-decision-v1.json)

---

## Decision summary

Operator-approved P0-B **implementation-neutral** semantic taxonomy and record schema package for ORCA Semantic Intelligence v1.

---

## Selected models

| Area | Selection |
|------|-----------|
| Taxonomy architecture | Multi-axis: intent + goal + signal + ambiguity + eligibility + risk + workflow |
| Intent granularity | 27 primary intents (commercial, self-service, knowledge, employment, quality) |
| Signal model | 31 typed signals with NONE–EXPLICIT strength and evidence spans |
| Eligibility model | ACCEPT / REJECT / ABSTAIN with reason code families |
| Ambiguity model | 13 ambiguity types with severity; mandatory ABSTAIN rules |
| Risk model | 12 dimensions; overall = max(dimension) unless blocking |
| Workflow model | 11 workflow statuses separate from eligibility |
| Schema approach | JSON Schema draft 2020-12 + 20 invariants + decision trace |
| Null policy | Explicit unknown vs null vs not assessed; forbidden sentinels |

---

## Unresolved decisions (defer to P0-C and later)

| ID | Topic | Notes |
|----|-------|-------|
| U-01 | Annotation guideline binding | P0-C authorized — operator approval of guideline pending |
| U-02 | Threshold profiles numeric values | CONSERVATIVE vs STANDARD cutoffs |
| U-03 | Assessor disagreement resolution SLA | Adjudication workflow timing |
| U-04 | Service catalog binding format | candidate_service_ids authority |
| U-05 | Automated validator implementation | Human doc validation only in P0-B |
| U-06 | LLM prompt authority boundaries | Evidence-only vs label authority |
| U-07 | Operator seed validation workflow | VALIDATED_OPERATOR_SEED governance |

---

## Consequences

1. **Corvonero legacy labels** are not taxonomy authority; new records use ORCA v1 vocabularies only.
2. **Fixtures** validate shape — not gold labels for benchmark.
3. **Campaign production** remains blocked until Semantic Core approval gates pass.
4. **Classifier and benchmark** are NOT STARTED; no claim of runtime implementation.
5. **ABSTAIN** is normal operations, not failure — reduces false-positive spend risk.
6. **Protected strata** (career, educational, diy, regulatory) require conservative defaults.

---

## Next gate

**P0-C — Annotation Guideline** — authorized per B7; operator approval of drafted guideline required before P0-D.

Deliverables: annotator handbook, edge-case playbook, disagreement protocol, binding to this taxonomy.

---

## Approval record

| Role | Name | Date | Status |
|------|------|------|--------|
| Operator | Approved | 2026-06-22 | APPROVED — IMPLEMENTATION NOT STARTED |
| Architecture | ADR v1 | 2026-06-22 | APPROVED |
| P0-B package | This decision | 2026-06-22 | APPROVED — IMPLEMENTATION NOT STARTED |
| P0-B operator record | B1–B7 | 2026-06-22 | [`ORCA-P0-B-TAXONOMY-AND-SCHEMA-OPERATOR-APPROVAL-v1.md`](ORCA-P0-B-TAXONOMY-AND-SCHEMA-OPERATOR-APPROVAL-v1.md) |

---

## Related documents

- [`../README.md`](../README.md)
- [`../taxonomy/ORCA-SEMANTIC-TAXONOMY-PRINCIPLES-v1.md`](../taxonomy/ORCA-SEMANTIC-TAXONOMY-PRINCIPLES-v1.md)
- [`../validation/ORCA-SEMANTIC-TAXONOMY-AND-SCHEMA-VALIDATION-v1.md`](../validation/ORCA-SEMANTIC-TAXONOMY-AND-SCHEMA-VALIDATION-v1.md)
