# FP-0002 V9-06E27C — Route Ownership Audit

**Evidence:** `validation/v9-06e27c-page-service-ownership-decision/route-ownership-audit.json`

## Conflict routes (high severity)

| Route | HTTP | WP queried object | Template | Current owner | Menu owner | Conflict |
|---|---:|---|---|---|---|---|
| `/uslugi/zavisimosti/` | 200 | service `#73` | `single-service.php` subdivision | service `#73` | page `#6` (item `#301`) | **HIGH** |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | service `#77` | `single-service.php` subdivision | service `#77` | — | **HIGH** (shadow page `#7`) |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | service `#84` | `single-service.php` subdivision | service `#84` | — | **HIGH** (shadow page `#8`) |

## Non-conflict reference routes

| Route | HTTP | Owner | Template | Notes |
|---|---:|---|---|---|
| `/uslugi/` | 200 | page `#5` | `services-hub.php` | Canonical hub — correct |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 200 | service `#74` | leaf | Child of `#73` |
| `/uslugi/zavisimosti/profilakticheskiy-analiz/` | 200 | service `#75` | leaf | Child of `#73` |
| `/uslugi/zavisimosti/specialistam/` | 404 | — | — | Static V9 route; no WP service object (separate gap) |

## Body-class evidence

- `/uslugi/zavisimosti/`: `single-service postid-73 page-service-subdivision-v1` — **not** `page-id-6`
- Canonical URL header: `http://shpigovsky.test/uslugi/zavisimosti/` → service permalink

## Conclusion

**Runtime route owner = service CPT** for all three conflicted subdivision paths. Legacy pages exist in DB but do not win HTTP resolution.
