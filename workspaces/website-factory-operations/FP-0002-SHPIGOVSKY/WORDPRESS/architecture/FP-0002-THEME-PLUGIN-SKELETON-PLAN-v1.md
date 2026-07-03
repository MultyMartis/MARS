# FP-0002 V9-06A Theme and Plugin Skeleton Plan

**Task:** V9-06A.1 / V9-06C update | **Date:** 2026-07-04
**Status:** Design complete — **V9-06B skeleton implemented**; **V9-06C content model source implemented**; runtime delivery not performed.

---

## Theme `theme/shpigovsky/`

| Path | Responsibility |
|------|----------------|
| `style.css` | Theme header metadata |
| `functions.php` | Bootstrap inc/* |
| `header.php` | Global header wrapper |
| `footer.php` | Global footer + modal + scroll |
| `front-page.php` | Home orchestration |
| `home.php` | Blog archive |
| `page.php` | Fallback page |
| `single.php` | Blog article |
| `single-service.php` | Service router by layout meta |
| `404.php` | Not found |
| `search.php` | Optional search |
| `page-templates/*.php` | Hub, institutional, reviews, contacts, legal |
| `inc/setup.php` | Supports, menus |
| `inc/assets.php` | Enqueue V9 build assets |
| `inc/template-tags.php` | Breadcrumbs, helpers |
| `inc/service-template-loader.php` | Layout meta → stack partial |
| `template-parts/**` | V9 partial ports |
| `assets/css/`, `assets/js/`, `assets/img/` | Built from V9 pipeline |
| `languages/` | i18n |

**Complexity:** Moderate — follows gulp-starter port pattern; no framework.

---

## Plugin `plugins/shpigovsky-core/`

| Path | Responsibility |
|------|----------------|
| `shpigovsky-core.php` | Plugin bootstrap |
| `src/ContentTypes/Service.php` | Register `service` CPT |
| `src/Taxonomies/` | Empty — taxonomy rejected |
| `src/Fields/AcfIntegration.php` | JSON load/save paths; ACF Pro dependency check; dependency notices |
| `src/Fields/FieldGroups.php` | V9-06C ACF Pro local field group source definitions |
| `src/Fields/RepeaterValidation.php` | Server-side repeater bound enforcement and field validation hooks |
| `src/Migrations/` | Versioned data migrations |
| `src/Forms/ConsultationHandler.php` | Form POST handler |
| `src/Admin/OptionsPage.php` | Register options |
| `src/Admin/EditorRestrictions.php` | Hide block editor where needed |
| `inc/compat.php` | ACF active check |
| `languages/` | i18n |

**Complexity:** Moderate — no custom framework; explicit classes per concern.

---

## Delivery note

Skeleton implementation completed in **V9-06B**. See [FP-0002-V9-06B-SKELETON-IMPLEMENTATION-REPORT-v1.md](../reports/FP-0002-V9-06B-SKELETON-IMPLEMENTATION-REPORT-v1.md).

## V9-06B.2 dependency boundary

The skeleton remains source-only and inert. ACF PRO is available as an operator-managed runtime dependency for later public API integration, but no ACF groups, runtime JSON, CPT activation, options pages, or field registration were created in V9-06B.2.

## V9-06C source implementation boundary

Content model source is implemented in Shpigovsky Core and ACF JSON source is generated. `SHPIGOVSKY_CORE_SKELETON` remains `true`, so the source is not registered in runtime until a later explicitly authorized delivery phase.

