# FP-0002 V9-06E25A — Final Visibility Contract

**Wave:** V9-06E25A  
**Generated:** 2026-07-09

## Visible UI entry points

1. **Услуги list table** — row action `Дублировать` under title (hover row actions).
2. **Редактировать услугу** — side meta box `Дублирование` with button `Дублировать услугу`.

## Hooks

- `page_row_actions` → `ServiceDuplicate::add_row_action`
- `post_row_actions` → `ServiceDuplicate::add_row_action` (non-hierarchical safety)
- `add_meta_boxes` → `ServiceDuplicate::register_meta_boxes`
- `admin_post_fp02_duplicate_service` → `ServiceDuplicate::handle_admin_post` (preserved)

## Guards

- Post type `service` only
- Not autosave / revision / auto-draft / trash
- `user_can_duplicate( $post_id )` — `edit_post` + CPT-mapped create cap

## Nonce

- Action: `fp02_duplicate_service_{post_id}`
- URL: `admin-post.php?action=fp02_duplicate_service&post_id={id}&_wpnonce=...`

## Copy logic (preserved from E25)

- Draft status, title suffix ` — копия`
- Full postmeta copy (ACF refs, `hero_cta_label`, media IDs)
- Markers `_fp02_duplicated_*`, wave `V9-06E25`

## Operator QA checklist

1. Open **Услуги** → hover a service row → confirm **Дублировать** appears.
2. Open **Редактировать услугу** → confirm side box **Дублирование** with **Дублировать услугу**.
3. Click duplicate → confirm redirect to new draft edit screen with success notice.
4. Confirm source service unchanged; duplicate remains draft.

## Evidence

`validation/v9-06e25a-service-duplicate-action-visibility-repair/final-e25a-visibility-contract.json`

**Result:** PASS
