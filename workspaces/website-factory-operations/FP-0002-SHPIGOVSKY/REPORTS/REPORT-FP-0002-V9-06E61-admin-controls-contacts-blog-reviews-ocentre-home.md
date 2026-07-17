# REPORT — FP-0002 V9-06E61 Admin Controls and Page Refinements

**Date:** 2026-07-17  
**Runtime:** `http://shpigovsky.test/`  
**Database:** `mars_wp_fp0002`  
**Evidence:** `REPORTS/evidence/v9-06e61-admin-controls-contacts-blog-reviews-ocentre-home/`  
**Backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e61-before-admin-controls-contacts-blog-reviews-ocentre-home-20260717-141747`

---

## 1. Status

| Item | Result |
|------|--------|
| Overall | **PARTIAL PASS** |
| Operator review | **pending** |
| DB writes | **yes** (settings seeds + 10 demo posts + 1 review_service) |
| Commit / push / freeze | **no** |

Local FE smoke: target routes HTTP 200; multi-phone, empty Contacts crumbs shell, review expand hooks, O-centre gallery/CTA-1 removal, Home spans, Blog `/blog/page/2/` OK. Gaps: full viewport screenshot pack / admin UI screenshots not captured in this wave; founder quote admin field group still relies on static fallbacks (no `block_founder_quote` PHP group); nested `<section>` CTA inside `#who-we-treat` (works, markup not ideal).

---

## 2. Pre-Change Backup

| Item | Value |
|------|-------|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e61-before-admin-controls-contacts-blog-reviews-ocentre-home-20260717-141747` |
| DB dump | `db/mars_wp_fp0002.sql` — 4 111 440 bytes — SHA256 `ACC4F85C957C3A166802A82928D1B9F6073FEDC10387FE896DF1E145D8AD51A4` |
| Validation | **PASS** (`CREATE TABLE` + `INSERT`; `--no-tablespaces`; `BACKUP-OK.txt`) |
| Hashes / manifest | `hashes.csv`, `operator-change-manifest.csv` |

---

## 3. Latest Operator Changes Canonized

| Item | Detail |
|------|--------|
| CSS `v9-style.css` | Runtime promoted → source **before** wave (`5E4378756424`); includes operator breadcrumb **16px/22px**, footer/feature-grid tweaks |
| JS `v9-shell.js` | Runtime promoted (infra slider `slidesPerView` tweaks) |
| Lifebuoy CSS | Runtime promoted (`opacity: 0.2`) |
| Post-wave CSS | Additive only (+24 lines: contacts `__text`, review clamp, phone-row helpers) → `DCB0C163AD41` |
| Unresolved theme drift after delivery | **0** for delivered exact files |

---

## 4. Global Breadcrumb Controls

| Item | Detail |
|------|--------|
| Fields | `show_breadcrumbs_pages`, `show_breadcrumbs_services` on `fp02-site-settings-general` (default **1**) |
| Ownership | Site Options — Contacts/Organisation group (+ PHP `FieldGroups::site_options_contacts`) |
| Pages | `page` templates, blog posts page, Contacts, Reviews, institutional pages → **pages** toggle |
| Services | CPT `service` singular → **services** toggle |
| Disabled | Trail omitted; `internal-page-nav` keeps subnav when present |
| Contacts/Reviews empty | Structural empty `<nav class="breadcrumbs" data-breadcrumbs-empty="1">` when toggle ON (no invented crumbs) |
| Operator styles | Preserved (16/22 on internal-page-nav crumbs) |

---

## 5. Span Wrapper Changes

| Selector | Status |
|----------|--------|
| `.program-approach-band__intro` | wrapped |
| `.home-rehabilitation-program__intro` | wrapped (2) |
| `.home-genotyping__text` | wrapped (3) |
| `.services-program-v2__intro` | wrapped |
| `.infrastructure-narrative__lead` | wrapped + red-line class |
| `.infrastructure-narrative__bullet` | wrapped |

---

## 6. Contacts

| Item | Result |
|------|--------|
| Heading field | `contacts_heading` first; seeded «Контакты» |
| Admin order | heading → form intro → phones → messengers → locations |
| Multiple phones | Repeater render; DB rows 2 preserved (`Телефон 2` intact); FE shows **2** `tel:` links |
| Messenger block | After phone-row; classes share header messengers; uses `shpigovsky_get_messenger_link_rows()` (incl. `#` visual fallback) |
| `.contacts-location__value` | Removed; content via `.contacts-location__text` / address |
| Breadcrumb skeleton | Empty shell present |
| Page ID | **20** |

---

## 7. Blog Archive

| Item | Result |
|------|--------|
| Editor | Hidden for `page_for_posts` (**19**) via `admin-editor.php` |
| Fields | `blog_archive_title`, `blog_archive_intro`, `blog_archive_posts_per_page` (1–50, default 12), `blog_archive_show_cta`, `blog_archive_show_founder_word` |
| Reusable ownership | CTA → `fp02-block-cta-bands`; Founder → `fp02-block-founder-quote` helper + static fallbacks |
| Pagination | `pre_get_posts` + `/blog/page/2/` **200** |
| Demo articles | IDs **1745–1754**, slugs `demo-pagination-article-01`…`10` |

---

## 8. Reviews

