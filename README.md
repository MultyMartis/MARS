# MARS

**Multi-Agent Runtime System**

**Navigation (Tier 0–3):** honesty — this file + [`AGENTS.md`](AGENTS.md); **post–Cycle 8 posture** — [`governance/mars-operational-evolution-state-after-cycles-1-8-v0.md`](governance/mars-operational-evolution-state-after-cycles-1-8-v0.md) (governance **maintenance mode**, **operational-first** default); ecosystem question — **one** of [`governance/ecosystem-topology-index.md`](governance/ecosystem-topology-index.md) or [`governance/mars-reality-index-v0.md`](governance/mars-reality-index-v0.md); pack work — pack README → OPERATIONAL-INDEX **Core Run**. Model: [`governance/survivability-canonical-entrypoint-model-v0.md`](governance/survivability-canonical-entrypoint-model-v0.md).

This directory is the **main local working copy** of the MARS project: design notes, the Phase 1 documentation pack, **v0 contracts and minimal experimental R1** JavaScript under [`mars-runtime/`](mars-runtime/), and **future** broader implementation as phases progress. The repository remains **primarily documentation-first**; R1 is narrow and **not** a full production runtime (see **Planned implementation** below).

## Operator infrastructure (physical)

| Layer | Path | Role |
|-------|------|------|
| **Workspace root** | `C:\AI MARS` | This git repository — governance, projects, workspaces, docs. |
| **Bulk storage** | `C:\AI MARS STORAGE` | Out-of-git bulk (baselines, archives, snapshots). **Not** a second repo or MARS instance. |

Canonical reference: [`governance/mars-infrastructure-reality-v1.md`](governance/mars-infrastructure-reality-v1.md). In-repo [`storage/`](storage/) is **documentation** for the architecture Storage Layer — not the physical `C:\AI MARS STORAGE` path.

## What this repository contains (by status)

### Documented architecture

- Design and system documentation is maintained as Markdown under [`web-gpt-sources/`](web-gpt-sources/).  
- **Status:** **documented** — these files describe the intended shape of MARS (layers, components, security, observability, interfaces, rules, migration, roadmap). They are **documentation**, not a guarantee that any particular piece is implemented.

### Planned implementation

- A production-grade multi-agent runtime, services, agents, tools, storage integrations, and deployment assets are **planned** for later phases.  
- **Status:** **planned** for the full system — this repository is **primarily documentation-first** in Phase 1. It also contains **minimal experimental R1** JavaScript under [`mars-runtime/`](mars-runtime/) that demonstrates a **narrow** task → bridge → adapter → webhook flow. R1 is **not** a full MARS runtime, **not** production-ready, and does **not** imply that the complete planned implementation exists in-tree.

### Legacy / imported material

- The `web-gpt-sources/` pack originated as a **Web-GPT** documentation import: it is **legacy imported** reference material used to bootstrap the written architecture. Treat it as input to the design; it may be revised, split, or replaced as MARS evolves.

## Current phase

**Phase 1 — documentation-first** (see `governance/master-build-map.md`, `logs/lifecycle-log.md`, `AGENTS.md`).

| Kind | What it means here |
|------|---------------------|
| **Documented** | Markdown contracts and governance artefacts in-repo; normative **for documentation**, not proof of runnable product. |
| **Planned** | Full multi-agent runtime, services, enforcement engines, and most adapters — **not** evidenced as shipped in this tree unless a path is cited. |
| **Experimental R1** | Narrow JavaScript under `mars-runtime/` (task → bridge → adapter → webhook demos). **Not** a full MARS runtime; **not** production; **not** autonomous orchestration or an implemented control plane. |
| **Operationally verified** | **Human-controlled** repo work (e.g. editor + local shell) per `governance/execution-model.md`. **Not** a claim that MARS core **automates** or **verifies** end-to-end product behaviour in-repo. |

- **Documentation progression:** **Stage 7.5** consistency gate and **Stage 8.5** Runtime Readiness **P0** contracts are **closed** in governance (`logs/lifecycle-log.md` **evt-2026-0002**, **evt-2026-0003**). **Documentation milestones** for **Stages 9–15** are **recorded** in the lifecycle log (**evt-2026-0004**–**evt-2026-0010**); **per-stage** labels (**`partial-docs`**, **`near-complete-docs`**, residuals) stay **authoritative** in `governance/master-build-map.md` — those stages are **not** “fully implemented MARS.”  
- **Next (governance / roadmap):** **Stage 16 — Pilot** remains **`planned-docs`** until a pilot is chartered in registry + lifecycle; until then, follow each stage’s **Next required action** and residual rows in `governance/master-build-map.md` (ongoing contract hygiene, risk/dependency updates when scope changes).  
- **Implementation boundary:** There is **no** full production **MARS** runtime, services stack, or application platform evidenced here. **Minimal R1** code exercises only a **narrow** handoff path; queues, schedulers, durable MARS run state, and model routing remain **external** or **`planned-implementation`** per `AGENTS.md`.

