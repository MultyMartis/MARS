# V6 pre-final-rollout-wave snapshot report — v1

**Date:** 2026-05-28  
**Task:** Full stable recovery snapshot before final V6 rollout wave  
**Snapshot ID:** `snap-20260528-triumph-v6-pre-final-rollout-wave`

---

## Snapshot path

| Field | Value |
|-------|--------|
| **Relative** | `workspaces/_snapshots/snap-20260528-triumph-v6-pre-final-rollout-wave/` |
| **Full** | `C:\AI MARS\workspaces\_snapshots\snap-20260528-triumph-v6-pre-final-rollout-wave\` |
| **Manifest** | `SNAPSHOT-MANIFEST.md` in snapshot root |
| **Source workspace** | `workspaces/triumph-manipulator-landing-v6/` |
| **Baseline commit** | `5811d82eb3d8e0758d164145739a252a574f9c69` |

---

## Included / excluded

**Included:** `src/`, `backend/`, `docs/`, `reports/`, `tools/`, `package.json`, `package-lock.json`, `gulpfile.js`, `README.md`

**Excluded:** `node_modules/`, `dist/`, `.cache/`, `logs/`, `tmp/`, `temp/`, `*.log`, `_backup/`, `_snapshots/`

| Path | Source files | Snapshot files | Parity |
|------|-------------:|---------------:|--------|
| `src/` | 202 | 202 | PASS |
| `backend/` | 11 | 11 | PASS |
| `docs/` | 11 | 11 | PASS |
| `reports/` | 19 | 19 | PASS (at copy; this report added post-copy) |
| `tools/` | 4 | 4 | PASS |

Excluded directories verified absent in snapshot root.

---

## Route verification (`dist/*.html`)

Verified after `npm run build` on live workspace (dist not stored in snapshot).

| Route | Dist file | `#contacts` | `faq--split-cta` | `contact-cta--embedded` | `.hero__notice` | mock handler | legacy `send.php` ref | Canonical markers | Result |
|-------|-----------|-------------|------------------|---------------------------|-----------------|--------------|----------------------|-------------------|--------|
| `index` | `dist/index.html` | 1 | yes | yes | absent | absent | absent | all 7 | **PASS** |
| `5-tonn` | `dist/5-tonn.html` | 1 | yes | yes | absent | absent | absent | all 7 | **PASS** |
| `bytovki` | `dist/bytovki.html` | 1 | yes | yes | absent | absent | absent | all 7 | **PASS** |
| `konteynery` | `dist/konteynery.html` | 1 | yes | yes | absent | absent | absent | all 7 | **PASS** |
| `oborudovanie` | `dist/oborudovanie.html` | 1 | yes | yes | absent | absent | absent | all 7 | **PASS** |
| `fbs-zhbi` | `dist/fbs-zhbi.html` | 1 | yes | yes | absent | absent | absent | all 7 | **PASS** |

Canonical markers checked: `hero__cargo-action`, `machine-showcase__spec-panel`, `machine-transport--ops-grid`, `pricing-factors--system`, `order-steps--process`, `faq--split-cta`, `contact-cta--embedded`.

---

## Build verification

| Step | Result |
|------|--------|
| `npm run build` | **PASS** (exit 0, ~1.47s) |
| `dist/index.html` | **PASS** |
| `dist/5-tonn.html` | **PASS** |
| `dist/bytovki.html` | **PASS** |
| `dist/konteynery.html` | **PASS** |
| `dist/oborudovanie.html` | **PASS** |
| `dist/fbs-zhbi.html` | **PASS** |
| `dist/backend/send-lead.php` | **PASS** |
| `dist/backend/api/forms/send.php` | **PASS** (absent) |

---

## Pending rollout wave (not in this freeze)

Routes with source scaffolds but **not** in accepted calibration set at freeze time:

- `armatura`
- `kirpich-bloki`
- `stroymaterialy`
- `vezdehod`
- `yurlic`
- `kray`

Several pending-route hero partials still contain `.hero__notice` in `src/` — expected until each route completes rollout QA.

---

## Calibration state

Updated: `projects/triumph-manipulator-landing/V6-CALIBRATION-STATE.md` — accepted routes through `fbs-zhbi`; note added for this freeze.

---

## Regression risks

- Pending routes may reintroduce `.hero__notice` or duplicate `#contacts` if `final-contact-cta.html` is included alongside split FAQ.
- Icon subset (`screen-icons.css`) must be verified per route before freeze.
- `dist/` is not in snapshot; restore requires rebuild.
- Browser visual QA remains mandatory HITL gate (not captured in this report).

---

## SAFE UNKNOWN

- Full browser visual parity at all breakpoints (1440 / 1280 / 1025 / 1024 / 560 / 390) not executed in this freeze pass.
- Route-specific second-screen image mapping completeness not re-audited at freeze time.
