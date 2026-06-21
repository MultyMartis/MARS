# REPORT — PDP MOBILE PASS V1

**Project:** SITE-002 (ZPM TEST)  
**Environment:** https://zpm.new-site.space/  
**Baseline rollback:** `SITE-002-STABLE-PDP-V4-2026-06-10`  
**Reference SKU:** SPKB-18/7-ВЛ5  
**Reference URL:** https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850  
**Deployed at (UTC):** 2026-06-09T20:05:16  
**Git:** Commit NO · Push NO

---

## 1. Changed files

| File | Action |
|------|--------|
| `projects/ocpilot/sites/site-002/mobile-pass-v1-work/style.css` | Mobile media queries appended (work copy + live deploy) |
| `projects/ocpilot/sites/site-002/mobile-pass-v1-work/mobile-pass-v1-deploy.py` | FTP deploy script |
| `projects/ocpilot/sites/site-002/mobile-pass-v1-work/mobile-pass-v1-qa.py` | Automated QA |
| `projects/ocpilot/sites/site-002/mobile-pass-v1-work/mobile-pass-v1-screenshot.py` | Screenshot capture |
| `projects/ocpilot/sites/site-002/mobile-pass-v1-work/mobile-pass-v1-qa-result.json` | QA evidence |
| `projects/ocpilot/sites/site-002/backups/style.css.pre-mobile-pass-v1.bak` | Pre-deploy rollback copy (= V4 baseline CSS) |
| `projects/ocpilot/sites/site-002/backups/mobile-pass-v1-deploy-manifest-20260609-200516.json` | Deploy manifest |
| `projects/ocpilot/sites/site-002/qa/mobile-pass-v1/*.png` | Screenshots (10 full-page + 10 hero) |
| `projects/ocpilot/sites/site-002/reports/SITE-002-PDP-MOBILE-PASS-V1.md` | This report |

**Live remote changed:** `assets/css/style.css` only  
**Twig / PHP / JS:** not changed

---

## 2. What changed

Added block **`SITE-002 — PDP MOBILE PASS V1`** at end of `style.css`. Desktop/laptop rules untouched. Only `@media` additions.

### Hero (≤768px)

- Preserved existing V4 mobile stack via `display: contents` + order (identity → media → commerce → specs) at 1024px
- Identity column stacks title/article above wishlist/compare controls
- Gallery image: `min-height` 280px, `max-height` 420px, `object-fit: contain` — not thumbnail-sized
- Commerce/service cards full width; `btn-Question` width 100%
- **Primary specs:** `grid-template-columns: repeat(2, minmax(0, 1fr))` — 2×2 grid
- **Secondary specs:** `overflow-wrap`, flex-wrap, min-width fixes for long values
- Title max-width 100%

### Product content (≤768px)

- Existing V4 stack preserved: specs → documents → product-help (order 1/2/3 at 1024px)
- Spec table rows wrap; long values break correctly
- Documents: reduced padding, note block padding-left removed, title wrap
- **Product-help:** single column — text/button top, illustration bottom (`order: 1/2`)

### Related products

- Image heights tuned per breakpoint (768→380px … 360→260px) — cards stay in container, slider logic unchanged

### Overflow

- `overflow-x: clip` on hero/content/related/help sections
- `document.body.scrollWidth ≤ viewport` verified at all test widths

### Breakpoint refinements

Additional tuning at **576**, **390**, **375**, **360** for gallery heights, doc icon sizes, primary spec gaps.

---

## 3. SHA256

| Artifact | SHA256 |
|----------|--------|
| V4 rollback (`style.css.pre-mobile-pass-v1.bak`) | `084c402af786bd817c46657d56dcc085cf7706174db3e62dd6638d2a111c83b2` |
| Deployed mobile pass CSS | `9ae7ac39174394fee130a177c09179bd00df9eb47fe099bda5267922e27d95a1` |

---

## 4. Screenshots

Directory: `projects/ocpilot/sites/site-002/qa/mobile-pass-v1/`

| Viewport | Full page | Hero |
|----------|-----------|------|
| 768 | `spkb-pdp-768.png` | `spkb-hero-768.png` |
| 576 | `spkb-pdp-576.png` | `spkb-hero-576.png` |
| 390 | `spkb-pdp-390.png` | `spkb-hero-390.png` |
| 375 | `spkb-pdp-375.png` | `spkb-hero-375.png` |
| 360 | `spkb-pdp-360.png` | `spkb-hero-360.png` |

---

## 5. QA table

| # | Check | 768 | 576 | 390 | 375 | 360 | Notes |
|---|-------|-----|-----|-----|-----|-----|-------|
| 1 | Hero order (title → photo → price → help → specs) | PASS | PASS | PASS | PASS | PASS | commerce & service above specs |
| 2 | Price card visible before specs | PASS | PASS | PASS | PASS | PASS | |
| 3 | Cart / qty hooks present | PASS | PASS | PASS | PASS | PASS | static DOM |
| 4 | Qty controls | PASS | PASS | PASS | PASS | PASS | not interactively tested |
| 5 | Wishlist | PASS | PASS | PASS | PASS | PASS | in identity block |
| 6 | Compare | PASS | PASS | PASS | PASS | PASS | in identity block |
| 7 | Gallery / Fancybox hooks | PASS | PASS | PASS | PASS | PASS | not interactively tested |
| 8 | Documents (list, PDF icons, download, mini-CTA) | PASS | PASS | PASS | PASS | PASS | docs-list logic unchanged |
| 9 | CTA forms hooks | PASS | PASS | PASS | PASS | PASS | `#zpmFbQuestion` preserved |
| 10 | Related products visible | PASS | PASS | PASS | PASS | PASS | |
| 11 | Footer visible | PASS | PASS | PASS | PASS | PASS | |
| 12 | No horizontal overflow (`scrollWidth ≤ viewport`) | PASS | PASS | PASS | PASS | PASS | |
| 13 | Primary specs 2×2 grid | PASS | PASS | PASS | PASS | PASS | computed columns 2×2 |
| 14 | Content order: specs → docs → help | PASS | PASS | PASS | PASS | PASS | |
| 15 | Product-help stack (text top, visual bottom) | PASS | PASS | PASS | PASS | PASS | single column grid |
| 16 | PHP/Twig errors absent | PASS | — | — | — | — | static |
| 17 | Live CSS contains MOBILE PASS V1 block | PASS | — | — | — | — | static |

**Overall:** PASS (`mobile-pass-v1-qa-result.json`)

---

## 6. Rollback

To revert to **SITE-002-STABLE-PDP-V4-2026-06-10**:

1. Upload `projects/ocpilot/sites/site-002/backups/style.css.pre-mobile-pass-v1.bak` → remote `assets/css/style.css`
2. Clear `system/storage/cache/template/` on FTP
3. Verify SHA256 on live CSS = `084c402af786bd817c46657d56dcc085cf7706174db3e62dd6638d2a111c83b2`
4. Full V4 rollback (all 6 files): see `reports/SITE-002-STABLE-PDP-V4-2026-06-10.md` §6

---

## 7. Constraints confirmed

- Business logic: unchanged  
- Twig conditions: unchanged  
- JS cart / gallery / documents / forms: unchanged  
- New visual styles: none — only responsive layout/spacing/sizing via existing tokens  
- Desktop/laptop: unchanged (new rules only inside mobile `@media`)

---

*Generated after deploy + automated QA + screenshots. Interactive cart/gallery/fancybox clicks not exercised in automation.*
