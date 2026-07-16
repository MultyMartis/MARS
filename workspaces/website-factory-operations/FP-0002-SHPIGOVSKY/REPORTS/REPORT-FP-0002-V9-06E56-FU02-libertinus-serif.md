# REPORT — FP-0002 V9-06E56-FU02 Libertinus Serif

**Factory Project:** FP-0002 — Шпиговский  
**Wave:** V9-06E56-FU02  
**Date:** 2026-07-16  
**Runtime:** http://shpigovsky.test/  
**Scope:** font-only — local Libertinus Serif Regular for `.hero__title` and `.services-inner-hero-v2__title`

## 1. Status

| Field | Value |
|-------|-------|
| Verdict | **PASS** (implementation + local validation) |
| Operator review | **pending** — not accepted / not frozen |
| DB writes | **0** |
| Commit | **none** |
| Push | **none** |
| Freeze | **none** |
| E56 acceptance | **not declared** |

## 2. Pre-Change Checkpoint

| Field | Value |
|-------|-------|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e56-fu02-before-libertinus-serif-20260716-210337\` |
| Protected files | source+runtime `v9-style.css`; `assets.php`; current `assets/fonts/`; incoming `Libertinus_Serif.zip` copy |
| Protected CSS baseline SHA256 | `0E1D29F169A386127E07D5C844DAD0281192E77C80D27AF6CA8C3EA9EAA143E9` |
| Marker | BACKUP-INFO states: FP-0002 V9-06E56-FU02; font-only; operator CSS protected; `lifebuoy.webp` excluded; DB writes prohibited; no commit/push/freeze |

## 3. Archive Inspection

| Field | Value |
|-------|-------|
| Archive | `INCOMING/OPERATOR-ASSETS/E56/Libertinus_Serif.zip` |
| Contained | `LibertinusSerif-Regular.ttf`, Italic, Bold, BoldItalic, SemiBold, SemiBoldItalic, `OFL.txt` |
| Selected | **LibertinusSerif-Regular.ttf** only |
| Internal metadata | family `Libertinus Serif`; subfamily `Regular`; PostScript `LibertinusSerif-Regular`; version `7.051;RELEASE`; `usWeightClass` **400** |
| License | SIL Open Font License 1.1 (`OFL.txt`) |
| Format decision | **TTF fallback** — archive had no WOFF2; no approved local converter (`fontTools` / `woff2_compress` / `ttf2woff2` unavailable); online conversion forbidden |

## 4. Operator Changes Preserved

| Check | Result |
|-------|--------|
| Source/runtime drift pre-wave | **MATCH** for `v9-style.css`, `assets.php`, `hero.php` |
| Promote required | **No** — operator FU01 CSS already canonical in both trees |
| Protected CSS baseline | `0E1D29F1…EA143E9` captured before edit |
| Unresolved in-scope drift | **None** |
| Operator rules retained | `.hero__title` 30px @≤550; `.services-inner-hero-v2__media` aspect cascade; Inter faces; all prior media queries |

## 5. Font Implementation

| Item | Detail |
|------|--------|
| Canonical font | `WORDPRESS/theme/shpigovsky/assets/fonts/libertinus-serif/libertinus-serif-regular.ttf` |
| Runtime font | `wp-content/themes/shpigovsky/assets/fonts/libertinus-serif/libertinus-serif-regular.ttf` |
| License / provenance | `OFL.txt` + `LIBERTINUS-SERIF-PROVENANCE.md` beside the font |
| `@font-face` | family `"Libertinus Serif"`; style `normal`; weight `400`; `font-display: swap`; `format("truetype")` — single declaration in `v9-style.css` Fonts section |
| Preload / enqueue | **No preload** — theme does not preload Inter; fonts load via CSS only; `assets.php` unchanged |
| Selectors | `.hero__title` and `.services-inner-hero-v2__title` — `font-family: "Libertinus Serif", serif;` only |

## 6. Typography Preservation Proof

Evidence: `REPORTS/evidence/v9-06e56-fu02-libertinus-serif/computed-style-matrix.csv` (24/24 PASS).

Summary (family after always begins with `Libertinus Serif`; size/weight/line-height/letter-spacing unchanged vs before):

| selector | viewport | family before → after | size | weight | line-height | letter-spacing | result |
|----------|----------|------------------------|------|--------|-------------|----------------|--------|
| `.hero__title` | 1440×900 | Inter… → Libertinus Serif, serif | 70px | 400 | 70px | normal | PASS |
| `.hero__title` | 1024×768 | Inter… → Libertinus Serif, serif | 50px | 400 | 50px | normal | PASS |
| `.hero__title` | 767×1024 | Inter… → Libertinus Serif, serif | 40px | 400 | 40px | normal | PASS |
| `.hero__title` | 390×844 | Inter… → Libertinus Serif, serif | 30px | 400 | 30px | normal | PASS |
| `.hero__title` | 375×812 | Inter… → Libertinus Serif, serif | 30px | 400 | 30px | normal | PASS |
| `.hero__title` | 320×568 | Inter… → Libertinus Serif, serif | 30px | 400 | 30px | normal | PASS |
| `.services-inner-hero-v2__title` | 1440×900 | Inter… → Libertinus Serif, serif | 36px | 400 | 36px | normal | PASS |
| `.services-inner-hero-v2__title` | ≤767 (token) | Inter… → Libertinus Serif, serif | 26px | 400 | 30px | normal | PASS |

Full 6-viewport × Home / Section / Service / Hub matrix in evidence CSV.

## 7. Font Loading Proof

| Check | Result |
|-------|--------|
| Request URL | `/wp-content/themes/shpigovsky/assets/fonts/libertinus-serif/libertinus-serif-regular.ttf` |
| HTTP | **200** |
| MIME | `font/ttf` |
| `document.fonts.check('400 70px "Libertinus Serif"')` | **true** |
| Decoding errors | **0** |
| Duplicate Libertinus requests per navigation | **1** |
| Preload failures / CORS | **none** (no preload used) |
| Verdict | **PASS** |

## 8. Exact Files Changed

### Canonical source

- `WORDPRESS/theme/shpigovsky/assets/css/v9-style.css` (additive `@font-face` + two `font-family` lines)
- `WORDPRESS/theme/shpigovsky/assets/fonts/libertinus-serif/libertinus-serif-regular.ttf` (new)
- `WORDPRESS/theme/shpigovsky/assets/fonts/libertinus-serif/OFL.txt` (new)
- `WORDPRESS/theme/shpigovsky/assets/fonts/libertinus-serif/LIBERTINUS-SERIF-PROVENANCE.md` (new)

### Runtime (exact-file delivery)

- Matching copies of the four paths above

### Reports / evidence

- `REPORTS/REPORT-FP-0002-V9-06E56-FU02-libertinus-serif.md`
- `REPORTS/evidence/v9-06e56-fu02-libertinus-serif/*`
- `PROJECT-STATUS.md` (status line)

### Unchanged (intentionally)

- `inc/assets.php` (no preload)
- templates / ACF / DB / `lifebuoy.webp` / admin E55 files

## 9. Source-to-Runtime Delivery

| File | Before | After | Match |
|------|--------|-------|-------|
| `v9-style.css` | `0E1D29F1…EA143E9` | `2F7CC5AC…74793E` | source=runtime **YES** |
| `libertinus-serif-regular.ttf` | absent | `CF4D09A5…C2F17A` | source=runtime **YES** |
| `OFL.txt` / provenance | absent | delivered | **YES** |
| `assets.php` | unchanged | unchanged | **YES** |

- Exact-file only; **no broad theme sync**
- Operator CSS preserved inside the same `v9-style.css`

## 10. Regression

Routes checked (all HTTP 200; no PHP warning heuristics; no page JS errors in probe):

- `/`, `/uslugi/`, `/uslugi/zavisimosti/`, alcohol service, depression service, `/o-centre/`, `/kontakty/`, `/blog/`

| Area | Result |
|------|--------|
| Floating header | present |
| Forms | present |
| Home hero | present |
| Font isolation | only the two title selectors |
| Admin / E55 files | not modified this wave |
| DB writes | **0** |

Evidence: `frontend-regression-matrix.csv`, `regression.json`

## 11. Reserved Asset

| Check | Result |
|-------|--------|
| `lifebuoy.webp` still in `INCOMING/OPERATOR-ASSETS/E56/` | **yes** |
| SHA256 unchanged | `B4F1C9F6A09A68F6F7C31565CF1383DA92F223BB99347D9E22D19B7543430011` |
| Connected to site this wave | **no** |
| Parallax | **deferred** |

## 12. Risks and Tails

1. **TTF fallback** — larger than WOFF2; acceptable for local bounded task; optional future local WOFF2 conversion wave if tooling is approved.
2. **MIME `font/ttf`** — served correctly; no browser decoding errors observed.
3. **No preload** — intentional parity with Inter loading architecture; FOUT possible under `font-display: swap` (expected).
4. Visual fine-tuning after operator review may still be requested (tracking/size unchanged by charter).
5. Pre-existing unrelated FP-0002 dirty WIP outside this wave remains untouched.

## 13. Git Status

- Branch: `mars/canonical-post-recovery`
- **No commit / no push**
- FU02 exact scope only mutated intentionally; monorepo foreign WIP left alone
- Do not stage with `git add .`

## 14. Operator Review Checklist

- [ ] Home hero title appearance (Libertinus Serif)
- [ ] Service / section / hub hero title appearance
- [ ] Desktop + mobile readability
- [ ] Title sizes and weights unchanged (still 400; responsive sizes intact)
- [ ] No operator CSS loss (aspect-ratio / 30px mobile title / galleries)

---

**Evidence root:** `REPORTS/evidence/v9-06e56-fu02-libertinus-serif/`  
**Checkpoint:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e56-fu02-before-libertinus-serif-20260716-210337\`
