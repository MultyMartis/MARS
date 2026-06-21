# MARS v2 Structural Coherence Audit v0

**Status:** audit / stabilization report.  
**Date:** 2026-05-19.  
**Scope:** repository-wide structural coherence audit of the live MARS repository.  
**Posture:** documentation-first, governance-centered, human-supervised operational methodology.  
**Non-claim:** this report does not claim a deployed MARS runtime, autonomous orchestration platform, policy engine, registry service, or self-managing AI ecosystem.

---

## 0. Audit Method

This audit reconstructs the live repository topology from actual files and directory state, not from the legacy source pack alone.

### Coverage

Mandatory target coverage:

| Area | Live state observed | Audit note |
|------|---------------------|------------|
| `governance/` | Present, 66 files | Core governance spine and many stabilization layers. |
| `registry/` | Present, 1 file | Project registry only. |
| `agents/` | Present, 79 files | Agent registry, cards, frontend packs, Forge overlay. |
| `projects/` | Present, 911 files | Six project/system packs plus dense Website Factory and ORCA documentation. |
| `mars-runtime/` | Present, 50 files | v0 contracts plus narrow R1 JavaScript experiments and run state JSON. |
| `tools/` | Present, 21 files | Manual helper scripts plus Tool Layer v0 docs. |
| `web-gpt-sources/` | Present, 35 files | Historical/imported source pack plus `mars-v2/` and chat migration snapshots. |
| `continuity/` | Present, 10 files | IdeaBox / human-operated continuity workflow. |
| `logs/` | Present, 1 file | Lifecycle log only; no `decision-log.md`. |
| `onboarding/` | Absent | Governance has onboarding-survivability docs, but no top-level onboarding folder. |
| `control-plane/` | Present, 3 files | Planned contract docs only. |
| `workflows/` | Present, 5 files | Planned workflow/task contracts only. |
| `memory/` | Present, 7 files | Documentation-only memory/RAG contracts. |
| `interfaces/` | Present, 7 files | Documentation-only introspection/self-* contracts. |
| `observability/` | Present, 5 files | Documentation-only observability contracts. |
| `evaluation/` | Present, 4 files | Documentation-only evaluation contracts. |
| `security/` | Present, 5 files | Documentation-only security/guardrail contracts. |
| `shared/` | Present, large vendor-sensitive tree | Local shared assets; not governance or runtime. |

Additional ecosystem areas observed:

| Area | Live state observed | Classification |
|------|---------------------|----------------|
| `models/` | Present, 6 files | Documentation-only Model Layer v0. |
| `storage/` | Present, 6 files | Documentation-only Storage Layer v0. |
| `integrations/` | Present, 7 files | Documentation-only Integration Layer v0. |
| `workspaces/` | Present, 4 workspace directories | Execution locus for local project work; not canonical MARS governance SoT. |

Representative files directly analyzed include:

- Root and rules: `README.md`, `AGENTS.md`.
- Governance: `governance/README.md`, `current-operational-state-v1.md`, `master-build-map.md`, `registry-source-of-truth.md`, `system-entity-model.md`, `system-boundaries.md`, `canonical-terminology-registry.md`, `frontend-legacy-and-foundation-map-v0.md`, `mars-forge-operational-design-v0.md`.
- Registries and logs: `registry/project-registry.md`, `logs/lifecycle-log.md`, `continuity/registry/master-index.md`.
- Agent layer: `agents/README.md`, `agents/registry.md`, `agents/frontend-gulp-agent/README.md`, `agents/mars-forge/README.md`, `agents/mars-forge/AGENT.md`.
- Runtime/tooling/core layers: `mars-runtime/README.md`, `mars-runtime/architecture-map.md`, `tools/README.md`, `control-plane/README.md`, `workflows/README.md`, `interfaces/README.md`, `memory/README.md`, `models/README.md`, `storage/README.md`, `observability/README.md`, `evaluation/README.md`, `security/README.md`, `integrations/README.md`, `shared/README.md`.
- Projects: `projects/mars-website-factory/README.md`, `OPERATIONAL-INDEX.md`, `agent-map.md`, `roadmap.md`, `system-integration-check-v1.md`; `projects/orca/README.md`, `OPERATIONAL-INDEX.md`; `projects/wpilot/README.md`; `projects/metabot-seo-content-agent/README.md`; `projects/seo-content-agent/README.md`.

---

## 1. Current Ecosystem Topology

The live repository is not a single runtime product. It is a documentation-first ecosystem with several different kinds of artifacts sharing one tree:

