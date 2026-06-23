# FP-0002 V6 Pre-reviews block map v2

**Authority:** `HOME-PAGE-FULL-MOCKUP.jpg` (SHA-256 `CDD1D5BCC512B617DCF93EFA97AF88CF4AD99A0895CFC27A63C07BC704945290`)  
**Supersedes:** `FP-0002-V6-PRE-REVIEWS-BLOCK-MAP.md` (v1 — **REJECTED_INCOMPLETE**)

## Inspected range

Gallery start through Reviews boundary (Reviews **NOT STARTED**).

| Order | Block name | Start Y | End Y | Main content | Existing implementation | Required action |
| ----: | ---------- | ------: | ----: | ------------ | ----------------------- | --------------- |
| 1 | Photo gallery (4 slides) | 3610 | 3810 | horizontal Swiper strip, no heading | `home-gallery.html` + Swiper vendor | REPAIR |
| 2 | Why-us heading + 8 icon cards | 3860 | 4544 | H2, lead, body, feature cards | `home-why-us.html` | PRESERVE |
| 3 | Staff group photo | 4544 | 4992 | full-width team photograph | **NONE** → `home-staff-photo.html` | IMPLEMENT |
| 4 | Centered feature grid (6 cards) | 4992 | 5480 | 3×2 text-only benefit cards | **NONE** → `home-feature-grid.html` | IMPLEMENT |
| 5 | Clinic landscape photo | 5480 | 6064 | full-width exterior photograph | **NONE** → `home-clinic-landscape.html` | IMPLEMENT |
| 6 | Reviews | 6064 | — | review cards + heading «Отзывы» | NOT STARTED | **STOP** |

**Total blocks before Reviews:** 5 (gallery + why-us + 3 recovered blocks)  
**Reviews start Y:** 6064 (`BLOCK-013` / Figma frame `1:1050`)

## V1 omissions

| Missing from v1 | Resolution |
| --------------- | ---------- |
| Staff group photo (SECTION-003) | Implemented `home-staff-photo.html` |
| Centered 6-card grid (BLOCK-010) | Implemented `home-feature-grid.html` |
| Clinic landscape (BLOCK-011) | Implemented `home-clinic-landscape.html` |
| Reviews boundary Y | Corrected to **6064** (not 3740 overlap) |
| Benefit 6-grid at 6064 | **Not a separate block** — Y 6064 is Reviews heading band |

## Existing visual system mapping

| Needed role | Existing system |
| ----------- | --------------- |
| Container | `.container` |
| Heading | `.home-why-us__heading` pattern / H2 tokens |
| Icon cards | `.home-recovery-intro__card*` (why-us) |
| Centered cards | `.home-feature-grid__card*` (reuses border/radius/spacing tokens) |
| Bleed photos | `.home-staff-photo__*`, `.home-clinic-landscape__*` |
| Radius | `--radius-main` |
| Spacing | `--pad-gap`, `--pad-y` |

## Placeholder content

NONE — texts from Figma extract / canonical mockup crops; images cropped from canonical JPG.
