# Evidence Decay Rules v1

## Purpose

Defines how ORCA reduces confidence when commercial intelligence becomes old, unstable, contradicted, or less applicable. Evidence freshness matters because SERPs, offers, competition, and user paths change.

ORCA observes reality. ORCA does not define reality. Commercial intelligence can decay over time and must remain revisable.

## Decay Triggers

- stale observation timestamp;
- changed SERP layout;
- new aggregator or marketplace pressure;
- changed local pack dominance;
- changed CTA or offer patterns;
- new contradiction;
- changed regional behavior;
- changed seasonal context;
- source reliability loss;
- market volatility increase.

## Freshness States

- `current` - suitable for present use in the same context.
- `recent` - usable with review and limits.
- `stale` - requires refresh before strategic use.
- `expired` - should not support confidence without new evidence.
- `unknown` - freshness cannot be verified.

## Rules

- Stale evidence cannot support VERY HIGH confidence.
- Expired evidence cannot support strategic conclusions without refresh.
- High-volatility markets decay faster.
- Seasonal evidence decays outside its season unless comparable history exists.
- Contradicted evidence must be downgraded or bounded.
- Decay does not require deleting old evidence.
- Human review is required before retiring or reactivating decayed evidence.

## Output Notes

Every decayed pattern should record:

- original confidence;
- decay reason;
- latest usable context;
- required refresh evidence;
- contradiction links;
- reviewer decision.

## Boundary

These rules govern documentation freshness. They are not telemetry, live monitoring, automated expiration, scraping, or prediction infrastructure.