```text
MARS repository
├─ governance spine
│  ├─ core truth / boundary / stage maps
│  ├─ S1-S7 stabilization and reality-audit layers
│  ├─ frontend consolidation and Forge design history
│  └─ terminology / source-of-truth rules
├─ registries and logs
│  ├─ project registry
│  ├─ agent registry
│  ├─ tool registry
│  ├─ continuity manual index
│  └─ lifecycle log
├─ MARS core contract folders
│  ├─ control-plane, workflows, interfaces, security
│  ├─ tools, models, storage, memory
│  ├─ observability, evaluation, integrations
│  └─ mars-runtime contracts + R1 experiments
├─ operational system / project packs
│  ├─ mars-website-factory
│  ├─ ORCA
│  ├─ WPilot
│  ├─ MetaBOT SEO Content Agent
│  ├─ legacy SEO Content Agent
│  └─ Triumph Manipulator Landing
├─ agent / overlay packs
│  ├─ Gulp Frontend Agent
│  ├─ MARS Forge
│  ├─ Website Factory planned agent cards
│  └─ design governance agent material
├─ continuity / IdeaBox
│  └─ human-operated idea and discovery capture
├─ historical imports
│  └─ web-gpt-sources, chat migration, mars-v2 source-pack distillates
├─ execution loci and local assets
│  ├─ workspaces/*
│  └─ shared/*
└─ images / diagrams / local artifacts
```

### Canonical vs non-canonical layers

| Layer | Canonical for | Non-canonical / lower authority |
|-------|---------------|----------------------------------|
| `AGENTS.md` | Workspace honesty, status boundaries, closeout discipline | Any document implying runtime beyond evidence. |
| `governance/current-operational-state-v1.md` | Current visibility snapshot, with re-verification warning | Not live telemetry; does not override `AGENTS.md`. |
| `governance/master-build-map.md` | Roadmap / build order / stage status | Not implementation certificate. |
| `registry/project-registry.md` | Project identity rows | Project folders without rows are registry-level SAFE UNKNOWN. |
| `agents/registry.md` | Agent role ids and status vocabulary | Agent pack prose when registry status conflicts. |
| `tools/registry.md` | Tool Layer row semantics | R1 `tool-registry.js`, helper script filenames. |
| `projects/*/README.md` and `OPERATIONAL-INDEX.md` | Pack-local navigation and posture | Not higher than central registry for identity/status. |
| `web-gpt-sources/` | Historical/imported design input and bootstrap context | Not live repository layout or implementation truth. |
| `workspaces/*` | Local execution work, if opened by operator | Not governance SoT; not proof of MARS runtime. |

---

## 2. Major Operational Domains

### 2.1 Governance Core

**Classification:** operational as human-maintained documentation discipline; conceptual as contracts; not runtime enforcement.

Major files:

- `governance/README.md`
- `governance/master-build-map.md`
- `governance/current-operational-state-v1.md`
- `governance/canonical-terminology-registry.md`
- `governance/registry-source-of-truth.md`
- `governance/system-entity-model.md`
- S1-S7 operational survivability, tooling, operationalization, experiment, and reality-audit docs.

This is the strongest canonical spine in the repo, but it has also become dense enough to create governance discoverability and maintenance risks.

### 2.2 Registries / Identity / Logs

**Classification:** operational as human-maintained catalogs; not registry services.

Major files:

- `registry/project-registry.md`
- `agents/registry.md`
- `tools/registry.md`
- `continuity/registry/master-index.md`
- `logs/lifecycle-log.md`

The repo has strong registry honesty rules, but actual project/system creation has outpaced registry and lifecycle updates in several places.

### 2.3 MARS Core Contract Layers

**Classification:** mostly conceptual / future; documentation-only contracts.

Folders:

- `control-plane/`
- `workflows/`
- `interfaces/`
- `security/`
- `tools/`
- `models/`
- `storage/`
- `memory/`
- `observability/`
- `evaluation/`
- `integrations/`

These folders are topologically coherent as layer placeholders and contract packs. Their main risk is terminology pressure: “control plane”, “runtime”, “validation runtime”, “orchestrator”, “bus”, and “self-heal” sound executable even though the docs repeatedly deny that.

### 2.4 Experimental Runtime Boundary

**Classification:** conceptual contracts plus experimental R1 code; not production runtime.

`mars-runtime/` contains:

- Stage 8.5 / Stage 13 / Stage 14 runtime-facing Markdown contracts.
- Narrow JavaScript experiments under `adapters/`, `runtime/`, and `state/`.
- Run state JSON snapshots.

The folder is structurally useful, but it is the highest mythology-pressure folder because its name and JS files invite overclaiming.

### 2.5 Website Factory

**Classification:** strategic documentation-first operational methodology; planned/future runtime-assisted execution; not automation.

`projects/mars-website-factory/` is the largest and densest system pack. It contains:

- Workflow, runbook, artifact, semantic, validation, and delivery models.
- A large family of frontend/design/governance drift taxonomies.
- Agent map and stable planned Website Factory agent ids.
- OPERATIONAL-INDEX to reduce navigation burden.
- Reference cases and production-pack links.

This domain is the biggest source of documentation growth and conceptual layering risk.

### 2.6 Frontend Execution Methodology

**Classification:** operational doc packs and overlays; human/Cursor execution only.

Major entities:

