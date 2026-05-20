# HomeGateway v4.ai — roadmap v0.1

**Статус:** **DRAFT** · **PLANNING**

Фазы 0–8. Даты **не** фиксируются — human-operated progression.

---

## Phase 0 — MARS project entity and architecture docs

**Статус:** **выполняется / baseline** (2026-05-20)

| Deliverable | State |
|-------------|-------|
| `projects/homegateway-v4-ai/` pack | ✓ this task |
| Architecture docs v0.1 | ✓ |
| Registry row | ✓ see project-registry |

**Не claim:** frontend, backend, integrations.

---

## Phase 1 — UX discovery and cockpit architecture

**Статус:** **baseline complete** (2026-05-20) — foundation docs; wireframes **not** started.

| Output | Doc | State |
|--------|-----|-------|
| UX discovery notes | [ux-discovery-notes-v0.1.md](ux-discovery-notes-v0.1.md) | ✓ draft |
| Screen map | [screen-map-v0.1.md](screen-map-v0.1.md) | ✓ draft |
| Block-screen taxonomy | [block-screen-taxonomy-v0.1.md](block-screen-taxonomy-v0.1.md) | ✓ draft |
| Layout zones | [cockpit-layout-zones-v0.1.md](cockpit-layout-zones-v0.1.md) | ✓ draft |
| Admin entry + static prep | [admin-entry-and-future-crud-notes-v0.1.md](admin-entry-and-future-crud-notes-v0.1.md) | ✓ draft |
| Blueprint / module / signal updates | cockpit-architecture, module-registry, signal-system | ✓ aligned |

**Exit → Phase 2:** multi-view UX architecture docs (see Phase 2 section).

**Entry:** [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) rows 2a–2e.

---

## Phase 2 — Multi-view cockpit UX architecture + wireframes

**Статус:** **wireframe pack complete** (2026-05-20) — UX + wireframe docs; **HTML prototype not started**.

| Output | Doc | State |
|--------|-----|-------|
| Multi-view cockpit system | [multi-view-cockpit-system-v0.1.md](multi-view-cockpit-system-v0.1.md) | ✓ draft |
| Operational modes A–H | [operational-modes-v0.1.md](operational-modes-v0.1.md) | ✓ draft |
| Navigation hierarchy | [navigation-hierarchy-v0.1.md](navigation-hierarchy-v0.1.md) | ✓ draft |
| Layout variants reframe (A–D = modes) | [layout-variants-analysis-v0.1.md](layout-variants-analysis-v0.1.md) | ✓ draft |
| Cognitive load / density | [cognitive-load-and-density-notes-v0.1.md](cognitive-load-and-density-notes-v0.1.md) | ✓ draft |
| Cockpit OS concept (conceptual only) | [cockpit-os-concept-notes-v0.1.md](cockpit-os-concept-notes-v0.1.md) | ✓ draft |
| Screen map + layout zones alignment | screen-map, cockpit-layout-zones | ✓ aligned |
| Wireframe Exploration Pack v0.1 | [wireframes/](wireframes/) | ✓ draft (docs only) |
| HTML wireframe prototype | `workspaces/homegateway-v4-ai/` | **not started** |
| Block-screen size variants on wireframes | S / M / L in wireframe docs | ✓ referenced |

**Exit → Phase 3:** visual direction charter; HTML prototype after workspace charter.

**HTML-first:** [wireframes/wireframe-exploration-pack-v0.1.md](wireframes/wireframe-exploration-pack-v0.1.md).

**Entry:** [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) Phase 2 rows.

**SAFE UNKNOWN:** Workspace charter date; Gulp vs plain npm in workspace.

---

## Phase 3 — Visual direction: dark/light cockpit style

| Output | Notes |
|--------|-------|
| Visual reference board | Glass, glow restraint |
| Token value freeze (draft → approved) | [theme-system-draft-v0.1.md](theme-system-draft-v0.1.md) |

---

## Phase 4 — Static frontend MVP

**Label:** **STATIC-FIRST**

| Must have | Must not |
|-----------|----------|
| Static login ([screen-map](screen-map-v0.1.md)) | Real auth backend |
| Main cockpit + layout zones sample | Live MARS API |
| Sample clients/projects, deadlines, recurring | n8n execution |
| MARS + bots display-only blocks | Admin CRUD |
| Leads (Polygon + MetaCODE) sample | Backend |
| Quick actions + clipboard mock | Workspace (until charter) |
| Popup layer mock | |
| Admin entry visible (stub) | Production deploy claim |
| Dark/light semantic tokens | Hardcoded colors |
| Admin-aware HTML structure ([admin-entry notes](admin-entry-and-future-crud-notes-v0.1.md)) | |

**Workspace:** path TBD (`workspaces/homegateway-v4-ai/` recommended — **not created** in Phase 0).

---

## Phase 5 — Admin area design

| Output | Notes |
|--------|-------|
| Admin IA + wireframes | [admin-layer-plan-v0.1.md](admin-layer-plan-v0.1.md) |
| Entity forms spec | Align module registry |

Implementation still **after** static MVP validation.

---

## Phase 6 — Dynamic data model

| Output | Notes |
|--------|-------|
| Data schema (clients, projects, deadlines, …) | Storage choice charter |
| Replace sample data in cockpit | Admin CRUD implementation begins |

**FUTURE-INTEGRATION** boundary: still no full MARS control.

---

## Phase 7 — Integrations with MARS / n8n / bots / leads

**Label:** **FUTURE-INTEGRATION**

| Integration | Direction |
|-------------|-----------|
| Local data storage | Operator machine or self-hosted |
| n8n bridge | Status / last run display |
| Telegram bot status | Registry + health display |
| MARS display API or export | Read-only blocks |
| Event/task history | Timeline module |
| Lead/request feed | Polygon + MetaCODE |
| Admin CRUD | Live |
| System health checks | Optional HTTP probes |

**Не claim** orchestration or autonomous actions.

---

## Phase 8 — Operational hardening

| Topic | Examples |
|-------|----------|
| Security | Auth hardening, secrets hygiene |
| Backup/export | Cockpit data export |
| Audit | Admin change log |
| Performance | Lazy load, large lists |
| Reliability | Degraded mode when MARS/n8n unreachable |

---

## Dependency graph (simplified)

```text
Phase 0 ──► Phase 1 ──► Phase 2 ──► Phase 3 ──► Phase 4 (STATIC MVP)
                                                      │
                      Phase 5 (admin design) ◄────────┤
                              │
                              ▼
                      Phase 6 (data model)
                              │
                              ▼
                      Phase 7 (integrations)
                              │
                              ▼
                      Phase 8 (hardening)
```

---

## SAFE UNKNOWN

- Parallel vs serial Phases 5 and 4 — operator choice.
- Whether Phase 7 subsets ship incrementally — yes, likely; order TBD.

---

*Last updated: 2026-05-20 — Wireframe Exploration Pack v0.1.*
