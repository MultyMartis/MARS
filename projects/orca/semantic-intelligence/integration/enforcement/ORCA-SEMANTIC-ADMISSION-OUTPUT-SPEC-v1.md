# ORCA Semantic Admission Output Specification v1

**Spec ID:** `orca-semantic-admission-output-v1`  
**Date:** 2026-06-22

---

## Permitted automated admission values

Only these values may appear in `commercial_eligibility.decision` as **semantic authority**:

| Value | Required companion fields |
|-------|---------------------------|
| `ACCEPT` | positive commercial evidence, reason_code, confidence, risk assessment |
| `REJECT` | reason_code from reject families, opposing evidence |
| `ABSTAIN` | unresolved_questions ≥ 1, ambiguity severity, review_required=true |

---

## Required record fields (admission output)

Every automated admission record must contain:

| Field | Source |
|-------|--------|
| `literal_interpretation` | Query understanding |
| `likely_user_goal` | Taxonomy consumer |
| `primary_intent` | Taxonomy consumer |
| `signals[]` | Annotation policy + signal taxonomy |
| `supporting_evidence[]` | Commercial evidence standard |
| `opposing_evidence[]` | Conflict detection |
| `ambiguity` | Ambiguity taxonomy |
| `commercial_eligibility.decision` | Tri-state only |
| `commercial_eligibility.reason_code` | Taxonomy |
| `commercial_eligibility.confidence` | Risk mode consumer |
| `risk` | Risk taxonomy + mode |
| `review.reviewer_required` | Router input |
| `versioning` | All contract versions consumed |
| `assessor_versions` | Orchestrator, ruleset, validator versions |
| `provenance_status` | COMPLETE / PARTIAL — not MISSING for auto decision |
| `audit` | Full trace |

---

## Forbidden authority values

Must **not** appear as final `commercial_eligibility.decision` or equivalent authority field:

- `ELIGIBLE COMMERCIAL`
- `NOT ELIGIBLE — *`
- `HOLD — AMBIGUOUS`
- `NEEDS OPERATOR REVIEW` (as decision substitute)
- Provisional intent classes from legacy regex (`COMMERCIAL SERVICE`, `CAREER/EMPLOYMENT`, etc.)

### Diagnostic comparison only

Legacy values permitted in:

```json
"diagnostic_comparison": {
  "legacy_intent_class": "...",
  "legacy_eligibility_decision": "...",
  "legacy_service_map": []
}
```

---

## Pre-ownership constraints

At admission output:

- `service_candidate.mapping_status` ∈ `{NOT_STARTED, CANDIDATE_ONLY}`
- No `cluster_id`, `negative_keyword_id`, `campaign_id`, `export_row_id`
- No numeric narrative placeholders in `literal_interpretation` or `reason` text

---

## Silent rewrite prohibition

Malformed phrases must retain `raw_query` unchanged. Normalization metadata in dedicated fields — no silent semantic repair.
