# ORCA ↔ Website Factory — Coordination Layer

**Status:** v1 foundation (2026-05-28)  
**Scope:** Triumph Manipulator Krasnodar — production semantic pack generation and Factory handoff  
**Not:** runtime, orchestration engine, auto-page generation, or Factory replacement

---

## What this layer is

Human-operated **coordination architecture** between:

| Lane | Role |
|------|------|
| **ORCA** | Semantic authority — PPC, intent, trust, CTA, FAQ, route strategy, visual semantics, semantic locks |
| **Website Factory** | Frontend implementation authority — HTML, SCSS, responsive, layout polish, overflow fixes |
| **Human operator** | Final approval, drift resolution, launch gates, semantic conflict arbitration |

This folder **does not** implement integration. It **defines contracts, pipelines, checklists, and route priorities** so ORCA can produce production-ready semantic packs and Factory can implement them in **V6** without rewriting commercial meaning.

---

## Production baseline (canonical)

| Item | Path |
|------|------|
| **Active frontend workspace** | `workspaces/triumph-manipulator-landing-v6/` |
| **V6 rules** | `projects/triumph-manipulator-landing/TRIUMPH-V6-CURRENT-FRONTEND-RULES.md` |
| **Rollout plan** | `projects/triumph-manipulator-landing/V6-PAGE-ROLLOUT-PLAN.md` |
| **V5 evolution reference** | `workspaces/triumph-manipulator-landing-v5/` — calibration/history only |
| **ORCA project container** | `projects/orca/projects/triumph-manipulator-krasnodar/` |
| **Route registry** | `projects/orca/projects/triumph-manipulator-krasnodar/landing-route-registry.json` |

**Rule:** All **new** production semantic packs target **V6** structure and partial conventions (`v5-ppc/<slug>/` + shared `v5-page01/*`). V5 is not the implementation target.

---

## Documents in this folder

| # | File | Purpose |
|---|------|---------|
| 01 | [orca-factory-coordination-protocol-v1.md](orca-factory-coordination-protocol-v1.md) | **Main contract** — role separation, deliverables, forbidden Factory actions |
| 02 | [semantic-pack-generation-system-v1.md](semantic-pack-generation-system-v1.md) | How ORCA produces structured landing content packs |
| 03 | [route-pack-generation-rules-v1.md](route-pack-generation-rules-v1.md) | Per-route generation rules for 11 remaining PPC routes |
| 04 | [route-priority-roadmap-v1.md](route-priority-roadmap-v1.md) | Generation order and rationale |
| 05 | [visual-semantic-injection-rules-v1.md](visual-semantic-injection-rules-v1.md) | How visual semantics reach frontend (not via CSS generation) |
| 06 | [semantic-density-control-v1.md](semantic-density-control-v1.md) | Density budgets — why v4 hero failed, v6 productive |
| 07 | [production-pack-readiness-checklist-v1.md](production-pack-readiness-checklist-v1.md) | Pre-handoff gate for ORCA packs |
| 08 | [remaining-routes-status-matrix-v1.md](remaining-routes-status-matrix-v1.md) | 12-route status snapshot |
| 09 | [factory-handoff-minimum-contract-v1.md](factory-handoff-minimum-contract-v1.md) | Minimum fields Factory must receive |

---

## Upstream references (read, do not duplicate)

| Layer | Path |
|-------|------|
| Semantic lock (MODE 1) | `projects/orca/intelligence/orca-website-factory-semantic-lock-v0.md` |
| Content pack system | `projects/orca/content-packs/content-pack-system-v0.md` |
| Pack → Factory workflow | `projects/orca/content-packs/workflows/pack-to-factory-workflow-v0.md` |
| Visual semantics | `projects/orca/visual-semantics/` |
| Calibration (Triumph) | `projects/orca/calibration/triumph-manipulator/` |
| PPC blueprints | `projects/orca/ppc/triumph-manipulator/landing-pages/` |
| Example packs | `projects/orca/content-packs/examples/triumph-manipulyator-zakaz-pack-v1/` · `triumph-manipulyator-5-tonn-pack-v0.md` |

### Operational mapping references (V5 — evolution only)

User charter references these as **operational mapping** aids. **SAFE UNKNOWN:** paths `TRIUMPH-V5-LANDING-LOCK-MAP.md`, `TRIUMPH-V5-CONTENT-SLOT-MAP.md`, `TRIUMPH-V5-SOURCE-MAP.md` were **not found** in-repo at coordination layer authoring. Use V6 structure map and pack section IDs until those files are committed or path is confirmed.

Substitutes:

- Slot / section model → `content-pack-system-v0.md` (10 sections)
- Locks → pack `factory/semantic-lock.md`, `factory/forbidden-drift.md`, visual semantics bundle
- V6 active partial map → `projects/triumph-manipulator-landing/V6-ACTIVE-STRUCTURE-MAP.md`

---

## Explicit non-goals

- No orchestration engine, crawler runtime, or autonomous workflows
- No changes to `governance/*`, `mars-runtime/*`, exporter-cli, validation-cli
- No batch auto-build of 11 pages
- No DOCX/PDF/XLSX generation in this layer (export remains separate human-operated tooling)

---

## Next operator step

1. Complete **one** pilot semantic pack + handoff for a HIGH-priority route (see [route-priority-roadmap-v1.md](route-priority-roadmap-v1.md)).
2. Factory implements in V6 per [factory-handoff-minimum-contract-v1.md](factory-handoff-minimum-contract-v1.md).
3. Update [remaining-routes-status-matrix-v1.md](remaining-routes-status-matrix-v1.md) after HITL QA.
