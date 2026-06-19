# WPilot Release Candidate — v0.3.0-RC1

**Classification:** Release candidate specification — no roadmap, no Sprint 3, no new endpoints.  
**Date:** 2026-06-19  
**Status:** RC1 package built (TEST-01) — clean install **not proven** (PARTIAL).  
**Plugin slug:** `metacode-wpilot`

---

## Version

| Field | Value |
|-------|-------|
| **Release label** | `v0.3.0-RC1` |
| **Plugin version** | `0.3.0` |
| **Schema version** | `0.2.0` |
| **Text domain** | `metacode-wpilot` |
| **REST namespace** | `wpilot/v1` |
| **Runtime maturity** | `proven_content_writes` |
| **Environment scope** | DEV only — human-supervised |

**Version sources (must match in RC package):**

- `metacode-wpilot.php` header → `Version: 0.3.0`
- `WPilot_Constants::VERSION` → `0.3.0`
- `WPilot_Constants::SCHEMA_VERSION` → `0.2.0`

---

## Schema

**DB tables** (`WPilot_Schema::maybe_upgrade()` on `plugins_loaded`):

| Table | Purpose |
|-------|---------|
| `{prefix}wpilot_backups` | `page.post_content` backup snapshots |
| `{prefix}wpilot_audit_log` | Sanitized lifecycle audit events |

**Options** (`WPilot_Settings`):

- Bridge flags: `bridge_enabled`, `write_enabled`, `dev_test_confirmed`, `emergency_disabled`
- Token hash only (no plaintext persistence in DB)
- Schema version marker

---

## Checkpoint

| Field | Value |
|-------|-------|
| **Runtime checkpoint** | `8c67478` — `feat(wpilot): freeze v0.3.0 proven runtime` |
| **State freeze** | [WPILOT-STATE-FREEZE-2026-06-19-v1.md](WPILOT-STATE-FREEZE-2026-06-19-v1.md) |
| **UX-01** | Completed in working tree; uncommitted atop `8c67478` at OPS-02 time |
| **Baseline decision** | [reports/wpilot-ops-02-baseline-decision.md](reports/wpilot-ops-02-baseline-decision.md) — **Variant B** |

---

## Release Baseline

**Canonical RC1 source tree:**

```
projects/wpilot/plugin/metacode-wpilot/   (25 files)
```

**Definition:** checkpoint `8c67478` **+ UX-01** (admin UI alignment + localization foundation).

**Not in RC1 scope:** Sprint 3, new REST routes, schema changes, auth changes, production deploy.

**Legacy ZIP (pre-RC1, Variant A only):**

- Path: `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0.zip`
- Size: 36,556 bytes (2026-06-19)
- Files: 22 — **stale** relative to RC1 baseline

---

## File Inventory

**Total:** 26 files in RC1 ZIP (25 source + compiled `.mo`). **No stray/debug/secret files** identified in plugin tree (OPS-02 verification).

### Core Runtime (9)

| File | Role |
|------|------|
| `metacode-wpilot.php` | Bootstrap, hooks, requires |
| `includes/class-wpilot-plugin.php` | Singleton, schema upgrade, textdomain, hooks |
| `includes/class-wpilot-constants.php` | Version, schema, maturity, endpoint counts |
| `includes/class-wpilot-settings.php` | Options, token, activation |
| `includes/class-wpilot-environment.php` | DEV/environment guards |
| `includes/class-wpilot-errors.php` | Error envelopes |
| `includes/class-wpilot-response.php` | Success envelopes |
| `includes/class-wpilot-request-context.php` | Request metadata |
| `includes/class-wpilot-operation-id.php` | Operation ID generation |

### Admin UI (2)

| File | Role |
|------|------|
| `admin/class-wpilot-admin-page.php` | Settings admin UI (UX-01 aligned) |
| `admin/class-wpilot-admin-ui-model.php` | Display-only UI data model **(UX-01)** |

### Localization (3)

| File | Role |
|------|------|
| `languages/metacode-wpilot.pot` | Translation template **(UX-01)** |
| `languages/metacode-wpilot-ru_RU.po` | Russian catalog — 78 msgids **(UX-01)** |
| `languages/metacode-wpilot-ru_RU.mo` | Compiled Russian catalog **(TEST-01)** |

### Runtime Services (9)

