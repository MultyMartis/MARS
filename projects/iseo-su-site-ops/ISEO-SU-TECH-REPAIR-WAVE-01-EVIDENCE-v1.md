# ISEO-SU TECH REPAIR WAVE 01 EVIDENCE v1

**Task ID:** `ISEO-SU-SITE-OPS-TECH-REPAIR-WAVE-01`  
**Date:** 2026-09-04  
**Status:** COMPLETE  
**Audit tip / origin start:** `5add8c2a`  
**Source audit:** TECH SEO RE-AUDIT 02 (contour `20260904-163451`)

---

## 1. Scope

IN SCOPE only:

1. Broken relative CSS on blog author pages (`/blog/author/css/...` and nested `/blog/author/libs/...`) — 6 broken CSS requests.
2. Broken `/img/logo.svg` → HTTP 404.

OUT OF SCOPE: canonical/title/meta/H1/alt/OG, sitemap, menu/navigation, content, forms, SEO backlog autofix.

---

## 2. Audit Findings

From `audits/tech-seo/ISEO-SU-TECH-SEO-REAUDIT-02-FINDINGS.csv`:

| Finding | Broken URL |
|---------|------------|
| CSS-BROKEN | `https://i-seo.su/blog/author/css/main.css` |
| CSS-BROKEN | `https://i-seo.su/blog/author/css/media.css` |
| CSS-BROKEN | `https://i-seo.su/blog/author/css/normalize.css` |
| CSS-BROKEN | `https://i-seo.su/blog/author/libs/fancybox/jquery.fancybox.min.css` |
| CSS-BROKEN | `https://i-seo.su/blog/author/libs/owl/owl.carousel.min.css` |
| CSS-BROKEN | `https://i-seo.su/blog/author/libs/owl/owl.theme.default.min.css` |
| IMG-BROKEN | `https://i-seo.su/img/logo.svg` |

Author slug sample from crawl: `/blog/author/{admin,denis,ilya,manager3,mars,olya}`.

---

## 3. Author CSS Root Cause

- `/blog/author/{slug}` is **not** a real WordPress author archive template.
- Live responses: **301 → `https://i-seo.su/`**; followed HTML is the **homepage** (`page-home.php`).
- Theme has **no** dedicated `author.php` authority for these URLs.
- Homepage stylesheets were linked as **document-relative** paths: `href="css/..."`, `href="libs/..."`.
- Crawlers resolving against the original request URL produced `/blog/author/css/...` and `/blog/author/libs/...` → **404**.
- Real assets already exist and return **200** at `/css/*` and `/libs/*`.
- **Do not** copy stylesheets under `/blog/author/css/`.

---

## 4. Author CSS Source Authority

| Field | Value |
|-------|--------|
| AUTHOR TEMPLATE | N/A (author URLs redirect to `/`) |
| CSS INCLUDE SOURCE | `production-source/theme/iseoblog/page-home.php` |
| REAL ASSET PATH | `/css/normalize.css`, `/css/main.css`, `/css/media.css`, `/libs/owl/*`, `/libs/fancybox/*` |

Bounded pattern scan: same relative CSS family is homepage-owned; blog post / category smoke after fix showed no relative CSS regression on sampled routes.

---

## 5. CSS Fix

Changed in `page-home.php` only:

- `href="css/..."` → `href="/css/..."`
- `href="libs/..."` → `href="/libs/..."`

One shared homepage template fixes all author-page crawl failures (because they land on homepage HTML).

---

## 6. Logo.svg Root Cause

| Field | Value |
|-------|--------|
| Live `/img/logo.svg` | HTTP **404** |
| Valid current logo | `/img/logo-intl.svg` → HTTP **200** |
| REFERENCE COUNT (live emitter) | 1 primary static file |
| SOURCE FILE(S) | `production-source/static-html/blog.html` (`src="img/logo.svg"`) |
| EXPECTED CORRECT PATH | `/img/logo-intl.svg` |

Stale/dead path; valid asset already in production. No redesign.

---

## 7. Logo Fix Decision

**MODEL A — STALE REFERENCE**

