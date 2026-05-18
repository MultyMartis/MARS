# WPilot Error And Refusal Model v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** standardized refusal and error contract for first plugin implementation.

The MVP philosophy is: safe refusal is better than unsafe action.

## Standard Error Structure

All non-success responses use:

```json
{
  "ok": false,
  "operation_id": "op_...",
  "error": {
    "code": "WPILOT_ERROR_CODE",
    "message": "Operator-readable message.",
    "stage": "validation",
    "mutation_performed": false,
    "rollback_available": false
  }
}
```

Rules:

- `code` is stable and machine-readable.
- `message` is short and operator-readable.
- `stage` identifies where processing stopped.
- `mutation_performed` must be false for refusals before write.
- `rollback_available` must be true only when a plugin-created backup can be used.
- No response includes secrets, token values, stack traces, SQL, or filesystem internals.

## Stages

Allowed stage values:

- `bootstrap`
- `state`
- `auth`
- `permission`
- `request`
- `validation`
- `dry_run`
- `backup`
- `checksum`
- `wpbakery`
- `write`
- `post_write_validation`
- `audit`
- `rollback`
- `safe_unknown`

## Security Refusals

| Code | Message | Stage |
|---|---|---|
| `BRIDGE_DISABLED` | Bridge is disabled. Enable it in plugin settings before using this endpoint. | `state` |
| `DEV_NOT_CONFIRMED` | DEV/test use has not been explicitly confirmed. | `state` |
| `EMERGENCY_DISABLED` | Bridge is emergency-disabled and requires administrator intervention. | `state` |
| `AUTH_MISSING` | Authentication token is required. | `auth` |
| `AUTH_INVALID` | Authentication token is invalid. | `auth` |
| `TOKEN_REVOKED` | Authentication token has been revoked. | `auth` |
| `PERMISSION_DENIED` | Current actor is not permitted to perform this operation. | `permission` |
| `DISALLOWED_OPERATION` | This operation is not allowed in the MVP. | `permission` |
| `SECRET_EXPOSURE_RISK` | Request or response would expose secret-bearing data. | `validation` |

## Validation Refusals

| Code | Message | Stage |
|---|---|---|
| `INVALID_REQUEST` | Request body is missing or malformed. | `request` |
| `TARGET_NOT_FOUND` | Target page or post was not found. | `validation` |
| `POST_TYPE_NOT_ALLOWED` | Target post type is not allowed in the MVP. | `validation` |
| `READ_NOT_ALLOWED` | Target cannot be read with current permissions. | `permission` |
| `APPROVAL_REQUIRED` | Human approval reference is required for this operation. | `validation` |
| `CHECKSUM_FAILED` | Content checksum could not be generated. | `checksum` |
| `CHECKSUM_MISMATCH` | Current content does not match the expected checksum. | `checksum` |
| `AUDIT_UNAVAILABLE` | Audit logging is unavailable for a required operation. | `audit` |
| `INVALID_CONFIG` | Plugin configuration is invalid or incomplete. | `state` |

## WPBakery Refusals

| Code | Message | Stage |
|---|---|---|
| `STRUCTURE_PARSE_FAILED` | Page structure could not be parsed safely. | `wpbakery` |
| `STRUCTURE_SAFE_UNKNOWN` | Page structure is SAFE UNKNOWN for this operation. | `wpbakery` |
| `FORBIDDEN_EDIT_ZONE` | Target text is inside a forbidden edit zone. | `wpbakery` |
| `MALFORMED_SHORTCODE` | Shortcode structure appears malformed. | `wpbakery` |
| `RAW_HTML_UNSAFE` | Target appears inside raw or encoded HTML that the MVP cannot safely edit. | `wpbakery` |
| `SHORTCODE_BOUNDARY_RISK` | Replacement would cross or modify shortcode boundaries. | `wpbakery` |

## Ambiguous Match Refusals

| Code | Message | Stage |
|---|---|---|
| `MATCH_ZERO` | Target text was not found. | `dry_run` |
| `MATCH_MULTIPLE` | Target text appears more than once. | `dry_run` |
| `MATCH_AMBIGUOUS` | Target match is ambiguous and cannot be edited safely. | `dry_run` |
| `REPLACEMENT_UNSAFE` | Replacement text contains unsupported or unsafe content. | `validation` |
| `MASS_REPLACE_EXCLUDED` | Mass replacement is excluded from the MVP. | `validation` |

## Backup And Rollback Failures

| Code | Message | Stage |
|---|---|---|
| `BACKUP_STORAGE_UNAVAILABLE` | Backup storage is unavailable. | `backup` |
| `BACKUP_FAILED` | Backup could not be created. | `backup` |
| `BACKUP_NOT_FOUND` | Requested backup was not found. | `rollback` |
| `BACKUP_TARGET_MISMATCH` | Backup does not belong to the requested target. | `rollback` |
| `BACKUP_CONTENT_UNAVAILABLE` | Backup content is unavailable. | `rollback` |
| `ROLLBACK_WRITE_FAILED` | Rollback write failed. | `rollback` |
| `ROLLBACK_VALIDATION_FAILED` | Rollback result could not be validated. | `rollback` |

## Write Failures

| Code | Message | Stage |
|---|---|---|
| `WRITE_FAILED` | WordPress content update failed. | `write` |
| `POST_WRITE_VALIDATION_FAILED` | Post-write validation failed; manual review is required. | `post_write_validation` |
| `MUTATION_UNVERIFIED` | Mutation result could not be verified. | `post_write_validation` |

## Disabled-Plugin Behavior

When the bridge is disabled:

- `ping` may report installed/disabled state.
- All authenticated operational endpoints refuse with `BRIDGE_DISABLED`.
- Write endpoints must not read target content before refusing.
- No mutation can occur.
- Refusal should be logged if audit storage is available.

## SAFE UNKNOWN Handling

Use `STRUCTURE_SAFE_UNKNOWN`, `SAFE_UNKNOWN_SITE_INFO`, or `INVALID_CONFIG` when the plugin cannot safely classify a condition.

Rules:

- SAFE UNKNOWN is not success.
- SAFE UNKNOWN must not trigger fallback mutation.
- Operator-readable message should say what evidence is missing.
- Implementation may suggest manual inspection, not automatic repair.

## Operator Message Rules

Messages should be:

- Short.
- Non-technical where possible.
- Clear about whether mutation occurred.
- Clear about whether rollback is available.

Messages must not:

- Include secret values.
- Include SQL.
- Include stack traces.
- Include full filesystem paths unless sanitized.
- Suggest bypassing safety checks.

