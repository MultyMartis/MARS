# REPORT — WPilot OPS-01

**Task:** Deploy & Release Readiness Pass  
**Date:** 2026-06-19  
**Scope:** Documentation and audit only — no deploy, no runtime changes, no Sprint 3  
**Checkpoint:** `8c67478` (`feat(wpilot): freeze v0.3.0 proven runtime`)  
**State freeze:** Active — [WPILOT-STATE-FREEZE-2026-06-19-v1.md](../WPILOT-STATE-FREEZE-2026-06-19-v1.md)

---

## 1. Release Readiness Audit

**Target:** `projects/wpilot/plugin/metacode-wpilot/`

### Summary

Plugin tree is **clean** — no debug dumps, temp files, backup copies, runtime evidence, reports, or secrets found inside the plugin directory. All files are legitimate PHP, i18n, or operator README artifacts.

**Current file count:** 25 (checkpoint `8c67478` = 22; UX-01 working tree adds 3).

### KEEP (25 files)

| Path | Rationale |
|------|-----------|
| `metacode-wpilot.php` | Plugin bootstrap |
| `README.md` | Operator install/readme |
| `admin/class-wpilot-admin-page.php` | Settings UI |
| `admin/class-wpilot-admin-ui-model.php` | UX-01 display model (uncommitted) |
| `includes/class-wpilot-*.php` (19 files) | Runtime services, REST, schema, auth |
| `languages/metacode-wpilot.pot` | i18n template (uncommitted) |
| `languages/metacode-wpilot-ru_RU.po` | Russian catalog (uncommitted) |

### REMOVE

**None identified.** No automatic deletion performed.

### SAFE UNKNOWN

| Item | Notes |
|------|-------|
| **`metacode-wpilot-ru_RU.mo`** | Not in plugin tree. WordPress loads `.mo` at runtime; `.po` alone does not activate translations. |
| **Release baseline** | Operator may ship checkpoint `8c67478` (22 files) or UX-01 tree (25 files). Working tree is uncommitted atop checkpoint. |
| **Plugin README step 5** | Still says "enable the read-only bridge" — copy lag, not a stray file. |
| **`WP_DEBUG` logging** | `class-wpilot-rest-controller.php` has DEV-safe debug hook — intentional code, not a stray log file. |

### Secret / artifact scan (plugin tree)

| Pattern | Result |
|---------|--------|
| `.bak`, `.tmp`, `.log`, `.json` evidence | Not found |
| Plaintext tokens / credentials | Not found |
| Reports inside plugin tree | Not found |
| `.git` / parent repo paths | Not found |

---

## 2. ZIP Deploy Audit

**Package:** `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0.zip`

| Check | Result |
|-------|--------|
| ZIP opens | ✓ |
| Size | 36,556 bytes |
| Last modified | 2026-06-19 16:17:24 |
| Root folder | `metacode-wpilot/` ✓ |
| `metacode-wpilot/metacode-wpilot.php` | ✓ Present |
| File count | **22** |
| Secrets / local tokens | ✓ None detected |
| Runtime evidence / STORAGE paths | ✓ None |

### ZIP inventory (22 files)

```
metacode-wpilot/metacode-wpilot.php
metacode-wpilot/README.md
metacode-wpilot/admin/class-wpilot-admin-page.php
metacode-wpilot/includes/class-wpilot-audit-service.php
metacode-wpilot/includes/class-wpilot-auth.php
metacode-wpilot/includes/class-wpilot-backup-service.php
metacode-wpilot/includes/class-wpilot-checksum.php
metacode-wpilot/includes/class-wpilot-constants.php
metacode-wpilot/includes/class-wpilot-dry-run.php
metacode-wpilot/includes/class-wpilot-environment.php
metacode-wpilot/includes/class-wpilot-errors.php
metacode-wpilot/includes/class-wpilot-operation-id.php
metacode-wpilot/includes/class-wpilot-plugin.php
metacode-wpilot/includes/class-wpilot-request-context.php
metacode-wpilot/includes/class-wpilot-response.php
metacode-wpilot/includes/class-wpilot-rest-controller.php
metacode-wpilot/includes/class-wpilot-rollback-service.php
metacode-wpilot/includes/class-wpilot-schema.php
metacode-wpilot/includes/class-wpilot-scoped-replace-service.php
metacode-wpilot/includes/class-wpilot-settings.php
metacode-wpilot/includes/class-wpilot-site-reader.php
metacode-wpilot/includes/class-wpilot-wpbakery-detector.php
```

