# HomeGateway v4.ai — screen map v0.1

**Статус:** **DRAFT** · **PLANNING** · Phase 2 aligned (was Phase 1)  
**Назначение:** ожидаемые экраны/страницы и их связь с **operational views** до wireframes.

**Не является:** sitemap deployed app, routing implementation.

**Phase 2:** HG — **multi-view cockpit**, не одна hub-страница. См. [multi-view-cockpit-system-v0.1.md](multi-view-cockpit-system-v0.1.md) · [operational-modes-v0.1.md](operational-modes-v0.1.md).

---

## Легенда

| Label | Meaning |
|-------|---------|
| **STATIC-FIRST** | Входит в static MVP v0.1 (mock/sample) |
| **stub** | Видимая точка входа без функционала |
| **FUTURE** | После static MVP / admin / integrations |
| **display-only** | Только чтение внешнего статуса |

---

## Screen inventory

| screen_id | Экран | STATIC-FIRST | Описание |
|-----------|-------|--------------|----------|
| `scr-login` | **Login** | ✓ mock | Статический экран входа; без real auth backend |
| `scr-cockpit-main` | **Main Cockpit** | ✓ | Hub: canvas block-screens + shell zones |
| `scr-clients-projects` | **Clients / Projects** | ✓ sample | Список клиентов и проектов; может быть view или блок на hub |
| `scr-project-detail` | **Project Detail** (Panel or View) | ✓ sample | Детали проекта: ссылки, статус, ресурсы, дедлайны проекта |
| `scr-signals-deadlines` | **Signals / Deadlines** | ✓ sample | Агрегированные дедлайны и recurring; может дублировать signal rail |
| `scr-mars-monitor` | **MARS Monitor** | ✓ display-only sample | Pack/lane hints, registry pointers — **без** control |
| `scr-bots-systems` | **Bots / Systems Monitor** | ✓ display-only sample | n8n, Telegram, прочие — placeholder status |
| `scr-leads-requests` | **Leads / Requests Monitor** | ✓ sample | Web Studio Polygon + MetaCODE |
| `scr-quick-actions` | **Quick Actions** | ✓ sample | Панель/полоса быстрых действий |
| `scr-settings` | **Settings** | ✓ partial | Theme switch; прочие prefs — stub/future |
| `scr-admin-entry` | **Admin Entry** | ✓ stub | Кнопка/ссылка с main shell — всегда видима |
| `scr-admin-area` | **Future Admin Area** | FUTURE | CRUD; не в static MVP |
| `scr-popup-overlay` | **Popup / Overlay layer** | ✓ mock | Модалки, detail panels поверх cockpit |

---

## Screen → operational view mapping (Phase 2)

| screen_id | Primary operational view | Notes |
|-----------|-------------------------|-------|
| `scr-cockpit-main` | `view-main-cockpit` | Default home; hybrid tendency **D** |
| `scr-mars-monitor` | `view-systems-monitor` | With bots/systems |
| `scr-bots-systems` | `view-systems-monitor` | Grid tendency **B** |
| `scr-signals-deadlines` | `view-tactical-signals` | May share content with signal rail |
| `scr-clients-projects` | `view-project` | List entry |
| `scr-project-detail` | `view-project` / `view-focus-workspace` | Panel (L3) or full view |
| `scr-quick-actions` | `view-quick-actions` | Also bottom strip globally |
| `scr-settings` | `view-settings` | |
| `scr-leads-requests` | `view-main-cockpit` (block) | Standalone view optional — TBD wireframes |
| `scr-admin-entry` / `scr-admin-area` | `view-admin` | FUTURE |
| `scr-popup-overlay` | Layer 3 | All views |

---

## Navigation model (Phase 2)

```text
                    ┌─────────────┐
                    │   Login     │  Layer 1
                    └──────┬──────┘
                           ▼
              ┌────────────────────────┐
              │  Cockpit shell (L1)   │
              └───────────┬────────────┘
                           ▼
     ┌─────────────────────────────────────────────┐
     │  Layer 2 — operational modes (views)         │
     │  Main · Systems · Focus · Tactical · Project  │
     │  · Quick Actions · Settings · Admin (future) │
     └───────────┬─────────────────────────────────┘
                 ▼
     Layer 3 — overlays (project detail, modals)
```

**Canonical:** specialized screens = **modes**, not optional extras on one dashboard. Детали: [navigation-hierarchy-v0.1.md](navigation-hierarchy-v0.1.md).

---

## Screen → block-screen / module mapping

| screen_id | Primary modules (see module registry) |
|-----------|--------------------------------------|
| `scr-cockpit-main` | Multiple — canvas composition |
| `scr-clients-projects` | `hg-client-list` |
| `scr-project-detail` | `hg-project-detail`, related links |
| `scr-signals-deadlines` | `hg-deadline-active`, `hg-deadline-recurring` |
| `scr-mars-monitor` | `hg-mars-monitor` |
| `scr-bots-systems` | `hg-bot-status` |
| `scr-leads-requests` | `hg-leads-polygon`, `hg-leads-metacode` |
| `scr-quick-actions` | `hg-quick-actions` |
| `scr-settings` | `hg-settings` |
| `scr-admin-entry` | `hg-admin-entry` |
| shell | `hg-popup-host`, theme zone |

---

## Static MVP screen checklist (v0.1)

| Must appear in static build | Notes |
|-----------------------------|-------|
| Login | Mock submit → cockpit |
| Main cockpit layout | With zones per [cockpit-layout-zones-v0.1.md](cockpit-layout-zones-v0.1.md) |
| Sample client/project blocks | Admin-ready structure |
| Sample deadline + recurring monitors | Signal levels visible |
| Sample MARS block | Display-only label |
| Sample bot/system block | Placeholder rows |
| Sample leads block | Polygon + MetaCODE samples |
| Sample quick actions + clipboard | Mock handlers |
| Popup layer mock | One example modal |
| Admin entry | Visible, links to stub |
| Dark/light theme | Token switch works on sample page |

**Must not:** real backend, live APIs, admin CRUD.

---

## Admin visibility rule

> **Admin area is not implemented in static MVP but must have a visible access point.**

Реализация: `scr-admin-entry` в top command bar или left rail — см. [admin-entry-and-future-crud-notes-v0.1.md](admin-entry-and-future-crud-notes-v0.1.md).

---

## SAFE UNKNOWN

- URL scheme (`/cockpit`, `/cockpit/systems`, …) — Phase 4.
- Leads as dedicated mode vs Main block only — wireframes.
- Deep linking to Project Detail from external tools — FUTURE.
- Minimum view count in static MVP Phase 4 — likely Main + one specialized demo.

---

*Last updated: 2026-05-20 — Phase 2 multi-view alignment.*
