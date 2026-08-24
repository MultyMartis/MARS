# ISEO-SU CURRENT STATE v1

**Programme:** ISEO-SU-SITE-OPS  
**Site:** `https://i-seo.su/`
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  
**Updated:** 2026-08-24 (SEO REVIEW PACK 01 — decision materials only)  
**Authority:** first current-state document for ordinary work

Historical REPORT files record earlier states and do not override this document or fresher accepted evidence.

## 1. Overall Status

The production site is operating; glossary publication, form hardening, form HMAC secret rotation to a production-local authority, technical/SEO audit, and the Metrika visitor-IP addon are complete milestones. HIGH FIX WAVE 01 is **CLOSED** (technical): root `/sitemap.xml` repaired, initial static allowlist generator deployed (historical coverage was incomplete), theme relative `img/` paths normalized to `/img/`. **Static sitemap completeness fix 01 is CLOSED**: SEO-supplied 54 missing public URLs validated and added; +2 legal pages from broader reconciliation; static sitemap **71 → 127**; completeness gate `PUBLIC_CANONICAL_STATIC_ROUTES - SITEMAP_STATIC_URLS = 0` required on regenerate. **TECH CLEANUP WAVE 01 is CLOSED**: `SM-MISSING-INDEXABLE` rechecked (eligible gap **0**), `LINK-TO-REDIR` residual **0**, `IMG-HUGE` residual **0**. Remaining open work is SEO-review audit findings only (separate charter).

## 2. Production Status

- Production: `https://i-seo.su/`; hosting: Beget; staging is absent.
- Main public page crawl was healthy: 0 page 4xx, 0 page 5xx, 0 broken internal links in the latest crawl graph.
- Current form HMAC authority is production-local at `.iseo-form-runtime/iseo-form-secrets.local.php`; active secret is absent from current tracked source.
- Production mutations require an exact charter, fresh backup, bounded validation, and rollback evidence.
- Do not perform generic onboarding or production rediscovery when current authorities already classify the target.

## 3. Architecture

i-seo.su is hybrid: physical PHP-capable HTML/static marketing files coexist with a WordPress root install and shared assets.

- `/` → WordPress `page-home.php`; `home.html` is a parallel legacy file.
- `/blog` → `page-blog.php`; posts use `/blog/%postname%.html`.
- `/tariff-calc` → hybrid WordPress/ACF/theme/JS/form-handler surface.
- `/offers` and `offer` CPT → offers/Web-KP surface.
- `/glossary/` and `/glossary/{slug}/` → public glossary archive and singles.
- Static marketing: root `*.html`, `/services/**`, `/cases/**`; shared `css/`, `js/`, `libs/`, `img/`.

See [Knowledge Base](ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md) and [Route Matrix](ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md).

## 4. Current Form Security

Current baseline: **12 root handlers** plus thin service-tree delegates; shared `iseo-form-security.php`, `iseo-form-config.php`, token endpoint, and `js/common.js`.

- server-side required-field/scalar/size/contact validation;
- honeypot `contact_company_url`;
- HMAC token and minimum fill time ≈3 seconds;
- limits ≈3 submissions/5 minutes/form/IP and ≈10/hour/IP;
- duplicate suppression ≈10 minutes;
- header/HTML injection protections;
- CAPTCHA absent by accepted design.

Authority: [Form Security Baseline](ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md).

## 5. Current Form Recipient

| Field | Current state |
|---|---|
| Production recipient | **`nikel007i33@yandex.ru` only** |
| `test_mode` | **OFF / false** |
| `im.work@mail.ru` | historical acceptance-only test address; removed from production |
| `im.work@nail.ru` | invalid historical typo; must remain absent |
| `chrra@yandex.ru` | inactive historical commented alternate; not a recipient |

## 6. Current Metrika State

Existing Yandex Metrika counter: **54287016**. Normal counter initialization, goals, clickmap, and Webvisor are independent of the visitor-IP addon. Example counter `39163020` is not production.

## 7. Visitor IP Addon

State: **ON**. Production paths: `/metrika-visitor-ip-config.php`, `/metrika-visitor-ip.php`, `/js/metrika-visitor-ip.js`; loader: `/js/common.js`; MARS source: `production-source/metrika-ip/`.

The endpoint uses validated IPv4/IPv6 `REMOTE_ADDR`, ignores forwarded headers, and sends parameter `ipaddress` to counter 54287016. It does not auto-block. Kill switch: set `"enabled" => false`; normal Metrika/Webvisor remain active. See [Metrika Baseline](ISEO-SU-METRIKA-VISITOR-IP-PARAM-BASELINE-v1.md).

## 8. Glossary

Production work is complete: source 241; public canonical 184; MERGED 30, DEFERRED 14, EXCLUDED 13; archive and eligible singles return HTTP 200; sitemap glossary URLs 184.

Archive has H1/intro/title `Глоссарий - INTLSEO Studio`; archive and singles use services-derived `page_scene` without rates; CTA `Подробнее` → `#SecondScreen`; singles have no hero description; related terms link only to eligible public terms. Desktop menu is live; mobile offcanvas is deferred; mobile overflow is fixed. Authority: [Glossary Final Baseline](ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md).

## 9. Sitemap

