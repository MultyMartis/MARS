# REPORT — FP-0002 V9-06E62B Blog/Reviews Pagination, SEO and Slider Links

**Date:** 2026-07-17  
**Runtime:** `http://shpigovsky.test/`  
**Database:** `mars_wp_fp0002`  
**Evidence:** `REPORTS/evidence/v9-06e62b-blog-reviews-pagination-seo-slider-links/`  
**Backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e62b-before-blog-reviews-pagination-seo-demo-content-20260717-162925`

---

## 1. Status

| Item | Result |
|------|--------|
| Overall | **PASS** (local validation) |
| Operator review | **pending** |
| DB writes | **yes** (demo Blog thumbs, 20 demo Reviews rows, Founder seed, featured tweaks) |
| Commit / push / freeze | **no** |

Architecture note: Reviews are **ACF Options repeater** (`reviews_items` on `fp02-reviews`), not a Review CPT. Demo “reviews” and anchors follow that model (`id="review-{1-based-row-index}"`).

---

## 2. Pre-Change Backup

| Item | Value |
|------|-------|
| Path | `…\v9-06e62b-before-blog-reviews-pagination-seo-demo-content-20260717-162925` |
| DB dump | `db/mars_wp_fp0002.sql` — 6 640 597 bytes — SHA256 `35F9D7B9…ACE3688F` |
| Validation | **PASS** (`CREATE TABLE` + `INSERT`; `--no-tablespaces`; `BACKUP-OK.txt`) |
| Hashes / manifest | `hashes.csv`, `operator-change-manifest.csv`, `BACKUP-INFO.md` |

---

## 3. Latest Operator Changes Canonized

| Item | Detail |
|------|--------|
| Pre-wave theme drift | **0** (php/css/js source = runtime) |
| Pre-wave plugin drift | **0** |
| CSS promote | None required; protected E62A hash `E11627B9…` then **wave-additive** → `18114D3C…` |
| Templates / HTML | No operator-only HTML drift |
| ACF JSON | 8 source-only groups **not** synced; **1** new founder group delivered (Blog/Reviews ownership only) |
| Breadcrumb CSS | Operator **16px / 22px** preserved |
| Unresolved drift | 8 historical source-only ACF groups (Service FAQ/relationships/etc.) — out of scope |

---

## 4. Demo Blog Images

| Item | Detail |
|------|--------|
| Post IDs | **1745–1754** |
| Mapping | See `demo-blog-image-mapping.csv` |
| Attachments used | `1106, 1089, 1088, 1087, 1086, 1085, 1084, 93, 92, 91` (existing local ML; no new uploads) |
| Idempotency | Empty thumb only; rerun → skip |
| Frontend | `/blog/`, `/blog/page/2/` HTTP 200; image URLs 200 |

---

## 5. Demo Reviews

| Item | Detail |
|------|--------|
| Model | ACF `reviews_items` (not CPT) |
| Added | **20** rows (`e62b-demo-01`…`20`) |
| Total rows | **30** (10 existing + 20 demo) |
| Services | Distributed across `#74, #314, #1019, #1017, #1016, #1013, #1018, #1011, #315, #316` |
| Length classes | short / boundary / long_slider / long_archive |
| Duplicate prevention | Source marker `e62b-demo-NN` + author prefix; rerun created **0** |
| Featured tweak | Last 5 pre-existing rows unfeatured so long demos enter home slider top-10 |

Matrix: `demo-reviews-matrix.csv`, anchors: `review-anchor-destination-matrix.csv`.

---

## 6. Blog Pagination

| Item | Value |
|------|-------|
| Setting | `blog_archive_posts_per_page` = **12** (page `#19`) |
| Total posts | **16** → **2** pages |
| Routes | `/blog/` 200; `/blog/page/2/` 200; `/blog/page/3/` **404** |
| Query | `pre_get_posts` helper unchanged in contract |

---

## 7. Reviews Pagination

| Item | Value |
|------|-------|
| Setting | `reviews_per_page` = **10** |
| Total | **30** → **3** pages |
| Routes | `/otzyvy/` 200; `/page/2/` 200; `/page/3/` 200; `/page/99/` **404** |
| Out-of-range | `redirect_canonical` blocked + `template_redirect` 404 |
| Anchors | `review-1`…`review-10` page1; `11–20` page2; `21–30` page3 |

