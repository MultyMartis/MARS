# FP-0002 V9-06E29B-FIX2C ACF Group Contract

## Hub — `group_fp02_page_ocentre_hub`

- Title: Page — O-Centre Hub
- Location: `post_type == page` AND `page == 11`
- Fields: hero + all `about_*` hub blocks + infrastructure + admin guidance messages
- Must NOT include: `institutional_content_sections`, `institutional_stages`

## Child — `group_fp02_page_institutional_child`

- Title: Page — Institutional Child
- Location: `page_template == page-templates/institutional.php` AND page in {12,13,14,15,16}
- Fields: placeholder notice + content sections + stages

## Retired

- `group_fp02_page_institutional` — must not attach to page #11
