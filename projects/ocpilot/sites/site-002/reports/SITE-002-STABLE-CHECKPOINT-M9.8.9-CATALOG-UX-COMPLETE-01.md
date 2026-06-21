# REPORT — SITE-002 STABLE CHECKPOINT M9.8.9 CATALOG UX COMPLETE 01

**Project:** SITE-002 (ЗПМ / BZPM)  
**Date:** 2026-06-21  
**Prior authority:** `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01`  
**New authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Mode:** Stable checkpoint registration — documentation only (no deploy, no FTP)

---

## 1. New Authority State

| Field | Value |
|-------|--------|
| **Authority** | `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` |
| **Supersedes** | `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` |
| **Environment** | TEST — https://zpm.new-site.space/ |
| **Manual UI policy** | **CANONICAL** — operator CSS/Twig/JS/UX edits on live TEST override pass reports and work copies |

---

## 2. Stable Scope

Registered as part of authority state:

### Filter Recovery

- 06D · 06F · 06H · 06J · 06M

### Filter UX

- 04 · 04A · 04B · 07 · 08 · 08A

### Wishlist / Compare

- 01

### Commercial Trust

- 03B · 03C · operator manual polish · FAQ redesign · OEM proof structure

### Catalog State Persistence

- 09A · 09B · 09C

**Joint behaviour:** `filter` + `limit` + `sort` + `pagination` + `only_with_price` work together on category PLP.

### Hub Cleanup

- 10 — removal of `page-intro__description` for `/katalog/nejtralnoe-oborudovanie`

### Carried forward (unchanged scope)

- M9.8.1 PDP Gallery · M9.8.2 Lightbox · M9.8.5 Products Per Page · operator manual PLP polish

---

## 3. Registered Discoveries

| Discovery | Pass | Summary |
|-----------|------|---------|
| **JS URL rebuild dropped non-filter params** | 09A | `updateBrowserUrl()` replaced entire query with `?filters=` only — `limit`, `sort`, `order`, `page` lost on filter toggle |
| **PHP URL generation omitted `filters`** | 09A | Sort/limit/pagination `$url` blocks in `category.php` did not append `filters` — full-page limit/pagination links dropped active filter |
| **Limit menu stale after AJAX** | 09B | `updateProducts()` refreshed grid + pagination but not `.category__limit` — operator path filter→limit used plain-page hrefs without `filters` |
| **Sort buttons unaffected** | 09B | Sort uses `data-sort` + `window.location.href` merge — reads live URL including `filters` |
| **Pagination refreshed after AJAX** | 09B | `.pagination` replaced from fetch response — asymmetry vs limit menu was root of 09C fix |
| **Limit toolbar refresh fix** | 09C | `updateProducts()` swaps `.category__limit` from response + re-inits `initCategoryLimitMenu()` |
| **Hub intro was controller hardcode** | 10 | `$pageintro->description` on neutral hub from `category.php` M9.5 logic — not CMS, not twig |

---

## 4. Knowledge Map Updates

**File:** [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)

| Change | Content |
|--------|---------|
| **§16 Catalog State Persistence** | **Added** — state model, `updateBrowserUrl()`, `updateProducts()`, `category__limit` refresh, pagination refresh, PHP URL generation, joint param behaviour |
| **§1 Authority** | Updated to `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` |
| **§13 PRE-TASK RULE** | Added domain-specific rule for filters / sort / pagination / limit / only_with_price — mandatory read §16 + 09A/09B/09C |

---

## 5. Operational Rule Updates

Before **any** task touching **filters**, **sort**, **pagination**, **limit**, or **only_with_price**:

1. Read Knowledge Map → **§16 Catalog State Persistence**
2. Read passes **M9.8.9-09A**, **M9.8.9-09B**, **M9.8.9-09C** as mandatory context
3. Read latest stable checkpoint — `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`
4. Test **interaction paths** (not only full-page URL loads): filter AJAX → limit click; limit → filter; full combo with sort + page

Registered in Knowledge Map §13 and baseline §9.

---

## 6. Updated Files

| File | Change |
|------|--------|
| `baselines/SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md` | **created** |
| `knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | §16 + authority + PRE-TASK update |
| `site-passport.md` | authority, status, catalog UX scope |
| `README.md` | authority, active checkpoint |
| `../../OCPILOT-STATE.md` | SITE-002 state |
| `../../OPERATIONAL-INDEX.md` | Run **4.145** |
| `reports/SITE-002-STABLE-CHECKPOINT-M9.8.9-CATALOG-UX-COMPLETE-01.md` | **created** — this report |

---

## 7. Git Result

| Item | Value |
|------|--------|
| Commit | **requested** — checkpoint registration commit |
| Push | **requested** |
| Live changes | **NONE** — documentation only |

---

## 8. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| M9.8.9-09C browser QA Q1–Q6 | **PENDING operator** — automated probe PASS; full interaction HITL not recorded in repo |
| Mobile filter shell limit control | **SAFE UNKNOWN** — 09C scoped to desktop `.category__limit` toolbar path |
| ocStore / OpenCart exact version | **SAFE UNKNOWN** |
| M10 scope and authorization | **not authorized** |

---

*Documentation only — no runtime claimed.*