### ZIP gaps vs current source (UX-01)

| Missing from ZIP | Impact |
|------------------|--------|
| `admin/class-wpilot-admin-ui-model.php` | **Fatal** if deployed with UX-01 `metacode-wpilot.php` (requires ui-model) |
| `languages/metacode-wpilot.pot` | i18n foundation absent in ZIP |
| `languages/metacode-wpilot-ru_RU.po` | Russian catalog absent in ZIP |
| `languages/metacode-wpilot-ru_RU.mo` | Absent everywhere — localization runtime gap |

### ZIP service coverage (checkpoint package)

| Surface | In ZIP |
|---------|--------|
| Runtime services (backup, rollback, scoped-replace, audit, schema) | ✓ |
| REST controller | ✓ |
| Admin page (pre-UX-01) | ✓ |
| UI model (UX-01) | ✗ |
| Languages | ✗ |

**Conclusion:** ZIP is a valid **checkpoint `8c67478`** package (22 files). It is **stale** relative to UX-01 working tree. ZIP installation on clean WordPress = **SAFE UNKNOWN** (not executed).

---

## 3. Localization Status

### Files present (working tree)

| File | Status |
|------|--------|
| `languages/metacode-wpilot.pot` | ✓ Exists |
| `languages/metacode-wpilot-ru_RU.po` | ✓ Exists (78 msgids) |
| `languages/metacode-wpilot-ru_RU.mo` | ✗ **Absent** |

### Textdomain alignment

| Source | Value | Match |
|--------|-------|-------|
| Plugin header `Text Domain` | `metacode-wpilot` | ✓ |
| `WPilot_Constants::TEXT_DOMAIN` | `metacode-wpilot` | ✓ |
| `.pot` / `.po` headers | `metacode-wpilot` | ✓ |
| `Domain Path` header | `/languages` | ✓ |

### `load_plugin_textdomain`

```60:64:projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-plugin.php
		load_plugin_textdomain(
			WPilot_Constants::TEXT_DOMAIN,
			false,
			dirname( plugin_basename( WPILOT_PLUGIN_FILE ) ) . '/languages'
		);
```

Present in **UX-01 working tree only** — not in committed `8c67478` `class-wpilot-plugin.php`.

### Verdict

**Localization Deploy Gap**

- Foundation (`.pot`, `.po`, textdomain, bootstrap) is correct in UX-01 source.
- **Not runtime-ready** for `ru_RU` until `metacode-wpilot-ru_RU.mo` is compiled and deployed.
- ZIP package contains **no** localization files.
- Per task: `.mo` was **not** created manually.

---

## 4. Clean Install Checklist

**Created:** [WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md](../WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md)

Canonical 10-step path:

1. Чистый WordPress  
2. Установка ZIP  
3. Активация  
4. Создание таблиц  
5. Проверка Settings  
6. Проверка REST  
7. Проверка Runtime Dashboard  
8. Проверка Localization  
9. Проверка Backup  
10. Проверка Rollback  

**Execution status:** Not performed (documentation only).

---

## 5. Release Inventory

**Created:** [WPILOT-RELEASE-INVENTORY-v0.3.0.md](../WPILOT-RELEASE-INVENTORY-v0.3.0.md)

Captures: version, schema, checkpoint, proven capabilities, runtime maturity, 22+3 file inventory, 12 endpoints, known limitations, not-yet-proven surface.

---

## 6. Ecosystem Sync Result

Reviewed against UX-01 completion:

| Document | UX-01 impact | Action |
|----------|--------------|--------|
| [WPILOT-STATE-FREEZE-2026-06-19-v1.md](../WPILOT-STATE-FREEZE-2026-06-19-v1.md) | UX-01 is admin/i18n only; freeze rules and proven runtime unchanged | No update |
| [WPILOT-PROVEN-CAPABILITIES-v1.md](../WPILOT-PROVEN-CAPABILITIES-v1.md) | No new proven capabilities from admin UI alignment | No update |
| [runtime-contracts/WPILOT-RUNTIME-CONTRACTS-v1.md](../runtime-contracts/WPILOT-RUNTIME-CONTRACTS-v1.md) | REST/schema/auth unchanged | No update |
| [README.md](../README.md) | Runtime status still accurate; no localization mention required for freeze | No update |
| [ecosystem-sync/WPILOT-ECOSYSTEM-SYNC-2026-06-v1.md](../ecosystem-sync/WPILOT-ECOSYSTEM-SYNC-2026-06-v1.md) | Cross-system patterns unchanged | No update |

