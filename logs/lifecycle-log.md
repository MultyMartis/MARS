# MARS — Lifecycle log

**Normative role:** This file is the **single source of truth** for **documented lifecycle events** in the MARS repository: a human- and tool-maintained **append-only** log. New information is added by **appending** new rows at the end of the event table. **Do not** delete or rewrite past rows except where repository policy explicitly allows correction of non-factual errors (e.g. typos), and if so, record a follow-up **event_type** explaining the correction.

**Version:** v0 (schema stable unless superseded by a governance revision).

---

## Event schema (required fields)

Each log entry **must** include:

| Field | Type / values | Meaning |
|-------|----------------|---------|
| **event_id** | Opaque string, unique in this file | Stable identifier for the event (e.g. `evt-2026-0001`). |
| **timestamp** | ISO-8601 datetime (UTC preferred) | When the event occurred or was recorded. |
| **entity_id** | String | Subject of the event: `project_id`, agent id, document path, or other agreed id namespace. |
| **event_type** | Short token | Category (e.g. `project.status_changed`, `registry.updated`, `phase.transition`). |
| **description** | Free text, factual | What happened, grounded in repo or governance; no speculation. |

---

## Events (append below)

| event_id | timestamp | entity_id | event_type | description |
|----------|-----------|-----------|------------|-------------|
| evt-2026-0001 | 2026-04-27T00:00:00Z | registry | registry.updated | Initialized formal **project-registry** and **lifecycle-log** sources of truth; introspection v0 bindings updated in `interfaces/introspection-v0.md`. |
| evt-2026-0002 | 2026-04-27T12:00:00Z | governance | governance.stage_7_5_complete | **Stage 7.5** consistency fix pass and re-check completed; **P0** introspection path conflict resolved (repository-root-relative paths in `interfaces/`); **Consistency Fix gate** satisfied per `governance/master-build-map.md`; **Stage 8** documentation may proceed. |
| evt-2026-0003 | 2026-04-27T18:00:00Z | governance | governance.stage_8_5_complete | **Stage 8.5** closed: **Runtime Readiness P0** **documentation** **complete**; **7/7** **P0** **contracts** **documented** (per `governance/master-build-map.md`); **Stage 9** (Tool) documentation **may** **proceed** **after** a **documented** **backup**; **no** in-repo **runtime** **implementation** (see `AGENTS.md`). |
| evt-2026-0004 | 2026-04-28T12:00:00Z | governance | governance.stage_9_complete | **Stage 9** (Tool Registry / Tool Permissions) documentation milestone recorded per `governance/master-build-map.md`; **documentation-only, no runtime implementation**. |
| evt-2026-0005 | 2026-04-28T12:00:00Z | governance | governance.stage_10_complete | **Stage 10** (Model Layer / Provider Routing) documentation milestone recorded per `governance/master-build-map.md`; **documentation-only, no runtime implementation**. |
| evt-2026-0006 | 2026-04-28T12:00:00Z | governance | governance.stage_11_complete | **Stage 11** (Storage / Memory / RAG) documentation milestone recorded per `governance/master-build-map.md`; **documentation-only, no runtime implementation**. |
| evt-2026-0007 | 2026-04-28T12:00:00Z | governance | governance.stage_12_complete | **Stage 12** (Observability / Evaluation) documentation milestone recorded per `governance/master-build-map.md`; **documentation-only, no runtime implementation**. |
| evt-2026-0008 | 2026-04-28T12:00:00Z | governance | governance.stage_13_complete | **Stage 13** (Runtime / Execution Orchestration) documentation milestone recorded per `governance/master-build-map.md`; **documentation-only, no runtime implementation**. |
| evt-2026-0009 | 2026-04-28T12:00:00Z | governance | governance.stage_14_complete | **Stage 14** (Runtime Infrastructure / Deployment Model) documentation milestone recorded per `governance/master-build-map.md`; **documentation-only, no runtime implementation**. |
| evt-2026-0010 | 2026-04-28T12:00:00Z | governance | governance.stage_15_complete | **Stage 15** (External Integrations) documentation milestone recorded per `governance/master-build-map.md`; **documentation-only, no runtime implementation**. |

---

## Append-only rule

1. **Append only** — Add new rows to the bottom of the table; do not reorder historical rows for convenience.
2. **Integrity** — Prefer immutable **event_id** values; never reuse an **event_id**.
3. **Cross-reference** — For project-scoped events, **entity_id** should align with **project_id** in `registry/project-registry.md` when the subject is a project.
