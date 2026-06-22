# ORCA Risk Mode Consumer v1

**Consumer ID:** `orca-risk-mode-consumer-v1`  
**Primary contract:** P0-A admission policy and risk taxonomies

---

## Input paths

| Contract | Path |
|----------|------|
| Admission policy | `architecture/semantic-intelligence/orca-semantic-admission-policy-v1.json` |
| Risk taxonomy | `semantic-intelligence/taxonomy/orca-semantic-risk-taxonomy-v1.json` |
| Quality gates | `architecture/semantic-intelligence/orca-semantic-intelligence-quality-gates-v1.json` |

## Supported versions

`v1`; Corvonero initial mode: `CONSERVATIVE` (ADR A4).

## Required fields consumed

- `risk_mode`: `CONSERVATIVE` | `BALANCED` | `EXPLORATORY`
- Threshold tables per mode
- Auto-ACCEPT prohibition under CONSERVATIVE for HIGH/CRITICAL ambiguity

## Output

- `risk.overall_risk`, `risk.dimensions[]`, `risk.blocking_conditions[]`
- `commercial_eligibility.confidence` capped per mode
- Elevated review requirement flags

## Blocking conditions

- ACCEPT under CONSERVATIVE with confidence below threshold → `SI-RISK-001`
- ACCEPT with `overall_risk: CRITICAL` → `SI-RISK-002`
- Missing risk_mode in run context → `SI-RISK-003`

## Error behavior

BLOCKING for threshold violations; routes to human review when borderline per mode.

## Audit trace

`audit.risk_mode`: `{mode, thresholds_version, checks[]}`.

## Fallback behavior

Default to `CONSERVATIVE` if mode unspecified in pilot — log warning `SI-RISK-WARN-001`. No downgrade to legacy regex confidence.
