# REPORT — SITE-002 STABLE CHECKPOINT AND KNOWLEDGE MAP

**Project:** SITE-002 (ЗПМ / BZPM)  
**Date:** 2026-06-19  
**Prior authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Mode:** Documentation-only registration — no FTP, no deploy

---

## 1. New Authority State

| Field | Value |
|-------|--------|
| **Authority** | `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01` |
| **Supersedes** | `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` |
| **Environment** | TEST — https://zpm.new-site.space/ |
| **Manual UI policy** | **CANONICAL** — operator CSS/Twig/UX edits on live TEST |

---

## 2. Checkpoint Registered

**File:** [baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md](../baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md)

**Registered recovery scope:**

| Item | Status |
|------|--------|
| Clean Product Reset | complete |
| Fresh 1C Import | complete (~594 active products) |
| Price Index Recovery | complete (06D rebuild + 06F hook) |
| Numeric Attribute Fix | complete (06J) |
| Effective Price Hotfix | complete (06M) |
| Working Filters | active |
| Working Only With Price | active |
| Working Price Sort | active |
| PDP Gallery Compact (M9.8.1) | active |
| PDP Lightbox Constraints (M9.8.2) | active |
| Products Per Page Selector (M9.8.5) | active |
| Operator Manual UI Polish | active (canonical) |

---

## 3. Knowledge Map Created

**Folder:** `projects/ocpilot/sites/site-002/knowledge/`  
**File:** [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)

**Sections:**

1. Authority Rules  
2. 1C Architecture (`import0_1.xml`, `offers0_1.xml`, cron, `common/cronjob`)  
3. Product Lifecycle (1C → import → oc_product → attributes → SEO → images → offers → price index)  
4. Pricing System (`price`, `price2`, `price3`, `discount1c`, `special`, customer groups)  
5. Price Index System (`oc_product_price_index`, M9.8.9-06D/06F/06H/06M discoveries)  
6. Filter System (profiles, numeric/slug attributes, 06J)  
7. Overlay System (mega menu, mobile menu, search, cart, catalog filter)  
8. PDP Architecture (gallery, lightbox, specs collapse, scroll offset)  
9. Catalog Architecture (products per page, filter profiles, megamenu, PLP layout)  
10. Operational Rules — **PRE-TASK RULE** added

---

## 4. Updated Files

| File | Change |
|------|--------|
| `baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md` | **created** — new stable checkpoint |
| `knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | **created** — technical knowledge map |
| `site-passport.md` | authority, status, recovery scope, knowledge map link |
| `README.md` | authority, folder map (`knowledge/`), PRE-TASK rule |
| `../../OCPILOT-STATE.md` | SITE-002 state, authority, knowledge map |
| `../../OPERATIONAL-INDEX.md` | Run **4.142** registered; 4.140 marked superseded |
| `reports/SITE-002-STABLE-CHECKPOINT-AND-KNOWLEDGE-MAP-REGISTRATION.md` | **created** — this report |

---

## 5. Key Discoveries Preserved

| Discovery | Source | Preserved in |
|-----------|--------|--------------|
| Offers import updated `oc_product.price` but not `oc_product_price_index` | 06C | Knowledge Map §2, §5 |
| Category 301 index coverage was 0.24% (1/419) — collapsed price slider | 06C, 06D | Knowledge Map §5 |
| `refreshPriceIndex` hook added to `import_1C_offers.php` | 06F | Knowledge Map §2, §3 |
| `getCategoryPriceRange()` included zero-price SKUs in min | 06G, 06H | Knowledge Map §5 |
| Numeric `attr[51][]` failed because SQL matched empty `filter_name` | 06I, 06J | Knowledge Map §6 |
| `IFNULL(special, price)` treated `special=0` as effective price 0 | 06K, 06M | Knowledge Map §5 |
| PLP filter uses price index; PDP/cart/checkout do not | 06C | Knowledge Map §5 |
| Sidebar `syncFromRanges()` submits price params with every filter click | 06K | Knowledge Map §6 |
| Overlay hooks: `data-overlay`, `is-catalog-open`, `data-filter-sidebar` | live HTML/CSS | Knowledge Map §7 |

---

## 6. Operational Rules Added

### PRE-TASK RULE (mandatory for all SITE-002 work)

Before any SITE-002 task:

1. Read [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)
2. Read latest Stable Checkpoint — [SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md](../baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md)
3. Verify Authority State
4. Check Active Roadmap Stage — [BZPM-PRODUCT-ROADMAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md)
5. Only then perform audit or changes

---

## Git

| Action | Status |
|--------|--------|
| Commit | per operator request |
| Push | per operator request |
| Message | `site-002: register filter recovery stable checkpoint and technical knowledge map` |

---

## UNKNOWN / SECURITY

| Signal | Detail |
|--------|--------|
| **UNKNOWN** | ocStore exact version |
| **UNKNOWN** | Cart dropdown overlay mechanism (not fully traced) |
| **UNKNOWN** | Production source of `price2`, `price3`, `discount1c` |
| **SECURITY** | No secrets in registration artifacts |

---

*Documentation only — no runtime claimed.*
