# MARS — Ecosystem topology index

**Status:** **documented** — compact canonical visibility layer.  
**Version:** v0 (Structural Stabilization Phase 1).  
**Date:** 2026-06-02 (entity sync pass v1 — post-cycle8 systems visibility).  
**Supersedes:** nothing — **navigation aid** only; does not override `AGENTS.md`, registries, or pack READMEs.

**Not:** an ontology, semantic graph, registry engine, or runtime map.

**Post–Cycle 8 (2026-05-19):** stabilization baseline **achieved**; governance **maintenance mode**; default work is **operational-first** — [mars-operational-evolution-state-after-cycles-1-8-v0.md](mars-operational-evolution-state-after-cycles-1-8-v0.md).

**Tier 1 (ecosystem routing only)** — use when the question is *where entities live*; **not** parallel to [mars-reality-index-v0.md](mars-reality-index-v0.md) (pick **one** Tier 1 router per session). **After:** [AGENTS.md](../AGENTS.md). **Deep audit:** [mars-v2-structural-coherence-audit-v0.md](mars-v2-structural-coherence-audit-v0.md). **Tier model:** [survivability-canonical-entrypoint-model-v0.md](survivability-canonical-entrypoint-model-v0.md).

---

## How to use

**Pick-one rule:** If you already opened [mars-reality-index-v0.md](mars-reality-index-v0.md) this session, **do not** also read this file end-to-end — use the index that matches your question (placement **here** vs bucket **there**).

| Column | Meaning |
|--------|---------|
| **Operational status** | Human-maintained posture today — **not** deployed-product proof. |
| **Canonical path** | Where identity and boundaries are defined. |
| **Relationship role** | How this entity relates to MARS — **not** ownership of external runtimes. |

**Registry row ≠ runtime.** **Pack folder ≠ shipped product.**

---

## Topology (compact)

```text
AGENTS.md (honesty)
  └─ governance/          ← spine, boundaries, survivability
  └─ registry/ + agents/registry.md + tools/registry.md
  └─ projects/*         ← program / project packs
  └─ agents/*           ← operational doc packs + planned cards
  └─ mars-runtime/      ← contracts + narrow R1 experiments
  └─ continuity/        ← IdeaBox (human discipline)
  └─ workspaces/      ← local execution locus (not SoT)
  └─ web-gpt-sources/   ← legacy import (not live layout truth)
```

---

## Major entities

### MARS Core (contract layers)

| | |
|--|--|
| **What it is** | Documentation-first **contract folders** for control plane, workflows, interfaces, security, tools, models, storage, memory, observability, evaluation, integrations — plus narrow **R1** experiments under `mars-runtime/`. |
| **What it is NOT** | A shipped multi-agent platform, production runtime, orchestrator, or policy engine. |
| **Operational status** | **Conceptual / experimental** — contracts **operational** as human-maintained docs; R1 JS **experimental** only. |
| **Canonical path** | Layer READMEs at repo root; roadmap [master-build-map.md](master-build-map.md); runtime contracts [../mars-runtime/README.md](../mars-runtime/README.md). |
| **Relationship role** | **Design vocabulary** and future-integration boundaries for the ecosystem; **does not** execute Website Factory or external systems. |

---

### Governance

| | |
|--|--|
| **What it is** | Human-maintained **control documentation**: boundaries, execution model, registries rules, survivability (S1–S7), reality audit, frontend consolidation maps. |
| **What it is NOT** | Automated enforcement, CI substitute, certification product, or live telemetry. |
| **Operational status** | **Operational** (documentation discipline) — **maintenance mode** post–Cycle 8; not default session work product. |
| **Canonical path** | [mars-operational-evolution-state-after-cycles-1-8-v0.md](mars-operational-evolution-state-after-cycles-1-8-v0.md), [README.md](README.md) (one row), [current-operational-state-v1.md](current-operational-state-v1.md). |
| **Relationship role** | **Spine** for honesty, naming, registry precedence, and anti-mythology across all lanes. |

---

### MARS Website Factory