- Canonical root `/sitemap.xml` is a valid **sitemapindex** with exactly two children: `/sitemap-static.xml` and `/wp-sitemap.xml` (HIGH FIX WAVE 01).
- Obsolete Yoast-style children (`post|page|category-sitemap.xml`) are no longer advertised.
- `robots.txt` references `https://i-seo.su/sitemap.xml` only.
- Static inventory: **127** URLs via allowlist generator `tools/generate-sitemap-static.py` (`data/sitemaps/sitemap-static-urls-v1.txt` → `production-source/sitemaps/sitemap-static.xml`) with completeness validator.
- MARS SoT: `production-source/sitemaps/`.

See [Sitemap Architecture](ISEO-SU-SITEMAP-ARCHITECTURE-AND-CURRENT-STATE-v1.md) and [HIGH FIX WAVE 01 Evidence](ISEO-SU-HIGH-FIX-WAVE-01-EVIDENCE-v1.md).

## 10. Latest Tech/SEO Audit

Read-only audit (historical 2026-08-21): **1033 crawled**, **643 indexable**, 0 critical, 2 high, 6 medium, 8 low, 14 review; page 4xx/5xx 0; broken internal links 0.

| ID | Severity | Current status | Owner |
|---|---|---|---|
| `SM-CHILD-404` | HIGH | `CLOSED` (HIGH FIX WAVE 01) | MARS / SITE OPS |
| `IMG-BROKEN` | HIGH | `CLOSED` (HIGH FIX WAVE 01) | MARS / SITE OPS |
| `SM-MISSING-INDEXABLE` | MEDIUM | `CLOSED / RECHECKED` (TECH CLEANUP WAVE 01; eligible gap 0) | MARS / SITE OPS |
| `LINK-TO-REDIR` | LOW | `CLOSED` (TECH CLEANUP WAVE 01) | MARS / SITE OPS |
| `IMG-HUGE` | LOW | `CLOSED` (TECH CLEANUP WAVE 01) | MARS / SITE OPS |
| Remaining IDs in findings CSV | MEDIUM/LOW/REVIEW | `SEO_REVIEW` | CSV owner per finding |
| `SM-DUAL-ARCH` | INFO | `EXPECTED` (root repaired; ownership split remains) | SEO REVIEW |

Authority: [Audit Evidence](ISEO-SU-TECH-SEO-AUDIT-EVIDENCE-v1.md), backlog CSV, [TECH CLEANUP WAVE 01 Evidence](ISEO-SU-TECH-CLEANUP-WAVE-01-EVIDENCE-v1.md).

## 11. Open Technical Tasks

1. ~~Root sitemap repair~~ — **CLOSED** (HIGH FIX WAVE 01).
2. ~~Static sitemap maintenance~~ — **CLOSED** (allowlist generator + documented regen + completeness fix).
3. ~~Blog image paths~~ — **CLOSED** (theme `/img/` normalization + targeted recrawl PASS).
4. ~~Tech cleanup wave 01~~ — **CLOSED** (sitemap-gap recheck, redirect-link cleanup, two heavy images).
5. **SEO-review backlog:** remaining CANON/TITLE/META/ORPHAN/ALT/OG/SM-NONINDEX signals — **decision pack prepared** (`reports/ISEO-SU-SEO-REVIEW-PACK-01-RU.md`); awaiting SEO answers; no autofix; finding semantic statuses unchanged until SEO decides.

HIGH open: **0**. OPEN_TECH from wave 01: **0**.

## 12. Deferred Optional Work

Exactly five non-blocking items:

1. Mobile glossary offcanvas parity.
2. Glossary archive Yoast meta description.
3. MERGED alias/search polish.
4. Sitemap duplication beyond the target two-surface index, if ever justified.
5. WPilot Phase 6D bridge/read-only smoke.

## 13. Protected Areas

Protected means inspect, diff, back up, change intentionally, validate, and preserve rollback—not “never touch.” Forms/recipient config, shared CSS/JS, Metrika counter/addon switch, glossary baseline, sitemaps/robots, routing, offers, calculator, WordPress config/core, and local secrets require exact scope. See [Protected Zones](ISEO-SU-PROTECTED-ZONES-v1.md).

## 14. Git / Source Authority

- Runtime truth is live production; canonical editable mirrors include `production-source/forms/`, `production-source/js/common.js`, `production-source/metrika-ip/`, `production-source/css/main.css`, `production-source/sitemaps/`, `production-source/theme/iseoblog/` (homepage/cases/recommendations img paths), and `wordpress/iseoblog-glossary/`.
- After an accepted manual runtime edit: bounded **runtime → diff → canonical source promotion** before any automation overwrite.
- Canonical branch: `mars/canonical-post-recovery`.
- Main may contain foreign WIP. Never broad-stage, clean, reset, stash, or restore it.
- Use scoped exact paths and a clean `X:\AI MARS STORAGE\git-sync-*` worktree for safe synchronization.

## 15. Next Task Entry Point

1. Read this file, then [Knowledge Base](ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md).
2. Use [Task Routing](ISEO-SU-TASK-ROUTING-GUIDE-v1.md) and [Route Matrix](ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md).
3. Read [Protected Zones](ISEO-SU-PROTECTED-ZONES-v1.md) and the relevant specialized baseline.
4. Select one open task and name exact runtime/source paths.
5. For production mutation, require fresh backup, bounded deployment, validation, rollback, and source promotion.

WPilot 6D is not required for ordinary site operations.
