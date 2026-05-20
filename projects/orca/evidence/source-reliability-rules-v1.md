# Source Reliability Rules v1

## Purpose

Defines how ORCA qualifies evidence sources before using them in commercial intelligence. Source reliability protects research from synthetic contamination, weak observations, and unsupported conclusions.

ORCA observes reality. ORCA does not define reality. Source reliability describes evidence quality, not market truth.

## Source Classes

- `primary_observation` - direct human-reviewed SERP, landing, local pack, or competitor observation.
- `case_evidence` - evidence collected inside a known ORCA pilot or project case.
- `client_input` - business-provided facts requiring context and possible validation.
- `operator_note` - human research note requiring source context.
- `secondary_reference` - public report, platform documentation, or third-party statement.
- `synthetic_output` - AI-generated summary or suggestion. This is not evidence unless traced to verifiable observations.
- `SAFE_UNKNOWN` - source cannot be reliably classified.

## Reliability Signals

- timestamp is present;
- region and niche are defined;
- device context is known when SERP behavior matters;
- observation can be repeated or independently reviewed;
- source is close to the commercial reality being described;
- contradictions are recorded rather than suppressed;
- source does not depend only on AI-generated inference.

## Weak Source Signals

- missing timestamp;
- unclear region;
- no observable source trail;
- generated summary without underlying observations;
- stale SERP or landing evidence;
- high personalization risk;
- seasonal or regional distortion not marked;
- commercial claim copied without verification.

## Rules

- Synthetic output may help organize notes but must not be treated as source evidence.
- Client input may describe business reality but does not automatically describe market reality.
- Secondary references require date, region, and applicability checks.
- SERP observations are volatile and must include context.
- Regional differences matter and must not be flattened.
- Human review is required before weak sources influence confidence.

## Boundary

These rules govern source discipline for research documentation. They are not a source crawler, telemetry system, scraping process, or automated reliability engine.
