# FP-0002 V9-06D8 ACF / Options Field Inventory v1

**Date:** 2026-07-05  
**Task:** V9-06D8 Content Seed Planning  
**Evidence:** `validation/v9-06d8-content-seed-planning/acf-options-field-inventory.json`

---

## Summary

| Area | Groups | Fields | Required for MVP | Optional | Deferred | Admin UX concerns |
|---|---:|---:|---:|---:|---:|---:|
| Home | 1 | 10 | 4 | 4 | 2 | 4 |
| Services Hub | 1 | 4 | 0 | 1 | 0 | 1 |
| Services | 4 | 18 | 6 | 8 | 4 | 6 |
| Contacts | 1 | 6 | 3 | 3 | 0 | 2 |
| Site Options | 2 | 16 | 8 | 5 | 1 | 3 |
| Header/Footer/Global | 0 | 0 | 0 | 0 | 0 | 0 |

Header/footer/global chrome reads **Site Options** only (`shpigovsky_get_site_option()` in `inc/site-chrome.php`).

---

## Home (page ID 4, `group_fp02_page_home`)

| Field | Type | Seeded D4 | MVP wave | Source candidate | Olga UX |
|---|---|---:|---|---|---|
| `home_hero_slides` | repeater | partial | D8-B | V9 `index.html` hero | NEEDS_LABEL_HELP_TEXT |
| `home_service_nav_items` | repeater | yes | — | service parent titles | OK |
| `home_advantages` | repeater | no | D8-B | V9 `home-why-us` | NEEDS_LABEL_HELP_TEXT |
| `home_intro_bands` | repeater | no | D8-B | V9 treatment-prevention | NEEDS_FIELD_GROUP_REORDER |
| `home_gallery_media` | repeater | no | D8-B | V9 gallery + **media** | NEEDS_MEDIA |
| `home_faq_items` | repeater | no | D8-B | V9 home FAQ | OK |
| `home_cta_title` / `home_cta_text` | text | yes | — | V9 final-form | OK |
| `home_reviews_teaser` | repeater | no | DEFER | — | TOO_COMPLEX |
| `home_blog_teaser_enabled` | bool | no | DEFER | — | DEVELOPER_ONLY |

---

## Services Hub (page ID 5, `group_fp02_page_services_hub`)

| Field | Seeded | Wave | Notes |
|---|---:|---|---|
| `services_hub_intro` | yes | D8-D polish | Olga-editable intro |
| `services_hub_query_mode` | yes | — | **Developer-only** — do not change in seed |
| `services_hub_show_placeholders` | yes | — | **Developer-only** |
| `services_hub_faq_items` | no | D8-D | V9 `uslugi-v2.html` FAQ |

No ACF fields exist for genotyping hub, category galleries, hero image, founder/comfort — **DEFER** (shared static blocks).

---

## Services (IDs 73, 74, 77, 84)

### Layout & hero (`group_fp02_service_layout_hero`)

- `service_layout_variant` — **seeded**; required; **developer-controlled** (do not change 74 variant).
- `hero_lead` — seeded all four; Olga-editable.
- `hero_media` — **MEDIA_REQUIRED**; separate authorization.
- `hero_title_override`, `hero_cta_*` — optional D8-C.

### Structured sections (`group_fp02_service_structured_sections`)

- **Service 74 MVP:** `programme_items`, `stages`, `cta_*` — source V9 `usluga-konechnaya-v1.html`.
- **Service 74 seeded:** `intro_text`, `signs_items`.
- **73/77/84:** optional `intro_text`, `signs_items`, `programme_items` for richness.

### FAQ (`group_fp02_service_faq`)

- `faq_items` — **MVP for 74**; optional for others.

### Relationships (`group_fp02_service_relationships`)

- `manual_related_services` — **DEFER** (sibling query fallback works).

---

## Contacts (page ID 20, `group_fp02_page_contacts`)

| Field | Seeded | Wave | Source |
|---|---:|---|---|
| `contacts_address` | yes | D8-E sync | V9 + site options |
| `contacts_phones` | yes | D8-E | prefer **site options** as canonical |
| `contacts_form_intro` | yes | — | V9 kontakty |
| `contacts_messengers` | no | D8-E | site `social_links` or page repeater |
| `contacts_map_url` | no | D8-E | **operator map URL** |
| `contacts_blocks` | no | D8-E | V9 location blocks |

---

## Site Options (`fp02-site-settings`)

**Never seeded in D4.** All values empty at D7-F.

### Contacts group (`group_fp02_site_options_contacts`)

MVP D8-A: `organisation_name`, `phone_primary`, `site_email`, `site_address`, `opening_hours`, `map_link`, `social_links`.

### Modal/CTA group (`group_fp02_site_options_modal_cta`)

MVP D8-A: `default_button_label`, `global_cta_title`, `global_cta_text`; SHOULD: callback title/text.

---

## Result

**COMPLETE** — machine inventory in JSON; shared V9 blocks without ACF documented as DO_NOT_SEED.
