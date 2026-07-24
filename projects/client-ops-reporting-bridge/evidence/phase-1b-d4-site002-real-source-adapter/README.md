# Phase 1B-D4 — SITE-002 Real-Source Adapter Evidence

**Phase:** 1B-D4
**Mode:** OFFLINE / READ-ONLY vs SITE-002 runtime, n8n, Telegram, scheduler
**D4 verdict target (historical):** READY_FOR_REAL_SOURCE_ADAPTER_OFFLINE_BASELINE_COMMIT
**Post-D4B readiness:** READY_FOR_FIRST_MANUAL_REAL_SOURCE_CONNECTION_CHARTER

## Classification

| Class | Items |
|-------|-------|
| PROVEN_LIVE | synthetic producer HTTPS; Header Auth; durable dedupe; Telegram one-send/replay (prior D3) |
| PROVEN_OFFLINE | SITE-002 real-source adapter; parsing; status mapping; run identity; firewall; deterministic event_id; mock responses |
| SOURCE_AUTHORITY | SITE-002-MVP-INTAKE + ARTIFACT-AUTHORITY + hardening contract + monitor tool (read-only) |
| DEFERRED | real SITE-002 artifact live POST; automatic monitor integration; scheduler; SENT ledger; concurrency |
| FORBIDDEN_D4 | monitor execution; real-source HTTP POST; scheduler; unattended processing |

Storage reads: **0**. Storage mutations: **0**.
