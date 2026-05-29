# V6 after image mapping snapshot report — v1

**Date:** 2026-05-29  
**Task:** Full recovery snapshot after image mapping micro-correction  
**Snapshot ID:** `snap-20260529-triumph-v6-after-image-mapping-v1`

---

## Snapshot path

| Field | Value |
|-------|--------|
| **Relative** | `workspaces/_snapshots/snap-20260529-triumph-v6-after-image-mapping-v1/` |
| **Full** | `C:\AI MARS\workspaces\_snapshots\snap-20260529-triumph-v6-after-image-mapping-v1\` |
| **Manifest** | `SNAPSHOT-MANIFEST.md` in snapshot root |
| **Source workspace** | `workspaces/triumph-manipulator-landing-v6/` |
| **Baseline commit** | `dc05c479eedd50233442009413fc90dbf314428f` |

**v5 guard:** No paths under `workspaces/triumph-manipulator-landing-v5/` used for copy or build.

---

## Included / excluded

**Included:** `src/`, `backend/`, `docs/`, `reports/`, `tools/`, `package.json`, `package-lock.json`, `gulpfile.js`, `README.md`

**Excluded:** `node_modules/`, `dist/`, `.cache/`, `logs/`, `tmp/`, `temp/`, `*.log`, `_backup/`, `_snapshots/`

| Path | Source files | Snapshot files | Parity |
|------|-------------:|---------------:|--------|
| `src/` | 208 | 208 | PASS |
| `backend/` | 11 | 11 | PASS |
| `docs/` | 11 | 11 | PASS |
| `reports/` | 20 | 20 | PASS (initial copy; this report added post-copy to live workspace) |
| `tools/` | 6 | 6 | PASS |

Excluded directories verified absent in snapshot root.

---

## Build verification

| Step | Result |
|------|--------|
| `npm run build` (live workspace) | **PASS** (exit 0, ~1.77s) |
| `dist/backend/send-lead.php` | **PASS** (present) |
| `dist/backend/api/forms/send.php` | **PASS** (absent) |
| No `.hero__notice` in `dist/*.html` | **PASS** |
| No `data-form-handler="mock"` | **PASS** |
| No `backend/api/forms/send.php` references | **PASS** |

`dist/` intentionally excluded from snapshot; regenerate after restore.

---

## Route verification (`dist/*.html`)

All **12** route pages present:

| Route | Dist file | `#contacts` | Result |
|-------|-----------|-------------|--------|
| `index` | `dist/index.html` | 1 | **PASS** |
| `5-tonn` | `dist/5-tonn.html` | 1 | **PASS** |
| `armatura` | `dist/armatura.html` | 1 | **PASS** |
| `bytovki` | `dist/bytovki.html` | 1 | **PASS** |
| `fbs-zhbi` | `dist/fbs-zhbi.html` | 1 | **PASS** |
| `kirpich-bloki` | `dist/kirpich-bloki.html` | 1 | **PASS** |
| `konteynery` | `dist/konteynery.html` | 1 | **PASS** |
| `kray` | `dist/kray.html` | 1 | **PASS** |
| `oborudovanie` | `dist/oborudovanie.html` | 1 | **PASS** |
| `stroymaterialy` | `dist/stroymaterialy.html` | 1 | **PASS** |
| `vezdehod` | `dist/vezdehod.html` | 1 | **PASS** |
| `yurlic` | `dist/yurlic.html` | 1 | **PASS** |

---

## Image mapping verification (`dist/`)

| Route | Expected asset | Forbidden in dist | Result |
|-------|----------------|-------------------|--------|
| `index` | `second-screen-zakaz.jpg` | route-specific vezdehod/yurlic assets | **PASS** |
| `vezdehod` | `second-screen-zakaz.jpg` | `second-screen-vezdehod.jpg` | **PASS** |
| `yurlic` | `second-screen-zakaz.jpg` | `second-screen-yurlic.jpg` | **PASS** |

Source alignment (post-correction): `zakaz/screen-02-specs.html`, `vezdehod/screen-02-specs.html`, `yurlic/screen-02-specs.html` reference `second-screen-zakaz.jpg`. Index page includes `v5-ppc/zakaz/screen-02-specs.html`.

---

## Regression risks

- Pending QA may change typography, hover, or density without a new snapshot.
- Other routes may still use route-specific second-screen filenames; only index/vezdehod/yurlic mapping verified here.
- Snapshot is gitignored (`workspaces/*`); recovery depends on filesystem retention, not git history.

---

## SAFE UNKNOWN

- Full browser visual parity at breakpoints not executed in this pass.
- Production CDN/cache invalidation after restore not verified.
- Whether all 12 routes’ second-screen images are final beyond the three-route mapping check above.
