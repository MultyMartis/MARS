# Hooks removed / retained — PROD-P13-FU01

Production probe after deploy (`QA-RUNTIME.json`).

## Removed (no longer registered)

| Hook | Callback | Why |
|------|----------|-----|
| `add_meta_boxes` | `PermalinkSlugUX::register_metabox` | duplicate **URL / ярлык** UI |
| `edit_form_after_title` | `PermalinkSlugUX::render_native_permalink_box` | second **Постоянная ссылка** row |
| `admin_head` | `PermalinkSlugUX::admin_css` | CSS/JS for `#edit-slug-box` + `fp02_post_name` sync |

Field `fp02_post_name` is gone. Module `admin.permalink-slug-ux` remains enabled for data-layer uniqueness only.

## Retained

| Hook | Priority | Role |
|------|----------|------|
| `wp_insert_post_data` | 99 | Preserve native `$_POST['post_name']`; empty native slug → regenerate from title; draft uniqueness `-copy-NN` (core `wp_unique_post_slug` returns early for drafts) |
| `wp_unique_post_slug` | 10 | Readable `-copy-01` / `-copy-02` instead of `-2` for published uniqueness |

## Service permalink sample (native Edit)

| Hook | Change |
|------|--------|
| `post_type_link` | now 4 accepted args; when `$leavename` is true, last path segment is `%postname%` so core can render **Изменить**. Frontend `get_permalink()` (`$leavename=false`) unchanged. |

No `save_post` slug rewriter. ActivityLog `save_post` is logging only.
