# PRODUCTION PROPOSAL REVIEW v1

## Decision

**READY FOR PHASE 3C CUTOVER GATE — proposal only; not applied.**

## Recommended cutover

1. Activate accepted Operational.dev and deactivate the original in the same approved window.
2. Do not patch the original in place.
3. Keep Admin activation as a separate decision.
4. Enforce Gmail race prevention: exactly one scheduled intake owner and explicit incoming-label ownership.
5. At cutover, set `environment=production` with `ai_enabled=false` initially.
6. Keep the original inactive as the immediate rollback option.

## Boundary

No production cutover, original deactivation, real Gmail processing, or client communication occurred in Phase 3B.2.
