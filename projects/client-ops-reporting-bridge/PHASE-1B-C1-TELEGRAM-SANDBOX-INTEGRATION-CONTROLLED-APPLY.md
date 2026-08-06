# PHASE-1B-C1 — Telegram Sandbox Integration Controlled Apply

**Status:** COMPLETE
**Date:** 2026-07-24
**Workflow:** `MARS Client Ops Bridge — bzpm.ru` (`tkM4H0G0gM3q9Foi`)
**Readiness:** `READY_FOR_NEXT_INACTIVE_SANDBOX_PHASE`
**Commit:** Phase 1B-C1B baseline commit (this evidence pack); not pushed

## Summary

Phase 1B-C1 applied the accepted Pattern B Telegram integration to the inactive real Client Ops workflow, verified exact structural delta, temporarily activated for one synthetic authenticated POST, confirmed one Telegram delivery, and restored `active=false`.

## Results

| Area | Result |
|------|--------|
| Pre-state | Exact match (nodes=9, exec=24, version `6c6d1282-…`, Header Auth bound, Telegram absent) |
| PUT | 1 |
| Post-PUT | nodes=10, version `900407ad-…`, inactive, Pattern B connected |
| Sandbox POST | HTTP 202 ACCEPTED / DEFERRED_SANDBOX |
| Execution | `3409` (24→25); Respond before Telegram |
| Telegram | attempts=1, delivered=1, duplicates=0, message_id=4, chat=499423375 |
| Containment | final `active=false`, running=0 |
| Rollback | prepared, not triggered |

## Evidence

`n8n/evidence/phase-1b-c1-telegram-sandbox-controlled-apply/`

## Next

**Phase 1B-D0 — Inactive Sandbox Next-Step Decision and Runtime Connection Charter**

Documentation/decision only unless separately authorized. Do not begin without explicit operator charter. Production activation remains forbidden.