| | |
|--|--|
| **What it is** | Largest **program pack**: documentation-first multi-agent **website production methodology** (workflows, artifacts, semantics, QA/HITL, reference-project layer). |
| **What it is NOT** | Runtime-ready factory engine, autonomous site builder, or in-repo deployment platform. |
| **Operational status** | **Strategic planned** — methodology **operational** for human/Cursor work; execution engine **excluded**. |
| **Canonical path** | [../projects/mars-website-factory/README.md](../projects/mars-website-factory/README.md); navigation [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md); registry `mars-website-factory`. |
| **Relationship role** | **Upstream contracts** for frontend handoff, agent ids (§4.1), and reference cases; consumes governance; points to WPilot as **future** WordPress bridge. |

---

### MARS Forge

| | |
|--|--|
| **What it is** | **Thin overlay** operational doc pack on `gulp_frontend_agent` — phased pipeline, freeze, anti-drift, overlay QA checklists. |
| **What it is NOT** | Second Gulp SoT, autonomous build bot, orchestration layer, or pixel-perfect engine (v0). |
| **Operational status** | **Operational doc pack** (`operational_doc_pack`) — human + Cursor/Codex only. |
| **Canonical path** | [../agents/mars-forge/README.md](../agents/mars-forge/README.md); card [../agents/cards/mars-forge-frontend-agent-v0.md](../agents/cards/mars-forge-frontend-agent-v0.md); transition notes [mars-forge-transition-stabilization-v0.md](mars-forge-transition-stabilization-v0.md). |
| **Relationship role** | **Extends** Gulp foundation + Factory contracts; **does not** replace them. Older design-only docs are **historical precedent** — see transition doc. |

---

### Frontend production (Gulp lane)

| | |
|--|--|
| **What it is** | **Canonical foundation** for static frontend implementation: `frontend-gulp-agent` pack + Factory `frontend-*` contracts + `workspaces/*` as execution locus. |
| **What it is NOT** | MARS-owned gulp-starter repo, CI proof, or workspace paths as governance SoT. |
| **Operational status** | **Operational doc pack** + external project execution. |
| **Canonical path** | [../agents/frontend-gulp-agent/README.md](../agents/frontend-gulp-agent/README.md); [frontend-legacy-and-foundation-map-v0.md](frontend-legacy-and-foundation-map-v0.md); [../projects/mars-website-factory/frontend-production-rules-v0.md](../projects/mars-website-factory/frontend-production-rules-v0.md). |
| **Relationship role** | **Production lane** for Factory Stage 11; Forge overlays this lane; Triumph and reference cases stress-test discipline. |

---

### Runtime research (`mars-runtime/`)

| | |
|--|--|
| **What it is** | Stage 8.5+ **architecture contracts** plus **narrow R1** JavaScript (bridge, adapters, tool-registry experiments, run-state JSON). |
| **What it is NOT** | Full MARS runtime, control plane implementation, or proof of autonomous agents. |
| **Operational status** | **Conceptual contracts** + **experimental R1** — highest mythology-pressure zone. |
| **Canonical path** | [../mars-runtime/README.md](../mars-runtime/README.md), [../mars-runtime/architecture-map.md](../mars-runtime/architecture-map.md); boundaries [runtime-registry-boundaries.md](runtime-registry-boundaries.md). |
| **Relationship role** | **Future-integration sketches** and demos; adapters **≠** external system ownership (see [external-systems-relationship-map-v0.md](external-systems-relationship-map-v0.md)). |

---

### MetaBOT — SEO Content Agent

| | |
|--|--|
| **What it is** | **External** multi-workflow operational system (n8n Intake/Worker/Admin); **canonical in-repo docs** only. |
| **What it is NOT** | MARS core runtime, in-repo orchestration, or duplicate of n8n graphs. |
| **Operational status** | **Active** (documentation pack); **execution external** (live n8n is SoT for graphs). |
| **Canonical path** | [../projects/metabot-seo-content-agent/README.md](../projects/metabot-seo-content-agent/README.md); registry `metabot-seo-content-agent`; boundaries [external-system-boundaries.md](external-system-boundaries.md). |
| **Relationship role** | **External systems lane**; legacy `seo-content-agent` is **do-not-extend**; R1 adapter is experimental label only. |

