# TYPOGRAPHY OWNER INVENTORY — PROD-P16

**Date:** 2026-08-17  
**Host:** http://shpigovsky.beget.tech/  
**Authority:** Beget DB = content; local source = code (after fresh drift check)

## Canonical owner (ONE)

| Role | Path |
|------|------|
| Processor | `WORDPRESS/plugins/shpigovsky-core/src/Typography/RussianTypography.php` |
| Render-time hooks | `WORDPRESS/plugins/shpigovsky-core/src/Typography/TypographyFilters.php` |
| Module id | `typography.russian` |

P08 had **no** runtime engine — only source string rewrites + specialist migration scripts. P16 **extends** that rule set into one PHP owner; **no second engine**.

## Classification map

| Owner | Surfaces | Classification | Strategy |
|-------|----------|----------------|----------|
| A. `post_title` | All public CPT/pages | RENDER-TIME ONLY | `the_title` frontend filter |
| B. `post_content` | Pages, posts, services, specialists | RENDER-TIME ONLY | `the_content` @20 (after TOC IDs @5) |
| C. `post_excerpt` | Cards / search snippets | RENDER-TIME ONLY | `the_excerpt` |
| D. ACF text | Leads, roles, CTA labels, short fields | RENDER-TIME ONLY | `acf/format_value` type=text |
| E. ACF textarea | Longer plain / light HTML | RENDER-TIME ONLY | `acf/format_value` type=textarea |
| F. ACF WYSIWYG | Generic body, service editorials, specialist WYSIWYG | RENDER-TIME ONLY | `acf/format_value` type=wysiwyg → HTML text nodes |
| G. ACF repeater/subfields | Nested text/textarea/wysiwyg | RENDER-TIME ONLY | Same ACF format filter on leaf fields |
| H. Options / site settings | Reusable blocks, chrome | RENDER-TIME ONLY | ACF option `get_field` → format_value |
| I. Service structured fields | Section/general parity text | RENDER-TIME ONLY | ACF |
| J. Specialist fields | Role, experience, specialty, … | RENDER-TIME ONLY | ACF (P08 already stored-normalized; filter idempotent) |
| K. Article content | `post` body + ACF article fields | RENDER-TIME ONLY | `the_content` + ACF |
| L. Page content | Generic lead/body | RENDER-TIME ONLY | ACF |
| M. CTA labels | Theme + ACF | SOURCE already / RENDER-TIME | Hardcoded P08; ACF via filter |
| N. Hardcoded source strings | Theme PHP maps / partials | AUTO TYPOGRAPHY SAFE (source) | P08 completed main maps; residual chrome may still use `&nbsp;` entities in HTML partials (valid) |
| O. Footer/header/social labels | Options + chrome helpers | RENDER-TIME / SOURCE | ACF + P08 helpers |
| P. SEO title / meta description | `fp02_seo_*` | RENDER-TIME ONLY (Unicode) | ACF format + `document_title_parts`; meta via `esc_attr` of typographed plain |

## Explicit EXCLUDE

| Item | Reason |
|------|--------|
| `post_name` / slugs | Anchors, URLs, sitemap |
| Heading `id` attributes | TOC / deep links (assigned before typography) |
| URL / phone / email / embed fields | Technical |
| `<script>`, `<style>`, `<code>`, `<pre>`, `<textarea>`, SVG | Exclusion zones |
| Shortcode payloads | Syntax |
| Revisions / trash / autosaves / Activity Log | Out of live scope |
| REST matching corpus | Search normalizes NBSP→space; stored DB stays editor-friendly |

## Why not STORED mass rewrite

1. Admin WYSIWYG must stay readable (no `&nbsp;` flood).  
2. Smart Search matches stored/plain spaces; render-time NBSP would break match unless collapsed (search helper now collapses).  
3. Future Olya content benefits automatically via the same filter.  
4. Idempotent presentational-only transforms without DB ownership ambiguity.

**Persisted DB mutations for P16:** none required for live WYSIWYG/ACF (strategy RENDER-TIME).

## Required token

`TYPOGRAPHY OWNER INVENTORY COMPLETE`
