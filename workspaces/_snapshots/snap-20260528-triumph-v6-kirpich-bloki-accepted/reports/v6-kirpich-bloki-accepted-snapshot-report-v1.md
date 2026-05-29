# V6 kirpich-bloki accepted snapshot report — v1

**Date:** 2026-05-29  
**Task:** Recovery snapshot + acceptance freeze for `kirpich-bloki` route  
**Snapshot ID:** `snap-20260528-triumph-v6-kirpich-bloki-accepted`

---

## Snapshot path

| Field | Value |
|-------|--------|
| **Relative** | `workspaces/_snapshots/snap-20260528-triumph-v6-kirpich-bloki-accepted/` |
| **Full** | `C:\AI MARS\workspaces\_snapshots\snap-20260528-triumph-v6-kirpich-bloki-accepted\` |
| **Manifest** | `SNAPSHOT-MANIFEST.md` in snapshot root |
| **Source workspace** | `workspaces/triumph-manipulator-landing-v6/` |
| **Baseline commit** | `781258f38206ffbfbe2241471148832fd590753e` |

---

## Included / excluded

**Included:** `src/`, `backend/`, `docs/`, `reports/`, `tools/`, `package.json`, `package-lock.json`, `gulpfile.js`, `README.md`

**Excluded:** `node_modules/`, `dist/`, `.cache/`, `logs/`, `tmp/`, `temp/`, `*.log`, `_backup/`, `_snapshots/`

| Path | Source files | Snapshot files | Parity |
|------|-------------:|---------------:|--------|
| `src/` | 204 | 204 | PASS |
| `backend/` | 11 | 11 | PASS |
| `docs/` | 11 | 11 | PASS |
| `reports/` | 20 | 20 | PASS (at copy; this report added post-copy) |
| `tools/` | 6 | 6 | PASS |

---

## Build verification

| Step | Result |
|------|--------|
| `npm run build` | **PASS** (exit 0, ~1.48s) |
| `dist/kirpich-bloki.html` | **PASS** |
| `dist/backend/send-lead.php` | **PASS** (present) |
| `dist/backend/api/forms/send.php` | **PASS** (absent) |

---

## Route verification (`dist/*.html`)

Verified after `npm run build` on live workspace (dist not stored in snapshot).

Literal `Что не перевозим` check fails on routes using `Что не&nbsp;перевозим` (parity-equivalent per calibration lessons). Normalized result below.

| Route | Dist file | `#contacts` x1 | split FAQ + embedded CTA | anti-patterns | canonical markers | fixed titles (normalized) | Result |
|-------|-----------|----------------|--------------------------|---------------|-------------------|---------------------------|--------|
| `index` | `dist/index.html` | n/a | n/a | n/a | n/a | n/a | **PASS** (exists) |
| `5-tonn` | `dist/5-tonn.html` | 1 | yes | clean | all 5 | yes (`&nbsp;` variant) | **PASS** |
| `bytovki` | `dist/bytovki.html` | 1 | yes | clean | all 5 | yes | **PASS** |
| `konteynery` | `dist/konteynery.html` | 1 | yes | clean | all 5 | yes | **PASS** |
| `oborudovanie` | `dist/oborudovanie.html` | 1 | yes | clean | all 5 | yes | **PASS** |
| `fbs-zhbi` | `dist/fbs-zhbi.html` | 1 | yes | clean | all 5 | yes | **PASS** |
| `armatura` | `dist/armatura.html` | 1 | yes | clean | all 5 | yes | **PASS** |
| `kirpich-bloki` | `dist/kirpich-bloki.html` | 1 | yes | clean | all 5 | yes | **PASS** |

Anti-patterns checked: `.hero__notice`, `data-form-handler="mock"`, `backend/api/forms/send.php` reference.

Canonical markers: `hero__cargo-action`, `machine-showcase__spec-panel`, `machine-transport--ops-grid`, `pricing-factors--system`, `order-steps--process`.

---

## Kirpich-bloki specific QA

| Check | Result |
|-------|--------|
| FAQ title `Частые вопросы` | **PASS** |
| Denied block title `Что не перевозим` (tasks screen) | **PASS** |
| `ppc-kirpich-bloki` CSS admission in built `style.css` | **PASS** |
| Hero cargo `fas fa-*` ⊆ `screen-icons.css` | **PASS** (no missing icons) |
| No legacy scaffold markers in route partials | **PASS** |
| No standalone `final-contact-cta` wired in page/dist | **PASS** |

---

## Calibration state

Updated: `projects/triumph-manipulator-landing/V6-CALIBRATION-STATE.md` — `kirpich-bloki` added to accepted routes.

---

## Regression risks

- Orphan `final-contact-cta.html` remains in `src/partials/.../kirpich-bloki/` but is not included; future edits must not wire it alongside split FAQ.
- `verify-final-wave-dist.mjs` literal title check can false-fail `5-tonn` (`&nbsp;` variant).
- `dist/` not in snapshot; restore requires rebuild.
- Browser visual QA remains mandatory HITL gate.

---

## SAFE UNKNOWN

- Full browser visual parity at all breakpoints not executed in this freeze pass.
- Route-specific second-screen image mapping completeness not re-audited at freeze time.
