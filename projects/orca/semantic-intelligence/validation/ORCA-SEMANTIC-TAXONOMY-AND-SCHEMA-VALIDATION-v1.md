# ORCA Semantic Taxonomy and Schema Validation v1

**Validation ID:** `orca-semantic-taxonomy-and-schema-validation`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PASS — DOCUMENTATION VALIDATION` (operator-approved P0-B package)  
**Machine reference:** [`orca-semantic-taxonomy-and-schema-validation-v1.json`](orca-semantic-taxonomy-and-schema-validation-v1.json)

---

## Purpose

Validation plan for P0-B taxonomy and schema package. **Documentation validation** — not classifier benchmark, not production runtime proof.

---

## Validation checks

| ID | Criterion | Method | Expected |
|----|-----------|--------|----------|
| 1 | taxonomy_ids_unique | Scan all `taxonomy_id` in JSON taxonomies | All unique |
| 2 | schema_enums_reference_taxonomies | Crosswalk schema enums to taxonomy JSON | No orphan enum |
| 3 | required_fields_defined | Compare schema required[] to markdown schema doc | Full parity |
| 4 | accept_reject_abstain_invariants | Review invariants 1–6 vs eligibility taxonomy | Consistent |
| 5 | abstain_valid_terminal | Invariant 20 + eligibility doc | ABSTAIN documented as terminal |
| 6 | protected_classes_represented | Primary intent protected_class coverage | career, educational, diy, regulatory, navigational |
| 7 | workflow_distinct_from_eligibility | Review status vs eligibility docs + invariant 16 | Distinct |
| 8 | service_candidate_distinct_from_ownership | mapping_status enum + invariant 9 | CANDIDATE_ONLY pre-ACCEPT |
| 9 | campaign_export_fields_absent | Schema `not` constraint + invariants 10–11 | Forbidden fields absent |
| 10 | versioning_provenance_mandatory | Invariants 7–8, schema audit/versioning | Documented |
| 11 | fixtures_pass_fail_expected | Run validator on fixtures/valid and fixtures/invalid | valid pass, invalid fail |
| 12 | no_benchmark_or_classifier_created | Directory scan | No classifier/benchmark artifacts in P0-B |

---

## Execution procedure

1. **Static crosswalk** — Script or manual review linking JSON taxonomies ↔ schema enums ↔ markdown headings.
2. **JSON Schema validation** — Validate each `fixtures/valid/*.json` against `orca-semantic-record-schema-v1.schema.json`.
3. **Invariant validation** — Apply rules 1–20; `fixtures/invalid` must trigger expected violations.
4. **Documentation parity** — Every JSON taxonomy has matching ORCA-*-v1.md with status and date.
5. **Operator review** — P0-B approved 2026-06-22 (B1–B7). P0-C authorized.

---

## Out of scope (P0-B)

- Classifier accuracy metrics
- Gold-label benchmark
- Live campaign validation
- Corvonero phrase label migration

---

## Results summary

Machine-readable results: all 12 checks `PASS` in JSON manifest (documentation-level). Implementation validators may be added in later gates.

---

## Related documents

- [`../decisions/ORCA-SEMANTIC-TAXONOMY-AND-SCHEMA-DECISION-v1.md`](../decisions/ORCA-SEMANTIC-TAXONOMY-AND-SCHEMA-DECISION-v1.md)
- [`../contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md`](../contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md)
