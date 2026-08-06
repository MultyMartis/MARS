# PHASE-1B-D5R2A — Controlled Real-Source Delivery with Temporary n8n Activation and Immediate Re-Containment

**Status:** COMPLETE
**Date (UTC):** 2026-07-26
**Charter:** NEW one-shot (does not reuse consumed D5R2 charter)
**Readiness:** `READY_FOR_D5R2A_EVIDENCE_BASELINE_COMMIT`

## Summary

D5R2A temporarily activated workflow `tkM4H0G0gM3q9Foi`, sent exactly one authenticated SITE-002 real-source producer POST for event `c84e29bf-79b1-5aea-98c4-9dc8d651fc96`, verified FIRST_SEEN end-to-end (n8n execution `3416`, Data Table row, Telegram `message_id=7`), then immediately deactivated the workflow. Final `active=false`. Retries/replay=0. Runtime remained clean at `8bb6e8f0`.

## Prior D5R2

- Classification: `D5R2_REQUEST_REJECTED_BEFORE_WORKFLOW_INTAKE`
- HTTP 404; executions +0; Data Table +0; Telegram 0
- Charter: **CONSUMED** (not reused)

## Authorization

Exact live phrase used:

`APPROVE D5R2A TEMPORARY ACTIVATE + ONE REAL SOURCE POST + DEACTIVATE — EVENT c84e29bf-79b1-5aea-98c4-9dc8d651fc96 — NO RETRY`

Tooling phrases (activation client allowlist):

- `ACTIVATE CLIENT OPS MANUAL REAL SOURCE D5 BZPM`
- `DEACTIVATE CLIENT OPS MANUAL REAL SOURCE D5 BZPM`

Producer CLI: `site002-controlled-live` (established path)

## Caps consumed

| Cap | Actual |
|-----|--------|
| Activation changes | 2 |
| Producer HTTP POST | 1 |
| n8n executions added | 1 |
| Data Table rows added | 1 |
| Telegram attempted/delivered | 1 / 1 |
| Retries / replay | 0 / 0 |
| Workflow content edits | 0 |
| Monitor / scheduler executions | 0 / 0 |
| Git commit / push | 0 / 0 |

## Evidence

`projects/client-ops-reporting-bridge/evidence/phase-1b-d5r2a-temporary-activation-one-shot/`

## Next (do not begin)

**Phase 1B-D5R2AB — Temporary-Activation Real-Source Delivery Evidence Baseline Commit**

## Limitations preserved

- Durable post-Telegram SENT ledger: **DEFERRED**
- Freshness/status semantics repair: **DEFERRED**
- Production activation / automatic monitor→producer: **NO**
