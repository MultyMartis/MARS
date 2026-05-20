# Observation Model v1

## Purpose

Standardizes how ORCA pilot cases record PPC research observations. The model keeps observation, interpretation, confidence, and strategic importance separate so that findings can accumulate without becoming automatic market conclusions.

## Required Fields

- `observation_id` - stable local identifier.
- `case_id` - pilot case source.
- `observation_type` - SERP, semantic, landing, CTA, trust, offer, aggregator, local pack, competitor, QA, regional commercial.
- `source` - SERP snapshot, landing page review, competitor page, local pack, operator note, client input, or SAFE UNKNOWN.
- `region` - city, oblast, country, or configured ad region.
- `niche` - service or market category.
- `device` - desktop, mobile, mixed, or SAFE UNKNOWN.
- `timestamp` - observation date and time when available.
- `finding` - concise factual observation.
- `interpretation` - human-reviewed meaning, if any.
- `confidence_level` - LOW, MEDIUM, HIGH, VERY HIGH.
- `evidence_strength` - weak, moderate, strong.
- `repeatability` - single, repeated, cross-query, cross-region, historical.
- `volatility` - low, medium, high, unknown.
- `recency` - current, recent, stale, unknown.
- `strategic_importance` - low, medium, high, critical.
- `safe_unknown` - missing or uncertain evidence.

## Observation Types

- `SERP` - ad blocks, organic results, local pack, aggregator visibility.
- `SEMANTIC` - query intent, ambiguity, negative candidates, local modifiers.
- `LANDING` - landing fit, page type, proof, friction, service match.
- `CTA` - call, form, booking, calculation, messenger, consultation.
- `TRUST` - reviews, guarantees, licenses, local proof, reputation cues.
- `OFFER` - price, urgency, guarantee, discount, bundle, financing.
- `AGGREGATOR` - marketplace or service aggregator pressure.
- `LOCAL_PACK` - maps/local result dominance and review density.
- `COMPETITOR` - visible positioning and message patterns.
- `QA` - completeness, mismatch, unsupported assumption, policy risk.
- `REGIONAL_COMMERCIAL` - region-specific pressure or behavior.

## Rules

- Record what was observed before explaining what it may mean.
- Treat SERP evidence as time-bound and region-bound.
- Do not infer budgets, bids, conversion rates, or account strategy.
- Do not convert observations into automatic optimizations.
- Human validation is required before reuse in strategy or campaign architecture.
- Use SAFE UNKNOWN when evidence is missing or unstable.

## Example

```yaml
observation_id: obs-001
case_id: local-cleaning-spb-001
observation_type: AGGREGATOR
source: SERP snapshot
region: Saint Petersburg
niche: apartment cleaning
device: mobile
timestamp: 2026-05-18T15:55:00+07:00
finding: Two service aggregators appear above most local provider organic results for urgent cleaning queries.
interpretation: Aggregator pressure may affect local provider visibility for urgent mobile searches.
confidence_level: MEDIUM
evidence_strength: moderate
repeatability: cross-query
volatility: medium
recency: current
strategic_importance: high
safe_unknown:
  - personalization influence
  - exact ad auction dynamics
```
