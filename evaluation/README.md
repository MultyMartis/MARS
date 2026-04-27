# `evaluation`

## Purpose

Reserved for **evals**, release-gate policy, and quality-metric names — the **Evaluation Layer** in `web-gpt-sources/02_architecture.md` and `10_observability_eval.md`. Pairs with [../governance/dependency-map.md](../governance/dependency-map.md) (Stage 12), [../interfaces/self-audit-v0.md](../interfaces/self-audit-v0.md), and the [Validator Agent](../agents/registry.md) (registry role).

## Status

**Documentation only** — no eval runner, test harness, golden data set, or automated gate enforcement in this repository (Phase 1). See [../AGENTS.md](../AGENTS.md) and [../governance/master-build-map.md](../governance/master-build-map.md) (Stage 12).

## Contract index (v0)

| Document | Role |
|----------|------|
| [evals-v0.md](evals-v0.md) | Eval types; relation to Self-Audit and Validator Agent |
| [release-gates-v0.md](release-gates-v0.md) | Which changes need evaluation; outcomes PASS / FAIL / NEED REVIEW |
| [quality-metrics-v0.md](quality-metrics-v0.md) | Named quality metrics; relation to observability and future telemetry |

## Relation to MARS architecture

Complements [../observability/](../observability/) and may exercise [../agents/](../agents/), [../models/](../models/), [../workflows/](../workflows/), and [../memory/](../memory/) in future harnesses. No implementation in Phase 1 unless code appears in-tree.
