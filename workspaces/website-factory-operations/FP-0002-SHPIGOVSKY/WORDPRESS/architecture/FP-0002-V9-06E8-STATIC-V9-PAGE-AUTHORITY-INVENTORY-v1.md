# FP-0002 V9-06E8 Static V9 Page Authority Inventory v1

**Task:** V9-06E8 | **Date:** 2026-07-06

## Authority source

| Surface | Path |
|---------|------|
| Services hub | `workspaces/fp-0002-shpigovsky-v9/src/pages/uslugi-v2.html` |
| Contacts | `workspaces/fp-0002-shpigovsky-v9/src/pages/kontakty.html` |
| Alcohol service leaf | `workspaces/fp-0002-shpigovsky-v9/src/pages/usluga-konechnaya-v1.html` |
| Dependencies subdivision | `workspaces/fp-0002-shpigovsky-v9/src/pages/usluga-podrazdel-v1.html` |

## Route map (summary)

| Route | Static source | V9 content | V9 layout | WP after E8 |
|-------|---------------|------------|-----------|-------------|
| `/uslugi/` | uslugi-v2.html | YES | YES | EXACT_V9_CONTENT_AND_LAYOUT |
| `/kontakty/` | kontakty.html | YES | YES | EXACT_V9_CONTENT_AND_LAYOUT |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | usluga-konechnaya-v1.html | PARTIAL (fixture lorem in program) | YES | EXACT_V9_LAYOUT + DEMO program copy |
| `/uslugi/psihicheskoe-zdorovie/` | placeholder page | NO | NO | TEMPLATE_MATCH_DEMO_CONTENT |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | placeholder page | NO | NO | TEMPLATE_MATCH_DEMO_CONTENT |
| `/uslugi/zavisimosti/` | usluga-podrazdel-v1.html | PARTIAL | YES | E6 accepted — regression PASS |

Evidence JSON: `validation/v9-06e8-static-v9-content-main-layout-authority-repair/static-v9-page-authority-inventory.json`
