# SITE-002 — Stable Live M9.8.9 Filter Recovery Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Registered at:** 2026-06-19 (operator-requested stable checkpoint after product reset, fresh 1C import, filter recovery hotfixes)  
**Mode:** Metadata-only registration — **no FTP**, **no deploy**, **no file capture**

---

## 1. Authority state

`SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`

**Current Authority State:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`

---

## 2. Current source of truth

| Priority | Source | Notes |
|----------|--------|-------|
| **1** | **Live TEST** — https://zpm.new-site.space/ | Authoritative storefront state |
| **2** | **Full Beget backup** | Operator attestation — backup confirmed before product reset |
| **3** | **Manual UI refinements** | **CANONICAL** |
| **4** | **Manual CSS refinements** | **CANONICAL** |
| **5** | **Manual Twig refinements** | **CANONICAL** |
| **6** | **Technical Knowledge Map** | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — persistent architecture reference |

Prior repo baselines, work copies (`*-work/`), `backups/stable-*` folders, and pre-pass `.bak` files are **historical** and must **not** be treated as current live state without a fresh live capture.

**Do not** use `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` as current authority — superseded by this checkpoint.

---

## 3. Registration context

This checkpoint supersedes `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` for **current live truth** and records the post-recovery state after:

1. Clean product reset (DB product tables cleared)
2. Fresh 1C import (`import0_1.xml` → `offers0_1.xml`)
3. Price index recovery (06D rebuild + 06F hook)
4. Filter hotfixes (06H, 06J, 06M)

---

## 4. Completed work (registered)

### Catalog / data recovery

| Pass | Status on live |
|------|----------------|
| **Clean Product Reset** | **complete** — 27 932 product-owned rows deleted; categories/attributes preserved |
| **Fresh 1C Import** | **complete** — ~594 active products post-import (operator sequence) |
| **Price Index Recovery** | **complete** — 06D subtree rebuild + 06F offers hook deployed |

### Filter / price hotfixes (live PHP)

| Pass | Status on live |
|------|----------------|
| **M9.8.9-06H — Price Range Exclude Zero** | **active** — `getCategoryPriceRange()` excludes `effective_price <= 0` |
| **M9.8.9-06J — Numeric Attribute Filter** | **active** — `attr[51][]` / numeric keys resolve via `attribute_id` |
| **M9.8.9-06M — Effective Price Hotfix** | **active** — `IF(special > 0, special, price)` in filter/sort/count |
| **Working Filters** | **active** — attribute + price filters operational on tested branches |
| **Working Only With Price** | **active** — `only_with_price=1` returns priced SKUs |
| **Working Price Sort** | **active** — `sort=p.price` ASC/DESC monotonic on tested branches |

### M9.8 UX (carried forward from prior checkpoint)

| Pass | Status on live |
|------|----------------|
| **M9.8.1 — PDP Gallery Compact** | **active** |
| **M9.8.2 — PDP Lightbox Constraints** | **active** |
| **M9.8.5 — Products Per Page Selector** | **active** |

### Operator manual refinements (CANONICAL)

| Pass | Status on live |
|------|----------------|
| **PLP Grid Density Pass** | **active** |
| **PLP Compact Pass** | **active** |
| **Filter Compact Pass** | **active** |
| **Breakpoint Polish Pass** | **active** |
| **Manual CSS Refinement Pass** | **active** |
| **Manual Twig Refinement Pass** | **active** |
| **Operator Manual UI Polish** | **active** |

---

## 5. Active stable state summary

| Item | Value |
|------|--------|
| Authority | **`SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`** |
| Active products (post-import, per 06K forensic) | **~594** |
| Price index coverage (post-import, cg=2) | **100%** (594/594 per 06K) |
| Live modified PHP (filter recovery) | `import_1C_offers.php` (06F) · `catalog/model/catalog/product.php` (06H, 06J, 06M) |
| Filters | **working** on Столы, Подтоварники, Тележки, Моечные ванны, Зонты (price); attr filters per branch |
| PDP Gallery / Lightbox | **active** (M9.8.1 / M9.8.2) |
| Products per page | **active** (10 / 20 / 50 / 100) |
| Knowledge map | [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) |
| Live truth | **hosting state on `zpm.new-site.space`** |
| Beget backup | Operator attests **full global backup exists** (pre-reset) |

---

## 6. Pass evidence (repo references — not live verification)

| Pass | Evidence |
|------|----------|
| Product Reset | [SITE-002-PRODUCT-RESET-EXECUTION.md](../reports/SITE-002-PRODUCT-RESET-EXECUTION.md) |
| Price Index Root Cause | [SITE-002-M9.8.9-06C-LIVE-PRICE-INDEX-ROOT-CAUSE.md](../reports/SITE-002-M9.8.9-06C-LIVE-PRICE-INDEX-ROOT-CAUSE.md) |
| Category 301 Reindex | [SITE-002-M9.8.9-06D-CATEGORY-301-PRICE-INDEX-REBUILD.md](../reports/SITE-002-M9.8.9-06D-CATEGORY-301-PRICE-INDEX-REBUILD.md) |
| 1C Price Index Hook | [SITE-002-M9.8.9-06F-IMPLEMENTATION-PASS.md](../reports/SITE-002-M9.8.9-06F-IMPLEMENTATION-PASS.md) |
| Price Range Exclude Zero | [SITE-002-M9.8.9-06H-PRICE-RANGE-EXCLUDE-ZERO-HOTFIX.md](../reports/SITE-002-M9.8.9-06H-PRICE-RANGE-EXCLUDE-ZERO-HOTFIX.md) |
| Numeric Attribute Filter | [SITE-002-M9.8.9-06J-NUMERIC-ATTRIBUTE-FILTER-HOTFIX.md](../reports/SITE-002-M9.8.9-06J-NUMERIC-ATTRIBUTE-FILTER-HOTFIX.md) |
| Effective Price Hotfix | [SITE-002-M9.8.9-06M-EFFECTIVE-PRICE-HOTFIX.md](../reports/SITE-002-M9.8.9-06M-EFFECTIVE-PRICE-HOTFIX.md) |
| Filter Forensic (post-import) | [SITE-002-M9.8.9-06K-FILTER-FORENSIC-AFTER-CLEAN-IMPORT.md](../reports/SITE-002-M9.8.9-06K-FILTER-FORENSIC-AFTER-CLEAN-IMPORT.md) |
| M9.8.1 PDP Gallery | [m9.8.1-pdp-gallery-compact-qa-result.json](../qa/m9.8.1-pdp-gallery-compact/m9.8.1-pdp-gallery-compact-qa-result.json) |
| M9.8.2 PDP Lightbox | [m9.8.2-pdp-lightbox-constraints-qa-result.json](../qa/m9.8.2-pdp-lightbox-constraints/m9.8.2-pdp-lightbox-constraints-qa-result.json) |
| M9.8.5 Products Per Page | [m9.8.5-products-per-page-qa-result.json](../qa/m9.8.5-products-per-page/m9.8.5-products-per-page-qa-result.json) |

This checkpoint does **not** re-verify live files — operator attestation + pass QA artifacts only.

---

## 7. Known open items (not blocking this checkpoint)

| Item | Status |
|------|--------|
| **EC-01** — filter sidebar empty subcategories on branch 80 | **open** — M9.8.7 deferred |
| Зонты `attr[construction][]` — 0 results | **data gap** — 1 SKU, missing attribute data (06K/06M) |
| M9.8.3/4/6/8 deferred UX passes | **not authorized** |
| **M10** | **not authorized** |

---

## 8. Rollback source

Rollback / restore options, in order of scope:

1. **Beget full backup** — full hosting restore (operator-controlled; external to repo)
2. **Current live TEST state** — operator live state on https://zpm.new-site.space/
3. **File-level backups from hotfixes** — `backups/*.pre-m9.8.9-06*` (06F, 06H, 06J, 06M)
4. **Prior repo STABLE folders** — historical; **not** guaranteed to match post-recovery live state

**Rollback source for this checkpoint:** **Beget full backup + current live TEST state + file-level pass backups**.

---

## 9. Rule before next tasks

Before any next SITE-002 change:

1. Read [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)
2. Read this checkpoint (latest stable)
3. Verify **Authority State** = `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`
4. Check **Active Roadmap Stage** in [BZPM-PRODUCT-ROADMAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md)
5. Live-capture only the specific files in scope before deploy

See [SITE-002-WORKING-RULES.md](../SITE-002-WORKING-RULES.md).

---

## Status

| Field | Value |
|-------|--------|
| Checkpoint type | **STABLE LIVE CHECKPOINT** (metadata-only) |
| Supersedes (live truth) | `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` |
| Knowledge map | [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) |
| Rollback source | **Beget full backup + current live TEST + file-level pass backups** |
| Deploy | **NO** (this registration) |
| FTP changes | **NO** (this registration) |

---

*Documentation only — no runtime claimed.*
