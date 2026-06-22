# Bounded QA Framework v1

**Wave 3 quality evaluation without mass operator labeling**

## Strata

| Stratum | Source | Role |
|---------|--------|------|
| Hard-negative fixtures | `fixtures/regression-corpus-v1.json` | Deterministic REJECT/ABSTAIN |
| Positive commercial fixtures | regression corpus + scale corpus | ACCEPT path |
| Adversarial pairs | regression corpus career/DIY/product families | Disambiguation |
| Protected-intent strata | hard-rules + assessor | Block false ACCEPT |
| Corvonero diagnostic failures | REG-012 etc. | Anti-pattern regression |
| Triumph structures | REG-011 (where valid) | Example only — not gold truth |
| Random QA sample | review-router 2% default | Bounded operator spot-check |
| Model disagreement | reassessment + adjudication | Automated — no operator labeling |

## Operator review package focus

- Systemic error families (not row-by-row corpus)
- Small high-risk samples (escalations, ownership conflicts)
- Policy choices (topical vs commercial)
- Domain conflicts (protected strata)

## Not claimed

Quality from completion rate alone. Production accuracy requires Wave 3.1 live model validation.
