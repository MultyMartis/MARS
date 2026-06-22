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
  └─ continuity/        ← IdeaBox (optional incubation)
  └─ incoming/        ← ecosystem intake (hybrid — Active Brain staging)
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
| **Relationship role** | **Upstream contracts** for frontend handoff, agent ids (§4.1), and reference cases; consumes governance; points to WPilot as **future** WordPress bridge. **Execution cases:** [execution-cases-registry-v1.md](../projects/mars-website-factory/execution-cases-registry-v1.md) (Triumph, ISBD, BZPM). **Physical records:** [../workspaces/website-factory-operations/](../workspaces/website-factory-operations/) LOC-ZONE (see § Website Factory LOC-ZONE). |

---

### MARS Forge

| | |
|--|--|
| **What it is** | **Thin overlay** operational doc pack on `gulp_frontend_agent` — phased pipeline, freeze, anti-drift, overlay QA checklists. |
| **What it is NOT** | Second Gulp SoT, autonomous build bot, orchestration layer, pixel-perfect engine (v0), **or Forge WordPress** (WordPress implementation subsystem). |
| **Operational status** | **Operational doc pack** (`operational_doc_pack`) — human + Cursor/Codex only. |
| **Canonical path** | [../agents/mars-forge/README.md](../agents/mars-forge/README.md); card [../agents/cards/mars-forge-frontend-agent-v0.md](../agents/cards/mars-forge-frontend-agent-v0.md); transition notes [mars-forge-transition-stabilization-v0.md](mars-forge-transition-stabilization-v0.md). |
| **Relationship role** | **Extends** Gulp foundation + Factory contracts; **does not** replace them. Older design-only docs are **historical precedent** — see transition doc. |

---

### Forge WordPress

| | |
|--|--|
| **What it is** | **Website Factory subsystem** — documentation-first WordPress **implementation** methodology (frontend package → WordPress implementation package → WPilot handoff). Operator alias: WP Forge. |
| **What it is NOT** | MARS Forge (frontend overlay), WPilot (operations), registered agent, `project_id`, runtime, theme/plugin implementation at FOUNDATION. |
| **Operational status** | **FOUNDATION** (FW-00 complete) — **not** operational, **not** architecture-started, **not** implementation-started. |
| **Canonical path** | [../projects/mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md](../projects/mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md); seed [AG-WP-001](../workspaces/website-factory-operations/internal-agent-seeds/AG-WP-001-forge-wordpress/). |
| **Relationship role** | **Candidate WordPress Implementation Layer** downstream of approved Factory frontend; upstream of WPilot operations. Internal seed **AG-WP-001** — not `agents/registry.md`. |

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
| **Relationship role** | **Interpretation layer** for PPC decisions: consumes human-approved MIG groundtruth where used, can hand off validated strategy/semantic outputs to Website Factory when that lane is selected, and remains operable without Factory on existing-client landing sources. |

---

### GitGuard

| | |
|--|--|
| **What it is** | **REGISTERED** **Repository Survivability Layer** — survivability advisory framework (checkpoint/freeze/rollback/baseline visibility, backup intelligence, release traceability) implemented under [../projects/mars-survivability/](../projects/mars-survivability/); also a **Program / Operational System** example name in [system-entity-model.md](system-entity-model.md). |
| **What it is NOT** | A `project_id` row, `projects/gitguard/` pack, autonomous backup service, or replacement for `GIT CHECKPOINT NEEDED` process signals ([system-signals-dictionary.md](system-signals-dictionary.md)). |
| **Operational status** | **REGISTERED** cross-cutting (Wave 2B) — **operational (human-operated)** via `mars-survivability`; **no** separate `project_id`. |
| **Canonical path** | [../projects/mars-survivability/registries/gitguard-system-entry-v1.md](../projects/mars-survivability/registries/gitguard-system-entry-v1.md); registry note [../registry/project-registry.md](../registry/project-registry.md); reality: [mars-reality-index-v0.md](mars-reality-index-v0.md) § GitGuard. |
| **Relationship role** | **Extends** post–Cycle 8 survivability discipline; complements [operational-survivability.md](operational-survivability.md) and program `mars-survivability` — **not** a parallel runtime. Evidence: [../logs/cleanup/actions/gitguard-registration-v1.md](../logs/cleanup/actions/gitguard-registration-v1.md). |

---

### WPilot

