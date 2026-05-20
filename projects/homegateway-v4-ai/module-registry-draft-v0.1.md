# HomeGateway v4.ai — module registry draft v0.1

**Статус:** **DRAFT** · **PLANNING** · Phase 1

Черновой реестр модулей кокпита. **Не** runtime registry, **не** JSON schema engine.

**Связи:** [screen-map-v0.1.md](screen-map-v0.1.md) · [block-screen-taxonomy-v0.1.md](block-screen-taxonomy-v0.1.md) · [cockpit-layout-zones-v0.1.md](cockpit-layout-zones-v0.1.md)

---

## Легенда полей

| Поле | Значения |
|------|----------|
| **module_id** | Стабильный идентификатор |
| **group** | Группа из architecture blueprint |
| **screen_id** | Экран из screen-map (если применимо) |
| **block_type** | `bs-type-*` из block-screen taxonomy |
| **zone_hint** | Предпочтительная зона layout (draft) |
| **phase** | `v0.1-static` \| `admin` \| `integration` |
| **status** | `planned` \| `sample` \| `future` |

---

## Registry

| module_id | Название | group | screen_id | block_type | zone_hint | phase | status | Описание |
|-----------|----------|-------|-----------|------------|-----------|-------|--------|----------|
| `hg-client-list` | Список клиентов | client/project | `scr-clients-projects` | `bs-type-client-card` | canvas | v0.1-static | sample | Карточки клиентов; admin entity `ent-client` |
| `hg-project-detail` | Экран проекта | client/project | `scr-project-detail` | `bs-type-project-panel` | canvas / overlay | v0.1-static | sample | Проект: статус, ссылки; `ent-project` |
| `hg-frequent-links` | Частые ссылки | frequent links | `scr-cockpit-main` | `bs-type-link-hub` | canvas / nav | v0.1-static | sample | `ent-frequent-link` |
| `hg-resource-hub` | Ресурсы | frequent links | `scr-cockpit-main` | `bs-type-link-hub` | canvas | v0.1-static | sample | Docs, repos, tools |
| `hg-website-links` | Сайты | website/admin | `scr-project-detail` | `bs-type-link-hub` | canvas | v0.1-static | sample | Production/staging |
| `hg-admin-panels` | Админки | website/admin | `scr-project-detail` | `bs-type-link-hub` | canvas | v0.1-static | sample | WP, hosting |
| `hg-related-links` | Связанные проекты | related links | `scr-project-detail` | `bs-type-link-hub` | canvas | v0.1-static | sample | `ent-project-link` |
| `hg-mars-monitor` | MARS monitor | MARS | `scr-mars-monitor` | `bs-type-status-row` | canvas | v0.1-static | sample | **Display-only** |
| `hg-bot-status` | Bot / system status | bot/system | `scr-bots-systems` | `bs-type-status-row` | canvas | v0.1-static | sample | `ent-bot-system` future |
| `hg-deadline-active` | Active deadlines | deadlines | `scr-signals-deadlines` | `bs-type-signal-list` | signal-rail | v0.1-static | sample | `ent-deadline` |
| `hg-deadline-recurring` | Recurring tasks | deadlines | `scr-signals-deadlines` | `bs-type-recurring` | signal-rail | v0.1-static | sample | `ent-recurring-task` |
| `hg-quick-actions` | Quick actions | quick actions | `scr-quick-actions` | `bs-type-action-strip` | bottom-strip | v0.1-static | sample | `ent-quick-action` |
| `hg-clipboard` | Clipboard blocks | clipboard | `scr-cockpit-main` | `bs-type-clipboard` | bottom-strip | v0.1-static | sample | `ent-clipboard-item` |
| `hg-admin-entry` | Admin entry | admin | `scr-admin-entry` | `bs-type-admin-gate` | top-command | v0.1-static | sample | Stub → future admin |
| `hg-leads-polygon` | Leads: Polygon | leads | `scr-leads-requests` | `bs-type-lead-feed` | canvas | v0.1-static | sample | `ent-lead-source`; was `future` — sample in static MVP |
| `hg-leads-metacode` | Leads: MetaCODE | leads | `scr-leads-requests` | `bs-type-lead-feed` | canvas | v0.1-static | sample | MetaCODE requests sample |
| `hg-notes` | Notes / plans | notes | — | — | canvas | future | planned | Опционально |
| `hg-settings` | Settings | settings | `scr-settings` | `bs-type-settings` | top / settings | v0.1-static | sample | Theme switch |
| `hg-popup-host` | Popup layer | shell | `scr-popup-overlay` | — | overlay | v0.1-static | sample | Modal host |

---

## Зависимости между модулями (логические)

```text
hg-settings ──► theme tokens (global)
hg-admin-entry ──► admin area (Phase 5+, stub v0.1)
hg-mars-monitor ──► MARS export (Phase 7, FUTURE-INTEGRATION)
hg-bot-status ──► n8n / Telegram (Phase 7)
hg-deadline-* ──► signal levels (signal-system-draft)
hg-leads-* ──► external feeds (SAFE UNKNOWN)
```

---

## Правила расширения

1. Новый module_id — append row; **не** переиспользовать id для другой семантики.
2. Display-only модули **не** получают кнопок «Run agent» / «Execute workflow» без human charter.
3. Любой модуль с live data — пометка **FUTURE-INTEGRATION** до Phase 6–7.

---

## Приоритет на hub (draft — из UX discovery)

| Priority | Modules |
|----------|---------|
| P0 | `hg-deadline-active`, `hg-deadline-recurring`, `hg-client-list`, `hg-frequent-links` |
| P1 | `hg-mars-monitor`, `hg-bot-status`, `hg-leads-*`, `hg-quick-actions` |
| P2 | `hg-clipboard`, `hg-notes` |

Финальный порядок — Phase 2 wireframes.

---

## SAFE UNKNOWN

- Collapse/expand persistence — Phase 6.
- `ent-cockpit-module` reorder UI — Phase 6 admin.

---

*Last updated: 2026-05-20 — Phase 1 screen/zone mapping.*
