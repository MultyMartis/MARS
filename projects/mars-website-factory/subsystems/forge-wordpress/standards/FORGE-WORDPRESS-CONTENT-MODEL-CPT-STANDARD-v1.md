# Forge WordPress — Content Model and CPT Standard v1

**ID:** FW-S-10  
**Extends:** [FW-S-01 Content Modeling](FORGE-WORDPRESS-CONTENT-MODELING-STANDARD-v1.md)  
**Status:** ACTIVE — PRODUCTION PROVEN WITH CAVEATS  
**Date:** 2026-08-18  
**Evidence case:** FP-0002 specialists (Pages → CPT `specialist`, P11) and services CPT; permalink native UX (P13-FU01)

---

## 1. Content primitive matrix (when to use what)

| Primitive | Use when | Do not use when |
|-----------|----------|-----------------|
| **Page** | Unique route, hub, legal, contacts, static shell | Repeated entities with own Admin list, order, search group |
| **Child Page** | True document hierarchy (breadcrumbs) **and** same primitive is enough | Staff/products that need CPT Admin UX |
| **Post** | Dated articles / news with native blog UX | Services, people, structured catalogs |
| **CPT** | Independent lifecycle, own permalinks, list table, template, sitemap/search type | One-off landing; purely presentational repeats |
| **ACF Option** | Site-wide globals (phones, social, SEO integrations) | Per-entity body copy |
| **ACF repeater on options** | Bounded sets without public singles (e.g. some review walls) | Public URLs per item — then CPT |
| **ACF repeater on page/CPT** | Ordered blocks owned by that entity | Site-wide contacts |
| **Structured content block** | Repeatable FE section with fields | Entire entity identity |
| **Reusable block** | Hybrid/Gutenberg zones only | PIXEL_PERFECT frozen chrome |
| **Frontend-only config** | Design tokens, motion that editors must not touch | Phone numbers, URLs, SEO |

**Reviews lesson (J):** FP-0002 stored reviews as options repeater + stable `review_uid`, not a CPT. Reuse only if items have **no** public single and editors accept options UX. If reviews need permalinks, authors, or sitemap entries → CPT.

---

## 2. WHEN TO CREATE A CPT (decision matrix)

Score **Yes** = 1. Create a CPT if **≥ 4** or if any **hard Yes** in the first three.

| # | Question | Hard? |
|---|----------|-------|
| 1 | Independent add/remove without editing a parent page? | Hard |
| 2 | Each item needs its own public permalink? | Hard |
| 3 | Dedicated Admin list (photo, role, order, filters) is required? | Hard |
| 4 | Separate template from generic pages? | |
| 5 | Own sitemap provider / search group? | |
| 6 | Hide page-only fields (parent, generic body, page template)? | |
| 7 | Reuse the entity on multiple hubs? | |
| 8 | menu_order / thumbnail are first-class? | |

**If majority No:** page + repeater, or options. Document in CONTENT-MODEL.  
**Anti-pattern AP-001:** generic Page for staff-like entities “because the URL is under a hub”.

---

## 3. Hub page + CPT singles

Canonical pattern (proven P11):

```text
Hub URL /section/     → Page (editable intro, SEO, layout)
Item URL /section/x/  → CPT rewrite slug = same first segment
has_archive           → false (hub page owns the archive URL)
```

**Migration:** change `post_type` in place; keep IDs; set `post_parent=0`; preserve `post_name`; move ACF location to the CPT; **delete leftover `_wp_page_template`** so template hierarchy can win; flush rewrite once; retarget Smart Search + sitemap to the CPT; keep the **user-visible** search group label stable.

---

## 4. CPT registration checklist

Complete before first production deploy of the type.

| Area | Requirement |
|------|-------------|
| `public` | Explicit; public singles vs Admin-only |
| `has_archive` | Usually **false** when a Page hub exists |
| `rewrite` | Exact slug; `with_front` decided; no clash with Page path |
| Native permalink UI | **Only** core `#edit-slug-box`; no second editor (AP-002) |
| `post_type_link` | Honor `$leavename` so sample permalink **Изменить** works |
| Supports | Typically `title`, `thumbnail`, `page-attributes` (menu_order); omit `editor` if ACF owns body |
| Capabilities | Map to project roles |
| Labels | Locale of the site (ru_RU Admin if Russian editors) |
| List columns | Meaningful (image, title, role, order) — not default Date-only |
| ACF location | `post_type == {cpt}` |
| Sitemap | Include or exclude explicitly |
| Smart Search | Query CPT; no duplicate Page hits for migrated IDs |
| SEO meta | Same entity-meta group as pages/posts if public |
| Template | `single-{cpt}.php` (+ force filter if leftover page template meta) |
| Assets | Enqueue only on relevant templates |
| i18n | All labels via gettext |
| Migration | ID/URL preservation plan; rewrite flush flag |

**Uniqueness:** if drafts must uniquify like published, implement data-layer `wp_unique_post_slug` (core skips drafts). FP-0002 used `-copy-NN`. Treat suffix format as **J** (project convention).

---

## 5. Native permalink rule (canonical)

```text
WordPress native permalink row is the only slug UX for public pages/posts/CPTs.
Custom slug metaboxes and cloned sample-permalink rows are forbidden.
```

P12 added custom UI → duplicate native row → `fp02_post_name` won over `post_name` → P13-FU01 removed custom UI. Data-layer collision handling may remain **without** a visible second field.

---

## 6. FP-0002 specialists (architectural lesson, anonymized)

| Stage | Model |
|-------|--------|
| Initial | Child Pages of specialists hub |
| Pain | Generic Content, parent, page template, poor columns |
| Final | CPT; hub Page retained; URLs unchanged; search group name unchanged |

Do **not** copy clinical fields. Copy the **decision and migration method**.

---

*FW-S-10 v1 — 2026-08-18.*
