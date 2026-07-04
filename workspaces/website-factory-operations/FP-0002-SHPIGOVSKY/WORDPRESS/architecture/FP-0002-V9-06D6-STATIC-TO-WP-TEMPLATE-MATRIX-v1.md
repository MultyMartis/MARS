# FP-0002 V9-06D.6 Static-to-WP Template Matrix v1

**Date:** 2026-07-04

| ID | V9 source | WP template | ACF groups | Current gap | Wave |
|---|---|---|---|---|---|
| home | `src/pages/index.html` | `front-page.php` | ['group_fp02_page_home'] | inert home partials; no V9 CSS/JS; many V9 sections lack dedicated WP partials/ACF fields | D7-B |
| services_hub | `src/pages/uslugi.html` | `page-templates/services-hub.php` | ['group_fp02_page_services_hub'] | H1 + placeholder only; no category hub markup; service cards not queried | D7-C |
| service_parent_zavisimosti | `src/pages/usluga-podrazdel-v1.html` | `single-service.php → subdivision-stack.php` | ['group_fp02_service_layout_hero', 'group_fp02_service_structured_sections', 'group_fp02_service_faq'] | layout variant not ACF-wired (defaults leaf); inert partials; Page6/Service73 path debt | D7-D |
| service_child_alcohol | `src/pages/usluga-konechnaya-v1.html` | `single-service.php → alcohol-stack.php` | ['group_fp02_service_layout_hero', 'group_fp02_service_structured_sections', 'group_fp02_service_faq'] | seeded layout/hero/intro/signs but inert partials; alcohol-special not selected by loader | D7-D |
| service_parent_psych | `src/pages/uslugi/psihicheskoe-zdorovie.html` | `single-service.php → subdivision-stack.php` | ['group_fp02_service_layout_hero'] | V9 is placeholder; minimal seed only; use subdivision + placeholder notice until content wave | D7-D |
| service_parent_rpp | `src/pages/uslugi/rasstroystva-pischevogo-povedeniya.html` | `single-service.php → subdivision-stack.php` | ['group_fp02_service_layout_hero'] | V9 is placeholder; minimal seed only | D7-D |
| contacts | `src/pages/kontakty.html` | `page-templates/contacts.php` | ['group_fp02_page_contacts'] | H1 + inert/minimal contacts partials; options not seeded | D7-E |
| global_header | `src/partials/layout/header.html` | `header.php → template-parts/layout/header.php` | [] | unstyled skeleton list nav | D7-A |
| global_footer | `src/partials/layout/footer.html` | `footer.php → template-parts/layout/footer.php` | ['group_fp02_site_options_contacts', 'group_fp02_site_options_modal_cta'] | unstyled skeleton footer; modal inert; forms disabled | D7-A |

Machine-readable: `FP-0002-V9-06D6-STATIC-TO-WP-TEMPLATE-MATRIX-v1.json`

## Result

COMPLETE
