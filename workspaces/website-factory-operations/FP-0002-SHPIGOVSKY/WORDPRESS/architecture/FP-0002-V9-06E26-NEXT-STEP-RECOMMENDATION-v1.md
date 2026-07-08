# FP-0002 V9-06E26 Next Step Recommendation v1

**Date:** 2026-07-09  
**Task:** V9-06E26 Blog And Other Pages Porting Architecture Audit  
**Baseline:** `7a6674db8046525d84abd69eb1b21b703b16094b`

## Recommended next action

**CREATE_V9_06E26A_ABOUT_PAGE_WORDPRESS_ACF_PORT_TASK**

## Rationale

1. `/o-centre/` is the largest remaining non-service page with **14 V9 sections**; current WP template renders hero + breadcrumbs only.
2. Institutional ACF group (`group_fp02_page_institutional`) already exists with local hero fields (E24) — extend and wire before blog waves.
3. Blog archive/single depend on shared reusable blocks (founder quote, program CTA, specialists, reviews) already used on institutional pages.
4. Blog route `/blog/` is assigned (`page_for_posts=19`) but templates are skeleton-only; permalink structure must be corrected to `/blog/%postname%/` during E26B — not blocking E26A.

## Wave order after E26A

| Order | Wave | Task charter |
|-------|------|--------------|
| 1 | E26A | `О центре` hub + child institutional pages — full V9 section stack |
| 2 | E26B | Blog archive `/blog/` — V9 layout, filters, pagination |
| 3 | E26C | Blog single — hero, TOC, body, lower stack, schema |
| 4 | E26D | Seed fixture post `nazvanie-stati` + visual QA |

## Explicitly deferred

- E27 obsolete pages cleanup (IDs 10, 17, 21, 25)
- MetaCODE WPilot / Word document automation
- `blog_public` indexing enablement (operator decision at launch)
- Legal text replacement

## Evidence

`validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/final-verdict.json`
