# Forge WordPress — Navigation Standard v1

**ID:** FW-S-15  
**Status:** ACTIVE — PRODUCTION PROVEN WITH CAVEATS  
**Date:** 2026-08-18  
**Class:** A / F  
**Evidence:** FP-0002 P13 L2 desktop + mobile accordion

---

## 1. Canonical model

Use **normal WordPress menus** (`wp_nav_menu` + walker). Do not invent a parallel menu CPT or hardcoded IA tree (unless WAD).

| Surface | Behavior |
|---------|----------|
| Desktop ≥ breakpoint | Second-level dropdown; `focus-within`; parent remains a **link** |
| Mobile | Accordion; **separate expand button** from the parent link |
| Keyboard | Tab into items; Escape closes; visible `:focus-visible` |
| ARIA | `aria-expanded` on the expand control; controls/id pairing |
| Closed | No hover-only traps; no layout shift on hover |

---

## 2. Acceptance checklist

| # | Check |
|---|--------|
| 1 | Menu editable in WP Admin Appearance → Menus |
| 2 | Parent URL works (not only toggle) |
| 3 | Mobile expand does not navigate away |
| 4 | One submenu open policy documented (accordion) |
| 5 | Escape closes open submenus / offcanvas |
| 6 | Offcanvas scroll-lock does not jump `scrollY` (floating header lesson) |
| 7 | No second proprietary menu model |

---

*FW-S-15 v1.*
