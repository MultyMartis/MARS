# DUPLICATE START FORENSIC v1

**Phase:** 3D.2.1  
**Date:** 2026-08-01  
**Workflow:** Admin.dev (`wLrLp4WQHm1VJmxz`)

## Classification

**expected_harness_overlap**

## Window

2026-07-31T18:10:00Z → 2026-07-31T18:30:00Z (Phase 3D.2 live harness)

## Counts (sanitized)

| Metric | Value |
|--------|-------|
| Admin executions in window | 9 |
| `/start` replies with Start panel text | 2 |
| Via Telegram Trigger | 0 |
| Via harness webhook | 2 |
| Reply-node runs per execution | 1 |
| Retries (`retryOf`) | 0 |
| Shared update_id | none (harness path; no Trigger update_id) |

## Root cause

Phase 3D.2 live harness deliberately invoked two authorized `/start` cases in sequence:

1. `auth_start` → `/start`
2. `auth_start_suffix` → `/start@…`

Both entered Normalize Command through a temporary harness webhook and both executed Safe Telegram Reply into the operator-private chat. The two messages were therefore **two deliberate test executions**, not:

- duplicate inbound Telegram updates;
- duplicate Telegram Trigger firings;
- dual command routes for one update;
- n8n retry;
- duplicate Safe Telegram Reply within one execution;
- readiness notice overlapping a Trigger `/start` (no Trigger `/start` in window).

## Patch decision

**No Admin command idempotency guard** — see `ADMIN-COMMAND-IDEMPOTENCY-v1.md`.

## Security

No update IDs, Telegram IDs, or raw payloads recorded in this evidence.
