# ISEO-SU WPILOT PACKAGE AUDIT v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-PHASE-4B-WPILOT-PREINSTALL-PACKAGE-AND-COMPATIBILITY-GATE  
**Date:** 2026-07-24  
**Mode:** Static package validation only — **no install, upload, activation, token, or REST**

---

## 1. Audit Status

| Field | Value |
|-------|-------|
| **Status** | **COMPLETE** |
| **Package classification** | **ACCEPTED MATCH** |
| **Canonical ZIP** | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc5.zip` |
| **SHA-256 (recomputed)** | `43c71a561872a037f294a12d5194d0925e988392599f02c1eeb2d8b1c52e1577` |
| **Source tree** | `X:\AI MARS\projects\wpilot\plugin\metacode-wpilot\` |
| **Source↔ZIP** | **27/27 files identical** (path, length, per-file SHA-256) |
| **ZIP created/modified this task** | **No** (read-only hash + inventory) |

---

## 2. Authority Sources

| Source | Role |
|--------|------|
| `projects/wpilot/OPERATIONAL-INDEX.md` | RC5 authority + version labels |
| `WPILOT-FINAL-STATE-RC5.md` / `WPILOT-AUTHORITY-STATE-RC5.md` | Freeze authority |
| `WPILOT-RELEASE-CANDIDATE-v0.3.0-RC5.md` | Package path + SHA-256 |
| `manifests/metacode-wpilot-v0.3.0-rc5-deploy.json` | Deploy manifest (Storage path + hash) |
| `reports/wpilot-fp0002-dev-runtime-reconciliation-2026-07-02.md` | Brain↔RC5 EXACT equivalence |
| `WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md` | Install packaging expectations |
| Inventory sibling | `metacode-wpilot-v0.3.0-rc5.inventory.json` (Storage) |

Historical path strings in older docs may still say `C:\AI MARS STORAGE\...`. Current X-drive authority maps the accepted package to **`X:\AI MARS STORAGE\wpilot\deploy-packages\`**.

---

## 3. Version Reconciliation

| Authority | Label | Classification |
|-----------|-------|----------------|
| OPERATIONAL-INDEX release candidate | `v0.3.0-RC5` | Canonical RC label |
| OPERATIONAL-INDEX plugin version | `0.3.0` (schema `0.2.0`) | Canonical runtime version |
| Plugin header `Version:` | `0.3.0` | Matches constants |
| `WPilot_Constants::VERSION` | `0.3.0` | Matches header |
| `WPilot_Constants::SCHEMA_VERSION` | `0.2.0` | Matches index |
| Package filename | `metacode-wpilot-v0.3.0-rc5.zip` | RC5 packaging label (not identical string to `0.3.0`) |
| Inventory / deploy SHA-256 | `43c71a56…1577` | Matches recomputed hash |
| Accepted REPORT evidence | RC5 freeze + FP-0002 reconciliation | Supports ACCEPTED MATCH |

**Discrepancy (documented, not normalized):** package/RC filename uses `v0.3.0-rc5` / `RC5`; plugin header and `WPILOT_VERSION` use `0.3.0` without RC suffix. This is **expected** under current WPilot authority and is **not** a package mismatch.

---

## 4. Canonical Source

| Field | Value |
|-------|-------|
| **Path** | `X:\AI MARS\projects\wpilot\plugin\metacode-wpilot\` |
| **Main file** | `metacode-wpilot.php` |
| **File count** | 27 (matches ZIP) |
| **Modified this task** | **No** |

---

## 5. Package Candidates

| Candidate | Location | SHA-256 | Classification |
|-----------|----------|---------|----------------|
| `metacode-wpilot-v0.3.0-rc5.zip` | `X:\AI MARS STORAGE\wpilot\deploy-packages\` | `43c71a561872a037f294a12d5194d0925e988392599f02c1eeb2d8b1c52e1577` | **CANONICAL ACCEPTED** |
| Same ZIP (cache) | `X:\MARS-Localhost\storage\packages\wpilot\` | identical | Mirror cache (read-only confirmed) |
| `metacode-wpilot-v0.3.0.zip` | Storage deploy-packages | `6309dd8157b93c3ba174101d35b45af47af0dc7d64236e939d5e913359c3771c` | **STALE** (pre-UX-01; 22-file era) |
| `metacode-wpilot-v0.3.0-rc1`…`rc4.zip` | Storage deploy-packages | (not recomputed as candidates) | **SUPERSEDED** packaging history |
| Fresh Brain rebuild ZIP | — | — | **NOT CREATED** this task |

No newer-than-RC5 accepted release package was found under documented WPilot deploy-package authority.

---

## 6. Canonical Package

| Field | Value |
|-------|-------|
| **Filename** | `metacode-wpilot-v0.3.0-rc5.zip` |
| **Bytes** | 54863 |
| **Entries** | 27 files |
| **Root folder** | single `metacode-wpilot/` |
| **Bootstrap** | `metacode-wpilot/metacode-wpilot.php` present |
| **Inventory JSON** | present beside ZIP; `valid: true` |

---

## 7. SHA-256

| Check | Result |
|-------|--------|
| Recomputed ZIP SHA-256 | `43c71a561872a037f294a12d5194d0925e988392599f02c1eeb2d8b1c52e1577` |
| Deploy manifest / RC5 docs | identical |
| Localhost package cache | identical |
| Stale `v0.3.0.zip` | different (`6309dd81…771c`) — do not use |

---

## 8. Archive Inventory

All paths use `/`. Single root `metacode-wpilot/`.

| Path |
|------|
| `metacode-wpilot/metacode-wpilot.php` |
| `metacode-wpilot/README.md` |
| `metacode-wpilot/admin/class-wpilot-admin-page.php` |
| `metacode-wpilot/admin/class-wpilot-admin-ui-model.php` |
| `metacode-wpilot/includes/class-wpilot-*.php` (21 includes) |
| `metacode-wpilot/languages/metacode-wpilot.pot` |
| `metacode-wpilot/languages/metacode-wpilot-ru_RU.po` |
| `metacode-wpilot/languages/metacode-wpilot-ru_RU.mo` |

No `node_modules`, no `.git`, no `.env`, no token files observed in inventory/secret scan field of sibling inventory JSON (`secret_scan_hits: []`).

---

## 9. Source-to-Package Comparison

| Metric | Result |
|--------|--------|
| Source-only files | 0 |
| ZIP-only files | 0 |
| Content hash mismatches | 0 |
| Exact match | **Yes — ACCEPTED MATCH** |

---

## 10. Package Safety Checks

| Check | Result |
|-------|--------|
| Single root folder `metacode-wpilot/` | PASS |
| Main plugin file present | PASS |
| Paths use `/` not `\` | PASS |
| No path traversal (`..`) | PASS |
| No absolute paths | PASS |
| No nested duplicate plugin folder | PASS |
| No unexpected build artifacts | PASS |
| Sensitive files in ZIP | none detected in bounded scan |
| Exact Brain source match | PASS |

---

## 11. Conflicts

| Conflict | Severity | Mitigation |
|----------|----------|------------|
| Stale `metacode-wpilot-v0.3.0.zip` still present in Storage | Medium (operator mix-up) | Use **only** `…-rc5.zip` + verify SHA-256 before upload |
| Historical `C:\…` path strings in older WPilot docs | Low | Prefer `X:\AI MARS STORAGE\…` per X-drive authority |
| Version string `0.3.0` vs filename `v0.3.0-rc5` | Low (documentation) | Do not normalize; cite both |

---

## 12. Decision

**Package gate input:** **ACCEPTED MATCH** for `metacode-wpilot-v0.3.0-rc5.zip`.

Overall Phase 4B pre-install decision is recorded in the REPORT as **CONDITIONAL GO** (compatibility / backup / HITL conditions — not package divergence).

---

## 13. SAFE UNKNOWN

| Item | Note |
|------|------|
| Whether operator will copy from Storage vs Localhost cache | Either OK if SHA-256 matches |
| Whether Beget / WP uploader will rewrite ZIP internals | Validate post-upload folder inventory in GATE 6A |
| Full professional malware scan of ZIP | Not performed; bounded inventory + source equivalence only |

---

*Package audit v1 · 2026-07-24 · no production access · ZIP not modified.*
