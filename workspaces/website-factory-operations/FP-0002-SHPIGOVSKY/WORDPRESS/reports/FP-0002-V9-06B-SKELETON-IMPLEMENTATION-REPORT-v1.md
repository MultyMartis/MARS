# FP-0002 V9-06B Skeleton Implementation Report v1

**Task:** V9-06B | **Date:** 2026-07-03  
**Result:** PASS (static validation)

---

## Summary

Canonical WordPress source skeleton implemented for FP-0002 under `WORDPRESS/theme/shpigovsky/` and `WORDPRESS/plugins/shpigovsky-core/`. Theme establishes template hierarchy, global shell boundaries, navigation locations, and inert template-part placeholders. Plugin establishes namespace/autoload boundary, `ModuleInterface` contracts, and bounded module stubs — all gated by skeleton mode with **no runtime model registration**.

---

## OD-002 authority (final)

| Field | Value |
|-------|-------|
| Legacy route | `/specyalisty/` |
| Canonical route | `/uslugi/zavisimosti/specialistam/` |
| Canonical entity | `SVC-SPECIALISTAM-ZAV` |
| Redirect | 301 after canonical Service returns HTTP 200 — **not implemented in V9-06B** |

Superseded: `/specyalisty/` → `/specialistam/` — recorded in [FP-0002-OD-002-ROUTE-AUTHORITY-v1.md](../architecture/FP-0002-OD-002-ROUTE-AUTHORITY-v1.md).

---

## Deliverables

### Theme (`theme/shpigovsky/`)

- Root templates: `index`, `front-page`, `home`, `page`, `single`, `single-service`, `404`, `search`
- Page templates: `services-hub`, `institutional`, `reviews`, `contacts`, `legal`
- Inc: `setup`, `assets`, `template-tags`, `service-template-loader`
- Template-parts: full hierarchy per `FP-0002-WORDPRESS-TEMPLATE-HIERARCHY-v1.md`
- Menu locations: `primary`, `footer_services`, `footer_o_centre`, `legal`
- Skeleton constant: `SHPIGOVSKY_THEME_SKELETON`

### Plugin (`plugins/shpigovsky-core/`)

- Namespace: `Shpigovsky\Core`
- Autoloader: `src/Loader/Autoloader.php`
- Contract: `src/Contracts/ModuleInterface.php`
- Modules (inert in skeleton): ContentTypes, Permalinks, Fields, Settings, Migrations, Forms, Admin
- Taxonomies: rejected — empty `src/Taxonomies/`
- Skeleton constant: `SHPIGOVSKY_CORE_SKELETON`
- Legacy `includes/class-bootstrap.php` removed

---

## Safety confirmation

| Boundary | Value |
|----------|------:|
| Runtime filesystem writes | 0 |
| Database writes | 0 |
| WordPress object writes | 0 |
| WPilot writes | 0 |
| ACF Pro install | 0 |
| Service CPT registered at runtime | no |
| Redirect implemented | no |

---

## Validation

```text
node WORDPRESS/validation/FP-0002-V9-06B-SKELETON-VALIDATION.mjs
```

Machine result: **PASS** (see validation output artifact in task closeout).

---

## Phase status

| Phase | Status |
|-------|--------|
| V9-06A | COMPLETE |
| V9-06A.1 | COMPLETE |
| V9-06B | **COMPLETE** |
| V9-06C | READY FOR OPERATOR AUTHORIZATION |

---

*Report generated as part of V9-06B skeleton implementation — no runtime delivery.*
