# V6 production candidate freeze report — v1

**Date:** 2026-05-29  
**Task:** Production-candidate rollback point for Triumph V6  
**Snapshot ID:** `snap-20260529-triumph-v6-production-candidate-v1`  
**Source workspace:** `workspaces/triumph-manipulator-landing-v6/`  
**Baseline commit:** `dc05c479eedd50233442009413fc90dbf314428f`  
**Branch:** `mars/post-cycle8-live-tests`

**Constraints honored:** no redesign, no content/CSS/route edits during freeze task; no commit; no push.

---

## 1. Snapshot path

| Field | Value |
|-------|--------|
| **Relative** | `workspaces/_snapshots/snap-20260529-triumph-v6-production-candidate-v1/` |
| **Full** | `C:\AI MARS\workspaces\_snapshots\snap-20260529-triumph-v6-production-candidate-v1\` |
| **Manifest** | `SNAPSHOT-MANIFEST.md` in snapshot root |
| **State doc** | `projects/triumph-manipulator-landing/V6-PRODUCTION-CANDIDATE-STATE.md` |

---

## 2. Included / excluded

**Included:** `src/`, `backend/`, `docs/`, `reports/`, `tools/`, `package.json`, `package-lock.json`, `gulpfile.js`, `README.md`

**Excluded:** `node_modules/`, `dist/`, `.cache/`, `logs/`, `tmp/`, `temp/`, `*.log`, `_backup/`, `_snapshots/`

| Path | Source files | Snapshot files | Parity |
|------|-------------:|---------------:|--------|
| `src/` | 208 | 208 | **PASS** |
| `backend/` | 11 | 11 | **PASS** |
| `docs/` | 11 | 11 | **PASS** |
| `reports/` | 22 | 22 | **PASS** (after this report filed) |
| `tools/` | 6 | 6 | **PASS** |

Excluded directories verified absent in snapshot root.

---

## 3. Production candidate checklist

| Check | Result |
|-------|--------|
| 12 PPC routes in `src/pages/` | **PASS** |
| `npm run build` | **PASS** (exit 0) |
| Single `id="contacts"` per route in `dist/` | **PASS** (12/12) |
| No `.hero__notice` in `dist/*.html` (12 routes) | **PASS** |
| No `data-form-handler="mock"` in `dist/*.html` | **PASS** |
| No `backend/api/forms/send.php` references in `dist/` | **PASS** |
| `dist/backend/send-lead.php` present | **PASS** |
| Canonical phone/email/messengers in `dist/` (12 routes) | **PASS** |
| No legacy phone/email/messenger strings in `dist/` | **PASS** |
| Footer nav clean-scroll wired | **PASS** (see §7) |
| Snapshot + manifest created | **PASS** |
| Git commit/push | **Skipped** (per charter) |

---

## 4. Route verification table

Built output: `dist/<route>.html` (index → `dist/index.html`).

| Route | `src/pages` | Dist exists | Build | `#contacts` = 1 | No `hero__notice` | No mock | No `send.php` ref | Overall |
|-------|-------------|-------------|-------|-----------------|-------------------|---------|-------------------|---------|
| `index` | Yes | Yes | PASS | PASS | PASS | PASS | PASS | **PASS** |
| `5-tonn` | Yes | Yes | PASS | PASS | PASS | PASS | PASS | **PASS** |
| `bytovki` | Yes | Yes | PASS | PASS | PASS | PASS | PASS | **PASS** |
| `konteynery` | Yes | Yes | PASS | PASS | PASS | PASS | PASS | **PASS** |
| `oborudovanie` | Yes | Yes | PASS | PASS | PASS | PASS | PASS | **PASS** |
| `fbs-zhbi` | Yes | Yes | PASS | PASS | PASS | PASS | PASS | **PASS** |
| `armatura` | Yes | Yes | PASS | PASS | PASS | PASS | PASS | **PASS** |
| `kirpich-bloki` | Yes | Yes | PASS | PASS | PASS | PASS | PASS | **PASS** |
| `stroymaterialy` | Yes | Yes | PASS | PASS | PASS | PASS | PASS | **PASS** |
| `vezdehod` | Yes | Yes | PASS | PASS | PASS | PASS | PASS | **PASS** |
| `yurlic` | Yes | Yes | PASS | PASS | PASS | PASS | PASS | **PASS** |
| `kray` | Yes | Yes | PASS | PASS | PASS | PASS | PASS | **PASS** |

**Note:** `node tools/verify-final-wave-dist.mjs` reports **FAIL** on `5-tonn` for optional marker `Что не перевозим` only. Production-candidate charter checks above all **PASS**.

---

## 5. Contact verification

Canonical values verified on all **12** `dist/*.html` routes:

| Channel | Expected | Dist scan |
|---------|----------|-----------|
| Phone (display) | `+7 (918) 991-2-991` / `+7&nbsp;(918)&nbsp;991-2-991` | **PASS** |
| Phone (tel) | `tel:+79189912991` | **PASS** |
| Email | `info@manipulator-triumph.ru` | **PASS** |

**Legacy scan** (`991-29-91`, `info@triumph`, `t.me/+`, `t.me/manipulator`, `wa.me/799`, `@gmail.com`): **0 hits** in `dist/*.html`.

**Source scan** (`src/**/*.html`, `src/**/*.js`): same legacy patterns — **0 hits**.

---

## 6. Messenger verification

| Channel | URL | Dist (12 routes) |
|---------|-----|------------------|
| MAX | `https://max.ru/u/f9LHodD0cOI8NplZUAfTNT7cDN89_7GhazWQy0u9B3AbC0ktxFkC6JWVPm0` | **PASS** |
| Telegram | `https://t.me/gruzotaxi_triumph` | **PASS** |
| WhatsApp | `https://wa.me/+79189912991` | **PASS** |

