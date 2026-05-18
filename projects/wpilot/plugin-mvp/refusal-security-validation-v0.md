# WPilot Refusal And Security Validation v0

**Status:** CORE / OPERATIONAL / DEV-ONLY.
**Scope:** live DEV refusal and security validation for the read-only WPilot plugin foundation.

Validation philosophy:

- deterministic
- observable
- refusal-first
- rollback-safe
- operator-visible

Excluded:

- hidden recovery
- silent fallback
- autonomous repair
- write execution

## Expected Error Envelope

All plugin refusals should use:

```json
{
  "ok": false,
  "error": {
    "code": "string",
    "message": "string"
  },
  "meta": {}
}
```

No refusal may include plaintext token, token hash, SQL, stack trace, unrestricted filesystem path, cookies, passwords, or unrelated personal data.

## Refusal Matrix

| Scenario | Setup | Expected code | Expected HTTP | Operator-visible behavior |
|---|---|---|---|---|
| Bridge disabled | Activate plugin, leave bridge disabled, call data endpoint | `BRIDGE_DISABLED` | 403 | Admin page shows bridge disabled; data endpoint refuses. |
| Missing token | Bridge enabled, token exists, omit header | `AUTH_MISSING` | 401 | Endpoint tells operator token is required. |
| Invalid token | Bridge enabled, send wrong token | `AUTH_INVALID` | 401 | Endpoint refuses without revealing token state details. |
| Token absent/revoked | Bridge enabled, no active token | `TOKEN_REVOKED` | 401 | Admin page shows token absent or revoked. |
| Emergency disabled | Trigger emergency disable, call data endpoint | `EMERGENCY_DISABLED` | 403 | Admin page shows emergency disabled; endpoints refuse. |
| DEV not confirmed | Bridge state saved without DEV confirmation, call data endpoint | `DEV_NOT_CONFIRMED` | 403 | Operator must explicitly confirm DEV/test use. |
| Invalid page ID | Valid token, request nonexistent page ID | `TARGET_NOT_FOUND` | 404 | Endpoint refuses without fallback search. |
| Malformed request | Invalid route parameter or malformed path | WordPress REST validation/method error or `TARGET_NOT_FOUND` | 400 or 404 | No mutation, no stack trace. |
| Unsupported endpoint | Request unregistered WPilot path or unsupported method | WordPress REST 404 or method refusal | 404 or 405 | No plugin success envelope. |

## Bridge Disabled Validation

Procedure:

1. Activate plugin.
2. Do not enable bridge.
3. Call `GET /wp-json/wpilot/v1/site-info`.

Expected:

- HTTP 403.
- `ok = false`.
- `error.code = BRIDGE_DISABLED`.
- No page/theme/plugin data is returned.

## Invalid Token Validation

Procedure:

1. Enable DEV bridge.
2. Generate token.
3. Call a data endpoint with `X-WPilot-Token: invalid`.

Expected:

- HTTP 401.
- `error.code = AUTH_INVALID`.
- No sensitive details about stored hash or generated token.

## Missing Token Validation

Procedure:

1. Enable DEV bridge.
2. Generate token.
3. Call a data endpoint without `X-WPilot-Token`.

Expected:

- HTTP 401.
- `error.code = AUTH_MISSING`.

## Emergency Disabled Validation

Procedure:

1. Enable bridge and generate token.
2. Confirm a read endpoint succeeds.
3. Click `Emergency Disable`.
4. Retry with the same valid token.

Expected:

- HTTP 403.
- `error.code = EMERGENCY_DISABLED`.
- Clearing emergency keeps bridge disabled.

## DEV Not Confirmed Validation

Procedure:

1. Save bridge form without DEV confirmation.
2. Call a data endpoint with any token state.

Expected:

- HTTP 403.
- `error.code = DEV_NOT_CONFIRMED` when bridge is enabled but DEV confirmation is absent.
- Token generation should be blocked until DEV confirmation is present.

## Invalid Page ID Validation

Procedure:

1. Enable bridge and generate token.
2. Call `GET /wp-json/wpilot/v1/pages/999999999`.
3. Call `GET /wp-json/wpilot/v1/pages/999999999/structure`.

Expected:

- HTTP 404.
- `error.code = TARGET_NOT_FOUND`.
- No fallback query or broad search.

## Malformed Request Validation

Procedure:

1. Call malformed page paths, for example non-numeric IDs.
2. Call supported paths with unsupported methods such as POST.

Expected:

- WordPress REST validation error, 404, or 405 depending on request.
- No plugin content mutation.
- No stack trace or secret-bearing error.

## Unsupported Endpoint Validation

Procedure:

1. Call `/wp-json/wpilot/v1/pages/{id}/backups`.
2. Call `/wp-json/wpilot/v1/pages/{id}/scoped-replace`.
3. Call `/wp-json/wpilot/v1/pages/{id}/rollback`.

Expected:

- 404 or method refusal.
- No plugin success envelope.
- No backup, dry-run, replace, or rollback behavior exists in this phase.

## Security Risks To Watch

- Token copied into chat, docs, screenshots, terminal history, or issue tracker.
- Security plugins stripping `X-WPilot-Token` header.
- Raw page content containing private data returned by page-read.
- Active plugin list exposing operational details.
- DEV site accidentally being production-like.

## Pass Criteria

Validation passes only if:

- read endpoints require token except `ping`;
- disabled/emergency states refuse data endpoints;
- invalid/missing token refuses deterministically;
- unsupported write-like routes do not exist;
- no endpoint mutates WordPress content, plugins, themes, files, or database records beyond plugin option state.
