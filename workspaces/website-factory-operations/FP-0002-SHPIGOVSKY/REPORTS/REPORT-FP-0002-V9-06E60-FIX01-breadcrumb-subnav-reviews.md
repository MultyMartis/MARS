# REPORT — FP-0002 V9-06E60-FIX01 Breadcrumb/Subnav Restore and Reviews Page

**Date:** 2026-07-17  
**Runtime:** `http://shpigovsky.test/`  
**Database:** `mars_wp_fp0002`  
**Evidence:** `REPORTS/evidence/v9-06e60-fix01-breadcrumb-subnav-reviews/`  
**Backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e60-fix01-before-breadcrumb-subnav-reviews-correction-20260717-020758`

---

## 1. Status

| Item | Result |
|------|--------|
| Overall | **PASS** |
| Operator review | **pending** |
| DB writes | **0** |
| Commit / push / freeze | **no** |

---

## 2. Pre-Change Backup

| Item | Value |
|------|-------|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e60-fix01-before-breadcrumb-subnav-reviews-correction-20260717-020758` |
| DB dump | `db/mars_wp_fp0002.sql` — 6 228 952 bytes — SHA256 `3A751318DCC17A384563034BF3D59D1F2F6DEA60DBC09C20BF8987C411F4BA86` |
| Validation | **PASS** (`CREATE TABLE` + `INSERT`; `BACKUP-OK.txt`) |
| Hashes / manifest | `hashes.csv`, `operator-change-manifest.csv` |
| Contents | current + E58 stable CSS; related templates; DB dump |

---

## 3. Latest Operator Changes Preserved

| Item | Detail |
|------|--------|
| CSS | Preflight: source ↔ runtime **MATCH** (`B60D01A4…`). No promote required. |
| Templates | Theme drift **0**. |
| Protected | All unrelated operator CSS/HTML retained; only breadcrumb hover + reviews name rules/markup touched. |
| Unresolved drift | **0** after exact-file delivery. |

---

## 4. Stable Backup Authority

