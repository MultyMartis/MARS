# REPORT — SITE-002 Blog RCK Logo and Title Image 01

**Operation ID:** `SITE-002-PROD-BLOG-RCK-LOGO-AND-TITLE-IMAGE-01`  
**OCPilot Run:** **4.271**  
**Date:** 2026-07-15  
**Environment:** PRODUCTION (`https://bzpm.ru/`)  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** untouched  

**Verdict:** `SITE-002 BLOG RCK LOGO AND TITLE IMAGE COMPLETE — POST 13 PACKAGED FOR SCHEDULED PUBLISH`

---

## 1. Scope

Finish packaging of existing scheduled blog post **id=13** (no new article):

1. Attach operator-uploaded RCK logo.
2. Generate and attach a relevant hero/title image (Composer-only).
3. Keep scheduled publish time, slug, text intent, and autopublish gate unchanged.

## 2. Blog image architecture (verified)

| Item | Authority |
|------|-----------|
| Classification | `CUSTOM_BLOG` |
| Table | `oc_blog_posts` |
| Main preview / hero field | `oc_blog_posts.image` → relative OpenCart path `catalog/blog/...` |
| Physical upload dir | `/public_html/image/catalog/blog/` |
| Post detail crop | `resizeCrop(..., 1400, 700)` in `catalog/controller/blog/post.php` |
| List / related crop | `resizeCrop(..., 600, 400)` in category/related loops |
| Body media | HTML `<img>` inside `content` (no separate gallery table) |
| Existing examples | `catalog/blog/news-01.jpg`, `news-02.jpg`, `seo-info-0N.jpg` |

**Implementation path chosen:**

- Hero → `oc_blog_posts.image`
- RCK logo → inserted into existing caption block in `content`

## 3. Incoming logo

| Item | Value |
|------|-------|
| Intake folder | `.../incoming/SITE-002-PROD-BLOG-SCHEDULED-NEWS-RCK-PRODUCTIVITY-01/` |
| Exact filename | **`logo-rck.png`** |
| Size | 2 169 354 bytes |
| Format | PNG RGBA 1536×1024 |
| SHA256 | `20fb59451e0f583f025ffb5db13c3db4efd02eb7e615f226f14fbc435d83d795` |

## 4. Generated hero / title image

| Item | Value |
|------|-------|
| Generation | Cursor Composer `GenerateImage` — **COMPOSER_ONLY_NO_API** |
| Composer source | `rck-productivity-hero-zpm-2026.png` |
| Normalized deliverable | **`rck-productivity-hero-zpm-2026.jpg`** (1400×700, JPEG q90) |
| Concept | Industrial productivity / stainless workshop / specialists reviewing process metrics |
| Remote | `/public_html/image/catalog/blog/rck-productivity-hero-zpm-2026.jpg` |
| DB path | `catalog/blog/rck-productivity-hero-zpm-2026.jpg` |
| SHA256 | `bb541b23e0693d5d5166f21c2ab9bd6cf418f6b72af483fc871e009fc412af92` |

## 5. Where images are attached

| Asset | Attachment point |
|-------|------------------|
| Hero / title image | `oc_blog_posts.image` for **post_id 13** |
| RCK logo | Body HTML after RCK paragraph: `<img src="/image/catalog/blog/rck-logo-altay-2026.png" ...>` + existing caption |

Remote logo name: **`rck-logo-altay-2026.png`** (bytes identical to intake `logo-rck.png`).

## 6. Post 13 invariants (unchanged)

| Field | Value |
|-------|--------|
| `post_id` | **13** |
| `date_added` | **`2026-07-16 03:00:00`** (Barnaul 07:00) |
| SEO keyword | `blog/news/proizvoditelnost-truda-rck-altayskiy-kray-2026` |
| SEO row | `seo_url_id=28673` |
| `active` | 1 |
| Autopublish gate | still `active='1' AND date_added <= NOW()` in catalog blog model |
| Public `БЗПМ` | **0** |

Content length: 1940 → 2103 (logo markup only).

## 7. Pre-publish verification

Checked after image attach, before Barnaul publish time:

| URL | Result |
|-----|--------|
| `/blog` | 200; slug/title **absent** |
| `/blog/news` | 200; slug/title **absent** |
| article SEO URL | **404** |
| `blog/post&blog_post_id=13` | **404** |
| `/contact` | 200 |
| `/sitemap.xml` | 200; slug absent |
| hero asset URL | **200** |
| logo asset URL | **200** |
| DB gate `date_added <= NOW()` for id 13 | **false** |
| Public `БЗПМ` on sanity pages | **0** |

## 8. Production mutation summary

| Channel | Count / note |
|---------|----------------|
| FTP writes | **2** images under `image/catalog/blog/` |
| DB writes | **1** scoped `UPDATE oc_blog_posts` WHERE `id=13` (+ date/active/image guards) |
| Schema changes | **0** |
| Autopublish model | **0** (untouched) |
| New article / SEO row | **0** |
| Forms / mail / import / monitor / scheduler | **0** |

## 9. Changed files (repo / Storage)

### Storage (operation artifacts)

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-BLOG-RCK-LOGO-AND-TITLE-IMAGE-01\`

Key paths:

- `image-input/`, `image-processed/`
- `ftp-upload/image-upload-result.json`
- `article-apply/content-after.html`, `apply-method.md`
- `db-backup/post13-before.sqlish.tsv`
- `verification/http-verify.json`
- `logs/prepare-and-apply-images.py`, `logs/apply-summary.json`
- `reports/SITE-002-PROD-BLOG-RCK-LOGO-AND-TITLE-IMAGE-01.md`

### Repo (authority worktree)

- `projects/ocpilot/sites/site-002/reports/SITE-002-PROD-BLOG-RCK-LOGO-AND-TITLE-IMAGE-01.md`
- `projects/ocpilot/sites/site-002/tools/site-002-prod-blog-rck-logo-and-title-image-01.py`
- `projects/ocpilot/sites/site-002/tools/README.md` (index line for Run 4.271)

## 10. Git commit + push status

See closeout after authority commit/push.

## 11. Final verdict

`SITE-002 BLOG RCK LOGO AND TITLE IMAGE COMPLETE — POST 13 PACKAGED FOR SCHEDULED PUBLISH`

Post **13** remains scheduled for **16.07.2026 07:00 Barnaul**, now has a hero image and RCK logo, stays hidden until the existing autopublish gate fires.
