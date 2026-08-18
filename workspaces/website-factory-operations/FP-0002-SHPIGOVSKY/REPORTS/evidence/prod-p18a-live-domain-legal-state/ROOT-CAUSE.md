# LEGAL DEMO BANNER — ROOT CAUSE (P18A)

**Required token:** LEGAL DEMO BANNER ROOT CAUSE PROVEN

## Owner

**One owner:** `WORDPRESS/theme/shpigovsky/template-parts/legal/document-page.php`  
Included by `page-templates/legal.php` for pages 3, 22, 23, 24.

No second banner in plugin filters / ACF conditionals / content filters.

## Cause class: **H** (exact)

The template **always** printed the DEMO notice. It did **not** read `legal_demo_marker`.

Not A–G as primary:

- A/B: no `?:` / `empty()` on this field in the template (field unused)
- C: no legacy meta fallback in the template
- D: `legal_status=production_ready` did not drive the banner (banner was unconditional)
- E: saved post meta is `0`; autosaves exist but published meta is OFF
- F: `[ДЕМО]` body placeholders exist only on #24; banner was on all four pages
- G: single owner

## Saved Admin state (MySQL)

All four legal pages: `legal_status=production_ready`, `legal_demo_marker=0`, `legal_production_blocker=0`. Keys **exist** (explicit false, not unset).

Autosave IDs: 2071 (#3), 2077 (#23), 2073 (#24) — slightly after last revision; screenshot matches **saved canonical** flags (`0`).

## Fix

`inc/legal-helpers.php` three-state boolean; template renders notice **only if** `shpigovsky_legal_demo_marker_enabled()`. Defaults apply only when the meta key is missing.
