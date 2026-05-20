# Negative Keyword Layering v1

## Purpose

Define simple negative keyword review layers for cleaner manual campaign preparation.

This is not automatic semantic filtering or autonomous upload generation.

## Layers

### Account / Shared Layer

Use for clearly irrelevant meanings that should not appear anywhere.

Examples:

- jobs;
- vacancies;
- free;
- DIY;
- instructions;
- unrelated equipment purchase.

### Campaign Layer

Use for meanings irrelevant to a specific campaign segment.

Examples:

- wrong city;
- wrong service line;
- planned-service terms in urgent campaigns;
- urgent terms in planned-service campaigns where response promise does not match.

### Ad Group Layer

Use for close ambiguity inside a specific intent group.

Examples:

- similar service variants;
- equipment capacity mismatch;
- B2B/B2C mismatch;
- competitor names outside competitor campaigns.

## Review Rules

- Do not over-block useful demand.
- Separate obvious waste from uncertain terms.
- Mark uncertain exclusions as `SAFE_UNKNOWN`.
- Review negatives against landing and service reality.
- Recheck negatives after campaign structure changes.

## Import Readiness

Before Direct Commander preparation, review:

- duplicate negatives;
- contradictory negatives;
- wrong-layer negatives;
- overbroad match risks;
- missing geo exclusions;
- missing informational exclusions.

## Boundary

ORCA does not upload negative keywords or manage campaign exclusions. Human review is mandatory.
