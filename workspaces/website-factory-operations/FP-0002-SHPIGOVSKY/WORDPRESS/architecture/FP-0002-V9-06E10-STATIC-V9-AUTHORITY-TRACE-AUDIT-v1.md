# FP-0002 V9-06E10 Static V9 Authority Trace Audit v1

**Evidence JSON:** `validation/v9-06e10-full-backup-wp-port-root-cause-audit/static-v9-authority-trace-audit.json`

## Summary

| Route | Static V9 source | WP template/partials | Authority status |
|-------|------------------|----------------------|------------------|
| `/` | `src/pages/index.html` | `front-page.php` + 19 home partials | ADAPTED_V9_WITH_ACF |
| `/uslugi/` | `src/pages/uslugi-v2.html` | `services-hub.php` + CPT-driven groups | SEMANTIC_REBUILD |
| `/uslugi/zavisimosti/` | `src/pages/usluga-podrazdel-v1.html` | `subdivision-stack.php` | ADAPTED_V9_PARTIAL |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | `src/pages/usluga-konechnaya-v1.html` | `alcohol-stack.php` | DOM_MATCH / VISUAL_DRIFT |
| `/kontakty/` | `src/pages/kontakty.html` | `contacts.php` | ADAPTED_V9 |
| `/otzyvy/` | `src/pages/otzyvy.html` | `reviews.php` | ADAPTED_V9 |
| Legal | `src/pages/*-policy*.html` + legal content partials | `legal.php` + `post_content` | CONTENT_EXACT / SHELL_ADAPTED |

## Did agents read static V9?

**Partially.** E8/E9 referenced `usluga-konechnaya-v1.html` and created section maps for alcohol leaf only. D7-D planning read static blocks but implemented **semantic PHP partials**, not direct HTML ports. No task enforced full static HTML diff before repair.

## Architecture finding

WordPress port is based on **semantic reconstruction** (ACF + helpers + CPT queries assembling "V9-compatible" markup), not **direct V9 section-stack porting**. Static V9 is cited in comments and `v9-static-content.php` but not loaded as HTML authority at render time.
