# WPilot Plugin Filesystem Plan v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** planned filesystem shape for the first installable plugin MVP.

This plan defines the expected plugin folder structure for implementation planning. It does not create plugin source code.

## Plugin Root

Planned folder name:

- `metacode-wpilot/`

Planned ZIP:

- `metacode-wpilot.zip`

## Folder Structure

```text
metacode-wpilot/
  metacode-wpilot.php
  readme.txt
  uninstall.php
  admin/
    class-admin-page.php
    class-admin-actions.php
  api/
    class-rest-controller.php
    class-auth.php
    class-permissions.php
    class-request-validator.php
  includes/
    class-plugin.php
    class-activator.php
    class-deactivator.php
    class-response.php
    class-sanitizer.php
  storage/
    class-options-store.php
    class-token-store.php
    class-backup-store.php
    class-audit-log-store.php
    schema.php
  rollback/
    class-page-backup.php
    class-page-rollback.php
    class-checksum.php
  logging/
    class-audit-logger.php
    class-event.php
  parser/
    class-wpbakery-map.php
    class-shortcode-boundary.php
    class-replacement-planner.php
  assets/
    admin.css
```

## File Plan

| File | Role | Responsibility | Security importance | MVP status |
|---|---|---|---|---|
| `metacode-wpilot.php` | Bootstrap | Plugin header, constants, loader, activation/deactivation hooks. | Must not execute request data or expose endpoints before WordPress initializes. | CORE |
| `readme.txt` | Operator metadata | DEV-only warning, install notes, exclusions. | Prevents overtrust and production misuse. | CORE |
| `uninstall.php` | Uninstall boundary | Remove plugin-owned options/tables only when uninstall is explicitly invoked. | Must not delete WordPress content or external backups. | CORE |
| `admin/class-admin-page.php` | Admin UI | Status screen, bridge enablement, token controls, DEV-only warnings. | Restricts configuration to administrators. | CORE |
| `admin/class-admin-actions.php` | Admin form handling | Enable/disable bridge, rotate/revoke token. | Must use nonces and capability checks. | CORE |
| `api/class-rest-controller.php` | REST route owner | Register narrow route allowlist and dispatch handlers. | Prevents accidental broad API surface. | CORE |
| `api/class-auth.php` | REST auth | Validate per-site token and reject disabled bridge. | Primary external request boundary. | CORE |
| `api/class-permissions.php` | Capability checks | Map operations to WordPress capabilities and MVP rules. | Prevents non-admin or unintended access. | CORE |
| `api/class-request-validator.php` | Request validation | Validate page IDs, operation types, replacement shape, approval fields. | Aborts malformed or risky operations before mutation. | CORE |
| `includes/class-plugin.php` | Composition root | Wires admin, API, storage, logging, parser, rollback services. | Keeps bootstrap explicit and small. | CORE |
| `includes/class-activator.php` | Activation | Create plugin storage or fail visibly. | Must not enable bridge by default. | CORE |
| `includes/class-deactivator.php` | Deactivation | Disable bridge and stop routes from operating. | Reduces exposure after deactivation. | CORE |
| `includes/class-response.php` | Response helper | Consistent success/error response shape. | Avoids leaking secrets or stack traces. | CORE |
| `includes/class-sanitizer.php` | Sanitization | Normalize output and log fields. | Prevents secret and unsafe data exposure. | CORE |
| `storage/class-options-store.php` | Options storage | Store enabled flag, plugin version, retention settings. | Avoids scattered option writes. | CORE |
| `storage/class-token-store.php` | Token storage | Store hashed token material, rotation metadata, revoked state. | Critical for token secrecy. | CORE |
| `storage/class-backup-store.php` | Backup metadata/content | Store plugin-created page backup snapshots. | Must scope backups to approved page content only. | CORE |
| `storage/class-audit-log-store.php` | Audit persistence | Store sanitized operation events. | Required for observability and accountability. | CORE |
| `storage/schema.php` | Schema owner | Define plugin-owned table names and schema versions. | Prevents ad hoc table mutation. | CORE |
| `rollback/class-page-backup.php` | Backup service | Create page backup before write. | Write must abort when backup fails. | CORE |
| `rollback/class-page-rollback.php` | Rollback service | Restore from plugin-created backup. | Must verify target and backup ownership. | CORE |
| `rollback/class-checksum.php` | Integrity helper | Generate before/after content hashes. | Detects unexpected content drift. | CORE |
| `logging/class-audit-logger.php` | Logging facade | Write accepted/rejected/failed/rollback events. | Write-like operations must not proceed if logging preflight fails. | CORE |
| `logging/class-event.php` | Event model | Normalize event fields and outcomes. | Keeps logs consistent and sanitized. | CORE |
| `parser/class-wpbakery-map.php` | Parser | Build shortcode-aware structure map. | Avoids blind string mutation. | CORE |
| `parser/class-shortcode-boundary.php` | Boundary helper | Detect allowed and forbidden edit zones. | Refuses edits that could corrupt structure. | CORE |
| `parser/class-replacement-planner.php` | Replacement planning | Produce dry-run plan for one target occurrence. | Separates validation from mutation. | CORE |
| `assets/admin.css` | Admin asset | Minimal admin screen styling. | Must not include remote assets or scripts. | CORE |

## Future-Only Candidates

These are **EXPERIMENTAL** or **PLANNED** outside the first installable MVP:

- Browser/admin automation files.
- Plugin/theme/core update modules.
- Cache purge modules.
- SEO plugin write adapters.
- Multi-site network administration.
- External log export workers.
- Background queue workers.
- SaaS connector clients.

## Uninstall Strategy

**CORE / PLANNED:**

- Deactivation disables the bridge but does not remove audit/backup records.
- Uninstall may remove plugin-owned options and plugin-owned tables only after explicit WordPress uninstall.
- Uninstall must not modify page content.
- Uninstall must not delete WordPress users, plugins, themes, uploads, core files, or external backups.
- Backup retention before uninstall is a human operator decision.

## Filesystem Safety Rules

The MVP plugin filesystem must not include:

- File manager logic.
- Arbitrary path read/write helpers.
- Shell execution wrappers.
- SQL console helpers.
- Code generation or eval paths.
- Remote update/deployment clients.

All planned filesystem access is limited to normal WordPress plugin loading and plugin-owned assets.

