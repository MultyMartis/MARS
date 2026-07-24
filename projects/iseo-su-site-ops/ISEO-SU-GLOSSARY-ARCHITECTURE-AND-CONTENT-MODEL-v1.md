# ISEO-SU GLOSSARY ARCHITECTURE AND CONTENT MODEL v1

**Programme:** ISEO-SU-SITE-OPS
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-ARCHITECTURE-TEMPLATE-AND-CONTENT-INTAKE
**Site:** https://i-seo.su/
**Date:** 2026-07-24

---

## 1. Feature Status

| Field | Value |
|-------|-------|
| Status | **FOUNDATION READY / TERMS IMPORTED AS DRAFTS** |
| Public launch | **HOLD** — operator review required |
| CPT | `glossary` deployed in theme `iseoblog` |
| Templates | `archive-glossary.php`, `single-glossary.php` |
| Draft terms | **241** |
| Published terms | **0** |
| Menu link | **not added** |
| Sitemap | **excluded** while `ISEO_GLOSSARY_PUBLIC_EXPOSURE` is false |
| Anonymous `/glossary/` | **404** |
| Import tool | deployed then **disabled** (`ISEO_GLOSSARY_IMPORT_ENABLED = false`) |
| New CSS | **none** |

---

## 2. Business Goal

Professional SEO / digital-marketing glossary managed in WordPress, alphabetically browsable, with individual term pages, extensible editorial metadata, and no invented definitions.

---

## 3. Source Workbook

| Field | Value |
|-------|-------|
| Original filename | `ГЛОССАРИЙ РАБОЧИЙ САЙТ.xlsx` (provider: Никита) |
| Canonical immutable source | `materials/glossary/ISEO-SU-GLOSSARY-SOURCE-NIKITA-v1.xlsx` |
| Classification | **SOURCE / IMMUTABLE / NIKITA v1** |
| SHA-256 | `f7651cffc5d03c497062ac6ee5b6288d9397ae5abede43fbd19f1a3ea26699de` |
| Byte size | `23820` |
| Source register | `ISEO-SU-GLOSSARY-SOURCE-MATERIAL-REGISTER-v1.md` |
| Provenance README | `materials/glossary/README.md` |
| Working copy (non-canonical) | `data/glossary-intake/glossary-rabochiy-sait.xlsx` |
| Sanitized inventory | `data/glossary-intake/glossary-terms-inventory-v1.json` + `.csv` (derived; parent hash above) |
| Sheet | `Лист1` |
| Columns | Термин · Ключевые слова · LSI-фразы · Синонимы |
| Versioning | never overwrite v1; future revisions → v2, v3, … |

---

## 4. Content Readiness

| Item | State |
|------|-------|
| Term titles | Ready (241 unique) |
| Keywords / LSI / synonyms | Imported as ACF editorial metadata |
| Definitions / excerpts | **Absent** — not invented |
| Publishable pages | **Not ready** |

---

## 5. WordPress Architecture

| Layer | Decision |
|-------|----------|
| Location | Active theme `iseoblog` includes under `inc/` + CPT templates at theme root |
| Pattern | Same modular require style as existing `inc/*` and CPT `offer` in `functions.php` |
| Child theme | **Not** created |
| External glossary plugin | **Not** used |
| Shared CSS/JS | Unchanged (`css/main.css`, `css/media.css`, `js/common.js`) |

Local source package: `projects/iseo-su-site-ops/wordpress/iseoblog-glossary/`.

---

## 6. CPT Model

| Setting | Value |
|---------|-------|
| Post type | `glossary` |
| Labels | Глоссарий / Термин / Добавить термин |
| Supports | title, editor, excerpt, revisions, custom-fields |
| Comments | off (not in supports) |
| `has_archive` | `glossary` → `/glossary/` |
| Rewrite | slug `glossary`, `with_front => false` (aligned with CPT `offer`, not blog `.html`) |
| REST | `show_in_rest => true` for Admin/ACF convenience; public published list currently empty |
| Search | `exclude_from_search => true` pre-launch |
| Nav menus | `show_in_nav_menus => false` |

---

## 7. ACF Model

PHP-registered local field group `group_iseo_glossary_term` (theme has no `acf-json`):

| Field | Name | Role |
|-------|------|------|
| Синонимы | `glossary_synonyms` | Optional public synonym line |
| Ключевые слова | `glossary_keywords` | Editorial |
| LSI-фразы | `glossary_lsi_phrases` | Editorial |
| Внутренние заметки | `glossary_source_notes` | Non-public notes |

Native WP:

- title = term
- content = full definition (empty for now)
- excerpt = short definition (empty for now)

Letter group is **derived** from title (not stored).

---

## 8. URL Model

| Surface | URL | Pre-launch behaviour |
|---------|-----|----------------------|
| Archive | `/glossary/` | Anonymous **404**; editors can preview |
| Single | `/glossary/{slug}/` | Anonymous **404** unless capability; drafts only via preview |
| Collision check | no physical `glossary` / `glossary.html` | clear |

