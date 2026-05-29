REPORT — V6 visual QA audit

**Date:** 2026-05-29  
**Mode:** QA-only / report-only (no fixes, no commit, no push)  
**Workspace:** `workspaces/triumph-manipulator-landing-v6/`  
**Baseline:** V6 Production Candidate v1 — `workspaces/_snapshots/snap-20260529-triumph-v6-production-candidate-v1/`  
**Baseline report:** `reports/v6-production-candidate-freeze-report-v1.md`  
**Routes audited:** 12 (`index`, `5-tonn`, `bytovki`, `konteynery`, `oborudovanie`, `fbs-zhbi`, `armatura`, `kirpich-bloki`, `stroymaterialy`, `vezdehod`, `yurlic`, `kray`)

---

## 1. Build status

| Step | Result |
|------|--------|
| Command | `npm run build` in `workspaces/triumph-manipulator-landing-v6` |
| Exit code | **0** |
| Duration | ~1.52s |
| Output | `dist/` regenerated (12 HTML routes, `dist/assets/*`, `dist/backend/send-lead.php`) |
| Warnings | Sass legacy JS API deprecation (non-blocking) |

**Verdict:** **PASS** — build succeeded; audit continued.

---

## 2. Static QA table

Built HTML checked at `dist/<route>.html` (index → `dist/index.html`). Footer JS checked at `dist/assets/js/header-menu.js`.

| Route | Dist exists | `#contacts` ×1 | No `hero__notice` | No mock handler | No `send.php` ref | Phone display | `tel:` link | Email | MAX | Telegram | WhatsApp | Footer nav | Footer clean-scroll JS | Overall |
|-------|:-----------:|:--------------:|:-----------------:|:-----------------:|:-----------------:|:-------------:|:-----------:|:-----:|:---:|:--------:|:--------:|:----------:|:------------------------:|:-------:|
| index | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| 5-tonn | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| bytovki | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| konteynery | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| oborudovanie | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| fbs-zhbi | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| armatura | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| kirpich-bloki | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| stroymaterialy | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| vezdehod | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| yurlic | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| kray | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |

**Canonical values (all 12 routes):**

| Channel | Expected | Result |
|---------|----------|--------|
| Phone (display) | `+7 (918) 991-2-991` (incl. `&nbsp;` variant) | **PASS** |
| Phone (`tel:`) | `tel:+79189912991` | **PASS** |
| Email | `info@manipulator-triumph.ru` | **PASS** |
| MAX | `https://max.ru/u/f9LHodD0cOI8NplZUAfTNT7cDN89_7GhazWQy0u9B3AbC0ktxFkC6JWVPm0` | **PASS** |
| Telegram | `https://t.me/gruzotaxi_triumph` | **PASS** |
| WhatsApp | `https://wa.me/+79189912991` | **PASS** |
| Form endpoint (JS) | `backend/send-lead.php` in `dist/assets/js/form.js` | **PASS** |
| Legacy phone/email patterns | `991-29-91`, `info@triumph`, old messenger URLs | **0 hits** in `dist/*.html` |

**Footer clean-scroll evidence:** `initLandingFooterNav`, `footerNavInit`, `bindSectionNavLinks`, `handleSectionNavigation` present in `dist/assets/js/header-menu.js` (mirrors `src/js/header-menu.js`).

**Supplementary tool run:** `node tools/verify-final-wave-dist.mjs` → **FAIL** on `5-tonn` only for optional copy marker `Что не перевозим` (not in production-candidate charter; tracked as **P2** below).

---

## 3. Visual QA method

| Item | Detail |
|------|--------|
| **Method** | Playwright Chromium headless against local static `dist/` HTTP server |
| **Breakpoints** | 390, 430, 560, 768, 1024, 1280, 1440 (viewport width × 900 height) |
| **Coverage** | 12 routes × 7 breakpoints = **84** full-page PNG captures |
| **Screenshot path** | `reports/_qa-screenshots-v6-visual-audit-v1/` |
| **Automated checks** | Document horizontal overflow; broken images (`naturalWidth === 0`); hero cargo card `scrollWidth > clientWidth`; clipped selectors (hero title, cargo card, primary button, contact channels, footer nav) |
| **Manual review** | Spot-check of captures + targeted re-check of machine-showcase images after `scrollIntoView` |

**Not executed:** Live deploy preview, real-device browsers, modal open/close interaction matrix, form POST to production mail, footer hash strip in address bar after click.

---

## 4. Route-by-route findings

| Route | Static QA | Visual QA | Notes |
|-------|-----------|-----------|-------|
| **index** | PASS | **P2** @ 1280 | Hero cargo card action text clips inside 1 card (~20px internal overflow). No page-level horizontal overflow. Machine image loads when in viewport (`second-screen-zakaz.jpg`, 514×767px displayed). |
| **5-tonn** | PASS | **P2** @ 1280 | Same cargo-card clip as index. Optional copy `Что не перевозим` absent (`verify-final-wave-dist.mjs`). |
| **bytovki** | PASS | **OK** | No automated visual defects. |
| **konteynery** | PASS | **P2** @ 1280 | 2 cargo cards with internal action-text overflow (9–22px). |
| **oborudovanie** | PASS | **P2** @ 1280 | 1 cargo card internal overflow (automated pass flagged during full sweep). |
| **fbs-zhbi** | PASS | **OK** | — |
| **armatura** | PASS | **OK** | — |
| **kirpich-bloki** | PASS | **OK** | — |
| **stroymaterialy** | PASS | **OK** | — |
| **vezdehod** | PASS | **OK** | — |
| **yurlic** | PASS | **OK** | — |
| **kray** | PASS | **OK** | — |

**Cross-route observations (non-blocking):**

