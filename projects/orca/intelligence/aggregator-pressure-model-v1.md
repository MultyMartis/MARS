# Aggregator Pressure Model v1

## Purpose

Defines how ORCA pilot cases classify aggregator pressure in PPC research. Aggregator pressure describes visible influence from directories, marketplaces, lead platforms, review platforms, and service aggregators.

## Signals To Record

- aggregator ad visibility;
- aggregator organic visibility;
- local pack overlap;
- marketplace or directory presence;
- review/rating dominance;
- lead form or quote flow;
- price comparison framing;
- ranking or "best provider" claims;
- local provider displacement.

## Pressure Levels

## LOW

- aggregators absent or rare;
- local providers remain visible;
- no clear aggregator message dominance.

## MEDIUM

- aggregators visible for some queries;
- local providers still compete visibly;
- aggregator claims may influence comparison behavior.

## HIGH

- aggregators appear across multiple commercial queries;
- aggregator pages occupy strong positions;
- local providers may need stronger trust and offer differentiation.

## VERY HIGH

- aggregators dominate ads, organic, or comparison paths;
- local provider visibility is heavily compressed;
- aggregator trust, review, or price framing shapes the visible market.

## Interpretation Rules

- Record region, device, query set, and date.
- Distinguish aggregator pressure from brand dominance.
- Do not infer aggregator conversion share.
- Do not infer actual CPC impact.
- Do not claim user preference from visibility alone.
- Require repeated evidence before HIGH or VERY HIGH confidence.

## PPC Research Implications

Aggregator pressure may suggest human review of:

- landing trust proof;
- local differentiation;
- offer specificity;
- review visibility;
- query segmentation;
- exclusion or competitor-risk handling.

These implications are not automatic optimization rules.

## SAFE UNKNOWN Examples

- true click share;
- ad spend;
- lead quality;
- organic stability;
- personalization influence;
- region-wide representativeness.

## Boundary

This model supports human-supervised market interpretation. It does not perform scraping, monitoring, bidding, campaign control, or autonomous competitive strategy.
