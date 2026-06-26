# FP-0002 SERVICE SUBDIVISION — DEPENDENCIES BORDER REMOVAL v1

- Selector: `.page-service-subdivision-v1 .service-subdivision-dependencies-v1 .services-category-section-v2__service`
- Removed declaration: `border-bottom: var(--border-width) solid var(--color-border-subtle);`
- Preserved: padding, flex layout, typography, link alignment, responsive rules, `:last-of-type` rule
- Desktop computed border (4 rows): `border-bottom-width: 0px`, `border-bottom-style: none`
- Mobile: same scoped rule — no row dividers
- Other pages affected: **none** (scoped selector only)
- Verdict: **PASS**
