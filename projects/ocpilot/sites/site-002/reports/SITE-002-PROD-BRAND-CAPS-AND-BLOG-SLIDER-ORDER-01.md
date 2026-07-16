# REPORT — SITE-002 Brand Caps and Blog Slider Order 01

**Operation ID:** `SITE-002-PROD-BRAND-CAPS-AND-BLOG-SLIDER-ORDER-01`  
**OCPilot Run:** **4.276**  
**Date:** 2026-07-16  
**Site:** https://bzpm.ru/ (SITE-002 Production)

---

## 1. Scope

Controlled Production patch for:

- **Task A:** Company full-name capitalization — `Завод` uppercase in approved full-name phrases; `ЗПМ` unchanged; no blind global replace.
- **Task B:** Blog article card sliders — newest-first (`date_added DESC`), max **24**, publish gate, real meta including reading time; no hardcoded fake meta.

**Allowed mutations:** exact DB text rows; exact blog slider PHP sources; exact information controller brand strings; OC modification/cache clear.  
**Forbidden (honored):** import, scheduler, monitor baseline, forms/mail, dirty main mutation.

---

## 2. Operator request

Operator approved capitalization sweep for full company name variants and blog slider order/limit/meta fix across all article card sliders (`.zpm-rel-articles-card__meta`, related slider, home slider).

Target article: post **13** — `/blog/news/proizvoditelnost-truda-rck-altayskiy-kray-2026`.

---

## 3. Preflight

| Check | Result |
|-------|--------|
| Authority worktree | `X:\AI MARS STORAGE\git-sync-e01\repo` |
| Volume | `AI WS` (X:) |
| Branch | `site-002-git-authority-realign-after-wave-e` |
| HEAD | `adb230fd` |
| origin/mars/canonical-post-recovery | `adb230fd` (aligned) |
| Dirty main | read-only; not mutated |
| Foreign WIP in authority | 3 untracked tools (not staged) |

Evidence: Storage `preflight/authority-git.txt`, `preflight/dirty-main-readonly.txt`.

---

## 4. Brand capitalization audit

**Classification:** `BRAND_CAPS_HITS_FOUND`

DB audit across `oc_blog_posts`, `oc_information_description`, `oc_category_description`, `oc_product_description`.

| Area | Hits | Notes |
|------|------|-------|
| Post 13 | 5 fields | title, content, short_description, meta_title, meta_description — lowercase `завод` in full-name phrases |
| Info page 12 | meta_title | `завод пищевого машиностроения` → `Завод пищевого машиностроения` |
| Info page 15 | meta_keyword | same nominative fix |
| Other rows | IGNORE | legal ALL-CAPS `ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ`; already-correct `Завод`; generic standalone `завод` |

Source audit: `contact.php`, `about.php` controllers had hardcoded lowercase genitive/nominative in `setDescription`.

Evidence: `brand-audit/db-brand-hits.csv`, `brand-audit/source-brand-hits.csv`, `brand-audit/post-13-brand-hits.md`.

---

## 5. Brand capitalization patch plan

| Row | Action |
|-----|--------|
| `oc_blog_posts` id=13 (5 fields) | `REPLACE_SAFE` |
| `oc_information_description` id=12 meta_title | `REPLACE_SAFE` |
| `oc_information_description` id=15 meta_keyword | `REPLACE_SAFE` |
| Legal-name ALL-CAPS blocks | `IGNORE_NOT_COMPANY_NAME` |
| Generic `завод` without full phrase | `IGNORE_NOT_COMPANY_NAME` |

Evidence: `brand-patch-plan/brand-replacements-plan.csv`.

---

## 6. Brand capitalization mutations

**Classification:** `BRAND_CAPS_FIXED`

### DB updates (7 field writes, 3 logical rows)

- `oc_blog_posts` **13**: title, content, short_description, meta_title, meta_description
- `oc_information_description` **12**: meta_title
- `oc_information_description` **15**: meta_keyword

### FTP source updates (2 controllers)

- `catalog/controller/information/contact.php` — meta description genitive fix
- `catalog/controller/information/about.php` — meta description nominative fix

Modification cache at `/home/a/assum/bzpm.ru/storage/modification/` held stale `contact.php` override; cleared via SSH (correct path; initial clear used wrong `assum_zpmmars` path).

Evidence: `brand-db-backup/`, `brand-apply/brand-update-result.txt`, `source-after/brand-source-after/`.

---

## 7. Brand public verification

| URL | Status | БЗПМ | Bad full-name patterns | Good `Завод` hits |
|-----|--------|------|------------------------|-------------------|
| post 13 | 200 | 0 | 0 | 7 |
| `/blog` | 200 | 0 | 0 | 6 |
| `/` | 200 | 0 | 0 | 3 |
| `/contact` | 200 | 0 | 0 | 1 (after mod cache clear) |

Post 13 title on live: **«Барнаульский Завод пищевого машиностроения участвует…»** — confirmed.

Evidence: `frontend-verification/brand-public-check.csv`.

---

## 8. Blog slider discovery

**Classification:** `ORDER_WRONG` + `LIMIT_WRONG` + `READING_TIME_MISSING` (home)

