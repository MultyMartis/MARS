# HomeGateway v4.ai — operational index

**Статус:** **DRAFT** · **PLANNING** · Phase 2 active (Phase 1 foundation complete)  
**Назначение:** одна короткая карта для оператора и агента — куда идти в сессии, без полного каталога governance.

**Не является:** runtime-индексом, API-каталогом, реестром деплоя.

**Идентичность пакета:** [README.md](README.md) · **project_id:** `homegateway-v4-ai`

---

## Canonical entry

- **[README.md](README.md)** — границы, честность, карта документов v0.1.

---

## Phase 1 pack (UX discovery foundation)

Использовать при работе в **Phase 1** (до wireframes). Полный набор:

| Doc | Role |
|-----|------|
| [ux-discovery-notes-v0.1.md](ux-discovery-notes-v0.1.md) | JTBD, сценарии, pain points |
| [screen-map-v0.1.md](screen-map-v0.1.md) | Экраны и static MVP checklist |
| [block-screen-taxonomy-v0.1.md](block-screen-taxonomy-v0.1.md) | Типы и размеры block-screen |
| [cockpit-layout-zones-v0.1.md](cockpit-layout-zones-v0.1.md) | Зоны shell (non-binding layout) |
| [admin-entry-and-future-crud-notes-v0.1.md](admin-entry-and-future-crud-notes-v0.1.md) | Admin entry + admin-aware static prep |

---

## Core Run (default session)

Открывать **одну строку** за сессию, если задача не требует соседних фаз явно.

| # | Concern | Purpose | Entry file | When to use | Output expected |
|---|---------|---------|------------|-------------|-----------------|
| 1 | **Project architecture** | Роль HG в MARS, block-screen, границы MVP | [cockpit-architecture-blueprint-v0.1.md](cockpit-architecture-blueprint-v0.1.md), [product-positioning-v0.1.md](product-positioning-v0.1.md) | Новый участник; scope gate | Модель кокпита; non-goals |
| 2a | **UX discovery notes** | Задачи оператора, сценарии дня, приоритеты | [ux-discovery-notes-v0.1.md](ux-discovery-notes-v0.1.md) | Старт Phase 1; перед screen map | JTBD table; open questions list |
| 2b | **Screen map** | Инвентарь экранов, static MVP screen checklist | [screen-map-v0.1.md](screen-map-v0.1.md) | После 2a; перед wireframes | Согласованный screen inventory |
| 2c | **Block-screen taxonomy** | Типы, размеры, разметка admin-aware | [block-screen-taxonomy-v0.1.md](block-screen-taxonomy-v0.1.md) | Параллельно 2b; перед layout | Taxonomy + markup conventions |
| 2d | **Layout zones** | Shell zones; variants = mode tendencies | [cockpit-layout-zones-v0.1.md](cockpit-layout-zones-v0.1.md), [layout-variants-analysis-v0.1.md](layout-variants-analysis-v0.1.md) | Phase 2 | Zone catalog + A–D reframe |
| 2e | **Admin-aware static prep** | Entry point + CRUD entity map для static HTML | [admin-entry-and-future-crud-notes-v0.1.md](admin-entry-and-future-crud-notes-v0.1.md), [admin-layer-plan-v0.1.md](admin-layer-plan-v0.1.md) | До Phase 4 static | Admin entry spec + data-structure checklist |
| **2f** | **Multi-view cockpit system** | HG как connected views, не one dashboard | [multi-view-cockpit-system-v0.1.md](multi-view-cockpit-system-v0.1.md) | Phase 2 start | Canonical multi-view model |
| **2g** | **Operational modes** | Modes A–H: purpose, density, risks | [operational-modes-v0.1.md](operational-modes-v0.1.md) | После 2f | Mode spec table |
| **2h** | **Navigation hierarchy** | L1/L2/L3, overlays, mode switch | [navigation-hierarchy-v0.1.md](navigation-hierarchy-v0.1.md) | После 2g | Navigation model |
| **2i** | **Cockpit ergonomics** | Density, cognitive load, overload risks | [cognitive-load-and-density-notes-v0.1.md](cognitive-load-and-density-notes-v0.1.md) | Параллельно wireframes | Density guidelines |
| **2j** | **Cockpit OS concept** | Conceptual environment direction only | [cockpit-os-concept-notes-v0.1.md](cockpit-os-concept-notes-v0.1.md) | On demand | Terminology guardrails |
| 3 | **Wireframes** | HTML-oriented exploration pack | [wireframes/README.md](wireframes/README.md), [wireframes/wireframe-exploration-pack-v0.1.md](wireframes/wireframe-exploration-pack-v0.1.md) | После 2f–2h | Wireframe docs (no HTML yet) |
| **3a** | **Main cockpit wireframe** | Mode D composition | [wireframes/main-cockpit-wireframe-v0.1.md](wireframes/main-cockpit-wireframe-v0.1.md) | Row 3 | ASCII layout + blocks |
| **3b** | **Systems monitor wireframe** | Mode B grid | [wireframes/systems-monitor-wireframe-v0.1.md](wireframes/systems-monitor-wireframe-v0.1.md) | Row 3 | Status grid spec |
| **3c** | **Focus workspace wireframe** | Mode C minimal | [wireframes/focus-workspace-wireframe-v0.1.md](wireframes/focus-workspace-wireframe-v0.1.md) | Row 3 | Low-noise layout |
| **3d** | **Tactical signals wireframe** | Urgency + filters | [wireframes/tactical-signals-wireframe-v0.1.md](wireframes/tactical-signals-wireframe-v0.1.md) | Row 3 | Signal display rules |
| **3e** | **Navigation shell** | L1/L2/L3 | [wireframes/navigation-shell-wireframe-v0.1.md](wireframes/navigation-shell-wireframe-v0.1.md) | Row 3 | Shell + mode indicator |
| **3f** | **Overlay behavior** | L3 panels | [wireframes/overlay-and-popup-behavior-v0.1.md](wireframes/overlay-and-popup-behavior-v0.1.md) | Row 3 | Overlay types + stack rules |
| **3g** | **Static prototype readiness** | Phase 4 HTML prep | [wireframes/static-prototype-readiness-checklist-v0.1.md](wireframes/static-prototype-readiness-checklist-v0.1.md) | Before workspace | Checklist gate |
| 4 | **Visual direction** | Dark/light cockpit, glass, signals | [theme-system-draft-v0.1.md](theme-system-draft-v0.1.md) | Перед static MVP | Token groups approved for Phase 3 |
| 5 | **Static frontend MVP** | Mock login, cockpit, samples, admin stub | [screen-map-v0.1.md](screen-map-v0.1.md) § Static MVP · [README.md](README.md) | Phase 4 only | Static prototype; **no** backend |
| 6 | **Admin layer (future CRUD)** | Полный CRUD после static | [admin-layer-plan-v0.1.md](admin-layer-plan-v0.1.md) | Phase 5–6 | Admin IA + entity forms |
| 7 | **Future integrations** | MARS/n8n/bots/leads | [roadmap-v0.1.md](roadmap-v0.1.md) Phase 7, [signal-system-draft-v0.1.md](signal-system-draft-v0.1.md) | После static MVP | FUTURE-INTEGRATION backlog |

