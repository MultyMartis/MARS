# FP-0002 — Services General Asset Map v1

**Planning ID:** `services-general-01`  
**Date:** 2026-06-26  
**Rule:** No exports performed in this task. No PNG copied to `src/`.

---

## Asset table

| Section | Asset role | Existing source asset | New export required | Format | Notes |
| ------- | ---------- | --------------------- | ------------------: | ------ | ----- |
| Hero | Background photo | None for Services | **Yes** | webp | Interior hallway from PNG; distinct from `hero-main.png` |
| Category 1 | Gallery ×3 | None | **Yes** | webp | Category-specific clinical/lifestyle photos per PNG |
| Category 2 | Gallery ×3 | None | **Yes** | webp | Mental health themed |
| Category 3 | Gallery ×3 | None | **Yes** | webp | Eating disorders themed |
| Category 4 | Gallery ×3 | None | **Yes** | webp | Genotyping themed |
| Category * | BG watermark | None | **Yes** | webp/svg | Lifebuoy watermark — Figma layer export |
| Program | Direction images | `assets/img/content/rehabilitation-program/*.webp` | No | webp | Reuse existing 4 images |
| Founder | Portrait | `assets/img/content/founder-sergey-shpigovsky.png` | No | png | Reuse |
| Founder | Quote mark | Inline SVG in partial | No | svg | Reuse |
| Comfort | Gallery set | `assets/img/content/home-comfort/*.webp` | No | webp | Reuse + logo.svg |
| FAQ | Chevron icons | Font Awesome (existing) | No | — | Reuse |
| Services list | External link icon | `assets/svg/external-link.svg` | No | svg | Reuse from Package #002 |
| Final form | Band background | CSS / existing pattern | SAFE_UNKNOWN | — | Verify against PNG dark band |
| Header/Footer | Logo, icons | Existing branding assets | No | svg | Reuse |

---

## Reuse summary

| Status | Count |
|--------|------:|
| Reuse existing | 8 asset groups |
| New export required | 13+ images (hero + 4× gallery + watermark) |
| AI-generated | **None** |

---

## Export authority

1. Figma `Услуги хаб` visible image fills  
2. PNG 26.06.2026 crop reference for object-position  
3. Operator-provided INCOMING assets if already present

---

## Asset verdict

**New exports required before visual QA pass.** Pass 1 may use placeholder paths only if operator explicitly approves — default gate: export from Figma before final QA.

---

*End of asset map v1.*
