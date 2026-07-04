# FP-0002 V9-06D7E Contacts Template Inventory v1

**Date:** 2026-07-05  
**Task:** V9-06D7-E Contacts Template Source

## V9 source files

| File | Role |
|------|------|
| `src/pages/kontakty.html` | Page orchestration |
| `src/partials/sections/contacts-map-body.html` | Hero, intro, phone, messengers, two location cards |
| `src/partials/sections/contacts-rehabilitation-steps.html` | Steps, CTA band, support list, photo |

## Section order

1. Breadcrumbs (`contacts-page__breadcrumbs`)
2. `contacts-map-body` → WP `template-parts/contacts/map-body.php`
3. `contacts-rehabilitation-steps` → WP `template-parts/contacts/rehabilitation-steps.php`

## Contact info structure

- H1 + intro paragraph
- Phone row with messenger icon links (Telegram, WhatsApp, Max)
- Two `contacts-location` articles with address, hours, email, static map PNG each

## Form / final-form

V9 Contacts page does **not** include `final-form`; CTA uses `program-cta-band` opening consultation modal only.

## Deferred

- Map PNG assets (`contacts-map-mo-region.png`, `contacts-map-moscow.png`)
- Rehabilitation interior photo
- Live form endpoint
- Derived breadcrumb trail

**Result:** PASS
