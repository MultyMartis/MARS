# REPORT — WPilot TEST-01: Clean Install Proof

**Date:** 2026-06-19  
**Task:** TEST-01 — Clean Install Proof (final gate before Sprint 3)  
**Baseline:** Variant B — checkpoint `8c67478` + UX-01  
**Release target:** `metacode-wpilot` v0.3.0-RC1  
**Operator:** Cursor agent (human-supervised)

---

## Executive Summary

| Phase | Scope | Result |
|-------|-------|--------|
| 1 | RC1 ZIP package build | **PASS** |
| 2 | Localization compile (`.mo`) | **PASS** |
| 3 | Disposable install target | **FAIL** — no qualifying instance available |
| 4 | Clean ZIP install + activation | **FAIL** — RC1 on DEV (`dev.gktriumph.ru`); see [RC1 Install Failure](#rc1-install-failure-dev-operator-attempt) |
| 5 | Runtime verification (post-install) | **NOT EXECUTED** |
| 6 | Optional smoke (backup) | **NOT EXECUTED** |
| 7 | Classification | **PARTIAL** |

**Gate verdict:** **PARTIAL** — RC2 package built and validated; **RC1 ZIP install on DEV failed** (collision with prior FTP deploy). **C — Clean Install Proven** is **not** met. Sprint 3 must **not** start on this evidence alone.

---

## Phase 1 — Build RC1 Package

### Artifact

| Field | Value |
|-------|-------|
| **ZIP path** | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc1.zip` |
| **Inventory** | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc1.inventory.json` |
| **SHA-256** | `d89411e81befb629bb28b67ddb3129fbb5801665643ab638a31cc1c82f275237` |
| **Size** | 48,722 bytes |
| **Root folder** | `metacode-wpilot/` |
| **File count** | **26** (25 source + compiled `.mo`) |
| **Bootstrap** | `metacode-wpilot/metacode-wpilot.php` — present |
| **UX-01 files** | `admin/class-wpilot-admin-ui-model.php`, `languages/*` — present |
| **Excluded** | `.git`, reports, backups, tokens, evidence, temp files — confirmed absent |

### Source tree

```
projects/wpilot/plugin/metacode-wpilot/
```

### Package inventory (26 files)

| # | Path |
|---|------|
| 1 | `metacode-wpilot/metacode-wpilot.php` |
| 2 | `metacode-wpilot/README.md` |
| 3–4 | `admin/class-wpilot-admin-page.php`, `admin/class-wpilot-admin-ui-model.php` |
| 5–22 | `includes/class-wpilot-*.php` (18 service/runtime files) |
| 23–25 | `languages/metacode-wpilot.pot`, `metacode-wpilot-ru_RU.po`, `metacode-wpilot-ru_RU.mo` |
| 26 | *(count includes all listed; see inventory JSON for canonical list)* |

Full file list: see `metacode-wpilot-v0.3.0-rc1.inventory.json`.

### Verification checks

| Check | Result |
|-------|--------|
| ZIP opens | ✓ |
| Root folder `metacode-wpilot/` | ✓ |
| `metacode-wpilot.php` exists | ✓ |
| Expected file count (25 + `.mo`) | ✓ 26 |
| No secrets in archive | ✓ (manual tree review) |

**Phase 1 result:** **PASS**

---

## Phase 2 — Localization Compile

| Field | Value |
|-------|-------|
| **Tool** | Python 3.14 + `polib` (`py -m pip install polib`) |
| **Input** | `languages/metacode-wpilot-ru_RU.po` |
| **Output** | `languages/metacode-wpilot-ru_RU.mo` (9,502 bytes) |
| **Included in RC1 ZIP** | Yes |
| **`msgfmt` / `wp i18n`** | Not available on operator machine |

**Phase 2 result:** **PASS** (compiled via `polib`; not hand-authored)

---

## Phase 3 — Disposable Install Target

### Requirement

Disposable WordPress: not production, not client live site, **not previously used as WPilot proof environment**.

### Environment survey

| Candidate | Role | Qualifies? | Reason |
|-----------|------|------------|--------|
| `https://dev.gktriumph.ru` | Known DEV/test WP (Beget) | **No** | Primary WPilot proof environment (FTP deploy + runtime sprints); plugin already installed |
| `https://gktriumph.polygon-ws.ru` | Historical staging GUID host | **SAFE UNKNOWN** | Not reachable from operator network during TEST-01 (`curl` exit 6) |
| Local Docker / LocalWP / XAMPP | Local disposable WP | **No** | `docker`, `php`, `wp` CLI not available on operator machine |
| Fresh Beget subdomain | New disposable instance | **Not provisioned** | No credentials or provisioning path in scope for TEST-01 |

### Reference environment (excluded from install proof)

Documented for operator context only — **not** used as TEST-01 install target:

| Field | Value (reference) |
|-------|-------------------|
| **URL** | `https://dev.gktriumph.ru` |
| **WordPress** | REST API active; `wpilot/v1` namespace registered (prior FTP install) |
| **PHP version** | **SAFE UNKNOWN** — not captured in TEST-01 (no `site-info` token probe on disposable target) |
| **Theme** | The7 + child (`dt-the7`, `dt-the7-child`) — from prior DEV evidence |
| **Plugins** | Multiple (Yoast, Contact Form 7, Popup Maker, WPBakery, WPilot, etc.) — from prior DEV `wp-json` namespace list |
| **WPilot state** | Installed via **FTP** (not RC1 ZIP); ping returns `0.3.0` bridge active |

**Phase 3 result:** **FAIL** — no disposable WordPress instance available for ZIP-only clean install.

---

## Phase 4 — Clean Install

**Status:** **NOT EXECUTED**

**Blockers:**

1. No disposable WordPress with `manage_options` admin access in agent reach.
2. WordPress plugin ZIP upload requires authenticated **wp-admin** session (Plugins → Upload Plugin) — not automatable without admin credentials.
3. Task restriction: **ZIP only, not FTP** — cannot substitute FTP deploy on `dev.gktriumph.ru` as install proof.

| Step | Result |
|------|--------|
| Install ZIP via WP admin | NOT EXECUTED |
| Activate plugin | NOT EXECUTED |
| Open admin page | NOT EXECUTED |
| Open settings page | NOT EXECUTED |

---

## Phase 5 — Runtime Verification

**Status:** **NOT EXECUTED** (depends on Phase 4 clean install)

| Endpoint | Post-install check |
|----------|-------------------|
| `GET /ping` | NOT EXECUTED on clean install |
| `GET /site-info` | NOT EXECUTED |
| `GET /plugins` | NOT EXECUTED |
| `GET /pages` | NOT EXECUTED |
| Backup route discovery | NOT EXECUTED |

**Reference only (prior FTP install on dev — does not satisfy TEST-01):** `GET https://dev.gktriumph.ru/wp-json/wpilot/v1/ping` returned HTTP 200 with `plugin: metacode-wpilot`, `status: installed` during package build window.

---

## Phase 6 — Optional Runtime Smoke

**Status:** **NOT EXECUTED** — skipped (no clean install; writes not in scope without install proof).

---

## Phase 7 — Result Classification

### Criteria matrix

| Criterion | Required for PASS | TEST-01 |
|-----------|-------------------|---------|
| ZIP install works | Yes | **Not proven** |
| Activation works | Yes | **Not proven** |
| Schema bootstrap | Yes | **Not proven** on clean DB |
| REST surface | Yes | **Not proven** on clean install |
| Admin UI (UX-01) | Yes | **Not proven** on clean install |
| Localization foundation | Informational | **PASS** (`.po` + compiled `.mo` in package) |
| RC1 package integrity | Prerequisite | **PASS** |

### Classification

**PARTIAL**

- **Package layer:** RC1 ZIP built, verified, inventoried; `.mo` compiled and included.
- **Install layer:** Clean WordPress ZIP install path **not executed** — gate to Sprint 3 **not cleared**.

Release readiness remains:

| Level | Status |
|-------|--------|
| B — RC Ready | **Current** (package now built) |
| C — Clean Install Proven | **Not met** |

---

## Deliverables

| Deliverable | Path | Status |
|-------------|------|--------|
| TEST-01 report | `projects/wpilot/reports/wpilot-test-01-clean-install-proof.md` | Created |
| RC1 ZIP | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc1.zip` | Created |
| Package inventory | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc1.inventory.json` | Created |
| Evidence bundle | `C:\AI MARS STORAGE\wpilot\clean-install\test-01-20260619\` | Created |
| RC1 doc update | `WPILOT-RELEASE-CANDIDATE-v0.3.0-RC1.md` | Updated |
| PROVEN-CAPABILITIES update | `WPILOT-PROVEN-CAPABILITIES-v1.md` | **Not updated** (proof not succeeded) |

---

## Changed Files (TEST-01)

| Path | Change |
|------|--------|
| `projects/wpilot/reports/wpilot-test-01-clean-install-proof.md` | Created |
| `projects/wpilot/WPILOT-RELEASE-CANDIDATE-v0.3.0-RC1.md` | Updated — Clean Install Status |
| `projects/wpilot/plugin/metacode-wpilot/languages/metacode-wpilot-ru_RU.mo` | Generated (compile artifact) |
| `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc1.zip` | Created |
| `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc1.inventory.json` | Created |
| `C:\AI MARS STORAGE\wpilot\clean-install\test-01-20260619\` | Evidence copy |

---

## UNKNOWN

| Item | What would verify |
|------|-------------------|
| WordPress / PHP version on disposable target | Provision disposable WP; read Site Health or `site-info` after install |
| ru_RU runtime UI on clean install | Install RC1 on `ru_RU` locale WP; open WPilot settings with `.mo` in package |
| ZIP upload on Beget shared hosting | Operator wp-admin upload of RC1 ZIP on fresh disposable subdomain |

---

## SECURITY RISK

| Signal | Level | Note |
|--------|-------|------|
| RC1 ZIP contents | Low | No tokens/secrets in package (tree review) |
| FTP credentials in STORAGE scripts | **Medium** | `secure-recovery/dev.gktriumph.ru/*.py` contain live FTP credentials outside git — operator hygiene; not introduced by TEST-01 |
| Using `dev.gktriumph.ru` as install proxy | N/A | Correctly excluded — would not prove clean install |

---

## Next Operator Actions (to reach PASS)

1. Provision **fresh disposable** WordPress (new subdomain or local stack with PHP + MySQL).
2. Upload `metacode-wpilot-v0.3.0-rc1.zip` via **Plugins → Add New → Upload Plugin** only.
3. Activate; verify schema tables; run REST checklist from [WPILOT-CLEAN-INSTALL-TEST-PLAN-v1.md](../WPILOT-CLEAN-INSTALL-TEST-PLAN-v1.md).
4. Record evidence under `C:\AI MARS STORAGE\wpilot\clean-install\<site>\<timestamp>\`.
5. Re-run TEST-01 classification; update RC1 to **C — Clean Install Proven** only on full PASS.

**Do not start Sprint 3 until PASS.**

---

## RC1 Install Failure (DEV operator attempt)

**Date:** 2026-06-19  
**Target:** `https://dev.gktriumph.ru`  
**Package:** `metacode-wpilot-v0.3.0-rc1.zip`

### Status

**FAIL for RC1 packaging / install path** — operator ZIP install on DEV did not complete activation. TEST-01 gate remains **PARTIAL**; **C — Clean Install Proven** is **not** met.

### Observed symptoms

| # | Symptom |
|---|---------|
| 1 | WordPress upload reported install success |
| 2 | Activation failed: «Файл плагина не найден.» |
| 3 | Plugins list showed **two** MetaCODE WPilot entries |
| 4 | Deleting inactive plugin in WP Admin appeared successful; entry returned after refresh |
| 5 | Manual deletion of plugin folder on hosting did not clear ghost registry |
| 6 | Reinstalling same RC1 ZIP reproduced activation failure |

### Forensic — RC1 ZIP on disk (agent re-inspection)

| Check | RC1 artifact |
|-------|----------------|
| Root folder | `metacode-wpilot/` only (single root) |
| Bootstrap | `metacode-wpilot/metacode-wpilot.php` present |
| Nested `metacode-wpilot/metacode-wpilot/` | **Absent** |
| Versioned parent `metacode-wpilot-v0.3.0-rc1/` | **Absent** |
| Backslash paths | **Absent** |
| File count | 26 |
| SHA-256 | `d89411e81befb629bb28b67ddb3129fbb5801665643ab638a31cc1c82f275237` |

**Structural verdict:** RC1 ZIP tree matches WordPress plugin packaging spec locally. Archive is **not** invalid due to nested-folder or versioned-root defects.

### Cause (forensic conclusion)

**Primary:** Install-state collision on DEV — site already had WPilot deployed via **FTP** (`metacode-wpilot/metacode-wpilot.php`). ZIP upload on a non-clean plugins directory produced **duplicate plugin registrations** and **orphaned/ghost entries** after partial folder deletes. Activation targeted a path whose files were removed or mismatched.

**Contributing:** Operator cleanup removed one folder copy but not all suffix/nested variants; WordPress plugin scanner re-listed surviving or partial trees on refresh.

**Not proven:** Whether operator uploaded a different byte-identical artifact than STORAGE RC1 (no on-host ZIP hash captured).

### Plugin basename analysis

| Field | Value |
|-------|-------|
| WordPress plugin slug (folder) | `metacode-wpilot` |
| Main plugin file | `metacode-wpilot.php` |
| Registered path | `metacode-wpilot/metacode-wpilot.php` |
| Plugin Name (header) | MetaCODE WPilot |
| Text Domain | `metacode-wpilot` |
| Domain Path | `/languages` |

Header is compatible with folder layout `metacode-wpilot/metacode-wpilot.php`. Failure was not caused by header/folder name mismatch in the source package.

### Next package

| Field | Value |
|-------|-------|
| **Package** | `metacode-wpilot-v0.3.0-rc2.zip` |
| **Path** | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc2.zip` |
| **Inventory** | `metacode-wpilot-v0.3.0-rc2.inventory.json` |
| **Cleanup runbook** | [wpilot-zip-install-cleanup-runbook.md](wpilot-zip-install-cleanup-runbook.md) |

**Operator action:** Full plugins-folder cleanup per runbook, then RC2 ZIP upload only. Do **not** mark TEST-01 PASS until RC2 install + activation + runtime checks succeed.

### TEST-01 gate after RC1 failure

| Criterion | Status |
|-----------|--------|
| RC1 ZIP structural build | PASS (local tree) |
| RC1 ZIP install on DEV | **FAIL** |
| RC2 ZIP built + validated | PASS (see inventory) |
| RC2 install proof | **NOT EXECUTED** |
| Sprint 3 | **BLOCKED** |
