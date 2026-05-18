# WPilot REST API Contracts v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** exact REST contracts for the first installable plugin MVP.

All responses are compact, deterministic, JSON objects. No response may include secrets, plaintext tokens, auth headers, stack traces, database dumps, unrestricted filesystem paths, or unrelated personal data.

## Shared Contract

Namespace:

- `wpilot/v1`

Auth:

- Read and write endpoints require per-site token authentication except where noted.
- Admin UI token generation is not a REST endpoint in this MVP contract.

Standard success envelope:

```json
{
  "ok": true,
  "operation_id": "op_...",
  "data": {},
  "warnings": []
}
```

Standard refusal/error envelope:

```json
{
  "ok": false,
  "operation_id": "op_...",
  "error": {
    "code": "WPILOT_ERROR_CODE",
    "message": "Operator-readable message.",
    "stage": "auth",
    "mutation_performed": false,
    "rollback_available": false
  }
}
```

Common refusal reasons:

- `BRIDGE_DISABLED`
- `DEV_NOT_CONFIRMED`
- `AUTH_MISSING`
- `AUTH_INVALID`
- `TOKEN_REVOKED`
- `PERMISSION_DENIED`
- `INVALID_REQUEST`
- `AUDIT_UNAVAILABLE`

## READ: ping

Route:

- `GET /wp-json/wpilot/v1/ping`

Auth requirement:

- No token required.

Request schema:

- Empty.

Response schema:

```json
{
  "ok": true,
  "data": {
    "plugin": "metacode-wpilot",
    "status": "installed",
    "bridge_enabled": false,
    "dev_confirmed": false
  }
}
```

Possible refusal reasons:

- `INVALID_CONFIG` if plugin storage/state cannot be read.

Audit requirements:

- Optional audit event; no secrets.

Rollback relevance:

- None.

SAFE UNKNOWN:

- Whether `ping` should expose plugin version before auth depends on implementation security review.

## READ: site-info

Route:

- `GET /wp-json/wpilot/v1/site-info`

Auth requirement:

- Token required.

Request schema:

- Empty.

Response schema:

```json
{
  "ok": true,
  "operation_id": "op_...",
  "data": {
    "wp_version": "6.x",
    "site_url_host": "example.test",
    "multisite": false,
    "php_version": "8.x",
    "bridge_enabled": true,
    "dev_confirmed": true
  },
  "warnings": []
}
```

Possible refusal reasons:

- Common auth/state refusals.
- `SAFE_UNKNOWN_SITE_INFO` when a field cannot be read safely.

Audit requirements:

- Log route, outcome, actor class, no secrets.

Rollback relevance:

- None.

SAFE UNKNOWN:

- Exact fields may be reduced if hosting/security plugins restrict access.

## READ: themes

Route:

- `GET /wp-json/wpilot/v1/themes`

Auth requirement:

- Token required.

Request schema:

- Empty.

Response schema:

```json
{
  "ok": true,
  "operation_id": "op_...",
  "data": {
    "active_theme": {"name": "Theme", "version": "x.y", "stylesheet": "theme"},
    "child_theme_active": true,
    "themes": [{"name": "Theme", "version": "x.y", "active": true}]
  },
  "warnings": []
}
```

Possible refusal reasons:

- Common auth/state refusals.
- `THEME_INFO_UNAVAILABLE`.

Audit requirements:

- Log read request and outcome.

Rollback relevance:

- None. Endpoint must not update themes.

SAFE UNKNOWN:

- Theme-specific builders and licensing signals may be incomplete.

## READ: plugins

Route:

- `GET /wp-json/wpilot/v1/plugins`

Auth requirement:

- Token required.

Request schema:

- Empty.

Response schema:

```json
{
  "ok": true,
  "operation_id": "op_...",
  "data": {
    "plugins": [
      {"name": "WPBakery Page Builder", "version": "x.y", "active": true}
    ]
  },
  "warnings": []
}
```

Possible refusal reasons:

- Common auth/state refusals.
- `PLUGIN_INFO_UNAVAILABLE`.

