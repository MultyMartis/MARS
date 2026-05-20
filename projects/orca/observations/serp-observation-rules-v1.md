# SERP Observation Rules v1

## Purpose

Defines how ORCA pilot cases record SERP observations for PPC research. SERP observations are contextual snapshots, not live monitoring, scraping infrastructure, or automatic optimization inputs.

## Required Context

- search engine;
- region;
- device;
- timestamp;
- exact query;
- localization notes;
- personalization risk;
- screenshot or manual reference when available.

## What To Observe

- top ad count;
- bottom ad count;
- visible offer patterns;
- visible CTA patterns;
- local pack presence;
- aggregator presence;
- marketplace presence;
- organic competitor types;
- review and trust signals;
- landing types;
- informational contamination;
- policy or sensitive-claim risk.

## Interpretation Rules

- Describe visible evidence first.
- Mark SERP data as time-bound.
- Treat region as a core variable.
- Record device differences.
- Do not infer bids, budgets, conversion rates, or account strategy.
- Do not claim stable dominance from one snapshot.
- Do not claim user preference from result order alone.

## Volatility Notes

Add volatility notes when:

- ad count changes across queries;
- local pack appears inconsistently;
- aggregators appear in some queries but not others;
- personalization may affect results;
- seasonality may affect demand;
- observed results conflict with prior cases.

## SAFE UNKNOWN Examples

- personalization effect;
- exact auction pressure;
- competitor account intent;
- complete market coverage;
- whether layout is stable over time;
- whether local pack behavior persists outside the observed region.

## Boundary

SERP observation supports human-supervised PPC research. It does not create automated monitoring, browser agents, scraping engines, live optimization, or autonomous market conclusions.
