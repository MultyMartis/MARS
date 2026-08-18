# ISEO-SU PUBLIC ROUTE REGISTER v1

**Programme:** ISEO-SU-SITE-OPS  
**Phase:** 2B — read-only production audit  
**Status:** EXPANDED from root-only intake  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  
**Last updated:** 2026-07-24  

## Rules

- Populate from operator-provided URLs **or** authorized Phase 2B read-only evidence (SFTP + public GET/REST).  
- No secrets.  
- WordPress Admin URL remains an admin interface URL, not a marketing route.

## Field definitions

| Field | Meaning |
|-------|---------|
| **route ID** | Stable ID |
| **public URL/path** | Public path or URL |
| **page purpose** | Plain-language purpose |
| **preliminary owner** | static / WordPress / hybrid / unknown |
| **owner classification** | Boundary class |
| **business criticality** | high / medium / low / unknown |
| **expected renderer** | static HTML / WordPress / hybrid / other |
| **related tool** | calculator, tariffs, forms, offers, report-hub, none |
| **evidence source** | Who/what supplied |
| **status** | CANDIDATE / ACCEPTED / INTAKE / DEFERRED |
| **SAFE UNKNOWN notes** | Open questions |

---

## Register

| route ID | public URL/path | page purpose | preliminary owner | owner classification | business criticality | expected renderer | related tool | evidence source | status | SAFE UNKNOWN notes |
|----------|-----------------|--------------|-------------------|----------------------|----------------------|-------------------|--------------|-----------------|--------|--------------------|
| R-001 | https://i-seo.su/ | Homepage | hybrid | SHARED_BUT_WORDPRESS_RENDERED | HIGH | WP page template with static-like markup | calculator, tariffs, forms | Phase 2B REST + public GET + theme `page-home.php` | ACCEPTED | Parallel `home.html` drift |
| R-002 | https://i-seo.su/home.html | Homepage file copy | static | STATIC_FILE_OWNED | MEDIUM | PHP-capable HTML file | calculator, tariffs | Phase 2B SFTP + GET | ACCEPTED | Not primary `/` |
| R-003 | https://i-seo.su/blog/ | Blog | WordPress | WORDPRESS_OWNED | HIGH | WordPress | none | Phase 2B GET generator + WP page `blog` | ACCEPTED | |
| R-004 | https://i-seo.su/blog.html | Legacy/static blog file | static | STATIC_FILE_OWNED | LOW | PHP-capable HTML | none | Phase 2B SFTP | ACCEPTED | Not live `/blog/` |
| R-005 | https://i-seo.su/tariff-calc | Tariff calculator page | WordPress | WORDPRESS_OWNED | HIGH | WP template `page-tariffcalc.php` | calculator, tariffs | Phase 2B REST | ACCEPTED | |
| R-006 | https://i-seo.su/offers | Offers / proposals listing | WordPress | WORDPRESS_OWNED | HIGH | WP page | offers CPT (web-KP candidate) | Phase 2B REST | ACCEPTED | Confirm if this is “web-KP” |
| R-007 | https://i-seo.su/services.html | Services hub | static | STATIC_FILE_OWNED | HIGH | PHP-capable HTML | forms | Phase 2B SFTP + sitemap-static | ACCEPTED | |
| R-008 | https://i-seo.su/services/seo.html | SEO services | static | STATIC_FILE_OWNED | HIGH | PHP-capable HTML | calculator, tariffs, forms | Phase 2B | ACCEPTED | |
| R-009 | https://i-seo.su/services/** | Service leaf pages | static | STATIC_FILE_OWNED | HIGH | PHP-capable HTML | forms | Phase 2B tree + sitemap-static (71 URLs) | ACCEPTED | Enumerate further in passport |
| R-010 | https://i-seo.su/cases/** | Case studies | static | STATIC_FILE_OWNED | MEDIUM | PHP-capable HTML | forms | Phase 2B SFTP | ACCEPTED | |
| R-011 | https://i-seo.su/contacts.html | Contacts | static | STATIC_FILE_OWNED | HIGH | PHP-capable HTML | forms | Phase 2B | ACCEPTED | |
| R-012 | https://i-seo.su/about.html | About | static | STATIC_FILE_OWNED | MEDIUM | PHP-capable HTML | forms | Phase 2B | ACCEPTED | |
| R-013 | https://i-seo.su/report-hub/ | Report Hub app | external/static | EXTERNAL_TOOL | MEDIUM | Static HTML app | report-hub | Phase 2B SFTP | ACCEPTED | Sibling product surface |
| R-014 | https://i-seo.su/wp-admin/ | WordPress Admin | admin | n/a (not marketing) | HIGH | WordPress Admin | — | Operator Wave A | ACCEPTED (admin) | JS challenge for non-browser clients |

Additional root marketing pages observed on disk (not each given an ID yet): `reviews.html`, `partners.html`, `bonuses.html`, `career.html`, `guarantees.html`, `privacy-policy.html`, `user-agreement.html`, `cookie-files-policy.html`, etc.

---

## Intake notes

| Note | Classification |
|------|----------------|
| Architecture is hybrid root WP + physical HTML trees | CONFIRMED BY SANITIZED EVIDENCE (Phase 2B) |
| `sitemap-static.xml` lists 71 static URLs | CONFIRMED BY SFTP |
| Web-KP dedicated URL | SAFE UNKNOWN (candidates R-006 / CPT `offer`) |
| Agent public GETs in Phase 2B were limited to classification samples under explicit audit charter | Task-authorized |

---

*Public route register v1 · updated 2026-07-24 Phase 2B.*
