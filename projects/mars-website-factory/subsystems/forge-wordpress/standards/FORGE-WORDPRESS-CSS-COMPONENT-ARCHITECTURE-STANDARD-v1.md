# Forge WordPress — CSS and component architecture standard v1

**ID:** FW-S-35  
**Status:** ACTIVE — CANONICAL DEFAULT  
**Date:** 2026-08-18  
**Evidence:** FP-0002 theme: large `v9-style.css` plus `fp02-*.css` extras; operator CSS drift (AP-003); duplicate visual owners

---

## 1. CSS layers (ownership)

| Layer | Contains | Owner file pattern |
|-------|----------|--------------------|
| Tokens / root | custom properties | one foundation file |
| Base | reset, html/body, typography defaults | base |
| Layout | containers, grids, header/footer shells | layout |
| Components | one file or block per component family | components |
| Page / template scope | **last resort** overrides for a named template | `page-{name}` only |
| Utilities | spacing/visibility **only where justified** | utilities |
| Responsive overrides | same owners, inside the component/layout file | no orphan media-query dumps |

Do not spread one-off selectors across a 10k-line dump plus three “hotfix” files for the same card.

---

## 2. Component ownership (one owner)

Each UI component has exactly one:

| Owner | Artifact |
|-------|----------|
| Markup | theme template-part or documented plugin-rendered HTML |
| CSS | one canonical stylesheet (or one BEM root in the foundation file) |
| JS | one module ([FRONTEND-INTERACTION-OWNERSHIP](FORGE-WORDPRESS-FRONTEND-INTERACTION-OWNERSHIP-STANDARD-v1.md)) |
| CMS/data | [COMPONENT-DATA-CONTRACT](FORGE-WORDPRESS-COMPONENT-DATA-CONTRACT-STANDARD-v1.md) |

Do **not** implement the same card/header/modal in several unrelated templates with divergent class names.

Track instances in [COMPONENT-INVENTORY](../templates/FORGE-WORDPRESS-COMPONENT-INVENTORY-TEMPLATE-v1.md).

---

## 3. Forbidden as ordinary architecture

| Pattern | Why |
|---------|-----|
| Arbitrary one-off selectors in unrelated files | undiscoverable; drift |
| Specificity escalation / selector wars | next fix uses `!important` |
| `!important` as default | reserved for proven third-party override |
| Duplicate component owners | two headers, two CTAs |
| Styling by fragile DOM accident (`article > div > div:nth-child(3)`) | editor/ACF changes break it |
| Hand-editing `dist/` or live CSS as SoT | AP-003 |

---

## 4. Enqueue

- Named handles + file versions (filemtime or release SHA)  
- Page-scope CSS only on the templates that need it  
- Admin CSS in Admin only  
- Vendor (Swiper, Fancybox) loaded **once**, owned by the interaction that needs it  

---

## 5. Factory → WordPress

If markup/SCSS originated in Website Factory: preserve BEM/class names unless a WAD renames them. Canonize production CSS **into source** before the next deploy.

---

*FW-S-35 v1.*
