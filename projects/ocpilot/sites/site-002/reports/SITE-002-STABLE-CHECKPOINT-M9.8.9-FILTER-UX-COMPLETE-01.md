# REPORT — SITE-002 STABLE CHECKPOINT M9.8.9 FILTER UX COMPLETE

**Project:** SITE-002 (ЗПМ / BZPM)  
**Date:** 2026-06-19  
**Prior authority:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`  
**Mode:** Documentation-only registration — no FTP, no deploy

---

## 1. New Authority State

| Field | Value |
|-------|--------|
| **Authority** | `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01` |
| **Supersedes** | `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01` |
| **Environment** | TEST — https://zpm.new-site.space/ |
| **Manual UI policy** | **CANONICAL** — operator CSS/Twig/JS/UX edits on live TEST |

---

## 2. Checkpoint Registered

**File:** [baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md](../baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md)

**Registered scope:**

### Filter recovery

| Pass | Status |
|------|--------|
| M9.8.9-06D Category 301 Price Index Rebuild | active |
| M9.8.9-06F 1C Price Index Hook | active |
| M9.8.9-06H Exclude Zero Price From Range | active |
| M9.8.9-06J Numeric Attribute Filter Fix | active |
| M9.8.9-06M Effective Price Hotfix | active |

### Filter UX

| Pass | Status |
|------|--------|
| M9.8.9-07 Hide Subcategories Filter Block | active |
| M9.8.9-04 Filter Scroll Logic | active |
| M9.8.9-04A Operator offset tuning | deployed; superseded by 04B on live |
| M9.8.9-04B Operator manual JS refinements | canonical |
| M9.8.9-08 Filter Group Reset | active |
| M9.8.9-08A Filter Group Reset UX Polish | active |

### Other UX

| Pass | Status |
|------|--------|
| M9.8.9-01 Wishlist / Compare Smart Tooltips | active |

---

## 3. Knowledge Map Updates

**File:** [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)

**Added sections:**

| Section | Content |
|---------|---------|
| **§7 Filter Architecture** | Sidebar, AJAX flow, `syncChoiceClasses()`, `updateBrowserUrl()`, `updateProducts()`, group reset, global reset, numeric attributes, effective price, price index dependency, hidden subcategories policy |
| **§8 Live Files With Business Logic** | `product.php`, `import_1C_offers.php`, `filterssidebar.twig`, `main.js`, `style.css` — role per file |
| **PRE-TASK RULE UPDATE** | Domain-specific rule for filter / catalog / 1C / price / PLP tasks |

**Updated:** authority references throughout; evidence cutoff; §13 Operational Rules.

---

## 4. Updated Files

| File | Change |
|------|--------|
| `baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md` | **created** — new stable checkpoint |
| `knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | Filter Architecture, Live Files, PRE-TASK rule, authority |
| `site-passport.md` | authority, status, completed passes |
| `README.md` | authority, active checkpoint table |
| `../../OCPILOT-STATE.md` | SITE-002 state, authority |
| `../../OPERATIONAL-INDEX.md` | Run **4.143** registered; 4.142 marked superseded |
| `reports/SITE-002-STABLE-CHECKPOINT-M9.8.9-FILTER-UX-COMPLETE-01.md` | **created** — this report |

---

## 5. Key Discoveries Preserved

| Discovery | Source | Preserved in |
|-----------|--------|--------------|
| Price index sparse after import | 06C/06D | Knowledge Map §5, §7 |
| Offers import must call `refreshPriceIndex` | 06F | Knowledge Map §2, §8 |
| Zero-price SKUs collapse slider min | 06H | Knowledge Map §5, §7 |
| Numeric `attr[51][]` needs `attribute_id` branch | 06J | Knowledge Map §6, §7 |
| `IFNULL(special, price)` breaks filters when special=0 | 06M | Knowledge Map §5, §7 |
| Filter AJAX via full-page fetch + DOM swap | 08 forensic | Knowledge Map §7 |
| Subcategories hidden UI-only; backend `s[]` intact | 07 | Knowledge Map §7 |
| Group reset reuses `updateBrowserUrl` chain | 08/08A | Knowledge Map §7 |
| Operator scroll offset 0 is canonical | 04B | Knowledge Map §12 |
| Wishlist/compare tips context-aware | 01 | Knowledge Map §9 (catalog cards) |

---

## 6. Operational Rules Updated

| Location | Update |
|----------|--------|
| Knowledge Map §13 | PRE-TASK RULE — general + domain-specific (filters, catalog, 1C, price, PLP) |
| site-passport.md | Next work rule → new authority |
| README.md | PRE-TASK rule reference |
| OPERATIONAL-INDEX.md | Run 4.143; authority `FILTER-UX-COMPLETE-01` |
| OCPILOT-STATE.md | SITE-002 focus → filter UX complete |

---

## 7. Git Result

| Item | Value |
|------|--------|
| Commit | *(filled after commit)* |
| Push | *(filled after push)* |
| Scope | Documentation only — no live files |

---

*Documentation only — no runtime claimed.*
