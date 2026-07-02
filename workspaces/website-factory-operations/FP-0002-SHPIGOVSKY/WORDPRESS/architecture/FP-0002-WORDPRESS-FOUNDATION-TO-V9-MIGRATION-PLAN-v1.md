# FP-0002 WordPress Foundation-to-V9 Migration Plan v1

**Task:** V9-06A | **Date:** 2026-07-03  
**Scope:** Planning only — no mutations

---

## 1. Migration principles

1. **Do not** change `post_type` in place on existing Pages → Services.
2. **Create-new-and-map** for service catalogue; retire old Page records after URL verification.
3. Preserve V9 slugs and public URLs.
4. Every destructive step requires backup, dry-run, operator approval (FW-07C charter).
5. Foundation placeholder copy replaced from V9 `dist/` in V9-08.

---

## 2. Foundation object classification

| Foundation object | Slug / route | Action | Notes |
|-------------------|--------------|--------|-------|
| Главная | `glavnaya` / `/` | KEEP_AS_SYSTEM_PAGE | `page_on_front` |
| Услуги | `uslugi` | KEEP_AS_PAGE | Hub — not CPT |
| Зависимости | `zavisimosti` | MIGRATE_TO_SERVICE | Create service; retire page |
| Психическое здоровье | `psihicheskoe-zdorovie` | MIGRATE_TO_SERVICE | |
| РПП | `rasstroystva-pischevogo-povedeniya` | MIGRATE_TO_SERVICE | |
| Генотипирование | `genotipirovanie` | RETIRE_AFTER_MIGRATION | Forbidden route |
| Специалисты | `specyalisty` | RETIRE_AFTER_MIGRATION | No V9 route |
| О центре | `o-centre` | KEEP_AS_PAGE | |
| O-centre children (5) | various | KEEP_AS_PAGE | Reparent if needed |
| Интервью и СМИ | `intervyu-i-smi` | RETIRE_AFTER_MIGRATION | |
| Отзывы | `otzyvy` | KEEP_AS_PAGE | |
| Статьи | `blog` | KEEP_AS_SYSTEM_PAGE | `page_for_posts` |
| Контакты | `kontakty` | KEEP_AS_PAGE | |
| Правовая информация | `pravovaya-informaciya-pilzovatelyu` | RETIRE_AFTER_MIGRATION | |
| Legal ×4 | privacy, etc. | KEEP_AS_PAGE | REASSIGN_TEMPLATE legal |
| Missing service leaves (14) | — | CREATE in service CPT | Per route map |
| Missing fixture post | `nazvanie-stati` | CREATE | Post type |
| Alcohol dependence | — | CREATE | New service, special layout |

---

## 3. Action counts

| Action | Count |
|--------|------:|
| KEEP_AS_PAGE | 12 |
| KEEP_AS_SYSTEM_PAGE | 2 |
| MIGRATE_TO_SERVICE | 3 |
| CREATE (service) | 12 |
| CREATE (post) | 1 |
| REASSIGN_TEMPLATE | 17 |
| REPARENT | 0–2 |
| RETIRE_AFTER_MIGRATION | 4 |
| MANUAL_REVIEW | 2 |

---

## 4. Page → Service migration procedure (V9-06D)

For each subdivision Page (`zavisimosti`, `psihicheskoe-zdorovie`, `rasstroystva-pischevogo-povedeniya`):

1. Export Page ID, slug, title, parent, menu refs.
2. Create `service` post with identical slug segment and title.
3. Map menu items to new service permalink.
4. Verify `/uslugi/{slug}/` resolves to CPT.
5. Set Page to draft → trash only after redirect/404 check and backup.
6. **Do not** reuse Page ID.

For new leaf services: create directly as `service` with correct `post_parent`.

---

## 5. Menu reconciliation

| Menu | Action |
|------|--------|
| Primary | Remove specyalisty; add missing service links per V9 |
| Footer | Split into footer_services + footer_o_centre |
| Legal | Remove pravovaya hub; keep 4 discrete legal pages |

---

## 6. Template assignment migration

| Object | Template |
|--------|----------|
| glavnaya | front-page |
| uslugi | services-hub |
| o-centre* | institutional |
| otzyvy | reviews |
| kontakty | contacts |
| legal* | legal |
| blog | (posts page — home.php) |
| services | single-service + layout meta |

---

## 7. Rollback path

- Pre-migration WPilot snapshot (`foundation-002` or V9-06D baseline).
- Object ID map JSON stored in `delivery/fixtures/`.
- Retired Pages remain in trash 30 days before permanent delete.

---

## 8. Redirect behavior

| From | To | Type |
|------|-----|------|
| `/specyalisty/` | MANUAL_REVIEW | 301 or retire |
| `/uslugi/genotipirovanie/` | 410 or remove | RETIRE |
| Old Page service URLs (if any drift) | New service URL | 301 |

---

*No migration executed in V9-06A.*
