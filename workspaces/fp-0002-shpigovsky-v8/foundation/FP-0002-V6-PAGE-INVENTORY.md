# FP-0002 V6 Page Inventory

**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`  
**Upstream:** `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PAGE-INVENTORY-v1.md` + XLSX audit `reviews/services-page/FP-0002-SITE-STRUCTURE-XLSX-AUDIT-v1.md`  
**Updated:** 2026-06-23 (services foundation)

## Static implementation status

| Page | Parent | Future WordPress slug | Static source page | Menu presence | Status |
| ---- | ------ | --------------------- | ------------------ | ------------: | ------ |
| Главная | — | `/` | `src/pages/index.html` | Header (logo `/`) | **IMPLEMENTED** — operator canonical |
| Услуги — хаб | — | `/uslugi/` | `src/pages/uslugi.html` | Header «Лечение и профилактика» → `/uslugi/` | **FOUNDATION** — reused blocks only |
| Услуга — подраздел | Услуги | `/uslugi/{section}/` | — | Footer service columns | **NOT STARTED** |
| Услуга — конечная | Подраздел | `/uslugi/…/{leaf}/` | — | Footer / in-page | **NOT STARTED** |
| Генотипирование | Услуги (parallel) | `/uslugi/genotipirovanie/` | — | Header + footer | **NOT STARTED** |
| Специалисты | — | `/specyalisty/` | — | Header | **NOT STARTED** (no PDF) |
| О центре | — | `/o-centre/` | — | Header + footer | **NOT STARTED** — V8 charter complete 2026-06-29; see `audits/o-centre-page-charter/` |
| Отзывы | — | `/otzyvy/` | — | Header | **NOT STARTED** |
| Статьи — хаб | — | `/blog/` | — | Header | **NOT STARTED** |
| Статья | Статьи | `/blog/{slug}/` | — | — | **NOT STARTED** |
| Контакты | — | `/kontakty/` | — | Header | **NOT STARTED** |
| Правовая информация | — | `/pravovaya-informaciya-pilzovatelyu/` | — | Footer legal | **NOT STARTED** |
| Privacy / consent / etc. | Legal | `/privacy-policy/` etc. | — | Footer | **URL ONLY** in footer |
| 404 | — | system | — | — | **NOT STARTED** |

## Notes

- **Operator canonical law** applies to `src/` — inventory tracks implementation, does not override operator labels.
- Services hub foundation deliberately omits BLK-011 category grid and internal service hero until dedicated tasks.
