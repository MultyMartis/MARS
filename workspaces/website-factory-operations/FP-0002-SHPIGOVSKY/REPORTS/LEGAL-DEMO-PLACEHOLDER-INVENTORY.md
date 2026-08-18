# LEGAL-DEMO-PLACEHOLDER-INVENTORY — FP-0002 P18A

**Date:** 2026-08-18  
**Scope:** published pages using `page-templates/legal.php`  
**Mutation:** none (inventory only; legal wording not rewritten)

Canonical legal pages: **3, 22, 23, 24**. Template owner: `page-templates/legal.php` → `template-parts/legal/document-page.php`. Content owner: native `post_content`.

| Page ID | Title | Field / content owner | Placeholder type | Visibility | Action |
|---------|-------|------------------------|------------------|------------|--------|
| 3 | Политика конфиденциальности | `post_content` | none (`[ДЕМО` = 0, Lorem = 0) | publish | ALREADY RESOLVED |
| 22 | Пользовательское соглашение | `post_content` | none | publish | ALREADY RESOLVED |
| 23 | Согласие на обработку персональных данных | `post_content` | none | publish | ALREADY RESOLVED |
| 24 | Политика Cookie-файлов | `post_content` | `[ДЕМО: перечень подключённых систем аналитики]` | publish frontend | OPERATOR CONTENT REQUIRED |

No ACF postmeta values contained `[ДЕМО`. No Lorem/test placeholders on these four published pages.

**Do not invent** legal entity names or analytics vendor lists. Cookie placeholder replacement is an operator/Olya content task.

Banner vs placeholder: DEMO **banner** is owned by `legal_demo_marker` (now OFF on all four). Remaining `[ДЕМО: …]` in cookie copy is **body content**, not the banner.

Evidence: `REPORTS/evidence/prod-p18a-live-domain-legal-state/LEGAL-PLACEHOLDER-EXTRACT.json`
