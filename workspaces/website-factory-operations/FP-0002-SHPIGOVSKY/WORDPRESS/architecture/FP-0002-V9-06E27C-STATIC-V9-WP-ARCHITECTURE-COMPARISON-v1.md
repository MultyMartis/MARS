# FP-0002 V9-06E27C — Static V9 vs WP Architecture Comparison

**Static authority:** `workspaces/fp-0002-shpigovsky-v9/tools/v9-route-manifest.json`  
**Evidence:** `validation/v9-06e27c-page-service-ownership-decision/static-v9-wp-architecture-comparison.json`

## Conflicted subdivision routes

| Route | Static V9 role | Static status | WP page | WP service | Rendered owner | Recommended owner |
|---|---|---|---|---|---|---|
| `/uslugi/zavisimosti/` | SERVICE_SUBDIVISION | APPROVED_FULL | `#6` (shadow) | `#73` | service `#73` | **service `#73`** |
| `/uslugi/psihicheskoe-zdorovie/` | SERVICE_SUBDIVISION | PLACEHOLDER | `#7` (shadow) | `#77` | service `#77` | **service `#77`** |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | SERVICE_SUBDIVISION | PLACEHOLDER | `#8` (shadow) | `#84` | service `#84` | **service `#84`** |

## Architecture alignment

| Surface | Intent |
|---|---|
| Static V9 | Subdivision routes = service family templates (`usluga-podrazdel-v1`) |
| WP architecture doc | Hub `/uslugi/` = page; subdivisions + leaves = hierarchical service CPT |
| `ServicePermalinks.php` | Child `/uslugi/*` paths claimed by service rewrite rules |
| Current runtime | Already aligned with service CPT — legacy pages are migration residue |

## Hub (no conflict)

| Route | Static V9 | WP | Owner |
|---|---|---|---|
| `/uslugi/` | SERVICES_HUB | page `#5` | page `#5` ✓ |

## Out-of-scope gap (informational)

`/uslugi/zavisimosti/specialistam/` exists in static V9 manifest but has **no** service CPT object and returns HTTP 404. Not part of pages `#6/#7/#8` ownership debt; track under future service seeding.