| Item | Result |
|------|--------|
| Model | Options `fp02-reviews` repeater (not CPT) |
| `review_service` | post_object → service CPT; label «Повод обращения» |
| Frontend | «Повод обращения:» + title/link; seeded row0 → service **#1019** |
| Expandable text | CSS clamp + JS (`data-review-read-more`); labels Читать весь отзыв / Свернуть |
| `reviews_per_page` | default **10** |
| Page ACF | `group_fp02_page_reviews` → RU notice + link to Reviews admin |

---

## 9. O-centre

| Item | Result |
|------|--------|
| `#o-centre-cta-1` | **gone** |
| Span wrappers | program intro + infrastructure lead/bullets |
| Program CTA | After `#who-we-treat` body (`o-centre-who-we-treat-cta`); guest CTA retained later |
| Who-we-treat gallery | **removed** |
| Home sections | staff / feature-grid / clinic-landscape (`Команда` / `Преимущества` / `Территория клиники`) |
| Red-line lead | `.infrastructure-narrative__lead.block-whith-red-line` under head |

---

## 10. Home

| Item | Result |
|------|--------|
| Dotted leaders | Already present on `.home-treatment-prevention__service-item` + `__service-leader` (operator canon); no markup rewrite required |
| Operator layout / lifebuoy | Preserved |

---

## 11. Database Changes

See `evidence/.../db-writes.json` and `demo-posts.csv`.

- `contacts_heading` @20  
- `show_breadcrumbs_pages/services` = 1  
- Blog #19: posts_per_page=12, show_cta/show_founder=1  
- `reviews_per_page`=10; `reviews_items_0_review_service`=1019  
- Posts 1745–1754 created  
- Phones **not** overwritten  
- Unrelated writes claimed **0**

---

## 12. Exact Files Changed

**Theme (source + runtime delivered):** template-tags, contacts/blog/reviews helpers, admin-editor, reusable-blocks-helpers, breadcrumbs, internal-page-nav, contacts map-body/location-card, review-archive-card, blog lower-stack, home rehab/genotyping/founder-quote, institutional who-we-treat/approach/about-program/infrastructure, institutional.php, contacts.php, reviews.php, home.php, v9-style.css, v9-shell.js, (+ related partials touched earlier in wave).

**Plugin:** `src/Fields/FieldGroups.php` (+ prior RepeaterValidation WIP foreign).

**ACF JSON:** page_contacts, blog_archive_settings, site_options_contacts, site_options_reviews, page_reviews.

**Reports/evidence:** this report, seed runner, db-writes, demo-posts, hashes.

---

## 13. Source-to-Runtime Delivery

Exact-file copy (no broad sync). Sample hashes match source↔runtime for delivered theme/plugin files (`FieldGroups` match=True).

---

## 14. Validation

| Route | HTTP | Notes |
|-------|------|-------|
| `/` | 200 | spans; leaders present |
| `/kontakty/` | 200 | 2 phones; messengers; empty crumbs; no `__value` |
| `/otzyvy/` | 200 | service line; read-more hooks |
| `/blog/` | 200 | pagination UI |
| `/blog/page/2/` | 200 | page 2 |
| `/o-centre/` | 200 | no cta-1; no who gallery; CTA after body; home blocks |
| `/uslugi/` | 200 | smoke |

Viewports 1440/1024/480/370: **SAFE UNKNOWN** (no screenshot pack this run). Admin screens: **SAFE UNKNOWN** (fields registered; not screenshot-verified).

---

## 15. Regression

Smoke only: header messengers still render; maps/locations present on Contacts; CTA bands on O-centre; lifebuoy CSS operator opacity preserved. Full gallery/forms/video matrix: **SAFE UNKNOWN**.

---

## 16. Risks and Tails

- Demo posts 1745–1754 need operator cleanup later  
- Legacy contacts postmeta dormant (address/blocks) untouched  
- Founder quote admin ACF group not fully registered (runtime fallbacks OK)  
- Nested section CTA in who-we-treat  
- Review expand overflow measure depends on fonts/load (same pattern as service signs)  
- ACF JSON vs DB duplicate groups: soft-sync may be needed in wp-admin on next load  

---

## 17. Git Status

- **No commit / no push**  
- FP-0002 WORDPRESS paths modified; foreign WIP outside allowlist untouched  
- Branch `mars/canonical-post-recovery` @ `7443c4e9…` (pre-existing unpushed history remains)

---

## 18. Operator Review Pages

**Priority 1 — frontend**

1. `/kontakty/` — phones ×2, messengers after phone, no location value class, empty crumbs shell, heading  
2. `/otzyvy/` — повод обращения, expand/collapse, pagination density  
3. `/blog/` + `/blog/page/2/` — demo posts, CTA/founder toggles visually  
4. `/o-centre/` — no old CTA-1, who-we-treat without gallery, program CTA, three Home-like blocks, red-line lead  
5. `/` — intro spans + dotted leaders  
6. One service page + `/uslugi/` — breadcrumb toggle sanity  

**Priority 2 — admin**

1. Настройки сайта → General: breadcrumb toggles  
2. Page Контакты (#20): field order heading → intro → phones  
3. Page Блог (#19): no classic editor; archive fields only  
4. Отзывы (`fp02-reviews`): review_service + reviews_per_page  
5. Page Отзывы (#18): notice/link only  

---

**No freeze. No commit. No push.**