- `agents/frontend-gulp-agent/`
- `agents/mars-forge/`
- `projects/mars-website-factory/frontend-*`
- `projects/triumph-manipulator-landing/`
- `workspaces/triumph-manipulator-landing*`
- `shared/assets/icon-libraries/`

The frontend area has clear foundation rules, but also the clearest live drift between older governance maps and newer Forge material.

### 2.7 ORCA

**Classification:** operational human-supervised PPC toolkit; runtime excluded.

`projects/orca/` has strong anti-bloat posture and fast-path discipline. It is structurally healthier than Website Factory in terms of operational entry points, but it is also expanding into many PPC knowledge sublayers.

### 2.8 WPilot

**Classification:** documented operational system / external systems lane; future plugin bridge planned; not runtime.

`projects/wpilot/` is a significant Program / Operational System with Phase 1 operational docs and plugin MVP planning. It is not registered in `registry/project-registry.md`, which is a direct source-of-truth gap.

### 2.9 MetaBOT / SEO Content Agent

**Classification:** external operational system documented in repo; n8n owns execution; legacy folder deprecated/historical.

Current topology is clear:

- Canonical: `projects/metabot-seo-content-agent/`.
- Legacy: `projects/seo-content-agent/`.
- Experimental bridge hints: `mars-runtime/adapters/seo-content-agent-adapter.js`, `mars-runtime/runtime/run-seo-content-agent-test.js`.

The strongest risk here is confusing external n8n execution truth with MARS in-repo runtime evidence.

### 2.10 Continuity / IdeaBox

**Classification:** operational human discipline; not memory system.

`continuity/` is well bounded. The master index is explicitly manual and non-authoritative for completeness. Its risk is future pressure to become hidden memory or ontology.

---

## 3. Major Systems / Entities

### 3.1 Current systems and entities by classification

| Entity | Location | Classification | Current coherence |
|--------|----------|----------------|-------------------|
| MARS governance core | `governance/` | Operational documentation discipline + conceptual contracts | Strong spine, high density. |
| Project registry | `registry/project-registry.md` | Operational catalog | Authoritative but incomplete against live `projects/`. |
| Lifecycle log | `logs/lifecycle-log.md` | Operational event log | Canonical but stale relative to recent new packs/docs. |
| MARS Website Factory | `projects/mars-website-factory/` | Strategic planned / documentation-first operational methodology | Rich but over-layered. |
| Gulp Frontend Agent | `agents/frontend-gulp-agent/` | Operational doc pack | Coherent foundation. |
| MARS Forge | `agents/mars-forge/` | Operational overlay doc pack | Live pack exists; older governance design docs are stale. |
| ORCA | `projects/orca/` | Operational human-supervised PPC toolkit | Clear boundaries; large but anti-bloat aware. |
| WPilot | `projects/wpilot/` | Program / Operational System, external systems lane | Clear local docs; missing project registry row. |
| MetaBOT SEO Content Agent | `projects/metabot-seo-content-agent/` | External multi-workflow AI system | Canonical pack clear; live n8n remains external truth. |
| SEO Content Agent legacy | `projects/seo-content-agent/` | Historical / legacy | Correctly marked do-not-extend. |
| Triumph Manipulator Landing | `projects/triumph-manipulator-landing/`, `workspaces/*` | Project docs + local execution workspaces | Multiple versions create topology/authority risk. |
| R1 runtime experiments | `mars-runtime/**/*.js` | Experimental | Useful but mythology-prone. |
| Control Plane | `control-plane/` | Conceptual / future | Coherent docs, no implementation. |
| Tool helpers | `tools/*` scripts | Operational/expt manual helpers | Well bounded as local hints. |
| Shared Font Awesome assets | `shared/` | Local / licensing-sensitive asset support | Not governance; high vendor bulk risk. |
| IdeaBox | `continuity/` | Operational human continuity discipline | Well bounded, manual SoT. |

### 3.2 Orphan or under-registered entities

| Entity / concept | Evidence | Gap |
|------------------|----------|-----|
| WPilot | `projects/wpilot/README.md` classifies it as Program / Operational System | Missing row in `registry/project-registry.md`. |
| MARS Forge pack | `agents/mars-forge/README.md`, `agents/registry.md` §4.1 | Some governance docs still say pack/card do not exist yet. |
| Onboarding | Governance has `onboarding-survivability.md`; mandatory target folder is absent | Top-level onboarding domain exists conceptually only. |
| Triumph workspace variants | `workspaces/triumph-manipulator-landing`, `-v2`, `-v3`, `-v4` | Registry has one project id; version/workspace authority map is not central. |
| Raw/local operational folders | WPilot docs mention `C:\AI MARS\backups\` and `C:\AI MARS\local\` as local-only | Not repo canonical, but could be mistaken as hidden system if present locally. |
| Image artifacts | `MARS MAP.png`, `mermaid-diagram.png` in git status | Relationship to canonical topology docs is unclear. |

---

## 4. Relationship Graph Analysis

### 4.1 Actual relationship graph

```text
AGENTS.md
  -> constrains all claims and reports

