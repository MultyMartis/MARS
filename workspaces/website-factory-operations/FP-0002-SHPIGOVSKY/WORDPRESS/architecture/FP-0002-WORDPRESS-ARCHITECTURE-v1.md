# FP-0002 WordPress Architecture v1

**Project:** FP-0002 — Шпиговский  
**Task:** V9-06A  
**Date:** 2026-07-03  
**Status:** ARCHITECTURE APPROVED (V9-06A.1)  
**Authority:** Operator architecture-first mandate; supersedes V9-04 mechanical all-Pages object model for planning

---

## 1. Purpose

Design a deliberate WordPress product for FP-0002 that decomposes the approved V9 static frontend into a reusable theme + project-plugin system. This document is **design authority only** — no runtime registration, no theme implementation, no WordPress object creation.

**Visual authority:** `workspaces/fp-0002-shpigovsky-v9/dist/`  
**Structural authority:** this architecture pack + V9 route manifest (31 routes)

---

## 2. Responsibility split

| Layer | Owns | Must not own |
|-------|------|--------------|
| **Theme `shpigovsky`** | Template hierarchy, header/footer, template parts, assets, presentation, V9 markup integration | CPT registration, business forms backend, WPilot, migrations |
| **Plugin `shpigovsky-core`** | `service` CPT, fields wiring, migrations, capabilities, form handler, bounded meta | Visual markup, CSS, header/footer HTML, WPilot features |
| **WPilot** | Inspection, bounded mutations, backup/rollback | Project business logic |
| **`mars-local-runtime` MU** | Local guards, email suppression | Project content |

---

## 3. V9 system decomposition

### 3.1 Global shell (theme-owned, single instance)

| Component | V9 source | Ownership |
|-----------|-----------|-----------|
| Document head | `partials/layout/head.html` | THEME_CODE + DERIVED meta |
| Body start | `partials/layout/body-start.html` | THEME_CODE |
| Header | `partials/layout/header.html` | THEME_CODE structure; menus WORDPRESS_OPTION/MENU |
| Footer | `partials/layout/footer.html` | THEME_CODE structure; links MENU |
| Global modal | `partials/layout/global-consultation-modal.html` | THEME_CODE + OPTIONS labels |
| Scroll-to-top | `partials/components/scroll-to-top.html` | THEME_CODE |
| Breadcrumbs | per-template | DERIVED from hierarchy |

**Excluded:** preloader (none active), G6 infrastructure blocks (forbidden), genotyping home section (unpublished route).

### 3.2 Content families

| Family | V9 routes | WordPress entity |
|--------|-----------|------------------|
| Home | `/` | Page (`page_on_front`) |
| Services hub | `/uslugi/` | **Native Page** (not Service, not CPT archive) |
| Service subdivision | 3 subdivisions | `service` CPT (parent=0) |
| Service leaf | 12 leaves | `service` CPT (child) |
| Institutional | `/o-centre/` + 5 children | Pages (hierarchical) |
| Reviews | `/otzyvy/` | Page |
| Blog archive | `/blog/` | Posts page + `home.php` |
| Blog article | `/blog/{slug}/` | Post |
| Contacts | `/kontakty/` | Page |
| Legal | 4 routes | Pages + legal template |

### 3.3 Reusable section families (from V9 audit)

Sections map to `template-parts/sections/` with bounded field binding — not ad hoc HTML in `functions.php`.

Key families: hero, intro, advantages, indications/signs, symptoms, stages, programme/process, specialists, testimonials/reviews teaser, FAQ, related services, contacts/CTA, trust/credentials, article cards, legal content, placeholder notice, infrastructure narrative (G0–G5 only).

---

## 4. Entity model summary

See [FP-0002-WORDPRESS-ENTITY-REGISTRY-v1.json](FP-0002-WORDPRESS-ENTITY-REGISTRY-v1.json).

**Core decision:** introduce hierarchical **`service`** CPT for all `/uslugi/*` content except the hub Page at `/uslugi/`. Rejects V9-04's "all services as nested Pages" planning model.

| Entity | Decision |
|--------|----------|
| Native Pages | **APPROVED** — hubs, institutional, contacts, reviews, legal |
| `service` CPT | **APPROVED** — hierarchical catalogue |
| `service_category` taxonomy | **REJECTED** |
| Native Posts | **APPROVED** — blog only |
| Review CPT | **REJECTED** |
| Specialist CPT | **REJECTED** |

