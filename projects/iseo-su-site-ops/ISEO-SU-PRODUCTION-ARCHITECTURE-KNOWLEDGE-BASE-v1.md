# ISEO-SU PRODUCTION ARCHITECTURE KNOWLEDGE BASE v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-COMPLETE-PRODUCTION-ARCHITECTURE-ROUTE-KNOWLEDGE-CAPTURE  
**Site:** https://i-seo.su/  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  
**Status:** CURRENT / CANONICAL / ARCHITECTURE KNOWLEDGE READY FOR SITE WORK
**Current-state reconciliation:** 2026-08-24 (HIGH FIX WAVE 01 closed)
**Evidence basis:** accepted repository evidence through 2026-08-24; no production probe in this consolidation

No credentials, tokens, customer proposal bodies, cookies, or passwords are stored here. The sole current production form recipient is recorded because it is an operator-approved routing authority, not a secret.

---

## 1. Project Identity

| Field | Current authority |
|---|---|
| Programme | `ISEO-SU-SITE-OPS` |
| Site | `https://i-seo.su/` |
| Organization | i-SEO |
| Operator | Андрей |
| MARS locus | `X:\AI MARS\projects\iseo-su-site-ops\` |
| Hosting | Beget |
| Architecture | Hybrid physical PHP-capable HTML/static + WordPress |
| Current-state entry | [ISEO-SU-CURRENT-STATE-v1.md](ISEO-SU-CURRENT-STATE-v1.md) |

This file is the broad current production-architecture authority. Specialized baselines remain authoritative for forms, Metrika visitor IP, glossary, sitemap, and the latest technical/SEO audit.

## 2. Purpose and Ownership

The knowledge base lets a future operator classify a request, find the correct owner/source, protect shared dependencies, and start a bounded task without replaying chronological history. MARS/Site Ops owns technical changes; SEO/product owners decide semantic priorities where the audit marks `SEO_REVIEW`. Historical REPORT files are immutable evidence, not operating instructions.

## 3. Production Domain

Production is `https://i-seo.su/`. The WordPress install and direct marketing files share the same document root. Physical files/directories win before WordPress rewrite; `.html`/`.htm` are PHP-capable. Staging is absent. Production probing was not performed for this documentation task.

## 4. MARS Project Locus

