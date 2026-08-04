# CONCURRENT ACTION SAFETY v1

- First valid pending → processed|spam wins.
- Second actor sees conflict / idempotent response.
- One business transition event.
- All known cards converge to the accepted final status.
- No reversal in this phase.