---

## 8. Pagination SEO

No Yoast/RankMath/AIOSEO active. Theme owns Blog/Reviews canonicals via `inc/pagination-seo.php` (core `rel_canonical` removed on those views).

| Route | Status | Canonical | Robots | Title | OG URL | Result |
|-------|--------|-----------|--------|-------|--------|--------|
| `/blog/` | 200 | `/blog/` | `noindex, nofollow` (site-wide local) | Статьи — … | — | PASS self-canonical |
| `/blog/page/2/` | 200 | `/blog/page/2/` | same | Статьи — Страница 2 — … | — | PASS (not page1) |
| `/blog/page/3/` | 404 | — | noindex | 404 title | — | PASS |
| `/otzyvy/` | 200 | `/otzyvy/` | same | Отзывы — … | — | PASS |
| `/otzyvy/page/2/` | 200 | `/otzyvy/page/2/` | same | Отзывы — Страница 2 — … | — | PASS |
| `/otzyvy/page/3/` | 200 | `/otzyvy/page/3/` | same | Отзывы — Страница 3 — … | — | PASS |
| `/otzyvy/page/99/` | 404 | — | noindex | 404 title | — | PASS |

Canonical count on valid pages: **1**. No canonical-to-page-1 from page 2+.  
SAFE UNKNOWN: site-wide `noindex, nofollow` is local WP policy (`blog_public` / local meta) — not introduced by this wave.

Evidence: `seo-canonical-matrix.csv`, `head-*.html`.

---

## 9. Review Slider Full Links

| Item | Detail |
|------|--------|
| Templates | `template-parts/shared/reviews-slider.php` (Home, Service, O-centre via `home/reviews`) |
| Clamp | CSS `-webkit-line-clamp: 5` + JS overflow detect |
| Link | Semantic `<a>Читать весь отзыв</a>` only when overflow; no in-place expand |
| Target helper | `shpigovsky_get_review_archive_url( $review_id )` (request-cached map) |
| Anchor | `id="review-{ID}"` + `scroll-margin-top: 120px` |
| Archive | E61 expand/collapse unchanged (`data-review-read-more`, LINE_COUNT 6) |
| Tested | Home (10 `data-review-slider-full-link` attrs); alcohol service slider; O-centre route smoke |
| Page calc | `#1` → `/otzyvy/#review-1`; `#11` → `/otzyvy/page/2/#review-11`; `#21` → `/otzyvy/page/3/#review-21` |

---

## 10. Founder’s Word Ownership

| Item | Detail |
|------|--------|
| Previous | Menu slug existed; fields empty → static fallbacks |
| Final owner | Reusable options `fp02-block-founder-quote` + `group_fp02_block_founder_quote` |
| Blog | Toggle `blog_archive_show_founder_word` only |
| Seeded | paragraphs×4, name, role, CTA, photo `#754` (empty-only) |
| Removed UI | No Blog duplicate content fields were present (already E61); instructions updated to point at reusable block |
| Preserved | Same visible copy/image as prior fallbacks |

---

## 11. Database Changes

| Scope | Change |
|-------|--------|
| posts/postmeta | `_thumbnail_id` on `#1745–1754` |
| options repeater | +20 `reviews_items`; 5 existing `review_featured` → 0 |
| options founder | `founder_quote_*` seed on `fp02-block-founder-quote` |
| Unrelated writes | **0** (no deletes of real content / dormant meta) |

Log: `db-writes.csv` (first apply; idempotent rerun → 0 writes).

---

## 12. Exact Files Changed

