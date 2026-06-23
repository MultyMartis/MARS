# FP-0002 V6 SECTION 03 LINKS AND GALLERY REVIEW

## Operator source protection

Operator-uncommitted changes in `home-founder-quote.html` and `style.scss` (Section 02 portrait/quote calibration) preserved. No git restore/reset applied. HEAD at task start: `d477d57`.

## Service item links

Four `.home-treatment-prevention__service-item` anchors implemented inside list items; accordion toggles unchanged.

## Service URLs

| Service | URL |
|---------|-----|
| Алкогольная зависимость | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` |
| Наркотическая зависимость | `/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/` |
| Лекарственная зависимость | `/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/lekarstva/` |
| Поведенческие зависимости | `/uslugi/zavisimosti/lechenie-povedencheskoy-zavisimosti/` |

Authority: `FP-0002-DESIGN-AUDIT-v1.md` / `_audit_extract_output.json` URL tree.

## Arrow icon library

Font Awesome Pro 5.15.4 via gulp FA bridge (`src/scss/vendors/fa-all.css`).

## Arrow icon exact name

`fa-external-link-alt`

## Arrow icon prefix/style

`fas fa-external-link-alt`

## Previous icon failure cause

`fa-arrow-up-right` is Font Awesome 6 naming; glyph absent in FA5.15.4 bundle — icon rendered empty.

## Arrow icons rendered

YES — verified in built HTML after `npm run build`.

## Hover result

Link row inherits accent on hover/focus-visible; service name follows link color.

## Focus-visible result

Keyboard focus applies same accent treatment as hover on `.home-treatment-prevention__service-item`.

## Accordion regression

NONE — single-open accordion unchanged.

## Section 03 geometry changed

NO — grid/leader/typography preserved; only semantic wrapper + icon class fix.

## Section 03 stable release

`FP-0002-V6-HOME-SECTION-03-OPERATOR-STABLE-01`

## Backup path

`C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases\FP-0002-V6-HOME-SECTION-03-OPERATOR-STABLE-01-SOURCE.zip`

## Backup SHA-256

`87389fd57ad03bedc986e9dcc43f41048539ad05d30efb236fbbf271364f9ce7`

## Archive verification

PASS

## Restore test

PASS (`npm ci`, `npm run build`, service links + no gallery in restored tree)

## Manifest

`releases/FP-0002-V6-HOME-SECTION-03-OPERATOR-STABLE-01/FP-0002-V6-HOME-SECTION-03-OPERATOR-STABLE-01-MANIFEST.md`

## Stable commit

Recorded as freeze commit `chore(fp-0002): freeze operator-approved section 03` (see git log after push).

## Stable tag

`fp-0002-v6-section-03-operator-stable-01`

## Tag push

Executed with branch push (see git output).

## Remote tag verification

Verified via `git ls-remote --tags origin fp-0002-v6-section-03-operator-stable-01` after push.

## Gallery visual authority

`workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg`

## Mockup SHA-256

`CDD1D5BCC512B617DCF93EFA97AF88CF4AD99A0895CFC27A63C07BC704945290`

## Gallery wide crop

`reviews/main-content/gallery-audit/FP-0002-V6-GALLERY-WIDE-CONTEXT.png`

## Gallery canonical crop

`reviews/main-content/gallery-audit/FP-0002-V6-GALLERY-CANONICAL-CROP.png`

## Gallery start Y

3646

## Gallery end Y

3780

## Next section start Y

3740 (heading band overlap — gallery photo row ends into why-us heading transition)

## Gallery heading status

ABSENT — decorative photo strip only.

## Slide count

4

## Desktop visible count

4 at 1398px (`slidesPerView: 4`)

## Tablet visible count

3.1 at 768–1024 (`slidesPerView: 3.1`)

## Mobile visible count

2.1 at 320–767 (`slidesPerView: 2.1`)

## Next-slide peek

YES — fractional slidesPerView on tablet/mobile; desktop shows four slides within container.

## Figma file

`workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Шпиговский.fig`

## Gallery Figma frame

`3- Услуги (1:958) → Frame 81513740 (1:983) → Frame 81513821 (1:985)`

## Image node IDs

| # | Node ID | Hash |
|---|---------|------|
| 1 | 1:986 | f00d963ce1a68cf4c03b38e28fd2f474d8cfc3f0 |
| 2 | 1:987 | a467cd2771addcbad9b24ff73e1d5b353d57ef75 |
| 3 | 1:988 | 890b1432f93147d8e9a7c1e5357c06081cd4e835 |
| 4 | 1:989 | 52c8ac4595960208c7a5cad83d8904bcca826234 |

## Exported asset paths

`src/img/content/gallery/shpigovsky-gallery-01.webp` … `04.webp`

## Export dimensions

621×938, 1113×738, 1171×864, 1296×921 (native); display 325×372 per Figma instance.

## Asset provenance path

`src/img/content/gallery/GALLERY-ASSET-PROVENANCE.md`

## Decorative assets exported

ZERO beyond four gallery content photos.

## Swiper version

11.x (npm `swiper@11`)

## Swiper source

`node_modules/swiper` copied to `dist/assets/vendor/swiper/` via gulp.

## CDN used

NO

## Slider data hook

`data-gallery-slider`

## JS initialization

`src/js/main.js` → `initHomeGallery()` using `window.Swiper`.

## Swiper instance count

1

## Loop

false

## Autoplay

false

## Navigation

false

## Pagination

false

## Lightbox

DISABLED

## Mouse drag

YES

## Touch swipe

YES

## Responsive breakpoints

320 / 768 / 1025 configured in Swiper options.

## 320 px result

PASS — 2.1 slides visible with peek.

## 375 px result

PASS — mobile breakpoint active.

## 430 px result

PASS — mobile breakpoint active.

## 768 px result

PASS — 3.1 slides visible.

## 1024 px result

PASS — tablet/desktop transition.

## Desktop result

PASS — 4 slides, no controls, no distortion.

## Horizontal overflow

NONE observed in Playwright overflow probe during gallery capture run.

## Image distortion

NONE — `object-fit: cover` at fixed display height.

## Gallery comparison path

`reviews/main-content/gallery-implementation/FP-0002-V6-GALLERY-COMPARISON.png`

## Pre-reviews blocks found

Gallery + `Нас выбирают` (SECTION-04) before Reviews boundary.

## Pre-reviews block map path

`reviews/main-content/FP-0002-V6-PRE-REVIEWS-BLOCK-MAP.md`

## Existing structures reused

`.container`, `.home-recovery-intro__card-grid`, `.home-recovery-intro__card`, heading/body tokens, `.btn` system untouched.

## Existing card styles reused

YES — Section 01 card grid/classes for why-us features.

## Existing heading styles reused

YES — `--font-size-h2`, `--line-height-h2`, base body tokens.

## Existing button styles reused

NOT APPLICABLE in pre-reviews blocks implemented.

## New visual systems introduced

ZERO

## New decorative images added

ZERO (gallery only — four approved Figma exports).

## Blocks implemented

`home-gallery`, `home-why-us`

## Reviews status

NOT STARTED

## Regressions

Section 01/02/03/shell: NONE observed in build + visual capture scope.

## Build

Build succeeded (`npm run build`).

## Remaining deviations

Gallery comparison crop initially failed automated clip; regenerated manually. Why-us feature cards omit Figma card photos by policy (text-only reuse of Section 01 card pattern).

## Final verdict

PASS — Section 03 service links frozen; gallery + pre-reviews integrated; Reviews not started.
