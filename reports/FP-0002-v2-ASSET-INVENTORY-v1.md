# FP-0002 v2 — Asset Inventory v1

**Document type:** Asset Inventory (v2 audit pass)  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-22  
**Sources:** FIG forensic (`Шпиговский.fig`), `INCOMING/01_DESIGN/`, `INCOMING/03_BRANDING/`, legacy stress-test findings (reference only)

**Status legend:** **FOUND** · **MISSING** · **SAFE UNKNOWN**

---

## 1. Executive summary

| Asset class | Standalone intake | Embedded in FIG | v2 build readiness |
|-------------|-------------------|-----------------|-------------------|
| Logos | **MISSING** | **FOUND** (raster in header — e.g. `image 219`) | Extract at Discovery |
| Photos | **MISSING** | **FOUND** (166 ZIP images, 562 fill refs) | Extract with hash manifest |
| Icons | **MISSING** | **FOUND** (vectors + messenger icons in chrome) | Extract / SVG trace TBD |
| Illustrations | **MISSING** | **FOUND** (decorative vectors) | Per-block extraction |
| Backgrounds | **MISSING** | **FOUND** (hero washes, band fills) | CSS + raster split TBD |
| Videos | **MISSING** | **SAFE UNKNOWN** — poster frame in FIG `Видео`; no video file in intake | Operator drop or embed URL |
| Favicons | **MISSING** | **SAFE UNKNOWN** — not in FIG export metadata | Await client drop |
| Fonts (WOFF/TTF) | **MISSING** | **FOUND** (family names on TEXT nodes) | CDN Inter per Production Standards v3 |

---

## 2. Brand assets

| ASSET | LOCATION | STATUS | Notes |
|-------|----------|--------|-------|
| Logo — primary mark | FIG `Хедер` → `image 219` | **FOUND** (FIG) | No standalone SVG/PNG in `03_BRANDING/` |
| Logo — decorative vectors | FIG `Frame 81513852` | **FOUND** (FIG) | Hero/header overlap zone |
| Brand guidelines PDF | `03_BRANDING/` | **MISSING** | README only |
| Color specification file | — | **MISSING** | Colors in FIG variables + Production Standards v3 |
| Wordmark / subtitle text | FIG TEXT nodes | **FOUND** (FIG) | «Центр профилактики…», «Шпиговский дом» |

---

## 3. Raster inventory (FIG embedded)

| Metric | Value | Source |
|--------|-------|--------|
| Files in FIG ZIP `images/` | **166** | FIGMA Forensic Test v1 |
| Image fill references in tree | **562** | Same |
| Standalone pack in INCOMING | **0** | Source Availability Check |
| JPG visual control (Home only) | **1** — `HOME-PAGE-FULL-MOCKUP.jpg` | **FOUND** · 8.1 MB |

**Extraction contract (v2):** per-block manifest with SHA-1 from FIG hash filenames — **mandatory** before wiring `src/img/`.

---

## 4. Icon inventory

| Context | FIG evidence | Standalone | Status |
|---------|--------------|------------|--------|
| Messenger (Telegram/WhatsApp) | FRAME `telegramm`, `watsapp` | — | **FOUND** (FIG) |
| Search | INSTANCE `search` | — | **FOUND** (FIG) |
| Chevron / accordion | `chevron-down`, `Стрелка` | — | **FOUND** (FIG) |
| UTP / feature / step icons | INSTANCE `Цифра`, `этап` | — | **FOUND** (FIG) |
| Social footer icons | Footer subtree | — | **FOUND** (FIG) · **SAFE UNKNOWN** exact export set |
| SVG sprite pack | — | — | **MISSING** |

---

## 5. Font assets

| Font | FIG TEXT usage | Files in intake | Status |
|------|----------------|-----------------|--------|
| **Inter** (Light/Medium/Regular/Thin/Bold) | **1860+** nodes | **MISSING** | **FOUND** (reference) — load via Google Fonts per Production Standards v3 |
| Libertinus Serif | 52 nodes | **MISSING** | **FOUND** (FIG) — display/accent; **SAFE UNKNOWN** if required in production CSS |
| Roboto / Rubik / Manrope / Prata / Raleway | ≤33 nodes each | **MISSING** | **SAFE UNKNOWN** — legacy or component-library residue; verify before loading |

---

## 6. Favicon

| Item | Status |
|------|--------|
| favicon.ico / PNG set in `INCOMING/` | **MISSING** |
| Favicon in FIG | **SAFE UNKNOWN** |
| Legacy `src/favicon/` (old workspace) | **REFERENCE ONLY** — **do not copy** without hash verify |

---

## 7. ASSET_IDENTITY_COLLISION register

| ID | Finding | Severity | v2 action |
|----|---------|----------|-----------|
| **COL-001** | Legacy Home stress-test: hash **`d3ac7d00`** reused across unrelated section exports | **CRITICAL** | **REJECT** legacy `src/img/` for any v2 wiring |
| **COL-002** | ~56% orphan assets in legacy workspace vs DOM | **HIGH** | New manifest per pilot slice only |
| **COL-003** | FIG images keyed by SHA-1 — same hash = same file (expected); different blocks must not reuse wrong hash | **MEDIUM** | Discovery export QA gate |
| **COL-004** | JPG mockup vs FIG/PDF header phone strings differ | **MEDIUM** | Operator tie-break before header text-lock |

**Rule for v2:** No asset from `workspaces/fp-0002-shpigovsky-frontend/src/img/` enters v2 without per-file FIG hash match.

---

## 8. Per-page asset readiness (pilot-relevant)

| PAGE ID | Photos | Icons | Logos | Video | Ready for extract |
|---------|--------|-------|-------|-------|-------------------|
| PG-001 | FIG | FIG | FIG | Poster only | PARTIAL |
| PG-005 | FIG | FIG | Shared chrome | — | **YES** (with manifest pass) |
| PG-006 | FIG | FIG | Shared | — | YES |
| PG-011 | Minimal | FIG | Shared | — | YES |

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 (v2 audit pass) |
| Next | Discovery asset manifest for pilot slice |