| File | Role |
|------|------|
| `includes/class-wpilot-audit-service.php` | Audit log writes |
| `includes/class-wpilot-auth.php` | Token auth guards |
| `includes/class-wpilot-backup-service.php` | Backup create |
| `includes/class-wpilot-checksum.php` | SHA-256 checksums |
| `includes/class-wpilot-dry-run.php` | Dry-run analysis |
| `includes/class-wpilot-rollback-service.php` | Rollback execute |
| `includes/class-wpilot-scoped-replace-service.php` | Scoped replace execute |
| `includes/class-wpilot-site-reader.php` | Read endpoint data |
| `includes/class-wpilot-wpbakery-detector.php` | WPBakery signals |

### REST (1)

| File | Role |
|------|------|
| `includes/class-wpilot-rest-controller.php` | Route registration — 12 routes |

### Schema (1)

| File | Role |
|------|------|
| `includes/class-wpilot-schema.php` | DB schema upgrade |

### Operator documentation (1)

| File | Role |
|------|------|
| `README.md` | Plugin operator readme (minor copy lag vs v0.3.0 writes in step 5) |

### Extraneous files

**None.** No `.bak`, `.tmp`, `.log`, evidence JSON, secrets, or reports inside plugin tree.

---

## Runtime Inventory

Formal plugin REST proven on DEV (`https://dev.gktriumph.ru`) — see [WPILOT-PROVEN-CAPABILITIES-v1.md](WPILOT-PROVEN-CAPABILITIES-v1.md), [reports/wpilot-runtime-inventory-v0.3.0.md](reports/wpilot-runtime-inventory-v0.3.0.md).

| Capability | Mechanism |
|------------|-----------|
| `inspect` | Read REST (`site-info`, `pages`, `structure`, etc.) |
| `backup` | `POST /pages/{id}/backups` |
| `rollback` | `POST /pages/{id}/rollback` |
| `validate` | Post-write / post-rollback checksum verification |
| `apply_content_change` | `POST /pages/{id}/scoped-replace` (exact once, `post_content`) |
| Audit trail | `wpilot_audit_log` per `operation_id` |
| Checksum pipeline | `sha256:` on inspect, backup, apply, rollback |
| Dry-run analysis | `POST /pages/{id}/replace-text/dry-run` |
| WPBakery-safe recovery | Full `post_content` restore with shortcode integrity |

| Field | Value |
|-------|-------|
| **Maturity level** | `proven_content_writes` |
| **Write primitive** | Scoped exact-once replace on `page.post_content` only |
| **Deploy proven** | FTP upload of plugin source |
| **Deploy not proven** | WordPress ZIP clean install |

---

## Endpoint Inventory

Namespace: `/wp-json/wpilot/v1/` — **12 registered routes**

| # | Method | Route | Category | Auth |
|---|--------|-------|----------|------|
| 1 | GET | `/ping` | Read | Public |
| 2 | GET | `/site-info` | Read | Token + bridge |
| 3 | GET | `/themes` | Read | Token + bridge |
| 4 | GET | `/plugins` | Read | Token + bridge |
| 5 | GET | `/pages` | Read | Token + bridge |
| 6 | GET | `/pages/{id}` | Read | Token + bridge |
| 7 | GET | `/pages/{id}/structure` | Read | Token + bridge |
| 8 | GET | `/indexing-state` | Read | Token + bridge |
| 9 | POST | `/pages/{id}/replace-text/dry-run` | Analysis | Token + bridge + DEV + write_enabled |
| 10 | POST | `/pages/{id}/backups` | Proven write | Token + bridge + DEV + schema |
| 11 | POST | `/pages/{id}/scoped-replace` | Proven write | Token + bridge + DEV + write_enabled + schema |
| 12 | POST | `/pages/{id}/rollback` | Proven write | Token + bridge + DEV + write_enabled + schema |

**Counts (admin surface):** 8 read + 1 analysis + 3 proven write = 12 total.

---

## Known Limitations

| Limitation | Detail |
|------------|--------|
| DEV only | All sprint evidence on `dev.gktriumph.ru` |
| Single write primitive | `page.post_content` exact-once scoped replace only |
| No menu/widget/CSS plugin writes | Not implemented |
| No regex / mass replace | Not implemented |
| No production proof | Explicit boundary |
| No multisite proof | Single instance only |
| No autonomous execution | Human-supervised operator workflow |
| FTP deploy proven; ZIP not | Packaging exists; clean install not executed |
| **Localization on clean install** | `.mo` in RC1 ZIP; ru_RU runtime UI on fresh WP — **not proven** (TEST-01) |
| UX-01 uncommitted | Working tree diverges from checkpoint ZIP and git HEAD |
| Plugin README drift | Install step 5 still mentions "read-only bridge" |
| RC ZIP built; clean install not proven | TEST-01 PARTIAL — see Clean Install Status |

