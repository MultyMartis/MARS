# REPORT — WAVE 1B PDP SCROLL SECTIONS

**Site ID:** SITE-002 (ЗПМ TEST)  
**Environment:** https://zpm.new-site.space/  
**Wave:** 1B — PDP Tabs → Scroll Sections  
**Date:** 2026-06-09  
**Baseline accepted:** W1A.3 Hero Visual Alignment (Hero **not modified**)

**Sample PDP:**  
https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850

---

## 1. Backup paths

| File | Rollback copy | Timestamped copy |
|------|---------------|------------------|
| `producttabs.twig` | `projects/ocpilot/sites/site-002/backups/producttabs.twig.pre-w1b.bak` | `projects/ocpilot/sites/site-002/backups/producttabs.twig.20260608-220348.bak` |
| `style.css` | `projects/ocpilot/sites/site-002/backups/style.css.pre-w1b.bak` | `projects/ocpilot/sites/site-002/backups/style.css.20260608-220348.bak` |

Deploy manifest: `projects/ocpilot/sites/site-002/backups/w1b-deploy-manifest-20260608-220348.json`

Local work copies: `projects/ocpilot/sites/site-002/w1b-work/producttabs.twig`, `projects/ocpilot/sites/site-002/w1b-work/style.css`

---

## 2. Current tabs architecture (pre-change analysis)

**Template:** `catalog/view/theme/default/template/product/producttabs.twig`  
**Included from:** `product/product.twig` via `{{ producttabs }}` (controller renders partial with full `$data`).

| Zone | Data source | Mechanism |
|------|-------------|-----------|
| Описание | `{{ description }}` | HTML from product CMS field (`html_entity_decode` in controller) |
| Характеристики | `attribute_groups` → nested `ag.attribute` | `getProductAttributes()`; flat row loop (no group headings in UI) |
| Документы | `documents[]` with `name`, `filename`, `type` | Built in controller from product attachments |

**Tabs:** Pure Twig markup + **JS-driven** switching in `assets/js/main.js` — `initTabs()` on `.js-tabs`, toggling `.is-active` on `[data-tab]` buttons and `[data-panel]` panels. CSS hides inactive panels (`display: none`).

**Also available in partial (no controller change needed):** `super_atts[]` — dimensions (L/W/H/weight) plus attributes flagged `SUPER_ATTS` in controller. Already used in hero fit-grid (W1A); reused here for «Ключевые характеристики».

**Untouched:** `product-help` consult block below tabs; hero/gallery/buybox in `producthero.twig`.

---

## 3. Files changed

| Location | Path |
|----------|------|
| **Live (TEST FTP)** | `catalog/view/theme/default/template/product/producttabs.twig` |
| **Live (TEST FTP)** | `assets/css/style.css` |
| **Local work** | `projects/ocpilot/sites/site-002/w1b-work/producttabs.twig` |
| **Local work** | `projects/ocpilot/sites/site-002/w1b-work/style.css` |
| **Local mirror** | `projects/ocpilot/sites/site-002/w1a-work/style.css` (same CSS delta synced) |
| **QA artifacts** | `projects/ocpilot/sites/site-002/w1b-work/w1b-qa.py`, `w1b-screenshot.py`, `w1b-deploy.py` |
| **This report** | `projects/ocpilot/sites/site-002/reports/SITE-002-WAVE-1B-PDP-SCROLL-SECTIONS-v1.md` |

**Not changed:** controllers, models, DB, OCMOD, admin, `producthero.twig`, `product.twig`, `relproducts.twig`, `main.js`.

---

## 4. Before / After structure

### Before

```
[Описание] [Характеристики] [Документы]   ← tab buttons (JS switch)
─────────────────────────────────────────
(one visible panel at a time)
  • description OR flat attribute_groups OR documents
product-help (unchanged)
```

### After

```
Описание
  └ content block (description HTML)

Ключевые характеристики
  └ super_atts (max 12), 2-col grid desktop / 1-col mobile
     fallback: first 10 attributes from attribute_groups if super_atts empty

Полные характеристики
  └ all attribute_groups rows (same data loop as before)

Документы                    ← hidden if documents empty
  └ docs-list (same links/download attrs)

product-help (unchanged)
```

**Key specs data note:** Primary source is existing `super_atts` from controller (dimensions + `SUPER_ATTS`-flagged CMS attributes). No new characteristics invented. Fallback to first 10 CMS attributes documented for products without `super_atts`.

---

## 5. Screenshots — desktop

| File | Description |
|------|-------------|
| `projects/ocpilot/sites/site-002/qa/w1b-screenshots/w1b-desktop-sections-full.png` | Full `.product-tabs` block — all four sections visible, no tab bar |
| `projects/ocpilot/sites/site-002/qa/w1b-screenshots/w1b-desktop-sections-fold.png` | Above-fold viewport (1366×768) |

---

## 6. Screenshots — mobile

| File | Description |
|------|-------------|
| `projects/ocpilot/sites/site-002/qa/w1b-screenshots/w1b-mobile-sections-full.png` | Full sections stack, single-column key specs |
| `projects/ocpilot/sites/site-002/qa/w1b-screenshots/w1b-mobile-sections-fold.png` | Mobile fold (375×667) |

---

## 7. QA results

Automated run: `w1b-work/w1b-qa.py` on sample PDP.

| Check | Desktop | Mobile |
|-------|---------|--------|
| No `.js-tabs` on PDP | PASS | PASS |
| Description section visible | PASS | PASS |
| Key specs section visible | PASS | PASS |
| Full specs section visible | PASS | PASS |
| Documents section (present on sample) | PASS | PASS |
| No horizontal overflow | PASS | PASS |
| Hero untouched (no tabs in hero) | PASS | PASS |
| No JS page errors | PASS | PASS |

**Functional**

| Check | Result |
|-------|--------|
| Section order | Описание → Ключевые характеристики → Полные характеристики → Документы |
| Document link has real `href` | PASS (`documents_present: true`) |
| Tab switching removed | PASS — all content visible by scroll |
| Accordions / show-more / modals for specs | None added |

**Manual:** Document download not exercised in automation (link href verified only).

---

## 8. Rollback instructions

1. Upload `backups/producttabs.twig.pre-w1b.bak` → `catalog/view/theme/default/template/product/producttabs.twig`
2. Upload `backups/style.css.pre-w1b.bak` → `assets/css/style.css`
3. Clear `system/storage/cache/template/` on TEST FTP
4. Hard-refresh PDP in browser

Or run deploy script in rollback mode (upload backups manually via FTP client).

---

## 9. Remaining issues

| Issue | Severity | Notes |
|-------|----------|-------|
| Key specs overlap with full specs | Low | Expected — summary (`super_atts`) duplicates rows also in full list; same as Trapeza-style scan-then-detail |
| Key specs fallback | Info | If `super_atts` empty, first 10 flat attributes used; Twig counter may not increment in older Twig — verify on edge-case SKU |
| Sticky header over long specs | Low | Pre-existing site header behavior when scrolling deep into PDP; not introduced by W1B |
| Template cache | Info | Deploy cleared 0 cache files (dir empty or permissions); Twig change visible immediately on verify |
| `style.min.css` | Info | Live site loads `style.css` (verified W1A baseline); min bundle not updated |

---

## Git

**Commit:** NO  
**Push:** NO

---

## Security

No credentials committed. Deploy scripts with FTP secrets remain local under `w1b-work/` (same pattern as W1A); not added to git staging by this task.
