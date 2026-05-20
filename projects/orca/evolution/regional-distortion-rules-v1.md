# Regional Distortion Rules v1

## Purpose

Defines how ORCA handles regional differences in commercial observations. Region affects SERP layout, aggregator strength, local trust signals, competitor density, price sensitivity, and CTA behavior.

ORCA observes reality. ORCA does not define reality. Regional findings do not become universal market rules without repeated multi-region evidence.

## Regional Distortion Signals

- different local pack dominance;
- different aggregator or marketplace pressure;
- different ad density;
- different trust requirements;
- different price framing;
- different review density;
- different local provider maturity;
- different mobile SERP behavior;
- region-specific language or intent modifiers.

## Rules

- Attach region to every observation used for commercial intelligence.
- Do not transfer confidence from one region to another by default.
- Split patterns by region when findings diverge.
- Treat missing region as SAFE UNKNOWN and a confidence penalty.
- Preserve regional contradictions.
- Require multi-region confirmation before calling a pattern regional or general.
- Human review is required before applying one region's evidence to another.

## Confidence Limits

- Unknown region caps confidence at LOW.
- Single-region evidence cannot support general market conclusions.
- Multi-region evidence increases reliability only when regions are comparable.
- Strong contradiction between regions requires pattern splitting, not averaging.

## Boundary

These rules support regional evidence discipline. They are not geo-telemetry, automated localization, market coverage analytics, or regional forecasting.