| Item | Detail |
|------|--------|
| Exact path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e58-current-baseline-freeze-before-visual-audit-20260716-225434\` |
| CSS used | `operator-edits/v9-style.css` (SHA256 `307A111E…`) — freeze-protected operator canon; matches `theme-runtime` copy |
| Why authoritative | E58 freeze marker + operator acceptance before visual-audit corrections; charter names this backup as style authority for `.breadcrumbs` / `.services-page-subnav` |

Rule extraction: full selector parse of breadcrumb + subnav families (38 rules). Diff vs pre-FIX01 current: **5 hover color rules only**. Subnav: **0 diffs**.

---

## 5. Breadcrumb Restore

| selector | viewport | stable font-size/line-height | current-before | final | removed override | result |
|----------|----------|------------------------------|----------------|-------|------------------|--------|
| `.internal-page-nav .breadcrumbs__link` | 1440/1024/480/370 | 14px / 18px | 14 / 18 | 14 / 18 | — | PASS |
| `.page-blog …` / article crumbs | ≤1024 | 8px / 12px | 8 / 12 | 8 / 12 | — | PASS |
| `.blog-article-hero__breadcrumbs` desktop | 1440 | 13px / 18px | 13 / 18 | 13 / 18 | — | PASS |
| all page crumb `:hover`/`:focus-visible` | all | `var(--color-accent)` | `var(--color-accent-hover)` (E60) | `var(--color-accent)` | E60 accent-hover | PASS |
| `/kontakty/`, `/otzyvy/` crumb markup | all | CSS rules restored | skeleton empty nav (pre-existing) | skeleton unchanged | — | SAFE UNKNOWN (markup) |

Typography 14/18 and blog 8/12 were already identical to E58; E60 did not invent those values. Divergent active rules were **hover color only**.

---

## 6. Services Subnav Restore

| selector | viewport | stable font-size/line-height | current-before | final | removed override | result |
|----------|----------|------------------------------|----------------|-------|------------------|--------|
| `.services-page-subnav__link` | 1440/1024/480/370 | 14px / 20px | 14 / 20 | 14 / 20 | none needed | PASS |
| `:hover`/`:focus-visible` | all | border+color `var(--color-accent)` | identical | identical | none | PASS |

E60 did not alter subnav typography/hover. Stable backup already wins; no rule removal required beyond confirming parity.

---

## 7. Removed Current Rules

| selector | file | breakpoint | why removed |
|----------|------|------------|-------------|
| `.internal-page-nav .breadcrumbs__link:hover,:focus-visible { color: var(--color-accent-hover) }` | `v9-style.css` | default | E60 override vs E58 |
| `.contacts-page__breadcrumbs .breadcrumbs__link:hover,…` | same | default | same |
| `.reviews-page__breadcrumbs .breadcrumbs__link:hover,…` | same | default | same |
| `.blog-page__breadcrumbs .breadcrumbs__link:hover,…` | same | default | same |
| `.blog-article-hero__breadcrumbs .breadcrumbs__link:hover,…` | same | default | same |

Restored exact stable declarations: `color: var(--color-accent);`

---

## 8. Reviews Name Correction

| Item | Value |
|------|-------|
| Previous element | `<h2 class="review-archive-card__name">` |
| Final element | `<div class="review-archive-card__name">` |
| Class | `review-archive-card__name` (retained) |
| font-size | **18px** (all audited viewports) |
| line-height | **24px** |
| weight | `var(--font-weight-heading)` → computed **400** |
| Figma / V9 evidence | Operator requires 18px; design token `--font-size-base: 18px`; Home `.reviews__author-name` uses base; prior desktop used `--font-size-h3` (26px) — clear mismatch |

Template: `template-parts/components/review-archive-card.php` (standalone `/otzyvy/` archive cards only; slider titles untouched).

---

## 9. Reviews Page Audit

### Findings / fixes

| Finding | Action |
|---------|--------|
| Name as `<h2>` | Fixed → `<div>` |
| Desktop name 26px (h3 token) | Fixed → 18px / 24px |
| Mobile name already 18/24 (operator) | Kept (charter 18px) |
| Single-column card stack, mobile padding 20 / gap 12 / min-height 400 / body 15/20 | Match V9 EXACT_GEOMETRY — no change |
| V9 SCSS adaptive name note `16px` | **SAFE UNKNOWN / intentional keep 18px** per operator charter |
| `/otzyvy/` breadcrumbs skeleton empty | **SAFE UNKNOWN** pre-existing; CSS restored but trail not rendered |

### Four viewports (`/otzyvy/`)

| VP | tag | font-size | h2 count | div count | overflow |
|----|-----|-----------|----------|-----------|----------|
| 1440 | DIV | 18px | 0 | 10 | 0 |
| 1024 | DIV | 18px | 0 | 10 | 0 |
| 480 | DIV | 18px | 0 | 10 | 0 |
| 370 | DIV | 18px | 0 | 10 | 0 |

Screenshots: `evidence/.../screenshots/otzyvy-*.png`, `otzyvy-body-*.png`.

---

## 10. Exact Files Changed

### Canonical source
- `WORDPRESS/theme/shpigovsky/assets/css/v9-style.css`
- `WORDPRESS/theme/shpigovsky/template-parts/components/review-archive-card.php`

### Runtime
- `wp-content/themes/shpigovsky/assets/css/v9-style.css`
- `wp-content/themes/shpigovsky/template-parts/components/review-archive-card.php`

### Reports / evidence
- `REPORTS/REPORT-FP-0002-V9-06E60-FIX01-breadcrumb-subnav-reviews.md`
- `REPORTS/evidence/v9-06e60-fix01-breadcrumb-subnav-reviews/*`
- `PROJECT-STATUS.md`

---

## 11. Source-to-Runtime Delivery

| File | before | after | match |
|------|--------|-------|-------|
| `v9-style.css` | `B60D01A4…` | `3F8163FF…` | source = runtime YES |
| `review-archive-card.php` | `84059942…` | `60B5A707…` | source = runtime YES |

Exact-file copy only. No broad theme/plugin sync. Operator changes preserved outside scoped selectors.

---

## 12. Validation

| Area | Result |
|------|--------|
| Breadcrumb routes | `/uslugi/`, `/uslugi/zavisimosti/`, alcohol service, `/o-centre/`, `/blog/`, blog single @1024 → 8/12; `/kontakty/`+`/otzyvy/` skeleton (SAFE UNKNOWN) |
| Subnav routes | `/uslugi/`, `/zavisimosti/`, alcohol service — 14/20 PASS |
| Reviews | `/otzyvy/` — DIV + 18px PASS |
| Viewports | 1440 / 1024 / 480 / 370 |
| PHP warnings | **0** |
| JS errors | **0** |
| Horizontal overflow | **0** |

---

## 13. Regression

| Surface | Status |
|---------|--------|
| Header | present / untouched |
| Floating header | `fp02-floating-header` present / untouched |
| Offcanvas | not mutated |
| Service-name links | untouched |
| CTA bands | present / untouched |
| Maps / galleries | untouched |
| Footer | present / untouched |
| Lifebuoy | `fp02-lifebuoy-parallax` present / untouched |

---

## 14. Risks and Tails

1. **`/kontakty/` and `/otzyvy/`** still use `shpigovsky-skeleton-breadcrumbs` (empty). CSS for `.contacts-page__breadcrumbs` / `.reviews-page__breadcrumbs` restored, but trail markup is a separate future wave.
2. Playwright `:hover` computed color probe is unreliable headless; stylesheet rule text confirmed restored to `var(--color-accent)`.
3. V9 static HTML still shows `<h2>` for archive names; WP now follows operator/Figma 18px + neutral `<div>`.
4. V9 SCSS adaptive `16px` name note vs operator `18px` — kept 18px per charter.

---

## 15. Git Status

- **no commit**
- **no push**
- **no freeze**
- Exact FP-0002 scope only; foreign WIP untouched

---

## 16. Operator Review Pages

| URL | Inspect |
|-----|---------|
| `http://shpigovsky.test/uslugi/` | Breadcrumbs 14/18; subnav pills + hover accent (not accent-hover) |
| `http://shpigovsky.test/uslugi/zavisimosti/` | Same + section subnav |
| `http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | Service crumbs + subnav |
| `http://shpigovsky.test/blog/` (≤1024) | Blog crumbs 8/12 |
| `http://shpigovsky.test/blog/sryvy-i-retsidivy-signal-k-korrektirovke/` (≤1024) | Article crumbs 8/12 |
| `http://shpigovsky.test/otzyvy/` | Reviewer names as non-heading `div`, **18px**; card stack vs Figma |
| `http://shpigovsky.test/kontakty/` | Confirm unrelated surfaces; crumbs still skeleton |

Do not commit, push or freeze.
