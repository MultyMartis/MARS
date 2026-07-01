# FP-0002 V8 — Forge WordPress Handoff Map v1

**Date:** 2026-07-01  
**Expands:** [FP-0002-V8-WORDPRESS-READY-BASELINE-v1.md](FP-0002-V8-WORDPRESS-READY-BASELINE-v1.md) — does not replace it  
**Baseline frontend:** `workspaces/fp-0002-shpigovsky-v8/` @ `eb47ebb`

---

## Core rule

**Forge WordPress must reproduce the approved frontend output and adapt WordPress to it.** It must **not** redesign the approved frontend.

Generic contract: [WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md](../../../projects/mars-website-factory/subsystems/forge-wordpress/contracts/WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md)

**Status:** Handoff map only — **no** Forge implementation in Phase 07B.

---

## Global theme elements

| Element | WP template | Editable | Notes |
|---------|-------------|----------|-------|
| Header + nav | `header.php` | Menu (WP menu); logo media | Offcanvas mobile |
| Footer | `footer.php` | Widgets / ACF options | |
| Modal consultation | Footer hook + JS | Options: phone, copy | Visual form — policy in FP-0002 WP docs |
| Breadcrumbs | Partial | Yoast/RankMath or custom | Param logic from crumbs |
| CTA band | Partial | ACF block or options | `program-cta-band` |
| SEO meta | `head` partial | SEO plugin + post fields | |

---

## Page family mapping

### Home (`index.html`)

| Aspect | Mapping |
|--------|---------|
| Template | `front-page.php` |
| Post type | Static front page |
| Editor-managed | Limited — mostly page builder blocks or ACF flexible content mirroring sections |
| Template-managed | Section order shell matching approved DOM |
| Query-driven | `home-articles` — recent posts query |
| Menu | Primary nav — WP menu |
| Assets | Theme + media library |

### O-Centre, Contacts

| Aspect | Mapping |
|--------|---------|
| Template | `page-o-centre.php`, `page-contacts.php` or slug templates |
| Post type | Page |
| Fields | ACF for map embed, addresses, hours |
| Forms | Visual only until form plugin wired |

### Reviews archive

| Aspect | Mapping |
|--------|---------|
| Template | `page-reviews.php` or CPT archive |
| Query | Review posts / custom CPT |
| Cards | Loop → `review-archive-card` markup |

### Blog archive

| Aspect | Mapping |
|--------|---------|
| Template | `home.php` or `archive.php` for posts |
| Query | Main query paginated |
| Cards | `blog-archive-card` loop |
| Lower stack | Template partial (expert quote static or options) |

### Blog article (detail)

| Block | WP source |
|-------|-----------|
| Title | `post_title` |
| Slug | `post_name` |
| Date | `post_date` |
| Author | Author display name / coauthor plugin |
| Reading time | Computed meta |
| Featured image | `post_thumbnail` |
| TOC | Generated from H2 in `the_content()` |
| Excerpt | `post_excerpt` or dedicated field |
| Body | `the_content()` — single stream |
| Inline images | Editor content |
| Conclusion + founder quote | Template partial + author profile |
| Sources | ACF repeater or custom field |
| Related posts | `WP_Query` exclude current |
| CTA | Template partial |

### Services hub (v2)

| Aspect | Mapping |
|--------|---------|
| Template | `page-services.php` |
| Structure | Category sections — ACF repeater or child pages |
| Subnav | Generated from on-page anchors or child menu |

### Service subdivision / leaf

| Aspect | Mapping |
|--------|---------|
| Template | `page-service-section.php`, `page-service-leaf.php` |
| Hero | ACF: eyebrow, title, lead, image |
| Body sections | Mix of editor + ACF blocks per section |
| Program block | Repeater items → `services-program-v2-item` |

---

## Content ownership matrix

| Content type | Editor | Template | Query |
|--------------|--------|----------|-------|
| Article body H2/H3/p/img | ✓ | | |
| Article excerpt | ✓ (field) | | |
| Article TOC | | ✓ auto | |
| Related posts | | ✓ | ✓ |
| Sources | ✓ (repeater) | ✓ shell | |
| Nav menu | | | ✓ menu API |
| Home article teasers | | | ✓ |
| Footer legal links | ✓ options | ✓ | |

---

## URL / permalink expectations

| Page | Expected permalink |
|------|-------------------|
| Home | `/` |
| Blog archive | `/blog/` |
| Blog post | `/blog/{slug}/` |
| Services hub | `/uslugi/` |
| Service paths | `/uslugi/{section}/{leaf}/` per Excel IA |
| Contacts | `/kontakty/` |
| Reviews | `/otzyvy/` |
| O-Centre | `/o-centre/` |

Static V8 filenames (`uslugi-v2.html`) are build artifacts — not production URLs.

---

## Assets

| Type | Static demo | WordPress |
|------|-------------|-----------|
| Theme CSS/JS | `dist/assets/` | Enqueued theme assets |
| Content images | `dist/assets/img/` | Media library attachments |
| SVG icons | Theme | Theme directory or inline |

---

## Forms

| Form | Owner | Phase |
|------|-------|-------|
| Modal consultation | Form plugin + theme JS | Post-intake |
| final-form | Same | Post-intake |
| Policy | [FP-0002-LOCAL-MAIL-AND-FORM-POLICY-v1.md](../../../projects/mars-website-factory/subsystems/forge-wordpress/projects/fp-0002/FP-0002-LOCAL-MAIL-AND-FORM-POLICY-v1.md) | |

---

## SEO

| Owner | Scope |
|-------|-------|
| SEO plugin | Meta, schema, sitemap |
| Theme | Semantic HTML, one H1 |
| Editor | Article content |

---

## FW-06B intake alignment

Forge subsystem status: **FW-06B — Approved Frontend Intake — WAITING**

This map is input for FW-06B when operator authorizes WordPress integration. Local foundation (`shpigovsky.test`) exists; **frontend integration not started**.

---

## Test strategy (future)

1. Render WP templates to HTML  
2. Compare against static baseline (VL visual layers)  
3. Verify content ownership boundaries (excerpt, TOC, related outside body)  

---

*Forge WordPress handoff map — FP-0002 V8.*