Publication gate constant: `ISEO_GLOSSARY_PUBLIC_EXPOSURE` (default **false**).

---

## 9. Archive UX

Implemented with existing classes only:

1. H1 «Глоссарий» in `page_scene`
2. Intro in `content_block`
3. Alphabet nav via `blog_filter` / `blog_filter__btn` (only non-empty letters)
4. Groups as `content_block` + `h2` + `ul`/`li` links
5. Optional GET search `glossary_q` (server-side filter; no JS required)
6. Empty / no-results copy inside `content_block`
7. Single page for ~241 terms (`posts_per_page = -1`)

---

## 10. Single Term UX

`page_scene` + breadcrumbs + `content_block` article:

- H1 = term
- Excerpt (if any) near top
- Content definition
- Synonyms block when ACF filled
- Link back to archive
- No fake dates / authors / ratings / FAQ / invented schema

---

## 11. Existing Style Reuse

Reused from privacy/legal and blog chrome:

`page_scene`, `page_scene_inner`, `page_scene__description`, `container`, `row`, `breadcrumbs`, `see_more_btn`, `content_block`, `content_block__title`, `blog_filter*`, body classes `overlay_on content`, shared header/footer.

No new stylesheet, selectors, or inline styles in glossary templates.

---

## 12. Reference Pages and Components

| Reference | Role |
|-----------|------|
| `/privacy-policy.html` | Visual SoT for internal page scene + content_block |
| `/user-agreement.html` | Same pattern confirmation |
| Blog `blog_filter` | Alphabet chip/nav reuse |
| Theme `header.php` / `footer.php` | WP chrome |
| CPT `offer` registration | CPT rewrite precedent |

Privacy-policy file was **not modified**.

---

## 13. Import Model

| Item | Detail |
|------|--------|
| Inventory | Theme `inc/data/glossary-terms-inventory-v1.json` |
| Admin tool | Tools → Импорт глоссария (when enabled) |
| Modes | dry-run + draft create |
| Idempotency | skip existing by normalized title |
| Status | always `draft` |
| Definitions | never generated |
| Post-import | `ISEO_GLOSSARY_IMPORT_ENABLED = false` |

---

## 14. SEO and Indexation

| Control | State |
|---------|-------|
| `wp_robots` noindex/nofollow | forced while not publicly exposed |
| Yoast sitemap exclude | glossary post type excluded while gate closed |
| Menu | not linked |
| Published empties | none |

---

## 15. Editorial Workflow

1. Keep terms as drafts.
2. Write definition in editor + short excerpt.
3. Review synonyms if public.
4. Yoast title/description per term.
5. Operator opens publication gate (`ISEO_GLOSSARY_PUBLIC_EXPOSURE`).
6. Publish terms intentionally; add menu/sitemap only after content QA.

---

## 16. Validation

See task REPORT and receipts under `_glossary-scratch/` (local evidence; not authority docs).

Highlights: 241 drafts; ACF visible; archive preview for editors; anonymous 404; baselines 200; no WPilot REST; import disabled after use.

---

## 17. Rollback

1. Restore `functions.php` from `.bak-glossary-*` or pre-deploy backup.
2. Remove `archive-glossary.php`, `single-glossary.php`, `inc/glossary-*.php`, `inc/data/glossary-terms-inventory-v1.json`.
3. Delete only `glossary` draft posts (Admin bulk or scoped DB op under charter).
4. Flush permalinks.
5. Verify `/`, privacy, blog, tariff-calc, offers.

Full Beget backup remains last resort (operator-confirmed pre-task).

---

## 18. Risks

| Risk | Mitigation |
|------|------------|
| Empty public archive indexed | Gate + 404 + noindex + sitemap exclude |
| Accidental publish of empty terms | Editorial HOLD; drafts only |
| Search form conflicting with `common.js` lead forms | No `*__FORM*` ids/classes on glossary search |
| Russian alphabet sorting edge cases | Derived letter helper + explicit Cyrillic order including Ё |

---

## 19. SAFE UNKNOWN

| ID | Item |
|----|------|
| G-U-001 | Exact Yoast primary focus workflow preference per term (operator) |
| G-U-002 | Whether final public singles should use `.html` suffix like blog (currently CPT slash URLs like `offer`) |
| G-U-003 | Future related-terms UX / bidirectional links |
| G-U-004 | Whether inventory JSON should remain on server after import (currently present; import UI disabled) |

---

## 20. Publication Gate

Do **not** publish until operator confirms:

1. Definitions written for launch set (or explicit thin-page policy change — not recommended).
2. `ISEO_GLOSSARY_PUBLIC_EXPOSURE = true` deliberately set.
3. Sample published terms QA’d on desktop/mobile.
4. Menu / internal links / sitemap inclusion decided.
5. Fresh backup before mass publish.

---

*Glossary architecture and content model v1 · 2026-07-24.*
