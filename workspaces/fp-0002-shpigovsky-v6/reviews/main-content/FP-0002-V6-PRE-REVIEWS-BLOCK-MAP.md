# FP-0002 V6 Pre-reviews block map

| Order | Block role | Existing component mapping | New HTML needed | New styles needed | Status |
| ----: | ---------- | -------------------------- | --------------: | ----------------: | ------ |
| 1 | Photo gallery (4 slides) | `.container`, `--radius-main`, `--pad-gap`, Swiper vendor | YES (`home-gallery.html`) | YES (gallery block in `style.scss`) | IMPLEMENTED |
| 2 | Why-us heading + copy + feature cards (`Нас выбирают`) | `.home-recovery-intro__card-grid`, `.home-recovery-intro__card`, heading/body tokens | YES (`home-why-us.html`) | YES (spacing wrappers only in `style.scss`) | IMPLEMENTED |
| 3 | Reviews (`Отзывы`) | NOT STARTED | NO | NO | NOT_STARTED — boundary reached |

Authority: `HOME-PAGE-FULL-MOCKUP.jpg` gallery Y 3646–3780; next section heading at Y 3740 (`Нас выбирают`). Figma SECTION-04 frame `1:991`.

Reviews boundary: Figma SECTION-05 frame `1:1050` — **NOT STARTED**.

---

## Correction entry (2026-06-23) — v1 REJECTED_INCOMPLETE

v1 omitted staff group photo (Y 4544–4992), centered 6-card grid (Y 4992–5480), clinic landscape (Y 5480–6064). Superseded by `FP-0002-V6-PRE-REVIEWS-BLOCK-MAP-V2.md`. Reviews start Y corrected to **6064**.
