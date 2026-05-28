# V6 oborudovanie accepted snapshot report — v1

**Date:** 2026-05-28  
**Task:** Accepted-route freeze checkpoint for Triumph V6 `oborudovanie`  
**Snapshot ID:** `snap-20260528-triumph-v6-oborudovanie-accepted`

---

## Snapshot path

| Field | Value |
|-------|--------|
| **Relative** | `workspaces/_snapshots/snap-20260528-triumph-v6-oborudovanie-accepted/` |
| **Full** | `C:\AI MARS\workspaces\_snapshots\snap-20260528-triumph-v6-oborudovanie-accepted\` |
| **Manifest** | `SNAPSHOT-MANIFEST.md` in snapshot root |

---

## Included / excluded

**Included:** `src/`, `backend/`, `docs/`, `reports/`, `tools/`, `package.json`, `package-lock.json`, `gulpfile.js`, `README.md`

**Excluded:** `node_modules/`, `dist/`, `.cache/`, `logs/`, `tmp/`, `temp/`, `*.log`, `_backup/`, `_snapshots/`

---

## Build verification

| Check | Result |
|-------|--------|
| `npm run build` | **PASS** |
| `dist/index.html` | **PASS** |
| `dist/5-tonn.html` | **PASS** |
| `dist/bytovki.html` | **PASS** |
| `dist/konteynery.html` | **PASS** |
| `dist/oborudovanie.html` | **PASS** |
| `dist/backend/send-lead.php` | **PASS** |
| `dist/backend/api/forms/send.php` | **ABSENT (PASS)** |

---

## Oborudovanie route verification (`dist/oborudovanie.html`)

| Check | Result |
|-------|--------|
| Exactly one `id="contacts"` | **PASS** |
| No `.hero__notice` | **PASS** |
| No `data-form-handler="mock"` | **PASS** |
| No `backend/api/forms/send.php` reference | **PASS** |
| Hero cargo labels: `Торговое`, `Строительное`, `Промышленное` | **PASS** |
| Old long labels absent (`* оборудование`) | **PASS** |
| Icon classes present in `screen-icons.css` subset | **PASS** |
| `ppc-oborudovanie` CSS scope in compiled CSS | **PASS** |
| Canonical route markers (`hero__cargo-action`, showcase/transport/pricing/order/faq/contact blocks) | **PASS** |

---

## Regression check (existing calibrated routes)

| Route | Marker/contract pass |
|-------|----------------------|
| `index` | **PASS** |
| `5-tonn` | **PASS** |
| `bytovki` | **PASS** |
| `konteynery` | **PASS** |

---

## Operational notes captured at freeze

- Wrong-workspace incident was caught during rollout; work was recovered in V6 without V5 contamination for this scope.
- V5 workspace was restored clean for oborudovanie-related scope after the incident.
- Icon subset issue discovered: semantically correct Font Awesome classes may be absent from `screen-icons.css`; route rollout must verify subset membership before choosing icons.
- Future pages must run icon QA against `src/assets/vendor/fontawesome/css/screen-icons.css` before freeze.

---

## Notes

- Snapshot payload is local recovery artifact; `dist/` intentionally excluded (regenerate with `npm run build` after restore).
- This checkpoint does not start the next route rollout.
