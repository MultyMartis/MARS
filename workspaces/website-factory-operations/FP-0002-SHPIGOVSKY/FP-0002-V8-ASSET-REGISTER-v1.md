# FP-0002 V8 — Asset Register v1

**Date:** 2026-07-01  
**Workspace:** `workspaces/fp-0002-shpigovsky-v8/`  
**Dist mirror:** `dist/assets/`

Assets grouped by function — not a raw dist file listing.

---

## Brand

| Asset / group | Source path | Consumers | Authority | WP ownership |
|---------------|-------------|-----------|-----------|--------------|
| Logo (header/footer) | `src/svg/` + img references in header/footer | All pages | Figma `Spig_v1.2.fig` / operator-approved PNG | Theme customizer / media |
| OG default | `src/img/social/og-default.jpg` | Meta fallbacks | Project | Media library |
| Favicon set | `src/favicon/` | All pages | Starter pattern | Theme |

---

## Icons

| Asset / group | Source path | Consumers | Notes |
|---------------|-------------|-----------|-------|
| Font Awesome Pro 5.15.4 | `shared/assets/icon-libraries/...` (via gulp bridge) | UI icons (`fas fa-*`) | Not in `src/img` |
| Inline SVG | `src/svg/` | Decorative UI | Copied to `dist/assets/svg/` |

---

## Fonts

| Asset | Path | Consumers |
|-------|------|-----------|
| Inter WOFF2 | `src/fonts/` | Global typography in `style.scss` |

**Rule:** Local WOFF2 default; no arbitrary new font families without operator approval.

---

## Page imagery — Home

| Group | Path pattern | Consumers |
|-------|--------------|-----------|
| Hero | `src/img/content/hero/` | `hero.html` |
| Gallery | `src/img/content/home-gallery/` | `home-gallery.html` |
| Staff photo | `src/img/content/home-staff/` | `home-staff-photo.html` |
| Recovery life | `src/img/content/recovery-life/` | `home-recovery-life.html` |
| Clinic landscape | `src/img/content/clinic-landscape/` | `clinic-landscape.html` |
| Home articles teasers | `src/img/content/home-articles/` | `home-articles.html`, blog cards |

**Crop/fit:** `object-fit` and aspect wrappers in SCSS per block; do not normalize globally.

---

## Blog archive

| Asset | Path | Consumers |
|-------|------|-----------|
| Card thumbnails | `src/img/content/home-articles/*.webp` | Archive cards (shared with home teasers) |

**Mobile:** Same assets; layout stacks via SCSS.

---

## Blog Article

| Asset | Path | Consumers |
|-------|------|-----------|
| Featured image | `home-articles/article-alcohol-dependence.webp` | Hero media |
| Inline 01–04 | `src/img/content/blog-article/blog-article-inline-0N.webp` | Body stream figures |

**Replacement risk:** High — tied to fixture article; WP uses featured image + editor uploads.

---

## Founder / person

| Asset | Path | Consumers |
|-------|------|-----------|
| Founder portrait | Referenced in `founder-quote.html` / blog founder quote | Home, article conclusion |

---

## Service images

| Group | Path pattern | Consumers |
|-------|--------------|-----------|
| Service leaf hero | `src/img/content/services/service-leaf-alcohol-hero.webp` | `usluga-konechnaya-v1.html` |
| Service v2 category | `src/img/content/services/` | Category sections |
| O-Centre / infrastructure | `src/img/content/o-centre/` etc. | O-Centre sections |

---

## Reviews

| Group | Path | Consumers |
|-------|------|-----------|
| Review cards | `src/img/content/reviews/` (if present) or inline in partial | `review-archive-card.html` |

---

## Comfort / gallery

| Group | Path | Consumers |
|-------|------|-----------|
| Comfort slides | `src/img/content/comfort/` | `comfort-gallery.html` (Swiper) |

---

## Video

| Group | Path | Consumers |
|-------|------|-----------|
| Home videos | `src/video/` | `home-videos.html` |

---

## Production status

| Status | Meaning |
|--------|---------|
| APPROVED_BASELINE | In operator-approved baseline |
| PLACEHOLDER | Temporary copy-linked or duplicate slug assets |
| DEFERRED | Awaiting operator polish / client media |

Most raster assets are **APPROVED_BASELINE** for demo. Article internal link placeholders in copy are **PLACEHOLDER** (not asset defects).

---

## Static demo (07C) notes

- Demo package must copy `dist/assets/**` with relative paths.
- No absolute `X:\` or `file://` references.
- Excel-driven pages may reuse template imagery with placeholder content.

---

*Asset register — functional grouping for FP-0002 V8.*
