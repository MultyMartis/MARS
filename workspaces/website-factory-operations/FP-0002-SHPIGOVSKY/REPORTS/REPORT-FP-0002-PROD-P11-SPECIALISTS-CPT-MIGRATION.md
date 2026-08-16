# REPORT — FP-0002 PROD-P11 Specialists CPT Migration

**Date:** 2026-08-15 (UTC session 2026-08-14)  
**Host:** http://shpigovsky.beget.tech/  
**Mode:** exact-file / exact-object rollback (no full Beget backup required for this wave)  
**Commit/push:** none

## 1. Status

- **PASS / PARTIAL** — technical migration complete; operator visual/Admin HTTP acceptance pending (Beget antibot blocks automated WP Admin cookie login; PHP Admin structure proof PASS).
- Production file writes: **yes** (exact allowlist, 12/12 parity)
- DB object writes: **yes** (exact IDs `1031,1032,1033,1097` + delete of invalid `_wp_page_template` meta for those IDs)
- ACF mutations: location rule `post_type == specialist` (PHP FieldGroups + JSON); field keys preserved; no broad sync
- WPilot writes: **0** (`write_enabled=false`)
- Commit/push: **none**

## 2. Rollback

- File snapshots: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p11-layer-b-pre\`
- DB snapshots: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p11-db-snapshots\`
- **EXACT-FILE / EXACT-OBJECT ROLLBACK READY** — see evidence `EXACT-FILE-EXACT-OBJECT-ROLLBACK-READY.md`

## 3. Specialist Inventory

- Count: **4**
- IDs: `1031` shipovsky, `1032` kazakov, `1033` kostyuk, `1097` shapiguzova
- URLs: `/specyalisty/{slug}/`
- Legacy ownership: child `page` under hub `#1030` → migrated to CPT `specialist`
- Evidence: `SPECIALIST-INVENTORY.md`

## 4. CPT Architecture

- Post type: `specialist`
- Rewrite: slug `specyalisty`, `with_front=false`, **`has_archive=false`**
- Hub `/specyalisty/` remains page `#1030`
- Supports: `title`, `thumbnail`, `page-attributes` (menu_order)
- Admin menu: top-level «Специалисты», position 22, `dashicons-groups`
- Owner: `shpigovsky-core` module `content-types.specialist` (same pattern as Услуги)

**SPECIALISTS ARE A DEDICATED WORDPRESS ENTITY**

## 5. URL Preservation

| ID | Old URL | New URL | HTTP |
|----|---------|---------|------|
| 1031 | /specyalisty/shipovsky/ | /specyalisty/shipovsky/ | 200 |
| 1032 | /specyalisty/kazakov/ | /specyalisty/kazakov/ | 200 |
| 1033 | /specyalisty/kostyuk/ | /specyalisty/kostyuk/ | 200 |
| 1097 | /specyalisty/shapiguzova/ | /specyalisty/shapiguzova/ | 200 |

**ALL SPECIALIST PUBLIC URLS PRESERVED**

## 6. Admin UX

- Structured group only on CPT: `group_fp02_specialist_profile`
- Groups on Kostyuk (`#1033`): **only** Specialist profile (no Generic Content)
- Supports omit editor; Generic Content / page layout / parent page no longer apply
- List columns: Фото, Имя, Должность/профессия, Порядок
- HTTP Admin browser QA: **blocked by Beget antibot** (same class of residual as P10); PHP structure proof PASS (`ADMIN-STRUCTURE-PROOF.json`)

**SPECIALIST ADMIN UX CLEAN AND PURPOSE-BUILT** (structure proven; operator visual pending)

## 7. Data Migration

- IDs preserved: **YES**
- `post_type`: `page` → `specialist` for exact IDs
- `post_parent`: `1030` → `0`
- Meta preserved (ACF keys unchanged)
- Legacy `generic_page_body` / related meta: **preserved** (not deleted)
- Cleared only invalid `_wp_page_template=page-templates/generic.php` (WP preferred it over `single-specialist.php`)

## 8. Frontend

