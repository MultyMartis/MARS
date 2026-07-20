# REPORT — SITE-002 Production Regression Hotfix 01

**Operation ID:** `SITE-002-PROD-REGRESSION-HOTFIX-01`  
**OCPilot Run:** **4.282**  
**Date:** 2026-07-20  
**Environment:** PRODUCTION (`https://bzpm.ru/`)  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** untouched (read-only inspect only)

**Verdict:** `SITE-002 PROD REGRESSION HOTFIX COMPLETE — PRODUCTS RESTORED AND NOTICES REMOVED`

---

## 1. Scope

Urgent production regression diagnostic and minimal hotfix: restore product pages opened from parent catalog listings; remove visible `has_children` PHP notices; preserve blog SEO if safe.

## 2. Operator incident

Operator reported:

1. Public PHP notices: `Undefined index: has_children` in `header.php` lines 201/217.
2. Product pages show «Товар не найден» (including older products).
3. Admin top-bar cache-clean button disappeared.
4. Latest prior op: Run 4.281 onboarding 05 (meta/allowlist only, no FTP).

Suspected: Run 4.278 `seo_url.php` blog full-path patch.

## 3. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority worktree | `X:\AI MARS STORAGE\git-sync-e01\repo` |
| Authority HEAD | `1be9dd9c` (= `origin/mars/canonical-post-recovery`) |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Staged | empty |
| Untracked tools (authority) | 3 pre-existing — **not committed** |
| Dirty main `X:\AI MARS` | foreign WIP — **read-only**; **0 mutations** |

Evidence: Storage `preflight/`.

## 4. Incident confirmation

| Check | Before |
|-------|--------|
| `has_children` notices on `/`, categories, blog, contact | **YES** (public HTML; `config_error_display=1`) |
| Parent-path product URL `/…/stoly/{product-slug}` | **200 + «Товар не найден»** |
| Leaf-path product URL | **200 + cart OK** |
| Bare product slug / `product_id` route | **200 + cart OK** |
| Blog SEO + route | **200** |
| `/stoly` product hrefs | incomplete path (missing leaf category) |

## 5. SEO URL root cause

**Classification: `SEO_REGRESSION_CONFIRMED`** (mechanism ≠ blog keyword collision).

Ruled out: blog full-path decode consuming product keywords (product keywords are single-segment; multi-segment SEO rows are blog-only). Production `seo_url.php` matched Run 4.278 mirror byte-for-byte before hotfix.

Confirmed chain:

1. Parent PLP builds `path=<parent>&product_id=N`.
2. Rewrite emits `/parent-cats/product-slug`.
3. Decode sets incomplete `path` + `product_id`.
4. `product.php` `checkProductCategory()` requires direct `oc_product_to_category` membership in path ids.
5. Product is only in leaf category → `$product_info` cleared → «Товар не найден».

Matches operator browsing parent categories and clicking any product.

## 6. Header notice root cause

**Classification: `HEADER_NOTICE_CONFIRMED`**

`prepareMegamenuCategories()` sets `has_children` on roots only; nested children / empty roots may omit the key. `header.php` read `$c['has_children']` / `$c1['has_children']` bare. Onboarding 05 likely refreshed megamenu cache shapes; `config_error_display=1` made notices public.

## 7. Hotfix decision

| Issue | Decision |
|-------|----------|
| Products | **Option A** — keep blog; normalize product `path` in `seo_url.php` when membership fails |
| Header | Safe `!empty(...['has_children'])` |
| Blog rollback | **Rejected** (unnecessary) |
| Admin cache button | Observe only → **SAFE UNKNOWN** |

## 8. Production backup

| File | SHA256 (before) |
|------|-----------------|
| `seo_url.php` | `9c2c297d17e99c35a3c624ff03f7e5d26beb20d376467c280aaa2b5e41685273` |
| `header.php` | `3fdf469c75c5de662681f85a7c15aeee67a2f75d2fda381db6e06ffdceb8b338` |

Storage: `production-backup/`.

## 9. Source patch

| File | Change |
|------|--------|
| `seo_url.php` | After path canonicalization: if `product_id` set and path lacks direct product category, rebuild path from `product_to_category` + `category_path` |
| `header.php` | `!empty($c['has_children'])` / `!empty($c1['has_children'])` |

