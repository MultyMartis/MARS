# HomeGateway v4.ai — cockpit architecture blueprint v0.1

**Статус:** **DRAFT** · **PLANNING** · **STATIC-FIRST** (target UI shape)

**Phase 1–2 supplements:** [ux-discovery-notes-v0.1.md](ux-discovery-notes-v0.1.md) · [screen-map-v0.1.md](screen-map-v0.1.md) · [block-screen-taxonomy-v0.1.md](block-screen-taxonomy-v0.1.md) · [cockpit-layout-zones-v0.1.md](cockpit-layout-zones-v0.1.md) · **Phase 2:** [multi-view-cockpit-system-v0.1.md](multi-view-cockpit-system-v0.1.md) · [operational-modes-v0.1.md](operational-modes-v0.1.md) · [navigation-hierarchy-v0.1.md](navigation-hierarchy-v0.1.md) · [cockpit-os-concept-notes-v0.1.md](cockpit-os-concept-notes-v0.1.md)  
**Post–Prototype v0.1 spatial canon:** [cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md) · [tactical-signal-philosophy-v0.1.md](tactical-signal-philosophy-v0.1.md) · [viewport-and-scroll-philosophy-v0.1.md](viewport-and-scroll-philosophy-v0.1.md) · [visual-language-direction-v0.1.md](visual-language-direction-v0.1.md) — full pack in [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) § Spatial cockpit architecture

---

## Архитектурная роль

HomeGateway — **Personal Operational Cockpit** / **spatial operational cockpit environment with layered tactical awareness** для владельца веб-студии, AI-assisted production ecosystem, клиентских операций и MARS-connected infrastructure.

Концептуальное направление (не продукт ОС): **Cockpit OS** = unified operational environment — см. [cockpit-os-concept-notes-v0.1.md](cockpit-os-concept-notes-v0.1.md).

Слой: **operational surface** → **multi-view spatial cockpit UI** → **display/control preparation** (управление — только после admin + integrations).

**Phase 2:** HG **не** одна dashboard-страница — connected views per [multi-view-cockpit-system-v0.1.md](multi-view-cockpit-system-v0.1.md).

**Post–Prototype v0.1 (canonical):** dashboard-grid interpretation **deprecated**. Пространственная модель tri-focus (`main_menu` + `main_area` + `info_area`) — [cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md). Legacy `zone-*` ids map to spatial IDs in that doc.

---

## Базовая UX-единица: block-screen

**Block-screen** — основной визуальный и UX-модуль кокпита.

Определение: HTML UI-модуль, который визуально ведёт себя как **high-tech полупрозрачный информационно-действенный экран** («стеклянная» панель на фоне кокпита), в духе sci-fi cockpit interfaces.

**Полная таксономия:** [block-screen-taxonomy-v0.1.md](block-screen-taxonomy-v0.1.md) (типы, размеры, разметка, admin-aware hooks).

### Block-screen может содержать

| Категория | v0.1 | Позже |
|-----------|------|-------|
| Текст, заголовки, метки | ✓ sample | ✓ |
| Ссылки (внутренние/внешние) | ✓ | ✓ |
| Данные клиента/проекта | ✓ sample | live data |
| Индикаторы статуса | ✓ sample | live |
| Дедлайны / recurring | ✓ sample | live |
| Quick actions | ✓ sample | wired actions |
| Clipboard actions | ✓ mock | API/local |
| Графики / инфографика | — | FUTURE |
| Формы | — | admin / inline |
| MARS / bot / system signals | display-only sample | FUTURE-INTEGRATION |

### Block-screen — не

- отдельный iframe-приложение с собственным auth;
- микрофронтенд с независимым деплоем (на v0.1);
- MARS agent card или n8n node.

---

## Структура приложения (логическая)

Shell zones: **canonical spatial** — [cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md); legacy zone_id — [cockpit-layout-zones-v0.1.md](cockpit-layout-zones-v0.1.md).

```text
┌──────────────────────────────────────────────────────────┐
│  top_bar · logo · system_status · theme · admin · user      │
├────┬─────────────────────────────────────────────┬───────┤
│ L  │  main_area (block-screens · operational work) │ info  │
│ E  │  ┌─────────┐ ┌─────────┐ ┌─────────┐        │ area  │
│ F  │  │ block   │ │ block   │ │ block   │  ...   │tactical│
│ T  │  └─────────┘ └─────────┘ └─────────┘        │aware. │
│nav │  main_menu · favorites_used                  │       │
├────┴─────────────────────────────────────────────┴───────┤
│  bottom strip (quick actions · clipboard) — optional      │
├──────────────────────────────────────────────────────────┤
│  overlay layer (L3 — project detail) — mock v0.1          │
└──────────────────────────────────────────────────────────┘
         │
         ▼ (future, not v0.1)
    Admin area (separate route) — entry visible from v0.1
```

---

## Зоны контента главного кокпита

Группы модулей (детали — [module-registry-draft-v0.1.md](module-registry-draft-v0.1.md)):