Audit requirements:

- Log read request and outcome.

Rollback relevance:

- None. Endpoint must not install, update, activate, deactivate, or delete plugins.

SAFE UNKNOWN:

- Exact plugin metadata may vary by WordPress permission and filesystem visibility.

## READ: pages

Route:

- `GET /wp-json/wpilot/v1/pages`

Auth requirement:

- Token required.

Request schema:

- Query params: `post_type` optional, default `page`; `limit` optional, capped by MVP constant.

Response schema:

```json
{
  "ok": true,
  "operation_id": "op_...",
  "data": {
    "items": [
      {"id": 123, "post_type": "page", "status": "publish", "title": "Sample"}
    ]
  },
  "warnings": []
}
```

Possible refusal reasons:

- Common auth/state refusals.
- `POST_TYPE_NOT_ALLOWED`.
- `LIMIT_TOO_LARGE`.

Audit requirements:

- Log route, post type, count, outcome.

Rollback relevance:

- None.

SAFE UNKNOWN:

- Draft/private visibility depends on capability checks.

## READ: page-read

Route:

- `GET /wp-json/wpilot/v1/pages/{id}`

Auth requirement:

- Token required.

Request schema:

- Path: `id` integer.

Response schema:

```json
{
  "ok": true,
  "operation_id": "op_...",
  "data": {
    "id": 123,
    "post_type": "page",
    "status": "publish",
    "title": "Sample",
    "content": "...",
    "content_checksum": "sha256:..."
  },
  "warnings": []
}
```

Possible refusal reasons:

- Common auth/state refusals.
- `TARGET_NOT_FOUND`.
- `POST_TYPE_NOT_ALLOWED`.
- `READ_NOT_ALLOWED`.

Audit requirements:

- Log target ID, outcome, checksum if generated.

Rollback relevance:

- None.

SAFE UNKNOWN:

- Returning full content may be restricted later if content contains secrets or PII.

## READ: structure-read

Route:

- `GET /wp-json/wpilot/v1/pages/{id}/structure`

Auth requirement:

- Token required.

Request schema:

- Path: `id` integer.

Response schema:

```json
{
  "ok": true,
  "operation_id": "op_...",
  "data": {
    "id": 123,
    "content_checksum": "sha256:...",
    "builder": "wpbakery",
    "nodes": [
      {"type": "shortcode", "name": "vc_row", "depth": 0, "zone": "structure"}
    ],
    "safe_unknown": []
  },
  "warnings": []
}
```

Possible refusal reasons:

- Common auth/state refusals.
- `TARGET_NOT_FOUND`.
- `STRUCTURE_PARSE_FAILED`.
- `STRUCTURE_SAFE_UNKNOWN`.

Audit requirements:

- Log target ID, parser outcome, no raw content dump.

Rollback relevance:

- Used for pre-write validation only; does not create rollback state.

SAFE UNKNOWN:

- Full WPBakery/The7 compatibility.

## READ: indexing-state

Route:

- `GET /wp-json/wpilot/v1/indexing-state`

Auth requirement:

- Token required.

Request schema:

- Optional `page_id` integer for page-specific frontend metadata check.

Response schema:

```json
{
  "ok": true,
  "operation_id": "op_...",
  "data": {
    "blog_public": "0",
    "robots_txt_observed": "SAFE_UNKNOWN",
    "frontend_meta_robots": "SAFE_UNKNOWN"
  },
  "warnings": []
}
```

Possible refusal reasons:

- Common auth/state refusals.
- `INDEXING_SIGNAL_UNAVAILABLE`.

Audit requirements:

- Log read request and outcome.

Rollback relevance:

- None. MVP does not modify indexing settings through this endpoint.

SAFE UNKNOWN:

- SEO/cache/security plugin behavior may hide or transform indexing signals.

## WRITE: backup-create

Route:

- `POST /wp-json/wpilot/v1/pages/{id}/backups`

Auth requirement:

- Token required, bridge enabled, DEV confirmed.

Request schema:

