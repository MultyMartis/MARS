# PHASE-1B-D3 — Controlled Sequential Producer Connection Charter and Synthetic Live POST

## Purpose

First authorized real Client Ops producer HTTPS request through the sequential producer layer, under narrow D3 gates.

## Parts

- **Part A** — transport/gating/tests/docs; no live mutation
- **Part B** — one activation, one FIRST_SEEN producer POST, optional exact replay, deactivation in finally

## Non-goals

SITE-002 runtime connection, scheduler, workflow graph change, Data Table admin mutation, automatic retries, concurrency > 1, production activation.

## Success readiness

`READY_FOR_CONTROLLED_PRODUCER_CONNECTION_BASELINE_COMMIT` (D3 functional)

After D3B evidence baseline commit: `READY_FOR_REAL_SOURCE_ADAPTER_AND_MANUAL_CONNECTION_CHARTER`

Does **not** mean production runtime is ready. Does **not** authorize SITE-002 monitor connection, scheduler, or unattended producer.