---

### ORCA

| | |
|--|--|
| **What it is** | Human-supervised **PPC operational toolkit** and live review framework (methodology, heuristics, fast-path, pilots). |
| **What it is NOT** | Autonomous bidding, scheduling, validator daemon, or MARS runtime component. |
| **Operational status** | **Operational** (documentation / human workflow); **runtime excluded**. |
| **Canonical path** | [../projects/orca/README.md](../projects/orca/README.md), [OPERATIONAL-INDEX.md](../projects/orca/OPERATIONAL-INDEX.md); registry `orca`. |
| **Relationship role** | **Mostly self-contained** program pack under `projects/`; uses MARS governance honesty, not MARS execution engine. |

---

### GitGuard

| | |
|--|--|
| **What it is** | **Named example** of a Program / Operational System in [system-entity-model.md](system-entity-model.md) — **no** `projects/gitguard/` pack observed in-repo at Phase 1 stabilization. |
| **What it is NOT** | A registered MARS project, runtime module, or evidenced subsystem in this tree. |
| **Operational status** | **SAFE UNKNOWN** at registry level — treat as **conceptual / future** until a pack and registry row exist. |
| **Canonical path** | Entity model example only; **no** canonical project path yet. |
| **Relationship role** | **Placeholder taxonomy** — do not cite as live ecosystem member without evidence. |

---

### WPilot

| | |
|--|--|
| **What it is** | Human-supervised **WordPress administration** operational system (Phase 1 MVP docs + **planned** plugin bridge docs). External Systems lane. |
| **What it is NOT** | Autonomous WP admin, MARS runtime, deploy bot, or production bridge (plugin is **planned** documentation only). |
| **Operational status** | **Operational** (Phase 1 documentation discipline); plugin MVP **planned**. |
| **Canonical path** | [../projects/wpilot/README.md](../projects/wpilot/README.md); registry `wpilot`; plugin reconciliation [../projects/wpilot/plugin-mvp/reconciliation-map-v0.md](../projects/wpilot/plugin-mvp/reconciliation-map-v0.md). |
| **Relationship role** | **Future** Factory-native WordPress handoff target; **Mode B** legacy compatibility; uses Beget/WordPress **outside** MARS ownership. |

---

### MIG (Market Intelligence Groundtruth)

| | |
|--|--|
| **What it is** | **R1** market groundtruth research acquisition layer — session manifests, evidence grading, handoff packs; **narrow v0.1** session spine (Node.js + n8n export) in-repo. |
| **What it is NOT** | Production orchestration, autonomous ORCA handoff, full SERP/competitor pipeline (mostly **planned**), or MARS core runtime. |
| **Operational status** | **Operational** (human-supervised acquisition); v0.1 tooling **experimental**; production n8n deployment **not proven**. |
| **Canonical path** | [../projects/mig/README.md](../projects/mig/README.md), [OPERATIONAL-INDEX.md](../projects/mig/OPERATIONAL-INDEX.md); registry `mig`. |
| **Relationship role** | **MIG acquires reality; ORCA interprets reality** — human-only handoff per mig-orca contract; upstream of PPC interpretation, not campaign engine. |

---

### OCPilot

| | |
|--|--|
| **What it is** | Human-supervised **OpenCart / ocStore** operational pack (External Systems lane): read-only audit, baselines, site passport, controlled-change discipline. CMS/Ecommerce Pilots family **sibling** to WPilot. |
| **What it is NOT** | WPilot child, MARS runtime, autonomous OpenCart admin, deploy bot, or in-repo plugin/runtime proof. |
| **Operational status** | **Operational** (Phase 0+ documentation baseline); live site access **external**. |
| **Canonical path** | [../projects/ocpilot/README.md](../projects/ocpilot/README.md), [OPERATIONAL-INDEX.md](../projects/ocpilot/OPERATIONAL-INDEX.md); registry `ocpilot`. |
| **Relationship role** | **Future** ecommerce CMS bridge; may consume **EAR Runtime** snapshots when chartered; shares external-access patterns with WPilot — **not** WPilot-owned. |