Retarget `blog.html` logo `src` to `/img/logo-intl.svg`.  
Do **not** invent or redraw `/img/logo.svg`.

Note: bare `/img/logo.svg` URL remains 404 by design (unused expected path after retarget). Live broken **references** after fix: **0**.

---

## 8. Production Backup

| Field | Value |
|-------|--------|
| Backup root | `X:\AI MARS\local\sites\iseo-su-production\_tech-repair-wave-01\20260904T155608Z\` |
| Timestamp | `20260904T155608Z` |
| `page-home.php` SHA-256 before | `6756424fdf8132481a14b4fadf3258d9ee78ed37a63b047adfe200f98d0deafd` |
| `blog.html` SHA-256 before | `a62ead5ed695c4456e4bd545bac545fd77f279e72f219e491341294f4a2498c1` |

Evidence tool JSON: `tools/_wave_tech_repair_01_deploy_validate.json`.

---

## 9. Deployment

| File | Remote path | Action | SHA-256 after | Remote matches local |
|------|-------------|--------|---------------|----------------------|
| `page-home.php` | `{DOC}/wp-content/themes/iseoblog/page-home.php` | UPDATE | `4d0a45a2b47c20c2aa9d17f0a53554d0d0d3b4709d64301ef134789c2f1cc903` | YES |
| `blog.html` | `{DOC}/blog.html` | UPDATE | `4aad6518d7eeae6bb5a59776de457dac3cf3a6db68bc9db4f20bb4c0a6f98427` | YES |

Deploy helper: `tools/_wave_tech_repair_01_backup_deploy_validate.py`.

---

## 10. Author Page Validation

All six author URLs (admin, denis, ilya, manager3, mars, olya):

- HTTP follow: **200** (final `https://i-seo.su/`)
- Stylesheets: root-relative `/css/*` and `/libs/*` → **200**
- Nested `/blog/author/css/...` requests: **0**
- Targeted recrawl: `AUTHOR_CSS_BROKEN_AFTER: 0`

JSON: `tools/_wave_tech_repair_01_recrawl.json`.

---

## 11. Logo Validation

| Check | Result |
|-------|--------|
| Stale `logo.svg` refs on sampled pages | **0** |
| `/img/logo-intl.svg` | **200** |
| `/img/logo.svg` (orphan URL) | still **404** (no live reference required) |
| MODEL | A |

---

## 12. Targeted Recrawl

Bounded recrawl over author pages, homepage, blog hub, category sample, blog post smoke, logo assets.

| Metric | Before | After |
|--------|--------|-------|
| BROKEN CSS (author family) | 6 | **0** |
| BROKEN LOGO references | 1 | **0** |
| BROKEN IMG (sampled refs) | 1 | **0** |

---

## 13. Regression

Smoke: `/`, `/blog/`, representative post, representative category.

- CSS healthy (no relative nested author paths)
- Layout restored to intended homepage CSS (no redesign)
- Sitemap HTTP 200 unchanged
- Related blog routes regression: **NONE**

---

## 14. SEO Mutation Check

| Marker | Changed |
|--------|---------|
| title | NO |
| description | NO |
| H1 | NO |
| canonical | NO |
| robots | NO |
| sitemap | NO |
| menu/navigation | NO |

SEO review backlog unmodified.

---

## 15. Production / Source Alignment

Both deployed files checksum-match canonical MARS `production-source/` copies. No production-only hotfix.

---

## 16. Rollback

Restore from:

`X:\AI MARS\local\sites\iseo-su-production\_tech-repair-wave-01\20260904T155608Z\`

exact backup files for `page-home.php` and `blog.html` via scoped SFTP overwrite.

---

## 17. Final Decision

**COMPLETE — ISEO-SU TECH REPAIR WAVE 01 / BLOG AUTHOR CSS FIXED / LOGO 404 RESOLVED / SEO BACKLOG UNTOUCHED**

Scoped Git: wave commit `87204916` + tip stamp `b98aced0` on `origin/mars/canonical-post-recovery` (fast-forward from `5add8c2a`).

STOP after docs + scoped Git sync. Do not start canonical/title/meta/alt/OG/menu work.
