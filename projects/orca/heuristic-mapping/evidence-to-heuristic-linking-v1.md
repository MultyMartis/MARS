# Evidence-to-Heuristic Linking v1

## Purpose

Defines how ORCA links evidence records and observations to strategic heuristics without turning limited evidence into universal claims.

Evidence supports bounded human judgment. It does not automatically generate, validate, or evolve heuristics.

## Minimum Evidence Requirements

A heuristic link should include:

- at least two comparable supporting observations or one pilot finding plus corroborating observation;
- traceable source records with timestamp, region, niche, device, and query or page context;
- explicit supporting observation notes;
- explicit contradiction review;
- freshness review;
- human reviewer decision.

One observation may create a hypothesis. It should not create a reusable heuristic.

## Repeated Observation Requirements

Repeated observations must be comparable by:

- commercial intent;
- niche;
- region or local market type;
- device context;
- SERP or landing context;
- season or demand cycle when relevant.

Repetition inside one unstable SERP, one synthetic summary, or one unsupported pilot thread does not establish stable guidance.

## Contradiction Handling

When evidence conflicts:

- preserve both supporting and conflicting records;
- record whether the conflict is regional, seasonal, device-related, CTA-related, SERP-related, or unknown;
- cap or downgrade confidence until reviewed;
- narrow applicability when the conflict is bounded;
- mark `SAFE_UNKNOWN` when the cause cannot be explained.

Contradictions are evidence. They must not be hidden to protect a preferred heuristic.

## Evidence Penalties

Apply weak evidence penalties for:

- single-source repetition;
- missing timestamp;
- unclear region;
- unclear niche;
- missing device context;
- unreviewed assumptions;
- synthetic-only summaries;
- unsupported pilot generalization.

Apply stale evidence penalties for:

- old screenshots;
- changed SERP layouts;
- changed competitor mix;
- changed local pack behavior;
- changed CTA or offer patterns;
- changed seasonality;
- expired or unknown freshness.

## Mismatch Risks

Region mismatch risks include:

- applying city-level evidence to national markets;
- transferring findings between regions with different aggregator pressure;
- using evidence from one local pack structure in another market.

Niche mismatch risks include:

- applying urgent-service logic to planned-service demand;
- applying trust-heavy patterns to commodity comparisons;
- applying high-CPC pressure rules to low-pressure markets.

Mismatch does not invalidate evidence. It limits where the heuristic may be used.

## Boundary

These rules support human evidence linking. They are not automated validation, telemetry analytics, scraping, market intelligence automation, or autonomous strategy selection.
