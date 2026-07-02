# FP-0002 V7 Head — WordPress Migration Boundary

**Workspace:** `workspaces/fp-0002-shpigovsky-v7/`  
**Package:** #001 Phase 2

---

## Static Gulp (current)

| Piece | Authority |
|-------|-----------|
| Markup | `src/partials/layout/head.html` |
| Per-page values | Explicit JSON parameters on each `src/pages/*.html` |
| Favicon | `src/favicon/*` → `dist/assets/favicon/*` |
| OG image | `src/img/social/og-default.jpg` |
| Robots (template) | `index, follow` — production contract only |

Static head is **replaceable** — no business logic embedded in partial beyond meta/CSS/favicon links.

---

## Future WordPress

| Concern | Target authority |
|---------|------------------|
| Title | `add_theme_support('title-tag')` + `wp_get_document_title()` |
| Meta description | SEO plugin or controlled theme layer — **one** source |
| Canonical | SEO plugin or `rel_canonical` — **one** source |
| Open Graph | SEO plugin (Yoast/RankMath/etc.) or custom controlled layer — **one** source |
| Twitter Card | Same layer as OG — **one** source |
| Favicon / app icon | WordPress **Site Icon** + theme enqueue |
| Extra CSS | Theme `inc/assets.php` — vendor + main stylesheet |

Invoke `wp_head()` in theme header; **do not** duplicate static `<title>` / canonical / OG from Gulp export.

---

## Duplicate prevention (mandatory)

On WordPress cutover, forbidden pairs:

```text
static <title> + wp title
static canonical + SEO plugin canonical
static OG + SEO plugin OG
static twitter + SEO plugin twitter
duplicate favicon link sets
```

Migration step: remove or gate static meta partial; port **values** into theme/SEO config, not parallel HTML.

---

## Static head replacement boundary

1. Export final per-page title/description/canonical/OG map from V7 page parameters.  
2. Map into WP page templates / SEO fields.  
3. Delete static meta block from theme when `wp_head()` owns the same tags.  
4. Keep body partials separate from head ownership.

---

## `wp_head()` boundary

Theme `header.php` should contain:

- charset/viewport (or via `add_theme_support` / core)
- `wp_head()` hook output
- theme stylesheet enqueue — not hardcoded duplicate `style.css` if already enqueued

Gulp `head.html` is **reference implementation**, not runtime on WP.

---

## SEO plugin duplicate prevention

- Pick **one** SEO authority before launch.
- Disable theme hardcoded OG if plugin provides OG.
- Verify view-source: single `og:title`, single `canonical`, single `description`.

---

## WordPress site icon boundary

- Use WP Customizer → Site Icon for favicon/apple-touch.
- Do not also ship static favicon `<link>` set from Gulp in production theme.
- SVG favicon policy: follow WP version + browser support decision at cutover.

---

## Environment note

Static template keeps `robots: index, follow`. Dev/staging WP should use infrastructure/policy `noindex` — not by editing production static contract.
