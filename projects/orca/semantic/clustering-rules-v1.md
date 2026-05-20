# Clustering Rules v1

## Purpose

Defines how ORCA groups keywords into PPC-ready semantic clusters for human-reviewed campaign architecture.

## Cluster Acceptance Rules

- Shared primary intent.
- Shared service or product category.
- Shared landing page fit.
- Shared geography or explicit geo logic.
- Compatible ad message and CTA.
- No hidden B2B/B2C conflict.

## Split Rules

Split clusters when:

- urgent and non-urgent terms need different messaging;
- local and non-local terms produce different SERPs;
- price-sensitive queries need distinct offer handling;
- competitor queries require separate policy and strategy review;
- informational terms weaken commercial relevance;
- aggregators dominate one subset but not another.

## Merge Rules

Merge only when:

- SERP intent is materially the same;
- landing page can satisfy all terms;
- ad copy can remain specific;
- negatives can control minor variation;
- human operator accepts the tradeoff.

## Cluster Contamination Flags

- `informational_leakage`.
- `geo_mixed`.
- `service_mixed`.
- `audience_mixed`.
- `competitor_mixed`.
- `landing_unclear`.
- `broad_match_risk`.

## Boundary

Clustering is a preparation method. It does not create live ad groups, control campaign settings, run automation, or manage bids.
