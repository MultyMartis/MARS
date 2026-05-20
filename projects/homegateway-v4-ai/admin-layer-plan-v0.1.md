# HomeGateway v4.ai — admin layer plan v0.1

**Статус:** **DRAFT** · **PLANNING** · **FUTURE-INTEGRATION** (implementation after static MVP)

Admin-область **обязательна в roadmap**, но **не** входит в static MVP v0.1. Архитектура и фронтенд проектируются так, чтобы данные **не** оказались безвозвратно захардкожены.

**Phase 1 detail:** [admin-entry-and-future-crud-notes-v0.1.md](admin-entry-and-future-crud-notes-v0.1.md) (entry point, admin-aware checklist, entity map).

---

## Принцип

> Main cockpit must include an interface access point to admin area **from the beginning**.

v0.1: видимая точка входа (кнопка/ссылка) → stub page или «coming soon» — **без** CRUD.

---

## Почему admin после static frontend

| Причина | Detail |
|---------|--------|
| UX validation | Сначала плотность block-screen и навигация |
| Token + layout stability | Тема и shell до data model |
| Honest scope | Нет backend — нечему питать CRUD |

Phase 5 (design) → Phase 6 (data model) по [roadmap-v0.1.md](roadmap-v0.1.md).

---

## Сущности admin (planned CRUD)

| Entity | Operations | Notes |
|--------|------------|-------|
| Frequent links | add / edit / delete | URL, title, group, sort |
| Clients | add / edit / delete | Name, tags, primary contact ref |
| Projects | add / edit / delete | Client link, status, dates |
| Project resources | add / edit / delete | Repo, staging, Figma, docs |
| Deadline items | add / edit / delete | Date, level override, client/project |
| Recurring tasks | add / edit / delete | Cron-like monthly rules (human-defined) |
| Quick actions | add / edit / delete | Label, target, safety class |
| Clipboard items | add / edit / delete | **No secrets** — templates only |
| Cockpit modules | enable / reorder / configure | Visibility on main cockpit |
| Bot/system registry | add / edit / delete | Display metadata for status blocks |
| Lead source entries | add / edit / delete | Polygon, MetaCODE, future sites |
| Theme/settings | edit where appropriate | Overrides within token system |

---

## Admin UX (draft)

```text
/admin
  ├── dashboard (counts, recent edits)
  ├── entities/*  (CRUD lists + forms)
  └── settings (theme defaults, module defaults)
```

Auth для admin — **тот же** login boundary, что и cockpit (детали **SAFE UNKNOWN**).

---

## Anti-patterns (запретить с Phase 4)

- Клиенты только в HTML-комментариях без структуры.
- Ссылки только в SCSS `content:` — недоступны admin.
- Дедлайны только в JS constants без schema hint.
- Отдельный «скрытый» admin URL без entry с main cockpit.

---

## Static MVP requirements (admin-ready)

| Requirement | v0.1 |
|-------------|------|
| `hg-admin-entry` visible | ✓ |
| Sample data in JSON or `data-*` hooks | ✓ recommended |
| CRUD forms | ✗ |
| API | ✗ |

---

## Future technical options (SAFE UNKNOWN)

- Headless JSON files in repo (git-backed admin) — possible Phase 6 experiment.
- Local SQLite / browser IndexedDB — operator machine only.
- Small backend API — explicit human charter required.

**Не выбирать** в v0.1 без charter.

---

## SAFE UNKNOWN

- Role model (single operator vs delegate) — not needed v0.1.
- Audit log for admin edits — Phase 8 hardening.
- Import/export pack format — TBD.

---

*Last updated: 2026-05-20 — Phase 1 admin-entry cross-ref.*
