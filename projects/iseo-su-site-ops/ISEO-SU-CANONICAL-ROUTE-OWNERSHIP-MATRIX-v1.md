# ISEO-SU CANONICAL ROUTE OWNERSHIP MATRIX v1

**Programme:** ISEO-SU-SITE-OPS  
**Authority rank:** #3 (after task evidence + task routing guide)  
**Companion:** [ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md](ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md)  
**Evidence:** 2026-07-24 discovery, reconciled with accepted form/glossary/audit/Metrika state through 2026-08-24

## Classification vocabulary (exact one primary)

| Code | Meaning |
|------|---------|
| `STATIC_HARDCODED` | Standalone HTML/PHP file owns response |
| `WORDPRESS_CONTENT` | WP page/post/CPT/tax via normal routing + editable content/fields |
| `WORDPRESS_TEMPLATE_STATIC_LIKE` | WP-owned route; markup mostly hardcoded in custom PHP template |
| `HYBRID_COMPOSITE` | Material WP + non-WP (shared JS/PHP handlers/ACF/static) dependency |
| `REDIRECT_OR_ALIAS` | Redirect / non-canonical alias |
| `LEGACY_OR_PARALLEL` | Parallel file/route; not primary public owner |
| `SAFE_UNKNOWN` | Insufficient or contradictory evidence |
| `EXTERNAL_SIBLING` | Sibling product surface (Report Hub) |

Confidence: **HIGH** / **MEDIUM** / **LOW**

---

## Core business routes

