# V6 production candidate polish — snapshot report v1

**Date:** 2026-05-29  
**Task:** Final scoped checkpoint for accepted V6 production-candidate polish  
**Snapshot ID:** `snap-20260529-triumph-v6-production-candidate-polish-v1`  
**Source workspace:** `workspaces/triumph-manipulator-landing-v6/`  
**Baseline HEAD (pre-commit):** `f235bf13945008cea6dc4949a69370744cb56b44`  
**Branch:** `mars/post-cycle8-live-tests`

**Constraints honored:** no new development, redesign, content rewrite, or route generation during checkpoint task.

---

## 1. Snapshot path

| Field | Value |
|-------|--------|
| **Relative** | `workspaces/_snapshots/snap-20260529-triumph-v6-production-candidate-polish-v1/` |
| **Full** | `C:\AI MARS\workspaces\_snapshots\snap-20260529-triumph-v6-production-candidate-polish-v1\` |
| **Manifest** | `SNAPSHOT-MANIFEST.md` |

---

## 2. Included / excluded

**Included:** `src/`, `backend/`, `docs/`, `reports/`, `tools/`, `package.json`, `package-lock.json`, `gulpfile.js`, `README.md`

**Excluded:** `node_modules/`, `dist/`, `.cache/`, `logs/`, `tmp/`, `temp/`, `*.log`, `_backup/`, `_snapshots/`

| Path | Snapshot files |
|------|---------------:|
| `src/` | 208 |
| `backend/` | 11 |
| `docs/` | 11 |
| `reports/` | 107 |
| `tools/` | 6 |

---

## 3. Polish checklist (accepted state)

| Track | Result |
|-------|--------|
| Global phone/email update | **PASS** |
| Messenger links (MAX / Telegram / WhatsApp) | **PASS** |
| Footer nav clean-scroll | **PASS** |
| Image mapping v1 + micro-correction | **PASS** (see project doc) |
| Hero cargo cleanup | **PASS** |
| Open Sans typography normalization | **PASS** |
| Hero cargo readability (`1025–1510px`) | **PASS** |
| Hero proof label typography (`761px+`) | **PASS** |
| `npm run build` | **PASS** |

---

## 4. Route verification (dist)

Built output: `dist/<route>.html` (12 PPC routes).

| Route | Dist | `#contacts`=1 | No notice | No mock | No send.php ref |
|-------|------|---------------|-----------|---------|-----------------|
| index | PASS | — | — | — | — |
| 5-tonn | PASS | PASS | PASS | PASS | PASS |
| bytovki | PASS | PASS | PASS | PASS | PASS |
| konteynery | PASS | PASS | PASS | PASS | PASS |
| oborudovanie | PASS | PASS | PASS | PASS | PASS |
| fbs-zhbi | PASS | PASS | PASS | PASS | PASS |
| armatura | PASS | PASS | PASS | PASS | PASS |
| kirpich-bloki | PASS | PASS | PASS | PASS | PASS |
| stroymaterialy | PASS | PASS | PASS | PASS | PASS |
| vezdehod | PASS | PASS | PASS | PASS | PASS |
| yurlic | PASS | PASS | PASS | PASS | PASS |
| kray | PASS | PASS | PASS | PASS | PASS |

**Note:** `node tools/verify-final-wave-dist.mjs` reports **FAIL** on `5-tonn` for optional marker `Что не перевозим` only. Charter checks above **PASS**.

---

## 5. Contact / messenger verification

Canonical values present on all **11** PPC `dist/*.html` routes (index excluded from PPC contact block checks where N/A):

| Channel | Expected | Dist |
|---------|----------|------|
| Phone | `+7 (918) 991-2-991` / `tel:+79189912991` | **PASS** |
| Email | `info@manipulator-triumph.ru` | **PASS** |
| MAX | `https://max.ru/u/f9LHodD0cOI8NplZUAfTNT7cDN89_7GhazWQy0u9B3AbC0ktxFkC6JWVPm0` | **PASS** |
| Telegram | `https://t.me/gruzotaxi_triumph` | **PASS** |
| WhatsApp | `https://wa.me/+79189912991` | **PASS** |

---

## 6. Backend / forms

| Check | Result |
|-------|--------|
| `dist/backend/send-lead.php` exists | **PASS** |
| `dist/backend/api/forms/send.php` absent | **PASS** |
| No `backend/api/forms/send.php` in dist HTML | **PASS** |

---

## 7. Typography / hero CSS evidence

| Check | Source / dist | Result |
|-------|---------------|--------|
| `$font-main: 'Open Sans'` | `src/scss/utils/_tokens.scss` | **PASS** |
| Montserrat absent from compiled CSS | `dist/assets/css/*.css` | **PASS** |
| Roboto absent from compiled CSS | `dist/assets/css/*.css` | **PASS** |
| Open Sans in compiled CSS | `dist/assets/css/*.css` | **PASS** |
| `.hero-proof__label` @ `761px+` | `src/scss/sections/_v5-hero-extensions.scss` L337–343 | **PASS** |
| `.hero__cargo-card` @ `1025–1510px` | same file L506–510 | **PASS** |

---

## 8. Footer navigation

| Check | Evidence | Result |
|-------|----------|--------|
| Footer nav partial | `landing-footer.html` / v5-page01 variant | **PASS** |
| Handler shared with header | `initLandingFooterNav()` in `src/js/header-menu.js` | **PASS** |
| Hash stripped after nav | `stripHashFromUrl()` / `history.replaceState` | **PASS** |

---

## 9. Git checkpoint scope (this commit)

**Staged for commit:** V6 workspace `src/` polish, Triumph project state docs, snapshot manifest + this report only (not full snapshot payload tree).

**Not staged:** `dist/`, `node_modules/`, QA screenshot binaries, unrelated repo paths.

---

## 10. Regression risks

- Optional dist marker `Что не перевозим` missing on `5-tonn` (verify script only; not charter-blocking).
- `zakaz` partials updated for contact parity but route not in 12-route production set.
- QA screenshot folder under `reports/_qa-screenshots-v6-visual-audit-v1/` remains untracked (large binaries).

---

## 11. SAFE UNKNOWN

- Live mail delivery on production host not re-tested in this checkpoint (filesystem/build only).
- Deployed CDN/cache behavior on target host **UNKNOWN**.
- Human visual sign-off on all 12 routes at all breakpoints **UNKNOWN** (automated dist/CSS checks only).

---

*End of report.*
