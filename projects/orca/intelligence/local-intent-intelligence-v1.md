# Local Intent Intelligence v1

## Purpose

Defines reusable intelligence for local service intent in ORCA pilot cases. Local intent intelligence captures how region, proximity, urgency, and local trust signals affect PPC research.

## Local Intent Signals

- city or district modifiers;
- "near me" or nearby intent;
- urgent or same-day language;
- phone-first behavior cues;
- local pack presence;
- map rating density;
- service-area language;
- local provider visibility;
- region-specific terminology;
- local landing page fit.

## Intent Categories

- `explicit_local` - query includes city, district, near-me, or service-area language.
- `implicit_local` - query lacks geo modifier but SERP shows local pack or local providers.
- `urgent_local` - query combines local need with time pressure.
- `comparison_local` - query suggests comparing providers, ratings, or prices.
- `informational_local` - query asks for information with local context but weak purchase intent.
- `mixed_local` - signals conflict or require human interpretation.

## Intelligence Record

```yaml
local_intent_pattern:
  pattern_id:
  niche:
  region:
  query_examples:
  observed_serp_behavior:
  local_pack_role:
  trust_signal_role:
  landing_fit_requirement:
  confidence_level:
  reuse_limits:
  safe_unknown:
```

## Interpretation Rules

- Local intent varies by region and service category.
- Local pack presence can indicate local behavior but does not prove conversion behavior.
- Urgent local queries may require different landing and CTA review, but not automatic campaign changes.
- Region-specific terminology must be validated before reuse.
- Mobile and desktop behavior should be separated when evidence differs.

## Reuse Rules

Reusable local intent intelligence must include:

- original pilot case source;
- region boundary;
- niche boundary;
- query examples;
- confidence level;
- observed distortions;
- human validation note.

## SAFE UNKNOWN Examples

- actual user location;
- personalization effect;
- conversion behavior;
- local pack stability;
- mobile vs desktop split;
- seasonality effect.

## Boundary

Local intent intelligence supports human-supervised PPC planning. It is not automatic geo targeting, bid adjustment, campaign activation, or autonomous local strategy.