| Группа | Назначение |
|--------|------------|
| **client/project screens** | Клиенты, проекты, статусы, связанные ресурсы |
| **frequent links & resources** | Частые URL, инструменты, документация |
| **website / admin links** | Сайты, WP-admin, панели хостинга |
| **related project links** | Соседние репозитории, staging, Figma, tickets |
| **MARS monitor** | Display-only: статус паков, сигналы, **без** control plane |
| **bot / system status** | n8n, Telegram, прочие automation surfaces |
| **deadline & recurring monitors** | Active, monthly, reports, danger proximity |
| **quick action blocks** | One-click операторские действия (подготовка) |
| **clipboard data blocks** | Копирование типовых строк, токенов handoff (без секретов в repo) |
| **admin access point** | Видимая точка входа с первого дня |
| **lead/request monitor** | Web Studio Polygon + MetaCODE sites |
| **notes / simple plans** | Опционально / future |
| **settings / interface controls** | Тема, плотность, будущие prefs |

---

## Страницы (минимальный набор v0.1)

Полная карта: [screen-map-v0.1.md](screen-map-v0.1.md).

| Страница | Статус v0.1 |
|----------|-------------|
| Login (mock/static) | STATIC-FIRST |
| Main Cockpit (hub) | STATIC-FIRST |
| Clients / Projects | STATIC-FIRST sample |
| Project Detail (panel or view) | STATIC-FIRST sample |
| Signals / Deadlines | STATIC-FIRST sample |
| MARS Monitor | STATIC-FIRST display-only |
| Bots / Systems Monitor | STATIC-FIRST display-only |
| Leads / Requests | STATIC-FIRST sample |
| Quick Actions | STATIC-FIRST sample |
| Settings (theme) | STATIC-FIRST partial |
| Admin Entry | STATIC-FIRST stub |
| Future Admin Area | **не реализован** |
| Popup / overlay layer | STATIC-FIRST mock |

---

## Потоки данных (честность)

| Слой | Phase |
|------|-------|
| Static HTML + sample JSON inline | v0.1 |
| Local storage / file | Phase 6+ |
| Admin CRUD API | Phase 5–6 |
| MARS / n8n / bots | Phase 7 (**FUTURE-INTEGRATION**) |

**Не проектировать** orchestration pipeline в v0.1.

---

## Принципы проектирования фронтенда

1. **Data attributes over hardcode** — см. [block-screen-taxonomy-v0.1.md](block-screen-taxonomy-v0.1.md) § разметка.
2. **Admin-ready markup** — [admin-entry-and-future-crud-notes-v0.1.md](admin-entry-and-future-crud-notes-v0.1.md).
3. **Theme tokens only** — [theme-system-draft-v0.1.md](theme-system-draft-v0.1.md).
4. **Signal levels visible** — [signal-system-draft-v0.1.md](signal-system-draft-v0.1.md).
5. **Display-only MARS/bots** — без кнопок run/orchestrate на v0.1.

---

## Static MVP boundary (v0.1 recap)

| Include | Exclude |
|---------|---------|
| Static login, main cockpit layout, sample block-screens (clients, deadlines, recurring, MARS, bots, leads, quick actions, clipboard) | Backend |
| Popup mock, admin entry visible, dark/light tokens | Real MARS/n8n/bot APIs |
| Admin-aware HTML structure | Admin CRUD, workspace (until Phase 4 charter) |

---

## Multi-view architecture (Phase 2 summary)

| Concern | Doc |
|---------|-----|
| View system | [multi-view-cockpit-system-v0.1.md](multi-view-cockpit-system-v0.1.md) |
| Modes A–H | [operational-modes-v0.1.md](operational-modes-v0.1.md) |
| Navigation L1–L3 | [navigation-hierarchy-v0.1.md](navigation-hierarchy-v0.1.md) |
| Layout tendencies A–D | [layout-variants-analysis-v0.1.md](layout-variants-analysis-v0.1.md) |
| Density / cognitive load | [cognitive-load-and-density-notes-v0.1.md](cognitive-load-and-density-notes-v0.1.md) |

**Default home:** Main Cockpit (hybrid tendency D).

---

## Spatial cockpit architecture (post–Prototype v0.1)

| Concern | Doc |
|---------|-----|
| Spatial zones + tri-focus | [cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md) |
| `info_area` / tactical signals | [tactical-signal-philosophy-v0.1.md](tactical-signal-philosophy-v0.1.md) |
| Viewport / no page scroll | [viewport-and-scroll-philosophy-v0.1.md](viewport-and-scroll-philosophy-v0.1.md) |
| Surfaces + motion + depth | [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md), [motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md), [depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md) |
| Priority + focus + empty | [information-priority-model-v0.1.md](information-priority-model-v0.1.md), [operational-focus-state-model-v0.1.md](operational-focus-state-model-v0.1.md), [loading-and-empty-state-philosophy-v0.1.md](loading-and-empty-state-philosophy-v0.1.md) |
| Visual direction (Phase 3) | [visual-language-direction-v0.1.md](visual-language-direction-v0.1.md) |

---

## SAFE UNKNOWN

- Wireframe fidelity per mode — Phase 2 in progress.
- Routing (MPA vs light SPA) — Phase 4.
- i18n — не в scope v0.1.

---

*Last updated: 2026-05-24 — Post–Prototype v0.1 spatial cockpit canon.*
