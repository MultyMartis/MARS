# Evidence Discipline Model v1

## Purpose

Defines how ORCA records, qualifies, and reuses commercial research evidence. The discipline prevents observations from becoming unsupported market truth, synthetic intelligence, or automatic strategy.

ORCA observes reality. ORCA does not define reality. Every conclusion remains human-supervised, contextual, revisable, and limited by the evidence that produced it.

## Evidence Record Fields

- `evidence_id` - stable local identifier.
- `evidence_source` - SERP snapshot, landing review, competitor page, local pack review, client input, operator note, or SAFE UNKNOWN.
- `observation_timestamp` - date and time of observation when available.
- `region` - city, oblast, country, configured ad region, or SAFE UNKNOWN.
- `niche` - service, product, or market category.
- `serp_conditions` - query set, search engine, visible ads, local pack, aggregators, personalization risk, and layout notes.
- `device_context` - desktop, mobile, mixed, or SAFE UNKNOWN.
- `repeatability` - isolated, repeated, cross-query, cross-case, cross-region, historical.
- `volatility` - low, medium, high, or unknown.
- `confidence` - LOW, MEDIUM, HIGH, VERY HIGH.
- `human_reviewer` - person or role that reviewed the evidence.
- `evidence_freshness` - current, recent, stale, expired, or unknown.
- `strategic_impact` - low, medium, high, critical, or SAFE UNKNOWN.
- `contradictions` - linked contradictory or limiting observations.
- `safe_unknown` - missing, unstable, or unverifiable context.

## Discipline Rules

- Record visible evidence before interpretation.
- Treat every observation as time-bound, region-bound, niche-bound, and device-aware.
- Keep observation, interpretation, confidence, and strategic impact separate.
- Repeated evidence increases reliability only when observations are comparable.
- Contradictory evidence must be preserved and linked.
- Unsupported abstractions are forbidden.
- SERP volatility, regional uncertainty, seasonality, and evidence aging reduce confidence.
- Human validation is required before evidence informs campaign architecture, offer framing, or commercial conclusions.

## Forbidden Uses

- Do not present observations as absolute market truth.
- Do not infer hidden CPC, budgets, bids, conversion rates, or competitor account strategy.
- Do not convert hypotheses into reusable rules without repeated evidence.
- Do not hide unstable findings to make a pattern look stronger.
- Do not claim runtime analytics, telemetry, scraping infrastructure, browser automation, or self-learning intelligence.

## Output Format

```yaml
evidence:
  evidence_id:
  evidence_source:
  observation_timestamp:
  region:
  niche:
  serp_conditions:
  device_context:
  repeatability:
  volatility:
  confidence:
  human_reviewer:
  evidence_freshness:
  strategic_impact:
  contradictions:
  safe_unknown:
```

## Boundary

This model is an evidence discipline for human-supervised commercial research. It is not runtime analytics, telemetry infrastructure, autonomous market intelligence, scraping cloud, browser automation, or a self-learning AI system.
