# FP-0002 V9-06D.3 Minimal Visual Content Seed Plan v1

**Proposed next phase:** V9-06D.4 MINIMAL CONTENT SEED FOR VISUAL ROUTE QA
**This phase (D.3) does not execute the seed.**

## Objects in first writable wave

### Pages

- ID 4 `/` fields: ['home_hero_slides[0].title', 'home_hero_slides[0].text', 'home_service_nav_items[0..2].title', 'home_cta_title', 'home_cta_text']
- ID 5 `/uslugi/` fields: ['services_hub_intro', 'services_hub_query_mode', 'services_hub_show_placeholders']
- ID 20 `/kontakty/` fields: ['contacts_address', 'contacts_phones[0].label', 'contacts_phones[0].phone', 'contacts_form_intro']

### Services

- ID 73 `SVC-ZAVISIMOSTI` fields: ['service_layout_variant', 'hero_lead']
- ID 74 `SVC-ALKOGOL` fields: ['service_layout_variant', 'hero_lead', 'intro_text', 'signs_items[0].title', 'signs_items[0].text']
- ID 77 `SVC-PSYCH` fields: ['service_layout_variant', 'hero_lead']
- ID 84 `SVC-RPP` fields: ['service_layout_variant', 'hero_lead']

### Explicitly excluded from D.4

- Legal pages production copy
- Blog fixture article full body (optional minimal title-only later)
- Options Page values (unless operator authorizes a separate micro-gate)
- Menus, redirects, rewrite flush
- V9 HTML/CSS/JS integration
- Deletion of `/specyalisty/` or PAGE_TO_SERVICE_SOURCE pages

## Content source per field

- Extract short text from V9 `src/` for the mapped route only.
- Prefer non-legal, non-demo strings.
- Media optional in D.4; text-only seed is acceptable for visual route QA.

## Validation URL list

- http://shpigovsky.test/
- http://shpigovsky.test/uslugi/
- http://shpigovsky.test/uslugi/zavisimosti/
- http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/
- http://shpigovsky.test/uslugi/psihicheskoe-zdorovie/
- http://shpigovsky.test/uslugi/rasstroystva-pischevogo-povedeniya/
- http://shpigovsky.test/kontakty/

## Visual QA checklist

- [ ] HTTP 200 on each URL (or documented rewrite limitation)
- [ ] Correct template family renders without fatal error
- [ ] Hero/intro text visible where seeded
- [ ] Placeholder services still show placeholder state
- [ ] No menu drift
- [ ] No legal DEMO promoted as production

## Rollback strategy

1. Create DB dump checkpoint before D.4 writes.
2. Record exact object IDs and field keys written.
3. On failure: restore dump; re-validate object counts and empty ACF content state.

## Stop conditions

- Any unauthorized menu/redirect/rewrite change
- ACF Extended PRO field usage required
- Object count drift from 15 Services
- Attempt to delete legacy `/specyalisty/`

## Result

READY FOR OPERATOR REVIEW — not authorized to execute.