```json
{
  "reason": "pre_scoped_replace",
  "approval_ref": "human-approved-id"
}
```

Response schema:

```json
{
  "ok": true,
  "operation_id": "op_...",
  "data": {
    "backup_id": 1,
    "target_id": 123,
    "content_checksum": "sha256:..."
  },
  "warnings": []
}
```

Possible refusal reasons:

- Common auth/state refusals.
- `APPROVAL_REQUIRED`.
- `TARGET_NOT_FOUND`.
- `BACKUP_STORAGE_UNAVAILABLE`.
- `CHECKSUM_FAILED`.

Audit requirements:

- Log request, backup creation, backup ID, checksum, outcome.

Rollback relevance:

- Creates rollback source for plugin-created write.

SAFE UNKNOWN:

- Backup retention policy until implementation finalizes cleanup UI.

## WRITE: scoped-replace

Route:

- `POST /wp-json/wpilot/v1/pages/{id}/scoped-replace`

Auth requirement:

- Token required, bridge enabled, DEV confirmed, approval required for execute.

Request schema:

```json
{
  "mode": "dry_run",
  "before_text": "old text",
  "after_text": "new text",
  "match_mode": "exact_once",
  "approval_ref": "human-approved-id",
  "expected_checksum": "sha256:..."
}
```

Response schema:

```json
{
  "ok": true,
  "operation_id": "op_...",
  "data": {
    "mode": "dry_run",
    "target_id": 123,
    "match_count": 1,
    "allowed_zone": "plain_text",
    "backup_id": null,
    "before_checksum": "sha256:...",
    "after_checksum": null,
    "mutation_performed": false
  },
  "warnings": []
}
```

Execute mode response sets `mutation_performed: true`, includes `backup_id`, `after_checksum`, and `replacement_count`.

Possible refusal reasons:

- Common auth/state refusals.
- `APPROVAL_REQUIRED`.
- `MATCH_ZERO`.
- `MATCH_MULTIPLE`.
- `MATCH_AMBIGUOUS`.
- `FORBIDDEN_EDIT_ZONE`.
- `STRUCTURE_PARSE_FAILED`.
- `STRUCTURE_SAFE_UNKNOWN`.
- `CHECKSUM_MISMATCH`.
- `BACKUP_FAILED`.
- `WRITE_FAILED`.
- `POST_WRITE_VALIDATION_FAILED`.

Audit requirements:

- Log dry-run request, execute request, backup ID, write outcome, checksums, refusal stage.

Rollback relevance:

- Execute mode must create or reference plugin-created backup before mutation.

SAFE UNKNOWN:

- Some WPBakery/HTML structures may be refused until parser behavior is proven.

## WRITE: rollback

Route:

- `POST /wp-json/wpilot/v1/pages/{id}/rollback`

Auth requirement:

- Token required, bridge enabled, DEV confirmed, approval required.

Request schema:

```json
{
  "backup_id": 1,
  "approval_ref": "human-approved-id",
  "expected_current_checksum": "sha256:..."
}
```

Response schema:

```json
{
  "ok": true,
  "operation_id": "op_...",
  "data": {
    "target_id": 123,
    "backup_id": 1,
    "restored_checksum": "sha256:...",
    "mutation_performed": true
  },
  "warnings": ["manual_frontend_verification_required"]
}
```

Possible refusal reasons:

- Common auth/state refusals.
- `APPROVAL_REQUIRED`.
- `BACKUP_NOT_FOUND`.
- `BACKUP_TARGET_MISMATCH`.
- `BACKUP_CONTENT_UNAVAILABLE`.
- `CHECKSUM_MISMATCH`.
- `ROLLBACK_WRITE_FAILED`.
- `ROLLBACK_VALIDATION_FAILED`.

Audit requirements:

- Log rollback request, target, backup ID, outcome, checksum.

Rollback relevance:

- This is the rollback endpoint. It must only restore plugin-created backups.

SAFE UNKNOWN:

- Rollback cannot guarantee cache/CDN/frontend immediate visibility.