## Repository layout

**Do not depth-first explore this table** — use [`governance/ecosystem-topology-index.md`](governance/ecosystem-topology-index.md) for entity placement, or a pack **OPERATIONAL-INDEX** **Core Run** for live work.

| Path | Role |
|------|------|
| `governance/` | Boundaries, execution/state/versioning models, capability map, **master build map**; [`governance/enforcement/`](governance/enforcement/README.md) (Phase S1 **documentation-only** review aids); parallel chat lanes ([`governance/parallel-cursor-chat-work-mode-v0.md`](governance/parallel-cursor-chat-work-mode-v0.md)) |
| `registry/` | **Project registry** and other registry-style anchors (`project-registry.md`) |
| `projects/` | **Project / program packs** — e.g. `projects/mars-website-factory/` (**strategic planned**, doc-first website production); `projects/orca/` (**operational** PPC toolkit, runtime **excluded**); `projects/wpilot/` (**operational** WordPress admin discipline, External Systems lane, plugin **planned**); `projects/metabot-seo-content-agent/` (**canonical** MetaBOT pack, **external** n8n execution); `projects/seo-content-agent/` (**legacy** — do not extend). Compact map: [`governance/ecosystem-topology-index.md`](governance/ecosystem-topology-index.md) |
| `logs/` | **Lifecycle log** (documented lifecycle events, append-only discipline) |
| `control-plane/` | Control plane contract and components (documentation) |
| `agents/` | Agent registry, cards, factory/builder documentation |
| `workflows/` | Task contract, workflow standard, execution flow, failure model (MARS-native contracts) |
| `interfaces/` | Introspection, self-check, self-audit, self-describe, self-heal, recovery playbooks (v0 contracts) |
| `security/` | Security README and MARS-native security/threat/permissions contracts (documentation) |
| `tools/` | Tool layer placeholder and future tool-registry contracts |
| `models/` | Model layer placeholder and future provider-routing contracts |
| `storage/` | Storage / checkpoint / runtime-state **documentation** (contracts; no adapters) |
| `memory/` | Memory **documentation** and memory-write policy (contracts) |
| `observability/` | Observability placeholder and future contracts |
| `evaluation/` | Evaluation placeholder and future contracts |
| `mars-runtime/` | v0 **architecture contracts** (e.g. architecture map, **Execution Bridge v0**) **and** **minimal experimental R1** JavaScript (narrow task → bridge → adapter → webhook demo; **not** a full production runtime) |
| `shared/` | **Shared local files** for frontends (e.g. Font Awesome checkout for icon reference on this machine; **not** governance, **not** `mars-runtime/`). See [`shared/README.md`](shared/README.md); usage note [`shared/assets/icon-libraries/fontawesome-pro-5.15.4-usage.md`](shared/assets/icon-libraries/fontawesome-pro-5.15.4-usage.md). **Licensing-sensitive** — selective, agreement-bound use; do not commit the whole vendor tree unless policy explicitly allows. |
| `web-gpt-sources/` | Numbered topic Markdown files (system, architecture, core, agents, …) — **legacy imported** pack |

---

*Last updated: 2026-05-19 — **post–Cycle 8 ecosystem sync:** operational-first default, governance maintenance mode — [`governance/mars-operational-evolution-state-after-cycles-1-8-v0.md`](governance/mars-operational-evolution-state-after-cycles-1-8-v0.md). Prior **2026-05-15** — **`shared/`** row and controlled asset-layer note added (see `shared/README.md`). Prior **2026-05-14** — **Phase S0 truth repair:** root README aligned with `logs/lifecycle-log.md` (Stages **9–15** documentation **milestones** recorded **2026-04-28**) and per-stage tables in `governance/master-build-map.md`; **`planned-docs` / `partial-docs` / `near-complete-docs`** semantics unchanged; **no** runtime-completion claim. Prior notes: `projects/mars-website-factory/` (**strategic planned**, doc-first); `projects/metabot-seo-content-agent/` (**canonical** MetaBOT pack); `projects/seo-content-agent/` (**legacy**); **minimal R1** under `mars-runtime/` only — **no** full MARS production runtime in-repo.*
