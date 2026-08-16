# CPT SLUG INVENTORY — PROD-P12

**Date:** 2026-08-16  
**Authority:** production DB + `shpigovsky-core` ModuleRegistry (post-intake)

## Inventory

| Entity | post_type | public? | rewrite | single permalink | supports slug UI today (pre-P12) | should be editable | Class |
|--------|-----------|---------|---------|------------------|----------------------------------|--------------------|-------|
| Услуги | `service` | yes | `uslugi` hierarchical | yes `/uslugi/.../` | partial (classic; no dedicated control) | **yes** | **A** |
| Специалисты | `specialist` | yes | `specyalisty` | yes `/specyalisty/{slug}/` | partial | **yes** | **A** |
| Страницы | `page` | yes | native | yes | native WordPress | leave intact | **D** |
| Статьи | `post` | yes | native | yes | native WordPress | leave intact | **D** |
| Отзывы | *(not a CPT)* | archive via options/ACF `reviews_items` | n/a | **no per-review permalink CPT** | n/a | **no slug control** | **B/C** |
| ACF field/group | `acf-field*` | admin | n/a | no | no | no | **C** |
| Attachments | `attachment` | media | n/a | attachment URLs | native | leave | **D** |
| Nav menu items | `nav_menu_item` | internal | n/a | no public singles | no | no | **C** |

## Classification key

- **A** — public + single permalink → needs editable slug UX  
- **B** — public but no single permalink → no slug edit  
- **C** — admin-only/internal → no slug edit  
- **D** — page-like already handled natively → leave intact  

## Reviews note

Operator named «Отзывы». Production model stores reviews in Site Settings / ACF options repeater (`reviews_items`), **not** as a public CPT with `post_name`. Therefore reviews are **out of slug-edit scope** (no competing URL field invented).

## P12 behavior (A entities)

1. Admin metabox **«URL / ярлык»** on `service` + `specialist`  
2. Canonical storage: `wp_posts.post_name` only  
3. Empty slug on save → regenerate from title  
4. Collision → `-copy-01`, `-copy-02`, … (also for drafts via `wp_insert_post_data`)  
5. Existing production slugs **not** mass-regenerated  

PUBLIC CUSTOM ENTITIES HAVE EDITABLE WORDPRESS-NATIVE SLUGS
