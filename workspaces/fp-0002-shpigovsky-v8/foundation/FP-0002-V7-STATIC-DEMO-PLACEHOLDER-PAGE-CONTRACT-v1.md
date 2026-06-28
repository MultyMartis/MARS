# FP-0002 V7 — Static Demo Placeholder Page Contract v1

**Status:** READY (contract only — no HTML pages created in freeze pass)  
**Next phase:** FP-0002 STATIC CLIENT DEMO SITE

## Structure

```
Header
→ optional breadcrumbs
→ <main>
    → unique H1
    → neutral message: «Раздел скоро будет опубликован»
→ Footer
→ Modal (consultation)
```

## Future phase requirements

| Requirement | Rule |
| ----------- | ---- |
| Unique `<title>` | Per page instance from Excel/URL registry |
| Unique H1 | Per page instance; plausible section name |
| Real URL | Assigned in demo site file tree |
| Working menu | Links to existing demo pages or placeholders |
| Working Footer | Standard site footer include |
| No broken links | All nav targets resolve to a page |
| No fake finished content | Placeholder message only in main |
| No engine/CMS | Static HTML only |
| Static HTML only | Gulp build output; no runtime CMS |

## Explicit non-scope (freeze pass)

- No placeholder HTML files created in this pass.
- No Excel structure intake.
- No URL registry population.
- No menu URL rewiring for demo site.

## Relationship to canonical templates

Canonical templates (FP0002-TPL-001 … FP0002-TPL-004) are **finished design references**. Placeholder pages use the same Header/Footer/Modal shell but **not** the full template body — they are a separate, minimal page type for unimplemented Excel rows.