**Phase 1 exit criteria:** docs 2a–2e согласованы ✓ (2026-05-20).

**Phase 2 exit criteria (draft):** 2f–2h + layout variants analysis ✓; wireframe pack (row 3, 3a–3g) ✓ (2026-05-20); **HTML files not started**.

---

## Wireframe pack (HTML-first, Phase 2)

| Doc | Role |
|-----|------|
| [wireframes/README.md](wireframes/README.md) | Folder entry |
| [wireframes/wireframe-exploration-pack-v0.1.md](wireframes/wireframe-exploration-pack-v0.1.md) | Master pack + density experiments |
| [wireframes/main-cockpit-wireframe-v0.1.md](wireframes/main-cockpit-wireframe-v0.1.md) | Default home (D) |
| [wireframes/systems-monitor-wireframe-v0.1.md](wireframes/systems-monitor-wireframe-v0.1.md) | Systems (B) |
| [wireframes/focus-workspace-wireframe-v0.1.md](wireframes/focus-workspace-wireframe-v0.1.md) | Focus (C) |
| [wireframes/tactical-signals-wireframe-v0.1.md](wireframes/tactical-signals-wireframe-v0.1.md) | Tactical / rail hybrid |
| [wireframes/navigation-shell-wireframe-v0.1.md](wireframes/navigation-shell-wireframe-v0.1.md) | Shell L1–L3 |
| [wireframes/overlay-and-popup-behavior-v0.1.md](wireframes/overlay-and-popup-behavior-v0.1.md) | Overlays |
| [wireframes/static-prototype-readiness-checklist-v0.1.md](wireframes/static-prototype-readiness-checklist-v0.1.md) | Phase 4 gate |

**Decision:** HTML wireframe prototype preferred over Figma-first.

---

## Phase 2 pack (multi-view cockpit UX)

| Doc | Role |
|-----|------|
| [multi-view-cockpit-system-v0.1.md](multi-view-cockpit-system-v0.1.md) | Why multi-view; view inventory |
| [operational-modes-v0.1.md](operational-modes-v0.1.md) | Modes A–H specification |
| [navigation-hierarchy-v0.1.md](navigation-hierarchy-v0.1.md) | L1/L2/L3 navigation |
| [layout-variants-analysis-v0.1.md](layout-variants-analysis-v0.1.md) | A–D reframe + SaaS anti-patterns |
| [cognitive-load-and-density-notes-v0.1.md](cognitive-load-and-density-notes-v0.1.md) | Density scaling, risks |
| [cockpit-os-concept-notes-v0.1.md](cockpit-os-concept-notes-v0.1.md) | Cockpit OS concept (not real OS) |

---

## Supporting docs (on demand)

| Concern | Entry |
|---------|--------|
| Module inventory | [module-registry-draft-v0.1.md](module-registry-draft-v0.1.md) |
| Signals & deadlines | [signal-system-draft-v0.1.md](signal-system-draft-v0.1.md) |
| Phases 0–8 | [roadmap-v0.1.md](roadmap-v0.1.md) |
| Registry row | [registry/project-registry.md](../../registry/project-registry.md) |

---

## Session discipline

1. **Один Core Run row** — Phase 1: последовательность 2a → 2e или одна строка за сессию.
2. **STATIC-FIRST** — не проектировать backend в Phase 1.
3. **FUTURE-INTEGRATION** — live MARS/n8n/bots только planned.
4. **STOP** — после screen map + zones достаточно для wireframes; не уходить в Phase 4 code.

---

## SAFE UNKNOWN

| Topic | Note |
|-------|------|
| Wireframes location | `projects/homegateway-v4-ai/wireframes/` (docs); HTML in future workspace |
| Workspace folder | `workspaces/homegateway-v4-ai/` — **не создан** |
| Leads dedicated mode vs Main block | Wireframes |
| Static MVP minimum view count | Likely Main + 1 specialized |

---

*Last updated: 2026-05-20 — Wireframe Exploration Pack v0.1.*
