# FP-0002 V9 Forge WordPress Intake Pack v1

**Project:** FP-0002 Shpigovsky.ru  
**Phase:** V9-04 — Forge WordPress Intake Pack  
**Date:** 2026-07-02  
**Status:** `FP0002_V9_FORGE_WORDPRESS_INTAKE_PACK_COMPLETE` (upon checkpoint)

## Identity

| Field | Value |
|-------|-------|
| Stable commit | `a51376872fbfefb7d5f68a58b440c726d6cf3de3` |
| Stable tag | `fp-0002-v9-operator-approved-static-frontend-stable-01` |
| Source authority | `workspaces/fp-0002-shpigovsky-v9/src/` |
| Rendered authority | `workspaces/fp-0002-shpigovsky-v9/dist/` |
| Routes | 31 published |
| Form mode | STATIC_DEMO_NO_BACKEND |

## Purpose

Complete formal contract for Forge / AG-WP-001 to implement WordPress theme and content model **without re-auditing project history**.

**This pack does not authorize WordPress installation or theme creation by itself.**

## Package contents

### Authority & audits
- [Authority hierarchy](./authority/FP-0002-V9-04-FORGE-AUTHORITY-HIERARCHY-v1.md)
- [Existing docs audit](./validation/FP-0002-V9-04-EXISTING-WORDPRESS-DOCS-AUDIT-v1.md)
- [Forge capability audit](./validation/FP-0002-V9-04-FORGE-CAPABILITY-AUDIT-v1.md)

### Routes & objects
- [Canonical route inventory](./routes/FP-0002-V9-04-CANONICAL-ROUTE-INVENTORY-v1.md)
- [WordPress object model](./routes/FP-0002-V9-04-WORDPRESS-OBJECT-MODEL-v1.md)
- [Permalink contract](./seo/FP-0002-V9-04-PERMALINK-AND-REDIRECT-CONTRACT-v1.md)

### Templates & components
- [Page-to-template map](./templates/FP-0002-V9-04-PAGE-TO-TEMPLATE-MAP-v1.md)
- [Theme target map](./templates/FP-0002-V9-04-FORGE-THEME-TARGET-MAP-v1.md)
- [Component map](./components/FP-0002-V9-04-COMPONENT-TO-TEMPLATE-PART-MAP-v1.md)

### Content & fields
- [Content ownership](./content/FP-0002-V9-04-CONTENT-OWNERSHIP-MODEL-v1.md)
- [Migration manifest](./content/FP-0002-V9-04-CONTENT-MIGRATION-MANIFEST-v1.md)
- [Native fields](./fields/FP-0002-V9-04-NATIVE-WORDPRESS-FIELDS-MAP-v1.md)
- [ACF architecture](./fields/FP-0002-V9-04-ACF-FIELD-ARCHITECTURE-v1.md)
- [Repeater policy](./fields/FP-0002-V9-04-REPEATER-AND-FLEXIBLE-CONTENT-POLICY-v1.md)
- [Global options](./fields/FP-0002-V9-04-GLOBAL-SITE-OPTIONS-v1.md)
- [ACF sync policy](./fields/FP-0002-V9-04-ACF-OWNERSHIP-AND-SYNC-POLICY-v1.md)

### Blog & reviews
- [Blog architecture](./blog/FP-0002-V9-04-BLOG-ARCHITECTURE-v1.md)
- [Reviews architecture](./reviews/FP-0002-V9-04-REVIEWS-ARCHITECTURE-v1.md)

### Navigation & forms
- [Menus](./menus/FP-0002-V9-04-MENUS-AND-NAVIGATION-v1.md)
- [Breadcrumbs](./menus/FP-0002-V9-04-BREADCRUMBS-CONTRACT-v1.md)
- [Forms & modal](./forms/FP-0002-V9-04-FORMS-AND-MODAL-CONTRACT-v1.md)
- [Scroll-to-top](./forms/FP-0002-V9-04-SCROLL-TO-TOP-CONTRACT-v1.md)

### Assets, legal, SEO
- [Assets migration](./assets/FP-0002-V9-04-ASSET-AND-MEDIA-MIGRATION-v1.md)
- [Legal pages](./legal/FP-0002-V9-04-LEGAL-PAGES-CONTRACT-v1.md)
- [Placeholder policy](./legal/FP-0002-V9-04-PLACEHOLDER-PAGE-POLICY-v1.md)
- [SEO boundary](./seo/FP-0002-V9-04-SEO-METADATA-BOUNDARY-v1.md)

### Implementation & validation
- [Frontend runtime](./implementation/FP-0002-V9-04-FRONTEND-RUNTIME-CONTRACT-v1.md)
- [Implementation sequence](./implementation/FP-0002-V9-04-FORGE-IMPLEMENTATION-SEQUENCE-v1.md)
- [Dependency policy](./implementation/FP-0002-V9-04-WORDPRESS-DEPENDENCY-POLICY-v1.md)
- [Acceptance matrix](./validation/FP-0002-V9-04-FORGE-ACCEPTANCE-MATRIX-v1.md)
- [Intake pack review](./validation/FP-0002-V9-04-INTAKE-PACK-REVIEW-v1.md)

### Registers
- [Production blockers](./registers/FP-0002-V9-04-PRODUCTION-BLOCKER-REGISTER-v1.md)
- [Risks](./registers/FP-0002-V9-04-FORGE-RISK-REGISTER-v1.md)
- [Open decisions](./registers/FP-0002-V9-04-OPEN-DECISIONS-v1.md)

### Machine manifests
- [Routes JSON](./manifests/FP-0002-V9-FORGE-ROUTES-v1.json)
- [Templates JSON](./manifests/FP-0002-V9-FORGE-TEMPLATES-v1.json)
- [Components JSON](./manifests/FP-0002-V9-FORGE-COMPONENTS-v1.json)
- [Fields JSON](./manifests/FP-0002-V9-FORGE-FIELDS-v1.json)
- [Acceptance JSON](./manifests/FP-0002-V9-FORGE-ACCEPTANCE-v1.json)
- [Blockers JSON](./manifests/FP-0002-V9-FORGE-BLOCKERS-v1.json)

## Summaries

| Area | Summary |
|------|---------|
| Templates | 12 families (front-page, services, institutional, blog, legal, placeholder…) |
| ACF groups | 13 documented groups |
| Blog | Native Posts + home.php |
| Reviews | Page repeater (no CPT default) |
| Modal | Triumph runtime, Shpigovsky visuals |
| Blockers | Legal DEMO, placeholders, forms, cookie |

## Next action for Forge

**V9-05 — Forge WordPress Implementation Environment Gate and Execution Plan**

1. Verify FW-06B operator charter.
2. Run `npm run validate:forge-intake`.
3. Provision local WP against existing foundation (`shpigovsky.test`).
4. Begin F0–F1 only after gate PASS — no production mutations.

## Constraints

- Do not edit V9 `src/` or `dist/` during WP implementation planning.
- Do not recreate preloader, G6, or genotyping route.
- Do not ship legal DEMO tokens to production.
