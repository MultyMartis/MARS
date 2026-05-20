# HomeGateway v4.ai — block-screen taxonomy v0.1

**Статус:** **DRAFT** · **PLANNING** · Phase 1

Таксономия типов **block-screen** — базовой визуальной единицы cockpit UI.

---

## Определение block-screen

**Block-screen** — основной визуальный UI-модуль HomeGateway.

Это HTML-модуль, который визуально ведёт себя как **high-tech полупрозрачный информационно-действенный экран**, вдохновлённый sci-fi cockpit interfaces: стекло, мягкое свечение, чёткая иерархия сигналов.

### Block-screen может показывать

| Категория контента | v0.1 | Future |
|--------------------|------|--------|
| info (текст, метрики) | sample | live |
| links | sample | admin-managed |
| status | sample | live |
| signals (badges, levels) | sample | computed + manual override |
| actions (buttons) | mock | wired quick actions |
| project data | sample | CRUD-backed |
| deadline data | sample | CRUD-backed |
| clipboard actions | mock | templates from admin |
| bot/system state | display-only sample | FUTURE-INTEGRATION |
| MARS state | display-only sample | FUTURE-INTEGRATION |
| lead/request data | sample | feed integration |
| forms / mini-controls | — | admin Phase 5+ |

### Block-screen — не

- MARS agent, n8n node, Telegram bot.
- Autonomous widget с side effects без human click.
- iframe с отдельным auth (v0.1).

---

## Размеры (draft — для wireframes)

| size_id | Название | Назначение |
|---------|----------|------------|
| `bs-s` | Compact | Один статус, 1–3 ссылки, мини-action |
| `bs-m` | Standard | Основной список, 4–8 строк |
| `bs-l` | Wide | Таблица дедлайнов, lead feed |
| `bs-xl` | Hero / focus | Project detail summary, MARS summary |

Точные grid spans — **SAFE UNKNOWN** (Phase 2).

---

## Типы по функции (taxonomy)

| type_id | Тип | Описание | Пример module_id |
|-------|-----|----------|------------------|
| `bs-type-link-hub` | Link hub | Группа ссылок с заголовком | `hg-frequent-links` |
| `bs-type-client-card` | Client card | Клиент + краткий статус | `hg-client-list` (card mode) |
| `bs-type-project-panel` | Project panel | Проект, ресурсы, deadlines | `hg-project-detail` |
| `bs-type-signal-list` | Signal list | Строки с level INFO…OVERDUE | `hg-deadline-active` |
| `bs-type-recurring` | Recurring monitor | Monthly / repeating tasks | `hg-deadline-recurring` |
| `bs-type-status-row` | Status row | Bot/system/MARS line item | `hg-bot-status`, `hg-mars-monitor` |
| `bs-type-lead-feed` | Lead feed | Заявки с сайтов | `hg-leads-*` |
| `bs-type-action-strip` | Action strip | Quick actions horizontal | `hg-quick-actions` |
| `bs-type-clipboard` | Clipboard | Copy prepared text | `hg-clipboard` |
| `bs-type-settings` | Settings | Theme, prefs | `hg-settings` |
| `bs-type-admin-gate` | Admin gate | Entry only | `hg-admin-entry` |

---

## Типы по интерактивности

| interactivity | Поведение v0.1 |
|---------------|----------------|
| **read-only** | MARS monitor, часть status |
| **navigate** | Links open URL / internal view |
| **action-mock** | Quick actions — `console` / alert stub |
| **clipboard** | `navigator.clipboard` or fallback mock |
| **expand** | Opens popup layer ([screen-map](screen-map-v0.1.md)) |

---

## Разметка (admin-aware, draft)

Рекомендуемые атрибуты для static MVP (имена могут уточняться Phase 4):

```html
<section class="hg-block-screen"
         data-hg-module="hg-deadline-active"
         data-hg-block-type="bs-type-signal-list"
         data-hg-block-size="bs-m"
         data-hg-entity-kind="deadline"
         data-hg-entity-id="sample-001">
  ...
</section>
```

**Принцип:** контент внутри повторяемых row/item шаблонов с `data-hg-item-id`, не уникальный HTML на каждую сущность.

---

## Визуальные правила (связь с theme)

- Фон: `var(--hg-surface-glass)` + blur.
- Сигналы: только semantic tokens — [theme-system-draft-v0.1.md](theme-system-draft-v0.1.md).
- OVERDUE и due-today **визуально различимы** (icon + label + color).

---

## Composition on Main Cockpit (hint)

Типичный hub mix (draft priority — см. [ux-discovery-notes-v0.1.md](ux-discovery-notes-v0.1.md)):

1. Signal-heavy blocks → signal rail или top of canvas.
2. Client/project → central canvas.
3. Link hubs → left rail or canvas grid.
4. MARS/bots/leads → canvas columns.
5. Quick actions → bottom strip.

Детали зон: [cockpit-layout-zones-v0.1.md](cockpit-layout-zones-v0.1.md).

---

## SAFE UNKNOWN

- Collapse/expand per block-screen — Phase 2.
- Drag-reorder modules — Phase 6 admin.
- Charts inside block-screen — FUTURE.

---

*Last updated: 2026-05-20.*
