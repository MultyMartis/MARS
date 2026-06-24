# FP-0002 V7 Gallery Caption Audit

**Frontend section:** `<section class="home-gallery">`  
**Figma desktop frame:** `3- Услуги` → `Frame 81513740` (`1:983`)  
**Partial:** `src/partials/sections/home-gallery.html`

| Slide order | Image source | Figma image node | Caption node (override) | Visible desktop | Visible mobile | Exact caption |
| ----------: | ------------ | ---------------- | ----------------------- | --------------: | -------------: | ------------- |
| 1 | `shpigovsky-gallery-01.webp` | `1:986` | `535:11179` override on instance | YES | SAFE UNKNOWN (mobile home uses separate `Услуги с фото` subtree; same asset hash `f00d963c…` with caption `1:4098` on first card) | Лечение зависимости от алкоголя |
| 2 | `shpigovsky-gallery-02.webp` | `1:987` | `535:11179` override | YES | SAFE UNKNOWN | Лудомания лечение зависимости |
| 3 | `shpigovsky-gallery-03.webp` | `1:988` | `535:11179` override | YES | SAFE UNKNOWN | Лечение подростковой зависимости |
| 4 | `shpigovsky-gallery-04.webp` | `1:989` | `535:11179` override | YES | SAFE UNKNOWN | Зависимость от постоянных покупок |

## Excluded

| Item | Reason |
|------|--------|
| `1:990` fifth card | Not in frontend gallery (4 slides) |
| Image layer names `Услуга` | Not used as captions |
| Hidden price/promo text on mobile cards | `EXCLUDED_BY_VISIBILITY` / out of gallery slide scope |

## DOM decision

**OPTION A — MINIMAL SAFE ADDITION:** `<p class="home-gallery__caption">` inside existing `.home-gallery__slide.swiper-slide`.

## Verdict

`GALLERY CAPTIONS` — **PASS** (4 visible desktop captions implemented; hidden/fifth slide excluded)