---

### EAR Runtime

| | |
|--|--|
| **What it is** | **Engineering project** for Mode 2 acquisition helpers (connectors, evidence, snapshots) — separate from frozen EAR Architecture in `shared/external-access-runtime/`. |
| **What it is NOT** | EAR Architecture normative layer, `mars-runtime/` control plane, live SFTP/production acquisition, or OCPilot site analysis. |
| **Operational status** | **Engineering started** — R1 skeleton + config loader only; connector **not started**; human R1 approval **pending**. |
| **Canonical path** | [../projects/ear-runtime/README.md](../projects/ear-runtime/README.md), [OPERATIONAL-INDEX.md](../projects/ear-runtime/OPERATIONAL-INDEX.md), [EAR-RUNTIME-STATE.md](../projects/ear-runtime/EAR-RUNTIME-STATE.md); registry `ear-runtime`. |
| **Relationship role** | Implements chartered helpers **conforming** to EAR Architecture; publishes snapshots for OCPilot / future WPilot — **consumers do not own acquisition mechanics**. |

---

### MARS Survivability

| | |
|--|--|
| **What it is** | Operational **safety domain** pack: destructive-ops policy, safe execution layer, Cursor guardrails, protected zones, human-invoked validator/helpers, drill reports. |
| **What it is NOT** | Automated policy engine, CI substitute, GitGuard product, or replacement for `governance/operational-survivability.md` or `AGENTS.md`. |
| **Operational status** | **Operational** (documentation + human-invoked tools); enforcement is **human-operated**. |
| **Canonical path** | [../projects/mars-survivability/README.md](../projects/mars-survivability/README.md), [OPERATIONAL-INDEX.md](../projects/mars-survivability/OPERATIONAL-INDEX.md); registry `mars-survivability`. |
| **Relationship role** | **Extends** post–Cycle 8 survivability discipline across Factory, agents, and git workflows; GitGuard remains **design contract** until separate pack exists. |

---

### NOVA (Mobile Application Factory)

| | |
|--|--|
| **What it is** | Documentation-first **mobile / PWA production methodology** (RBM foundation v1) — vocabulary counterpart to Website Factory. |
| **What it is NOT** | Runtime, agent engine, orchestration product, governance system, or implemented factory. |
| **Operational status** | **Foundation complete** — implementation and agent cards **not started** (`planned` registry band). |
| **Canonical path** | [../projects/nova/README.md](../projects/nova/README.md), [NOVA-FOUNDATION-STATUS-v1.md](../projects/nova/NOVA-FOUNDATION-STATUS-v1.md); registry `nova`. |
| **Relationship role** | **Methodology parallel** to Website Factory for mobile domain; no OPERATIONAL-INDEX yet — README + foundation status suffice at current scale. |

---

### Continuity / IdeaBox

| | |
|--|--|
| **What it is** | Filesystem-backed **human-operated** continuity workflow — ideas, lightweight protocols, manual index. |
| **What it is NOT** | Autonomous memory, semantic graph, orchestration, or governance auto-mutation. |
| **Operational status** | **Operational** (discipline). |
| **Canonical path** | [../continuity/README.md](../continuity/README.md); manual index [../continuity/registry/master-index.md](../continuity/registry/master-index.md); **not** a `project_id` row. |
| **Relationship role** | **Optional** anti-entropy complement to governance [context-continuity-rules.md](context-continuity-rules.md). |

---

### External systems (collective lane)

| | |
|--|--|
| **What it is** | Systems whose **execution truth** lives outside the repo: n8n (MetaBOT), WordPress/Beget (WPilot), hosting, Telegram, Sheets, etc. |
| **What it is NOT** | Subsystems owned or dispatched by MARS core runtime. |
| **Operational status** | **Operational** where human workflows exist; integration depth varies per system. |
| **Canonical path** | [external-systems-relationship-map-v0.md](external-systems-relationship-map-v0.md), [external-system-boundaries.md](external-system-boundaries.md), [system-boundaries.md](system-boundaries.md). |
| **Relationship role** | **Boundary layer** — MARS holds contracts and operator discipline; **live consoles** hold execution truth. |

