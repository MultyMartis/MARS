# FP-0002 V9-04 Page-to-Template Map v1

**Date:** 2026-07-02

## Minimum template family

| Template ID | PHP file | Routes served | Variants |
|-------------|----------|---------------|----------|
| TPL-FRONT-PAGE | `front-page.php` | `/` | approved-full |
| TPL-SERVICES-HUB | `templates/page-services-hub.php` | `/uslugi/` | approved-full |
| TPL-SERVICE-SUBDIVISION | `templates/page-service-subdivision.php` | subdivision routes | full + placeholder |
| TPL-SERVICE-LEAF | `templates/page-service-leaf.php` | leaf routes | full-alcohol-exception + placeholder |
| TPL-INSTITUTIONAL | `templates/page-institutional.php` | `/o-centre/` + children | full + placeholder |
| TPL-REVIEWS | `templates/page-reviews.php` | `/otzyvy/` | approved-full |
| TPL-CONTACTS | `templates/page-contacts.php` | `/kontakty/` | approved-full |
| TPL-LEGAL | `templates/page-legal.php` | 4 legal routes | legal-demo |
| TPL-PLACEHOLDER | `templates/page-placeholder.php` | fallback | generic |
| TPL-BLOG-ARCHIVE | `home.php` | `/blog/` | approved-full |
| TPL-BLOG-SINGLE | `single.php` | posts | approved-full |
| TPL-PAGE | `page.php` | safety fallback | generic |

## Shared components per family

All templates include: head, header, footer, global modal (once), scroll-to-top (once), breadcrumbs.

**Do not** collapse alcohol dependence full page into placeholder leaf template.
