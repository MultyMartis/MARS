# SITE-002-UX-TASK-INTAKE-01

**Site:** SITE-002 (ЗПМ / bzpm.ru)  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Issued:** 2026-07-07  
**Operation:** `SITE-002-PROD-UX-TASK-INTAKE-01` (OCPilot Run 4.217)  
**Type:** Read-only UX task intake audit baseline — **not** a Production mutation checkpoint  
**Parent checkpoint:** `SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01`

---

## Summary

Read-only intake for two operator UX tasks: new catalog section entry points (Лари, Кондитерский инвентарь) and PDP attribute «Дополнительные сведения» layout separation.

| Field | Value |
|-------|-------|
| Beget full backup | Operator confirmed before task |
| Production mutations | **0** |
| Task 01 tile gap | Лари + Кондитерский инвентарь in megamenu; **not** on homepage/hub `zpm-cat-card` grid |
| Task 02 attribute sample | **66/100** PDPs (66%) with «Дополнительные сведения» in spec table |
| Recommended Task 01 path | `category_visibility.php` branch IDs + category images (Run 4.195 pattern) |
| Recommended Task 02 path | Controller extraction in `product.php` + Twig block after specs toggle |
| Server monitor migration | **DEFERRED** — local Windows Task remains accepted |

Report: [SITE-002-PROD-UX-TASK-INTAKE-01.md](../reports/SITE-002-PROD-UX-TASK-INTAKE-01.md)
