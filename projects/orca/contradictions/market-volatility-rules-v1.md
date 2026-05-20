# Market Volatility Rules v1

## Purpose

Defines how ORCA records and applies market volatility to evidence confidence. Volatility means visible commercial conditions may change quickly and conclusions need stricter limits.

ORCA observes reality. ORCA does not define reality. Volatile markets reduce confidence unless repeated current evidence supports the pattern.

## Volatility Sources

- unstable SERPs;
- changing ad density;
- aggregator entry or exit;
- local pack dominance shifts;
- seasonal demand changes;
- competitor offer changes;
- CTA changes;
- trust signal changes;
- regional commercial maturity changes;
- promotional or event-driven behavior.

## Volatility Levels

- `low` - pattern remains consistent across comparable observations.
- `medium` - pattern changes sometimes but has identifiable boundaries.
- `high` - pattern changes frequently or contradictions remain open.
- `unknown` - evidence is insufficient to classify volatility.

## Rules

- High volatility reduces confidence and evidence strength.
- Unknown volatility requires SAFE UNKNOWN.
- Volatility must be tied to evidence, not assumed.
- Repeated observations matter more than isolated volatile snapshots.
- Volatility can be regional, seasonal, niche-specific, or device-specific.
- Commercial intelligence can decay faster in high-volatility contexts.
- Human review is required before using volatile evidence strategically.

## Confidence Effects

- High volatility usually caps confidence at MEDIUM.
- Open contradictions plus high volatility usually cap confidence at LOW.
- Stable repeated evidence can raise confidence only within the observed context.
- Volatility penalties must remain visible in downstream summaries.

## Boundary

These rules document human-supervised volatility handling. They are not market monitoring, runtime analytics, alerting, scraping, or predictive automation.
