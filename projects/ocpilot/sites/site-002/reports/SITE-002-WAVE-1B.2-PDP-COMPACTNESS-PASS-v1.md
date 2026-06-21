# REPORT — WAVE 1B.2 PDP COMPACTNESS PASS

**Site:** SITE-002 (TEST) — https://zpm.new-site.space/  
**Wave:** 1B.2 — compactness pass only (CSS-only)  
**Deployed:** 2026-06-08 UTC (manifest `w1b2-deploy-manifest-20260608-222135.json`)

---

## 1. Backup paths

| File | Rollback backup |
|------|-----------------|
| `producthero.twig` | `projects/ocpilot/sites/site-002/backups/producthero.twig.pre-w1b2.bak` |
| `producttabs.twig` | `projects/ocpilot/sites/site-002/backups/producttabs.twig.pre-w1b2.bak` |
| `style.css` | `projects/ocpilot/sites/site-002/backups/style.css.pre-w1b2.bak` |

Timestamped live snapshots (pre-deploy FTP pull):  
`projects/ocpilot/sites/site-002/backups/*.{20260608-222135.bak}`

Work copy: `projects/ocpilot/sites/site-002/w1b2-work/`

---

## 2. Changed files

| File | Change |
|------|--------|
| `assets/css/style.css` | **Modified** — hero, buy box, scroll sections, specs, documents compactness |
| `catalog/view/theme/default/template/product/producthero.twig` | Unchanged (re-deployed as-is) |
| `catalog/view/theme/default/template/product/producttabs.twig` | Unchanged (re-deployed as-is) |

Supporting scripts (local only, not deployed):  
`w1b2-work/w1b2-deploy.py`, `w1b2-screenshot.py`, `w1b2-measure.py`, `w1b2-interaction-qa.py`

---

## 3. What was compacted

### Task 1 — Hero compactness
- Outer hero top padding: `70px` → `40px`
- Layout gap/padding: `30px` → `20px`; `align-items: stretch` → `start`
- Removed vertical stretch (`min-height: 100%`, `grid-template-rows: 1fr`) on desktop fit layout
- Identity column gap tightened; title `40/44px` → `36/40px` (mobile `30/36px`)
- Brand logo cap `32px` → `28px`
- Gallery: content-based height, hero main image `max-height: 340px`, thumb slide padding reduced
- Attribute grid cells: `min-height 72px` → `56px`, tighter padding/gap

### Task 2 — Buy box compactness
- Inner padding `30px` → `20px`; lighter shadow
- Status / price / fav-compare divider spacing halved (`30px` → `10px`)
- Price value `28/34px` → `26/32px` (still prominent)

### Task 3 — Section spacing
- Tabs top padding `70px` → `40px`
- Section stack gap `70px` → `30px`
- Section body padding `30px` → `20px`; internal gap reduced

### Task 4 — Full specs compactness
- Spec table row gap `20px` → `10px` inside PDP section
- Row vertical padding `6px 0` added for readable but tighter rows

### Task 5 — Documents compactness
- PDF card `min-height 280px` → `160px`
- Icon pseudo-element `70×70px` → `64×64px`
- Card padding/gap reduced

**Not touched:** cart/qty/wishlist/compare hooks, fancybox attributes, document links, controllers, JS, HTML structure.

---

## 4. Before / after measurements

Test URL: [Стол производственный СП-П-18/6](https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850)

| Metric | Desktop before | Desktop after | Δ | Mobile before | Mobile after | Δ |
|--------|---------------:|--------------:|--:|--------------:|-------------:|--:|
| **Page height** | 5237 px | 4769 px | **−468 (−8.9%)** | 7386 px | 7073 px | **−313 (−4.2%)** |
| **Hero height** | 825 px | 603 px | **−222 (−26.9%)** | 1610 px | 1293 px | **−317 (−19.7%)** |
| **Buy box height** | 527 px | 385 px | **−142 (−26.9%)** | 481 px | 339 px | **−142 (−29.5%)** |
| **Sections block** | 1763 px | 1547 px | **−216 (−12.3%)** | 1859 px | 1873 px | +14 |
| **Docs section** | 409 px | 267 px | **−142 (−34.7%)** | 387 px | 245 px | **−142 (−36.7%)** |
| **Docs PDF card** | 280 px | 160 px | **−120 (−42.9%)** | 280 px | 160 px | **−120 (−42.9%)** |
| **Media width %** | 24% | 24% | 0 | 74% | 79% | +5 |

