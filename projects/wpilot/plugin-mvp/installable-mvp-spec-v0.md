# WPilot Installable MVP Spec v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** first installable MetaCODE WPilot WordPress plugin MVP.
**Source context:** `reconciliation-map-v0.md`, `../metacode-wpilot-plugin-concept.md`, `../metacode-wpilot-plugin-mvp-roadmap.md`.

This spec defines the first real installable plugin shape. It is an engineering contract for implementation planning, not plugin source code and not evidence that the plugin exists.

## Exact MVP Boundaries

The MVP is a small WordPress plugin installed from a local ZIP on an explicitly confirmed development or test site.

The plugin is:

- **DEV-ONLY**.
- Disabled by default after activation.
- Enabled only by a human WordPress administrator.
- Authenticated by a per-site token for REST calls.
- Limited to read-only inspection, plugin-created page backups, single scoped text replacement, rollback from plugin-created backup, audit logs, and DEV indexing signal inspection.
- Human-supervised at every write-like step.

The plugin is not a MARS runtime component, autonomous agent, deployment system, browser automation layer, file manager, SQL console, shell bridge, SaaS service, or production-ready plugin.

## What The First Installable Plugin Can Do

**CORE / PLANNED:**

- Activate and deactivate as a normal WordPress plugin.
- Show an admin status/configuration page.
- Remain disabled until an administrator explicitly enables the bridge.
- Generate, rotate, and revoke a per-site REST token.
- Register a narrow REST API namespace.
- Authenticate REST requests with the per-site token.
- Log accepted, rejected, failed, and rollback operations without secrets.
- Return sanitized site information.
- Return active theme and plugin inventory without update actions.
- List pages and read one approved page.
- Detect common WPBakery shortcode structure.
- Create a plugin-owned backup snapshot for one page.
- Validate one scoped replacement request.
- Perform one text-only replacement on one target page after backup and validation.
- Roll back one page from a plugin-created backup.
- Report DEV indexing signals, such as WordPress visibility, `robots.txt` visibility, and frontend robots metadata where safely detectable.

## What It Cannot Do

**EXCLUDED:**

- Execute arbitrary SQL.
- Expose a SQL query endpoint.
- Access unrestricted filesystem paths.
- Edit plugin, theme, WordPress core, uploads, or `wp-config.php` files.
- Execute PHP, shell, JavaScript, template, or user-supplied code.
- Install, update, deactivate, or delete plugins, themes, or WordPress core.
- Perform mass replacement.
- Perform background autonomous edits.
- Scrape or control the WordPress admin UI through browser automation.
- Store credentials, cookies, plaintext tokens, database dumps, or backup archives in this repository.
- Claim production readiness.

## DEV-Only Restrictions

The MVP must visibly warn that it is DEV-only.

Required restrictions:

- Admin page includes DEV-only warning.
- Plugin enablement requires a human confirmation checkbox or equivalent explicit action.
- Write endpoints should refuse operation unless the bridge is enabled.
- Production-safe detection is **SAFE UNKNOWN**; the plugin must not claim it can reliably identify production.
- Operators must manually confirm the environment before first write test.

## Human-Supervised Requirements

Human supervision is required for:

- Plugin installation.
- Plugin activation.
- Bridge enablement.
- Token generation and rotation.
- Selecting the target page.
- Approving the dry-run result.
- Approving a scoped replacement.
- Verifying frontend result.
- Triggering rollback if needed.
- Confirming closeout and token revocation.

The plugin may assist with deterministic checks, but it must not decide that a risky write is acceptable without human approval.

## Security Assumptions

**CORE / PLANNED assumptions:**

- Only administrators can configure the plugin.
- REST requests require token authentication.
- Token values are not logged.
- Stored token material is hashed where feasible.
- All routes enforce an operation allowlist.
- Write-like routes require backup-first checks.
- Audit logging is best effort, but failure to log a write-like operation must abort the write.
- Errors returned to clients are sanitized.

**SAFE UNKNOWN:**

- Exact WordPress/PHP versions.
- Hosting security plugin behavior.
- Cache plugin interference.
- Token storage implementation details.
- Whether object cache or DB permissions affect storage reliability.

## Expected Install Flow

1. Build a local ZIP from the plugin folder.
2. Human administrator uploads the ZIP in WordPress admin.
3. Human administrator activates the plugin.
4. Plugin creates required storage on activation or reports a blocking setup error.
5. Plugin starts disabled.
6. Administrator opens plugin settings.
7. Administrator confirms DEV-only use and enables the bridge.
8. Administrator generates a per-site token.
9. Operator runs a first authenticated status request.

## Expected Operator Workflow

1. Confirm target site is DEV/test.
2. Install and activate plugin.
3. Enable bridge and generate token.
4. Run status and read-only inspection.
5. Inspect target page and WPBakery map.
6. Submit dry validation for proposed replacement.
7. Create backup or allow write operation to create required backup.
8. Execute scoped replacement only after approval.
9. Manually verify frontend and admin state.
10. Review audit log.
11. Roll back if result is wrong.
12. Revoke token or disable bridge after test.

## Failure Handling Philosophy

The MVP should be deterministic, minimal, observable, rollback-first, and refusal-first.

Preferred behavior:

- Refuse ambiguous requests.
- Abort before mutation when validation is incomplete.
- Return compact error codes with safe messages.
- Log refusal and failure events.
- Require manual verification instead of hidden repair.
- Preserve rollback path over completing a risky operation.

Not allowed:

- Smart autonomous editing.
- Hidden recovery.
- Automatic repair logic.
- Best-effort mutation after failed validation.
- Silent partial writes.

## MVP Completion Criteria

The first installable MVP is complete only when:

- Local ZIP install works on a confirmed DEV WordPress site.
- Plugin activates disabled by default.
- Token generation, rotation, and revocation work.
- Authenticated read-only endpoints work.
- Backup creation works for one page.
- A single scoped replacement can be dry-validated, executed, audited, manually verified, and rolled back.
- Refusal cases are observable and logged.
- No excluded capability is present.