Authority mirrors:

- `tools/seo_url-site-002-prod-regression-hotfix-01.php`
- `tools/header-site-002-prod-regression-hotfix-01.php`
- `tools/seo_url-site-002-prod-blog-seo-url-routing-fix-01.php` (updated to post-hotfix)

Remote `php -l`: `seo_url.php` OK; `header.php` CLI “Errors parsing” also on **pre-hotfix** backup (PHP 5.6 CLI quirk with existing UTF-8 content) — not introduced by this patch; live HTTP OK.

## 10. FTP apply

| Remote | SHA256 (after) | Verified |
|--------|----------------|----------|
| `/public_html/catalog/controller/startup/seo_url.php` | `545cfeb6eaef46e73f14c001eac6912fe7e5bc0006a3cdb1da2311df165fceeb` | yes |
| `/public_html/catalog/controller/common/header.php` | `d8ce4f5c849c2427b7710c559c6a8f07b7f87a5686fe48df16a517fb77d92323` | yes |

## 11. Cache actions

- `storage/modification` compiled files cleared.
- `storage/cache/cache.*` cleared (includes megamenu `cat-list-header` materialization path).

## 12. HTTP after verification

| URL class | Result |
|-----------|--------|
| Previously failing parent-path product | **200**, NF=no, cart=yes, notices=no |
| Leaf / bare / route products | **200**, OK |
| `/`, `/stoly`, premium-3, contact, about | **200**, notices=no |
| Blog hub/news/post13 SEO+route | **200**, notices=no |
| `/kontakty` | **404** (pre-existing accepted policy) |
| Sitemap | **200** |
| Public `БЗПМ` | **0** |

## 13. Admin cache button observation

**ADMIN_CACHE_BUTTON_SAFE_UNKNOWN** — admin UI login not performed in this wave. Operator should manually check top-bar cache-clean plugin after public fix.

## 14. Regression check

DB/import/scheduler/baseline/forms/dirty-main: **0**. Blog SEO preserved. No public `БЗПМ`.

## 15. Production mutation summary

- FTP files changed: **2**
- DB writes: **0**
- Admin saves: **0**
- Import runs: **0**
- Manual monitor runs: **0**
- Scheduler changes: **0**
- Monitor baseline changes: **0**
- Form/mail changes: **0**
- Cache clears: **yes** (`storage/modification`, `storage/cache/cache.*`)
- Dirty main changes: **0**

## 16. Rollback plan

Restore `production-backup/seo_url.php` + `header.php` via FTP; clear modification + cache; re-verify parent-path product + notices + blog.

## 17. Git/worktree summary

- Authority: patch mirrors + report + docs committed/pushed to `mars/canonical-post-recovery` (this run).
- Dirty main: untouched.

## 18. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\hotfixes\SITE-002-PROD-REGRESSION-HOTFIX-01\`

## 19. SAFE UNKNOWN / blockers

- Admin cache-clean button visibility: **SAFE UNKNOWN** (manual operator check).
- Exact historical start date of parent-path product failure: **SAFE UNKNOWN** (likely longstanding interaction of parent PLP path + `checkProductCategory`; noticed as incident with visible notices).

## 20. Final verdict

**SITE-002 PROD REGRESSION HOTFIX COMPLETE — PRODUCTS RESTORED AND NOTICES REMOVED**

Classifications:

- Product pages: **PRODUCT_PAGES_RESTORED**
- Header notices: **HEADER_NOTICES_REMOVED**
- Blog SEO: **BLOG_SEO_PRESERVED**
- Admin cache button: **ADMIN_CACHE_BUTTON_SAFE_UNKNOWN**

## 21. Next recommendation

1. Operator: manually confirm admin cache-clean button.
2. Optional follow-up: harden PLP product link generation to use product leaf category path (reduces reliance on seo_url path rebuild).
3. Optional: set `has_children` on nested megamenu children in `prepareMegamenuCategories()` (defense in depth).
4. Continue deferred **`SITE-002-MONITOR-BASELINE-REFRESH-04`** when operator authorizes (not part of this incident).
