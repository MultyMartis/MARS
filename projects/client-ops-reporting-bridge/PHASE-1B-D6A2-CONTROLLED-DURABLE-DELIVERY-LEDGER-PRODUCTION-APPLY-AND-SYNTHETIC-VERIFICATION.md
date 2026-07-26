# PHASE-1B-D6A2 — Controlled Durable Delivery Ledger Production Apply and Synthetic Verification

**Status:** COMPLETE (contained)
**Date:** 2026-07-26 / 2026-07-27 (operator local)
**Readiness:** `READY_FOR_D6A2_EVIDENCE_BASELINE_COMMIT`

## Summary

Accepted D6A offline durable delivery-ledger delta was applied once to production workflow `tkM4H0G0gM3q9Foi` (17→20 nodes) while inactive. Synthetic non-customer verification proved PENDING→SENT with HTTP 202 intake semantics, one Telegram delivery (sanitized message_id `8`), duplicate replay with zero Telegram, and immediate recontainment (`active=false`). Historical real event remained PENDING. SITE-002 runtime untouched. No commit/push.

## Evidence

`evidence/phase-1b-d6a2-controlled-durable-delivery-ledger-production-apply/`

## Tooling

- `n8n/runners/run-client-ops-d6a2-delivery-ledger-production-apply.mjs`
- Activation phrases added to `n8n/runners/lib/client-ops-n8n-activation-client.mjs`

## Production readiness

- `CLIENT_OPS_UNATTENDED_PRODUCTION_READY=NO`
- `CLIENT_OPS_AUTOMATIC_SITE002_CONNECTION_AUTHORIZED=NO`
- D6B / D6C / D6E / D6D = NOT STARTED

## Next (do not begin automatically)

1. **Phase 1B-D6A2B — Durable Delivery Ledger Production Evidence Baseline Commit**
2. After accepted commit: **Phase 1B-D6B — Source Status vs Delivery Freshness Semantics Separation**
3. Historical PENDING reconciliation (event `c84e29bf-…`) via separate charter if desired
