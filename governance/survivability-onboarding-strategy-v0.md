# MARS — Onboarding survivability strategy (Phase 3)

**Status:** **documented** — lightweight strategy only. **Not** an LMS, **not** training curriculum, **not** automated onboarding.  
**Date:** 2026-05-19.  
**Builds on:** [onboarding-survivability.md](onboarding-survivability.md), [operator-load-management.md](operator-load-management.md).

**Goal:** Shortest viable orientation paths; less “where do I start?” pressure; fewer repeated explanations — **without** a giant onboarding system.

---

## 1. Audit summary (entry surfaces)

| Surface | Role today | Onboarding friction | Survivability note |
|---------|------------|---------------------|-------------------|
| [README.md](../README.md) | Repo identity, layout table, phase posture | Layout table lists **many** contract folders — architecture shock | **Mandatory stop 1** — read § What this repository contains + Current phase only on first day |
| [AGENTS.md](../AGENTS.md) | Honesty, three-way split, SAFE UNKNOWN | Dense but essential | **Mandatory stop 2** — do not re-derive in prompts |
| [onboarding-survivability.md](onboarding-survivability.md) | Minimum 4-file global path (incl. canonical entry model) | Correct but easy to skip | **Mandatory stop 3–4** for MARS-core tasks |
| [governance/README.md](README.md) | Full governance addenda table (~70+ rows) | Feels like required reading | **Optional** — **one row** when task needs governance lookup, not day-one full scan |
| [ecosystem-topology-index.md](ecosystem-topology-index.md) | Ecosystem map after AGENTS | Second “start” after AGENTS | Use when task spans **multiple** packs |
| [mars-reality-index-v0.md](mars-reality-index-v0.md) | Bucket orientation (operational vs conceptual…) | Overlaps topology index | Use when **mythology** risk is the question |
| [projects/mars-website-factory/README.md](../projects/mars-website-factory/README.md) | Pack identity + large Pack index | Pack index ~200 lines competes with OPERATIONAL-INDEX | Factory tasks: README header + [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) **one row** |
| [projects/mars-website-factory/OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) | Stabilization by concern | Very wide table | **Live session SoT** for Factory — not full table scan |
| [projects/orca/OPERATIONAL-INDEX.md](../projects/orca/OPERATIONAL-INDEX.md) | Live-first PPC sessions | Healthier pattern than Factory width | Model for **single live index** discipline |
| [agents/mars-forge/README.md](../agents/mars-forge/README.md) | Forge orientation + long checklist list | Scroll + mirror anxiety | Forge tasks: README § What Forge is + [AGENT.md](../agents/mars-forge/AGENT.md) |
| [mars-runtime/README.md](../mars-runtime/README.md) | Contracts vs R1 | Runtime implied by folder name | **Only** if task is runtime/R1; else skip |
| [web-gpt-sources/](../web-gpt-sources/) | Legacy imported pack | Contradicts current governance if read first | **Historical** — never day-one unless reconciling legacy |
| [web-gpt-sources/chat-migration/README.md](../web-gpt-sources/chat-migration/README.md) | Chat handoff bridge | Points to governance S2–S7 | Use for **session migration**, not greenfield onboarding |
| [continuity/README.md](../continuity/README.md) | IdeaBox capture | Optional discipline | After core four — if capturing ideas cross-session |

---

## 2. Shortest viable orientation paths

### Path A — MARS core (any lane, day one)

Aligns with [onboarding-survivability.md](onboarding-survivability.md) §1:

1. [README.md](../README.md) — identity + phase (not full layout table)  
2. [AGENTS.md](../AGENTS.md)  
3. [survivability-canonical-entrypoint-model-v0.md](survivability-canonical-entrypoint-model-v0.md) — Tier 0–3; **one** Tier 1 router per session when needed  
4. [parallel-cursor-chat-work-mode-v0.md](parallel-cursor-chat-work-mode-v0.md) — if using multiple Cursor chats or mixed lanes  
5. **Stop** — open **one** task-specific file (governance/README = **one row** only if required)

**Time budget:** one session segment; no pack depth unless assigned.

### Path B — Website Factory delivery

1. Path A stops 1–2 only (honesty baseline)  
2. [projects/mars-website-factory/README.md](../projects/mars-website-factory/README.md) — pack boundary paragraph  
3. [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) — **pick one concern row**  
4. [website-factory-workflow-v0.md](../projects/mars-website-factory/website-factory-workflow-v0.md) **or** [first-operational-runbook-v0.md](../projects/mars-website-factory/first-operational-runbook-v0.md)  
5. If frontend implementation: [agents/frontend-gulp-agent/README.md](../agents/frontend-gulp-agent/README.md) → then Forge [AGENT.md](../agents/mars-forge/AGENT.md) if overlay applies  

