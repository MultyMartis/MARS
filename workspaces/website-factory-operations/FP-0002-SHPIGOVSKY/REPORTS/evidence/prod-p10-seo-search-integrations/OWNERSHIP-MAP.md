# PROD-P10 — Ownership / Capability Map

**Date:** 2026-08-14  
**Host:** http://shpigovsky.beget.tech/  
**Future domain:** shpigovsky.ru (DNS cutover DEFERRED)

## Authority

| Layer | Authority |
|-------|-----------|
| Beget filesystem | LIVE RUNTIME TRUTH |
| Beget DB | LIVE CONTENT / ADMIN AUTHORITY |
| Local FP-0002 WORDPRESS tree | CODE / SOURCE AUTHORITY |

## SEO / Sitemap

| Concern | Pre-P10 owner | P10 decision |
|---------|---------------|--------------|
| Native WP sitemap `/wp-sitemap.xml` | Core available but **404** while `blog_public=0` | Extend native via `wp_sitemaps_*` filters; enable generation independently of indexing |
| Plugin SEO sitemap | None (no Yoast/RankMath/AIOSEO in source) | Do not install third-party SEO plugin |
| Custom competing sitemap | None | Do not create second system |
| `robots.txt` | Core: `User-agent: *` / `Disallow: /` (indexing closed) | Preserve Disallow; append `Sitemap:` when generation enabled |
| Canonical | Theme `pagination-seo.php` for Blog/Reviews pagination; core otherwise | Unchanged in P10 |
| CPT `service` | `shpigovsky-core` ContentTypes\Service | Include in native posts provider |
| Articles | Core `post` | Include |
| Specialists | Child `page` under `/specyalisty/` | Custom native provider `specialists` (not duplicate under pages) |
| Pages | Core `page` | Include; exclude legal/system + specialists |
| Taxonomies | None public custom | Empty taxonomies provider |
| Users sitemap | Core | Disabled |

## Smart Search

| Concern | Owner |
|---------|--------|
| REST | `GET /wp-json/shpigovsky/v1/smart-search` — `inc/search-helpers.php` |
| Frontend | `assets/js/v9-shell.js` shared binder (desktop + mobile) |
| Styles | `assets/css/fp02-search.css` (+ operator-canonized `v9-style.css` out of P10 mutate set) |
| Pre-P10 admin | None (hardcoded min=3, limit=5, all groups) |
| P10 admin | ACF under «Настройки сайта → SEO и интеграции → Умный поиск» |

## Site settings / Integrations

| Concern | Owner |
|---------|--------|
| Settings framework | `shpigovsky-core` ACF options pages |
| Parent menu | `fp02-site-settings` («Настройки сайта») |
| P10 subpage | `fp02-site-settings-seo-integrations` («SEO и интеграции») |
| Field group | `group_fp02_site_options_seo_integrations` / `SeoIntegrationsOptions` |
| Pre-P10 analytics/verification | None |
| Map embeds | Page-level contacts only — not reused for global trackers |

## Technical SEO (pre-audit)

| Concern | Owner / state |
|---------|----------------|
| Title | WP document title + theme search/pagination parts |
| Meta description | No dedicated theme owner (no SEO plugin) |
| robots meta | `noindex,nofollow` sitewide while `blog_public=0` |
| Structured data | SAFE UNKNOWN / minimal |
| OpenGraph | Not theme-owned |
| Temporary domain | Expected; DOMAIN CUTOVER findings only |

## Non-duplication rule

One Admin surface: **SEO и интеграции** with tabs Sitemap / Умный поиск / Аналитика и верификация.  
One sitemap system: WordPress native.  
One smart-search engine: existing P09 REST endpoint.
