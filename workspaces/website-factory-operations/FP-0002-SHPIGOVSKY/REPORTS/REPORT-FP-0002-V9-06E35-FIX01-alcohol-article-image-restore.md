# REPORT — FP-0002 V9-06E35-FIX01 ALCOHOL ARTICLE IMAGE RESTORE

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | `X:` |
| Label | `AI WS` |
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `ebfaeb225a86d7c0b98ef446908b29c25a9e45df` (session start snapshot was `710f10c99c5b49e0fcf125ddf6da7bea948f2a37`; no git mutation by this task) |
| Staged files before | empty |
| WIP count only | ~699–707 (foreign monorepo WIP; ignored) |
| Commit allowed | NO — foreign WIP + unpushed commits on branch; task = no git reconciliation |
| Result | PASS (preflight OK; commit wave blocked by policy) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e35-fix01-alcohol-article-image-before-20260713-030319\` |
| DB dump | `mars_wp_fp0002.sql` (2 159 895 bytes) — PASS |
| Theme hash/copy | `theme-sha256.txt` (631 files) + bounded theme file copies under `theme/` |
| Uploads/media manifest | `uploads-media-manifest.txt` (98 files) |
| Target post meta before | `target-post-meta-before.json` (+ `audit-before.php`) |
| HTML snapshots before | `html-snapshots/home.html`, `blog.html`, `article-nazvanie-stati.html` |
| Result | PASS |

## 3. Target post audit

| Field | Value |
|---|---|
| Post ID | `750` |
| Title | `Лечение алкогольной зависимости: почему сила воли здесь ни при чём` |
| Slug | `nazvanie-stati` |
| URL | `http://shpigovsky.test/blog/nazvanie-stati/` |
| Status | `publish` |
| Featured image before | none (`_thumbnail_id` empty / `0`) |
| Blog/ACF image meta before | no ACF image fields; article text/meta only |
| Broken image URL/path | `http://shpigovsky.test/wp-content/themes/shpigovsky/assets/images/blog-no-photo.svg` on Home card, Blog archive card, and single hero (HTTP 200 SVG placeholder — not thematic; visually “missing” vs original demo) |
| Broken image source file/helper | `shpigovsky_get_article_hero_image()` / `shpigovsky_build_blog_archive_card_args()` in `inc/blog-helpers.php` → featured empty → `shpigovsky_get_blog_archive_card_fallback_image()` → `shpigovsky_get_blog_no_photo_image()` |

**Root cause:** E26D seeded the demo with `theme_asset_fallback_no_upload` (documented thematic file `article-alcohol-dependence.webp`, no Media Library attachment). After E35, fallback became the global blog no-photo, so post `#750` without featured image lost its thematic image.

## 4. Original image discovery

| Candidate | Path | Exists | Evidence | Decision |
|---|---|---|---|---|
| `article-alcohol-dependence.webp` | Runtime: `wp-content/themes/shpigovsky/assets/img/content/home-articles/article-alcohol-dependence.webp` | YES | E26D report: featured strategy = this file; home-articles asset name; SHA256 `3CA88A61…A709D3` matches source + runtime | **SELECTED** |
| Same file | Source: `WORDPRESS/theme/shpigovsky/assets/img/content/home-articles/article-alcohol-dependence.webp` | YES | Hash match with runtime | corroborating |
| `blog-article-inline-0N.webp` | `assets/img/content/blog-article/` | YES | Inline body images only | rejected (not card/hero thematic) |
| `article-bos-therapy.webp` / `article-yoga-therapy.webp` | `home-articles/` | YES | Other home demo cards | rejected |
| Media Library prior attachment | search by filename | NO | empty before FIX01 | N/A |

## 5. Media Library binding

| Item | Value |
|---|---|
| Attachment action | created |
| Attachment ID | `1106` |
| Attachment URL | `http://shpigovsky.test/wp-content/uploads/2026/05/article-alcohol-dependence.webp` |
| File path | `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\wp-content\uploads\2026\05\article-alcohol-dependence.webp` |
| Alt/title | title + alt: `Лечение алкогольной зависимости` |
| Result | PASS (file on disk; SHA256 matches theme original; WP generated large `…-763x1024.webp`) |

## 6. Post image binding

