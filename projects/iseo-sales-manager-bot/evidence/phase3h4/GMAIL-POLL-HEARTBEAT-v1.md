# GMAIL POLL HEARTBEAT v1

## Contract version

`iseo-gmail-poll-heartbeat-v1.0`

## Write trigger

Every **successful** scheduled poll completion on Operational.dev, including **empty** Gmail Fetch runs (Intake Gate empty route).

## CONFIG keys (mirror set)

| Key | Purpose |
|---|---|
| `gmail_poll_heartbeat` | Compact JSON heartbeat blob |
| `last_poll_success_at` | ISO timestamp mirror for `/status` |
| `last_poll_heartbeat_version` | `iseo-gmail-poll-heartbeat-v1.0` |

## Heartbeat JSON shape (sanitized)

```json
{
  "version": "iseo-gmail-poll-heartbeat-v1.0",
  "at": "<ISO-8601>",
  "empty_run": true|false,
  "messages_fetched": 0
}
```

## Non-test production stamp (on non-test success)

Additionally stamps:

- `last_production_processed_at`
- `last_production_processed_lead_id`

Only when a **real** production lead completes processing — not on empty polls.

## Pre-repair failure mode

Update Last Success returned `[]` on empty runs → no CONFIG advancement → `/status` showed poll frozen since 05.08.2026 13:34 МСК.

## Architecture reference

See `architecture/GMAIL-POLL-HEARTBEAT-CONTRACT-v1.md`.
