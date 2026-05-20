# Intent Classification System v1

## Purpose

Defines practical PPC intent classes for ORCA semantic work, with emphasis on Yandex.Direct, service businesses, local lead generation, and search-first campaign architecture.

## Intent Classes

- `hot_commercial` - user is ready to contact, order, book, calculate, or buy.
- `warm_commercial` - user is evaluating a service and may convert after trust or price checks.
- `cold_research` - user is learning before commercial selection.
- `urgent_intent` - user needs fast action: emergency, today, now, 24/7, same day.
- `comparison_intent` - user compares providers, prices, ratings, conditions, or alternatives.
- `local_intent` - user needs service in a specific city, district, metro area, or nearby context.
- `b2b_intent` - organization, wholesale, contract, corporate, tender, or business buyer signals.
- `b2c_intent` - private individual, household, personal service, retail lead signals.
- `branded_intent` - query includes the advertiser brand.
- `competitor_intent` - query includes a competitor brand or provider name.
- `informational_intent` - how-to, meaning, guide, DIY, symptoms, laws, examples.
- `mixed_intent` - SERP or wording supports more than one realistic intent.

## Ambiguity Rules

- Mark `mixed_intent` when SERP results split between ads, guides, aggregators, and local services.
- Do not force ambiguous queries into commercial clusters to increase volume.
- Preserve uncertainty for human review instead of hiding it inside broad ad groups.
- Use SERP evidence when keyword wording is unclear.

## Multi-Intent Risks

- Weak ad relevance.
- Poor landing match.
- Informational leakage into paid traffic.
- B2B and B2C audience conflict.
- Local and national intent conflict.
- Duplicate campaign coverage.

## SERP Mismatch Risks

- Keyword looks commercial but SERP is informational.
- Keyword looks local but SERP is aggregator-dominated.
- Keyword looks service-specific but SERP shows marketplaces.
- Keyword looks urgent but landing page lacks urgent service proof.

## Boundary

Intent classification guides human-reviewed structure. It does not automate bidding, campaign control, runtime decisions, or live optimization.
