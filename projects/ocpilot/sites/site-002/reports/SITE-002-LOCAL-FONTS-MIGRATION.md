# REPORT — SITE-002 Local Fonts Migration

**Site:** SITE-002 (TEST — https://zpm.new-site.space/)  
**Checkpoint:** `SITE-002-STABLE-LIVE-LOCAL-FONTS-01`  
**Authority baseline:** `SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01`  
**Date:** 2026-06-29  
**Environment:** TEST only — production **NOT touched**

---

## 1. Verdict

| Gate | Result |
|------|--------|
| All fonts local | **PASS** |
| Google Fonts absent | **PASS** |
| CDN font CSS absent | **PASS** |
| External `@font-face` absent | **PASS** |
| Font HTTP 404 | **PASS** (all 5 weights 200) |
| Design / typography unchanged | **PASS** (font-face + preload + header only) |
| Operator Manual Polish baseline preserved | **PASS** |

**Overall:** **PASS** — `SITE-002-STABLE-LIVE-LOCAL-FONTS-01`

---

## 2. Font audit

### Families found

| Family | Usage |
|--------|--------|
| **Inter** | Sole UI sans-serif (`--font-sans`, `body`, components) |
| Font Awesome Pro | Icons only (`/assets/vendor/fontawesome-pro-5.15.4/`) — not migrated (icon font, already local) |

### Weights used in `style.css` (live pre-migration)

| Weight | Declarations | Action |
|--------|--------------|--------|
| 400 | 12 | `@font-face` → `Inter-Regular.woff2` (+ woff fallback) |
| 500 | 38 | `@font-face` → `Inter-Medium.woff2` (+ woff fallback) |
| 600 | 15 | **Fixed** — was mapped to Medium; now `Inter-SemiBold.woff2` |
| 700 | 6 | **Added** — `Inter-Bold.woff2` (new on server) |
| 800 | 3 | **Added** — `Inter-ExtraBold.woff2` (cart totals; new on server) |
| 900 | 1 | Browser synthesizes from 800 (cart grand total — single rule) |

### Weights not copied

| Weight | Reason |
|--------|--------|
| 300 and below | Not used in CSS |
| 900 file (Inter-Black) | Only 1 CSS rule — nearest weight 800 sufficient |

### Previous source

| Before | Finding |
|--------|---------|
| Google Fonts (`fonts.googleapis.com`) | **Not present** on live TEST at audit time |
| `fonts.gstatic.com` | **Not present** |
| `@font-face` in `style.css` | Local paths `../fonts/Inter-*.woff2` — **partial** (600 wrong file; 700/800 missing) |
| FOUT cause | Late CSS load chain + `font-display: swap` + missing 600/700 files + no preload |

### Local destination

```
assets/fonts/
  Inter-Regular.woff2 / .woff
  Inter-Medium.woff2 / .woff
  Inter-SemiBold.woff2 / .woff
  Inter-Bold.woff2          ← new
  Inter-ExtraBold.woff2     ← new
```

Provenance for new files: `@fontsource/inter@5.2.8` (Inter v20 latin subset, OFL).

---

## 3. Changes deployed (TEST)

| File | Change |
|------|--------|
| `assets/css/style.css` | 5 `@font-face` blocks; weight 600 → SemiBold; add 700/800 |
| `assets/css/style.min.css` | Sync `@font-face` block (safety if ever enabled) |
| `catalog/view/theme/default/template/common/header.twig` | Local `preload` for Regular + Medium woff2; remove cache-buster query on `style.css` |
| `assets/fonts/Inter-Bold.woff2` | **uploaded** |
| `assets/fonts/Inter-ExtraBold.woff2` | **uploaded** |

**Not changed:** layout, colors, spacing, typography tokens, Twig body markup, JS, controllers.

---

## 4. Backups

| Type | Path |
|------|------|
| Pre-deploy FTP → repo | `backups/style.css.pre-site-002-local-fonts-01.bak` |
| | `backups/style.min.css.pre-site-002-local-fonts-01.bak` |
| | `backups/catalog__view__theme__default__template__common__header.twig.pre-site-002-local-fonts-01.bak` |
| Pre-work git checkpoint | `13c7e6ed` — `CHECKPOINT-PRE-LOCAL-FONTS.md` |
| Work artifacts | `reports/local-fonts-work/` |

---

## 5. SHA256 (post-deploy)

| Artifact | SHA256 |
|----------|--------|
| `style.css` | `78c6e13b17632e8f8638515af5141c8a79c432ff45e215e75d56c5b3430635d7` |
| `style.min.css` | `559283779628ccff246d4a913ff5feab21540485a7da4a8d274417614fb43df9` |
| `header.twig` | `25e77e036aec73d58bda40b493da3502c73db04e6753d222cac6eeb8db9a71da` |
| `Inter-Bold.woff2` | `6f56409fd3d64bb85f7d070bce20749db2d66b6d63cec586cc22d1c761be2491` |
| `Inter-ExtraBold.woff2` | `a7d0a50f15d389cad679238466bdb5fc9787aa0715719064ce25abaff042820d` |

---

## 6. HTTP / Network verification

| URL | Status | googleapis | gstatic | preload |
|-----|--------|------------|---------|---------|
| `/` | 200 | absent | absent | Inter-Regular + Medium |
| `/about` | 200 | absent | absent | yes |
| `/katalog/` | 200 | absent | absent | yes |

| Font URL | HTTP |
|----------|------|
| `/assets/fonts/Inter-Regular.woff2` | 200 |
| `/assets/fonts/Inter-Medium.woff2` | 200 |
| `/assets/fonts/Inter-SemiBold.woff2` | 200 |
| `/assets/fonts/Inter-Bold.woff2` | 200 |
| `/assets/fonts/Inter-ExtraBold.woff2` | 200 |

`style.min.css` remains **HTML-commented** in `header.twig` — not loaded.

---

## 7. Performance notes

| Check | Status |
|-------|--------|
| Console | **SAFE UNKNOWN** — no automated browser console pass |
| Layout Shift (CLS) | **SAFE UNKNOWN** — preload should reduce swap; operator Ctrl+F5 confirmation recommended |
| Font swap | `font-display: swap` retained per spec; preload mitigates visible FOUT |
| Double `@font-face` load | **PASS** — single `style.css` active |

---

## 8. Documentation updated

| File | Change |
|------|--------|
| `baselines/SITE-002-STABLE-LIVE-LOCAL-FONTS-01.md` | **created** |
| `knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | §1 authority + **§27 Local Fonts 01** |
| `site-passport.md` | checkpoint |
| `README.md` | active checkpoint |
| `../../OCPILOT-STATE.md` | SITE-002 focus |
| `../../OPERATIONAL-INDEX.md` | Run **4.162** |

---

## 9. Git

| Item | Value |
|------|--------|
| Pre-work checkpoint | `13c7e6ed` |
| Branch | `mars/canonical-post-recovery` |
| Production | **NOT touched** |

---

## 10. Operator follow-up

Recommended HITL: Ctrl+F5 on Home, Catalog, PDP — confirm no visible font switch. Automated HTTP pass cannot replace operator visual confirmation for FOUT.
