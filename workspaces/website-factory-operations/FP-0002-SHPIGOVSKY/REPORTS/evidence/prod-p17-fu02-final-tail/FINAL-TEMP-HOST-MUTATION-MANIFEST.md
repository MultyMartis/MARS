# FINAL TEMPORARY-HOST MUTATION MANIFEST

**Wave:** P17-FU02  
**Current host:** `http://shpigovsky.beget.tech`  
**Final host:** `https://shpigovsky.ru`  
**Required token:** `FINAL DOMAIN MUTATION SET IS EXACT AND BOUNDED`

Machine-readable: `FINAL-TEMP-HOST-MUTATION-MANIFEST.json`

Classification:

| Class | Meaning |
|-------|---------|
| A | MUST CHANGE DURING CUTOVER (exact object) |
| B | DYNAMIC — follows `home`/`siteurl` automatically |
| C | TEMPORARY HOST INFRA — intentionally remains |
| D | HISTORICAL — ignore |
| E | EXTERNAL — intentional |

No UNKNOWN live-impacting occurrence remains.

## A — must change (exact)

| Owner | Object | Current | Final pattern |
|-------|--------|---------|---------------|
| WP options | `siteurl` | `http://shpigovsky.beget.tech` | `https://shpigovsky.ru` |
| WP options | `home` | `http://shpigovsky.beget.tech` | `https://shpigovsky.ru` |
| ACF options | `fp02-block-specialists_specialists_all_link_url` | `http://shpigovsky.beget.tech/specyalisty/` | `https://shpigovsky.ru/specyalisty/` |
| ACF options | `fp02-block-comfort_comfort_all_link_url` | `http://shpigovsky.beget.tech/o-centre/galereya-o-dome/` | `https://shpigovsky.ru/o-centre/galereya-o-dome/` |
| ACF postmeta | `home_genotyping_link_url` on publish post **4** (revisions 2034/2036 optional) | `http://shpigovsky.beget.tech/uslugi/genotipirovenie/` | `https://shpigovsky.ru/uslugi/genotipirovenie/` |
| ACF postmeta | `home_why_us_items_{0-3}_url` on publish post **4** | beget absolute paths below | same path on https://shpigovsky.ru |
| ACF postmeta | `section_approach_more_url` on **73, 77, 84** (rev 2037 optional) | `http://shpigovsky.beget.tech/o-centre/programma-lecheniya/` | `https://shpigovsky.ru/o-centre/programma-lecheniya/` |
| ACF postmeta | `section_nature_genotyping_link_url` on **73** | `http://shpigovsky.beget.tech/uslugi/zavisimosti/profilakticheskiy-analiz/` | `https://shpigovsky.ru/uslugi/zavisimosti/profilakticheskiy-analiz/` |
| ACF postmeta | `service_general_approach_more_url` on 27 service IDs listed in JSON | `http://shpigovsky.beget.tech/o-centre/programma-lecheniya/` | `https://shpigovsky.ru/o-centre/programma-lecheniya/` |
| robots.txt | Sitemap absolute URL | `http://shpigovsky.beget.tech/wp-sitemap.xml` | `https://shpigovsky.ru/wp-sitemap.xml` (PHASE C / indexing) |
| `.htaccess` | host/HTTPS rules | none for final host | PHASE A after SSL (see file plan) |

Home why-us current values:

- `0` → `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`
- `1`/`2`/`3` → `/uslugi/zavisimosti/`

Method: exact option/meta write (string URLs). **Not** serialized PHP. **Not** broad `SEARCH REPLACE` SQL.

## B — dynamic

- Canonical tags, `admin_url`, attachment URLs derived from `home`/`siteurl`, menus that store object IDs (empty `_menu_item_url` for pages), theme `home_url()` links.
- Live HTML currently shows many `shpigovsky.beget.tech` hrefs; they change when `home` changes.
- Post `guid` (119 rows): WordPress internal; frontend media uses `_wp_attached_file` + siteurl.

## C — temporary host infra

- Beget vhost / alias `shpigovsky.beget.tech` itself.
- Post-cutover desired 301 from this host is Host-conditional (file plan PHASE A, after smoke).

## D — historical / ignore

- Post GUIDs containing beget or `shpigovsky.test`.
- Revisions still containing `new-site.space` after live content fix (2 revisions of post 750; 4 revision meta rows).
- `auto_core_update_notified` email `mli-fp0002@localhost.test` (core option, not a user).
- Disabled ACF field-group posts mentioning localhost in admin help HTML.
- ACF field notice HTML pointing at `shpigovsky.test/wp-admin` (admin-only).
- `acf_site_health` `activated_url` (ACF plugin telemetry JSON; not public). Leave unless ACF admin requires it; if updated, JSON-safe write only.

## E — external

- None required for launch. Public phones/emails are production contacts, not temp-host.

## Live frontend residue closed this wave

- `https://shpigovsky-wp.new-site.space/wp-content/uploads/...` on publish post **750** and live `generic_page_body` → host stripped to site-relative `/wp-content/uploads/...` (host-independent).
