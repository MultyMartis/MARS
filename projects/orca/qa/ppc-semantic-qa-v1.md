# PPC Semantic QA v1

## Purpose

Defines QA checks for PPC semantics before campaign architecture, export, or human platform use.

## Checks

- Intent purity per cluster.
- Geo purity and service coverage.
- Commercial purity and informational leakage.
- Duplicate intent across clusters.
- Broad match danger from vague phrases.
- B2B/B2C audience conflict.
- Competitor and branded query separation.
- Negative keyword coverage.
- Landing page availability.

## Severity

- Blocker - likely to waste spend, violate offer scope, or break campaign structure.
- Warning - usable only after human decision.
- Note - context for later copy, landing, or export review.

## Human Checkpoints

- Approve ambiguous terms.
- Accept or reject negative keyword candidates.
- Confirm region and service coverage.
- Confirm whether mixed intent is allowed.

## Output

- Semantic QA report.
- Blockers and warnings.
- Duplicate map.
- SAFE UNKNOWN list.
- Human action list.

## Boundary

Semantic QA supports quality over automation. It does not upload keywords, choose bids, operate runtime checks, or optimize live campaigns.
