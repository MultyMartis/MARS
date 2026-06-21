# MARS — Lifecycle log

**Normative role:** This file is the **single source of truth** for **documented lifecycle events** in the MARS repository: a human- and tool-maintained **append-only** log. New information is added by **appending** new rows at the end of the event table. **Do not** delete or rewrite past rows except where repository policy explicitly allows correction of non-factual errors (e.g. typos), and if so, record a follow-up **event_type** explaining the correction.

**Operating model (Wave 2B):**

| Mode | Purpose |
|------|---------|
| **Key Event History** (default) | Material registry, governance, and stage changes — append `event_id` rows |
| **Lifecycle Tracking Mode** (optional) | Long-running human operations needing a durable temporal trail in this file — operator choice |

**Normal work** (task REPORTs, routine cleanup evidence, program notes) **does not** require a lifecycle row. **Long operations** (e.g. multi-session stabilization) **may** use Lifecycle Tracking Mode. Distinct from `logs/cleanup/` (audit) and `logs/releases/` (publication). Evidence: [logs/cleanup/actions/lifecycle-alignment-v1.md](cleanup/actions/lifecycle-alignment-v1.md).

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
| evt-2026-0011 | 2026-05-04T12:00:00Z | seo-content-agent | registry.updated | **SEO Content Agent** registered in `registry/project-registry.md` (`project_id` **seo-content-agent**, status **planned**); documentation pack added under `projects/seo-content-agent/` (architecture, workflows, prompts, schemas, roadmap); **no** runtime, n8n workflows, or credentials added. |
| evt-2026-0012 | 2026-05-11T12:00:00Z | mars-website-factory | registry.updated | **Website Factory entity identity normalization:** planned Website Factory **`agent_id`** rows added to `agents/registry.md` §4.1; Website Factory v0 entities and **MetaBOT** documentation pack edges added to `governance/dependency-map.md` §4; **no** runtime implementation; **prepares** future Website Factory agent cards (cards **not** authored in this change). |
| evt-2026-0013 | 2026-05-11T18:00:00Z | mars-website-factory | governance.identity_normalization | **Website Factory entity identity normalization** (doc-only checkpoint): planned agents registered in `agents/registry.md` §4.1; Website Factory v0 entities mapped in `governance/dependency-map.md` §4; **no** runtime implementation; prepares future Website Factory agent cards; **GIT CHECKPOINT** scope excluded `mars-runtime/adapters/seo-content-agent-adapter.js`, `mars-runtime/runtime/run-seo-content-agent-test.js`, and `projects/seo-content-agent/integrations/`. |
| evt-2026-0014 | 2026-05-11T20:00:00Z | mars-website-factory | registry.updated | **Website Factory design / UX / QA agent cards v0** (documentation-only checkpoint): added IA, UX Structure, AI Designer, Wireframe Generator, Full Design Generator, Design QA, SEO QA, and Conversion QA cards under `agents/cards/`; updated `agents/registry.md` §4.1, `projects/mars-website-factory/agent-map.md`, `projects/mars-website-factory/README.md`, and `governance/master-build-map.md` for cross-references; **no** runtime implementation or autonomy claims; **excluded** from commit scope: `mars-runtime/adapters/seo-content-agent-adapter.js`, `mars-runtime/runtime/run-seo-content-agent-test.js`, `projects/seo-content-agent/integrations/`. |
| evt-2026-0015 | 2026-05-14T00:00:00Z | governance | governance.doc_truth_repair | **Phase S0 — truth repair (documentation, governance + tools only):** root `README.md` aligned with this lifecycle log (Stages **9–15** documentation **milestones** already recorded **2026-04-28**) and `governance/master-build-map.md` per-phase tables; executive anchor clarified in master build map; added `governance/runtime-registry-boundaries.md`; `governance/enforcement/` (Phase S1 **documentation-only** aids); governance **S2–S7** semantics and reality-audit framework docs; operational helper pilots and helper stabilization/review under `tools/`; **no** full runtime shipped, **no** control-plane or orchestration implementation claims, **no** workspaces changes. |
| evt-2026-0016 | 2026-05-19T20:00:00Z | governance | governance.structural_stabilization_phase_2 | **Structural Stabilization Phase 2 (documentation only):** added `governance/mars-reality-index-v0.md`, `lifecycle-synchronization-review-v0.md`, `website-factory-navigation-compression-strategy-v0.md`, `runtime-mythology-pressure-review-v0.md`, `cross-system-clarity-review-v0.md`; lifecycle/registry gap findings recorded for human backfill; **no** Factory rewrite, **no** runtime implementation, **no** governance expansion beyond stabilization artefacts. |
| evt-2026-0017 | 2026-05-10T12:00:00Z | metabot-seo-content-agent | registry.updated | Canonical MetaBOT documentation pack registered **active** in `registry/project-registry.md`; external n8n execution; legacy `seo-content-agent` superseded for new docs; **no** runtime added in-repo. Timestamp aligned to registry row date (approximate session time — see `logs/cleanup/actions/lifecycle-backfill-review-v1.md`). |
| evt-2026-0018 | 2026-05-13T12:00:00Z | triumph-manipulator-landing | registry.updated | Triumph project pack + workspace placeholder registered **planned**; Website Factory reference case linkage; **not** deployed site. Timestamp aligned to registry row date (approximate session time — see `logs/cleanup/actions/lifecycle-backfill-review-v1.md`). |
| evt-2026-0019 | 2026-05-18T12:00:00Z | orca | registry.updated | ORCA registered **active** as human-supervised PPC operational toolkit; runtime **excluded** per registry boundaries. Timestamp aligned to registry row date (approximate session time — see `logs/cleanup/actions/lifecycle-backfill-review-v1.md`). |
| evt-2026-0020 | 2026-05-19T12:00:00Z | wpilot | registry.updated | WPilot registered **active** (External Systems lane); Phase 1 MVP documentation; plugin bridge **planned**; **not** MARS runtime. Timestamp aligned to registry row date (approximate session time — see `logs/cleanup/actions/lifecycle-backfill-review-v1.md`). |
| evt-2026-0021 | 2026-05-19T18:00:00Z | governance | governance.structural_stabilization_phase_1 | Phase 1 stabilization documentation pass (topology index, Factory navigation compression review, Forge transition notes, external-systems relationship map, structural coherence audit) — **documentation only**; per `governance/lifecycle-synchronization-review-v0.md` backlog. Timestamp approximate — exact operator session time **SAFE UNKNOWN**. |
| evt-2026-0022 | 2026-06-05T12:00:00Z | ops | registry.updated | **OPS** registered in `registry/project-registry.md` (`project_id` **ops**, status **planned**); ecosystem topology and reality index updated; registration evidence `logs/ops/ops-registration-v1.md`; Foundation, Data Model, Workflow Architecture, Mission Layer, Registration Assessment, WF-01 Pilot and Alignment completed — **no** runtime, automation, ATLAS foundation edits, or workflow redesign. |
| evt-2026-0023 | 2026-06-09T12:00:00Z | site-002 | registry.updated | **SITE-002** (ЗПМ) registered in OCPilot `project-site-registry.md`; repo container `projects/ocpilot/sites/site-002/` and external bulk `C:\AI MARS STORAGE\ocpilot\project-sites\site-002\` prepared; status **AWAITING INTAKE**; evidence `logs/ocpilot/site-002-registration-v1.md` — **no** site connection, audit, FTP scan, or credentials in git. |
| evt-2026-0024 | 2026-06-04T12:00:00Z | atlas | registry.updated | **ATLAS** registered in `registry/project-registry.md` (`project_id` **atlas**, status **planned**); Cross-Cutting Registry Infrastructure — Business Reality Registry; foundation Phase 1 complete under `projects/atlas/foundation/`; ecosystem topology updated; registration evidence `logs/atlas/atlas-registration-v1.md` — **no** runtime, persistence engine, CRM/ERP, or consumer API implementation. Backfill per Awareness Alignment Pass 2026-06 (audit gap vs `ops` evt-2026-0022). |

---

## Append-only rule

1. **Append only** — Add new rows to the bottom of the table; do not reorder historical rows for convenience.
2. **Integrity** — Prefer immutable **event_id** values; never reuse an **event_id**.
3. **Cross-reference** — For project-scoped events, **entity_id** should align with **project_id** in `registry/project-registry.md` when the subject is a project.