- Template: `single-specialist.php` (+ force filter against leftover page-template meta)
- Structured sections / empty-state / P08 design preserved
- Hub page remains Generic Content placeholder page

## 9. Gallery / Fancybox

Kostyuk: certs grid + `data-fancybox` present; portrait/role present.

**SPECIALIST CERTIFICATE GALLERY FANCYBOX = PASS**

## 10. Hub

- `/specyalisty/` page `#1030` intact
- Listing/cards owner: CPT query via `shpigovsky_get_specialists_cards()` — **4 cards**, same order (10/20/30/40), no duplicates

## 11. Smart Search

- Group «Специалисты» returns CPT objects (e.g. «кос» → `#1033`)
- No overlap with «Страницы» for specialist IDs
- Settings keys unchanged (P10)

Desktop/mobile live UI: not re-automated beyond REST (P09/FU01 residual acceptance still operator-facing).

## 12. Sitemap

- `wp-sitemap-specialists-1.xml` lists 4 specialist URLs once
- Specialist child URLs **absent** from pages map
- Admin semantic label «Специалисты» retained

## 13. ACF

- Exact group: `group_fp02_specialist_profile`
- Location: `post_type == specialist`
- Field keys preserved
- No broad sync

## 14. Exact Files Changed

Source (and production-matched):

1. `WORDPRESS/plugins/shpigovsky-core/src/ContentTypes/Specialist.php` (**new**)
2. `WORDPRESS/plugins/shpigovsky-core/src/ModuleRegistry.php`
3. `WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php`
4. `WORDPRESS/plugins/shpigovsky-core/src/Admin/EditorRestrictions.php`
5. `WORDPRESS/acf-json/group_fp02_specialist_profile.json`
6. `WORDPRESS/theme/shpigovsky/single-specialist.php` (**new**)
7. `WORDPRESS/theme/shpigovsky/inc/specialist-helpers.php`
8. `WORDPRESS/theme/shpigovsky/inc/reusable-blocks-helpers.php`
9. `WORDPRESS/theme/shpigovsky/inc/search-helpers.php`
10. `WORDPRESS/theme/shpigovsky/inc/sitemap-helpers.php`
11. `WORDPRESS/theme/shpigovsky/inc/admin-editor.php`
12. `WORDPRESS/theme/shpigovsky/inc/template-tags.php`

Docs/evidence: this report, `PROJECT-STATUS.md`, `REPORTS/evidence/prod-p11-specialists-cpt-migration/*`

## 15. Exact DB Objects Changed

| Object | Change |
|--------|--------|
| `fp02_posts` ID 1031/1032/1033/1097 | `post_type=specialist`, `post_parent=0` |
| `fp02_postmeta` those IDs | DELETE `_wp_page_template=page-templates/generic.php` |
| `fp02_options` | `fp02_specialist_cpt_rewrite_flushed_p11=1` (one-time flush flag) |

## 16. Source / Production Parity

**12/12 SOURCE ↔ PRODUCTION MATCH** (`DEPLOY-MANIFEST.json`)

## 17. Regression

Home /uslugi/ /o-centre/ /blog/ /otzyvy/ HTTP 200. P07–P10 systems not intentionally mutated beyond Specialist ownership wiring. Residual: Beget Admin HTTP antibot.

## 18. WPilot

`write_enabled=false`; business writes **0**

## 19. Secret Safety

Exposed 0; tracked 0 (secrets only in gitignored local path; not copied into evidence)

## 20. Git

Commit none; push none; foreign WIP untouched

## 21. Acceptance

**PROD-P11 TECHNICAL CLOSEOUT COMPLETE — OPERATOR VISUAL/ADMIN ACCEPTANCE PENDING**

## 22. Next Recommendation

1. Operator opens WP Admin → **Специалисты** → edit Kostyuk; confirm clean fields/gallery/order visually.
2. Spot-check Fancybox on `/specyalisty/kostyuk/` and Smart Search on desktop/mobile.
3. Do **not** delete legacy `generic_page_*` meta without a separate cleanup charter.
4. Keep DNS/HTTPS/`shpigovsky.ru` cutover deferred.
