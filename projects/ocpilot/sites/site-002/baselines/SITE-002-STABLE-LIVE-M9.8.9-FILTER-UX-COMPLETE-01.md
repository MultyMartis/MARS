# SITE-002 — Stable Live M9.8.9 Filter UX Complete Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Registered at:** 2026-06-19 (operator-requested stable checkpoint after filter recovery + filter UX polish complete)  
**Mode:** Metadata-only registration — **no FTP**, **no deploy**, **no file capture**

---

## 1. Authority state

`SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01`

**Current Authority State:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01`

**Supersedes:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`

---

## 2. Current source of truth

| Priority | Source | Notes |
|----------|--------|-------|
| **1** | **Live TEST** — https://zpm.new-site.space/ | Authoritative storefront state |
| **2** | **Full Beget backup** | Operator attestation — disaster recovery |
| **3** | **Manual UI refinements** | **CANONICAL** |
| **4** | **Manual CSS refinements** | **CANONICAL** |
| **5** | **Manual Twig refinements** | **CANONICAL** |
| **6** | **Manual JS refinements** | **CANONICAL** — incl. operator offset tuning (04A/04B) |
| **7** | **Technical Knowledge Map** | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) |

Prior repo baselines, work copies (`*-work/`), `backups/stable-*` folders, and pre-pass `.bak` files are **historical** unless refreshed by live capture.

**Do not** use `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01` as current authority — superseded by this checkpoint.

---

## 3. Registration context

This checkpoint supersedes `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01` and records the state after:

1. Filter recovery wave (06D–06M) — carried forward from prior checkpoint
2. Filter UX polish wave (04, 04A, 04B, 07, 08, 08A)
3. Other UX: M9.8.9-01 Wishlist / Compare Smart Tooltips

---

## 4. Completed work (registered)

### Filter recovery (carried forward)

| Pass | Status on live |
|------|----------------|
| **M9.8.9-06D — Category 301 Price Index Rebuild** | **active** |
| **M9.8.9-06F — 1C Price Index Hook** | **active** — `refreshPriceIndex()` in offers import |
| **M9.8.9-06H — Exclude Zero Price From Range** | **active** |
| **M9.8.9-06J — Numeric Attribute Filter Fix** | **active** |
| **M9.8.9-06M — Effective Price Hotfix** | **active** |

### Filter UX

| Pass | Status on live |
|------|----------------|
| **M9.8.9-07 — Hide Subcategories Filter Block** | **active** — UI-only Twig gate; backend intact |
| **M9.8.9-04 — Filter Scroll Logic** | **active** — `scrollToCategorySection()` after AJAX |
| **M9.8.9-04A — Operator offset tuning** | **deployed** — superseded on live by 04B |
| **M9.8.9-04B — Operator manual JS refinements** | **canonical** — scroll offset **0** |
| **M9.8.9-08 — Filter Group Reset** | **active** — per-attribute-group reset |
| **M9.8.9-08A — Filter Group Reset UX Polish** | **active** — reset under options; disabled/active states |

### Other UX

| Pass | Status on live |
|------|----------------|
| **M9.8.9-01 — Wishlist / Compare Smart Tooltips** | **active** — context-aware tip text |

### M9.8 UX (carried forward)

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
| Authority | **`SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01`** |
| Active products (post-import) | **~594** |
| Price index coverage (cg=2) | **100%** (594/594 per 06K forensic) |
| Live business-logic files | `product.php` · `import_1C_offers.php` · `filterssidebar.twig` · `main.js` · `style.css` |
| Filters | **working** — recovery + UX polish complete on tested branches |
| Filter sidebar | Subcategories block **hidden** (07); group reset **active** (08/08A) |
| Filter AJAX scroll | **active** — offset **0** (04B canonical) |
| PDP Gallery / Lightbox | **active** (M9.8.1 / M9.8.2) |
| Products per page | **active** (10 / 20 / 50 / 100) |
| Knowledge map | [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) |
| Live truth | **hosting state on `zpm.new-site.space`** |

---

## 6. Pass evidence (repo references)

### Filter recovery