| route | final URL | HTTP | class | conf | public role | SoT | WP object | slug | template | primary file | shared CSS | shared JS | forms/handlers | ACF | CPT | calc | web-KP | redirect/alias | parallel | safe edit | backup | rollback | validation | protected deps | unresolved |
|-------|-----------|------|-------|------|-------------|-----|-----------|------|----------|--------------|------------|-----------|----------------|-----|-----|------|--------|----------------|----------|-----------|--------|----------|------------|----------------|------------|
| `/` | `https://i-seo.su/` | 200 | WORDPRESS_TEMPLATE_STATIC_LIKE | HIGH | Homepage | theme `page-home.php` | page 1732 | glavnaya | page-home.php | `wp-content/themes/iseoblog/page-home.php` | css/* | js/common.js + libs | calc/tariff/callback via common.js | none on page | — | yes (embedded) | no | — | `home.html` | SFTP theme file | theme file + Beget | restore theme file | `/` title+calc markers | shared css/js, forms | editor unused |
| `/home.html` | `…/home.html` | 200 | LEGACY_OR_PARALLEL | HIGH | Parallel homepage file | physical file | — | — | — | `home.html` | css/* | js/common.js | same family | — | — | yes | no | not primary | live `/` | avoid unless intentional sync | file | restore file | `/home.html` | drift vs `/` | which inbound links remain |
| `/blog` `/blog/` | `…/blog` | 200 | WORDPRESS_TEMPLATE_STATIC_LIKE | HIGH | Blog hub | `page-blog.php` + posts | page 1730 | blog | page-blog.php | theme `page-blog.php` | theme+css | common.js + theme js | theme chrome forms | — | — | possible chrome | no | slash alias | `blog.html` | WP page chrome via theme; posts separately | theme+DB | restore | `/blog` generator WP | theme chrome | — |
| `/blog.html` | `…/blog.html` | 200 | LEGACY_OR_PARALLEL | HIGH | Static blog mock | file | — | — | — | `blog.html` | css/* | js | — | — | — | no | no | not `/blog` | live `/blog` | avoid | file | restore | status | — | — |
| `/blog/{slug}.html` | same | 200 | WORDPRESS_CONTENT | HIGH | Blog article | post + ACF «Записи» + `single.php` | post | slug | single.php | theme `single.php` | theme+css | common.js + rate-my-post | — | Записи | — | no | no | permalink pattern | `blog-article.html` mock | WP Admin post + ACF | DB+media | revisions/restore | article URL | ACF group | — |
| `/blog/category/{slug}` | same | 200 | WORDPRESS_CONTENT | HIGH | Category archive | taxonomy + theme archive | category | slug | archive.php (theme) | theme archive/index | theme | theme js | — | — | — | no | no | — | — | WP taxonomy/content | DB | restore | category URL | — | exact template pick |
| `/tariff-calc` | `…/tariff-calc` | 200 | HYBRID_COMPOSITE | HIGH | Tariff calculator | ACF + `tarif-calc.php` + common.js + handlers | page 1734 | tariff-calc | page-tariffcalc.php | theme `page-tariffcalc.php` + `template-parts/tarif-calc.php` | theme+css | common.js | calc/tariff FORM.php | Настройки калькулятора (+ channels group) | — | **yes** | no | slash→no slash | theme tarifs parts on other pages | ACF fields and/or theme part — not editor HTML | ACF+theme+handlers scope | restore each layer | `/tariff-calc` | ACF, js, FORM.php | options vs page field location nuance |
| `/offers` | `…/offers` | 200 | WORDPRESS_CONTENT | HIGH | Offers listing / KP entry | WP page + CPT ecosystem | page 1377 | offers | default | theme `page.php` / content-page | theme | theme | — | — | offer list related | no | **candidate** | slash alias | — | WP page + CPT posts | DB | restore | `/offers` | private offers | empty editor — listing UX detail |
| `/offer/*` | private singles | — | WORDPRESS_CONTENT | MEDIUM | Single commercial proposal | CPT `offer` + `single-offer.php` + ACF «Предложения» | offer CPT | slug | single-offer.php | theme `single-offer.php` | theme | theme | — | Предложения | **offer** | no | **yes** | robots disallow | — | WP Admin offer + ACF; no public scrape | DB | restore | structural only | **PII/commercial** | public URL pattern variants |
| `/glossary/` | `…/glossary/` | 200 anon | WORDPRESS_CONTENT | HIGH | Glossary archive (public) | CPT `glossary` + `archive-glossary.php` | glossary CPT | — | archive-glossary.php | theme `archive-glossary.php` | theme+css | theme | search GET only | glossary ACF | **glossary** | `/wp-sitemap.xml` family | no header | slash alias | — | final baseline only | theme+DB+package | scoped restore | public hub/H1/intro/CTA | 184 public; non-eligible stay draft | mobile offcanvas deferred; overflow fixed |
| `/glossary/{slug}/` | same | 200 published | WORDPRESS_CONTENT | HIGH | Glossary term | CPT `glossary` + `single-glossary.php` | glossary | slug | single-glossary.php | theme `single-glossary.php` | theme+css | theme | — | synonyms/related | **glossary** | `/wp-sitemap.xml` family (184) | — | — | — | publish eligible only | DB+package | draft/scoped restore | public single/related links | 30 MERGED + 14 DEFERRED + 13 EXCLUDED non-public | single hero has no description |
| `/web-kp/` `/kp/` | 404 | 404 | SAFE_UNKNOWN | HIGH | no public app at these paths | — | — | — | — | — | — | — | — | — | — | — | naming only | — | use `/offers`+CPT | — | — | — | — | — | operator nickname mapping |
| `/services.html` | `…/services.html` | 200* | STATIC_HARDCODED | HIGH | Services hub | file | — | — | — | `services.html` | css | common.js | forms | — | — | possible | no | — | — | SFTP file | file | restore | URL+title | intermittent 500 once | root cause of intermittent 500 |
| `/services/**/*.html` | same | 200 | STATIC_HARDCODED | HIGH | Service leaves | files under `services/` | — | — | — | matching path | css | common.js | often local FORM copies | — | — | often | no | — | — | SFTP exact file | file(+handler if touched) | restore | URL | handler copies drift | — |
| `/cases.html` + `/cases/**` | same | 200 | STATIC_HARDCODED | MEDIUM | Cases | files | — | — | — | matching | css | common.js | forms | — | — | no | no | — | theme cases-* parts (WP) | SFTP | file | restore | URL | — | — |
| `/contacts.html` | same | 200 | STATIC_HARDCODED | HIGH | Contacts | file | — | — | — | `contacts.html` | css | common.js | callback/page forms | — | — | no | no | — | — | SFTP | file | restore | URL | forms | — |
| `/about.html` | same | 200 | STATIC_HARDCODED | HIGH | About | file | — | — | — | `about.html` | css | common.js | forms | — | — | no | no | — | — | SFTP | file | restore | URL | — | — |
| `/reviews.html` | same | 200 | STATIC_HARDCODED | MEDIUM | Reviews | file | — | — | — | `reviews.html` | css | common.js | review__FORM | — | — | no | no | — | — | SFTP | file | restore | URL | forms | — |
| `/partners.html` | same | 200 | STATIC_HARDCODED | MEDIUM | Partners | file | — | — | — | `partners.html` | css | common.js | partners__FORM | — | — | no | no | — | — | SFTP | file | restore | URL | forms | — |
| `/bonuses.html` | same | 200 | STATIC_HARDCODED | MEDIUM | Bonuses | file | — | — | — | `bonuses.html` | css | common.js | bonus__FORM | — | — | no | no | — | — | SFTP | file | restore | URL | forms | — |
| `/career.html` | same | 200 | STATIC_HARDCODED | MEDIUM | Career | file | — | — | — | `career.html` | css | common.js | career__FORM | — | — | no | no | — | — | SFTP | file | restore | URL | forms | — |
| `/guarantees.html` | same | 200 | STATIC_HARDCODED | MEDIUM | Guarantees | file | — | — | — | `guarantees.html` | css | common.js | — | — | — | no | no | — | — | SFTP | file | restore | URL | — | — |
| legal `*-policy.html` / `user-agreement.html` | same | 200 | STATIC_HARDCODED | HIGH | Legal | files | — | — | — | matching | css | — | — | — | — | no | no | — | — | SFTP | file | restore | URL | compliance | — |
| `/report-hub/` | same | 200 | EXTERNAL_SIBLING | HIGH | Report Hub app | `report-hub/*` | — | — | — | report-hub HTML | local | local | — | — | — | no | no | — | `projects/iseo-report-hub` | separate programme | — | — | URL | do not treat as marketing | — |
| `/varvara-new.php` | same | 200 | STATIC_HARDCODED | MEDIUM | VVR-Searcher tool | PHP file | — | — | — | `varvara-new.php` | — | — | — | — | — | no | no | — | — | SFTP chartered only | file | restore | title VVR-Searcher | unknown business use | deeper purpose |
| `/sitemap.xml` | same | 200 | HYBRID_COMPOSITE | HIGH | Root sitemap entry | current owner/generator must be traced | — | — | — | current root index | — | — | — | — | — | no | no | — | — | exact charter only | root+static+robots | restore | XML/index + children | SEO | **OPEN_TECH `SM-CHILD-404`: advertises post/page/category children = 404; target two-child index not implemented** |
| `/sitemap-static.xml` | same | 200 | STATIC_HARDCODED | HIGH | Static URL inventory | physical XML / generator unknown | — | — | — | `sitemap-static.xml` | — | — | — | — | — | no | no | — | — | SFTP or proven generator | file+procedure | restore | XML/count/URLs | SEO | maintenance strategy OPEN: safe automation preferred, manual procedure fallback |
| `/wp-sitemap.xml` | same | 200 | WORDPRESS_CONTENT | HIGH | Working WordPress sitemap index | WordPress core sitemap provider | WP objects | — | WP sitemap | WordPress runtime | — | — | — | — | posts/pages/CPT/taxonomy | no | offers/glossary included per rules | — | — | WP hooks/settings only under charter | DB/theme/plugin scope | restore | index and representative children | SEO | target child of root `/sitemap.xml` |
| `/robots.txt` | same | 200 | STATIC_HARDCODED | HIGH | Robots policy | file/current runtime | — | — | — | `robots.txt` | — | — | — | — | — | no | no | disallow offer/* | — | SFTP careful | file | restore | directives | SEO | target after root repair: reference only `https://i-seo.su/sitemap.xml`; not yet implemented |
| `/wp-admin/` | admin | 200 | WORDPRESS_CONTENT | HIGH | Admin | WP core | — | — | — | wp-admin | — | — | — | — | — | no | no | JS cookie gate | — | Admin HITL / Playwright under charter | — | — | — | credentials local-only | — |
| `www.i-seo.su/*` | apex https | 301 | REDIRECT_OR_ALIAS | HIGH | Host alias | `.htaccess` | — | — | — | `.htaccess` | — | — | — | — | — | — | — | to `https://i-seo.su` | — | **do not edit** casually | htaccess | restore | redirect chain | routing | — |

\* `/services.html` also observed **500** once — re-validate when editing.

---

## Shared security, analytics, and source ownership

| Surface/path | Class | Runtime owner | Canonical MARS mirror | Safe edit route | Protected invariants | Current state |
|---|---|---|---|---|---|---|
| Root `*__FORM.php` (12) | HYBRID_COMPOSITE | thin root wrappers + shared send | `production-source/forms/` | exact form charter; keep delegates thin | server validation, honeypot, HMAC, limits, duplicate protection | hardened |
| `services/**/*__FORM.php` | HYBRID_COMPOSITE | thin delegates to root | `production-source/forms/` where mirrored | modify shared root/config unless delegate bug proven | no divergent recipients/security | delegates |
| `/iseo-form-config.php` | HYBRID_COMPOSITE | shared recipient/threshold/test config | `production-source/forms/iseo-form-config.php` | source/runtime bounded diff | recipient `nikel007i33@yandex.ru` only; `test_mode=false` | current |
| `/iseo-form-security.php` + token/runtime | HYBRID_COMPOSITE | shared validation/anti-spam | `production-source/forms/` | exact security charter | `contact_company_url`; ≈3s HMAC; ≈3/5m/form/IP; ≈10/h/IP; ≈10m duplicate | active |
| `/metrika-visitor-ip-config.php` | HYBRID_COMPOSITE | addon feature config | `production-source/metrika-ip/metrika-visitor-ip-config.php` | one-flag kill switch + source promotion | counter 54287016 unchanged; true→false disables only addon | ON |
| `/metrika-visitor-ip.php` | HYBRID_COMPOSITE | same-origin read-only endpoint | `production-source/metrika-ip/` | exact addon charter | validated IPv4/IPv6 `REMOTE_ADDR`; no forwarded headers | active |
| `/js/metrika-visitor-ip.js` | HYBRID_COMPOSITE | Metrika `ipaddress` params call | `production-source/metrika-ip/` | exact addon charter | no re-init, no auto-blocking, fail-open | active |
| `/js/common.js` | HYBRID_COMPOSITE | shared forms/calc/addon loader | `production-source/js/common.js` | minimal diff + broad route smoke | revenue/analytics shared dependency | active |
| `/css/main.css` | HYBRID_COMPOSITE | shared runtime CSS | `production-source/css/main.css` | runtime→diff→source promotion | preserve operator glossary/overflow hunks | aligned accepted baseline |
| Glossary theme files | WORDPRESS_CONTENT | active `iseoblog` theme | `wordpress/iseoblog-glossary/` | bounded theme/content charter | 184 public; hero/CTA/menu/title/related baseline | complete |

Any accepted operator runtime edit takes priority over an older mirror until it is reconciled by runtime → diff → canonical source promotion.

---

## Bulk marketing inventory

All `sitemap-static.xml` URLs (71) are **STATIC_HARDCODED** unless a physical file is missing (then WP may catch). Enumerate leaves under `services/` and `cases/` from that sitemap before mass edits.

---

## Quick decision tree

1. Does a physical file exist at the path? → **STATIC_HARDCODED** (or LEGACY if known twin).
2. Else WP page with hardcoded template and empty editor? → **WORDPRESS_TEMPLATE_STATIC_LIKE**.
3. Else WP + ACF/handlers/shared JS material? → **HYBRID_COMPOSITE**.
4. Else normal post/CPT/tax content? → **WORDPRESS_CONTENT**.
5. Else redirect? → **REDIRECT_OR_ALIAS**.
6. Else → **SAFE_UNKNOWN**.

---

*Canonical route ownership matrix v1 · current-state reconciliation 2026-08-24.*
