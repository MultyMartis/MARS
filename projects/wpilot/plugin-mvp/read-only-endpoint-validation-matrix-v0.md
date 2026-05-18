# WPilot Read-only Endpoint Validation Matrix v0

**Status:** CORE / OPERATIONAL / DEV-ONLY.
**Scope:** live DEV validation matrix for `wpilot/v1` read-only endpoints.

All data endpoints except `ping` require `X-WPilot-Token`. All endpoint responses must use the deterministic envelope shape:

```json
{"ok": true, "data": {}, "meta": {}}
```

or:

```json
{"ok": false, "error": {"code": "string", "message": "string"}, "meta": {}}
```

## Matrix

| Endpoint | Auth | Expected success payload | Refusal behavior | HTTP codes | WPBakery relevance |
|---|---|---|---|---|---|
| `GET /ping` | No token required | plugin, status, bridge_enabled, write_enabled false, state | Should not expose token or sensitive config | 200 | None |
| `GET /site-info` | Token required | site_url, home_url, wp_version, php_version, active_theme, is_multisite, bridge_enabled, write_enabled false | bridge/auth/state refusals | 200, 401, 403 | None |
| `GET /themes` | Token required | active theme name, version, template, stylesheet | bridge/auth/state refusals | 200, 401, 403 | Indirect theme context |
| `GET /plugins` | Token required | active plugins name, version, plugin_file | bridge/auth/state refusals | 200, 401, 403 | Confirms WPBakery active plugin when present |
| `GET /pages` | Token required | list of id, title, status, modified, link, has_wpbakery | bridge/auth/state refusals | 200, 401, 403 | `has_wpbakery` per page |
| `GET /pages/{id}` | Token required | id, title, status, modified, content_raw, content_checksum, has_wpbakery | state/auth refusals; invalid page refusal | 200, 401, 403, 404 | Detects WPBakery on target page |
| `GET /pages/{id}/structure` | Token required | id, has_wpbakery, shortcode_counts, basic_integrity, warnings | state/auth refusals; invalid page refusal | 200, 401, 403, 404 | Primary WPBakery structure endpoint |
| `GET /indexing-state` | Token required | blog_public, robots_txt_available, discourage_search_engines, notes | bridge/auth/state refusals | 200, 401, 403 | None |

## Safe Test Procedure

1. Begin with bridge disabled.
2. Call `ping` without token and confirm success.
3. Call each data endpoint without token and confirm refusal.
4. Enable DEV bridge and generate token.
5. Repeat each data endpoint with valid token.
6. Capture only response shape and non-secret field presence.
7. Do not store the token in repo files, screenshots, public logs, or validation docs.
8. Use a disposable DEV page for page and structure endpoints.

## Endpoint-specific Failure Conditions

### ping

Failure conditions:

- Does not respond after plugin activation.
- Exposes token hash, plaintext token, filesystem paths, or stack trace.
- Claims write capability is enabled.

### site-info

Failure conditions:

- Succeeds when bridge is disabled.
- Succeeds with missing/invalid token.
- Exposes sensitive server paths or credentials.
- Reports `write_enabled` as true.

### themes

Failure conditions:

- Succeeds with missing/invalid token.
- Mutates theme state.
- Lists inactive themes beyond MVP expectation if not intentionally expanded.

### plugins

Failure conditions:

- Succeeds with missing/invalid token.
- Installs, activates, deactivates, updates, or deletes plugins.
- Exposes filesystem paths beyond plugin file identifiers.

### pages

Failure conditions:

- Succeeds with missing/invalid token.
- Returns more than the MVP capped list.
- Mutates page status/content.
- Omits `has_wpbakery`.

### page-read

Failure conditions:

- Succeeds with missing/invalid token.
- Reads non-page post types in MVP.
- Mutates content.
- Omits checksum.
- Returns token or admin credentials in payload.

### structure-read

Failure conditions:

- Succeeds with missing/invalid token.
- Mutates content.
- Claims edit safety beyond read-only shortcode signal detection.
- Omits `shortcode_counts`, `basic_integrity`, or `warnings`.

### indexing-state

Failure conditions:

- Succeeds with missing/invalid token.
- Writes SEO/search settings.
- Claims external crawler truth from local-only signals.

## Expected Refusal Codes

- `BRIDGE_DISABLED`: bridge disabled.
- `DEV_NOT_CONFIRMED`: DEV/test use not confirmed.
- `EMERGENCY_DISABLED`: emergency stop active.
- `AUTH_MISSING`: token header missing.
- `AUTH_INVALID`: token invalid.
- `TOKEN_REVOKED`: token absent/revoked.
- `TARGET_NOT_FOUND`: invalid page ID.

Unsupported endpoints should use WordPress REST 404 or method errors rather than plugin-specific success.