| | |
|--|--|
| **What it is** | **First proven CMS Pilot runtime reference implementation** in MARS — human-supervised WordPress administration (Phase 1 docs + DEV plugin `metacode-wpilot` v0.3.0-RC5 proven on DEV). External Systems lane. |
| **What it is NOT** | Autonomous WP admin, MARS runtime, deploy bot, production bridge, active MVP development target, or Sprint 3 authorization from RC5 freeze alone. |
| **Operational status** | **Reference Implementation** — `proven_content_writes` + `proven_connection_runtime` on DEV (`https://dev.gktriumph.ru`); human-supervised only. Authority: `WPILOT-RC5-PROVEN-CONNECTION-RUNTIME-2026-06-19`; commit `648632acbdd42703427fd76a0cb1fd8d88641dcc`. RC5 development focus **closed**. Sprint 3 **HOLD**. |
| **Canonical path** | [../projects/wpilot/WPILOT-FINAL-STATE-RC5.md](../projects/wpilot/WPILOT-FINAL-STATE-RC5.md); [../projects/wpilot/OPERATIONAL-INDEX.md](../projects/wpilot/OPERATIONAL-INDEX.md); [../projects/wpilot/README.md](../projects/wpilot/README.md); registry `wpilot`; RC5 [../projects/wpilot/WPILOT-RELEASE-CANDIDATE-v0.3.0-RC5.md](../projects/wpilot/WPILOT-RELEASE-CANDIDATE-v0.3.0-RC5.md). |
| **Relationship role** | **Reference runtime** and **validation source** for CMS Pilot family; **future** Factory-native WordPress handoff target; **Mode B** legacy compatibility; uses Beget/WordPress **outside** MARS ownership. Token storage: `C:\AI MARS\local\tokens\wpilot-dev-gktriumph.token` (local-only; no value in repo). |

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
| **Relationship role** | **Future** ecommerce CMS bridge; may consume **EAR Runtime** snapshots when chartered; shares external-access patterns with WPilot — **not** WPilot-owned. **Sites:** site-001 (Triumph-related operational context) and **site-002 (ЗПМ)** registered in OCPilot local registry (`evt-2026-0023`) — not separate `project_id` rows. |

---

### Website Factory LOC-ZONE (`website-factory-operations/`)

| | |
|--|--|
| **What it is** | **LOC-ZONE** — Authorized Records filesystem root for Factory structured records (RT-G04/RT-G05 physical artifact plane). Portfolio catalog ROC-01; pilot **FP-0001** (REG-0001) Waves 1–3 **complete**; **FP-0002** (Shpigovsky) material present — **not** ROC-01 enrolled (visibility only). Internal agent seed **AG-WP-001** (Forge WordPress) lives under `internal-agent-seeds/` — canonical methodology home: [subsystems/forge-wordpress/](../projects/mars-website-factory/subsystems/forge-wordpress/). |
| **What it is NOT** | Second Factory methodology SoT (doctrine stays in `website-factory-reference-v1/`); `project_id` row; runtime or automation product; replacement for `execution-cases-registry-v1.md`. |
| **Operational status** | **Operational** (human-maintained records) — Waves 1–3 complete on FP-0001; FP-0002 foundation active. |
| **Canonical path** | [../workspaces/website-factory-operations/README.md](../workspaces/website-factory-operations/README.md); catalog [ROC-01-catalog-aggregate.md](../workspaces/website-factory-operations/POC-02-registry-facet/ROC-01-catalog-aggregate.md). |
| **Relationship role** | **Physical artifact plane** for Factory operations; **ATLAS-aware** (FP-0001/FP-0002 bind ORG/PRJ/WEB ids where attested); complements `projects/mars-website-factory/` methodology pack and `projects/website-factory/` BZPM execution case tree. |

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
| **Relationship role** | **Extends** post–Cycle 8 survivability discipline across Factory, agents, and git workflows; **implements** registered **GitGuard** direction (see § GitGuard — no `projects/gitguard/` pack). |

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

### ATLAS (Business Reality Registry)

| | |
|--|--|
| **What it is** | **Cross-Cutting Registry Infrastructure** — documentation-first **Business Reality Registry** (canonical business entity identity intent: organizations, people, structural projects, websites, domains, relationships). Phase 1 **foundation complete** under `projects/atlas/foundation/`. |
| **What it is NOT** | Runtime, storage engine, CRM/ERP/finance, PM/tasks, ORCA/MIG operational artifacts, MARS `project_id` registry (`registry/project-registry.md` remains separate), agent orchestration, or automated enforcement. |
| **Operational status** | **REGISTERED** (`planned` registry band) — foundation **complete**; **documentation-layer population** Waves 1–6B + Agreement layers **complete** (human-attested registers under `population/`); persistence engine and APIs **not started**. |
| **Canonical path** | [../projects/atlas/foundation/ATLAS-REALITY-MODEL-v1.md](../projects/atlas/foundation/ATLAS-REALITY-MODEL-v1.md), [ATLAS-BOUNDARIES-v1.md](../projects/atlas/foundation/ATLAS-BOUNDARIES-v1.md); [OPERATIONAL-INDEX.md](../projects/atlas/OPERATIONAL-INDEX.md); registry `atlas`. Evidence: [../logs/atlas/atlas-registration-v1.md](../logs/atlas/atlas-registration-v1.md). |
| **Relationship role** | **Business-reality SoT intent** for ecosystem consumers (read-only contract); **consumes** operator attestation only — **does not** subsume program packs, market groundtruth (MIG), or PPC interpretation (ORCA). **Consumed by** OPS (reporting bindings). |

