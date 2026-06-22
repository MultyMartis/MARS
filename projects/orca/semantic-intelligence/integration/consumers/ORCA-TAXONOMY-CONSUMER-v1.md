# ORCA Taxonomy Consumer v1

**Consumer ID:** `orca-taxonomy-consumer-v1`  
**Primary contracts:** P0-B taxonomy JSON family

---

## Input paths

| Contract | Path |
|----------|------|
| Primary intent | `semantic-intelligence/taxonomy/orca-primary-intent-taxonomy-v1.json` |
| User goal | `semantic-intelligence/taxonomy/orca-user-goal-taxonomy-v1.json` |
| Signal | `semantic-intelligence/taxonomy/orca-semantic-signal-taxonomy-v1.json` |
| Commercial eligibility | `semantic-intelligence/taxonomy/orca-commercial-eligibility-taxonomy-v1.json` |
| Ambiguity | `semantic-intelligence/taxonomy/orca-ambiguity-taxonomy-v1.json` |
| Risk | `semantic-intelligence/taxonomy/orca-semantic-risk-taxonomy-v1.json` |
| Review status | `semantic-intelligence/taxonomy/orca-semantic-review-status-v1.json` |

## Supported versions

`v1` only. Manifest checksum required.

## Required fields consumed

- `intent_id`, `goal_id`, `signal_type`, `strength`, `eligibility_decision`, `ambiguity_type`, `risk_dimension`, `review_status` enums

## Output

- Validated enum assignments on semantic record
- `versioning.taxonomy_*` populated per taxonomy file version

## Blocking conditions

- Unknown `primary_intent` or `likely_user_goal` ID → `SI-TAX-001`
- Signal type/strength not in taxonomy → `SI-TAX-002`
- Eligibility decision not in `{ACCEPT, REJECT, ABSTAIN}` → `SI-TAX-003`

## Error behavior

FATAL — pipeline cannot assess intent without taxonomy load.

## Audit trace

`audit.contracts_loaded[]` entry per taxonomy file: `{contract_id, version, checksum, loaded_at}`.

## Fallback behavior

**None.** Missing taxonomy → `BLOCKED — REQUIRED SEMANTIC CONTRACT NOT LOADED`.
