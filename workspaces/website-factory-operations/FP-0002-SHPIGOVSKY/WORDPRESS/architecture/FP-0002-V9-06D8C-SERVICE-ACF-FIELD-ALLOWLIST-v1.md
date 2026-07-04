# FP-0002 V9-06D8C Service ACF Field Allowlist v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d8c-services-mvp-content-seed/service-acf-field-allowlist.json`

---

## Authorized objects

| Service ID | Route | Layout |
|---:|---|---|
| 73 | `/uslugi/zavisimosti/` | subdivision |
| 74 | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | alcohol_special |
| 77 | `/uslugi/psihicheskoe-zdorovie/` | subdivision |
| 84 | `/uslugi/rasstroystva-pischevogo-povedeniya/` | subdivision |

---

## Authorized fields (exact)

From `seed-wave-design.json` wave D8-C + ACF JSON confirmation:

- `hero_lead`
- `intro_text`
- `intro_note`
- `signs_items`
- `programme_items`
- `stages`
- `faq_items`
- `cta_title`
- `cta_text`
- `cta_button_label`

---

## Forbidden writes

- `service_layout_variant` (especially service 74)
- `hero_media`, `hero_eyebrow`, `hero_title_override`, `hero_cta_label`, `hero_cta_target`
- `manual_related_services`
- `post_title`, `post_content`
- All non-target services, pages, options, menus, redirects

---

## Write summary

| Service | Writable ops | Skipped |
|---:|---:|---:|
| 73 | 3 | 7 |
| 74 | 6 | 4 |
| 77 | 3 | 7 |
| 84 | 3 | 7 |

**Total field updates applied:** 15

---

## Result

**PASS**
