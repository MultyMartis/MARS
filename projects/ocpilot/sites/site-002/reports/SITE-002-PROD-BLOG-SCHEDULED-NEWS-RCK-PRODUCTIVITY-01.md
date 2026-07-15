# REPORT — SITE-002 Blog Scheduled News RCK Productivity 01

**Operation ID:** `SITE-002-PROD-BLOG-SCHEDULED-NEWS-RCK-PRODUCTIVITY-01`  
**OCPilot Run:** **4.270**  
**Date:** 2026-07-15  
**Environment:** PRODUCTION (`https://bzpm.ru/`)  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** untouched  

**Verdict:** `SITE-002 BLOG SCHEDULED NEWS COMPLETE — ARTICLE SCHEDULED FOR 2026-07-16 07:00 BARNAUL`

---

## 1. Scope

Create one scheduled ЗПМ news article about participation in the federal project «Производительность труда» with RCK Altai experts; schedule for **2026-07-16 07:00 Barnaul (UTC+7)**; verify pre-publish frontend hiding; add minimal autopublish if missing.

## 2. Operator approval

Operator approved the article text (title, teaser, body, SEO title/description, slug). Brand policy: public **ЗПМ**, forbid **БЗПМ**. Tone: participation / ongoing first stage / upcoming interim results — not completed claims.

## 3. Blog architecture discovery

**Classification:** `CUSTOM_BLOG`

| Item | Value |
|------|--------|
| Hub | `/blog` → `blog/category` |
| News list | `/blog/news` → `blog_category_id=1` |
| Article | `/blog/news/{slug}` → `blog_post_id=N` |
| Tables | `oc_blog_posts`, `oc_blog_themes` |
| Admin | `blog/posts`, `blog/themes` |
| Catalog model | `catalog/model/blog/blog.php` |
| Image dir | `image/catalog/blog/` (`catalog/blog/...` in DB) |
| Sitemap | Google sitemap **does not** include blog posts |

Evidence: Storage `deployments/.../blog-discovery/`.

## 4. Autopublish capability

**Classification (before patch):** `AUTOPUBLISH_NOT_SUPPORTED`

Frontend filtered only `active = '1'`. No date gate on list/detail/related. Admin shows all posts and can set «Дата» → `date_added`.

## 5. Image input/upload

**Status:** `IMAGE INPUT MISSING — OPERATOR MUST PLACE LOGO INTO INTAKE FOLDER`

- Intake `.../incoming/SITE-002-PROD-BLOG-SCHEDULED-NEWS-RCK-PRODUCTIVITY-01/` was empty
- `/mnt/data/2CjTf_mU.jpg` unavailable
- Article created **without** RCK logo file; caption text kept as italic note in body
- FTP image uploads: **0**

## 6. Article content

| Field | Value |
|-------|--------|
| `post_id` | **13** |
| SEO keyword | `blog/news/proizvoditelnost-truda-rck-altayskiy-kray-2026` |
| Public URL | https://bzpm.ru/blog/news/proizvoditelnost-truda-rck-altayskiy-kray-2026 |
| Category | `category_id=1` (Новости) |
| `active` | 1 |
| Title / teaser / body / SEO | approved text |
| Public `БЗПМ` in content | **0** |

## 7. Publication schedule and timezone handling

| Clock | Value |
|-------|--------|
| Target (Barnaul) | `2026-07-16 07:00:00 +07` |
| PHP / MySQL | `Europe/Moscow` (UTC+3); `NOW()` = UTC+3 |
| Stored `date_added` | **`2026-07-16 03:00:00`** (Moscow wall = Barnaul 07:00) |
| Gate | `date_added <= NOW()` in catalog blog model |

Frontend displays date as `d.m.Y` → **16.07.2026**.

## 8. Article creation method

Direct DB INSERT mirroring admin `ModelBlogBlog::addPost`:

1. `oc_blog_posts` row id **13**
2. `oc_seo_url` id **28673** (`blog_post_id=13` → keyword above)

Admin can open/edit the same row via `blog/posts`.

## 9. Autopublish patch decision

**Patched** production file:

`/public_html/catalog/model/blog/blog.php`

Change: `active = '1'` → `active = '1' AND date_added <= NOW()` in `getPost`, `getPosts`, `getTotalPosts`, `getOtherPosts`.

- Admin model unchanged (scheduled posts remain visible in admin)
- No schema change
- Sitemap unchanged (blog not listed)
- Repo mirror: `tools/catalog_model_blog_blog-site-002-prod-blog-scheduled-publish-01.php`
- Pre-patch backup in Storage `autopublish-patch-if-needed/backup-pre-patch-blog.php`

## 10. Admin verification

DB-backed (same tables admin reads):

- post **13** exists, `active=1`, `date_added=2026-07-16 03:00:00`
- SEO row present
- Content lengths: title 101, short 367, content 1940
- Meta title/description set

## 11. Frontend pre-publish verification

Checked before Barnaul publish time:

| URL | Result |
|-----|--------|
| `/blog` | 200; slug/title **absent** |
| `/blog/news` | 200; slug/title **absent** |
| article SEO URL | **404** |
| `blog/post&blog_post_id=13` | **404** |
| `sitemap.xml` | no slug (blog not in feed) |
| DB `date_added <= NOW()` for id 13 | **false** |
| Legacy post 8 still visible under gate | **true** |
| Public `БЗПМ` | **0** |

## 12. Sitemap/cache verification

- Blog not in Google sitemap (pre-existing) — no sitemap patch
- Attempted OC `cache.*` clear under discovered storage cache dirs (scoped)

## 13. Production mutation summary

| Channel | Count / note |
|---------|----------------|
| FTP writes | **1** code file (`catalog/model/blog/blog.php`); **0** images |
| DB writes | **1** `oc_blog_posts` + **1** `oc_seo_url` |
| Schema changes | **0** |
| Admin saves | **0** (DB insert method) |
| Import runs | **0** |
| Scheduler changes | **0** |
| Monitor changes | **0** |
| Form/mail changes | **0** |

## 14. DB mutation summary

- INSERT `oc_blog_posts` id=13  
- INSERT `oc_seo_url` id=28673  
- Pre-insert backup snapshot in Storage `db-backup/`

## 15. FTP mutation summary

- Uploaded patched `catalog/model/blog/blog.php` (hash-verified)
- Image upload skipped (missing input)

## 16. Git/worktree summary

- Authority HEAD before work: `32737c0e` (= `origin/mars/canonical-post-recovery`)
- Docs + PHP mirror + report committed/pushed from authority worktree (see closeout)
- Dirty main `X:\AI MARS`: **not mutated**

## 17. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-BLOG-SCHEDULED-NEWS-RCK-PRODUCTIVITY-01\`

## 18. SAFE UNKNOWN / blockers

- **IMAGE INPUT MISSING** — RCK logo not placed; article live without image asset
- Playwright/admin UI login browse not required for success (DB + HTTP verification sufficient)
- Exact post-publish HTTP confirmation awaits **2026-07-16 07:00 +07** (checklist in Storage `verification/postpublish-checklist.md`)

## 19. Final verdict

`SITE-002 BLOG SCHEDULED NEWS COMPLETE — ARTICLE SCHEDULED FOR 2026-07-16 07:00 BARNAUL`

## 20. Post-publish check recommendation

After **2026-07-16 07:00 Barnaul**, run Storage checklist: article URL 200, appears in `/blog` and `/blog/news`, meta OK, `БЗПМ`=0. Optionally upload RCK logo into intake and attach via admin or scoped DB/FTP update.
