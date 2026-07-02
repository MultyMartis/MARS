# CF-003 Pre-Implementation Inventory

**Date:** 2026-06-28  
**Family:** CF-003 — Internal upper navigation  
**Authority decision:** Hub (`.page-uslugi-v2`) wrapper geometry + breadcrumbs/subnav CSS; Subdivision wrapper geometry matches Hub; Leaf drift rejected.

---

## Canonical authority

| Criterion | Hub | Subdivision | Leaf | Selected |
|-----------|-----|-------------|------|----------|
| Wrapper gap (desktop) | 15px | 15px | 12px | **15px (Hub/Subdivision)** |
| Wrapper padding (desktop) | 0 | 0 | 16px/8px | **0 (Hub/Subdivision)** |
| Breadcrumbs font-size (desktop) | 14px / 18px lh | 14px / 14px lh | 12px / 12px lh | **14px / 18px lh (Hub)** |
| Subnav desktop layout | nowrap row | wrap | wrap | **nowrap row (Hub)** |
| Mobile wrapper gap | 8px + padding-top 8px | 5px | 12px/6px padding | **8px + padding-top 8px (Hub)** |

**Target class family:** `.internal-page-nav`  
**Target partial:** `partials/components/internal-page-nav.html`

---

## Page: Services Hub (`uslugi-v2.html`)

| Field | Value |
|-------|-------|
| Body class | `page-uslugi-v2` |
| Legacy wrapper | `.page-uslugi-v2__upper-nav.container` |
| DOM order | hero → upper-nav (breadcrumbs, subnav) → category sections |
| Breadcrumbs depth | Home → current (2 items) |
| Subnav links | 6 anchor links |
| ARIA | `breadcrumbs` nav + `services-page-subnav` nav |
| Desktop gap | 15px |
| Desktop padding | 0 |
| Mobile gap | 8px; padding-top 8px |
| Next section | `.services-category-section-v2` |

---

## Page: Service Subdivision (`usluga-podrazdel-v1.html`)

| Field | Value |
|-------|-------|
| Body class | `page-service-subdivision-v1` |
| Legacy wrapper | `.page-service-subdivision-v1__upper-nav.container` |
| DOM order | hero → upper-nav → dependencies section |
| Breadcrumbs depth | Home → Услуги → current (3 items) |
| Subnav links | 7 anchor links |
| Desktop gap | 15px |
| Desktop padding | 0 |
| Mobile gap | 5px (drift vs Hub) |
| Breadcrumbs CSS drift | muted colors, 4px list gap vs Hub 8px |
| Subnav CSS drift | wrap vs Hub nowrap; different border token |
| Next section | `.service-subdivision-dependencies-v1` |

---

## Page: Service Leaf (`usluga-konechnaya-v1.html`)

| Field | Value |
|-------|-------|
| Body class | `page-service-leaf-v1` |
| Legacy wrapper | `.page-service-leaf-v1__upper-nav.container` |
| DOM order | hero → upper-nav → intro section |
| Breadcrumbs depth | Home → Услуги → Зависимости → current (4 items) |
| Subnav links | 6 anchor links |
| Desktop gap | 12px (drift) |
| Desktop padding | 16px top / 8px bottom (drift) |
| Breadcrumbs | 12px typography (drift) |
| Subnav | wrap, 8px gap (drift) |
| Mobile overflow | on `__list` not nav wrapper (drift vs Hub) |
| Next section | `.service-leaf-intro-v1` |

---

## Shared partials (unchanged markup)

- `partials/components/breadcrumbs.html`
- `partials/components/services-page-subnav.html`

---

## CSS sources to consolidate

1. `.page-uslugi-v2__upper-nav` + `.page-uslugi-v2 .breadcrumbs*` + `.page-uslugi-v2 .services-page-subnav*` (+ mobile)
2. `.page-service-subdivision-v1__upper-nav` + page-scoped breadcrumbs/subnav (+ mobile)
3. `.page-service-leaf-v1__upper-nav` + page-scoped breadcrumbs/subnav (+ mobile)
4. Adjacent: `.page-uslugi-v2__upper-nav + .services-category-section-v2`

---

## Implementation target

```html
<div class="internal-page-nav">
  <div class="container">
    <!-- breadcrumbs include -->
    <!-- services-page-subnav include -->
  </div>
</div>
```

Single CSS block scoped under `.internal-page-nav` using Hub authority values.
