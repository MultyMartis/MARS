# FP-0002 PROD-P13 — ownership notes

Human-maintained ownership after P13. Not a runtime product.

## Social / messengers

- **Canonical Admin owner:** `Настройки сайта → Social networks and messengers` (`fp02-site-settings-social`), ACF repeater `social_platforms` (type, url, show_header, show_footer).
- **Legacy:** `social_links` on General is hidden in Admin; values retained for rollback. Frontend falls back to it only if `social_platforms` is empty.
- **Frontend consumers:** header, floating header, mobile/offcanvas, footer, Contacts page. All read `shpigovsky_get_social_platform_rows()`.
- **Visibility:** header/floating/offcanvas use `show_header`; footer uses `show_footer`; Contacts shows every configured platform with a URL (flags do not hide Contacts).

## Entity SEO

- **Owner:** ACF group `group_fp02_seo_entity_meta` on `page`, `post`, `service`, `specialist`.
- **Fields:** `fp02_seo_title`, `fp02_seo_description`.
- **Output:** theme `inc/seo-entity-meta.php`. Empty title → WordPress `title-tag`. Empty description → omit meta description (no invented copy).
- **Reviews:** no public single URL — no SEO fields.

## Activity log

- Table `fp02_user_activity_log`. Admin screen `Журнал действий`. User ID 0 renders as System, never `#0`.

## Blog TOC

- Owner: theme `inc/blog-helpers.php`. TOC items = article-body **H2 only**, with deterministic heading IDs.

## DOCX importer

- Plugin module `admin.docx-importer`. Drafts only. Template: `plugins/shpigovsky-core/assets/docx/fp02-article-template.docx`.

## Slug UX

- Canonical URL owner remains `wp_posts.post_name`.
- Admin UI for `service` and `specialist` is the **native WordPress permalink row only** (PROD-P13-FU01). No `fp02_post_name` metabox and no second `#edit-slug-box`.
- Data-layer only: `wp_insert_post_data` priority 99 preserves a submitted native slug; empty native slug regenerates from title; drafts get `-copy-NN` uniqueness (core skips drafts).
- `wp_unique_post_slug` applies the same `-copy-01` / `-copy-02` policy when core uniquifies.
- Service `post_type_link` honors `$leavename` so sample permalink HTML can show native **Изменить**. Frontend resolved URLs are unchanged.