| Pass | Evidence |
|------|----------|
| 06D | [SITE-002-M9.8.9-06D-CATEGORY-301-PRICE-INDEX-REBUILD.md](../reports/SITE-002-M9.8.9-06D-CATEGORY-301-PRICE-INDEX-REBUILD.md) |
| 06F | [SITE-002-M9.8.9-06F-IMPLEMENTATION-PASS.md](../reports/SITE-002-M9.8.9-06F-IMPLEMENTATION-PASS.md) |
| 06H | [SITE-002-M9.8.9-06H-PRICE-RANGE-EXCLUDE-ZERO-HOTFIX.md](../reports/SITE-002-M9.8.9-06H-PRICE-RANGE-EXCLUDE-ZERO-HOTFIX.md) |
| 06J | [SITE-002-M9.8.9-06J-NUMERIC-ATTRIBUTE-FILTER-HOTFIX.md](../reports/SITE-002-M9.8.9-06J-NUMERIC-ATTRIBUTE-FILTER-HOTFIX.md) |
| 06M | [SITE-002-M9.8.9-06M-EFFECTIVE-PRICE-HOTFIX.md](../reports/SITE-002-M9.8.9-06M-EFFECTIVE-PRICE-HOTFIX.md) |

### Filter UX

| Pass | Evidence |
|------|----------|
| 07 | [SITE-002-M9.8.9-07-REMOVE-SUBCATEGORIES-FILTER-BLOCK.md](../reports/SITE-002-M9.8.9-07-REMOVE-SUBCATEGORIES-FILTER-BLOCK.md) |
| 04 | [SITE-002-M9.8.9-04-FILTER-SCROLL-OFFSET-FIX.md](../reports/SITE-002-M9.8.9-04-FILTER-SCROLL-OFFSET-FIX.md) |
| 04A | [SITE-002-M9.8.9-04A-FILTER-SCROLL-OFFSET-TUNING.md](../reports/SITE-002-M9.8.9-04A-FILTER-SCROLL-OFFSET-TUNING.md) |
| 04B | [SITE-002-M9.8.9-04B-OPERATOR-MANUAL-JS-POLISH-REGISTRATION.md](../reports/SITE-002-M9.8.9-04B-OPERATOR-MANUAL-JS-POLISH-REGISTRATION.md) |
| 08 | [SITE-002-M9.8.9-08-FILTER-GROUP-RESET-IMPLEMENTATION.md](../reports/SITE-002-M9.8.9-08-FILTER-GROUP-RESET-IMPLEMENTATION.md) |
| 08A | [SITE-002-M9.8.9-08A-FILTER-GROUP-RESET-POSITION-POLISH.md](../reports/SITE-002-M9.8.9-08A-FILTER-GROUP-RESET-POSITION-POLISH.md) |

### Other UX

| Pass | Evidence |
|------|----------|
| 01 | [SITE-002-M9.8.9-01-WISHLIST-COMPARE-SMART-TOOLTIPS.md](../reports/SITE-002-M9.8.9-01-WISHLIST-COMPARE-SMART-TOOLTIPS.md) |

### Prior checkpoint

| Pass | Evidence |
|------|----------|
| Filter Recovery baseline | [SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md](SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md) |

This checkpoint does **not** re-verify live files — operator attestation + pass QA artifacts only.

---

## 7. Known open items (not blocking this checkpoint)

| Item | Status |
|------|--------|
| **EC-01** — filter sidebar empty subcategories on branch 80 | **resolved by policy** — subcategories block hidden (07); M9.8.7 deferred |
| Зонты `attr[construction][]` — 0 results | **data gap** — 1 SKU, missing attribute data |
| M9.8.3/4/6/8 deferred UX passes | **not authorized** |
| **M10** | **not authorized** |

---

## 8. Rollback source

1. **Beget full backup** — full hosting restore
2. **Current live TEST state** — https://zpm.new-site.space/
3. **File-level backups** — `backups/*.pre-m9.8.9-*` (01, 04a, 07, 08, 08a, 06*)
4. **Prior repo STABLE folders** — historical

---

## 9. Rule before next tasks

Before any next SITE-002 change:

1. Read [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)
2. Read this checkpoint (latest stable)
3. Verify **Authority State** = `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01`
4. For filter / catalog / 1C / price / PLP tasks — follow Knowledge Map **PRE-TASK RULE** (domain-specific)
5. Check **Active Roadmap Stage** in [BZPM-PRODUCT-ROADMAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md)

See [SITE-002-WORKING-RULES.md](../SITE-002-WORKING-RULES.md).

---

## Status

| Field | Value |
|-------|--------|
| Checkpoint type | **STABLE LIVE CHECKPOINT** (metadata-only) |
| Supersedes (live truth) | `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01` |
| Knowledge map | [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) |
| Rollback source | **Beget full backup + current live TEST + file-level pass backups** |
| Deploy | **NO** (this registration) |
| FTP changes | **NO** (this registration) |

---

*Documentation only — no runtime claimed.*
