# CPT inventory — PROD-P13-FU01

Authority: production `get_post_types()` after intake (2026-08-16). Classification per charter.

| Entity | post_type | class | public single URL | permalink edit |
|--------|-----------|-------|-------------------|----------------|
| Услуги | `service` | **A** | yes `/uslugi/.../` | native WP row (this wave) |
| Специалисты | `specialist` | **A** | yes `/specyalisty/{slug}/` | native WP row (this wave) |
| Страницы | `page` | **C** | yes | already native |
| Записи | `post` | **C** | yes | already native |
| Вложения | `attachment` | **C** | media URLs | native media |
| Отзывы | *(not a CPT)* | **B** | no per-item CPT URL | none |
| ACF / ACFE internals | `acf-*`, `acfe-*` | **C** | no | none |
| WP internals | `revision`, `nav_menu_item`, `wp_*` | **C** | no | none |

**A** — public + single permalink → native permalink edit required.  
**B** — no public single → no permalink edit UI.  
**C** — native page/post or non-public → leave / not applicable.

No custom URL meta fields invented. Canonical owner: `wp_posts.post_name`.
