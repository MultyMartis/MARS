# Market Evolution Tracking v1

## Purpose

Defines how ORCA tracks visible commercial market change over time. Evolution tracking records observed shifts; it does not forecast markets or define reality.

ORCA observes reality. ORCA does not define reality. Market conclusions remain human-supervised, evidence-backed, and revisable.

## Trackable Changes

- aggregator growth;
- CPC aggression changes based on visible ad density and messaging, not hidden CPC data;
- CTA shifts;
- mobile behavior shifts;
- trust architecture evolution;
- local pack dominance shifts;
- SERP saturation changes;
- commercial maturity changes;
- offer pressure changes;
- review and reputation signal changes.

## Required Context

- `evolution_id`;
- `region`;
- `niche`;
- `observation_period`;
- `device_context`;
- `baseline_evidence`;
- `new_evidence`;
- `change_description`;
- `repeatability`;
- `volatility`;
- `contradictions`;
- `confidence`;
- `human_reviewer`;
- `safe_unknown`.

## Rules

- Compare only observations with compatible region, niche, device, and query intent.
- Treat SERP data as volatile and time-bound.
- Do not infer hidden auction metrics from visible ad changes.
- Mark regional, seasonal, and device-specific distortion.
- Preserve contradictory evidence when a shift is uneven.
- Require repeated evidence before calling a change a stable trend.
- Downgrade confidence when evidence is stale, isolated, or contradicted.

## Evolution States

- `emerging` - early repeated signal, limited context.
- `active` - repeated and current change in a defined context.
- `stable` - observed consistently across time or cases.
- `volatile` - change appears inconsistent or SERP-dependent.
- `decaying` - prior pattern appears weaker in newer evidence.
- `SAFE_UNKNOWN` - evidence is insufficient.

## Boundary

This model supports human research continuity. It is not runtime analytics, telemetry, autonomous forecasting, scraping, browser automation, or self-learning market intelligence.