---

## Not Yet Proven Surface

| Surface | Status |
|---------|--------|
| WordPress ZIP clean install | Not proven |
| Deploy reproducibility on fresh WP | Not proven |
| `metacode-wpilot-ru_RU.mo` deploy path on clean WP | Not proven (in RC1 ZIP only) |
| RC1 ZIP package | **Built** — TEST-01 |
| RC1 clean install on disposable WP | **Not proven** — TEST-01 |
| Production environment | Not proven |
| Menu / widget / footer / CSS plugin REST writes | Not proven |
| Autonomous agent execution | Not proven |
| Sprint 3 features | Out of scope |

---

## Clean Install Status (TEST-01 — 2026-06-19)

| Field | Value |
|-------|-------|
| **Test report** | [reports/wpilot-test-01-clean-install-proof.md](reports/wpilot-test-01-clean-install-proof.md) |
| **Classification** | **PARTIAL** |
| **RC1 ZIP built** | Yes |
| **ZIP path** | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc1.zip` |
| **SHA-256** | `d89411e81befb629bb28b67ddb3129fbb5801665643ab638a31cc1c82f275237` |
| **File count** | 26 (25 source + `.mo`) |
| **`.mo` compiled** | Yes (`polib`) |
| **Disposable WP located** | No |
| **ZIP install executed** | No |
| **Activation / schema / REST / admin UI on clean WP** | Not proven |
| **Release gate** | **B — RC Ready** (unchanged); **C — Clean Install Proven** not met |
| **Sprint 3** | **Blocked** until full PASS |

---

## RC1 Package (built — TEST-01)

**Artifact:** `metacode-wpilot-v0.3.0-rc1.zip`

**Inventory:** `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc1.inventory.json`

**Root folder:** `metacode-wpilot/`

**Includes:** all 25 source files + compiled `languages/metacode-wpilot-ru_RU.mo` (26 total).

**Must NOT include:** secrets, tokens, STORAGE evidence, debug dumps, `.git`, parent repo paths.

**Delta vs legacy `metacode-wpilot-v0.3.0.zip` (22 files):**

| Change | Files |
|--------|-------|
| **Added (UX-01)** | `admin/class-wpilot-admin-ui-model.php`, `languages/metacode-wpilot.pot`, `languages/metacode-wpilot-ru_RU.po` |
| **Modified (UX-01)** | `metacode-wpilot.php`, `admin/class-wpilot-admin-page.php`, `includes/class-wpilot-constants.php`, `includes/class-wpilot-plugin.php` |
| **Added (TEST-01)** | `languages/metacode-wpilot-ru_RU.mo` (compiled, in RC1 ZIP) |

**Fatal mismatch warning:** deploying UX-01 `metacode-wpilot.php` with old 22-file ZIP → `require` fatal on missing `class-wpilot-admin-ui-model.php`.

---

## Release Readiness (OPS-02)

| Level | Status |
|-------|--------|
| A — Stay Internal | Superseded for RC prep |
| **B — RC Ready** | **Current** — RC1 ZIP built; install proof still outstanding |
| C — Clean Install Proven | Not met — TEST-01 PARTIAL (package only) |

---

## Related Documents

| Document | Role |
|----------|------|
| [reports/wpilot-ops-02-report.md](reports/wpilot-ops-02-report.md) | OPS-02 full report |
| [reports/wpilot-ops-02-baseline-decision.md](reports/wpilot-ops-02-baseline-decision.md) | Baseline Variant B decision |
| [WPILOT-CLEAN-INSTALL-TEST-PLAN-v1.md](WPILOT-CLEAN-INSTALL-TEST-PLAN-v1.md) | Clean install procedure |
| [WPILOT-RELEASE-INVENTORY-v0.3.0.md](WPILOT-RELEASE-INVENTORY-v0.3.0.md) | Prior inventory (OPS-01) |
| [reports/wpilot-test-01-clean-install-proof.md](reports/wpilot-test-01-clean-install-proof.md) | TEST-01 clean install proof |

---

## Document Status

| Field | Value |
|-------|-------|
| Version | v0.3.0-RC1 specification |
| Implements runtime | No — release record only |
| ZIP built | Yes (TEST-01) |
| Clean install executed | No (PARTIAL) |