- **`robots: noindex,nofollow`** on all 12 routes — intentional pre-release policy per freeze report (**OK** until release charter changes).
- **Review panel** uses placeholder cards (`review-list--placeholder`) — by design until widget integration; tall aside at desktop is expected, not a layout break.
- **Orphan source** `src/partials/sections/v5-page01/screen-01-hero.html` still contains `.hero__notice` — **not emitted** in any of the 12 `dist/*.html` routes.

---

## 5. Breakpoint findings

| Width | Horizontal page overflow | Broken images | Hero / cargo | FAQ / contact split | Footer / messengers | Modals |
|------:|:------------------------:|:-------------:|:------------:|:-------------------:|:-------------------:|:------:|
| 390 | OK | OK | OK | OK (stacked) | OK | Not opened |
| 430 | OK | OK | OK | OK | OK | Not opened |
| 560 | OK | OK | OK | OK | OK | Not opened |
| 768 | OK | OK | OK | OK | OK | Not opened |
| 1024 | OK | OK | OK | OK | OK | Not opened |
| **1280** | OK | OK | **P2:** cargo-card action text clip on index, 5-tonn, konteynery, oborudovanie | OK | OK | Not opened |
| 1440 | OK | OK | OK | OK | OK | Not opened |

**Machine showcase @ 1280:** Full-page captures can show an empty white media frame before lazy-loaded images enter the viewport; after `scrollIntoView`, images render correctly on index / 5-tonn / konteynery / bytovki (natural size 1696×2528, displayed ~514×767). **Not classified as a defect** without lazy-load policy change.

---

## 6. P0 / P1 / P2 summary

| Priority | Count | Items |
|----------|------:|-------|
| **P0** | 0 | — |
| **P1** | 0 | — |
| **P2** | 2 | (1) Hero `.hero__cargo-card` action label internal overflow at **1280px** on `index`, `5-tonn`, `konteynery`, `oborudovanie` — polish before/after deploy. (2) `5-tonn` missing optional copy block `Что не перевозим` per `verify-final-wave-dist.mjs`. |
| **OK** | 8 routes fully clean visually; all 12 routes pass static production-candidate checks |

**Static-risk watchlist (not promoted to P1 without visual proof):**

- `white-space: nowrap` in `_screen-04-faq.scss`, `_modal.scss`, `_screen-02-prices.scss` — possible long-string pressure on narrow widths; no overflow observed in this pass.
- `body { overflow-x: hidden; }` in `_base.scss` — masks edge overflow; page-level scroll checks still showed no excess width.

---

## 7. Recommended fix order

1. **P2 — Hero cargo cards @ 1280:** Relax `.hero__cargo-action` wrapping or reduce padding/font in `_v5-hero-extensions.scss` (1024–1320 band); re-run visual pass at 1280 on index + PPC heroes.
2. **P2 — `5-tonn` copy:** Add or restore `Что не перевозим` section if product owner wants parity with `verify-final-wave-dist.mjs` marker.
3. **Pre-release policy:** Remove `noindex,nofollow` from route heads when release charter approves indexing (all 12 pages).
4. **Post-deploy / optional:** Connect live review widget; confirm footer hash stripping in production CDN environment; live form mail spot-check per route.

**No P0/P1 blockers identified** for production-candidate static charter in this audit.

---

## 8. Files changed

| Path | Action |
|------|--------|
| `workspaces/triumph-manipulator-landing-v6/reports/v6-visual-qa-audit-report-v1.md` | **Created** (this report) |
| `workspaces/triumph-manipulator-landing-v6/reports/_qa-screenshots-v6-visual-audit-v1/*.png` | **Created** (84 screenshot artifacts — QA evidence only) |

**No source, SCSS, HTML, JS, backend, or config files were modified.**

`dist/` was regenerated by `npm run build` (build artifact; not committed).

---

## 9. SAFE UNKNOWN

- **Footer hash cleanup in real browser** after footer-nav click (`history.replaceState`) — logic present in bundle; click behavior not manually verified.
- **Modal layout** (phone / callback) at all breakpoints — modals not opened during automated pass.
- **Form submission / antispam / live mail** — not tested (requires server + mail config).
- **Full-page screenshots vs lazy `loading="lazy"`** — machine media may appear empty in captures taken before scroll; in-viewport check confirms images load.
- **Production CDN / caching** — not in scope.
- **Accessibility** (contrast, focus order, screen readers) — not audited.

---

## 10. Git status

**Workspace repo:** `C:\AI MARS` (branch `mars/post-cycle8-live-tests` per freeze report).

**This task scope (`workspaces/triumph-manipulator-landing-v6/reports/`):**

```
?? workspaces/triumph-manipulator-landing-v6/reports/_qa-screenshots-v6-visual-audit-v1/
?? workspaces/triumph-manipulator-landing-v6/reports/v6-visual-qa-audit-report-v1.md
?? workspaces/triumph-manipulator-landing-v6/reports/v6-production-candidate-freeze-report-v1.md
?? workspaces/triumph-manipulator-landing-v6/reports/v6-after-image-mapping-v1-snapshot-report.md
?? workspaces/triumph-manipulator-landing-v6/reports/v6-pre-final-rollout-wave-snapshot-report-v1.md
```

**Commit / push:** not performed (per charter).

**Note:** Broader repo has many unrelated modified/untracked paths outside this QA task; see `git status` at repo root for full picture.

---

**Audit conclusion:** V6 production candidate **passes** frozen static/contact/messenger/footer checks on all 12 routes after a clean build. Visual automation found **no P0/P1** issues; **P2** polish items at desktop 1280px (hero cargo CTA text) and optional `5-tonn` copy marker. **Safe to proceed** from a static-production-candidate perspective; address P2 items per product priority before or after deploy.
