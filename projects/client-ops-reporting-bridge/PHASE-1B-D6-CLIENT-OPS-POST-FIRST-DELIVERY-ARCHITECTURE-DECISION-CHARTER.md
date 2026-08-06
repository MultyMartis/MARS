# PHASE-1B-D6 — Client Ops Post-First-Delivery Architecture Decision Charter

**Phase:** 1B-D6
**Type:** DESIGN / ARCHITECTURE / DECISION only
**Date (UTC context):** 2026-07-26 / operator local 2026-07-27
**Status:** COMPLETE — decision recorded; no implementation started

## Purpose

Determine the safest and most technically correct order for remaining Client Ops architecture work after the first proven SITE-002 real-source end-to-end delivery.

## Non-goals (enforced)

- No next architecture item implementation
- No live delivery / producer POST / webhook call
- No n8n activation / content mutation / new executions
- No Data Table mutation / Telegram
- No SITE-002 production, runtime, scheduler, or monitor mutation
- No Git commit / push / index staging by this phase

## Accepted baseline

| Item | Value |
|------|-------|
| Evidence baseline commit | `e9c9be59f643e66970930e31339431acb8077b55` |
| Runtime pin | `8bb6e8f0f56388c12fdb013cf4cc1b27eb84331c` |
| First verified event | `c84e29bf-79b1-5aea-98c4-9dc8d651fc96` / run `2026-07-26_17-48-38` |
| Delivery acceptance | `D5R2A_FIRST_SEEN_DELIVERY_VERIFIED` |
| Containment | workflow `active=false`, executions=32, DT rows=3 / event rows=1 |

## Historical charter state (immutable)

| Charter | State | Notes |
|---------|-------|-------|
| OLD D5 | UNUSED | `real_http_requests=0` |
| D5R2 | CONSUMED | 1 HTTP 404 before intake; delivery=0 |
| D5R2A | CONSUMED | HTTP 202 / FIRST_SEEN; exec 3416; DT +1; Telegram message_id 7; activation changes=2; final `active=false` |

## Primary question

**What must be fixed / defined first before any unattended Client Ops operation can be safely authorized?**

Answer (dependency-first): durable post-Telegram SENT ledger (**A**), then freshness semantics separation (**B**), then controlled activation lifecycle (**C**), then retry/concurrency policy (**E**), then unattended integration (**D**).

## Decision summary

| Token | Value |
|-------|-------|
| Priority hypothesis | `D6_PRIORITY_HYPOTHESIS_CONFIRMED` |
| SENT ledger before unattended | `YES` |
| Freshness separation before unattended | `YES` |
| Activation model | `HYBRID` (near-term C1; unattended target C3) |
| Unattended architecture | `D2` (separate scheduled producer reads completed monitor artifacts) |
| Retry prerequisite | Durable SENT ledger + GET-only reconciliation + freshness separation |
| Max safe concurrency today | `1` |
| Unattended production ready | `NO` |
| Automatic SITE-002 connection authorized | `NO` |
| Next phase | Phase 1B-D6A — Durable Post-Telegram Delivery Ledger Design and Offline Implementation |
| Readiness | `READY_FOR_D6_FIRST_IMPLEMENTATION_CHARTER` |

## Evidence pack

`projects/client-ops-reporting-bridge/evidence/phase-1b-d6-post-first-delivery-architecture-decision/`

Machine decision: `D6-DECISION.json`

## Final verdict

COMPLETE — CLIENT OPS POST-FIRST-DELIVERY ARCHITECTURE DECISION COMPLETE; NEXT IMPLEMENTATION PRIORITY DEFINED, PRODUCTION REMAINS CONTAINED
