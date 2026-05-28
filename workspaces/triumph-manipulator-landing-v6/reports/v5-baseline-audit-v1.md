# V5 Baseline Audit (v1)

**Workspace:** `C:\AI MARS\workspaces\triumph-manipulator-landing-v5`  
**Scope:** `index.html` baseline only (`src/pages/index.html` → `dist/index.html`)  
**Date:** 2026-05-24  
**Method:** Human-operated Website Factory hardening audit (documentation + build grep)

---

## Summary

| Area | Status | Notes |
|------|--------|-------|
| Typography risks | **WARN** | Google Fonts external dependency; body safe-wrap prep applied |
| CLS risks | **WARN** | Hero `width`/`height` on img are placeholders (1920×1080); verify vs real asset |
| Unsafe fonts | **WARN** | Montserrat/Roboto via `fonts.googleapis.com` in `head-v5-page01.html` |
| Google Fonts | **FINDING** | Present — file:// works only if network available for font CSS |
| Unstable headings | **LOW** | `clamp()` on H2; `min-width: 0` on titles — acceptable for baseline |
| Overflow hacks | **PASS** | No `break-all` / `anywhere` in `src/` |
| Absolute `/assets/` paths | **PASS** | Built `dist/index.html`: 0× `/assets/`; relative `assets/` used |
| file:// compatibility | **PASS** | Relative asset paths; local Font Awesome vendor bundled |
| dist/src drift | **PASS** | Single page build; gulp rewrite confirmed |
| Duplicate DOCTYPE/head | **PASS** | 1× `<!DOCTYPE`, 1× `<html` in built output |
| shared-assets usage | **PASS** | Hero + second screen copied from design pack lock paths |
| Pseudo-bg hero patterns | **MITIGATED** | Index uses `<img class="first-screen__bg-media">`; legacy `.first-screen` CSS url remains in `_base.scss` but overridden for `ppc-*` pages |

---

## Typography

- **Applied (safe prep):** `overflow-wrap: break-word`, `word-break: normal`, `hyphens: manual` on `body` (`src/scss/base/_base.scss`).
- **Not applied:** META/ALT content unchanged (no typography engine).
- **Manual `&nbsp;`:** Preserved in partials — not stripped.
- **Risk:** External Google Fonts — FOUT/FOIT and offline file:// preview without network.

---

## CLS / layout

- Hero media layer is explicit `<img>` (not pseudo-element).
- Hero img dimensions declared — may not match true file dimensions → possible layout shift until human QA.
- Second screen uses `object-fit: contain`, `height: auto`, `overflow: visible` on `--index-baseline` — reduces crop-related CLS vs cover hack.
- Legacy `_base.scss` `.first-screen` still contains `url(../img/hero/hero-bg-final.jpg)` for non-PPC contexts — dead for `data-page-type="ppc-zakaz-manip"` but remains technical debt.

---

## Assets / paths

| Lock | Source | Workspace copy |
|------|--------|----------------|
| Hero | `projects/triumph-manipulator-landing/design/shared-assets/hero-bg-final.jpg` | `src/img/hero/hero-bg-final.jpg` |
| Second screen | `design/shared-assets/fotos secondscreen for landing/01.jpg` | `src/img/v5/second-screen/second-screen-index-baseline.jpg` |

**Note:** Task cited `01.png`; repo contains **`01.jpg` only** — documented as SAFE UNKNOWN.

---

## Scope / index-only

- **Pages:** Only `src/pages/index.html` retained; slug/legal pages removed from `src/pages/`.
- **Partials:** Full V4 partial tree retained (required for index includes) — not a 12-page rollout.
- **dist:** Contains `index.html` only at root; asset tree includes unused PPC second-screen images from clone (not removed in baseline pass).

---

## Build validation

| Check | Result |
|-------|--------|
| `npm run build` | **PASS** (gulp build completed) |
| Relative assets in `dist/index.html` | **PASS** |
| Hero src in dist | `assets/img/hero/hero-bg-final.jpg` |
| Second screen src in dist | `assets/img/v5/second-screen/second-screen-index-baseline.jpg` |

---

## Remaining risks (baseline)

1. Human visual QA not performed by AGENT.
2. Missing task `restored-from` path — clone source was live V4 workspace.
3. Google Fonts network dependency on file:// preview.
4. Header `backdrop-filter` — possible perf/compositing variance on older browsers.
5. Extra dist assets from clone — larger than minimal index-only asset set.
6. Hero `object-position` on img — acceptable for hero lock; second screen avoids position hacks per task.

---

## SAFE UNKNOWN

- Pixel parity vs design `01.jpg` / hero reference.
- Whether `restored-from` threaded V4 copy will appear later and differ from cloned V4.
- Production deploy parity.

---

*End of audit v1.*
