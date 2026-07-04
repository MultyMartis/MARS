# FP-0002 V9-06D8-E — Contacts ACF Field Allowlist v1

**Page:** #20 `/kontakty/`  
**Field group:** `group_fp02_page_contacts`  
**Phase:** V9-06D8-E

## Authorized writes (3)

| Field | Key | Type | Source | Classification |
|-------|-----|------|--------|----------------|
| `contacts_form_intro` | `field_fp02_contacts_form_intro` | textarea | V9 `contacts-map-body.html` intro | STATIC_V9_CONTENT |
| `contacts_address` | `field_fp02_contacts_address` | textarea | V9 location 2 address | STATIC_V9_CONTENT |
| `contacts_blocks` | `field_fp02_contacts_blocks` | repeater | V9 two location articles | STATIC_V9_CONTENT |

## Skipped (3)

| Field | Reason |
|-------|--------|
| `contacts_map_url` | OPERATOR_SUPPLIED_REQUIRED — D8-A `map_link` empty |
| `contacts_phones` | Canonical in D8-A Site Options (`phone_primary`) |
| `contacts_messengers` | OPERATOR_SUPPLIED_REQUIRED — V9 `#` placeholders; D8-A `social_links` empty |

## Forbidden

- Native `post_title` / `post_content`
- Home, Services Hub, Service CPT, site options
- Menus, redirects, rewrite flush, media uploads

Evidence: `validation/v9-06d8e-contacts-content-seed/contacts-acf-field-allowlist.json`
