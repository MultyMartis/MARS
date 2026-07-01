# FP-0002 V8 — WordPress-Ready Baseline v1

**Document type:** Architecture facts record (not full Forge specification)  
**Date:** 2026-07-01  
**Baseline:** FP-0002-V8-OPERATOR-APPROVED-FRONTEND-BASELINE-01

---

## Source of truth

The operator-approved HTML/CSS frontend in `workspaces/fp-0002-shpigovsky-v8/` is the baseline. Forge WordPress must adapt WordPress to this frontend — not redesign the approved output.

---

## Blog Article template mapping

| Frontend block | WordPress ownership |
|----------------|---------------------|
| Hero card (`.blog-article-hero__layout`) | Template-managed shell |
| H1, date, reading time, author | Post fields / computed reading time |
| Featured image | Post thumbnail |
| TOC (`.blog-article-hero__toc`) | Auto-generated from H2 in `the_content()` on save/render |
| Excerpt (`.blog-article-hero__excerpt`) | Post excerpt / dedicated field — **not** `the_content()` |
| Article body (`.blog-article-body__content`) | Single `the_content()` stream — editor-compatible |
| Inline images | Normal editor content inside `the_content()` |
| Conclusion heading | Template section |
| Founder quote | Template-managed from article conclusion + author profile |
| Sources | Template-managed / custom field — outside `the_content()` |
| Related posts | Query-driven; exclude current post |
| CTA band | Template-managed (`program-cta-band`) |
| Footer | Theme template |

---

## Constraints

- No mobile-specific editor markup; responsive behavior is CSS-only on shared DOM
- Shared components (header, footer, CTA, founder quote, cards) must preserve approved frontend output
- TOC must not require manual editor maintenance

---

## Deferred

Full Forge WordPress specification, field schema, and activation — Phase 07B+ and dedicated WordPress tasks.
