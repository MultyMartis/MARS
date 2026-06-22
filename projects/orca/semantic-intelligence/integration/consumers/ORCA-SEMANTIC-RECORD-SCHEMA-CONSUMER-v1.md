# ORCA Semantic Record Schema Consumer v1

**Consumer ID:** `orca-semantic-record-schema-consumer-v1`  
**Primary contract:** P0-B semantic record JSON Schema

---

## Input paths

| Contract | Path |
|----------|------|
| Record schema | `semantic-intelligence/schemas/orca-semantic-record-schema-v1.schema.json` |
| Schema manifest | `semantic-intelligence/schemas/orca-semantic-record-schema-v1.json` |
| Decision trace schema | `semantic-intelligence/schemas/orca-semantic-decision-trace-v1.schema.json` |

## Supported versions

`schema_version: v1`, `record_version` semver per manifest.

## Required fields consumed

All required top-level fields per `ORCA-SEMANTIC-RECORD-SCHEMA-v1.md`: `query_id`, `raw_query`, `normalized_query`, `literal_interpretation`, `likely_user_goal`, `primary_intent`, `signals`, `ambiguity`, `commercial_eligibility`, `risk`, `provenance_status`, `versioning`, `audit`.

## Output

- Schema-valid semantic record JSON per phrase
- Validation report with field-level errors

## Blocking conditions

- Record fails JSON Schema validation → `SI-SCH-001`
- Missing required admission field → `SI-SCH-002`
- Forbidden downstream fields present (`cluster_id`, `campaign_id`, `service_owner_final`) → `SI-SCH-003`

## Error behavior

FATAL for required field absence. BLOCKING for shape violations.

## Audit trace

`audit.schema_validation`: `{schema_id, schema_version, checksum, pass, errors[]}`.

## Fallback behavior

**None.** No silent field dropping or auto-fill of narrative placeholders.