governance/master-build-map.md
  -> orders MARS core contract layers
  -> references dependency-map/risk-register/lifecycle-log
  -> does not prove implementation

registry/project-registry.md
  -> canonical project identity
  -> should point to projects/*

agents/registry.md
  -> canonical agent role ids
  -> points to agents/cards/*
  -> delegates Website Factory role prose to projects/mars-website-factory/agent-map.md

projects/mars-website-factory/
  -> consumes core governance/workflow/security terminology
  -> owns Website Factory methodology
  -> depends on agents/registry for agent ids
  -> depends on frontend-gulp-agent and MARS Forge for frontend operational discipline
  -> points to WPilot as planned future WordPress bridge

agents/frontend-gulp-agent/
  -> canonical frontend foundation
  -> consumed by MARS Forge
  -> execution happens in workspaces/external gulp-starter, not in agents/

agents/mars-forge/
  -> overlay over gulp_frontend_agent
  -> consumes many Website Factory governance/taxonomy docs
  -> creates checklist mirror of many Website Factory layers

projects/orca/
  -> registered as active operational toolkit
  -> mostly self-contained human-supervised PPC methodology

projects/wpilot/
  -> relates to Website Factory future WordPress bridge
  -> uses external WordPress/Beget
  -> not present in project registry

projects/metabot-seo-content-agent/
  -> external n8n runtime truth
  -> canonical replacement for projects/seo-content-agent/
  -> narrow R1 bridge experiments exist under mars-runtime/

continuity/
  -> operational markdown continuity discipline
  -> referenced by governance as optional human-operated support
```

### 4.2 Relationship visibility gaps

| Gap | Why it matters |
|-----|----------------|
| No single system topology index across `governance`, `registry`, `agents`, `projects`, `mars-runtime`, `tools`, and `continuity`. | Operators must infer topology from several overlapping maps. |
| Project registry does not fully mirror live project/system folders. | New systems can become operational in docs before identity governance catches up. |
| Lifecycle log has not recorded several visible new entities / expansions. | Event SoT becomes less useful for reconstructing chronology. |
| Website Factory, Forge, Gulp, Triumph, shared assets, and workspaces form a real frontend ecosystem but are split across several maps. | High chance of stale SoT and duplicated frontend rules. |
| External execution truth is distributed across pack docs. | MetaBOT, WPilot, n8n, WordPress, Beget, Google Sheets, Telegram, and workspaces need clearer relationship visibility without claiming ownership. |

---

## 5. Source-of-Truth Conflicts

### 5.1 Direct conflicts

| Conflict | Evidence | Risk |
|----------|----------|------|
| WPilot exists as a Program / Operational System but is absent from project registry. | `projects/wpilot/README.md` vs `registry/project-registry.md`. | Registry SoT under-represents actual ecosystem. |
| Forge governance design says pack/card do not exist, but live pack and card exist. | `governance/frontend-legacy-and-foundation-map-v0.md` and `governance/mars-forge-operational-design-v0.md` vs `agents/mars-forge/README.md`, `agents/registry.md`, `agents/cards/mars-forge-frontend-agent-v0.md`. | Operators may follow stale “reserved future role” guidance. |
| Root README project overview lags newer system packs. | Root README emphasizes Website Factory / MetaBOT / legacy SEO; ORCA and WPilot are not equally visible. | Repository entry point under-explains live ecosystem. |
| Lifecycle log ends at truth repair / earlier milestones while visible repo has newer ORCA/WPilot/Forge/Factory expansions. | `logs/lifecycle-log.md` last row `evt-2026-0015` vs many files dated/updated after that in project packs and git status. | Chronology reconstruction becomes unreliable. |
| `current-operational-state-v1.md` is a canonical snapshot but explicitly not live telemetry. | It supersedes migration snapshot but requires re-verification. | Readers may treat it as live unless disciplined. |

### 5.2 Soft conflicts / ambiguous precedence

| Area | Ambiguity |
|------|-----------|
| Website Factory entry points | `README.md`, `OPERATIONAL-INDEX.md`, `roadmap.md`, `workflow-map.md`, `system-integration-check-v1.md`, and many layer overviews each act like local maps. |
| Frontend SoT | Factory frontend contracts, Gulp pack, Forge pack, foundation map, operational design, and Triumph project docs all describe frontend discipline at different abstraction levels. |
| Roadmap semantics | MARS core stages, Website Factory roadmap phases, ORCA phases, WPilot MVP phases, and plugin roadmap phases use similar words for different scopes. |
| Validation/runtime language | “Validation Runtime Model” is intentionally documentation-only, but “runtime” still creates pressure against `mars-runtime/` and real validation engines. |

---

## 6. Duplicated Structures

### 6.1 Topology / map duplication

| Structure | Duplicate / overlap | Assessment |
|-----------|---------------------|------------|
| Repository topology | Root `README.md`, `mars-runtime/architecture-map.md`, `governance/master-build-map.md`, `governance/current-operational-state-v1.md` | Mostly intentional, but no compact current ecosystem map exists. |
| Governance index | `governance/README.md`, master build map, current operational state, terminology registry | Useful but dense; creates entry-point fatigue. |
| Website Factory map | `README.md`, `OPERATIONAL-INDEX.md`, `layer-map.md`, `workflow-map.md`, `roadmap.md`, `system-integration-check-v1.md` | The OPERATIONAL-INDEX helps, but the pack still has many map-like files. |
| Frontend topology | `frontend-ecosystem-audit-v0.md`, `frontend-legacy-and-foundation-map-v0.md`, Forge docs, Factory frontend docs | Real duplication plus stale transition state. |
| Runtime boundary | `README.md`, `current-operational-state-v1.md`, `mars-runtime/README.md`, `architecture-map.md`, terminology registry | Necessary repetition, but every repeated boundary can drift. |

### 6.2 Pattern duplication

| Pattern | Examples | Risk |
|---------|----------|------|
| Governance triads | `*-governance.md`, `*-model.md`, `*-taxonomy.md` in Website Factory | Methodology expansion can outpace operator usefulness. |
| Checklist mirrors | Forge checklists mirror Website Factory governance layers | Maintenance cost and checklist fatigue. |
| Anti-mythology disclaimers | Repeated “not runtime / not automation / not autonomous” blocks | Good safety, but repetition can hide the few places where real evidence changes. |
| Project operational indexes | ORCA and Website Factory have OPERATIONAL-INDEX patterns | Good if intentionally reused, but no shared minimal standard exists. |
| Roadmap files | MARS master build map, Website Factory roadmap, WPilot roadmap, MetaBOT roadmap, ORCA state docs | Roadmap fragmentation and phase vocabulary collision. |

---

## 7. Unstable Conceptual Layers

### 7.1 High-risk vocabulary

| Term / layer | Current status | Instability |
|--------------|----------------|-------------|
| Runtime | Conceptual full runtime; R1 experimental only | Folder name and JS files create implementation-pressure. |
| Control Plane | Conceptual/future | Reads like a service but is only docs. |
| Orchestrator / orchestration | Conceptual / external / human coordination | Repeated in workflow semantics and Factory docs. |
| Validation Runtime | Conceptual validation semantics | Name contains “runtime” despite non-runtime boundary. |
| Artifact Bus | Conceptual handoff semantics | “Bus” implies queue/pub-sub unless repeatedly denied. |
| Self-Heal | Plan-only recovery semantics | Sounds automated; requires continuous boundary reminders. |
| Agent | Documentation role / human-operated pack / future runtime agent | Registry rows and cards can be mistaken for running agents. |
| Operational | Human-used discipline | Can be misread as automated production operation. |

### 7.2 Layer inflation signals

Website Factory now contains many specialized methodology layers: design intent, design tokens, implementation reliability, content density, source interpretation, reconstruction fidelity, layout shell, commercial pressure, rhythm, provenance, interaction, state consistency, accessibility, QA confidence, human escalation, multi-agent coordination, strategic intent, temporal evolution, workflow discipline, terminal survivability, production readiness, context survivability, failure recovery, transfer, organizational memory, governance minimalism, prioritization, adaptive governance, governance economics, cognitive load, compression, evolution, meta-governance, trust calibration, decision transparency, and more.

This depth is not wrong by itself. The instability is that many layers share the same shape and may become indistinguishable to operators unless they are grouped into modes or priority tiers.

---

## 8. Operational Overlaps

| Overlap | Current state | Risk |
|---------|---------------|------|
| Governance vs Website Factory governance | Global governance defines survivability, experiments, reality audit; Website Factory defines many local governance layers | Local governance may become parallel governance architecture. |
| Gulp Frontend Agent vs MARS Forge | Forge is explicitly overlay, but older docs still treat it as future/reserved | Transition ambiguity. |
| Frontend QA vs Design QA vs Forge overlay QA vs Validator | Each has a role, but boundaries overlap on visual, responsive, accessibility, and confidence checks | Reviewer/executor collapse or redundant QA. |
| Website Factory vs WPilot | Factory-native WordPress bridge is future direction; WPilot has plugin MVP planning | Future integration can be mistaken as existing bridge. |
| MetaBOT vs MARS runtime | External n8n owns execution; R1 adapter experiments exist | Bridge/adapters may be mistaken as MARS execution ownership. |
| ORCA review frameworks vs reality-audit/governance layers | ORCA has local anti-bloat/reality review; MARS has global reality audit | Good local adaptation, but potential duplicated review concepts. |
| Continuity / IdeaBox vs memory layer | IdeaBox is operational markdown continuity; memory layer is conceptual future | Hidden memory mythology pressure. |

---

## 9. Roadmap Fragmentation

### 9.1 Roadmap sources

| Source | Scope |
|--------|-------|
| `governance/master-build-map.md` | MARS core build order, documentation vs implementation status. |
| `web-gpt-sources/14_roadmap.md` | Historical imported roadmap. |
| `projects/mars-website-factory/roadmap.md` | Website Factory maturity phases. |
| `projects/wpilot/metacode-wpilot-plugin-mvp-roadmap.md` | WPilot plugin MVP sequence. |
| `projects/metabot-seo-content-agent/roadmap.md` | External MetaBOT stabilization/future work. |
| ORCA `current-state-v1.md`, starter/reality docs | Operational PPC toolkit evolution and pruning. |
| Lifecycle log | Event history, not roadmap authority. |

### 9.2 Fragmentation findings

1. MARS core stage numbers and project-local phase numbers are unrelated but use similar language.
2. Roadmap state and lifecycle state are not consistently synchronized.
3. Project-level operational evolution is visible in project folders before central registry/log updates.
4. Historical `web-gpt-sources` roadmap remains available and searchable, increasing the chance of stale roadmap resurrection.
5. “Planned”, “future”, “strategic”, “documentation-only”, “operational_doc_pack”, “active”, and “planned-docs” are all used, sometimes with subtle differences.

---

## 10. Ecosystem Entropy Risks

### 10.1 Highest entropy risks

| Rank | Risk | Why it is high |
|------|------|----------------|
| 1 | Registry drift | Live systems/packs can exist without central registry alignment (`WPilot`), while some registered entities remain doc-only. |
| 2 | Stale transition docs | Forge is now a live pack, but older governance still says it is not created. |
| 3 | Governance layer proliferation | Website Factory layer/checklist growth can exceed operator working memory. |
| 4 | Roadmap fragmentation | Multiple phase systems and roadmap files create ambiguous “what is next”. |
| 5 | Runtime mythology pressure | `mars-runtime/`, “Control Plane”, “Validation Runtime”, “Artifact Bus”, and R1 JS all require careful qualification. |
| 6 | Relationship invisibility | Cross-system relations are scattered and require deep reading to reconstruct. |
| 7 | Lifecycle log staleness | Event log no longer fully narrates visible ecosystem changes. |
| 8 | Workspace / governance confusion | `workspaces/*` hold real execution artifacts but are not canonical MARS docs. |
| 9 | Vendor/shared asset ambiguity | `shared/` is intentionally local but large and licensing-sensitive. |
| 10 | Historical source-pack resurrection | `web-gpt-sources` still contains broad architecture narratives that may conflict with current governance. |

### 10.2 Mythology pressure points

- “Multi-Agent Runtime System” name vs documentation-first reality.
- “runtime” folder with JS experiments.
- “Control Plane” contracts without implementation.
- “Agent Registry” rows and cards without agents-as-processes.
- “Validation Runtime Model” without validator runtime.
- “Artifact Bus” without bus infrastructure.
- External systems that really run elsewhere, especially n8n / MetaBOT, which can leak execution confidence into MARS core claims.

---

## 11. Structural Weak Points

### 11.1 Weak relationship visibility

The repository has many local maps but no compact current ecosystem topology map. The closest files are:

- `README.md`
- `governance/current-operational-state-v1.md`
- `governance/master-build-map.md`
- `mars-runtime/architecture-map.md`
- `projects/mars-website-factory/OPERATIONAL-INDEX.md`

Each is useful, but none is a live “system/entity relationship index” across all current systems.

### 11.2 Weak registry completeness

`registry/project-registry.md` is explicitly authoritative, but it does not include all live project/system packs. This creates a high-priority coherence issue because the repo now has a `system-entity-model.md` that says folders in `projects/` may represent Program / Operational System entities.

### 11.3 Weak lifecycle traceability

`logs/lifecycle-log.md` is append-only and authoritative for lifecycle events, but it has not kept pace with recent entity growth. The absence of `logs/decision-log.md` is already acknowledged in `master-build-map.md`.

### 11.4 Weak deprecation visibility

The legacy `seo-content-agent` folder is clearly marked. Other historical or superseded docs are less mechanically visible:

- `web-gpt-sources/` remains broad and searchable.
- Older Forge design docs now conflict with live Forge pack state.
- Multiple Triumph workspace versions exist without one central version authority map at the repo root.

### 11.5 Weak operational compression

Website Factory has many detailed layers, but the practical operating modes are not yet compressed enough. ORCA has a strong FAST PATH model; Website Factory and Forge would benefit from a similar “default / expanded / critical” reading and execution mode.

---

## 12. Stabilization Recommendations

These are practical stabilization directions, not a redesign mandate.

### Priority 1 — Repair registry completeness

Add or update registry rows only after human approval:

- Add `wpilot` to `registry/project-registry.md` as Program / Operational System, external systems lane, human-supervised, not runtime.
- Reconfirm whether all project folders under `projects/` should have rows, including `triumph-manipulator-landing`.
- Decide whether workspace variants need registry rows, a project-local version map, or explicit exclusion.

### Priority 2 — Resolve Forge transition drift

Without restructuring:

- Mark `governance/frontend-legacy-and-foundation-map-v0.md` §5 and `governance/mars-forge-operational-design-v0.md` as historical/design-precedent where they claim the Forge pack does not exist.
- Keep `agents/mars-forge/README.md`, `agents/registry.md`, and the card as current SoT for Forge identity.
- Add a small “Forge transition note” rather than rewriting the whole frontend governance area.

### Priority 3 — Create a compact ecosystem topology index

Create one small map, not an ontology:

- Candidate path: `governance/current-ecosystem-topology-v1.md`.
- Include only systems, classification, canonical SoT, relationship, and status.
- Keep it under 150-200 lines.
- Link to detailed maps rather than duplicating them.

### Priority 4 — Add lifecycle catch-up entries

Append lifecycle entries for major documented ecosystem changes that now exist in-tree:

- ORCA registration / operational toolkit posture if not already logged elsewhere.
- WPilot documentation pack / external systems lane.
- MARS Forge pack creation / status transition from reserved design to operational_doc_pack.
- Recent Website Factory governance/checklist expansions if treated as milestones.

Do not rewrite older lifecycle rows.

### Priority 5 — Compress Website Factory operating modes

Avoid deleting detail. Add an operator-facing compression layer:

- **Default mode:** minimal required docs for a normal frontend/project session.
- **Expanded mode:** use when source ambiguity, design drift, QA uncertainty, or cross-agent handoff appears.
- **Critical mode:** use for production-readiness, failure recovery, source conflict, or major structural change.

This would preserve deep governance while reducing default cognitive load.

### Priority 6 — Normalize roadmap vocabulary

Add a short cross-roadmap glossary:

- MARS core stage
- Project phase
- Operational mode
- Documentation milestone
- Implementation evidence
- External system status

This can live in governance or as a section in the topology index. Do not create a heavy ontology.

### Priority 7 — Strengthen external-system relationship visibility

Add one relationship table for:

- MetaBOT ↔ n8n ↔ Google Sheets ↔ Telegram ↔ MARS docs ↔ R1 bridge experiment.
- WPilot ↔ WordPress ↔ Beget ↔ Website Factory planned bridge.
- Workspaces ↔ Website Factory / Gulp / Forge docs.

The table should clarify ownership, execution truth, secrets boundary, and MARS claim boundary.

### Priority 8 — Keep helper tools bounded

`tools/` is currently well bounded. Preserve:

- Manual invocation.
- Hints only.
- No CI/enforcement claim unless separately decided.
- No hidden sync or registry mutation.

---

## 13. SAFE UNKNOWN Areas

| Area | SAFE UNKNOWN |
|------|--------------|
| External systems | Live n8n workflows, Telegram bot state, Google Sheets schemas, WordPress/Beget state, credentials, deployment status. |
| Runtime parity | Whether R1 adapter code matches live MetaBOT endpoints or any current external workflow payload. |
| Workspaces | Which `workspaces/triumph-*` version is current execution truth without operator confirmation. |
| Lifecycle completeness | Whether unlogged docs are intentionally unlogged because they are still uncommitted/in-progress. |
| Registry intent | Whether WPilot should be added immediately or held until a governance decision. |
| Shared assets | Exact licensing/redistribution permissions for local Font Awesome Pro tree. |
| Onboarding | Whether top-level `onboarding/` is intentionally absent or planned. |
| Image artifacts | Whether `MARS MAP.png` and `mermaid-diagram.png` are canonical diagrams, generated artifacts, or local notes. |

---

## 14. Stabilization Direction Summary

The MARS repository is structurally honest but increasingly dense. Its strongest property is repeated anti-mythology discipline. Its weakest property is relationship visibility after rapid documentation growth.

The practical stabilization path is:

1. Registry catch-up.
2. Forge transition note.
3. Compact ecosystem topology index.
4. Lifecycle catch-up entries.
5. Website Factory operating-mode compression.
6. Cross-roadmap vocabulary normalization.
7. External-system relationship table.

Do not solve this by creating a heavyweight ontology, runtime architecture, registry engine, or new governance bureaucracy. The repo needs fewer current-state entry points, clearer authority boundaries, and lightweight relationship visibility.

---

## 15. Report Closeout Data

### Files created by this audit

- `governance/mars-v2-structural-coherence-audit-v0.md`

### Files analyzed

Directly read / sampled:

- `README.md`
- `governance/README.md`
- `governance/current-operational-state-v1.md`
- `governance/master-build-map.md`
- `governance/registry-source-of-truth.md`
- `governance/system-entity-model.md`
- `governance/system-boundaries.md`
- `governance/canonical-terminology-registry.md`
- `governance/frontend-legacy-and-foundation-map-v0.md`
- `governance/mars-forge-operational-design-v0.md`
- `registry/project-registry.md`
- `continuity/registry/master-index.md`
- `logs/lifecycle-log.md`
- `agents/README.md`
- `agents/registry.md`
- `agents/frontend-gulp-agent/README.md`
- `agents/mars-forge/README.md`
- `agents/mars-forge/AGENT.md`
- `mars-runtime/README.md`
- `mars-runtime/architecture-map.md`
- `tools/README.md`
- `control-plane/README.md`
- `workflows/README.md`
- `interfaces/README.md`
- `security/README.md`
- `memory/README.md`
- `models/README.md`
- `storage/README.md`
- `observability/README.md`
- `evaluation/README.md`
- `integrations/README.md`
- `shared/README.md`
- `projects/mars-website-factory/README.md`
- `projects/mars-website-factory/OPERATIONAL-INDEX.md`
- `projects/mars-website-factory/agent-map.md`
- `projects/mars-website-factory/roadmap.md`
- `projects/mars-website-factory/system-integration-check-v1.md`
- `projects/orca/README.md`
- `projects/orca/OPERATIONAL-INDEX.md`
- `projects/wpilot/README.md`
- `projects/metabot-seo-content-agent/README.md`
- `projects/seo-content-agent/README.md`
- `continuity/README.md`

Directory/file inventory was also checked across all mandatory audit targets and additional top-level layer folders.

### Major findings

- The repository has a coherent documentation-first governance spine, but no single compact current ecosystem topology map.
- `registry/project-registry.md` is authoritative but incomplete against live `projects/` folders, especially `projects/wpilot/`.
- MARS Forge has moved from reserved design to live operational overlay pack, while older governance docs still contain stale “not created” language.
- Website Factory is the largest entropy source due to many governance/model/taxonomy/checklist layers.
- Runtime mythology pressure is controlled by many disclaimers, but remains structurally high because of folder names and contract vocabulary.
- Lifecycle logging has not visibly kept pace with recent ecosystem growth.

### Highest entropy risks

1. Registry drift.
2. Stale transition docs.
3. Website Factory governance/checklist proliferation.
4. Fragmented roadmap semantics.
5. Runtime / orchestration mythology pressure.
6. Weak cross-system relationship visibility.

### Stabilization priorities

1. Registry catch-up for WPilot and any other live system packs.
2. Minimal Forge transition note in governance maps.
3. Compact current ecosystem topology index.
4. Lifecycle catch-up entries.
5. Website Factory operating-mode compression.
6. External-system relationship table.

### Git status summary

At audit start, the working tree was already dirty with many modified and untracked documentation files, images, agent packs, governance docs, runtime files, and project docs. This audit created one additional report document and did not stage, commit, push, delete, move, or restructure files.

---

*End of audit report.*

---

## RC5 RESOLUTION NOTE (2026-06-19)

**What changed:** WPilot RC5 finalization (`v0.3.0-RC5`) established proven plugin REST runtime on DEV (`proven_content_writes` + `proven_connection_runtime`), registered authority `WPILOT-RC5-PROVEN-CONNECTION-RUNTIME-2026-06-19`, and shifted WPilot lifecycle to **Reference Implementation**. WPilot is registered in `registry/project-registry.md` (`wpilot`, updated 2026-06-19). In-repo plugin source exists at `projects/wpilot/plugin/metacode-wpilot/`. Sprint 3 is **HOLD**; active MVP development stream is closed.

**Supersedes (for current-state readers only — historical audit findings above remain valid for 2026-05-19):**

| Stale finding in this audit (2026-05-19) | Current SoT |
|------------------------------------------|-------------|
| §2.8 — WPilot "not runtime"; Phase 1 docs + plugin MVP planning only | [WPILOT-FINAL-STATE-RC5.md](../projects/wpilot/WPILOT-FINAL-STATE-RC5.md), [WPILOT-AUTHORITY-STATE-RC5.md](../projects/wpilot/WPILOT-AUTHORITY-STATE-RC5.md) |
| §2.8, §3.1, §3.2, §5.1 — WPilot missing from `registry/project-registry.md` | [registry/project-registry.md](../registry/project-registry.md) — `wpilot` row (2026-06-19) |
| §4.1, §8 — WPilot as "planned future WordPress bridge" / plugin MVP planning | [WPILOT-LIFECYCLE-STATE.md](../projects/wpilot/WPILOT-LIFECYCLE-STATE.md) — Reference Implementation; [cms-ecommerce-pilots-family.md](../projects/ocpilot/cms-ecommerce-pilots-family.md) |
| §12 Priority 1 — "Add wpilot to registry … not runtime" | Registry row now reflects reference implementation with proven DEV runtime; still **not** MARS core runtime |
| §13 SAFE UNKNOWN — "Whether WPilot should be added immediately" | Resolved — registered 2026-06-19 |

**Canonical discovery:** [projects/shared/reference-implementations/REFERENCE-IMPLEMENTATIONS-INDEX.md](../projects/shared/reference-implementations/REFERENCE-IMPLEMENTATIONS-INDEX.md)

*Historical findings in sections 0–15 remain valid for their audit date (2026-05-19).*
