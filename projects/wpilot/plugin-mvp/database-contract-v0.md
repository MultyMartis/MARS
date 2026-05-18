# WPilot Database Contract v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** exact plugin-owned storage contract for first implementation.

This contract defines plugin tables/options. It does not create arbitrary SQL execution capability and must not be implemented as a SQL console.

## Migration Philosophy

- Use WordPress activation/upgrade routines for plugin-owned schema only.
- Schema changes are versioned by `wpilot_schema_version`.
- Migration failure sets plugin state to `invalid-config`.
- Operational endpoints refuse while schema is invalid.
- No migration may touch WordPress core tables except through normal WordPress APIs for supported operations.

## Backup Table

Table:

- `{prefix}wpilot_backups`

Schema:

| Column | Type | Null | Notes |
|---|---|---|---|
| `id` | `BIGINT UNSIGNED AUTO_INCREMENT` | no | Primary key. |
| `operation_id` | `VARCHAR(64)` | no | Operation that created backup. |
| `target_type` | `VARCHAR(32)` | no | MVP values: `post`, `page`. |
| `target_id` | `BIGINT UNSIGNED` | no | WordPress post/page ID. |
| `post_type` | `VARCHAR(32)` | no | Original post type. |
| `post_status` | `VARCHAR(32)` | no | Original status. |
| `content_before` | `LONGTEXT` | no | Pre-write `post_content` snapshot only. |
| `content_checksum` | `VARCHAR(96)` | no | Example: `sha256:<hex>`. |
| `created_by_user_id` | `BIGINT UNSIGNED` | yes | WordPress user ID if available. |
| `created_at` | `DATETIME` | no | UTC preferred. |
| `source` | `VARCHAR(32)` | no | Must be `plugin`. |
| `rollback_used_at` | `DATETIME` | yes | Set after rollback use. |

Indexes:

- Primary key: `id`.
- Index: `operation_id`.
- Index: `(target_type, target_id)`.
- Index: `created_at`.
- Index: `rollback_used_at`.

Rules:

- Backup rows contain page/post content only.
- Backup rows are not full database backups.
- Backup rows must be created before mutation.
- Backup rows must be read only through plugin storage services.

## Audit Table

Table:

- `{prefix}wpilot_audit_log`

Schema:

| Column | Type | Null | Notes |
|---|---|---|---|
| `id` | `BIGINT UNSIGNED AUTO_INCREMENT` | no | Primary key. |
| `operation_id` | `VARCHAR(64)` | no | Groups lifecycle events. |
| `event_type` | `VARCHAR(64)` | no | Stable event type. |
| `route` | `VARCHAR(128)` | yes | REST route or admin action. |
| `actor_type` | `VARCHAR(32)` | no | `wp_user`, `token`, `system`, `unknown`. |
| `actor_user_id` | `BIGINT UNSIGNED` | yes | WordPress user ID if available. |
| `target_type` | `VARCHAR(32)` | yes | `site`, `page`, `backup`, `plugin`. |
| `target_id` | `BIGINT UNSIGNED` | yes | Target ID when applicable. |
| `outcome` | `VARCHAR(32)` | no | `accepted`, `rejected`, `failed`, `succeeded`, `rolled_back`. |
| `reason_code` | `VARCHAR(64)` | yes | Error/refusal code. |
| `backup_id` | `BIGINT UNSIGNED` | yes | Related backup. |
| `before_checksum` | `VARCHAR(96)` | yes | Pre-write checksum. |
| `after_checksum` | `VARCHAR(96)` | yes | Post-write checksum. |
| `metadata_json` | `TEXT` | yes | Small sanitized metadata object. |
| `created_at` | `DATETIME` | no | UTC preferred. |

Indexes:

- Primary key: `id`.
- Index: `operation_id`.
- Index: `event_type`.
- Index: `outcome`.
- Index: `(target_type, target_id)`.
- Index: `backup_id`.
- Index: `created_at`.

Rules:

- No plaintext tokens.
- No auth headers.
- No passwords/cookies.
- No raw stack traces.
- No full content snapshots in audit rows.
- Write-like operations must create audit preflight before mutation.

## Option Storage Model

Options:

| Option | Default | Purpose |
|---|---|---|
| `wpilot_enabled` | `false` | Bridge enabled flag. |
| `wpilot_dev_confirmed` | `false` | Human DEV/test confirmation. |
| `wpilot_emergency_disabled` | `false` | Emergency stop flag. |
| `wpilot_plugin_version` | plugin version | Installed plugin version. |
| `wpilot_schema_version` | schema version | Storage migration version. |
| `wpilot_retention_days` | `30` | Audit retention hint. |
| `wpilot_backup_retention_count` | `10` | Backup retention hint per target. |
| `wpilot_allowed_post_types` | `["page"]` | MVP allowed post types. |
| `wpilot_token_hash` | null | Hashed active token. |
| `wpilot_token_created_at` | null | Token creation timestamp. |
| `wpilot_token_rotated_at` | null | Last rotation timestamp. |
| `wpilot_token_revoked_at` | null | Revocation timestamp. |
| `wpilot_last_token_used_at` | null | Last successful auth timestamp. |
| `wpilot_last_safety_error` | null | Last safety/blocking error code. |

Rules:

- `wpilot_enabled` and `wpilot_dev_confirmed` must both be true for write endpoints.
- Token hash may be option-backed in MVP.
- Plaintext token is never stored.
- Emergency disabled overrides enabled/dev/token states.

## Token Storage Strategy

**CORE / PLANNED:**

- Generate high-entropy token.
- Show plaintext token only once.
- Store password-hash-style or keyed hash representation where feasible.
- Compare submitted token using constant-time comparison where feasible.
- Rotation invalidates prior token.
- Revocation sets token unusable.

SAFE UNKNOWN:

- Exact hashing helper depends on WordPress/PHP compatibility selected at implementation.

## Checksum Fields

Checksum format:

- `sha256:<hex>`

Required checksums:

- Backup `content_checksum`.
- Scoped replace `before_checksum`.
- Scoped replace `after_checksum`.
- Rollback `restored_checksum`.

Rules:

- Checksum mismatch aborts write/rollback where expected checksum is supplied.
- Checksum is for integrity, not authentication.

## Timestamps

Preferred:

- UTC datetime strings using WordPress current time helpers configured for GMT where feasible.

Required timestamp fields:

- Backup creation.
- Audit event creation.
- Token created/rotated/revoked/last-used.
- Rollback used time.

## Retention And Cleanup

**DEV-ONLY / PLANNED:**

- Retention is operator-visible.
- No cleanup runs during a write operation.
- Manual cleanup may remove old plugin-owned audit/backup records.
- Uninstall may remove plugin-owned tables/options only through explicit uninstall.
- Deactivation does not delete records.

## Forbidden Storage/DB Patterns

**EXCLUDED:**

- Arbitrary SQL endpoint.
- Raw SQL from REST request.
- SQL console helper.
- Direct mutation of WordPress content tables for scoped replace.
- Direct mutation of plugin/theme/core files.
- Storing plaintext tokens.
- Storing external credentials.
- Storing full database dumps.

