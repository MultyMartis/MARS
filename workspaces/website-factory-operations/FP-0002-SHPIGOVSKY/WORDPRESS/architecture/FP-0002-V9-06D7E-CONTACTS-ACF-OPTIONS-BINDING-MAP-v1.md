# FP-0002 V9-06D7E Contacts ACF Options Binding Map v1

**Date:** 2026-07-05  
**Task:** V9-06D7-E Contacts Template Source

## Page ACF (`group_fp02_page_contacts`)

| Field | Section usage |
|-------|---------------|
| `contacts_form_intro` | Intro paragraph (fallback: V9 static copy) |
| `contacts_phones` | Primary phone row |
| `contacts_messengers` | Messenger icons (fallback: `social_links` option) |
| `contacts_blocks` | Location cards when populated (simplified render) |
| `contacts_address` | Secondary location address when blocks empty |
| `contacts_map_url` | Allowlisted map iframe when present |

## Site options (`group_fp02_site_options_contacts`)

| Field | Section usage |
|-------|---------------|
| `phone_primary` | Phone fallback |
| `site_email` | Location email rows |
| `site_address` | Primary location address fallback |
| `opening_hours` | Hours lines fallback |
| `map_link` | Map embed fallback |
| `social_links` | Messenger fallback |
| `default_button_label` | CTA button label |

## Guard behavior

- All reads guarded with `function_exists('get_field')`
- Empty optional blocks omitted
- No raw field keys rendered
- No write functions

**Result:** PASS
