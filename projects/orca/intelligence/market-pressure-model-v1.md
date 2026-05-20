# Market Pressure Model v1

## Purpose

Classifies visible PPC market pressure in ORCA pilot cases. The model helps operators compare commercial environments while preserving context, uncertainty, and human review.

## Pressure Classes

## Aggregator Pressure

Measures visible influence of aggregators, marketplaces, directories, or lead platforms.

- `low` - few or no aggregators visible.
- `medium` - aggregators appear but do not dominate.
- `high` - aggregators occupy strong ad or organic positions.
- `critical` - aggregators dominate visible paths and may displace local providers.

## CPC Aggression

Research proxy for visible ad competition. This does not infer actual CPC, bids, budgets, or auction strategy.

- `low` - sparse ads or weak commercial messaging.
- `medium` - consistent ads for core queries.
- `high` - dense ads with aggressive offers and repeated competitors.
- `critical` - heavy ad density across urgent, local, and price-modified queries.

## Local Competition Density

Measures visible local provider competition.

- `low` - few local providers visible.
- `medium` - several local providers appear.
- `high` - many local providers compete across ads, local pack, and organic.
- `critical` - local provider density creates strong differentiation pressure.

## Trust Sensitivity

Measures how much visible evidence suggests trust proof matters.

- `low` - few trust signals visible.
- `medium` - some reviews, guarantees, or proof points visible.
- `high` - trust signals are common among visible competitors.
- `critical` - reviews, ratings, licenses, guarantees, or proof dominate commercial messaging.

## Urgency Pressure

Measures visible urgency claims and time-sensitive intent.

- `low` - little urgency language.
- `medium` - occasional fast-response claims.
- `high` - same-day, emergency, or immediate-response messaging is common.
- `critical` - urgency appears central to the niche or query set.

## Price Sensitivity

Measures visible price framing.

- `low` - price rarely shown.
- `medium` - some price-from or estimate messaging.
- `high` - price claims are common.
- `critical` - price dominates visible differentiation.

## Brand Dominance

Measures visible role of recognized brands.

- `low` - fragmented market.
- `medium` - some known brands visible.
- `high` - brands frequently occupy strong positions.
- `critical` - brand visibility may strongly shape user trust and click behavior.

## Local Pack Dominance

Measures importance of map/local results.

- `low` - local pack absent or weak.
- `medium` - local pack appears but does not dominate.
- `high` - local pack is prominent for core queries.
- `critical` - local pack visibility appears central to user path.

## Scoring Rules

- Score only visible evidence.
- Attach region, niche, device, query set, and date.
- Use SAFE UNKNOWN for missing evidence.
- Do not infer hidden auction metrics.
- Do not convert scores into automatic budget, bid, or campaign decisions.
- Require human review before using pressure classes in strategy.

## Output Format

```yaml
market_pressure:
  region:
  niche:
  device:
  observation_date:
  aggregator_pressure:
  cpc_aggression:
  local_competition_density:
  trust_sensitivity:
  urgency_pressure:
  price_sensitivity:
  brand_dominance:
  local_pack_dominance:
  confidence_level:
  safe_unknown:
```

## Boundary

This model supports research comparison and pilot intelligence. It is not live optimization, market forecasting, bidding automation, or autonomous advertising strategy.
