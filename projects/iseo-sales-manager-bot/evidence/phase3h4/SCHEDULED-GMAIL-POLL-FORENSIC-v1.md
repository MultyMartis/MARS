# SCHEDULED GMAIL POLL FORENSIC v1

## Classification

`POLLING_ACTIVE_BUT_HEARTBEAT_NOT_WRITTEN_ON_EMPTY_RUNS`

## Observed behavior (pre-repair)

| Signal | Value |
|---|---|
| Schedule Trigger | active · `minutesInterval=2` |
| Execution cadence | ~every 2 minutes |
| Typical empty-run path | Gmail Fetch → Intake Gate → **empty route** |
| Update Last Success output on empty runs | `[]` (no CONFIG write) |
| Frozen CONFIG key | `last_poll_success_at=2026-08-05T10:34:00.459Z` (= 05.08.2026 13:34 МСК) |

## `/status` impact

`/status` displayed stale poll success because heartbeat keys were not advanced on zero-message polls, even though scheduled polling continued.

## `/health` separation

`/health` Gmail probe is a **separate on-demand check** and must **not** be treated as evidence of scheduled poll heartbeat. Health may pass while scheduled heartbeat keys are stale.

## Repair direction

Write compact heartbeat JSON + mirror keys on **every** successful scheduled poll completion, including empty inbox runs — see `GMAIL-POLL-HEARTBEAT-v1.md`.
