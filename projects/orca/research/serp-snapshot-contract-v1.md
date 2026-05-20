# SERP Snapshot Contract v1

## Purpose

Standardizes a single human-reviewed SERP observation for ORCA PPC research. The snapshot supports Yandex.Direct campaign architecture and semantic QA; it is not scraping infrastructure, browser automation, or live optimization.

## Required Fields

- `search_engine` - Yandex, Google, or other explicitly named engine.
- `region` - city, oblast, country, or configured ad region.
- `device` - desktop, mobile, or SAFE UNKNOWN.
- `localization` - language, user location assumption, map region, VPN/proxy note if relevant.
- `timestamp` - date and time of observation.
- `query` - exact searched phrase.
- `serp_type` - commercial, local, aggregator-heavy, marketplace-heavy, informational, mixed.
- `ads_blocks` - top ads, bottom ads, count, visible message patterns.
- `maps_local_pack` - present, absent, dominant, or SAFE UNKNOWN.
- `aggregators` - visible aggregators and their positions.
- `marketplaces` - visible marketplaces and their positions.
- `review_signals` - ratings, review counts, trust snippets, complaint cues.
- `offer_patterns` - price, guarantee, speed, consultation, delivery, emergency, discount.
- `cta_patterns` - call, order, calculate, book, request quote, WhatsApp, callback.
- `landing_observations` - visible landing types: service page, aggregator page, catalog, lead form, map card.
- `safe_unknown` - missing or uncertain fields.

## Optional Fields

- `screenshots_ref`.
- `operator_notes`.
- `policy_risk_notes`.
- `seasonality_notes`.
- `personalization_risk`.

## Validation Notes

- Treat every snapshot as time-bound and region-bound.
- Do not infer competitor bids, budgets, conversion rate, or account strategy.
- Do not claim automated monitoring.
- Human review is required before downstream keyword, ad copy, or campaign decisions.

## Example

```yaml
search_engine: Yandex
region: Saint Petersburg
device: mobile
localization: ru, city-level local results
timestamp: 2026-05-18T15:40:00+07:00
query: срочный вывоз мебели
serp_type: local commercial
ads_blocks:
  top_count: 4
  visible_patterns:
    - same-day service
    - price from
maps_local_pack: dominant
aggregators:
  - Yandex Services
marketplaces: []
review_signals:
  - map ratings visible
offer_patterns:
  - urgent service
  - fixed price promise
cta_patterns:
  - call now
landing_observations:
  - local service landing pages
safe_unknown:
  - exact personalization influence
```

## Boundary

This contract supports research-first PPC quality. It does not enable autonomous advertising, automatic campaign control, bid management, or runtime orchestration.
