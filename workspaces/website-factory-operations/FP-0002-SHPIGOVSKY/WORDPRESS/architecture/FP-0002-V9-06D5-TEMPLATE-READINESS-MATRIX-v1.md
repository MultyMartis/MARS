# FP-0002 V9-06D.5 Template Readiness Matrix v1

**Date:** 2026-07-04  
**Phase:** V9-06D.5

## Source templates (canonical Git)

| Surface | File / family | State |
|---|---|---|
| Front page | `front-page.php` + `template-parts/home/*` | Skeleton orchestration; hero/parts are inert comments |
| Services hub | `page-templates/services-hub.php` | Skeleton; H1 + placeholder notice |
| Service single | `single-service.php` → leaf-stack default | Skeleton; layout meta filter not wired to ACF; stacks are inert comments |
| Contacts | `page-templates/contacts.php` | Skeleton; H1 + contacts partials (minimal) |
| Header / footer | `template-parts/layout/header.php`, `footer.php` | Present; unstyled lists |
| Permalinks | `plugins/shpigovsky-core/src/Permalinks/ServicePermalinks.php` | Depth-2 repaired (`service=$matches[1]/$matches[2]`) |

## Route classification

| Route | Classification | Reason | Next need |
|---|---|---|---|
| `/` | READY_FOR_V9_TEMPLATE_INTEGRATION | HTTP 200, non-blank skeleton | V9 home template integration |
| `/uslugi/` | READY_FOR_V9_TEMPLATE_INTEGRATION | HTTP 200, H1 visible, placeholder notice | V9 services-hub integration |
| `/uslugi/zavisimosti/` | READY_FOR_V9_TEMPLATE_INTEGRATION | HTTP 200, Service 73; inert service stack | V9 service subdivision template |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | READY_FOR_V9_TEMPLATE_INTEGRATION | HTTP 200, Service 74; inert leaf stack | V9 alcohol/leaf template |
| `/uslugi/psihicheskoe-zdorovie/` | READY_FOR_V9_TEMPLATE_INTEGRATION | HTTP 200, Service 77 | V9 service template |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | READY_FOR_V9_TEMPLATE_INTEGRATION | HTTP 200, Service 84 | V9 service template |
| `/kontakty/` | READY_FOR_V9_TEMPLATE_INTEGRATION | HTTP 200, H1 visible | V9 contacts template |

Secondary need for all seeded routes: **READY_FOR_CONTENT_MIGRATION_LATER** (minimal seed only; production content not migrated).

No route classified `NEEDS_TEMPLATE_REPAIR_BEFORE_INTEGRATION` or `ROUTE_BLOCKED`.

## Notes

- Service layout variant currently defaults to `leaf` for all services (ACF layout meta not driving stack selection yet).
- Visible service titles are absent in body (document `<title>` only). Integration must add real hero/title markup.