### Canonical source
- `WORDPRESS/theme/shpigovsky/functions.php`
- `WORDPRESS/theme/shpigovsky/inc/reviews-helpers.php`
- `WORDPRESS/theme/shpigovsky/inc/pagination-seo.php` *(new)*
- `WORDPRESS/theme/shpigovsky/template-parts/components/review-archive-card.php`
- `WORDPRESS/theme/shpigovsky/template-parts/reviews/archive-list.php`
- `WORDPRESS/theme/shpigovsky/template-parts/shared/reviews-slider.php`
- `WORDPRESS/theme/shpigovsky/assets/js/v9-shell.js`
- `WORDPRESS/theme/shpigovsky/assets/css/v9-style.css`
- `WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php`
- `WORDPRESS/plugins/shpigovsky-core/src/Admin/OptionsPage.php`
- `WORDPRESS/acf-json/group_fp02_block_founder_quote.json` *(new)*

### Runtime
Exact copies of the above under `wp-content/themes/shpigovsky/`, `wp-content/plugins/shpigovsky-core/`, `wp-content/acf-json/`.

### Reports / evidence
- `REPORTS/REPORT-FP-0002-V9-06E62B-blog-reviews-pagination-seo-slider-links.md`
- `REPORTS/evidence/v9-06e62b-blog-reviews-pagination-seo-slider-links/**`
- `PROJECT-STATUS.md`, `WORDPRESS/SOURCE-AUTHORITY.md`

---

## 13. Source-to-Runtime Delivery

| Item | Result |
|------|--------|
| Method | Exact-file copy only (**no** broad sync) |
| Match | **11/11** SHA256 match (`source-runtime-hashes.csv`) |
| Operator CSS | Additive only; crumbs preserved |

---

## 14. Validation

| Area | Result |
|------|--------|
| Blog images / pagination | PASS |
| Reviews pagination / 404 | PASS |
| Slider full links (markup + URL helper) | PASS |
| SEO self-canonicals | PASS |
| Founder reusable data | PASS (4 paragraphs + photo) |
| Viewports screenshots | Captured (1440/1024/480/370 set under `screenshots/`) |
| PHP warnings | **0** on probed routes |
| Admin UI screenshots | **PARTIAL** — not captured (admin login session not automated this wave); FE/admin field presence verified via WP/ACF bootstrap |

---

## 15. Regression

Routes in `regression-matrix.csv`: Home, Services hub, section, alcohol service, O-centre, Contacts, Blog, Reviews, 404 behavior for out-of-range. Shared shell retained. Alcohol slug note: correct path is `…/lechenie-alkogolnoy-zavisimosti/` (not `…noj…`).

---

## 16. Closed E61 Tails

Claimed closed by this wave:

1. Founder’s Word reusable ACF ownership  
2. Blog/Reviews viewport screenshot evidence pack (FE)  
3. Blog demo images + Reviews pagination density for operator review  

Not claimed: full E61 deep regression / O-centre deep work.

---

## 17. Remaining Tails for E62C

1. Nested CTA `<section>` risk in `#who-we-treat`  
2. O-centre deep validation  
3. Service ACF group cleanup (incl. 8 source-only JSON groups audit)  
4. Full final regression  
5. Demo-content cleanup decision (Blog `#1745–1754` + E62B demo reviews)  
6. Optional: admin UI screenshot capture for Blog/Reviews/Founder options  

---

## 18. Risks and SAFE UNKNOWN

- Demo content is **local-only**  
- Site-wide `noindex, nofollow` (local) — not wave-introduced  
- Review IDs are **repeater row indices** (reorder changes anchors)  
- Slider overflow depends on fonts/layout; rechecked on resize  
- 8 source-only ACF JSON groups remain unsynced by charter  

---

## 19. Git Status

- **No commit / no push / no freeze**  
- Exact FP-0002 paths only  
- Foreign WIP in monorepo untouched  

---

## 20. Operator Review Pages

1. http://shpigovsky.test/blog/  
2. http://shpigovsky.test/blog/page/2/  
3. http://shpigovsky.test/otzyvy/  
4. http://shpigovsky.test/otzyvy/page/2/  
5. http://shpigovsky.test/otzyvy/page/3/  
6. http://shpigovsky.test/ — review slider «Читать весь отзыв»  
7. http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ — service slider  
8. http://shpigovsky.test/o-centre/  
9. wp-admin: Posts page (Blog settings) `#19`  
10. wp-admin: `admin.php?page=fp02-reviews`  
11. wp-admin: `admin.php?page=fp02-block-founder-quote`  

Do not commit, push or freeze.
