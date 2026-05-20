# HomeGateway v4.ai — multi-view cockpit system v0.1

**Статус:** **DRAFT** · **PLANNING** · Phase 2  
**Назначение:** каноническая модель HG v4.ai как **связанной multi-view operational cockpit environment**, а не одной dashboard-страницы.

**Не является:** routing implementation, wireframes, frontend code, runtime product.

**Связанные документы:** [operational-modes-v0.1.md](operational-modes-v0.1.md) · [navigation-hierarchy-v0.1.md](navigation-hierarchy-v0.1.md) · [layout-variants-analysis-v0.1.md](layout-variants-analysis-v0.1.md) · [cockpit-os-concept-notes-v0.1.md](cockpit-os-concept-notes-v0.1.md)

---

## Каноническое утверждение (Phase 2)

> **HomeGateway v4.ai — это не одна dashboard-страница.**  
> Это **connected cockpit environment** с несколькими **operational views**, каждый из которых оптимизирован под разные операционные состояния оператора.

Предыдущие layout variants A/B/C/D **не** конкурирующие финальные дизайны — они описывают **operational cockpit mode tendencies** (см. [layout-variants-analysis-v0.1.md](layout-variants-analysis-v0.1.md)).

---

## Почему multi-view необходим

| Проблема single-page dashboard | Как multi-view cockpit отвечает |
|--------------------------------|----------------------------------|
| Один плотностной режим для всех задач | Разные режимы: обзор, мониторинг, фокус, тактика |
| Конкуренция блоков за внимание | Каждый view выделяет релевантный signal set |
| Утренний glance = вечерний deep work | Отдельные views под scan vs concentration |
| Статус систем и работа с клиентом смешаны | Systems Monitor vs Project View |
| Admin/settings загрязняют операционный поток | Admin Mode и Settings — отдельные контексты |

Оператор веб-студии переключается между **состояниями работы** (обзор дня, срочные сигналы, глубокая работа по проекту, проверка automation). Одна страница с равноправными карточками не отражает эту динамику и ведёт к **dashboard overload** и **signal fatigue**.

---

## Что такое operational view

**Operational view** — устойчивый режим кокпита с согласованным набором:

- плотности информации;
- signal intensity;
- navigation behavior;
- layout tendency (A/B/C/D как ориентир, не жёсткая сетка);
- dominant block-screen groups.

View **не** обязан быть отдельным URL на Phase 2 — может быть mode switch внутри shell, full-page route или hybrid. Решение wireframe/routing — Phase 2–4 ([screen-map-v0.1.md](screen-map-v0.1.md)).

---

## Inventory operational views (draft)

| view_id | Название | Роль | Детали |
|---------|----------|------|--------|
| `view-main-cockpit` | **Main Cockpit** | Default home / hybrid overview | [operational-modes-v0.1.md](operational-modes-v0.1.md) § A |
| `view-systems-monitor` | **Systems Monitor** | Bots, MARS, workflows, uptime | § B |
| `view-focus-workspace` | **Focus Workspace** | Active project/task, low noise | § C |
| `view-tactical-signals` | **Tactical Signals** | Deadlines, urgency, recurring | § D |
| `view-project` | **Project View** | Client/project-centric screen | § E |
| `view-quick-actions` | **Quick Actions Mode** | Fast launch, clipboard, utilities | § F |
| `view-admin` | **Admin Mode** | Future CRUD (FUTURE) | § G |
| `view-settings` | **Settings / Personalization** | Theme, layout prefs, behavior | § H |

Дополнительные specialized screens из Phase 1 (Leads, MARS-only page) **встраиваются** в views или deep panels — не дублировать как отдельную парадигму без причины.

---

## Как operational context меняет интерфейс

```text
Operational state          →  Preferred view        →  Density   →  Signal role
─────────────────────────────────────────────────────────────────────────────
Morning scan               →  Main / Tactical       →  medium    →  deadlines, leads
Client deep work           →  Focus / Project       →  low–med   →  project links
Infrastructure check       →  Systems Monitor       →  high      →  status grids
End-of-month recurring     →  Tactical Signals      →  med–high  →  recurring, reports
One-click routine          →  Quick Actions         →  low       →  actions only
Data maintenance (future)  →  Admin                 →  med       →  forms/tables
Comfort / prefs            →  Settings              →  low       →  theme, density
```

**Принцип:** интерфейс **следует за задачей**, а не зафиксирован в одном «универсальном» layout.

---

## Связность cockpit environment

Multi-view не означает изолированные приложения. Связность обеспечивается:

| Механизм | Описание |
|----------|----------|
| **Shared shell** | Top command bar, persistent mode access, theme, admin entry ([cockpit-layout-zones-v0.1.md](cockpit-layout-zones-v0.1.md)) |
| **Shared signal vocabulary** | [signal-system-draft-v0.1.md](signal-system-draft-v0.1.md) |
| **Cross-view deep links** | Project из Tactical → Project View; MARS hint → Systems Monitor |
| **Overlay layer** | Detail без полной смены view ([navigation-hierarchy-v0.1.md](navigation-hierarchy-v0.1.md) Layer 3) |
| **Consistent block-screen language** | [block-screen-taxonomy-v0.1.md](block-screen-taxonomy-v0.1.md) |

---

## Relationship к screen map (Phase 1 → 2)

| Phase 1 `screen_id` | Phase 2 mapping |
|---------------------|-----------------|
| `scr-cockpit-main` | Anchor для `view-main-cockpit`; не единственный «дом» |
| `scr-mars-monitor`, `scr-bots-systems` | Primary content `view-systems-monitor` |
| `scr-signals-deadlines` | Primary / shared с `view-tactical-signals` |
| `scr-clients-projects`, `scr-project-detail` | `view-project` + overlays |
| `scr-quick-actions` | `view-quick-actions` или bottom strip во всех views |
| `scr-settings` | `view-settings` |
| `scr-admin-area` | `view-admin` (FUTURE) |

---

## Default / home view (draft decision)

**Предлагаемый default:** `view-main-cockpit` (Hybrid Operational Cockpit, layout tendency **D**).

Обоснование: баланс обзора клиентов, сигналов и quick access без экстремальной плотности Systems Monitor или минимализма Focus Workspace. Оператор может переключиться за один шаг (Layer 2 navigation).

**SAFE UNKNOWN:** подтверждение на wireframes; возможен «last used view» preference в Settings.

---

## Phase 2 boundaries

| In scope (this doc set) | Out of scope |
|-------------------------|--------------|
| View inventory, purposes, relationships | HTML/CSS implementation |
| Mode ↔ layout tendency mapping | Figma production assets |
| Navigation philosophy | APIs, backend, MARS runtime |
| Cognitive / density targets | Autonomous view switching |

---

## SAFE UNKNOWN

- MPA vs SPA vs single HTML with mode classes — Phase 4.
- Сколько views обязательны в static MVP Phase 4 (минимум: Main + 1 specialized demo).
- Анимации переходов между views — visual direction Phase 3.
- Сохранение «last view» в localStorage — Phase 6+.

---

*Last updated: 2026-05-20 — Phase 2 multi-view foundation.*
