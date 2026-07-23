# Future automatic category creation design

## Goal

Importer must resolve and (when needed) **create** OpenCart categories from 1C group GUID + full path — never by leaf name alone into legacy collision targets.

## Identity store

Maintain mapping table (name TBD; recommended oc_1c_category_map or site-local equivalent):

| Column | Purpose |
|--------|---------|
| source_group_id (GUID PK) | 1C group <Ид> |
| category_id | OpenCart category_id |
| source_full_path | audit / fallback match |
| parent_group_id | optional |
| match_method | GUID / PATH / CREATED |
| updated_at | audit |

Also keep product xml_id (already on oc_product).

## Resolution precedence

See importer-resolution-precedence.md.

## Auto-create algorithm

When GUID not mapped and full-path missing under correct parent:

1. Resolve parent category_id via GUID map, else path, else stop with REVIEW.
2. Create oc_category under that parent (status per policy; default active for tech tree).
3. Insert description (name from 1C; meta stub; CATEGORY_CREATED_REVIEW_REQUIRED).
4. Rebuild oc_category_path.
5. Generate deterministic unique seo_keyword (slugify name; if taken, append -tehnologicheskoe / parent slug / short GUID suffix).
6. Insert oc_seo_url.
7. Write mapping row GUID → new category_id (CREATED).
8. Report entry for HITL review (meta/image polish).

## Collision guard

Never assign tech-tree source leaf to legacy 154/159/165 (or any category whose path root is legacy 153) by leaf-name alone when source path root is tech ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ / OC 362.

## Product assignment

- Map product by xml_id.
- Map each product group ref by GUID (preferred) / path.
- Prefer targeted upsert of product_to_category over blind wrong legacy REPLACE; if uncertain, hold previous safe assignment or assign parent hub + CATEGORY_MAPPING_REVIEW_REQUIRED.
- After leaf create wave, GUID map should point to real leaves so DELETE+INSERT lands correctly.

## Order relative to this charter

1. **This charter** — plan leaves.
2. **Leaf apply** — create 3 leaves + move 4 products.
3. **Mapping backfill** — GUID→id including new leaves.
4. **Importer patch** — precedence + auto-create + report fields.
5. Legacy cleanup / redirects — later.

## Out of scope for auto-create v1

- Deleting legacy categories
- Auto-redirects
- Auto image generation
- Changing monitor baseline
