# FP-0002 V9 — Client-Facing Action Inventory v1

**Phase:** V9-02  
**Routes audited:** 31  
**Total actions audited:** ~180 (header/footer/global + per-page CTAs)

## Global navigation (all pages)

| Source | Label | Type | Before | Decision | Final target | Status |
|--------|-------|------|--------|----------|--------------|--------|
| header | Logo | link | `/` | INTERNAL_EXISTING_ROUTE | `/` | OK |
| header | Услуги | link | `/uslugi/` | INTERNAL_EXISTING_ROUTE | `/uslugi/` | OK |
| header | О центре | link | `/o-centre/` | INTERNAL_EXISTING_ROUTE | `/o-centre/` | OK |
| header | Отзывы | link | `/otzyvy/` | INTERNAL_EXISTING_ROUTE | `/otzyvy/` | OK |
| header | Блог | link | `/blog/` | INTERNAL_EXISTING_ROUTE | `/blog/` | OK |
| header | Контакты | link | `/kontakty/` | INTERNAL_EXISTING_ROUTE | `/kontakty/` | OK |
| header | Telegram/WhatsApp | link | `#` | SOCIAL_PLACEHOLDER_ALLOWED | `#` | allowlisted |
| footer | Legal links (4) | link | legal routes | INTERNAL_EXISTING_ROUTE | `/privacy-policy/` etc. | OK |
| footer | Service links | link | service routes | INTERNAL_EXISTING_ROUTE | manifest routes | OK |
| footer | Social | link | `#` | SOCIAL_PLACEHOLDER_ALLOWED | `#` | allowlisted |

## Home (`/`)

| Label | Type | Final target | Status |
|-------|------|--------------|--------|
| все статьи | link | `/blog/` | FIXED V9-02 |
| Blog card ×3 | link | `/blog/nazvanie-stati/` | FIXED V9-02 |
| Все отзывы | link | `/otzyvy/` | FIXED V9-02 |
| Читать весь отзыв | span | non-navigation | FIXED V9-02 |
| Service accordion items | link | manifest service routes | OK |
| подробнее о доме | link | `/o-centre/galereya-o-dome/` | FIXED V9-02 |
| подробнее (program) | link | `/o-centre/programma-lecheniya/` | FIXED V9-02 |
| все специалисты | link | `/o-centre/` | FIXED V9-02 |
| Form consent | link | `/privacy-policy/`, `/consent-personal-data/` | OK |

## Blog (`/blog/`, `/blog/nazvanie-stati/`)

| Label | Final target | Status |
|-------|--------------|--------|
| Читать (cards) | `/blog/nazvanie-stati/` | OK |
| Pagination | span (prototype) | FIXED V9-02 |
| TOC anchors | `#section-id` | OK |

## Reviews (`/otzyvy/`)

| Label | Final target | Status |
|-------|--------------|--------|
| Все отзывы (from home) | `/otzyvy/` | FIXED V9-02 |
| Читать весь отзыв | span | FIXED V9-02 |
| Service tags | service routes | FIXED V9-02 |
| Pagination | span | FIXED V9-02 |

## Services

All hub/category/leaf links resolve per manifest. Genotyping absent.

## O-Centre

All six routes resolve; placeholders use standard copy.

## Legal pages

Cross-links between four legal routes verified.

## Summary

| Metric | Count |
|--------|-------|
| Broken links before | 12 |
| Broken links after | 0 |
| New placeholders | 0 |
| Non-allowlisted href="#" | 0 |
