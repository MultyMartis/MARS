# FP-0002 V8 O-Centre Gallery Reuse Audit v1

**Date:** 2026-06-29
**Hold resolved:** CF-015 `home-gallery` audit for O-Centre charter

---

## Candidates compared

| Gallery pattern | V8 partial | Mechanism | Page |
|---|---|---|---|
| **Home gallery** | `home-gallery.html` | Swiper `data-gallery-slider`; captions below slides; 4 slides | Home only |
| **Comfort mosaic** | `comfort.html` | CSS grid + Fancybox `data-fancybox="comfort"` | Home, Services hub |
| **Category inline gallery** | `services-category-section-v2` gallery slot | Static 3-up figures; no Fancybox in hub categories | Services |
| **O-Centre design** | — | Mobile: «Комфорт, приватность»; desktop: inside «преимущества» + who-we-treat 3-up | PG-005 |

---

## Criterion matrix

| Criterion | Home gallery | O-Centre gallery | Match | Consequence |
|---|---|---:|---|
| HTML structure | `figure.swiper-slide` in Swiper wrapper | Mosaic `a` tiles OR category `figure` grid | No | Different partial families |
| Grid layout | Horizontal slider (3.5 slides desktop) | 3-col static or comfort mosaic | No | Do not reuse Swiper shell |
| Image count | 4 fixed slides | 3 (who-we-treat) + 6–7 (comfort) | No | Content-parameterized grids |
| Aspect ratio | Mixed tall/wide in slider | Comfort room ratios; category thumbs | Partial | Asset sets differ |
| Caption model | `figcaption` under each slide | Comfort: none; category: caption under thumb | Partial | Caption policy per band |
| Fancybox behavior | **None** (Swiper only) | **Fancybox** on comfort tiles | No | Different JS binding |
| Mobile behavior | `slidesPerView: 2.15` breakpoints | Vertical mosaic / stacked figures | No | CSS/option divergence |
| Page semantics in name | `home-gallery` | About comfort / conditions | No | Neutralization needed if shared |
| Init hook | Global `querySelector('[data-gallery-slider]')` single instance | Fancybox group + comfort CSS | No | Home gallery init not portable |

---

## Structural identity

**False match.** O-Centre design does **not** use the Home Swiper gallery band. Primary gallery role on O-Centre maps to **comfort mosaic (BLK-023)** and optional **static 3-up category gallery** in who-we-treat narrative.

---

## Visual identity

Home gallery: horizontal filmstrip with pagination dots. O-Centre: interior mosaic (comfort) and editorial inline thumbs — visually distinct roles.

---

## Mobile identity

Home: swiper peek. O-Centre mobile: dedicated «Комфорт, приватность» tall section — aligns with `comfort.html` responsive rules, not `home-gallery`.

---

## Fancybox identity

Home gallery: no lightbox. O-Centre comfort: Fancybox group — matches `comfort.html`, not `home-gallery`.

---

## Classification

**`SIMILAR_BUT_DIFFERENT`**

Home gallery is **not** the O-Centre gallery. Shared media intent (show facility/conditions) but **different component families**.

---

## Implementation recommendation (for future prompt)

1. **Do not** include `home-gallery.html` on O-Centre.
2. **Direct reuse** `comfort.html` (CF-006) with O-Centre copy parameters and same Fancybox group name or page-scoped group if duplicate init risk — verify single comfort instance per page.
3. For who-we-treat 3-up band: **reuse** `services-category-section-v2` gallery slot pattern via parameters OR minimal variant modifier — **not** home-gallery.
4. CF-015 `home-gallery` neutralization remains **deferred** — not required for O-Centre launch; optional future `media-gallery-slider` family if another page needs Swiper captions.
5. **Do not neutralize** `home-gallery` in this charter task.

---

## Result

**PASS** — gallery reuse boundary resolved; false reuse of `home-gallery` rejected.
