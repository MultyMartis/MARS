# {PROJECT-ID} — Editor Workflow Acceptance Checklist v1

**Artifact ID:** EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST  
**Project:**  
**Date:**  
**Operator / editor:**  
**Standard:** [EDITOR UX](../standards/FORGE-WORDPRESS-EDITOR-UX-STANDARD-v1.md)

CMS architecture is not complete until these pass on a real (or staging) wp-admin — tabletop review of maps is allowed **before** Admin exists; launch requires live walkthrough.

---

## Global / chrome

| # | Workflow | Pass | Notes |
|---|----------|------|-------|
| 1 | Change primary phone once; header, mobile, floating header, footer, contacts update | ☐ | |
| 2 | Clear phone; no empty `tel:` / leftover number | ☐ | |
| 3 | Change social URL; chrome updates | ☐ | |
| 4 | Clear or hide social; icon disappears | ☐ | |
| 5 | Change global CTA label; pages using fallback update | ☐ | |

## Collections

| # | Workflow | Pass | Notes |
|---|----------|------|-------|
| 6 | Add a new service (or primary CPT); appears in Admin list, hub, single, search/sitemap as designed | ☐ | |
| 7 | Add a specialist / team entity; featured image + fields; card + single | ☐ | |
| 8 | Reorder collection (`menu_order` or documented order) | ☐ | |
| 9 | Unpublish related item; no broken card/link on parent | ☐ | |

## Pages / sections

| # | Workflow | Pass | Notes |
|---|----------|------|-------|
| 10 | Hide optional section (`enabled` or empty content) | ☐ | |
| 11 | Fill Hero fields; frontend matches contract | ☐ | |
| 12 | Internal CTA uses object selector; permalink follows slug change | ☐ | |
| 13 | External CTA uses URL only when type=external | ☐ | |

## Editorial

| # | Workflow | Pass | Notes |
|---|----------|------|-------|
| 14 | Add article; SEO fallback works if meta empty | ☐ | |
| 15 | Change SEO description; view-source unique | ☐ | |

## Negative tests

| # | Workflow | Pass | Notes |
|---|----------|------|-------|
| 16 | Editor cannot see raw Options dump / migration tools | ☐ | |
| 17 | Empty fields do not show Lorem/demo | ☐ | |
| 18 | Editor completes 6–7 without knowing field keys | ☐ | |

**Sign-off:** architecture done only if ☐ 18 is true.

| Role | Name | Date | Result |
|------|------|------|--------|
| Editor (or proxy) | | | PASS / FAIL |
| Admin UX | | | |

---

*AP-CMS-015 if skipped.*
