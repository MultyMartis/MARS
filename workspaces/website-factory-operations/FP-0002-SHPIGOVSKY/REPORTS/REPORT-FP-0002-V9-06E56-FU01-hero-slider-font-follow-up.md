# REPORT — FP-0002 V9-06E56-FU01 Hero, Slider and Font Follow-up

**Date:** 2026-07-16  
**Project:** FP-0002 «Шпиговский»  
**Runtime:** http://shpigovsky.test/  
**Overall:** PARTIAL PASS — operator review pending  
**Commit / push / freeze:** none  
**DB writes:** 0  

---

## 1. Overall Status

- **Verdict:** PARTIAL
- Operator review pending
- Tasks A–C: PASS (local validation)
- Task D Libertinus Serif: WAITING_FOR_OPERATOR_ASSET
- DB writes: **0**
- No commit, no push, no freeze

## 2. Pre-Change Checkpoint

- **Path:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e56-fu01-before-hero-slider-font-follow-up-20260716-191824\`
- Includes: source+runtime hero/gallery/CSS/JS/helpers copies, `hashes.csv`, `operator-change-manifest.csv`, `BACKUP-INFO.md`, `BACKUP-OK.txt`
- **Marker:** operator CSS/HTML = current canon; checkpoint before FU01; no broad sync; DB writes prohibited; no commit/push/freeze
- **Protected pre-wave runtime `v9-style.css`:** `0003146F3BFFB14516AFD4B478E52850DE20B17C2BA07A5116E86D9C6D3B9429`
- Full DB dump: not taken (no DB writes)

## 3. Operator Manual Changes Preserved

### Source/runtime inventory (pre-wave)

| Metric | Value |
|--------|-------|
| Same hash | 643 |
| Hash differ | 1 (`assets/css/v9-style.css`) |
| Only source / only runtime | 0 / 0 |

### Runtime-only promoted → source

- `v9-style.css` operator edits (footer credit hover; `.services-inner-hero-v2__media` aspect-ratio cascade 767→370; `.hero__title` 30px @550px)
- Promote hash: `0003146F…` (exact runtime authority)

### After FU01

- Additive FU01 CSS appended **after** operator rules (hero aspect + gallery chrome)
- Post-wave `v9-style.css`: `0E1D29F169A386127E07D5C844DAD0281192E77C80D27AF6CA8C3EA9EAA143E9` (source == runtime)
- Unresolved theme drift: **none** for delivered files

## 4. Home Hero Demo Fallback Removal

- **Root cause:** per-slide inject in `template-parts/home/hero.php`:
  - empty title → `Шпиговский дом`
  - empty text → `Центр профилактики и&nbsp;лечения зависимостей`
- **Exact fix:** conditional render only when ACF field non-empty; emergency empty-slides shell = image only
- **Empty-field behavior:** empty text → no `.hero__tagline`; empty title → no `.hero__title`; other fields independent
- **Validation:**
  - Slide 1: title + tagline populated — PASS
  - Slide 2: title `Центр реабилитации`, empty text — **no tagline element** — PASS
  - Per-slide button: N/A (no ACF button subfield; global CTA retained)
  - Image + title only: PASS (slide 2)

Evidence: `home-hero-fallback-source-trace.md`, Playwright `validation-matrix.json` → `heroSlides`

## 5. Home Hero Aspect-Ratio Alignment

### Operator authority rules (runtime, preserved)

| Breakpoint | `.services-inner-hero-v2__media` aspect-ratio |
|------------|-----------------------------------------------|
| ≤767 | 100/70 |
| ≤700 | 100/80 |
| ≤650 | 100/90 |
| ≤550 | 100/100 |
| ≤490 | 100/110 |
| ≤450 | 100/130 |
| ≤410 | 100/150 |
| ≤370 | 100/170 |

(Also pre-existing ≤1024 rule `100/60` + `min-height:410px` retained untouched.)

### Home selectors changed

- `.hero--home` — `height:auto; max-height:none; aspect-ratio:…` at the same breakpoints (≤767 cascade)
- Slider children forced to fill aspect box (`height:100%`)

### Comparison matrix (PASS 4/4)

| Viewport | Ordinary W×H | Ordinary aspect | Home W×H | Home aspect | Δ | Result |
|----------|--------------|-----------------|----------|-------------|---|--------|
| 767×1024 | 722×505.39 | 1.4286 | 752×526.39 | 1.4286 | ~0 | PASS |
| 390×844 | 345×517.5 | 0.6667 | 375×562.5 | 0.6667 | 0 | PASS |
| 375×812 | 330×495 | 0.6667 | 360×540 | 0.6667 | 0 | PASS |
| 320×568 | 290×493 | 0.5882 | 320×544 | 0.5882 | 0 | PASS |

Screenshots: `screenshots/home-hero-*`, `screenshots/ordinary-hero-media-*`

## 6. Service Category Gallery Alignment

### Home gallery authority

- JS: `shpigovskyGallerySwiperOptions` (shared)
- CSS: wrapper `display:flex`, slide `min-width:0`, image 372/max 310 (280 @≤1024)

### Old service CSS gap

- Swiper options already shared
- Image chrome used `aspect-ratio:4/3` + grid leftovers; wrapper lacked Home flex/`min-width` parity

### New service settings

- Additive CSS only under `.page-uslugi-v2 …[data-services-category-gallery]`
- Wrapper `display:flex`; item `min-width:0`; image heights match Home
- Home gallery / articles slider untouched

### Responsive validation (PASS 7/7)

Identical Swiper params + image heights + no page overflow at 1440/1280/1024/768/390/375/320.

Evidence: `gallery-comparison.csv`, `home-gallery-configuration-snapshot.md`

## 7. Libertinus Serif

- **Status:** WAITING_FOR_OPERATOR_ASSET
- No Libertinus files in project / OPERATOR-ASSETS / Storage search
- Required: local Regular WOFF2 for weight **400** (computed on both selectors)
- Preferred: `LibertinusSerif-Regular.woff2` (or equivalent Regular)
- Selectors pending: `.hero__title`, `.services-inner-hero-v2__title`
- Computed proof (390px): still Inter; size/weight/line-height/letter-spacing unchanged by this wave
- No CDN; no substitute font

## 8. Exact Files Changed

### Canonical source

- `WORDPRESS/theme/shpigovsky/template-parts/home/hero.php`
- `WORDPRESS/theme/shpigovsky/assets/css/v9-style.css` (operator promote + FU01 additive)

### Runtime

- Matching exact-hash delivery of the two files above

### Reports / evidence

- `REPORTS/REPORT-FP-0002-V9-06E56-FU01-hero-slider-font-follow-up.md`
- `REPORTS/evidence/v9-06e56-fu01-hero-slider-font-follow-up/*`
- `PROJECT-STATUS.md` (status line)

### Operator files merged

- Runtime `v9-style.css` promoted to source before edits

## 9. Source-to-Runtime Delivery

| File | Source SHA256 | Runtime SHA256 | Match |
|------|---------------|----------------|-------|
| `hero.php` | `10E090C4…0B4897B9` | `10E090C4…0B4897B9` | Yes |
| `v9-style.css` | `0E1D29F1…EA143E9` | `0E1D29F1…EA143E9` | Yes |

- Exact-file only; **no broad sync**
- Operator CSS rules retained inside the same file

## 10. Validation

| Area | Result |
|------|--------|
| Home hero empty text | PASS — no demo tagline on slide 2 |
| Aspect ratios | PASS 4/4 |
| Service galleries vs Home | PASS 7/7 |
| Font | WAITING_FOR_OPERATOR_ASSET |
| Frontend regression | PASS (listed routes 200; no PHP warning heuristics; no page JS errors in probe) |
| Admin regression | PASS structural (no ACF/admin/CSS admin files touched; DB writes 0) |

## 11. Risks and Tails

- Libertinus assets missing (Task D open)
- Gallery mobile base `slidesPerView:4` (<431) matches Home authority; visually dense on narrow phones — intentional parity
- Gallery screenshot crops of slider roots are small on some viewports; measurement CSV is primary proof
- Pre-existing unrelated FP-0002 dirty WIP outside this wave remains untouched
- `who-we-treat` gallery (non-Swiper) out of scope — no `data-services-category-gallery`

## 12. Git Status

- No commit
- No push
- Exact FP-0002 scope only
- Foreign WIP untouched

## 13. Operator Review Checklist

- [ ] Second Home hero slide has no demo description
- [ ] Home hero mobile height matches ordinary `.services-inner-hero-v2__media`
- [ ] Service category gallery behaves like Home gallery
- [ ] Libertinus appearance (blocked until font files provided)
- [ ] No operator CSS was lost (footer credit hover + media aspect cascade)

## Execution safety

- cwd: `X:\AI MARS`
- Volume: `AI WS` (X:)
- Branch: `mars/canonical-post-recovery`
- Scope lock: FP-0002 + MARS-Localhost shpigovsky (+ backup root)
- Destructive ops: none
