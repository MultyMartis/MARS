# REPORT — PDP CONTENT STRUCTURE REBUILD

**Site:** SITE-002 (ЗПМ TEST)  
**Environment:** https://zpm.new-site.space/  
**Date:** 2026-06-09  
**Scope:** `catalog/view/theme/default/template/product/producttabs.twig` only  
**Baseline:** `SITE-002-STABLE-PDP-V2-2026-06-09`

---

## 1. Backup path

| Role | Path |
|------|------|
| Pre-change rollback | `projects/ocpilot/sites/site-002/backups/producttabs.twig.pre-content-rebuild.bak` |
| Deploy manifest | `projects/ocpilot/sites/site-002/backups/content-rebuild-deploy-manifest-20260609-154211.json` |
| Local work copy | `projects/ocpilot/sites/site-002/content-rebuild-work/producttabs.twig` |

**SHA256**

| Version | SHA256 |
|---------|--------|
| Pre-change (rollback) | `4cfcec354486e6c8d9f8322bc0e071b465b1fda42c618f835a84e80171586110` |
| Deployed | `c9a02099c8dfbfc4d46f8a83a53ae71ea1b337b0059eaaf8e2405ba14cd2ea7b` |

---

## 2. Twig blocks changed

**File:** `catalog/view/theme/default/template/product/producttabs.twig` (live TEST FTP)

| Before | After |
|--------|-------|
| `<section class="product-tabs">` + tab UI (`.js-tabs`, `.tabs__head`, `.tabs__panel`) | `<section class="product-content">` — flat scroll sections |
| Fixed tab panels: desc / spec / docs always in DOM | Conditional sections per data availability |
| Specs only inside hidden tab panel | Specs always in `product-content__specifications` |
| Docs tab panel always present (empty `<ul>` when no docs) | Docs block omitted when `documents` empty |
| `product-help` consultation block | Unchanged (same markup, same position) |

**New structural blocks**

```
product-content
├── product-content__description          (optional)
├── product-content__specs-docs           (only when documents exist)
│   ├── product-content__specifications
│   └── product-content__documents
├── product-content__specifications       (standalone when no documents)
└── product-help                          (unchanged)
```

**Related products:** remain in `product.twig` as `{{ relproducts }}` — not moved.

---

## 3. Conditional logic

| Rule | Twig condition | Render behaviour |
|------|----------------|------------------|
| R1 — Description optional | `{% if description\|striptags\|trim %}` | Section omitted when CMS description empty or whitespace/HTML-only |
| R2 — Specs mandatory | Always rendered in `product-content__specifications` | Main info block; empty `spec-table` if no `attribute_groups` |
| R3 — Documents optional | `{% if documents %}` | Documents block omitted when array empty |
| R4 — Docs present | `{% if documents %}` → wrapper `product-content__specs-docs` | Specs + docs as sibling sections |
| R5 — Docs absent | `{% else %}` branch | Standalone `product-content__specifications` only; no docs wrapper/column |
| R6 — Consultation + related | Unchanged / external | `product-help` preserved; `rel-products` from `relproducts.twig` |

**Reused inner markup (no redesign):** `.content`, `.spec-table` / `.spec-table__row`, `.docs-list` / `.docs-list__link`, `.product-help` tree.

---

## 4. Tested URLs

### Live QA — PASS

| Case | URL | Result |
|------|-----|--------|
| **A** — desc + docs | https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850 | PASS |
| **C** — no desc + docs | https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-svarnye-premium/vanna-moechnaya-vms-p-2-600-1400h700h850 | PASS |

**Checks (both URLs):** no PHP/Twig errors · no tab UI · specs visible · consultation visible · related (`rel-products`) visible · no empty description wrapper (Case C) · documents list non-empty when present.

### Live QA — not found in catalog

| Case | Status | Notes |
|------|--------|-------|
| **B** — desc + no docs | **Not found** | BFS scan of 557+ PDP URLs: every product had category-level documents → always `product-content__specs-docs` wrapper |
| **D** — no desc + no docs | **Not found** | Same scan: no SKU without both description and documents |

**Template branches for B/D:** verified in Twig source (`{% else %}` standalone specs path; description guard). Live HTML verification pending a suitable SKU in admin/catalog.

**QA artifact:** `projects/ocpilot/sites/site-002/content-rebuild-work/content-rebuild-qa-result.json`

---

## 5. Render state matrix

| Case | Description | Documents | DOM structure | Live verified |
|------|-------------|-----------|---------------|---------------|
| A | yes | yes | description → specs-docs(specs + docs) → help → related | **yes** (SPKB) |
| B | yes | no | description → standalone specs → help → related | Twig only |
| C | no | yes | specs-docs(specs + docs) → help → related | **yes** (VMS-P-2-600) |
| D | no | no | standalone specs → help → related | Twig only |

---

## 6. Rollback procedure

1. Upload `projects/ocpilot/sites/site-002/backups/producttabs.twig.pre-content-rebuild.bak` → `catalog/view/theme/default/template/product/producttabs.twig` on TEST FTP (`polygonws.beget.tech`).
2. Clear `system/storage/cache/template/`.
3. Hard-refresh PDP — tab UI (Описание / Характеристики / Документы) should return.
4. Optional full PDP V2 rollback: see `reports/SITE-002-STABLE-PDP-V2-2026-06-09.md` §5.

---

## 7. Files touched

| Path | Action |
|------|--------|
| `catalog/view/theme/default/template/product/producttabs.twig` | **Deployed** (live TEST) |
| `projects/ocpilot/sites/site-002/backups/producttabs.twig.pre-content-rebuild.bak` | Created |
| `projects/ocpilot/sites/site-002/content-rebuild-work/*` | Local work + QA scripts |
| `projects/ocpilot/sites/site-002/reports/SITE-002-PDP-CONTENT-STRUCTURE-REBUILD.md` | This report |

**Not touched:** `producthero.twig`, `style.css`, `product.php`, `config.php`, `header.twig`, JS, OCMOD, DB.

---

## 8. Git

**Commit:** NO  
**Push:** NO

---

## 9. UNKNOWN / notes

- **Cases B & D:** no representative SKU on TEST storefront at scan time; conditional Twig paths are in place but not live-verified.
- **Styling:** `product-content` / `product-content__*` classes have no CSS yet — expected; next wave is design/CSS only.
- **Deploy scripts** under `content-rebuild-work/` contain FTP credentials (local-only pattern, same as prior waves).
