# REPORT — SITE-002 Blog SEO URL Routing Fix 01

**Operation ID:** `SITE-002-PROD-BLOG-SEO-URL-ROUTING-FIX-01`  
**OCPilot Run:** **4.278**  
**Date:** 2026-07-16  
**Environment:** PRODUCTION (`https://bzpm.ru/`)  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** untouched  

**Verdict:** `SITE-002 BLOG SEO URL ROUTING FIX COMPLETE — POST SEO URL WORKS`

---

## 1. Scope

Diagnose why blog post 13 and `/blog/news` returned SEO URL 404 while technical route URLs returned 200; apply minimal safe fix; verify no product/category regression.

## 2. Operator context

After Run 4.277 the article looked correct on the route URL, but SEO URL and `/blog/news` were 404. This operation fixed routing (not article content).

## 3. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority worktree | `X:\AI MARS STORAGE\git-sync-e01\repo` |
| Authority HEAD | `f54cfe02` (= `origin/mars/canonical-post-recovery`) |
| Dirty main | dirty (foreign WIP) — **read-only only** |
| Staged changes (authority) | none |

Evidence: Storage `preflight/`.

## 4. HTTP before

| URL | Status |
|-----|--------|
| `/` | 200 |
| `/blog` | 200 |
| `/blog/news` | **404** |
| route `blog/post&blog_post_id=13` | **200** |
| SEO post 13 | **404** |
| older post SEO (`blog_post_id=12`) | **404** |
| `/stoly` | 200 |
| `/contact` | 200 |
| `/sitemap.xml` | 200 |

## 5. Blog routing discovery

Custom blog (`CUSTOM_BLOG`):

| URL | Intended |
|-----|----------|
| `/blog` | `blog/category` |
| `/blog/news` | `blog_category_id=1` |
| `/blog/news/{slug}` | `blog_post_id=N` |

**Critical:** `system/config/catalog.php` loads **`startup/seo_url` only**. Setting `config_seo_url_type=seo_pro` is not wired. `seo_pro.php` is blog-aware but **not executed**.

## 6. SEO URL DB audit

| Row | query | keyword |
|-----|-------|---------|
| 28673 | `blog_post_id=13` | `blog/news/proizvoditelnost-truda-rck-altayskiy-kray-2026` |
| 1246 | `blog_category_id=1` | `blog/news` |
| 1244 | `blog/category` | `blog` |

Post 13 active, category 1, date_added `2026-07-16 03:00:00`. **DB correct — no DB mutation.**

## 7. Root cause

**`SEO_REWRITE_DOES_NOT_SUPPORT_BLOG_POST_QUERY`**

Active `seo_url.php` decodes segment-by-segment. Blog keywords are stored as **full paths** (`blog/news/...`). After matching `blog`, segment `news` misses → 404. Same for all multi-segment blog URLs (not only post 13).

## 8. Fix plan

Minimal patch to `catalog/controller/startup/seo_url.php`:

1. Full-path keyword decode for multi-segment `blog_post_id` / `blog_category_id`
2. Rewrite support for those keys
3. Guard against double prefix `/blog/blog/news` when both `route` and `blog_category_id` rewrite

No switch to `seo_pro` (preserves Lari `site002CanonicalCategoryPath` in seo_url).

## 9. DB mutations

**0** — rows already correct.

## 10. Source patch

| File | Action |
|------|--------|
| `/public_html/catalog/controller/startup/seo_url.php` | FTP overwrite (verified SHA256) |

Repo mirror: `tools/seo_url-site-002-prod-blog-seo-url-routing-fix-01.php`

## 11. Cache actions

- No OCMOD startup layer for this file
- Cleared any `cache.seo_pro*` if present
- Twig cache not required

## 12. HTTP after

| URL | Status |
|-----|--------|
| `/` | 200 |
| `/blog` | 200 |
| `/blog/news` | **200** |
| `/blog/info` | **200** |
| route post 13 | **200** |
| SEO post 13 | **200** |
| older post SEO | **200** |
| `/stoly` | 200 |
| `/katalog/stoly` | 200 |
| `/shkafy-i-lari/lari` | 200 |
| `/contact` | 200 |
| `/sitemap.xml` | 200 |
| Public `БЗПМ` | **0** |

## 13. Regression check

| Check | Result |
|-------|--------|
| Blog links from home / blog / news / post 13 | **0 broken** |
| Product/category/Lari SEO | unchanged 200 |
| Route URL still works | yes |

## 14. Production mutation summary

| Item | Count |
|------|-------|
| FTP files changed | **1** (`seo_url.php`) |
| DB rows changed | **0** |
| Admin saves | **0** |
| Import runs | **0** |
| Scheduler/monitor changes | **0** |
| Form/mail changes | **0** |
| Dirty main changes | **0** |

## 15. DB mutation summary

None.

## 16. FTP mutation summary

1 file uploaded and byte-verified: `catalog/controller/startup/seo_url.php`.

## 17. Git/worktree summary

Authority worktree used for docs/tools commit + push. Dirty main not mutated.

## 18. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-BLOG-SEO-URL-ROUTING-FIX-01\`

## 19. SAFE UNKNOWN / blockers

- Why `config_seo_url_type=seo_pro` is not wired into `action_pre_action` (historical misconfig vs intentional) — not changed this wave.
- Optional future: wire seo_pro safely with Lari decode parity (out of scope).

## 20. Final verdict

| Area | Classification |
|------|----------------|
| Post 13 SEO URL | `POST_13_SEO_URL_FIXED` |
| `/blog/news` | `BLOG_NEWS_ROUTE_FIXED` |
| Overall | **`SITE-002 BLOG SEO URL ROUTING FIX COMPLETE — POST SEO URL WORKS`** |

## 21. Next recommendation

- Durable: keep blog SEO keywords as full paths (`blog/news/{slug}`); ensure `seo_url.php` blog bridge remains when patching SEO startup.
- Optional follow-up charter: evaluate aligning `action_pre_action` with `config_seo_url_type=seo_pro` without regressing Lari category_path decode.
- Optional: include blog posts in Google sitemap (currently excluded by design).
