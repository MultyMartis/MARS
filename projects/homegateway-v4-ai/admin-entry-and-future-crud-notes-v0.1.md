# HomeGateway v4.ai — admin entry and future CRUD notes v0.1

**Статус:** **DRAFT** · **PLANNING** · **FUTURE-INTEGRATION** (CRUD after static MVP)

Дополнение к [admin-layer-plan-v0.1.md](admin-layer-plan-v0.1.md): точка входа admin, admin-aware static frontend, будущие сущности CRUD.

---

## Правило Phase 1

1. **Admin required** after first static frontend — реализация Phase 5–6.
2. **Admin-aware from day one** — static HTML структурирован так, будто данные придут из admin-managed entities.
3. **Visible admin entry** on main cockpit shell — **обязательно** в static MVP v0.1 (stub only).

---

## Admin entry (static MVP)

| Requirement | Implementation hint |
|-------------|---------------------|
| Always visible | `zone-top-command` or `zone-nav-left` footer |
| Clear label | «Admin», «Управление», icon + text |
| Target | Stub page: «Admin area — Phase 5» |
| Same auth boundary | Login mock → cockpit → admin stub (no separate auth v0.1) |
| module_id | `hg-admin-entry` |

**Не делать:** скрытый URL без UI; disabled без explanation.

---

## Future admin CRUD entities

| entity_id | Operations | Maps to cockpit |
|-----------|------------|-----------------|
| `ent-client` | add / edit / delete | Client list, project grouping |
| `ent-project` | add / edit / delete | Project blocks, detail view |
| `ent-project-link` | add / edit / delete | Related resources, staging, Figma |
| `ent-frequent-link` | add / edit / delete | Link hub block-screens |
| `ent-deadline` | add / edit / delete | Active deadline monitor |
| `ent-recurring-task` | add / edit / delete | Recurring monitor |
| `ent-quick-action` | add / edit / delete | Bottom strip / action blocks |
| `ent-clipboard-item` | add / edit / delete | Clipboard blocks (**no secrets**) |
| `ent-cockpit-module` | enable / reorder / configure | Which blocks appear on hub |
| `ent-bot-system` | add / edit / delete | Bot/system registry for status blocks |
| `ent-lead-source` | add / edit / delete | Polygon, MetaCODE, future sites |
| `ent-theme-settings` | edit where appropriate | Defaults within token system |

---

## Admin-aware static frontend checklist

При Phase 4 static build **каждая** сущность в sample data должна:

| Check | Example |
|-------|---------|
| Repeatable row template | `<li data-hg-entity-kind="client" data-hg-entity-id="…">` |
| Separable sample JSON | `samples/clients.json` inline or `<script type="application/json">` |
| No unique snowflake markup per client | Same structure, different text |
| Links as data fields | `href` from data, not hardcoded in CSS |
| Deadlines carry signal level | `data-hg-signal-level="WARNING"` |
| Modules declare `data-hg-module` | Matches [module-registry-draft-v0.1.md](module-registry-draft-v0.1.md) |

### Anti-patterns (reject in review)

- Клиент «Иванов» только в `<h3>` без entity id.
- Дедлайны в prose paragraph без list structure.
- MARS status как screenshot image only (no structured row for future API).
- Admin entry only in HTML comment.

---

## Data flow (future)

```text
Admin CRUD (Phase 6+)
        │
        ▼
  Storage (JSON / local DB / API — SAFE UNKNOWN)
        │
        ▼
  Cockpit render (replace sample injection)
        │
        ▼
  Block-screens (unchanged shell taxonomy)
```

Static MVP останавливается на **sample injection** слое.

---

## Lead sources (admin future)

| source_id | Site / system |
|-----------|---------------|
| `lead-polygon` | Web Studio Polygon |
| `lead-metacode` | MetaCODE websites |

Admin: URL feed config, display label, enable/disable — **FUTURE-INTEGRATION** for live feed.

---

## Relation to admin-layer-plan

- UX structure: этот документ + [admin-layer-plan-v0.1.md](admin-layer-plan-v0.1.md).
- Wireframes admin IA: Phase 5.
- Implementation: Phase 6 after static validation.

---

## SAFE UNKNOWN

- Git-backed JSON vs DB — human charter Phase 6.
- Whether admin lives at `/admin` or subdomain — TBD.
- Validation rules for URLs and quick action safety classes — Phase 5 spec.

---

*Last updated: 2026-05-20.*
