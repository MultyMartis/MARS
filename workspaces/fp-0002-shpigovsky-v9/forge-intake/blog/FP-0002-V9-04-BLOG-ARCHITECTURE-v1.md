# FP-0002 V9-04 Blog Architecture v1

**Date:** 2026-07-02

## Decision: native Posts

No article CPT. Archive via **Settings → Reading → Posts page** + `home.php`.

## Surfaces

| Surface | Template | Object |
|---------|----------|--------|
| `/blog/` | `home.php` | Posts page |
| `/blog/{slug}/` | `single.php` | `post` |

## Fixture migration

Migrate `/blog/nazvanie-stati/` as first post slug `nazvanie-stati` — reference only.

## Article structure (preserve)

1. Hero: breadcrumbs, H1, meta, featured image, **TOC (5 items from H2)**, excerpt
2. Body: single content stream with H2/H3, inline images
3. Lower: conclusion, founder quote, sources (8), related (3 cards), program CTA

## TOC

Auto-generate from H2 in content — do not hardcode fixture IDs.

## Permalink

`/blog/%postname%/` with trailing slash policy matching static.

## SEO boundary

Plugin-owned if selected; theme provides fallbacks only.
