# FP-0002 V6 LOCAL INTER ZERO-FOUT REVIEW

**Date:** 2026-06-23  
**Branch:** mars/post-cycle8-live-tests  
**Checkpoint before:** a4c7b9c9756d419701a58bf26eeb3e4a8522b231

## Operator observation

Operator continues to see visible fallback-to-Inter switch with Google Fonts + `font-display: swap`. Previous automated report incorrectly claimed the issue was materially resolved. Operator visual validation overrides automated CLS/screenshot acceptance.

## Previous root cause

External Google Fonts delivery with `display=swap` allowed fallback stack (`system-ui`, `Segoe UI`, etc.) to paint before Inter WOFF2 arrived from `fonts.gstatic.com`. Network latency caused visible font swap on Header phones, navigation, Hero heading/body, buttons, and Footer.

## Canonical src protection

| File | Operator changes detected | Protected | Allowed modification |
|------|---------------------------|----------:|----------------------|
| index/head | Google Fonts links only (no design edits) | YES | font delivery only |
| style.scss | Fonts section comments only; all design tokens/blocks unchanged | YES | local @font-face only |
| Gulpfile | No operator diff vs checkpoint | YES | no change required |
| Header/Hero/Footer partials | No operator diff vs checkpoint | YES | no design changes |

`git diff HEAD -- src/` showed zero design-value changes outside font delivery scope.

## Current Inter version

Google Fonts Inter **v20** (`fonts.gstatic.com/s/inter/v20/`), static subset WOFF2 equivalent via `@fontsource/inter@5.2.8`.

## Font source and provenance

- Package: `@fontsource/inter@5.2.8` (mirrors Google Fonts static WOFF2)
- License: SIL Open Font License 1.1
- Provenance note: `src/fonts/inter/INTER-FONT-PROVENANCE.md`

## Local files

```text
src/fonts/inter/inter-300.woff2
src/fonts/inter/inter-300-latin.woff2
src/fonts/inter/inter-400.woff2
src/fonts/inter/inter-400-latin.woff2
src/fonts/inter/inter-500.woff2
src/fonts/inter/inter-500-latin.woff2
```

## Required weights

300, 400, 500 — confirmed from `--font-weight-base`, `--font-weight-heading`, `--font-weight-button` in `style.scss`.

## Gulp font pipeline

**Before:** `fonts()` task copied `src/fonts/**/*` → `dist/assets/fonts/` (already present; no Gulp change required).  
**After:** Same pipeline; Inter WOFF2 files now populated under `src/fonts/inter/`.

## Local @font-face

Six `@font-face` rules at top of `src/scss/style.scss` — cyrillic + latin unicode-range per weight (300, 400, 500).

## font-display

`block` for all local Inter faces. `swap` removed.

## Preload strategy

Critical above-fold weights preloaded in `<head>` before main stylesheet:

- `inter-400.woff2` (cyrillic — nav, headings, phones Cyrillic context)
- `inter-400-latin.woff2` (latin — phone digits, schedule digits)
- `inter-300.woff2` (cyrillic — hero tagline / base weight)

500 not preloaded (buttons load via stylesheet discovery; acceptable latency with local files).

## Google Fonts removal

Removed from `src/pages/index.html`:

- `preconnect` to `fonts.googleapis.com`
- `preconnect` to `fonts.gstatic.com`
- stylesheet link to Google Fonts CSS

No `@import url("https://fonts.googleapis.com/...")` in SCSS.

## Network validation

| Check | Result |
|-------|--------|
| `fonts.googleapis.com` requests | 0 |
| `fonts.gstatic.com` requests | 0 |
| External Inter requests | 0 |
| Preload warnings | NONE |
| WOFF2 MIME (file:// cold load) | NOT APPLICABLE (local file protocol; production expects `font/woff2`) |

## Cold-cache validation

3 cold passes (Playwright Chromium, cache disabled, new context each):

| Pass | FCP ms | fonts.ready ms | FOUT | fallback visible |
|------|--------|----------------|------|------------------|
| cold_1 | 1112 | 0 | NOT OBSERVED | NOT OBSERVED |
| cold_2 | 276 | 0 | NOT OBSERVED | NOT OBSERVED |
| cold_3 | 260 | 0.1 | NOT OBSERVED | NOT OBSERVED |

## Warm-cache validation

2 warm passes — no font swap, no external font requests, `document.fonts.status = loaded`.

## Frame-by-frame evidence

Screenshots in `reviews/foundation/visual/`:

- `FP-0002-V6-LOCAL-INTER-FIRST-PAINT.png` (0 ms)
- `FP-0002-V6-LOCAL-INTER-50MS.png`
- `FP-0002-V6-LOCAL-INTER-100MS.png`
- `FP-0002-V6-LOCAL-INTER-FONTS-READY.png`
- `FP-0002-V6-LOCAL-INTER-FULL.png`

## document.fonts validation

All cold passes:

```text
document.fonts.check('300 16px "Inter"') → true
document.fonts.check('400 16px "Inter"') → true
document.fonts.check('500 16px "Inter"') → true
document.fonts.status → loaded
```

Computed fonts on Header phone, Hero title/tagline, Hero button: `font-family: Inter, ...` with correct weights.

## FOUT result

**NOT OBSERVED** in technical Playwright validation (no visible fallback-to-Inter switch in filmstrip captures).

## FOIT result

**NOT OBSERVED OR NOT MATERIAL** — `font-display: block` with local preload; text visible without extended blank period in captures.

## CLS result

| Metric | Before (Google Fonts) | After (local) |
|--------|-------------------------|---------------|
| cls_total | 0.0064 | 0.0100 (cold_1 primary pass) |

CLS slightly higher in one cold pass; shift sources remain hero/footer layout nodes — not new design values. Operator criterion (visible font switch) takes priority over small CLS delta.

## Header stability

PRESERVED — no design value changes. Font family resolves to Inter from first paint in validation.

## Hero stability

PRESERVED — no design value changes.

## Footer stability

PRESERVED — no design value changes. Minor FA YouTube glyph shift from prior pass not reintroduced by font change.

## Font Awesome note

FA remains external via shared vendor bridge; minor YouTube icon CLS from prior metrics not addressed in this task (out of scope). Does not affect Inter FOUT gate.

## Remaining risks

- Operator visual confirmation still required (file:// validation ≠ operator browser/CDN).
- Production server must serve WOFF2 with `font/woff2` and long cache headers.
- Weight 500 not preloaded — possible brief block on first button paint under extreme throttling.

## Final verdict

```text
FP-0002 INTER DELIVERY — LOCAL WOFF2
GOOGLE FONTS DEPENDENCY — REMOVED
EXTERNAL INTER REQUESTS — ZERO
CRITICAL FONT PRELOAD — ACTIVE
FONT-DISPLAY SWAP — REMOVED
VISIBLE FALLBACK-TO-INTER SWITCH — NOT OBSERVED IN TECHNICAL VALIDATION
OPERATOR FONT APPROVAL — PENDING OPERATOR REVIEW
```

## Previous report correction

Added to operational status and logs:

```text
Previous Google Fonts + swap solution did not eliminate visible FOUT.
Operator validation overrules automated screenshot/CLS acceptance.
```
