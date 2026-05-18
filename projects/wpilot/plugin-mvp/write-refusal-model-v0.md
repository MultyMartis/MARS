# WPilot Write Refusal Model v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** deterministic refusal codes for future WPilot Phase 2 write-like operations.

Safe refusal is a successful safety behavior. Refusal responses must be compact JSON, deterministic, and free of secrets.

## Standard Envelope

```json
{
  "ok": false,
  "error": {
    "code": "WRITE_DISABLED",
    "message": "Write operations are disabled.",
    "stage": "state",
    "mutation_performed": false,
    "rollback_available": false
  },
  "meta": {}
}
```

Rules:

- `code` is stable and machine-readable.
- `message` is short and operator-readable.
- `stage` identifies where processing stopped.
- `mutation_performed` must be accurate.
- `rollback_available` is true only for a specific plugin-created backup.
- No token, auth header, cookie, credential, SQL, stack trace, or filesystem internals may appear.

## Refusal Codes

| Code | HTTP | Stage | Operator meaning | Retry guidance |
|---|---:|---|---|---|
| `WRITE_DISABLED` | 403 | `state` | Write toggle is off or write state is not active. | Enable write mode only in DEV after operator sign-off. |
| `DRY_RUN_REQUIRED` | 409 | `dry_run` | Execute was requested without a matching accepted dry-run. | Run dry-run again and execute with the same inputs/checksum. |
| `PAGE_NOT_FOUND` | 404 | `validation` | Target page does not exist or is not readable as an MVP target. | Verify page ID with read endpoint. |
| `MULTIPLE_MATCHES` | 409 | `dry_run` | Source text appears more than once. | Provide a narrower exact source string. |
| `ZERO_MATCHES` | 404 | `dry_run` | Source text does not appear in current content. | Refresh page content and retry with current exact text. |
| `UNSAFE_WPBAKERY_ZONE` | 422 | `wpbakery` | Match is inside or crosses a forbidden builder zone. | Use a safer plain text target or edit manually. |
| `BACKUP_FAILED` | 500 | `backup` | Required plugin-owned backup could not be created or verified. | Do not execute; fix storage/config and retry dry-run. |
| `CHECKSUM_MISMATCH` | 409 | `checksum` | Content changed or checksum no longer matches approved plan. | Re-read content and repeat dry-run. |
| `CONTENT_TOO_LARGE` | 413 | `validation` | Content exceeds safe scan or structure-analysis bounds. | Reduce target scope or handle manually. |
| `UNSAFE_CONTENT_TYPE` | 422 | `validation` | Target content type, encoding, or zone is unsupported. | Use supported page text content only. |
| `ROLLBACK_REQUIRED` | 500 | `post_write_validation` | Mutation may have occurred and verification failed. | Review rollback availability and perform supervised rollback. |
| `MUTATION_ABORTED` | 409 | `write` | Execution stopped before write because safety conditions changed. | Repeat dry-run and execute only if still accepted. |
| `SAFE_UNKNOWN` | 422 | `safe_unknown` | Plugin cannot classify the condition safely. | Manual inspection required; do not force mutation. |

## Code Details

### WRITE_DISABLED

Use when write mode is off, missing, inconsistent, or emergency-disabled.

Mutation must not be attempted. Response should not read target content if state refusal occurs first.

### DRY_RUN_REQUIRED

Use when execute lacks a valid dry-run reference or the execute input differs from dry-run input.

Mutation must not be attempted.

### PAGE_NOT_FOUND

Use when the target page cannot be found through WordPress APIs or is not readable as an allowed MVP target.

Mutation must not be attempted.

### MULTIPLE_MATCHES

Use when exact source string appears more than once.

The plugin must not choose a match, replace all matches, or ask AI to disambiguate.

### ZERO_MATCHES

Use when exact source string is absent.

The plugin must not guess, fuzzy match, normalize into a match, or inspect rendered browser output to bypass stored-content mismatch.

### UNSAFE_WPBAKERY_ZONE

Use when the match is in a forbidden or unstable WPBakery zone.

Examples: shortcode names, attributes, boundaries, `vc_raw_html`, encoded blocks, script/style, HTML tag syntax, malformed nesting.

### BACKUP_FAILED

Use when required backup creation, storage, linkage, or checksum verification fails.

Mutation must not be attempted without backup.

### CHECKSUM_MISMATCH

Use when current content checksum differs from dry-run, request, or backup expectations.

Mutation must not proceed because content may have changed.

### CONTENT_TOO_LARGE

Use when safe scanning, counting, or structure analysis exceeds configured bounds.

Partial scanning must not produce a false safe result.

### UNSAFE_CONTENT_TYPE

Use when target content is unsupported, encoded, non-page, binary-like, generated outside approved field, or otherwise outside MVP.

### ROLLBACK_REQUIRED

Use after mutation may have occurred and post-write verification fails.

Response must identify whether a plugin-created backup is available without exposing raw content.

### MUTATION_ABORTED

Use when execution stops before write because a safety invariant changed after dry-run.

Examples: match span changed, occurrence count changed, write target changed, final pre-write plan no longer matches.

### SAFE_UNKNOWN

Use when the plugin lacks enough evidence to classify safety.

SAFE UNKNOWN is not success and must not trigger fallback mutation.

## HTTP Status Guidance

- `401`: auth missing/invalid/revoked, inherited from auth model.
- `403`: state, permission, or write disabled.
- `404`: target or exact source missing.
- `409`: stale dry-run, checksum mismatch, changed content, ambiguous matches.
- `413`: content too large.
- `422`: unsafe or unsupported content/zone.
- `500`: internal storage/write/verification failure after accepted operation.

## Retry Safety

Retry is allowed only after the operator corrects the cause.

Never retry by:

- Disabling validation.
- Broadening match mode.
- Replacing all matches.
- Skipping backup.
- Ignoring checksum mismatch.
- Falling back to SQL/filesystem/browser automation.