| Slider | Template | Controller | Model method | Issues |
|--------|----------|------------|--------------|--------|
| Home `relarticles` | `blog/other_news.twig` | `common/home.php` | `getOtherPosts(1,0,6)` | RAND/category filter/limit 6; no reading_time |
| Blog category footer | same | `blog/category.php` | `getOtherPosts($cat,0,6)` | RAND/limit 6 |
| Blog post related | same | `blog/post.php` | `getOtherPosts($cat,$id,6)` | RAND/category filter/limit 6 |
| Twig meta | `other_news.twig` | — | — | **OK** since Run 4.273 (`{{ item.views }}`, `reading_time_text`) |

`getPosts()` list/detail already: `ORDER BY date_added DESC`, publish gate `date_added <= NOW()`.

Evidence: `blog-slider-discovery/slider-source-files.md`, `blog-slider-discovery/current-order-limit-analysis.md`.

---

## 9. Blog slider patch

**Classification:** `BLOG_SLIDER_ORDER_LIMIT_META_FIXED`

### Model (`catalog/model/blog/blog.php`)

- Added `getSliderPosts($exclude_post_id = 0, $limit = 24)` — all published posts, `ORDER BY p.date_added DESC`, `active=1`, `date_added <= NOW()`, cap 24.
- `getOtherPosts()` fallback: `ORDER BY RAND()` → `ORDER BY p.date_added DESC` (unused by sliders after patch).

### Controllers

| File | Change |
|------|--------|
| `common/home.php` | `getSliderPosts(0, 24)`; added `formatReadingTimeText()`; pass `reading_time_text` |
| `blog/post.php` | `getSliderPosts($post_id, 24)` |
| `blog/category.php` | `getSliderPosts(0, 24)` |

### Regression during deploy

Initial `home.php` upload called `formatReadingTimeText()` without method → **Fatal error** on `/`. Fixed immediately: method added, re-uploaded, cache cleared.

Evidence: `source-after/slider-source-after/`, `ftp-apply/uploaded-files.txt`.

---

## 10. Frontend verification

| Page | Slider cards | Newest first | Reading time in meta | Hardcoded `3` |
|------|-------------|--------------|----------------------|---------------|
| `/` | 6 (all published) | yes — post 13 first | yes | no |
| `/blog/news` | 6 | yes | yes | no |
| post 13 | 5 (excludes self) | yes | yes | no |

DB has **6** published posts total; limit 24 satisfied (all shown). Publish gate confirmed via model SQL.

Evidence: `frontend-verification/slider-order-evidence.json`, `frontend-verification/blog-slider-check.csv`.

---

## 11. Regression check

| URL | Status | OK |
|-----|--------|-----|
| `/` | 200 | yes |
| `/blog` | 200 | yes |
| `/blog/news` | 200 | yes |
| post 13 | 200 | yes |
| `/contact` | 200 | yes |
| `/kontakty` | 404 | yes (accepted) |
| `/sitemap.xml` | 200 | yes |

Import: **0** runs. Scheduler/monitor/forms/mail: **unchanged**.

Evidence: `regression/site-regression.csv`.

---

## 12. Final decision

| Area | Classification |
|------|----------------|
| Brand caps | `BRAND_CAPS_FIXED` |
| Blog slider | `BLOG_SLIDER_ORDER_LIMIT_META_FIXED` |

---

## 13. Production mutation summary

| Type | Count / list |
|------|----------------|
| FTP files changed | **6** — `catalog/model/blog/blog.php`, `catalog/controller/common/home.php`, `catalog/controller/blog/post.php`, `catalog/controller/blog/category.php`, `catalog/controller/information/contact.php`, `catalog/controller/information/about.php` |
| DB writes | **7 fields** across **3 rows** (post 13 + info 12 + info 15) |
| Admin saves | 0 |
| Import runs | 0 |
| Scheduler changes | 0 |
| Monitor changes | 0 |
| Form/mail changes | 0 |
| Dirty main changes | 0 |

---

## 14. DB mutation summary

```text
oc_blog_posts id=13: title, content, short_description, meta_title, meta_description
oc_information_description id=12 language_id=1: meta_title
oc_information_description id=15 language_id=1: meta_keyword
```

---

## 15. FTP mutation summary

All paths under `/public_html/catalog/`. `other_news.twig` unchanged (already correct from Run 4.273). OC modification + cache cleared at `/home/a/assum/bzpm.ru/storage/modification/` and `public_html/system/storage/cache/`.

---

## 16. Git/worktree summary

Authority worktree commit: source mirrors in `projects/ocpilot/sites/site-002/tools/`, operation script, report, doc updates. Storage artifacts **not** committed.

---

## 17. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-BRAND-CAPS-AND-BLOG-SLIDER-ORDER-01\`

---

## 18. SAFE UNKNOWN / blockers

- None blocking. Transient home fatal error during first `home.php` upload — **resolved same session**.
- OC modification cache path on Beget: `/home/a/assum/bzpm.ru/storage/modification/` (not `assum_zpmmars`); documented in cache log.

---

## 19. Final verdict

**SITE-002 BRAND CAPS AND BLOG SLIDER COMPLETE — CAPS FIXED, SLIDER ORDER LIMIT META FIXED**

---

## 20. Next recommendation

- Durable rule: in public copy, full company phrase uses **`Завод`** (with inflection: `Завода`, `Барнаульского Завода`, etc.); short form **`ЗПМ`** unchanged.
- After PHP controller deploys, always clear **`/home/a/assum/bzpm.ru/storage/modification/`** — stale overrides can mask FTP updates.
- When blog post count exceeds 24, re-verify slider card count on home and blog category pages.