---

## 7. Footer navigation verification

| Check | Evidence | Result |
|-------|----------|--------|
| `.landing-footer__nav` in built footers | `v5-page01/landing-footer.html` included on PPC pages | **PASS** |
| Footer hash links use `#tasks`, `#pricing`, `#reviews`, `#faq`, `#contacts` | Footer partial | **PASS** |
| Same handler as header | `initLandingFooterNav()` → `bindSectionNavLinks` → `handleSectionNavigation` in `src/js/header-menu.js` | **PASS** |
| Hash stripped from URL after navigation | `stripHashFromUrl()` via `history.replaceState` on `pathname+search` | **PASS** |
| Compiled in dist | `dist/assets/js/header-menu.js` contains `initLandingFooterNav`, `handleSectionNavigation` | **PASS** |

**SAFE UNKNOWN:** Live browser confirmation that footer clicks never leave `#fragment` in the address bar was not executed in this pass (logic review + dist bundle presence only).

---

## 8. Build verification

| Step | Result |
|------|--------|
| Command | `npm run build` in `workspaces/triumph-manipulator-landing-v6` |
| Exit code | **0** |
| Duration | ~1.58s |
| `dist/backend/send-lead.php` | Present |
| `dist/backend/api/forms/send.php` | Absent |
| Default form endpoint in `dist/assets/js/form.js` | `backend/send-lead.php` |

---

## 9. Remaining known debts

- **Mobile / desktop visual QA** — not systematically executed.
- **Form / lead live mail** — spot-check beyond konteynery not confirmed for all routes.
- **Orphan partials** — route-level `final-contact-cta.html` files exist in `src/` but must stay disconnected from page graphs.
- **Source-only `hero__notice`** — remains in unused `v5-page01/screen-01-hero.html` (not in 12-route dist output).
- **`verify-final-wave-dist.mjs`** — `5-tonn` missing copy marker `Что не перевозим` (content debt, not freeze blocker).
- **`noindex` robots** — still on PPC pages until release charter changes policy.

---

## 10. Regression risks

- Running `tools/generate-ppc-rollout.mjs` without review may reintroduce `.hero__notice`, mock handlers, or duplicate contacts.
- Restoring snapshot without `npm run build` leaves no `dist/` (excluded from snapshot).
- Uncommitted V6 workspace changes are **not** in git history; filesystem snapshot is the rollback authority.
- Snapshot store may be gitignored; retention is operator-dependent.

---

## 11. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Full browser QA at breakpoints | SAFE UNKNOWN |
| Production host PHP/mailer config | SAFE UNKNOWN |
| CDN/cache behavior after deploy | SAFE UNKNOWN |
| Live mail on all 12 routes | SAFE UNKNOWN |
| Footer hash behavior in all browsers | SAFE UNKNOWN (logic verified in source + dist JS) |

---

## 12. Git status

| Field | Value |
|-------|--------|
| **HEAD** | `dc05c479eedd50233442009413fc90dbf314428f` |
| **Branch** | `mars/post-cycle8-live-tests` |
| **Commit created** | **No** |
| **Push** | **No** |
| **V6 workspace** | Many modified files under `workspaces/triumph-manipulator-landing-v6/` (contacts, messengers, footer, images) |
| **New project doc** | `projects/triumph-manipulator-landing/V6-PRODUCTION-CANDIDATE-STATE.md` (untracked) |
| **Snapshot** | Filesystem under `workspaces/_snapshots/` (typically outside git commit scope) |

---

*End of report — production candidate freeze v1*
