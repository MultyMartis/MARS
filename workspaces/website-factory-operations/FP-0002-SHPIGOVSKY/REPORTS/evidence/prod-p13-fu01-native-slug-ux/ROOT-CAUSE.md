# SLUG UX DUPLICATION ROOT CAUSE

**Wave:** FP-0002 PROD-P13-FU01  
**Status:** SLUG UX DUPLICATION ROOT CAUSE IDENTIFIED

## Duplicate UI owners

On Service `#73` and Specialist `#1033` **before** this wave, Admin HTML contained:

| Row | Owner | Markup |
|-----|--------|--------|
| 1 | WordPress core (`edit-form-advanced.php` `#titlediv`) | `<div id="edit-slug-box">` + `get_sample_permalink_html()` → label **Постоянная ссылка** |
| 2 | FP-0002 `PermalinkSlugUX::render_native_permalink_box` on `edit_form_after_title` | second `<div id="edit-slug-box" class="fp02-edit-slug-box">` + the same `get_sample_permalink_html()` |
| 3 (side) | FP-0002 `PermalinkSlugUX::register_metabox` | postbox `fp02_permalink_slug` titled **URL / ярлык**, field `fp02_post_name` |

Standard Page `#5` (`/uslugi/`) had **exactly one** `#edit-slug-box` and no FP-0002 metabox.

Evidence: `snippet-before-service-permalink.html`, `snippet-before-specialist-permalink.html`, `ADMIN-UX-BEFORE.json`.

## Why P13 added a second box

PROD-P13 FIX01 tried to restore a native-looking slug editor **and** keep the P12 custom metabox. `render_native_permalink_box` printed a second sample permalink under the title. Core already printed the first.

## Why Service lacked native «Изменить»

`ServicePermalinks::filter_service_permalink` registered `post_type_link` with **2** arguments and always returned a fully resolved URL (`/uslugi/zavisimosti/`). WordPress `get_sample_permalink_html()` only renders the Edit control when the sample permalink still contains `%postname%` or `%pagename%`.

Specialist (no such filter) already had native **Изменить**. Service did not. The custom metabox was compensating for that, not replacing a missing core row.

## Persistence conflict owner

`PermalinkSlugUX::filter_insert_post_data` (priority 99) preferred `$_POST['fp02_post_name']` over native `$_POST['post_name']`. Empty custom field forced title regeneration even when the native slug was present.

`wp_unique_post_slug` still skipped drafts in core; uniqueness for drafts required a data-layer hook (kept).

## Not used

CSS hiding of a duplicate row. The second box, metabox, and `fp02_post_name` JS/CSS were **removed from PHP**, not hidden.
