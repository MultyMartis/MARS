# WPilot Release Inventory — v0.3.0

**Classification:** Release state record — no roadmap, no marketing.  
**Date:** 2026-06-19  
**Scope:** `metacode-wpilot` v0.3.0 release surface as documented at OPS-01 pass.

---

## Version

| Field | Value |
|-------|-------|
| **Plugin version** | `0.3.0` |
| **Schema version** | `0.2.0` |
| **Text domain** | `metacode-wpilot` |
| **REST namespace** | `wpilot/v1` |
| **Plugin slug / folder** | `metacode-wpilot` |

**Version sources (must match):**

- `metacode-wpilot.php` header → `0.3.0`
- `WPilot_Constants::VERSION` → `0.3.0`
- `WPilot_Constants::SCHEMA_VERSION` → `0.2.0`

---

## Schema

**DB tables** (created/upgraded via `WPilot_Schema::maybe_upgrade()`):

| Table | Purpose |
|-------|---------|
| `{prefix}wpilot_backups` | Page `post_content` backup snapshots |
| `{prefix}wpilot_audit_log` | Sanitized lifecycle audit events |

**Options** (via `WPilot_Settings`):

- Bridge flags (`bridge_enabled`, `write_enabled`, `dev_test_confirmed`, `emergency_disabled`)
- Token hash only (no plaintext persistence)
- Schema version marker

---

## Checkpoint

| Field | Value |
|-------|-------|
| **Git checkpoint** | `8c67478` — `feat(wpilot): freeze v0.3.0 proven runtime` |
| **State freeze doc** | [WPILOT-STATE-FREEZE-2026-06-19-v1.md](WPILOT-STATE-FREEZE-2026-06-19-v1.md) |
| **Packaging ZIP** | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0.zip` (36,556 bytes, 2026-06-19) |
| **UX-01 status** | Completed in working tree; **uncommitted** atop `8c67478` at OPS-01 time |

---

## Proven Capabilities

Formal plugin REST proven on DEV (`https://dev.gktriumph.ru`) — see [WPILOT-PROVEN-CAPABILITIES-v1.md](WPILOT-PROVEN-CAPABILITIES-v1.md):

| Capability | Endpoint / mechanism |
|------------|---------------------|
| `inspect` | Read REST (`site-info`, `pages`, `structure`, etc.) |
| `backup` | `POST /pages/{id}/backups` |
| `rollback` | `POST /pages/{id}/rollback` |
| `validate` | Post-write / post-rollback checksum verification |
| `apply_content_change` | `POST /pages/{id}/scoped-replace` (exact once, `post_content`) |
| Audit trail | `wpilot_audit_log` per `operation_id` |
| Checksum pipeline | `sha256:` on inspect, backup, apply, rollback |
| Dry-run analysis | `POST /pages/{id}/replace-text/dry-run` |
| WPBakery-safe recovery | Full `post_content` restore with shortcode integrity |

**Deploy method proven:** FTP upload of plugin source files.  
**Deploy method not proven:** WordPress ZIP clean install.

---

## Runtime Maturity

| Field | Value |
|-------|-------|
| **Level** | `proven_content_writes` |
| **Environment** | DEV only |
| **Supervision** | Human-supervised |
| **Write primitive** | Scoped exact-once replace on `page.post_content` only |

---

## Plugin File Inventory

### Checkpoint tree (`8c67478`) — 22 files

Matches existing deploy ZIP.

| Path | Role |
|------|------|
| `metacode-wpilot.php` | Bootstrap, hooks, requires |
| `README.md` | Operator plugin readme |
| `admin/class-wpilot-admin-page.php` | Settings admin UI |
| `includes/class-wpilot-audit-service.php` | Audit log writes |
| `includes/class-wpilot-auth.php` | Token auth guards |
| `includes/class-wpilot-backup-service.php` | Backup create |
| `includes/class-wpilot-checksum.php` | SHA-256 checksums |
| `includes/class-wpilot-constants.php` | Version, headers, UI constants |
| `includes/class-wpilot-dry-run.php` | Dry-run analysis |
| `includes/class-wpilot-environment.php` | DEV/environment checks |
| `includes/class-wpilot-errors.php` | Error envelopes |
| `includes/class-wpilot-operation-id.php` | Operation ID generation |
| `includes/class-wpilot-plugin.php` | Plugin singleton / hooks |
| `includes/class-wpilot-request-context.php` | Request metadata |
| `includes/class-wpilot-response.php` | Success envelopes |
| `includes/class-wpilot-rest-controller.php` | REST route registration |
| `includes/class-wpilot-rollback-service.php` | Rollback execute |
| `includes/class-wpilot-schema.php` | DB schema upgrade |
| `includes/class-wpilot-scoped-replace-service.php` | Scoped replace execute |
| `includes/class-wpilot-settings.php` | Options, token, activation |
| `includes/class-wpilot-site-reader.php` | Read endpoints data |
| `includes/class-wpilot-wpbakery-detector.php` | WPBakery signals |

### UX-01 additions (working tree, not in checkpoint ZIP) — +3 files

| Path | Role |
|------|------|
| `admin/class-wpilot-admin-ui-model.php` | Display-only admin UI data model |
| `languages/metacode-wpilot.pot` | Translation template |
| `languages/metacode-wpilot-ru_RU.po` | Russian catalog (78 msgids) |

### Not in any package

| Path | Status |
|------|--------|
| `languages/metacode-wpilot-ru_RU.mo` | **Absent** — required for runtime Russian UI |

**Total current source:** 25 files (+ `.mo` gap).

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
| Localization runtime | `.po` present (UX-01); `.mo` absent — Russian UI not runtime-ready |
| UX-01 uncommitted | Working tree diverges from checkpoint ZIP |
| Plugin README drift | Still says "read-only bridge" in install step 5 — minor copy lag vs v0.3.0 writes |

---

## Not Yet Proven Surface

| Surface | Status |
|---------|--------|
| WordPress ZIP clean install | Not proven |
| Deploy reproducibility on fresh WP | Not proven |
| `metacode-wpilot-ru_RU.mo` deploy path | Not proven |
| Production environment | Not proven |
| Menu / widget / footer / CSS plugin REST writes | Not proven |
| Autonomous agent execution | Not proven |
| OCPilot parity | Not applicable — WordPress evidence only |

---

## Related Documents

| Document | Role |
|----------|------|
| [WPILOT-STATE-FREEZE-2026-06-19-v1.md](WPILOT-STATE-FREEZE-2026-06-19-v1.md) | Active freeze |
| [WPILOT-PROVEN-CAPABILITIES-v1.md](WPILOT-PROVEN-CAPABILITIES-v1.md) | Evidence register |
| [reports/wpilot-runtime-inventory-v0.3.0.md](reports/wpilot-runtime-inventory-v0.3.0.md) | Runtime snapshot |
| [WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md](WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md) | Clean install validation path |
| [reports/wpilot-ops-01-report.md](reports/wpilot-ops-01-report.md) | OPS-01 audit report |

---

## Document Status

| Field | Value |
|-------|-------|
| Version | v0.3.0 inventory |
| Implements runtime | No — release record only |
| Replaces State Freeze | No |