- Canonical project documentation/source locus: `X:\AI MARS\projects\iseo-su-site-ops\`.
- Bulk evidence/scratch storage: `X:\AI MARS STORAGE\`.
- Canonical local runtime root: `X:\MARS-Localhost\`; no i-seo local mirror is claimed here.
- Local credentials/profiles and WPilot token remain local-only and Git-ignored.

## 5. Source / Runtime / Production Authorities

| Layer | Authority rule |
|---|---|
| Live behavior | Production runtime is evidence of what currently executes |
| Forms | `production-source/forms/` and `production-source/js/common.js` mirror accepted deployable source |
| Metrika IP addon | `production-source/metrika-ip/` plus loader in `production-source/js/common.js` |
| Shared CSS | `production-source/css/main.css`, including accepted operator manual hunks |
| Glossary theme | `wordpress/iseoblog-glossary/` |
| Glossary corpus | `content/glossary/`, `data/glossary-editorial/`, and immutable workbook under `materials/glossary/` |
| WordPress content/ACF | Production database, edited only through chartered WP workflows |

An accepted manual runtime edit must be reconciled by **runtime → bounded diff → canonical source promotion** before later automation overwrites the same surface.

## 6. Repository and Git Model

MARS is a monorepo; main may contain foreign WIP. Canonical branch is `mars/canonical-post-recovery`. Never use `git add .`, `git add -A`, broad restore/stash/clean/reset, or force push to isolate i-seo work. Stage exact project paths only. When main is dirty or histories differ, use a clean `X:\AI MARS STORAGE\git-sync-*` worktree based on `origin/mars/canonical-post-recovery`, replay only accepted scoped changes, and keep commit and push as separately authorized waves.

## 7. High-Level Site Architecture

### 7.1 Hybrid Static + WordPress Model

Request order is redirects/routing → existing physical file or directory → WordPress front controller. A WordPress edit cannot change a same-path physical file; removing a physical file may expose a WordPress route.

### 7.2 Static Marketing Contour

Root `*.html`, `/services/**`, `/cases/**`, legal pages, verification files, direct handlers, and shared assets are physical docroot surfaces. Marketing chrome is largely copied/hardcoded or PHP-included, not centrally controlled by the WordPress menu.

### 7.3 WordPress Contour

WordPress owns `/`, `/blog`, blog posts/categories, `/tariff-calc`, `/offers`/`offer`, `/glossary/`/`glossary`, theme templates, ACF-backed content, and WP sitemap surfaces.

### 7.4 Shared Assets

`css/main.css`, `css/media.css`, `js/common.js`, `libs/*`, root `img/`, theme assets, and uploads have broad blast radius. `js/common.js` participates in forms, calculator/tariffs, and Metrika visitor-IP loading.

### 7.5 Form Handler Contour

Twelve root `*__FORM.php` handlers call shared security/config code. Copies under `services/**` are thin delegates and must not develop independent validation/recipient logic.

## 8. Route Ownership

### 8.1 Homepage

`/` is WordPress page 1732 rendered by `wp-content/themes/iseoblog/page-home.php`; editor content is not the live owner. `/home.html` is a parallel legacy twin and must not be edited as a substitute.

### 8.2 Services

`/services.html` and `/services/**/*.html` are physical PHP-capable HTML. Exact file ownership plus shared CSS/JS and form delegates must be considered.

### 8.3 Cases

`/cases.html` and `/cases/**` are physical marketing files. Similar theme parts do not automatically own these public files.

### 8.4 Blog

`/blog` is page 1730 via `page-blog.php`; posts are WordPress content via `single.php` and ACF, with permalinks `/blog/%postname%.html`. `/blog.html` is parallel/legacy.

### 8.5 Offers

`/offers` is the WordPress offers entry; CPT `offer`, ACF «Предложения», and `single-offer.php` own commercial proposals. `/web-kp/` and `/kp/` are not public product routes. Offer content is commercially sensitive and must not be dumped into Git.

### 8.6 Tariff Calculator

`/tariff-calc` combines page/template PHP, ACF calculator/channel settings, `template-parts/tarif-calc.php`, `js/common.js`, and calculator/tariff handlers.

### 8.7 Glossary

`/glossary/` and eligible `/glossary/{slug}/` singles are public WordPress CPT routes. Final state is complete; 184 eligible terms are public, while MERGED/DEFERRED/EXCLUDED remain non-public.

### 8.8 Legal / Other

Server-side form security continues to use PHP `mail()`-style handlers; recipient emails are documented only in the specialized form baseline. SMTP path remains **SAFE UNKNOWN**. Current HMAC secret authority is **production-local** under `.iseo-form-runtime/iseo-form-secrets.local.php`; tracked config carries only the loader path and null placeholder.

Legal pages are physical `*-policy.html`/`user-agreement.html`. `/report-hub/` is a sibling product surface. Unknown tools such as `varvara-new.php` require separate owner confirmation before change.

Use [ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md](ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md) for the operational map.

## 9. WordPress

### 9.1 Theme

Active custom theme: `iseoblog`. It owns custom page/archive/single templates and shared theme chrome.

### 9.2 Plugins / Dependencies

Architecture evidence records ACF PRO, Yoast, Jetpack, and WPilot RC6 as active. Exact version claims are historical unless refreshed by accepted evidence. WP-Optimize and Akismet were inactive in the accepted capture.

### 9.3 Custom Templates

Key templates: `page-home.php`, `page-blog.php`, `page-tariffcalc.php`, `single.php`, `single-offer.php`, `archive-glossary.php`, and `single-glossary.php`.

### 9.4 ACF

Known groups: «Записи», «Настройки калькулятора», «Настройки каналов и тарифов», and «Предложения»; glossary metadata has its own accepted model. Schema changes are higher risk than scoped value edits.

### 9.5 Yoast

Yoast/meta integration supplies SEO fields and glossary title filters, but the current root `/sitemap.xml` must not be described as healthy Yoast output. Working WordPress sitemap authority is `/wp-sitemap.xml`.

### 9.6 Protected WordPress Boundaries

`wp-config.php`, `.htaccess`, core, plugin activation/settings, theme PHP, ACF schema/data, CPT offers, glossary exposure, and sitemap/robots behavior require exact charters and rollback.

## 10. Static Frontend

### 10.1 HTML/PHP Structure

Physical `.html` files may execute PHP. Shared header/footer can be copied markup or PHP includes; verify the exact file before change.

### 10.2 CSS

Root CSS affects multiple static and WordPress-like templates. `production-source/css/main.css` contains accepted operator glossary/mobile overflow work; never overwrite it from an older snapshot.

### 10.3 JS

`js/common.js` is revenue- and analytics-adjacent. It drives forms/calculator/tariffs and loads the Metrika addon. Make minimal diffs and test representative route classes.

### 10.4 Shared Components

Global header/footer changes may require both static/PHP include surfaces and WordPress theme parts. Updating only a WP menu is not sufficient for all pages.

### 10.5 Manual Operator Edit Rule

Before automation touches an operator-edited runtime file: fetch the exact current runtime artifact, diff it against canonical source, preserve accepted manual hunks, promote the result into MARS, and only then deploy further changes.

## 11. Public Forms

### 11.1 Form Inventory

Twelve root handlers cover callback, page, audit, calculator, four tariff forms, bonus, career, partners, and review; service-tree paths delegate to roots.

### 11.2 Handler Architecture

Browser → `js/common.js` → thin `*__FORM.php` → `iseo-form-security.php` → `iseo-form-config.php` → PHP mail path. `.iseo-form-runtime/` stores bounded rate/duplicate markers, not full lead bodies.

### 11.3 Recipient Authority

Recipients belong only in shared `iseo-form-config.php`; handlers must not hardcode alternate To/CC/BCC addresses.

### 11.4 Server Validation

POST-only, required-field/contact plausibility, scalar enforcement, whitespace/punctuation rejection, size caps, normalization, escaping, and mail/header injection controls are server authoritative.

### 11.5 Honeypot

`contact_company_url` must exist and remain empty; missing or populated is rejected.

### 11.6 HMAC / Fill-Time

Signed `{t,s,id}` token and approximately 3-second minimum fill time reject direct/too-fast submissions.

### 11.7 Rate Limiting

Approximately 3 submissions per 5 minutes per form/IP and 10 per hour per IP; no permanent automatic blacklist.

### 11.8 Duplicate Protection

Same normalized payload/source fingerprint is suppressed for approximately 10 minutes after a successful send.

### 11.9 Test Mode

`test_mode` is **false/OFF**. `im.work@mail.ru` is historical acceptance-only and may exist only as an inactive test recipient. `im.work@nail.ru` is an invalid historical typo. `chrra@yandex.ru` is an inactive historical commented alternate. The active HMAC secret is production-local only and must never be committed to tracked source or docs.

### 11.10 Current Production Recipient

**`nikel007i33@yandex.ru` only.**

### 11.11 Rules for Future Form Changes

Keep shared validation/config centralized; retain delegates; never leave test mode on; avoid real lead submissions without operator HITL; back up every touched runtime file; promote lasting runtime state to `production-source/forms/` and `production-source/js/common.js`.

Specialized authority: [ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md](ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md).

## 12. Yandex Metrika

### 12.1 Counter

Current production counter is **54287016**. Counter `39163020` is an unused historical example.

### 12.2 Existing Initialization

The existing page initialization and Yandex loader remain the normal analytics owner; the addon does not reinitialize the counter.

### 12.3 Webvisor / Existing Features

Clickmap, track links, bounce tracking, Webvisor, and normal goals remain independent and must continue working when the addon is disabled.

### 12.4 Visitor IP Addon

Production files: `/metrika-visitor-ip-config.php`, `/metrika-visitor-ip.php`, `/js/metrika-visitor-ip.js`; loader: `/js/common.js`; source: `production-source/metrika-ip/`.

### 12.5 Parameter `ipaddress`

One page-load call sends the validated server-observed address as `ym(54287016, 'params', {ipaddress: ...})`.

### 12.6 Server IP Authority

Authority is PHP `REMOTE_ADDR`, validated as IPv4/IPv6. `X-Forwarded-For`, `X-Real-IP`, `CF-Connecting-IP`, and `Forwarded` are not trusted.

### 12.7 Kill Switch

Current state is **ON**: `"enabled" => true` in `/metrika-visitor-ip-config.php` and canonical source.

### 12.8 Disable Procedure

Set `"enabled" => false` in production config, verify endpoint returns 204/no IP and no `ipaddress` call, then promote the same lasting state to `production-source/metrika-ip/metrika-visitor-ip-config.php`.

### 12.9 Failure Behavior

Fail-open for site rendering: endpoint/network/`ym` failures stop silently. Disabled state affects only custom IP parameter collection; normal Metrika/Webvisor stay operational.

### 12.10 Manual IP Investigation Purpose

The addon supports later manual traffic/spam analysis. It does not persist IP history in Git, modify forms, or automatically block visitors.

Specialized authority: [ISEO-SU-METRIKA-VISITOR-IP-PARAM-BASELINE-v1.md](ISEO-SU-METRIKA-VISITOR-IP-PARAM-BASELINE-v1.md).

## 13. Glossary

### 13.1 Source Corpus

Immutable source corpus contains **241** terms.

### 13.2 Editorial Disposition

Final disposition: 184 eligible canonical; MERGED 30; DEFERRED 14; EXCLUDED 13.

### 13.3 Public Corpus

**184** canonical articles are public; archive and eligible singles return HTTP 200; glossary sitemap child contains 184 term URLs.

### 13.4 Non-Public Corpus

57 non-eligible records remain non-public. A new charter/editorial decision is required before reconsideration.

### 13.5 Routes

Archive `/glossary/`; singles `/glossary/{slug}/`.

### 13.6 Templates

`archive-glossary.php`, `single-glossary.php`, glossary helpers under `inc/`, and mirrored package `wordpress/iseoblog-glossary/`.

### 13.7 Hero

Services-derived `page_scene`; no `.page_scene__rates`. Archive has H1 and intro; singles have H1 but no hero description.

### 13.8 CTA

`Подробнее` scrolls to `#SecondScreen`.

### 13.9 Related Terms

Singles link only to published eligible targets.

### 13.10 Sitemap

Working WordPress glossary sitemap contains 184 URLs. Glossary URLs do not need duplication in the static sitemap.

### 13.11 Navigation

Desktop submenu includes «Глоссарий» immediately after «Калькулятор SEO (free)». Mobile offcanvas parity is deferred optional. Mobile overflow is fixed.

### 13.12 Final Production Baseline

Archive title: `Глоссарий - INTLSEO Studio`. Production work is complete/frozen; see [ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md](ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md).

## 14. Sitemap Architecture

### 14.1 Current Working Sitemaps

`/sitemap-static.xml` and `/wp-sitemap.xml` return working sitemap surfaces.

### 14.2 Current Broken Root Sitemap State

`/sitemap.xml` advertises `post-sitemap.xml`, `page-sitemap.xml`, and `category-sitemap.xml`; the three children were observed 404. Finding `SM-CHILD-404` is HIGH/`OPEN_TECH`.

### 14.3 Target Root Sitemap Architecture

**Not implemented:** `/sitemap.xml` should be a valid `<sitemapindex>` containing two `<sitemap><loc>` child entries: absolute URLs for `/sitemap-static.xml` and `/wp-sitemap.xml`. It must not inline URL sets or imply an invalid redirect chain.

### 14.4 `sitemap-static.xml` (root `/sitemap.xml` indexes it with `/wp-sitemap.xml` after HIGH FIX WAVE 01)

Physical static inventory is working. Maintenance decision is open: prefer safe automatic regeneration; fallback to bounded rebuild plus documented procedure.

### 14.5 WordPress Sitemap

`/wp-sitemap.xml` is the working WordPress index for posts/pages/CPT/taxonomy surfaces.

### 14.6 robots.txt

Current robots behavior is protected. Target after root repair: reference only `https://i-seo.su/sitemap.xml`; this is planned, not implemented.

### 14.7 Open Sitemap Task

Repair root index, remove obsolete children, validate both child indexes and representative URLs, update/verify robots, and choose static maintenance. See [ISEO-SU-SITEMAP-ARCHITECTURE-AND-CURRENT-STATE-v1.md](ISEO-SU-SITEMAP-ARCHITECTURE-AND-CURRENT-STATE-v1.md).

## 15. Technical SEO

### 15.1 Latest Audit

Read-only audit dated 2026-08-21; no audit remediation was applied.

### 15.2 Crawl Size

1033 crawled; 643 indexable; 0 critical; 2 high; 6 medium; 8 low; 14 review; page 4xx/5xx 0; broken internal links 0.

### 15.3 Confirmed HIGH Findings

| ID | Issue | Status | Owner |
|---|---|---|---|
| `SM-CHILD-404` | Root sitemap advertises three 404 children | `OPEN_TECH` | MARS / SITE OPS |
| `IMG-BROKEN` | ≈96 sampled relative blog image URLs resolve to 404 | `OPEN_TECH` | MARS / SITE OPS |

### 15.4 Medium / Low Findings

| ID | Severity | Short issue | Status | Owner |
|---|---|---|---|---|
| `CANON-MISSING` | MEDIUM | Missing canonical on content-like pages | `SEO_REVIEW` | MARS / SITE OPS |
| `CANON-MISMATCH` | MEDIUM | Canonical/self mismatch | `SEO_REVIEW` | MARS / SITE OPS |
| `SM-MISSING-INDEXABLE` | MEDIUM | Indexable URLs absent from sitemap union | `SEO_REVIEW` | SEO REVIEW |
| `SM-NONINDEX` | MEDIUM | Non-indexable URLs listed in sitemap | `SEO_REVIEW` | MARS / SITE OPS |
| `TITLE-DUP` | MEDIUM | Duplicate titles | `SEO_REVIEW` | SEO REVIEW |
| `ORPHAN-CRAWLER` | MEDIUM | Crawler-level orphan candidates | `SEO_REVIEW` | SEO REVIEW |
| `LINK-TO-REDIR`, `TITLE-LONG`, `META-MISSING`, `META-DUP` | LOW | Redirect/title/meta cleanup | `SEO_REVIEW` | CSV owner |
| `H1-MISSING`, `IMG-HUGE`, `IMG-ALT`, `OG-MISSING` | LOW | H1/image/social-meta review | `SEO_REVIEW` | CSV owner |

### 15.5 SEO Review Findings

Use the CSV owner/status per ID. `SM-DUAL-ARCH` is INFO/`EXPECTED`, not a defect by itself. Semantic choices for canonicals, titles/meta, orphan priority, alt text, and OG require SEO/product review before broad implementation.

### 15.6 Audit Artifact Locations

- `ISEO-SU-TECH-SEO-AUDIT-EVIDENCE-v1.md`
- `audits/tech-seo/ISEO-SU-TECH-SEO-FINDINGS-v1.csv`
- `audits/tech-seo/ISEO-SU-TECH-SEO-URL-INVENTORY-v1.csv`
- `reports/ISEO-SU-TECH-SEO-AUDIT-FOR-SEO-TEAM-v1.md`
- raw evidence: `X:\AI MARS STORAGE\iseo-su-site-ops\tech-seo-audit-01\`

### 15.7 Fix Policy

One scoped technical wave at a time; use actual finding IDs, preserve expected dual architecture, obtain SEO decisions where required, and run targeted regression rather than a speculative mass rewrite.

## 16. Blog Image Architecture

### 16.1 Current Relative-Path Defect

Finding `IMG-BROKEN` remains open. Relative `img/...` references on nested blog URLs resolve below the current blog path instead of root `/img/`.

### 16.2 Affected Pattern

Audit sampled ≈96 broken URLs, especially `/blog/20YY/.../img/...` and `/blog/author/.../img/...`.

### 16.3 Open Fix Task

Trace whether each reference is post content, ACF, or template output; convert only confirmed site-root assets to `/img/...`; preserve upload URLs; validate representative year/author/post pages; run targeted image crawl.

## 17. WPilot

### 17.1 Current State

WPilot RC6 is active with safe defaults; `dev_confirmed=false`.

### 17.2 Token

Token exists local-only and must never enter Git/docs.

### 17.3 Bridge

`bridge=false`.

### 17.4 Write Mode

`write=false`; WPilot is not authorized for static files, theme PHP, forms, ACF, offers, glossary publication, Metrika, or sitemap work.

### 17.5 Deferred 6D

Phase 6D bridge/read-only smoke is deferred optional and requires a separate exact approval and fresh backup.

### 17.6 When WPilot Is / Is Not Required

It is not required for ordinary SFTP/WP Admin Site Ops. Do not reopen onboarding unless a task explicitly needs WPilot capability.

## 18. Production Operations

### 18.1 Access Model

Use existing local-only i-seo credential/profile authorities. Never copy credentials, tokens, cookies, or session values into project files.

### 18.2 Scoped Backups

Before mutation: fresh operator full backup plus exact pre-change copies/attestations for every touched file/object.

### 18.3 SFTP

Use bounded reads/writes to named paths. No broad mirror/purge. Preserve modes and verify hashes where practical.

### 18.4 VPN Instability / Resume Rule

If VPN/network/SFTP is unstable, stop repeated mutation attempts. Re-establish identity, fetch current runtime again, verify whether the prior upload completed, and resume from evidence—not assumption.

### 18.5 Deployment Validation

Validate status/final URL/title/H1/marker/no fatal, plus route-class regressions for shared assets. Do not submit production forms without explicit operator HITL.

### 18.6 Runtime→Source Promotion

For lasting runtime changes, reconcile and promote exact final bytes into the canonical source mirror before declaring source alignment.

## 19. Backup / Rollback

### 19.1 Operator Full Backups

Fresh Beget backup is required before each production mutation wave.

### 19.2 Scoped Production File Backups

Keep exact pre-change copies and hashes/stamps for named runtime files; WP content uses revisions/DB backup as appropriate.

### 19.3 Storage

Large raw evidence/backups belong under approved `X:\AI MARS STORAGE\` task paths, not Git.

### 19.4 Rollback Expectations

Define rollback before deploy, restore only scoped artifacts, validate critical routes after rollback, and promote lasting rolled-back state to source.

## 20. Protected Zones

Protected means **inspect and change intentionally**, not “never touch.” Exact charter, backup, diff, validation, rollback, and source promotion apply to forms/recipient security, shared CSS/JS, Metrika counter/addon switch, glossary baseline, root/static/WP sitemaps and robots, `.htaccess`, `wp-config.php`, WP core/plugins/theme, ACF, offers, calculator, uploads, local secrets, and sibling Report Hub. See [ISEO-SU-PROTECTED-ZONES-v1.md](ISEO-SU-PROTECTED-ZONES-v1.md).

## 21. Known Manual Operator Decisions

- Production form recipient is `nikel007i33@yandex.ru` only; `test_mode` OFF.
- `im.work@mail.ru` was acceptance-only and removed; typo `im.work@nail.ru` remains invalid; `chrra@yandex.ru` is inactive historical comment only.
- CAPTCHA was not added; layered server protections are the accepted baseline.
- Visitor-IP addon is ON, analytics-only, manually investigated, and kill-switchable without disabling normal Metrika.
- Glossary public set is 184; non-eligible sets remain non-public; desktop link is live; mobile offcanvas remains deferred.
- Root sitemap target is the two-child index; static maintenance strategy remains open.

## 22. Current Open Technical Work

1. `SM-CHILD-404`: repair `/sitemap.xml`, remove three obsolete 404 children, point to working `/sitemap-static.xml` and `/wp-sitemap.xml`, then verify robots.
2. Decide/implement `/sitemap-static.xml` maintenance: safe automation preferred; manual rebuild/procedure fallback.
3. `IMG-BROKEN`: repair confirmed relative blog image path patterns and regression-crawl.
4. Review/route the remaining 6 MEDIUM, 8 LOW, and 14 REVIEW audit signals from the CSV.

## 23. Deferred Optional Work

1. Mobile glossary offcanvas parity.
2. Glossary archive Yoast meta description.
3. MERGED alias/search polish.
4. Sitemap duplication beyond the target two-surface index if ever justified.
5. WPilot Phase 6D bridge/read-only smoke.

These are non-blocking and must not be confused with `OPEN_TECH`.

## 24. Completed Major Work

- Production architecture intake and route ownership capture.
- WPilot RC6 install/activation and local-only token safety baseline.
- Glossary source canonicalization, editorial model, four content batches, and final corpus.
- Controlled publication of 184 glossary terms; hero/CTA/related terms/menu/title integration.
- Glossary mobile overflow correction and operator CSS promotion.
- Site Ops stabilization and scratch relocation.
- Form server validation/anti-spam hardening and 12/12 isolated acceptance.
- Recipient restoration/correction history followed by intentional operator-test-address removal; current single recipient confirmed.
- Read-only 1033-URL technical/SEO audit and findings artifacts.
- Metrika visitor-IP parameter addon with tested true→false→true kill switch.

## 25. SAFE UNKNOWN

Genuinely unresolved, non-blocking facts remain in [ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md](ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md): exact PHP runtime version, full ACF location-rule export, complete drift inventory, `/services.html` intermittent-500 cause, `/offers` listing composition detail, `varvara-new.php` ownership, Beget restore click-path details, mail transport/relay specifics, and selected WPilot internals. Unknowns are not open defects unless evidence creates a task.

## 26. Entry Procedure for the Next Task

1. Read [Current State](ISEO-SU-CURRENT-STATE-v1.md), then this KB.
2. Select one concrete task/finding ID.
3. Route via [Task Routing Guide](ISEO-SU-TASK-ROUTING-GUIDE-v1.md) and [Route Matrix](ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md).
4. Read [Protected Zones](ISEO-SU-PROTECTED-ZONES-v1.md) and the relevant specialized baseline.
5. Name exact runtime/source paths, backup, validation, rollback, and source-promotion plan.
6. Keep secrets local-only and foreign Git WIP untouched.
7. Persist only scoped accepted documentation/source evidence when explicitly authorized.

## 27. Canonical Supporting Documents

1. [ISEO-SU-CURRENT-STATE-v1.md](ISEO-SU-CURRENT-STATE-v1.md)
2. [ISEO-SU-TASK-ROUTING-GUIDE-v1.md](ISEO-SU-TASK-ROUTING-GUIDE-v1.md)
3. [ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md](ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md)
4. [ISEO-SU-PROTECTED-ZONES-v1.md](ISEO-SU-PROTECTED-ZONES-v1.md)
5. [ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md](ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md)
6. [ISEO-SU-METRIKA-VISITOR-IP-PARAM-BASELINE-v1.md](ISEO-SU-METRIKA-VISITOR-IP-PARAM-BASELINE-v1.md)
7. [ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md](ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md)
8. [ISEO-SU-SITEMAP-ARCHITECTURE-AND-CURRENT-STATE-v1.md](ISEO-SU-SITEMAP-ARCHITECTURE-AND-CURRENT-STATE-v1.md)
9. [ISEO-SU-TECH-SEO-AUDIT-EVIDENCE-v1.md](ISEO-SU-TECH-SEO-AUDIT-EVIDENCE-v1.md)
10. [ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md](ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md)
11. [ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md](ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md)
12. [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)
