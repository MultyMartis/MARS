# REPORT — FP-0002 PROD-P09 Specialist Fancybox + Smart Search

**Date:** 2026-08-14 (updated PROD-P09-FU01)  
**Host:** `http://shpigovsky.beget.tech/`  
**Docroot:** `/home/s/shpigovsky/shpigovsky.ru/public_html`  
**Evidence:** `REPORTS/evidence/prod-p09-specialist-fancybox-smart-search/`

---

## 1. Status

| Item | Result |
|------|--------|
| Wave verdict (P09) | **PASS** (technical closeout) |
| Wave verdict (P09-FU01) | **PASS** (mobile parity + CSS canonization) |
| Production file writes (FU01) | **3** (exact theme files) |
| DB / Admin writes | **0** |
| ACF mutations | **0** |
| WPilot writes | **0** (`write_enabled=false`) |
| Commit / push | **none** |

```text
OPERATOR DESKTOP SMART SEARCH VISUAL ACCEPTED
```

```text
SMART SEARCH DESKTOP + MOBILE PARITY COMPLETE
```

```text
PROD-P09 SMART SEARCH DESKTOP + MOBILE TECHNICAL CLOSEOUT COMPLETE — OPERATOR MOBILE VISUAL ACCEPTANCE PENDING
```

---

## 2. Backup / Rollback

```text
P09 EXACT-FILE ROLLBACK MODE AUTHORIZED BY OPERATOR
```

| Item | Result |
|------|--------|
| Full Layer A required | **NO** (wave exception) |
| P09 snapshot | `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p09-layer-b-pre\` |
| FU01 snapshot | `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p09-fu01-layer-b-pre\` |
| FU01 prod-after | `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p09-fu01-prod-after\` |
| Rollback ready | **YES** |

---

## 3. Fancybox Root Cause

| Item | Finding |
|------|---------|
| Assets | Fancybox CSS/JS already enqueued on specialist pages with certificates |
| Markup | `data-fancybox="specialist-certs-{id}"` + full-size JPEG `href` already present |
| Failure | `v9-shell.js` bound Comfort / o-centre / home-videos only — specialist gallery never received `Fancybox.bind()` |

---

## 4. Fancybox Fix

| Item | Result |
|------|--------|
| Selector | `.specialist-profile__certs-grid [data-fancybox]` |
| Initialization | Added inside existing `initComfortFancybox()` with shared gallery options |
| Navigation | Next/Prev **PASS** (`1/3`→`2/3`→`1/3`) |
| FU01 regression | **PASS** (unchanged) |

```text
SPECIALIST CERTIFICATE GALLERY FANCYBOX = PASS
```

---

## 5. Smart Search Architecture

| Layer | Owner |
|-------|--------|
| Desktop UI | Header `search-panel.php` + `searchform.php` |
| Mobile UI (FU01) | Offcanvas embedded `searchform.php` (`site-search-form--offcanvas`) |
| Endpoint | `GET /wp-json/shpigovsky/v1/smart-search` (shared) |
| JS | `initSmartSearchForms()` shared binder + `initSiteSearchPanel()` desktop chrome |
| CSS | `fp02-search.css` (operator-canonized + scoped mobile rules) |

```text
SMART SEARCH LIVE — 3+ CHARACTER SUGGESTIONS GROUPED BY CONTENT TYPE
```

```text
SMART SEARCH LIVE SUGGESTIONS ACTIVE ON MOBILE OFFCANVAS
```

---

## 6. Classification

| Group | Rule |
|-------|------|
| Услуги | published `service` |
| Статьи | published `post` |
| Специалисты | published child pages under `/specyalisty/` |
| Страницы | other published pages minus specialists + legal/system exclusions |
| Duplicate prevention | mutually exclusive `shpigovsky_smart_search_group_key()` |

---

## 7. Trigger / Transport

| Rule | Value |
|------|--------|
| Min chars | 3 (UTF-8 / Cyrillic-safe) |
| Debounce | 250 ms |
| Stale requests | AbortController + request sequence token (per instance) |
| Method | GET REST read-only |

---

## 8. Relevance

Tiers: exact title → starts-with → contains → excerpt/public short fields → body.  
Limit: 5 per group.

---

## 9. Search UX

Grouped RU headings; loading / empty («Ничего не найдено») / error soft-fail; Escape clears suggestions; Arrow/Enter preferred on results; native `/?s=` submit remains.  
Desktop: operator visual **accepted**.  
Mobile offcanvas: live suggest parity (FU01) — operator mobile visual acceptance **pending**.

---

## 10. Security / Performance

Sanitize query; escape HTML in JS; published-only WP_Query; no raw SQL; bounded payload; no secrets/admin meta; no browser-side full-site index.

---

## 11. Exact Files Changed

### P09 (prior)

1. `assets/js/v9-shell.js`
2. `assets/css/fp02-search.css`
3. `inc/search-helpers.php`
4. `inc/assets.php`
5. `searchform.php`
6. `template-parts/navigation/search-panel.php`

### P09-FU01

1. `assets/js/v9-shell.js` — shared Smart Search initializer + offcanvas clear-on-close
2. `assets/css/fp02-search.css` — operator CSS preserved + scoped offcanvas suggest rules
3. `template-parts/navigation/offcanvas.php` — embedded live-suggest search form

Also local-only canonization (no upload): `assets/css/v9-style.css` (operator layout drift).

Plus reports/evidence under `REPORTS/` and `PROJECT-STATUS.md`.

---

## 12. DB / ACF

```text
NO DB/ADMIN/ACF MUTATION
```

---

## 13. Source / Production Parity

| Wave | Files | Parity |
|------|------:|--------|
| P09 | 6/6 | **SOURCE ↔ PRODUCTION MATCH** |
| FU01 | 3/3 | **SOURCE ↔ PRODUCTION MATCH** (SFTP) |

See `deploy-manifest.json` / `FU01-DEPLOY-MANIFEST.json` / `FU01-SOURCE-PROD-PARITY.json`.

---

## 14. Frontend QA

- Specialist Fancybox desktop+mobile: **PASS**
- Desktop Smart Search regression: **PASS** (`DESKTOP SMART SEARCH ACCEPTED BEHAVIOR PRESERVED`)
- Mobile live suggest 375/390/767: **PASS**
- Breakpoint 768 dual-instance isolation: **PASS** (2 forms / 2 instances)

---

## 15. P07/P08 Regression

**PASS** smoke on sampled routes / Comfort Fancybox path retained / specialist structured template / WPilot write false. No unrelated fixes.

---

## 16. WPilot

`write_enabled=false` (public ping)  
Business writes: **0**

---

## 17. Secret Safety

Exposed: **0**  
Tracked secrets: **0**

---

## 18. Git

- Commit: **none**
- Push: **none**
- Foreign WIP: **untouched**

---

## 19. Operator CSS Canonization (FU01)

```text
OPERATOR CSS DRIFT PRESERVED AND CANONIZED
```

Production drift found in `fp02-search.css` + `v9-style.css`. Canonized into local source **before** FU01 implementation. Operator suggest spacing (`margin-top: 30px`, commented border/padding) preserved on production after deploy.

---

## 20. Acceptance

```text
PROD-P09 SMART SEARCH DESKTOP + MOBILE TECHNICAL CLOSEOUT COMPLETE — OPERATOR MOBILE VISUAL ACCEPTANCE PENDING
```

Do not execute any next wave automatically.

---

## 21. Remaining Work

- Operator mobile visual acceptance of offcanvas Smart Search
- Broader P08 WYSIWYG typography residual / out-of-scope items unchanged