**Do not** open meta-governance or drift taxonomies on day one.

### Path C — Forge overlay only

1. Path A stops 1–2  
2. [agents/frontend-gulp-agent/README.md](../agents/frontend-gulp-agent/README.md) — foundation first  
3. [agents/mars-forge/README.md](../agents/mars-forge/README.md) — § What Forge is / is not  
4. [agents/mars-forge/AGENT.md](../agents/mars-forge/AGENT.md) + [workflow.md](../agents/mars-forge/workflow.md)  
5. [operational-modes-model.md](../projects/mars-website-factory/operational-modes-model.md) — pick **light** or **standard** mode  

### Path D — Runtime / R1 experiment

1. Path A stops 1–2  
2. [mars-runtime/README.md](../mars-runtime/README.md)  
3. [runtime-registry-boundaries.md](runtime-registry-boundaries.md)  
4. [validation-chain-semantics.md](validation-chain-semantics.md) — validation class vocabulary  
5. Cited R1 script path only — manual invocation  

### Path E — ORCA / WPilot / MetaBOT (external lane)

1. Path A stops 1–2  
2. Pack README + pack **OPERATIONAL-INDEX** (ORCA) or [operator-entrypoints-v1.md](../projects/orca/operator-entrypoints-v1.md)  
3. [external-system-boundaries.md](external-system-boundaries.md) or [external-systems-relationship-map-v0.md](external-systems-relationship-map-v0.md) — **one** external map read  

---

## 3. Reducing “where do I start?” pressure

| Pressure | Strategy |
|----------|----------|
| Too many global maps | **One global map per question:** topology (entities) OR reality index (buckets) — not both |
| Factory README vs OPERATIONAL-INDEX | README = identity + honesty; OPERATIONAL-INDEX = **session navigation** |
| Governance README overwhelm | Treat as **catalog**, not syllabus — link from task, never read entire table |
| Forge vs Gulp | Always **Gulp foundation first**; Forge only when assignment says overlay |
| Chat migration pack vs governance | Migration pack = shortcut; governance wins on conflict |

---

## 4. Reducing repeated explanations

| Instead of re-writing… | Link once |
|------------------------|-----------|
| Documented vs planned vs legacy | [AGENTS.md](../AGENTS.md) |
| Registry ≠ runtime | [registry-architecture.md](registry-architecture.md) + [canonical-terminology-registry.md](canonical-terminology-registry.md) |
| Factory not an engine | [safe-unknown-boundary.md](../projects/mars-website-factory/safe-unknown-boundary.md) |
| Forge overlay rules | [mars-forge-transition-stabilization-v0.md](mars-forge-transition-stabilization-v0.md) |
| Lane discipline | [parallel-cursor-chat-work-mode-v0.md](parallel-cursor-chat-work-mode-v0.md) |

**Prompt discipline:** AGENTS + one governance file + one pack path — per [operator-load-management.md](operator-load-management.md).

---

## 5. Operator confusion hotspots (watch list)

1. **Triumph / V3 charter** read as production proof — charter is **doctrine validation**, not deployment.  
2. **OPERATIONAL-INDEX** read end-to-end — use **one row** per session.  
3. **web-gpt-sources** read as current product — mark **historical input**.  
4. **validation-runtime-overview-v0** — documentation vocabulary only.  
5. **Multiple START HERE** — [ecosystem-topology-index.md](ecosystem-topology-index.md) and [mars-reality-index-v0.md](mars-reality-index-v0.md) are **after** AGENTS, not parallel roots.

---

## 6. What we will NOT build

- Onboarding portal, checklist LMS, or video curriculum  
- Automated “read order” enforcement  
- Per-role mandatory reading lists longer than Path A–E above  
- New meta-onboarding governance layer  

---

## 7. Human maintenance hooks

When adding a pack or major doc cluster:

1. Add **one** OPERATIONAL-INDEX or pack index row — not a new README essay.  
2. State **path letter** (A–E) in the pack README header.  
3. If a new “start here” appears, **remove or downgrade** an old one in the same pass.  

---

## Related

- [survivability-canonical-entrypoint-model-v0.md](survivability-canonical-entrypoint-model-v0.md)  
- [survivability-architecture-weight-review-v0.md](survivability-architecture-weight-review-v0.md)
