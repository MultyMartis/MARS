# FINAL SOAK GMAIL HEARTBEAT T0 v1

| Field | Value |
|---|---|
| Contract | `iseo-gmail-poll-heartbeat-v1.0` |
| Schedule | every **2** minutes (Schedule Trigger) |
| Final T+0 | 2026-08-06 16:20 Europe/Moscow |
| Observation | 2026-08-06 ~19:42–19:52 Europe/Moscow |

## Cadence sample (scheduled / trigger mode)

Recent gaps between successive scheduled polls: **120s, 120s, 120s, 120s** — cadence OK.

## Latest automatic poll (example)

| Field | Value |
|---|---|
| Execution | sanitized ref `exec:24406` class |
| Started | 06.08.2026 19:46:37 МСК |
| Status | success |
| Source | `scheduled` |
| Matching messages | **0** |
| Empty successful poll | **yes** |
| Gmail Fetch executed | yes |
| Heartbeat CONFIG write | yes (`gmail_poll_heartbeat` + mirrors) |
| Apply Runtime State CONFIG | yes |

Heartbeat JSON (sanitized fields): `last_poll_state=success`, `last_poll_source=scheduled`, `last_poll_matching_messages=0`, `polling_interval_minutes=2`, `heartbeat_version=iseo-gmail-poll-heartbeat-v1.0`.

## Since T+0 (listed executions window)

| Metric | Value |
|---|---:|
| Ops executions listed since T+0 | 106 |
| Success | 106 |
| Error | 0 |
| Stuck | 0 |
| Scheduled polls inspected in detail | ≥15 (plus lead-path deep dives) |
| Stale heartbeat incidents | **0** (age ≪ 6-minute threshold) |

`/health` was **not** used as a substitute for scheduled polling proof.