---

### Reference projects (Factory layer)

| | |
|--|--|
| **What it is** | **Documentation methodology** for reference / production / sandbox project kinds, artifact trees, QA matrix, delivery packages — plus in-repo **reference cases** (e.g. Triumph). |
| **What it is NOT** | Project database, orchestration engine, or proof that reference runs executed in production. |
| **Operational status** | **Conceptual / operational methodology** — templates and cases for human-supervised runs. |
| **Canonical path** | [../projects/mars-website-factory/reference-project-model-v0.md](../projects/mars-website-factory/reference-project-model-v0.md); case [../projects/mars-website-factory/reference-cases/triumph-manipulator-landing/](../projects/mars-website-factory/reference-cases/triumph-manipulator-landing/); project row `triumph-manipulator-landing`. |
| **Relationship role** | **Calibration** for Factory semantics; workspaces hold implementation attempts — version authority is **operator-managed** (see compression review). |

---

## Canonical truth locations (quick)

| Question | Authoritative surface |
|----------|----------------------|
| Project identity? | [../registry/project-registry.md](../registry/project-registry.md) |
| Agent role ids? | [../agents/registry.md](../agents/registry.md) |
| Tool row semantics? | [../tools/registry.md](../tools/registry.md) |
| Governance precedence? | [registry-source-of-truth.md](registry-source-of-truth.md) |
| “What runs today?” honesty? | [AGENTS.md](../AGENTS.md), [execution-model.md](execution-model.md) |
| Pack-local navigation? | Each `projects/*/README.md` or `OPERATIONAL-INDEX.md` |
| Lifecycle events? | [../logs/lifecycle-log.md](../logs/lifecycle-log.md) (events, not implementation proof) |

---

## Related stabilization artefacts (Phase 1)

| Doc | Role |
|-----|------|
| [mars-forge-transition-stabilization-v0.md](mars-forge-transition-stabilization-v0.md) | Forge design → pack transition |
| [website-factory-compression-review-v0.md](website-factory-compression-review-v0.md) | Factory density / duplication signals |
| [external-systems-relationship-map-v0.md](external-systems-relationship-map-v0.md) | External operational systems |

## Related stabilization artefacts (post–Cycle 8)

| Doc | Role |
|-----|------|
| [mars-operational-evolution-state-after-cycles-1-8-v0.md](mars-operational-evolution-state-after-cycles-1-8-v0.md) | **Canonical** ecosystem posture after Cycles 1–8 |
| [mars-ecosystem-state-synchronization-review-v0.md](mars-ecosystem-state-synchronization-review-v0.md) | Continuity / deprecated assumptions (sync pass) |
| [mars-operational-evolution-transition-index-v0.md](mars-operational-evolution-transition-index-v0.md) | Pick-one transition task routing |

## Related stabilization artefacts (Phase 2)

| Doc | Role |
|-----|------|
| [mars-reality-index-v0.md](mars-reality-index-v0.md) | **Tier 1 router** when the question is bucket-oriented reality (operational vs conceptual vs …) — pick **one** with this index per session |
| [lifecycle-synchronization-review-v0.md](lifecycle-synchronization-review-v0.md) | Lifecycle log vs registry gaps |
| [website-factory-navigation-compression-strategy-v0.md](website-factory-navigation-compression-strategy-v0.md) | Factory nav compression tiers |
| [runtime-mythology-pressure-review-v0.md](runtime-mythology-pressure-review-v0.md) | Runtime vocabulary pressure relief |
| [cross-system-clarity-review-v0.md](cross-system-clarity-review-v0.md) | Cross-system boundary pairs |

---

*Structural Stabilization Phase 1 — compact map only; expand via governed registry rows, not via new ontology layers. Phase 2 reality index: [mars-reality-index-v0.md](mars-reality-index-v0.md).*
