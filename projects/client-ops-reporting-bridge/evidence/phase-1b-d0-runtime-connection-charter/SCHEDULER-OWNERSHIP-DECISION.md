# Scheduler Ownership Decision — Phase 1B-D0

**Status:** DECISION (no schedule created/modified)

## Options considered

| Owner | Fit | Notes |
|-------|-----|-------|
| Existing SITE-002 monitor scheduler | **Reject for Bridge producer** | Owns monitor only; historically runs from `X:\AI MARS` (dirty-main risk) |
| Windows Task Scheduler (Client Ops producer) | **PREFERRED later** | Separate task; disabled until gates; launch from clean checkout |
| n8n Schedule Trigger | Cautious / deferred | Changes webhook-driven architecture toward R4 |
| MARS runtime checkout scheduled job | Compatible pattern | Aligns with clean-checkout rule |
| Other | SAFE UNKNOWN | None accepted without evidence |

## Selected owner (PROPOSED for future)

**Windows Task Scheduler** dedicated to Client Ops exporter/producer (not the monitor task), after manual E2E success.

## Clean runtime boundary (REQUIRED)

- Scheduled/runtime jobs **must not** run from dirty `X:\AI MARS`.
- Use a clean runtime checkout under:
  - `X:\AI MARS STORAGE\runtime-checkouts\...` (canonical target when created under future charter)
- Never schedule from a dirty main monorepo.
- D0 does **not** create checkouts or Storage mutations.

## Manual-first order (SELECTED)

1. Offline fixture generation
2. Producer dry-run
3. Authenticated manual runtime POST (HITL temporary activation)
4. One end-to-end live-source controlled test (HITL)
5. Repeated manual observation
6. Scheduler connection (disabled→enabled under HITL)
7. Unattended inactive/active operation policy
8. Production activation (last)

## Temporary vs durable activation for first real-source test

**SELECTED:** first real-source test may use **temporary HITL activation** with deactivate-in-finally (as B2/C1), **not** durable production activation.

## Rollback for scheduler

- Disable/delete Client Ops task only.
- Do not touch SITE-002 monitor task unless separately chartered.
- Preserve evidence; do not `git clean` dirty main.
