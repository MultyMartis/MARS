# Strategic Heuristics Model v1

## Purpose

Defines the standard record model for ORCA strategic PPC heuristics. A heuristic is a reusable, evidence-backed guidance pattern for human review, not an automatic decision rule.

## Required Fields

```yaml
heuristic_id:
heuristic_name:
strategic_intent:
operational_rationale:
evidence_basis:
applicable_niches:
applicable_regions:
device_scope:
time_scope:
confidence_level:
evidence_freshness:
contradiction_sensitivity:
volatility:
expiration_review:
human_reviewer:
safe_unknown:
```

## Field Meanings

- `heuristic_id` - stable identifier for reference and contradiction tracking.
- `evidence_basis` - repeated observations, pilot findings, or validated pattern references.
- `applicable_niches` - niches where use is supported.
- `applicable_regions` - regions where evidence has been validated.
- `confidence_level` - current human-reviewed confidence.
- `contradiction_sensitivity` - how strongly conflicting evidence should limit use.
- `volatility` - expected instability from SERP, season, region, or competitor behavior.
- `expiration_review` - date or trigger for reassessment.
- `strategic_intent` - what decision area the heuristic informs.
- `operational_rationale` - why the heuristic may help in that context.
- `evidence_freshness` - age and relevance of supporting evidence.

## Interpretation Rules

- A heuristic is contextual, not universal.
- Human review is required before applying it to campaign strategy.
- Region, niche, device, time, and evidence freshness must be checked.
- Contradictory heuristics may coexist.
- Confidence can degrade as evidence ages.
- A heuristic cannot override missing evidence.

## Boundary

This model documents strategic guidance records. It is not a strategy generator, optimization engine, runtime scoring model, bidding system, or autonomous campaign decision system.
