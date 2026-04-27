# `observability`

## Purpose

Reserved for run history, events, tool-call records, and audit-relevant field semantics for MARS — the **Observability Layer** in `web-gpt-sources/02_architecture.md` and `10_observability_eval.md`. Pairs with [../governance/dependency-map.md](../governance/dependency-map.md) (Stage 12) and the [System Signals Dictionary](../governance/system-signals-dictionary.md).

## Status

**Documentation only** — no collectors, log pipelines, metrics backends, or dashboards in this repository (Phase 1). See [../AGENTS.md](../AGENTS.md) and [../governance/master-build-map.md](../governance/master-build-map.md) (Stage 12).

## Contract index (v0)

| Document | Role |
|----------|------|
| [run-history-v0.md](run-history-v0.md) | Per-run summary fields; relation to runtime state store and lifecycle log |
| [event-model-v0.md](event-model-v0.md) | Event fields, event types, relation to lifecycle log and future event bus |
| [tool-call-log-v0.md](tool-call-log-v0.md) | Per-invocation tool log; relation to tool contract and approval gates |
| [audit-trail-v0.md](audit-trail-v0.md) | What must be auditable, append-only principle, relation to risk register |

## Relation to MARS architecture

Complements the **Runtime State Store** ([../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md)) and **Execution Bridge** ([../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md)); does **not** replace the **append-only governance** [../logs/lifecycle-log.md](../logs/lifecycle-log.md). Ties to [../evaluation/](../evaluation/) for quality and release-gate evidence.