| Field/meta | Before | After | Result |
|---|---|---|---|
| Featured image | `0` | `1106` | PASS |
| Blog hero/card image field if any | none | none (templates use featured) | N/A — featured sufficient |
| Stale broken image meta | N/A (no stale attachment meta; SVG was helper fallback) | unchanged helper logic | PASS — no template change needed |

**E35 demos untouched:** posts `1101`–`1105` still featured `1100` (`blog-no-photo-placeholder.png`).

**DB writes:** 4 (sideload attachment + title update + alt meta + `set_post_thumbnail`).

## 7. Frontend validation

| Page | Check | Expected | Actual | Result |
|---|---|---|---|---|
| Target single | hero image | thematic image 200 | `…/article-alcohol-dependence-763x1024.webp` HTTP 200 | PASS |
| Home | article card image | thematic image 200 | same large URL HTTP 200 on `nazvanie-stati` card | PASS |
| Blog archive | article card image | thematic image 200 | same large URL HTTP 200 | PASS |
| Home/new demo posts | placeholder | blog no-photo | 5/5 cards use `blog-no-photo-placeholder-1024x683.png` | PASS |
| Blog/new demo posts | placeholder | blog no-photo | 5 placeholder refs on `/blog/` | PASS |
| Home slider | dots / no arrows | Swiper + pagination, no arrows | `data-articles-slider` + `data-articles-pagination`; no `swiper-button-prev/next` | PASS |

## 8. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | no fatal |
| `/blog/` | 200 | PASS | no fatal |
| `/blog/nazvanie-stati/` | 200 | PASS | thematic hero |
| `/blog/yoga-v-terapii-abstinentnyy-sindrom/` | 200 | PASS | E35 demo |
| `/blog/bos-terapiya-trenirovka-zon-mozga/` | 200 | PASS | E35 demo |
| `/blog/genotipirovanie-pri-zavisimostyah/` | 200 | PASS | E35 demo |
| `/blog/kak-prohodit-pervaya-konsultatsiya/` | 200 | PASS | E35 demo |
| `/blog/sryvy-i-retsidivy-signal-k-korrektirovke/` | 200 | PASS | E35 demo |
| `/specyalisty/` | 200 | PASS | |
| `/uslugi/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | |

## 9. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| — | — | — | — | **NO SOURCE FILE CHANGES** |

This fix was DB/Media Library only. No CSS/JS/template edits. (Foreign WIP already present under theme source tree was **not** touched.)

## 10. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | — |
| Commit skipped reason | Foreign monorepo WIP; unpushed commits on branch; DB/media changes are runtime-only; task forbids git reconciliation / unsafe commit |
| Push attempted | NO |

**Git classification (`git status --short`):**

| Class | Notes |
|---|---|
| Intended FP-0002 changes | this report file under `REPORTS/` (to be created) |
| Runtime-only | WP DB (`mars_wp_fp0002`); uploads `2026/05/article-alcohol-dependence*.webp`; attachment `#1106`; featured on post `#750` |
| DB changes | YES (4 writes) |
| Media/uploads changes | YES |
| Foreign WIP | large unrelated tree (MetaBOT, OCPilot, other FP reports, theme M files from prior waves) — ignored |

## 11. Final verdict

**PASS**

V9-06E35-FIX01 Alcohol article image restore:
COMPLETE

Original thematic image found:
PASS

Media Library binding:
PASS

Post image restored:
PASS

Home article image:
PASS

Blog archive image:
PASS

Single hero image:
PASS

New E35 placeholders preserved:
PASS

Regression:
PASS

Git commit:
SKIPPED

No foreign project work:
PASS

Recommended next phase:
CREATE_OPERATOR_REVIEW_CHECKLIST

## 12. Recommended next action

CREATE_OPERATOR_REVIEW_CHECKLIST

## 13. Final safety statement

Target folder:
X:\AI MARS

V9-06E35-FIX01 Alcohol article image restore performed:
YES

DB writes:
4

Source changes:
NO

Runtime delivery:
YES

WordPress changes:
YES

Media Library changes:
YES

Backup created:
YES

Git mutation:
NO

Git commit:
NO

Git push:
NO

Reset:
NO

Rebase:
NO

Stash:
NO

Cleanup:
NO

Foreign project work:
NO

FP-0002 product contaminated:
NO

WPilot confused with OCPilot:
NO

Secrets committed:
0
