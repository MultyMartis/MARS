# SITE-002 — Stable Live M9.8.9 Catalog UX Complete Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Registered at:** 2026-06-21 (operator-requested stable checkpoint after catalog UX cluster completion)  
**Mode:** Stable live checkpoint registration — **metadata only** (no deploy, no FTP capture in this registration)

---

## 1. Authority state

`SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`

**Current Authority State:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`

**Supersedes:** `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01`

---

## 2. Current source of truth

| Priority | Source | Notes |
|----------|--------|-------|
| **1** | **Live TEST** — https://zpm.new-site.space/ | Authoritative storefront state |
| **2** | **Full Beget backup** | Operator attestation — disaster recovery |
| **3** | **Manual UI refinements** | **CANONICAL** |
| **4** | **Manual CSS refinements** | **CANONICAL** |
| **5** | **Manual Twig refinements** | **CANONICAL** |
| **6** | **Manual JS refinements** | **CANONICAL** |
| **7** | **Technical Knowledge Map** | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — incl. **§16 Catalog State Persistence** |

Prior repo baselines, work copies (`*-work/`), pass reports, and pre-pass `.bak` files are **historical** unless refreshed by live FTP capture.

**Do not** use `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` as current authority — superseded by this checkpoint.

---

## 3. Registration context

This checkpoint supersedes `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` and records the state after the **catalog UX cluster** is complete:

1. Filter recovery wave (06D–06M) — carried forward
2. Filter UX polish wave (04, 04A, 04B, 07, 08, 08A) — carried forward
3. Wishlist / Compare smart tooltips (01) — carried forward
4. Commercial Trust block (03B/03C + operator manual polish + FAQ redesign + OEM proof structure) — carried forward
5. **Catalog State Persistence** — M9.8.9-09A / 09B / 09C
6. **Hub Cleanup** — M9.8.9-10 (page-intro description removal on neutral hub)

---

## 4. Completed work (registered)

### Filter recovery (carried forward)

| Pass | Status on live |
|------|----------------|
| **M9.8.9-06D — Category 301 Price Index Rebuild** | **active** |
| **M9.8.9-06F — 1C Price Index Hook** | **active** |
| **M9.8.9-06H — Exclude Zero Price From Range** | **active** |
| **M9.8.9-06J — Numeric Attribute Filter Fix** | **active** |
| **M9.8.9-06M — Effective Price Hotfix** | **active** |

### Filter UX (carried forward)

| Pass | Status on live |
|------|----------------|
| **M9.8.9-04 — Filter Scroll Logic** | **active** |
| **M9.8.9-04A — Filter Scroll Offset Tuning** | **historical deploy** — operator canonical offset **0** (04B) |
| **M9.8.9-04B — Operator manual JS refinements** | **canonical** — scroll offset **0** |
| **M9.8.9-07 — Hide Subcategories Filter Block** | **active** |
| **M9.8.9-08 / 08A — Filter Group Reset** | **active** |

### Wishlist / Compare (carried forward)

| Pass | Status on live |
|------|----------------|
| **M9.8.9-01 — Wishlist / Compare Smart Tooltips** | **active** |

### Commercial Trust (carried forward)

| Pass | Status on live |
|------|----------------|
| **M9.8.9-03B — Commercial Trust Block Redesign** | **design complete** |
| **M9.8.9-03C — Commercial Trust Block Implementation** | **deployed** |
| **Operator manual Commercial Trust polish** | **canonical** — certificate podium, OEM benefits, FAQ grid, form card, logo contours |
| **FAQ redesign** | **active** — 8-card FAQ grid in `zpm-catalog-faq` |
| **OEM proof structure** | **active** — cert podium + 3 OEM benefit rows |

### Catalog State Persistence (new in this checkpoint)

| Pass | Status on live |
|------|----------------|
| **M9.8.9-09A — Filter + Limit Persistence Hotfix** | **active** — JS `updateBrowserUrl()` merge + PHP `filters` on sort/limit/pagination URLs |
| **M9.8.9-09B — Limit Link Forensic After Hotfix** | **forensic complete** — identified stale `.category__limit` DOM after AJAX |
| **M9.8.9-09C — Limit Toolbar AJAX Refresh Hotfix** | **active** — `updateProducts()` refreshes `.category__limit` + `initCategoryLimitMenu()` |

**Joint behaviour (registered):** `filter` + `limit` + `sort` + `pagination` + `only_with_price` work together on PLP when combined via sidebar AJAX, limit menu, sort buttons, and pagination.

### Hub Cleanup (new in this checkpoint)

| Pass | Status on live |
|------|----------------|
| **M9.8.9-10 — Page Intro Description Removal** | **active** — hub-only hardcoded intro removed from `category.php`; `/katalog/nejtralnoe-oborudovanie` has no `page-intro__description` |

### Other UX (carried forward)

| Pass | Status on live |
|------|----------------|
| **M9.8.1 / M9.8.2 / M9.8.5** | **active** |
| **Operator manual PLP / filter / breakpoint / CSS / Twig polish** | **active** |

---

## 5. Active stable state summary

| Item | Value |
|------|--------|
| Authority | **`SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`** |
| Catalog state model | `filters` + `limit` + `sort` + `order` + `page` — joint persistence on PLP |
| State persistence files | `assets/js/main.js` (`updateBrowserUrl`, `updateProducts`, limit refresh) · `catalog/controller/product/category.php` (URL generation) |
| Commercial Trust scope | Category PLP only — unchanged from prior checkpoint |
| Hub intro | `/katalog/nejtralnoe-oborudovanie` — **no** `page-intro__description`; `/katalog` root intro **unchanged** |
| Knowledge map | [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — **§16 Catalog State Persistence** |
| Live truth | **hosting state on `zpm.new-site.space`** |

---

## 6. Pass evidence (repo references)

### Catalog State Persistence

| Pass | Evidence |
|------|----------|
| 09A | [SITE-002-M9.8.9-09A-FILTER-LIMIT-PERSISTENCE-HOTFIX.md](../reports/SITE-002-M9.8.9-09A-FILTER-LIMIT-PERSISTENCE-HOTFIX.md) |
| 09B | [SITE-002-M9.8.9-09B-LIMIT-LINK-FORENSIC-AFTER-HOTFIX.md](../reports/SITE-002-M9.8.9-09B-LIMIT-LINK-FORENSIC-AFTER-HOTFIX.md) |
| 09C | [SITE-002-M9.8.9-09C-LIMIT-TOOLBAR-AJAX-REFRESH-HOTFIX.md](../reports/SITE-002-M9.8.9-09C-LIMIT-TOOLBAR-AJAX-REFRESH-HOTFIX.md) |

### Hub Cleanup

| Pass | Evidence |
|------|----------|
| 10 | [SITE-002-M9.8.9-10-PAGE-INTRO-DESCRIPTION-REMOVAL.md](../reports/SITE-002-M9.8.9-10-PAGE-INTRO-DESCRIPTION-REMOVAL.md) |

### Commercial Trust (prior checkpoint — carried forward)

| Pass | Evidence |
|------|----------|
| 03B / 03C | [SITE-002-M9.8.9-03B-COMMERCIAL-TRUST-BLOCK-REDESIGN.md](../reports/SITE-002-M9.8.9-03B-COMMERCIAL-TRUST-BLOCK-REDESIGN.md) · [SITE-002-M9.8.9-03C-COMMERCIAL-TRUST-BLOCK-IMPLEMENTATION.md](../reports/SITE-002-M9.8.9-03C-COMMERCIAL-TRUST-BLOCK-IMPLEMENTATION.md) |
| Checkpoint capture | [m9.8.9-commercial-trust-checkpoint-work/live-capture/](../reports/m9.8.9-commercial-trust-checkpoint-work/live-capture/) |

### Prior checkpoint (superseded)

| Pass | Evidence |
|------|----------|
| Commercial Trust | [SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md](SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md) |

---

## 7. Known open items (not blocking this checkpoint)

| Item | Status |
|------|--------|
| **EC-01** | mitigated by subcategories hide (07) |
| M9.8.9-09C browser QA matrix (Q1–Q6) | **PENDING operator** — automated probe PASS; interaction path not fully HITL-verified |
| M9.8.3/4/6/8 deferred UX passes | **not authorized** |
| **M10** | **not authorized** |

**Closed in this checkpoint (were open in Commercial Trust 01):**

| Item | Resolution |
|------|------------|
| **limit + filter persistence** | **closed** — 09A + 09C |
| **page-intro__description on neutral hub** | **closed** — 10 |

---

## 8. Rollback source

1. **Beget full backup** — full hosting restore
2. **Current live TEST state** — https://zpm.new-site.space/
3. **File-level backups** — `backups/*.pre-m9.8.9-*` incl. 09a/09c pass backups
4. **Commercial Trust checkpoint capture** — [m9.8.9-commercial-trust-checkpoint-work/live-capture/](../reports/m9.8.9-commercial-trust-checkpoint-work/live-capture/)
5. **Prior repo STABLE folders** — historical

---

## 9. Rule before next tasks

Before any next SITE-002 change:

1. Read [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)
2. Read this checkpoint (latest stable)
3. Verify **Authority State** = `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`
4. For **filters / sort / pagination / limit / only_with_price** — read Knowledge Map **§16 Catalog State Persistence** + passes **09A / 09B / 09C**
5. For **trust block / certificates / dealers form / category CTA** — read Knowledge Map **§14** + this checkpoint
6. For filter / catalog / 1C / price / PLP — follow Knowledge Map **§13** domain-specific PRE-TASK rule

See [SITE-002-WORKING-RULES.md](../SITE-002-WORKING-RULES.md).

---

## Status

| Field | Value |
|-------|--------|
| Checkpoint type | **STABLE LIVE CHECKPOINT** (metadata registration) |
| Supersedes (live truth) | `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` |
| Knowledge map | [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) |
| Rollback source | **Beget full backup + current live TEST + file-level pass backups** |
| Deploy (this registration) | **NO** |
| FTP (this registration) | **NO** |

---

*Documentation only — no runtime claimed.*
