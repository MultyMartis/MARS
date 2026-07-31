# ADMIN-PRODUCTION-OBSERVABILITY-v1

**Phase:** 3C.2

## Structural

| Surface | Present |
|---------|---------|
| /health path nodes | yes |
| /stats path nodes | yes |
| /last_error path nodes | yes |
| Gmail health query wording (Phase 3C.1) | retained |

## Live invocation

Operator Telegram `/status` `/health` `/stats` `/last_error` live spam **not** re-fired in this phase (avoid chat noise).  

Operational evidence substitutes:

- Empty polls succeed after finalization (`intake_route=empty`).
- Lead success advanced PROCESSED/incoming removal.
- No dual-active intake.

## Expectation for operator spot-check

- `/status`: last poll / last processed should reflect post-11:24 window (not only 30.07 synthetic).
- `/health`: Gmail available; eligible count 0 when idle.
- `/stats`: excludes SYNTHETIC_TEST; includes real production rows in 7-day window.
- `/last_error`: must not present stale synthetic as current after newer successes.
