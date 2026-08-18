# Forge WordPress — SEO and Sitemap Standard v1

**ID:** FW-S-12  
**Status:** ACTIVE — PRODUCTION PROVEN WITH CAVEATS  
**Date:** 2026-08-18  
**Evidence:** FP-0002 P10, P13, P15, P17-FU02

---

## 1. Ownership

**One SEO owner** in the functionality plugin + theme output helpers. Do not stack Rank Math / Yoast / another custom title builder without an explicit WAD (AP-017).

| Surface | Owner |
|---------|--------|
| Title / meta description | Entity ACF or equivalent + fallbacks |
| Canonical | WordPress / `get_permalink` / `home_url` — no competing tags |
| Sitemap | Native `wp-sitemap.xml` + `wp_sitemaps_*` |
| robots.txt / blog_public | Core + launch SOP |
| Verification / analytics | Site Settings; empty = no output |
| Advanced head/body/footer | Site Settings, capability-gated |

---

## 2. CORE DEFAULT vs OPTIONAL vs CUTOVER-TIME

| Item | When |
|------|------|
| SEO Title + Description fields on public entities | **CORE DEFAULT** |
| Fallback: title ← post title; description ← excerpt/lead truncated | **CORE DEFAULT** |
| Native sitemap for public post types | **CORE DEFAULT** |
| Explicit exclusions (search, thank-you, private) | **CORE DEFAULT** |
| Webmaster / Search Console / Metrica / GA/GTM fields | **OPTIONAL** (fields exist; values optional) |
| Advanced raw code | **OPTIONAL** / Admin-only |
| `blog_public=1` and robots Allow | **CUTOVER-TIME** after indexing gate |
| Sitemap submission to Google/Yandex | **CUTOVER-TIME** |
| Final crawl | **CUTOVER-TIME** |

```text
SITEMAP GENERATION READINESS ≠ INDEXING ENABLED
```

Temporary/staging hosts: sitemap may be generated for QA while `blog_public=0`, `Disallow: /`, and meta noindex remain **intentional**.

---

## 3. Sitemap rules

- Prefer **extending WordPress core sitemaps**. Do not ship a second competing XML system.
- Include public CPTs that should be indexed; exclude hubs duplicated as archives when `has_archive=false` and the Page hub is the index.
- Admin: links to sitemap index + provider URLs; Russian/locale help text.
- URLs must be `home_url` / `get_permalink` — never hardcoded `.test` or temporary host after cutover.
- Google and Yandex: **XML sitemap** is the current official model.

```text
DO NOT INVENT A YANDEX PAGE/SERVICE FEED WHEN THE CURRENT OFFICIAL MODEL IS XML SITEMAP.
```

---

## 4. Indexing gate (summary)

Do **not** open indexing because HTTPS or the domain “works”. Required first: HTTPS PASS, canonical PASS, sitemap on **final** domain PASS, frontend smoke, WP Admin, **forms PASS**, **SMTP delivery PASS**, redirects PASS. Then robots → consoles → submit sitemap → crawl.

Full sequence: [PRE-CUTOVER-AND-LAUNCH-SOP](../runbooks/FORGE-WORDPRESS-PRE-CUTOVER-AND-LAUNCH-SOP-v1.md).

---

*FW-S-12 v1.*
