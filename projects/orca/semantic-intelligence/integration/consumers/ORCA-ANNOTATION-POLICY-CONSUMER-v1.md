# ORCA Annotation Policy Consumer v1

**Consumer ID:** `orca-annotation-policy-consumer-v1`  
**Primary contract:** P0-C annotation guideline family

---

## Input paths

| Contract | Path |
|----------|------|
| Master guideline | `semantic-intelligence/annotation/guidelines/orca-semantic-annotation-guideline-v1.json` |
| ACCEPT standard | `semantic-intelligence/annotation/guidelines/ORCA-ACCEPT-STANDARD-v1.md` |
| REJECT standard | `semantic-intelligence/annotation/guidelines/ORCA-REJECT-STANDARD-v1.md` |
| ABSTAIN standard | `semantic-intelligence/annotation/guidelines/ORCA-ABSTAIN-STANDARD-v1.md` |
| Commercial evidence | `semantic-intelligence/annotation/guidelines/ORCA-COMMERCIAL-EVIDENCE-STANDARD-v1.md` |
| Protected non-commercial | `semantic-intelligence/annotation/guidelines/ORCA-PROTECTED-NONCOMMERCIAL-INTENT-STANDARD-v1.md` |
| Short-head adjudication | `semantic-intelligence/annotation/guidelines/ORCA-SHORT-HEAD-TERM-ADJUDICATION-v1.md` |
| Problem-query adjudication | `semantic-intelligence/annotation/guidelines/ORCA-PROBLEM-QUERY-ADJUDICATION-v1.md` |
| Product vs service | `semantic-intelligence/annotation/guidelines/ORCA-PRODUCT-VS-SERVICE-ADJUDICATION-v1.md` |

## Supported versions

`v1` per guideline manifest.

## Required fields consumed

- Decision semantics: ACCEPT requires positive commercial evidence
- ABSTAIN mandatory conditions (ambiguity, conflict)
- REJECT reason families
- Protected strata rules (career, edu, DIY, download, navigational)

## Output

- `commercial_eligibility.decision` ∈ `{ACCEPT, REJECT, ABSTAIN}`
- `commercial_eligibility.reason_code`
- `signals` with strength tiers
- `supporting_evidence` / `opposing_evidence` arrays
- `review.reviewer_required` flag

## Blocking conditions

- Decision outside tri-state → `SI-ANN-001`
- ACCEPT without commercial evidence signal → `SI-ANN-002`
- REJECT without reason_code → `SI-ANN-003`
- ABSTAIN without unresolved question → `SI-ANN-004`

## Error behavior

BLOCKING — invalid decision cannot proceed to invariant validator as PASS.

## Audit trace

`audit.policy_applied[]`: `{policy_id, version, rules_triggered[]}`.

## Fallback behavior

On rule/model disagreement → **ABSTAIN** + human review route — never legacy `HOLD` or `ELIGIBLE NARROW`.
