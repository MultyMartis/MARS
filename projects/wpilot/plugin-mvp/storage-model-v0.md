# WPilot Storage Model v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** storage contract for first installable plugin MVP.

This model defines plugin-owned storage for backups, audit events, token metadata, and options. It is not a database migration script.

## Storage Principles

- Store only what the plugin needs for DEV-only operation.
- Keep storage plugin-owned and narrow.
- Never store external credentials.
- Never store plaintext tokens.
- Never store database dumps, full-site backups, `wp-config.php`, cookies, session data, or hosting secrets.
- Prefer deterministic records that support rollback, audit, and manual review.

## Backup Table Model

**Status:** CORE / PLANNED.

Planned table:

- `{prefix}wpilot_backups`

Purpose:

- Store plugin-created page/post content snapshots for rollback of scoped MVP edits.

Suggested fields:

| Field | Purpose |
|---|---|
| `id` | Backup identifier. |
| `operation_id` | Links backup to write operation. |
| `target_type` | Example: `post`, `page`. |
| `target_id` | WordPress post/page ID. |
| `post_type` | Original post type. |
| `post_status` | Original post status. |
| `content_before` | Content snapshot before write. |
| `content_checksum` | Hash of `content_before`. |
| `created_at` | Backup timestamp. |
| `created_by_user_id` | WordPress user ID where available. |
| `source` | Expected value: `plugin`. |
| `rollback_used_at` | Timestamp when backup was used for rollback, nullable. |

Rules:

- Backup scope is page/post content only.
- Backup must be created before mutation.
- Backup must be linked to operation ID.
- Backup must not contain full database dumps.
- Backup must not contain secrets from external systems.

## Audit Log Table Model

**Status:** CORE / PLANNED.

Planned table:

- `{prefix}wpilot_audit_log`

Purpose:

- Store sanitized operation events for observability and accountability.

Suggested fields:

| Field | Purpose |
|---|---|
| `id` | Event identifier. |
| `operation_id` | Groups lifecycle events. |
| `event_type` | `request`, `rejected`, `backup_created`, `write_started`, `write_succeeded`, `write_failed`, `rollback_started`, `rolled_back`. |
| `route` | REST route name. |
| `actor_type` | `wp_user`, `token`, `unknown`. |
| `actor_user_id` | WordPress user ID where safely available. |
| `target_type` | `site`, `page`, `backup`, `log`, etc. |
| `target_id` | Target identifier where applicable. |
| `outcome` | `accepted`, `rejected`, `failed`, `succeeded`, `rolled_back`. |
| `reason_code` | Sanitized reason or error code. |
| `backup_id` | Backup reference where applicable. |
| `before_checksum` | Pre-write checksum where applicable. |
| `after_checksum` | Post-write checksum where applicable. |
| `created_at` | Event timestamp. |
| `metadata_json` | Small sanitized metadata object. |

Rules:

- No plaintext tokens.
- No auth headers.
- No passwords.
- No cookies.
- No raw stack traces.
- No large content dumps in audit metadata.
- Refusals should be logged when logging is available.

## Token Storage Approach

**Status:** CORE / PLANNED.

Token storage should use WordPress options or plugin-owned storage.

Minimum fields:

- Token hash.
- Token label or generated ID.
- Created timestamp.
- Rotated timestamp.
- Revoked timestamp.
- Last used timestamp.
- Enabled/disabled state.

Rules:

- Show plaintext token only once at generation or rotation.
- Store hash, not plaintext token, where feasible.
- Never write token to audit log.
- Token revocation must make previous token unusable.
- Bridge disabled state must reject token-authenticated REST operations.

## Plugin Option Storage

**Status:** CORE / PLANNED.

Suggested option keys:

- `wpilot_enabled`
- `wpilot_dev_confirmed`
- `wpilot_plugin_version`
- `wpilot_schema_version`
- `wpilot_retention_days`
- `wpilot_allowed_post_types`
- `wpilot_last_token_rotation_at`

Rules:

- `wpilot_enabled` defaults to false.
- `wpilot_dev_confirmed` defaults to false.
- Write endpoints require both enabled and DEV confirmation.
- Options must not store secrets except hashed token material if option-based storage is selected.

## Retention Ideas

**Status:** PLANNED.

DEV-only retention should be conservative and visible:

- Default audit retention: 30 days or manual clear.
- Default backup retention: manual clear or limited count per page.
- No automatic deletion during write operations.
- Uninstall may remove plugin-owned records only through explicit WordPress uninstall.

Retention behavior is **SAFE UNKNOWN** until implementation chooses exact storage and admin controls.

## DEV-Only Assumptions

- Storage volume is small.
- Number of pages tested is small.
- Operation history is manually reviewed.
- Backups are rollback aids for plugin-created writes, not site backup replacements.
- Hosting-panel and database-level backups remain external human responsibilities.

## What Must Not Be Stored

**EXCLUDED:**

- WordPress passwords.
- Beget credentials.
- FTP/SFTP credentials.
- Database credentials.
- Cookies.
- Auth headers.
- Plaintext WPilot tokens.
- `wp-config.php`.
- Database dumps.
- Full-site backups.
- Hosting panel exports.
- Raw stack traces with paths/secrets.
- Personal data copied from user lists.
- Browser automation sessions.

## Failure Handling

Abort write-like operations if:

- Backup storage is unavailable.
- Audit log preflight fails.
- Token validation storage is unavailable.
- Required option reads fail.
- Backup checksum cannot be generated.

Do not fall back to arbitrary SQL, filesystem dumps, or hidden external storage.

## SAFE UNKNOWN

- Whether custom tables or option-based storage will be selected for first implementation.
- Exact schema migration mechanism.
- Exact retention UI.
- Target hosting database privileges.
- Object cache behavior.
- Multisite behavior, which is outside MVP unless separately planned.