---

## 5. URL and rewrite architecture

| Surface | URL | Mechanism | Class |
|---------|-----|-----------|-------|
| Home | `/` | `page_on_front` (slug `glavnaya`) | NATIVE |
| Services hub | `/uslugi/` | Page slug `uslugi` | PAGE_ROUTE |
| Service detail | `/uslugi/{path}/` | Hierarchical `service` CPT, `has_archive=false`, `CPT_REWRITE_PLUS_POST_TYPE_LINK_FILTER` | CPT_REWRITE |
| Institutional | `/o-centre/...` | Hierarchical Pages | PAGE_ROUTE |
| Reviews | `/otzyvy/` | Page | PAGE_ROUTE |
| Blog archive | `/blog/` | `page_for_posts` + `home.php` | NATIVE |
| Blog article | `/blog/{slug}/` | Post permalink | NATIVE |
| Legal | top-level slugs | Pages | PAGE_ROUTE |

**Conflict resolution:** Page `/uslugi/` takes precedence over CPT root; CPT does not register public archive (`has_archive=false`). Permalink contract: [FP-0002-SERVICE-PERMALINK-REWRITE-CONTRACT-v1.md](FP-0002-SERVICE-PERMALINK-REWRITE-CONTRACT-v1.md).

**Retire / redirect (post-migration):**

| Route | Action |
|-------|--------|
| `/uslugi/genotipirovanie/` | EXCLUDED — RETIRE (forbidden) |
| `/specyalisty/` | **301 → `/uslugi/zavisimosti/specialistam/`** after canonical target ready (OD-002) |
| `/o-centre/intervyu-i-smi/` | RETIRE_AFTER_MIGRATION |
| `/pravovaya-informaciya-pilzovatelyu/` | RETIRE_AFTER_MIGRATION |

**Custom rewrite:** optional `CUSTOM_REWRITE` rule only if hierarchical CPT + hub Page conflict requires explicit priority — validate in V9-06C.

---

## 6. Template variant strategy

| Variant | Selector | Templates |
|---------|----------|-----------|
| `home` | `front-page.php` | Home sections |
| `services-hub` | Page template | Hub only |
| `service-subdivision` | `single-service.php` + meta `layout=subdivision` | Subdivision |
| `service-leaf-standard` | `single-service.php` + meta `layout=leaf` | Placeholder leaves |
| `service-leaf-alcohol` | meta `layout=alcohol-special` | Alcohol full page |
| `institutional-full` | Page template + parent context | O-centre hub |
| `institutional-placeholder` | placeholder meta | O-centre children |
| `reviews` | Page template | Otzyvy |
| `contacts` | Page template | Kontakty |
| `legal` | Page template | 4 legal pages |
| `blog-archive` | `home.php` | Blog |
| `blog-article` | `single.php` | Posts |

**No slug-based conditionals** as primary selector — use post type, page template, and bounded service layout meta.

---

## 7. Navigation model

**Decision:** `HYBRID_BOUNDED`

| Area | Mechanism |
|------|-----------|
| Primary header | Manual menu (`primary`) — operator-controlled order and labels |
| Mobile | Same `primary` menu rendered in offcanvas OR dedicated `mobile` location if needed |
| Footer service column | Manual `footer_services` + optional query supplement for missing published services |
| Footer o-centre | Manual `footer_o_centre` |
| Legal | Manual `legal` |
| Service dropdown | Manual children under «Услуги» pointing to subdivision services |
| Home accordion | Query-driven published `service` children grouped by subdivision |

Menu locations to register in V9-06B: `primary`, `footer_services`, `footer_o_centre`, `legal` (extend foundation `footer` split or map in theme).

---

## 8. Forms architecture

| Concern | Owner |
|---------|-------|
| Modal markup | Theme |
| Client validation / mask | Theme assets |
| Server handler | `shpigovsky-core` Forms module |
| Nonce / spam | Plugin |
| Local email | Suppressed by `mars-local-runtime` |
| Storage | Defer — email or custom table in later phase |
| WPilot | Not involved in submission |

---

## 9. SEO boundary