---

### OPS (Business Operations Domain)

| | |
|--|--|
| **What it is** | **Business Operations Domain** — documentation-first, **human-supervised** operational back-office pack: reporting workflows, document workflows, approvals, deadlines, follow-ups, operational coordination. Foundation through WF-01 pilot and alignment **complete** under `projects/ops/`. |
| **What it is NOT** | Runtime, orchestration, CRM/ERP/accounting, legal authority, business-reality registry, central ecosystem authority, or autonomous operator. |
| **Operational status** | **REGISTERED** (`planned` registry band) — foundation **complete**; WF-01 and WF-02 **live binding pilots PARTIAL** (2026-06-10); implementation engine **not started**. |
| **Canonical path** | [../projects/ops/README.md](../projects/ops/README.md), [OPERATIONAL-INDEX.md](../projects/ops/OPERATIONAL-INDEX.md); registry `ops`. Evidence: [../logs/ops/ops-registration-v1.md](../logs/ops/ops-registration-v1.md). Visual: `programs.canvas` (Awareness Alignment 2026-06). |
| **Relationship role** | **Consumes** [ATLAS](#atlas-business-reality-registry) (business identity, when available). **May later surface through** HomeGateway, NOVA. **May consume operator-attested evidence from** MetaBOT, ORCA, MIG, WPilot, OCPilot — **does not** own those lanes. **Not** authority over ATLAS, MARS core, or external runtimes. |

---

### HomeGateway v4.ai

| | |
|--|--|
| **What it is** | Documentation-first **Personal Operational Cockpit** pack (private web surface layer) with static-first planning posture. |
| **What it is NOT** | MARS runtime/control plane, autonomous system, deployed backend integration layer, or execution owner of MARS/n8n/Telegram systems. |
| **Operational status** | **Planned** program (`planned` registry) + **operational documentation pack** + **UI prototype workspace** (`workspaces/homegateway-v4-ai/v1/`) — **not** deployed product or active control plane. |
| **Canonical path** | [../projects/homegateway-v4-ai/README.md](../projects/homegateway-v4-ai/README.md), [../projects/homegateway-v4-ai/OPERATIONAL-INDEX.md](../projects/homegateway-v4-ai/OPERATIONAL-INDEX.md); registry `homegateway-v4-ai`. |
| **Relationship role** | Ecosystem **surface layer** for operator visibility and quick actions; does not replace ORCA/WPilot/MetaBOT/MARS governance boundaries. |

---

### Continuity / IdeaBox

| | |
|--|--|
| **What it is** | Filesystem-backed **human-operated** **Incubation Layer** (optional) — ideas, discoveries, decisions; lightweight protocols, manual index. |
| **What it is NOT** | Autonomous memory, semantic graph, orchestration, mandatory entry path, or governance auto-mutation. |
| **Operational status** | **Operational** (discipline) — use when idea exists but implementation is deferred; **direct** program/governance creation remains valid. |
| **Canonical path** | [../continuity/README.md](../continuity/README.md); manual index [../continuity/registry/master-index.md](../continuity/registry/master-index.md); **not** a `project_id` row. Evidence: [../logs/cleanup/actions/ideabox-alignment-v1.md](../logs/cleanup/actions/ideabox-alignment-v1.md). |
| **Relationship role** | **Optional** incubation complement to [context-continuity-rules.md](context-continuity-rules.md); distinct from [../incoming/README.md](../incoming/README.md) (untrusted external drops). |

---

### Incoming (ecosystem intake)

| | |
|--|--|
| **What it is** | Root **`incoming/`** quarantine and transport for **untrusted** external material before human promotion — **Hybrid model:** **Active Incoming** stays in Active Brain; **Historical Bulk** retires to Storage Layer after triage (operator-gated). |
| **What it is NOT** | Registry row, runtime pipeline, long-term bulk store, or `archive/` substitute. |
| **Operational status** | **Operational** staging (e.g. `incoming/mig/`); baseline checkpoint **excludes** `incoming/**` by design. |
| **Canonical path** | [../incoming/README.md](../incoming/README.md); program-scoped zones e.g. `projects/ocpilot/incoming/`. |
| **Relationship role** | **Upstream** of program packs in observed information flow — see [../logs/cleanup/discoveries/observed-information-flow-v1.md](../logs/cleanup/discoveries/observed-information-flow-v1.md). Evidence: [../logs/cleanup/actions/incoming-hybrid-alignment-v1.md](../logs/cleanup/actions/incoming-hybrid-alignment-v1.md). |

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
| Lifecycle events? | [../logs/lifecycle-log.md](../logs/lifecycle-log.md) — **Key Event History**; optional **Lifecycle Tracking Mode** for long ops (not mandatory for normal work) |
| Observed information flow? | [../logs/cleanup/discoveries/observed-information-flow-v1.md](../logs/cleanup/discoveries/observed-information-flow-v1.md) — **not** a subsystem |

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
