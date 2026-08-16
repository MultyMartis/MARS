# Regression matrix — PROD-P13-FU01

| Check | Result | Evidence |
|-------|--------|----------|
| `/` HTTP 200 | PASS | `REGRESSION-SMOKE.json` |
| `/uslugi/` 200 | PASS | same |
| `/uslugi/zavisimosti/` 200 + child `lechenie-alkogolnoy-zavisimosti` | PASS | smoke + FE marker |
| `/specyalisty/` 200 + specialist chrome | PASS | smoke + hub fetch |
| `/specyalisty/kostyuk/` 200 | PASS | smoke |
| `/wp-sitemap.xml` 200 | PASS | smoke |
| Smart Search (`fp02-search` + `smart-search` on home) | PASS | FE marker |
| SEO metabox on Service editor | PASS | `admin-after-service_zavisimosti.html` `acf-group_fp02_seo_entity_meta` |
| Admin duplicate permalink UI | PASS (1 row) | `ADMIN-UX-AFTER.json` |
| Page editor still 1 native row | PASS | same |
| Existing service/specialist `post_name` accidental changes | **0** | `QA-RUNTIME.json` `url_safety` |
| Unrelated P13 features (DOCX, social, iOS) | not touched | deploy = 2 plugin files only |

`blog_public=0` unchanged (noindex environment). WPilot not written.