| Concern | Owner |
|---------|-------|
| `<title>` | Theme + native; SEO plugin later optional |
| Meta description | Per-entity bounded field or SEO plugin |
| Canonical | Derived |
| OG tags | Theme fallbacks; plugin optional |
| Breadcrumbs | Theme derived |
| Schema | Minimal MedicalOrganization in theme options — defer detail |

No duplicate SEO field stacks before plugin decision.

---

## 10. WordPress object skeleton plan (minimum, not created in V9-06A)

| Object | Count | Notes |
|--------|------:|-------|
| Pages | 17 | Includes front, hub, institutional×6, reviews, contacts, legal×4, blog posts page |
| Services | 15 | Full hierarchy under CPT |
| Posts | 1+ | Fixture `nazvanie-stati` |
| Categories | **0** | OD-003: none at launch |
| Menus | 4 | primary, footer_services, footer_o_centre, legal |
| Options | 2 ACF option pages | site + modal |

**Must not exist after migration:** genotipirovanie page, specyalisty, intervyu-i-smi, pravovaya hub.

---

## 11. Implementation sequence (proposed)

| Phase | Purpose | Mutations |
|-------|---------|-----------|
| V9-06A | Architecture | 0 |
| V9-06A.1 | Architecture reconciliation | 0 |
| V9-06B | Theme + core skeleton files | Filesystem source only |
| V9-06C | CPT, ACF Pro fields, admin UX | Code + ACF JSON — **requires ACF Pro prerequisite** |
| V9-06D | Minimum WP objects + migration | WP objects |
| V9-07A | Global shell integration | Theme |
| V9-07B | Service templates | Theme |
| V9-07C | Pages + Home | Theme |
| V9-07D | Blog + legal | Theme |
| V9-08 | Content migration + parity | Content |

**FW-07C-2D:** SUPERSEDED BY ARCHITECTURE-FIRST SEQUENCE — object reconciliation moves to V9-06D with charter refresh.

---

## 12. Validation summary

See [FP-0002-V9-06A-VALIDATION-REPORT-v1.md](FP-0002-V9-06A-VALIDATION-REPORT-v1.md) and [FP-0002-V9-06A1-ARCHITECTURE-RECONCILIATION-REPORT-v1.md](FP-0002-V9-06A1-ARCHITECTURE-RECONCILIATION-REPORT-v1.md).

**Result:** PASS (39/39 checks; machine validation 0 failures)

---

## 13. Related artefacts

| File | Purpose |
|------|---------|
| FP-0002-WORDPRESS-ENTITY-REGISTRY-v1.json | Entity decisions |
| FP-0002-V9-ROUTE-ENTITY-TEMPLATE-MAP-v1.json | 31-route map |
| FP-0002-WORDPRESS-TEMPLATE-HIERARCHY-v1.md | PHP template map |
| FP-0002-TEMPLATE-PART-REGISTRY-v1.json | Partial inventory |
| FP-0002-FIELD-OWNERSHIP-MATRIX-v1.json | Field classes |
| FP-0002-WORDPRESS-ADMIN-UX-MODEL-v1.md | Editor workflows |
| FP-0002-SERVICE-ENTITY-REGISTRY-v1.json | 15 Service entities |
| FP-0002-SERVICE-PERMALINK-REWRITE-CONTRACT-v1.md | Permalink contract |
| FP-0002-SERVICE-PERMALINK-TEST-MATRIX-v1.json | Permalink test matrix |
| FP-0002-PAGE-TO-SERVICE-MIGRATION-CONTRACT-v1.md | Page→Service migration |
| FP-0002-ROUTE-CONFLICT-REGISTER-RECONCILED-v1.md | Legacy route decisions |
| FP-0002-V9-06A1-ARCHITECTURE-RECONCILIATION-REPORT-v1.md | V9-06A.1 report |
| FP-0002-V9-06A1-ARCHITECTURE-VALIDATION.mjs | Machine validation |
| FP-0002-ACF-STRATEGY-v1.md | ACF Pro required (OD-001) |
| FP-0002-DATA-OWNERSHIP-MAP-v1.json | Data owners |
| FP-0002-WORDPRESS-FOUNDATION-TO-V9-MIGRATION-PLAN-v1.md | Migration |
| FP-0002-WORDPRESS-ARCHITECTURE-DECISIONS-v1.md | ADR log |

---

*Design authority only. Runtime mutations: 0.*
