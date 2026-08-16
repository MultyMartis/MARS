# ENVIRONMENT-INVENTORY — PROD-P15

**Host:** http://shpigovsky.beget.tech/  
**Fresh drift:** 705/705 MATCH (0 prod drift) before mutations  
**Authority:** Beget FS = LIVE RUNTIME; Beget DB = content/settings; local WORDPRESS = source after drift check  

## Classification legend

- **CLEAN NOW** — safe to fix in P15  
- **KEEP UNTIL CUTOVER** — temporary Beget host / domain  
- **KEEP UNTIL SMTP** — mail deferred  
- **KEEP UNTIL INDEXING** — robots/noindex deferred  
- **LEGACY DATA — DO NOT TOUCH** — historical/guid/revision/evidence  
- **UNKNOWN / STOP** — not mutated  

---

## A. wp-config.php

| Item | Before | Class | P15 action |
|------|--------|-------|------------|
| WP_ENVIRONMENT_TYPE | `local` | CLEAN NOW | → `production` |
| WP_DEBUG | true | CLEAN NOW | → false |
| WP_DEBUG_DISPLAY | false | KEEP (already correct) | none |
| WP_DEBUG_LOG | true | CLEAN NOW | → false |
| SCRIPT_DEBUG | true | CLEAN NOW | → false |
| SAVEQUERIES | unset | KEEP | none |
| DISALLOW_FILE_EDIT | true | KEEP | none |
| WP_HOME / WP_SITEURL | unset (options own URLs) | KEEP UNTIL CUTOVER | none |
| DB_* / salts | present | LEGACY/secrets | DO NOT TOUCH |

## B. WordPress options

| Item | Before | Class | P15 action |
|------|--------|-------|------------|
| siteurl / home | http://shpigovsky.beget.tech | KEEP UNTIL CUTOVER | none |
| blogname | Шпиговский Дом | KEEP (proven identity) | none |
| blogdescription | empty | KEEP | none |
| admin_email | mli-fp0002@localhost.test | CLEAN NOW | → Info@shpigovsky.ru (proven `options_site_email`) |
| WPLANG | ru_RU | KEEP | none |
| timezone_string | Europe/Moscow | KEEP | none |
| permalink_structure | /blog/%postname%/ | KEEP | none |
| default_role | subscriber | KEEP | none |
| blog_public | 0 | KEEP UNTIL INDEXING | none |
| specialists_all_link_url | http://shpigovsky.test/specyalisty/ | CLEAN NOW | → beget host |
| comfort_all_link_url | http://shpigovsky.test/o-centre/galereya-o-dome/ | CLEAN NOW | → beget host |
| auto_core_update_notified | contains localhost.test email | LEGACY DATA | DO NOT TOUCH |
| acf_site_health | beget host | KEEP UNTIL CUTOVER | none |
| options_site_email | Info@shpigovsky.ru | KEEP | none |

## C. Live frontend `.test` (Home #4 postmeta)

| Key | Before | Class | P15 action |
|-----|--------|-------|------------|
| home_why_us_items_0_url | …/lechenie-alkogolnoy-zavisimosti/ | CLEAN NOW | host → beget |
| home_why_us_items_1..3_url | …/uslugi/zavisimosti/ | CLEAN NOW | host → beget |
| home_genotyping_link_url | …/profilakticheskiy-analiz/ | CLEAN NOW | host → beget |
| Revision postmeta (1329+) | same URLs | LEGACY DATA | DO NOT TOUCH |
| post.guid `*.test` | historical | LEGACY DATA | DO NOT TOUCH |

## D. MU plugins / guards

| Item | Class | P15 action |
|------|-------|------------|
| mars-local-runtime.php (local identity filename) | CLEAN NOW | replace with `fp02-pre-cutover-mail-suppression.php` |
| pre_wp_mail suppression | KEEP UNTIL SMTP | retain (reclassified) |
| Admin LOCAL notices | already removed P13 | none |
| siteurl/home write guard | already removed P13 | none |

## E. Debug artifacts

| Item | Class | P15 action |
|------|-------|------------|
| wp-content/debug.log (~9.8MB) | CLEAN NOW | archive to Storage; stop future logging |
| _tmp-e47-fix04-val/ | CLEAN NOW if QA-only | inspect → remove if proven temp |
| mars-runtime/ | UNKNOWN | inspect; do not delete root blindly |
| core.zip / dumps in public_html | not found at known names | none |

## F. Indexing / robots / sitemap

| Item | Class | P15 action |
|------|-------|------------|
| blog_public=0 | KEEP UNTIL INDEXING | none |
| robots.txt Disallow + Sitemap | KEEP UNTIL INDEXING | none |
| /wp-sitemap.xml | KEEP (dynamic) | verify only |

## G. Source validation / ACF admin help

| Item | Class | P15 action |
|------|-------|------------|
| WORDPRESS/validation/*.php `.test` | LEGACY / local tools | DO NOT TOUCH |
| ACF JSON admin help links to shpigovsky.test/wp-admin | Admin residue | KEEP (not FE); optional later |
| ACF field posts with .test in notice HTML | Admin residue | KEEP |

## H. Typography residual

| Item | Class | P15 action |
|------|-------|------------|
| Broad WYSIWYG/ACF typography | NEXT WAVE | DO NOT START |

## Required gates tracked

- WP_ENVIRONMENT_TYPE = PRODUCTION  
- NO FRONTEND DEBUG OUTPUT  
- NO STALE LOCAL-RUNTIME IDENTITY  
- MAIL DEFERRED UNTIL SMTP  
- INDEXING INTENTIONALLY CLOSED  
- NO LIVE FRONTEND `.test` / LOCALHOST  
- SITEURL/HOME NOT PREMATURELY CUT OVER  
