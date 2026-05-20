# Seasonal Distortion Rules v1

## Purpose

Defines how ORCA identifies and limits seasonal distortion in commercial observations. Seasonality affects demand, urgency, price sensitivity, SERP composition, and offer behavior.

ORCA observes reality. ORCA does not define reality. Seasonal conclusions remain bounded to the evidence period unless repeated across comparable seasons.

## Seasonal Distortion Signals

- demand spikes or drops;
- urgent service language increases;
- price sensitivity shifts;
- discount or promotion density changes;
- local pack behavior changes;
- competitor ad density changes;
- aggregator visibility changes;
- weather, holiday, fiscal, or event-driven behavior;
- short-lived landing or CTA changes.

## Rules

- Record observation date and relevant seasonal context.
- Mark a finding as season-bound when timing may affect interpretation.
- Do not transfer seasonal evidence to non-seasonal periods without validation.
- Do not raise confidence from seasonal repetition unless the observations are seasonally comparable.
- Preserve contradictions between in-season and off-season evidence.
- Treat seasonal SERP volatility as a confidence penalty.
- Require human review before using seasonal evidence for strategy.

## Confidence Limits

- Single seasonal observation: cap at LOW.
- Repeated observations inside one season: cap at MEDIUM unless supported by prior comparable seasons.
- Cross-season contradiction: split the pattern by season or downgrade confidence.
- Stale seasonal evidence: mark as decayed until refreshed.

## Boundary

These rules document seasonal evidence discipline. They are not forecasting, demand modeling, telemetry, or automated seasonality detection.