Raw JSON:  
`projects/ocpilot/sites/site-002/qa/w1b2-screenshots/measurements-pre-w1b2.json`  
`projects/ocpilot/sites/site-002/qa/w1b2-screenshots/measurements-post-w1b2.json`

---

## 5. Screenshots

**Before (W1B.1):** `projects/ocpilot/sites/site-002/qa/w1b2-screenshots/pre-w1b2-*.png`

**After (W1B.2):** `projects/ocpilot/sites/site-002/qa/w1b2-screenshots/post-w1b2-*.png`

| Shot | File |
|------|------|
| Desktop hero | `pre-w1b2-desktop-hero-full.png` → `post-w1b2-desktop-hero-full.png` |
| Desktop sections | `pre-w1b2-desktop-sections-full.png` → `post-w1b2-desktop-sections-full.png` |
| Desktop full page | — → `post-w1b2-desktop-page-full.png` |
| Mobile hero | `pre-w1b2-mobile-hero-full.png` → `post-w1b2-mobile-hero-full.png` |
| Mobile sections | `pre-w1b2-mobile-sections-full.png` → `post-w1b2-mobile-sections-full.png` |

---

## 6. QA results

### Layout / visual
| Check | Desktop | Mobile |
|-------|---------|--------|
| Hero more compact | ✅ −223 px | ✅ −317 px |
| Buy box more compact | ✅ −142 px | ✅ −142 px |
| Sections closer | ✅ −216 px block | ⚠️ +14 px (description length variance; spacing rules applied) |
| Specs readable, 2-col hero attrs | ✅ | ✅ |
| Documents compact | ✅ card −120 px | ✅ |
| No horizontal overflow | ✅ | ✅ |
| Image early on mobile | ✅ (identity → media order preserved) | ✅ |
| CTA touch-usable | ✅ | ✅ |

### Functional (automated)
| Check | Result |
|-------|--------|
| Cart add → qty visible | ✅ |
| Qty + increment | ✅ |
| Wishlist toggle | ✅ |
| Compare toggle | ✅ |
| Gallery fancybox hook | ✅ `data-fancybox="product"` |
| Document PDF href | ✅ |
| No JS errors | ✅ |
| Section order (Описание → Полные характеристики → Документы) | ✅ |
| Hero attrs duplicated in full specs | ✅ |

---

## 7. Rollback instructions

1. Upload rollback backups to FTP (`polygonws.beget.tech`, user `polygonws_zpm`):
   - `backups/producthero.twig.pre-w1b2.bak` → `catalog/view/theme/default/template/product/producthero.twig`
   - `backups/producttabs.twig.pre-w1b2.bak` → `catalog/view/theme/default/template/product/producttabs.twig`
   - `backups/style.css.pre-w1b2.bak` → `assets/css/style.css`
2. Clear OpenCart template cache: `system/storage/cache/template/`
3. Hard-refresh browser / bust CSS cache if needed.

Or run: `py projects/ocpilot/sites/site-002/w1b2-work/w1b2-deploy.py` with rollback files copied into `w1b2-work/` from `.pre-w1b2.bak` sources.

---

## 8. Remaining visual issues

1. **Measured media column width ~24%** — grid allocation remains `28fr` (≥25%), but outer padding/gaps reduce rendered width slightly; unchanged from W1B.1 baseline.
2. **Mobile sections total height** — slightly taller (+14 px) due to content flow; section *gaps* are tighter but description block height dominates.
3. **Hero gallery max-height 340px** — on very tall product images, media may feel capped; acceptable for B2B compactness but worth eyeballing other SKUs with different aspect ratios.
4. **`product-help` block** below sections unchanged (out of scope) — still contributes significant page height below fold.
5. **Subtitle placeholder** — template still contains placeholder string guard; no subtitle shown on test SKU (expected).

---

## Git

**Commit:** NO  
**Push:** NO

## Security

FTP credentials used locally in deploy script only; not committed. No credentials in this report.
