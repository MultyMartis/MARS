# FP-0002 V9-06E2 Main Menu Alignment

**Date:** 2026-07-06  
**Evidence:** `validation/v9-06e2-legal-layout-menu-alignment-repair/main-menu-alignment-result.json`

Static V9 authority: `fp-0002-shpigovsky-v9/src/partials/layout/header.html`

| Static V9 item | WP result | Status |
|----------------|-----------|--------|
| Лечение и профилактика /uslugi/ | Menu item #27 relabeled; page #5 | PASS |
| Зависимости /uslugi/zavisimosti/ | New menu item → page #6 | PASS |
| О центре /o-centre/ | Menu item #29 | PASS |
| Отзывы /otzyvy/ | Menu item #30 | PASS |
| Статьи /blog/ | Menu item #31 | PASS |
| Контакты /kontakty/ | Menu item #32 | PASS |

Removed: Home (#26), Специалисты (#28). Mobile offcanvas uses same `primary` location — aligned automatically.

Deferred: mega-menu / submenu parity (not in static V9 top-level nav).
