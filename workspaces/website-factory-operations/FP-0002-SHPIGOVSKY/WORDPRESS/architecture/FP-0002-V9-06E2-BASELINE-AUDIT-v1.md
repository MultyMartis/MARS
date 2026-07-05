# FP-0002 V9-06E2 Baseline Audit

**Date:** 2026-07-06  
**Evidence:** `validation/v9-06e2-legal-layout-menu-alignment-repair/baseline-audit.json`

## Legal width restrictions

| Rule | Source | Present before repair |
|------|--------|----------------------|
| `.legal-document__container { max-width: 900px; }` | `theme/shpigovsky/assets/css/v9-style.css` | YES |
| `.legal-document__body { max-width: 820px; }` | same | YES |

`.plain-page-content__body { max-width: 820px; }` retained — not used on legal document template.

## Page #21 legal hub

| Field | Value |
|-------|-------|
| ID | 21 |
| Slug | `/pravovaya-informaciya-pilzovatelyu/` |
| Status before | publish |
| Legal menu item | #36 (first item in Legal menu) |

## Footer legal links (before)

1. Правовая информация → #21 hub  
2. Политика конфиденциальности → #3  
3. Пользовательское соглашение → #22  
4. Согласие на обработку ПД → #23  
5. Политика Cookie-файлов → #24  

## Primary menu (before vs static V9)

| Static V9 | WP before |
|-----------|-----------|
| Лечение и профилактика /uslugi/ | Главная / |
| Зависимости /uslugi/zavisimosti/ | Услуги /uslugi/ |
| О центре /o-centre/ | Специалисты /specyalisty/ |
| Отзывы /otzyvy/ | О центре /o-centre/ |
| Статьи /blog/ | Отзывы /otzyvy/ |
| Контакты /kontakty/ | Статьи /blog/ |
| — | Контакты /kontakty/ |

Mismatch: extra Home + Специалисты; missing Зависимости; wrong labels/order.
