# FP-0002 V9-06D9L ACF Admin Visibility Repair v1

**Date:** 2026-07-05  
**Task:** V9-06D9-L

## Repair performed

After Classic Editor activation, ACF field groups remained invisible in admin because all 13 groups existed only as local JSON pending sync.

**Allowed repair:** `wp acf json sync` — imported existing JSON definitions into DB without modifying JSON schema or field values.

| Item | Result |
|---|---|
| Groups synced | 13 |
| Home group DB ID | 114 |
| ACF JSON files changed | 0 |
| ACF field values changed | 0 |
| Location rule | `page_type == front_page` (valid for page #4) |

## Seeded Home fields preserved

All D9-I/D9-K seeded values verified intact post-repair (hero attachment 89, gallery attachments 90–93, text/repeater fields populated).

Evidence: `validation/v9-06d9l-admin-editor-acf-visibility-repair/acf-admin-visibility-repair-result.json`
