# MARS — Cross-system clarity review v0

**Status:** **documented** — relationship visibility (Phase 2).  
**Date:** 2026-05-19.  
**Is not:** new architecture, integration design, or orchestration spec.

**Complements:** [external-systems-relationship-map-v0.md](external-systems-relationship-map-v0.md), [ecosystem-topology-index.md](ecosystem-topology-index.md).

---

## 1. Factory ↔ Forge

| Dimension | Clarity |
|-----------|---------|
| **Factory owns** | Methodology, contracts, governance triads, workflow stages, agent **role** map |
| **Forge owns** | **Overlay** on Gulp frontend lane: phased build, freeze, operator checklists, QA finding blocks |
| **Handoff** | Factory `frontend-handoff-contract-v0.md` + production rules → Forge pipeline docs |
| **Not** | Forge does **not** replace Factory semantics or Gulp SoT; Factory does **not** execute builds |
| **Drift risk** | Duplicate concern in Factory governance + Forge checklist — treat checklist as **operational shorthand** |
| **SoT pair** | Factory README / OPERATIONAL-INDEX ↔ `agents/mars-forge/README.md` |

```text
Factory (methodology) ──contracts──► Gulp foundation ──overlay──► Forge (discipline/QA)
```

---

## 2. ORCA ↔ Website Factory

| Dimension | Clarity |
|-----------|---------|
| **Relationship** | **Loosely coupled** program packs; shared MARS governance honesty only |
| **ORCA owns** | PPC review, SERP/heuristics, campaign QA — **external ad platforms** |
| **Factory owns** | Site production methodology — **not** bidding or ad copy automation |
| **Overlap zone** | Landing **review** (ORCA) may reference Factory-produced sites — **human** crosswalk, no automatic bus |
| **Not** | ORCA is **not** a Factory stage; Factory is **not** an ORCA module |
| **Drift risk** | Similar “review checklist” language — different domains; label lane in REPORT |
| **SoT pair** | `projects/orca/OPERATIONAL-INDEX.md` ↔ `projects/mars-website-factory/OPERATIONAL-INDEX.md` |

---

## 3. MetaBOT ↔ External systems

| Dimension | Clarity |
|-----------|---------|
| **MetaBOT** | **External operational** system (n8n); MARS holds **canonical docs** + exports |
| **MARS relationship** | Boundary docs + optional **experimental** R1 adapter — **no dispatch** |
| **Legacy** | `seo-content-agent` — **deprecated** path; do not conflate with MetaBOT |
| **Execution truth** | Live n8n graphs, credentials, workflow IDs — **outside repo** |
| **Not** | MetaBOT ⊂ MARS core; MARS ⊂ MetaBOT ops |
| **SoT** | `projects/metabot-seo-content-agent/README.md` + [external-system-boundaries.md](external-system-boundaries.md) |

---

## 4. WPilot ↔ operational tooling

| Dimension | Clarity |
|-----------|---------|
| **WPilot** | External Systems lane — **human** WordPress administration discipline |
| **tools/** | Repo helpers (registry-checker, link validator, etc.) — **manual**, cross-lane |
| **Relationship** | WPilot may **later** consume Factory-approved payloads via **planned** plugin — not wired today |
| **tools/ ≠ WPilot** | Helpers do **not** administer WordPress; WPilot docs are **not** generic MARS tooling platform |
| **Mode A vs B** | Factory-native (target) vs legacy builder compatibility — see WPilot plugin concept |
| **SoT pair** | `projects/wpilot/README.md` ↔ [operational-tooling-overview.md](operational-tooling-overview.md) |

---

## 5. Runtime research ↔ Governance

| Dimension | Clarity |
|-----------|---------|
| **Governance owns** | Honesty, registries, execution model, **forbidden claims**, stage roadmap **documentation** |
| **mars-runtime owns** | Future-integration **contracts** + **narrow R1** experiments |
| **Relationship** | Governance **constrains claims** about runtime; runtime folder **does not** satisfy governance stages |
| **Stage 8.5 / 13** | Readiness **docs** — not implementation proof |
| **Not** | Governance markdown **enforcing** R1 scripts; R1 **proving** governance automation |
| **SoT pair** | [runtime-registry-boundaries.md](runtime-registry-boundaries.md) ↔ [execution-boundary-clarification.md](execution-boundary-clarification.md) |

---

## 6. Triumph ↔ reference / project / workspace boundaries

| Layer | Path role | Authority |
|-------|-----------|-----------|
| **Factory reference case** | `projects/mars-website-factory/reference-cases/triumph-…` | Methodology calibration — **doc-first simulated run** |
| **Project pack** | `projects/triumph-manipulator-landing/` | Passport, gates, V3 charter, handoff status |
| **Workspace** | `workspaces/triumph-manipulator-landing*` | **Execution locus** — implementation attempts; **not** governance SoT |
| **V3** | Charter docs | Battle-test **preparation** — **not** production authorization |
| **V2** | Stabilization / lessons | **Lessons only** for V3 — not implementation authority |

| Boundary rule |
|---------------|
| Workspace output **does not** prove Factory runtime |
| Reference case **does not** replace project pack for delivery decisions |
| Registry `planned` **does not** mean site unpublished — **SAFE UNKNOWN** for deploy state |

**SoT:** [../projects/triumph-manipulator-landing/V3-SOURCE-AUTHORITY.md](../projects/triumph-manipulator-landing/V3-SOURCE-AUTHORITY.md), [V2-FRONTEND-SOURCE-OF-TRUTH.md](../projects/triumph-manipulator-landing/V2-FRONTEND-SOURCE-OF-TRUTH.md)

---

## 7. Cross-system visibility matrix

| From → To | Factory | Forge | ORCA | MetaBOT | WPilot | mars-runtime | Triumph |
|-----------|---------|-------|------|---------|--------|--------------|---------|
| **Factory** | — | overlay target | optional landing review | SEO content **external** | future publish | no dispatch | reference case |
| **Forge** | consumes contracts | — | — | — | — | no runtime | battle-test QA |
| **ORCA** | landing context | — | — | — | — | — | live pilot notes |
| **MetaBOT** | content SEO **parallel** | — | — | — | — | experimental adapter | — |
| **WPilot** | future handoff | — | — | — | — | — | deploy **external** |
| **mars-runtime** | no factory engine | — | — | adapter sketch | — | — | — |

---

## 8. Recommended REPORT labels (lane discipline)

| Lane | Opening label |
|------|----------------|
| Factory / Forge / Triumph frontend | `Lane A — production methodology` |
| Governance / registry / stabilization | `Lane B — MARS core docs` |
| mars-runtime / adapters | `Runtime research — experimental` |
| MetaBOT / WPilot / n8n | `External systems — execution outside repo` |
| ORCA | `ORCA operational toolkit — human PPC` |

---

## 9. SAFE UNKNOWN

- Factory ↔ WPilot wire format when plugin ships — **not specified** in-tree  
- ORCA ↔ Triumph live pilot data freshness — **operator**  
- GitGuard future relationship to any pack — **none evidenced**  

---

*Cross-system clarity review — boundaries only; integrate via human envelopes and REPORT, not new buses.*