**No sync changes required.**

---

## 7. Recommended Release Status

### **B — Internal Release Ready**

| Criterion | Assessment |
|-----------|------------|
| **A — Not Ready** | Not applicable — no critical packaging corruption; runtime proven on DEV via FTP |
| **B — Internal Release Ready** | **Selected** — ZIP exists for checkpoint tree; release inventory and clean-install checklist prepared; clean install and ZIP path not proven |
| **C — Reproducible Deploy Proven** | Not met — no evidence of fresh WordPress ZIP install |

**Rationale:**

- Runtime = proven (DEV, FTP deploy).
- Deploy reproducibility = not proven.
- ZIP = packaging artifact for 22-file checkpoint; stale vs UX-01.
- Localization = deploy gap (`.mo` missing).
- Clean install checklist exists but **not executed**.

**Before external/production consideration:** rebuild ZIP from chosen baseline, compile `.mo`, execute [WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md](../WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md) on disposable WP, commit or tag UX-01 if it is release scope.

---

## 8. Git Status

```
 M projects/wpilot/plugin/metacode-wpilot/admin/class-wpilot-admin-page.php
 M projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-constants.php
 M projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-plugin.php
 M projects/wpilot/plugin/metacode-wpilot/metacode-wpilot.php
?? projects/wpilot/plugin/metacode-wpilot/admin/class-wpilot-admin-ui-model.php
?? projects/wpilot/plugin/metacode-wpilot/languages/
?? projects/wpilot/reports/wpilot-ux-01-report.md
?? projects/wpilot/WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md      (this OPS-01 pass)
?? projects/wpilot/WPILOT-RELEASE-INVENTORY-v0.3.0.md        (this OPS-01 pass)
?? projects/wpilot/reports/wpilot-ops-01-report.md           (this OPS-01 pass)
```

**HEAD:** `8c67478` — UX-01 and OPS-01 docs are uncommitted working-tree additions.

---

## 9. SAFE UNKNOWN

| Item | Detail |
|------|--------|
| **ZIP clean install** | Package not tested on fresh WordPress in this pass |
| **UX-01 vs checkpoint release** | Operator has not declared which tree is canonical for next deploy |
| **`.mo` compile environment** | `msgfmt` / WP-CLI availability on operator machine — not verified here |
| **ZIP rebuild after UX-01** | No new ZIP produced in OPS-01 |
| **Plugin README copy** | Install section partially pre-v0.3.0 wording |
| **Hosting constraints** | Beget-specific upload limits, PHP version on hypothetical clean WP — not audited |

---

## 10. SECURITY RISK

| Risk | Level | Notes |
|------|-------|-------|
| Secrets in plugin tree | **Low** | Scan clean |
| Secrets in deploy ZIP | **Low** | No tokens/credentials found |
| Token in git | **Low** | Only hash-in-DB design; UX-01 `.po` mentions "token" as UI strings only |
| ZIP stale vs UX-01 bootstrap | **Medium (operational)** | Deploying mixed state (new bootstrap + old ZIP) → fatal `require` error |
| Information disclosure (admin UI) | **Low** | REST route inventory is intentional operator surface |
| Production misuse | **Medium (policy)** | DEV-only guards exist; clean install not proven on arbitrary hosts |

No **SECURITY RISK** stop condition for internal DEV use. Operational caution: **rebuild ZIP** before any ZIP-based deploy if UX-01 is in scope.

---

## Deliverables Summary

| Deliverable | Path | Status |
|-------------|------|--------|
| Clean install checklist | `projects/wpilot/WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md` | Created |
| Release inventory | `projects/wpilot/WPILOT-RELEASE-INVENTORY-v0.3.0.md` | Created |
| OPS-01 report | `projects/wpilot/reports/wpilot-ops-01-report.md` | Created |

**Not performed:** deploy, runtime changes, Sprint 3, `.mo` creation, ZIP rebuild, file deletion.
