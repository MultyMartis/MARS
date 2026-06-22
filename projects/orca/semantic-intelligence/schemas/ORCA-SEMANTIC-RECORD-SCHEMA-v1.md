# ORCA Semantic Record Schema v1

**Schema ID:** `orca-semantic-record-schema`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**JSON Schema draft:** 2020-12  
**Machine schema:** [`orca-semantic-record-schema-v1.schema.json`](orca-semantic-record-schema-v1.schema.json)  
**Manifest:** [`orca-semantic-record-schema-v1.json`](orca-semantic-record-schema-v1.json)

---

## Purpose

Canonical **semantic record** per query phrase for ORCA Semantic Intelligence v1. Implementation-neutral; validates shape and enums, not classifier accuracy.

---

## Required top-level fields

| Field | Type | Description |
|-------|------|-------------|
| `query_id` | string | Stable phrase identifier |
| `record_version` | string | Semantic version of this record (semver) |
| `schema_version` | string | Const `v1` |
| `created_at` | date-time | ISO 8601 creation |
| `updated_at` | date-time | ISO 8601 last update |
| `raw_query` | string (minLength 1) | Immutable source phrase |
| `normalized_query` | string | Normalized form |
| `language` | string | e.g. `ru`, `en` |
| `source_type` | string | Corpus source class |
| `provenance_status` | enum | COMPLETE / PARTIAL / MISSING / UNKNOWN |
| `literal_interpretation` | string | Literal reading before commercial inference |
| `likely_user_goal` | string | goal_id from user-goal taxonomy |
| `primary_intent` | string | intent_id from primary-intent taxonomy |
| `signals` | array | Signal records (see signal taxonomy) |
| `ambiguity` | object | types[], severity, competing_interpretations, unresolved_questions |
| `commercial_eligibility` | object | decision, reason_code, confidence, reviewer_required, … |
| `risk` | object | overall_risk, dimensions, blocking_conditions |
| `service_candidate` | object | mapping_status (NOT_STARTED / CANDIDATE_ONLY only pre-core) |
| `review` | object | workflow_status + review metadata |
| `versioning` | object | taxonomy, rule, model, prompt versions |
| `audit` | object | lineage, overrides, supersession refs |

---

## Optional top-level fields

| Field | Type | Description |
|-------|------|-------------|
| `source_ids` | string[] | Source corpus identifiers |
| `source_rows` | integer[] | Row numbers in source extract |
| `frequency_evidence` | object \| null | Frequency stats if available |
| `secondary_intents` | string[] | Competing intent_ids |
| `entities` | string[] | Extracted entities |
| `actions` | string[] | Extracted actions |
| `objects` | string[] | Extracted objects |
| `problems` | string[] | Extracted problems |
| `desired_outcomes` | string[] | Extracted outcomes |
| `modifiers` | string[] | Modifiers |
| `geography` | string \| null | Geo token |
| `product_or_module` | string \| null | Product reference |
| `configuration_or_version` | string \| null | Version/config reference |
| `industry_context` | string \| null | Industry hint |

---

## Nested object summaries

### ambiguity

| Field | Required | Notes |
|-------|----------|-------|
| `types` | yes | Array of ambiguity type enums |
| `severity` | yes | LOW / MEDIUM / HIGH / CRITICAL |
| `competing_interpretations` | no | Human-readable hypotheses |
| `unresolved_questions` | conditional | Required min 1 when decision=ABSTAIN |

### commercial_eligibility

See [`ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md`](../taxonomy/ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md).

### risk

| Field | Required |
|-------|----------|
| `overall_risk` | yes |
| `dimensions` | recommended |
| `blocking_conditions` | recommended |

### service_candidate

Pre-ACCEPT only **candidate** mapping — not final service ownership (invariant 9).

| Field | Required |
|-------|----------|
| `mapping_status` | yes |
| `candidate_service_ids` | optional |
| `mapping_confidence` | optional |
| `mapping_conflicts` | optional |

### versioning (recommended keys)

`taxonomy_version`, `rule_version`, `model_version`, `prompt_version`, `guideline_version`

### audit (recommended keys)

`prior_decision`, `override_reason`, `superseded_by`, `decision_trace_id`

---

## Forbidden fields

Schema `not` constraint forbids top-level:

- `campaign_group`
- `export_fields`
- `cluster_id`
- `ad_group`

Campaign structure is downstream; SI record is semantic-only (invariants 10–11).

---

## Validation

- JSON Schema validation against `orca-semantic-record-schema-v1.schema.json`
- Invariant checks per [`ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md`](../contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md)
- Fixtures in `fixtures/valid` and `fixtures/invalid`

---

## Related documents

- [`ORCA-SEMANTIC-NULL-UNKNOWN-POLICY-v1.md`](ORCA-SEMANTIC-NULL-UNKNOWN-POLICY-v1.md)
- [`ORCA-SEMANTIC-DECISION-TRACE-v1.md`](ORCA-SEMANTIC-DECISION-TRACE-v1.md)
