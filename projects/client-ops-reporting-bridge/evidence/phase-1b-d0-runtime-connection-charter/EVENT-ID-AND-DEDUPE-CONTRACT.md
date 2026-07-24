# Event ID and Dedupe Contract — Phase 1B-D0

**Status:** CONTRACT FREEZE for future implementation (extends `EVENT-ID-AND-DEDUPE-V1.md`)
**Implementation:** NOT STARTED

## Authoritative `event_id` source

| Rule | Decision |
|------|----------|
| Authority | **Producer** (Client Ops exporter) computes `event_id` before POST |
| Algorithm | UUID v5 over SHA-256 of canonical identity document (Phase 1A implemented) |
| Namespace | Fixed non-secret `MARS_CLIENT_OPS_REPORT_NAMESPACE_UUID` in exporter constants |
| n8n role | Validate UUID shape; **must not** recompute identity from raw monitor artifacts |

## UUID requirements

- Must be UUID string.
- Deterministic for identical normalized observation.
- Must not embed secrets, paths, chat IDs, or delivery timestamps.

## Retry vs new monitor run

| Case | `event_id` |
|------|------------|
| Producer network retry of same envelope | **Same** |
| Telegram delivery retry | **Same** |
| New monitor run folder / changed normalized facts | **New** |
| Re-export identical normalized facts | **Same** |

## Dedupe lookup key

- Primary key: `event_id`
- Conflict detector: `envelope_sha256` (canonical envelope bytes)

## Dedupe state values (PROPOSED)

| State | Meaning | Telegram |
|-------|---------|----------|
| `NEW` | No prior terminal record | Allowed per send policy |
| `ACCEPTED_PENDING_DELIVERY` | Webhook accepted; delivery not confirmed | In flight |
| `SENT` | Telegram confirmed | No |
| `DUPLICATE_ALREADY_SENT` | Prior SENT | No |
| `FAILED_RETRYABLE` | Delivery/infra failed; retry allowed | Yes on retry |
| `FAILED_TERMINAL` | Exhausted retries / conflict | No (manual) |
| `CONFLICTING_EVENT_ID` | Same `event_id`, different envelope hash | No — HITL |

## Completion definition

An event is **completed** when dedupe record is `SENT` **or** `FAILED_TERMINAL` / `CONFLICTING_EVENT_ID` after operator disposition.

HTTP **202 ACCEPTED** means intake accepted under current gates; it is **producer acknowledgement of acceptance**, not proof of Telegram SENT (Pattern B is post-response).

## Telegram failure vs webhook response

- Telegram failure **must not** rewrite HTTP accept/reject once Respond node has returned (Pattern B).
- Delivery status updates dedupe/ops fields only.
- Automatic Telegram retries: **not enabled in D0**; future bounded retries require D1+ charter.

## Retention

| Item | PROPOSED MVP |
|------|----------------|
| Dedupe row retention | ≥ 90 days or until explicit purge charter |
| Milestone sanitized evidence | Committed packs + ignored local runtime evidence |
| Raw execution payloads | Not committed |

## Collision handling

- Same `event_id` + same hash → duplicate path.
- Same `event_id` + different hash → `CONFLICTING_EVENT_ID`; fail closed.

## Manual replay

- Operator override requires explicit charter + evidence that prior state is `FAILED_RETRYABLE` or forced replay with documented risk.
- Replay keeps same `event_id` unless identity fields intentionally change (then it is a new event).

## Assumptions (labeled)

- ASSUMPTION: OK continues to always-send during validation period (existing MVP gate).
- ASSUMPTION: Single producer instance for SITE-002 MVP (concurrency beyond that is SAFE UNKNOWN until proven).
