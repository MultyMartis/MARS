# ISEO-SU CANONICAL ROUTE OWNERSHIP MATRIX v1

**Programme:** ISEO-SU-SITE-OPS  
**Authority rank:** #3 (after task evidence + task routing guide)  
**Companion:** [ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md](ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md)  
**Evidence:** 2026-07-24 read-only discovery  

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
| `/glossary/` | `…/glossary/` | 200 anon | WORDPRESS_CONTENT | HIGH | Glossary archive (public) | CPT `glossary` + `archive-glossary.php` | glossary CPT | — | archive-glossary.php | theme `archive-glossary.php` | theme+css | theme | search GET only | glossary ACF | **glossary** | yoast/wp sitemap | no header | slash alias | — | published only; exposure true | theme+DB | publish→draft + exposure false | public hub | non-eligible stay draft | menu deferred |
| `/glossary/{slug}/` | same | 200 published | WORDPRESS_CONTENT | HIGH | Glossary term | CPT `glossary` + `single-glossary.php` | glossary | slug | single-glossary.php | theme `single-glossary.php` | theme+css | theme | — | synonyms/related | **glossary** | yoast/wp | — | — | — | publish eligible only | DB | draft rollback | public singles | no non-eligible publish | related links gated |
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
| `/sitemap.xml` | same | 200 | STATIC_HARDCODED | HIGH | Canonical sitemap index | physical file → static + wp-sitemap | — | — | — | `sitemap.xml` | — | — | — | — | — | no | no | — | — | SFTP file | file | restore | index lists static+WP only | SEO | HIGH FIX WAVE 01 |
| `/sitemap-static.xml` | same | 200 | STATIC_HARDCODED | HIGH | Static URL inventory | allowlist + completeness inventory + generator (**127** URLs) | — | — | — | `sitemap-static.xml` | — | — | — | — | — | no | no | — | — | SFTP + regen | file | restore | count/URLs + completeness=0 | SEO | keep allowlist≡inventory |
| `/robots.txt` | same | 200 | STATIC_HARDCODED | HIGH | Robots | file | — | — | — | `robots.txt` | — | — | — | — | — | no | no | disallow offer/* | — | SFTP careful | file | restore | directives | SEO | — |
| `/wp-admin/` | admin | 200 | WORDPRESS_CONTENT | HIGH | Admin | WP core | — | — | — | wp-admin | — | — | — | — | — | no | no | JS cookie gate | — | Admin HITL / Playwright under charter | — | — | — | credentials local-only | — |
| `www.i-seo.su/*` | apex https | 301 | REDIRECT_OR_ALIAS | HIGH | Host alias | `.htaccess` | — | — | — | `.htaccess` | — | — | — | — | — | — | — | to `https://i-seo.su` | — | **do not edit** casually | htaccess | restore | redirect chain | routing | — |

\* `/services.html` also observed **500** once — re-validate when editing.

---

## Bulk marketing inventory

All `sitemap-static.xml` URLs (**127**) are **STATIC_HARDCODED** unless a physical file is missing (then WP may catch). Enumerate leaves under `services/` and `cases/` from that sitemap before mass edits. Completeness authority: `data/sitemaps/public-canonical-static-routes-v1.txt`.

---

## Quick decision tree

1. Does a physical file exist at the path? → **STATIC_HARDCODED** (or LEGACY if known twin).
2. Else WP page with hardcoded template and empty editor? → **WORDPRESS_TEMPLATE_STATIC_LIKE**.
3. Else WP + ACF/handlers/shared JS material? → **HYBRID_COMPOSITE**.
4. Else normal post/CPT/tax content? → **WORDPRESS_CONTENT**.
5. Else redirect? → **REDIRECT_OR_ALIAS**.
6. Else → **SAFE_UNKNOWN**.

---

*Canonical route ownership matrix v1 · 2026-07-24.*
