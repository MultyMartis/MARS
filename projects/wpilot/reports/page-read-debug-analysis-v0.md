# WPilot Page Read Debug Analysis v0

**Date:** 2026-05-19
**Scope:** `projects/wpilot/plugin/metacode-wpilot/**`
**Mode:** controlled debugging and stabilization only.

## Observed Failure

- `GET /wp-json/wpilot/v1/pages/{id}` returned HTTP 500 with a generic WordPress critical error page.
- `GET /wp-json/wpilot/v1/pages/{id}/structure` returned HTTP 500 with a generic WordPress critical error page.
- Token auth, refusal model, page list, site-info, themes, plugins, ping, and indexing-state were reported working.

## Primary Root Cause Finding

The two failing routes were the only active WPilot read routes using a REST path parameter validator:

```php
'validate_callback' => 'is_numeric',
```

WordPress REST validation callbacks receive more than one argument. Passing the PHP internal function `is_numeric` directly can produce an argument-count fatal on PHP 8+ when WordPress calls the validator with the route value, request object, and parameter key. That failure occurs before the endpoint handler can return the WPilot JSON envelope, matching the observed generic WordPress critical error page.

The route validators were replaced with WPilot-owned callbacks that accept the route value safely and ignore extra callback arguments by method signature behavior.

## Secondary Failure Risks Found

- Page detail returned `content_raw` directly from `WP_Post::post_content`; invalid UTF-8 could break JSON serialization in edge cases.
- The structure endpoint ran regex scans directly on unchecked content.
- `preg_match_all()` retained all matches, which is unnecessary for counts and can increase memory pressure on large WPBakery/The7 pages.
- Endpoint handlers did not catch reader/detector exceptions, so unexpected runtime failures could still escape as raw WordPress fatal output.
- Request ID and metadata handling was already bounded and did not expose token values.

## Stabilization Applied

- Replaced direct `is_numeric` route validation with WPilot-owned `validate_page_id()` and `sanitize_page_id()` methods.
- Switched page ID access from array-style request access to `get_param( 'id' )`.
- Added JSON-safe content normalization through `wp_check_invalid_utf8()` where available.
- Added plain-text title fallback with `wp_strip_all_tags()`.
- Added safe fallbacks for status, modified time, and permalink values.
- Added bounded WPBakery shortcode scanning:
  - maximum scan window: 1 MiB;
  - maximum count per shortcode pattern: 10,000;
  - no retention of full match payloads.
- Added guarded regex execution with suppressed regex warnings and deterministic fallback counts.
- Added controlled page and structure endpoint exception envelopes:
  - `PAGE_READ_FAILED`;
  - `PAGE_STRUCTURE_READ_FAILED`.

## Error Envelope Behavior

On guarded runtime failure after auth succeeds, page endpoints now return:

```json
{
  "ok": false,
  "error": {
    "code": "PAGE_READ_FAILED",
    "message": "Page read failed safely."
  },
  "meta": {}
}
```

or:

```json
{
  "ok": false,
  "error": {
    "code": "PAGE_STRUCTURE_READ_FAILED",
    "message": "Page structure read failed safely."
  },
  "meta": {}
}
```

The actual response `meta` is populated through the existing WPilot request metadata builder.

## Live Probe Evidence

Public live probe:

- `GET https://dev.gktriumph.ru/wp-json/wpilot/v1/ping`
- Result: HTTP 200 JSON envelope.
- Bridge snapshot: `bridge_enabled=true`, `dev_confirmed=true`, `write_enabled=false`, `state=token-generated`.

Invalid-token live probe:

- `GET https://dev.gktriumph.ru/wp-json/wpilot/v1/site-info` with `X-WPilot-Token: invalid-test-token`
- Result: HTTP 401 JSON refusal path.

Invalid-token page route probe:

- `GET https://dev.gktriumph.ru/wp-json/wpilot/v1/pages/1` with `X-WPilot-Token: invalid-test-token`
- Result: HTTP 500 HTML failure.
- `GET https://dev.gktriumph.ru/wp-json/wpilot/v1/pages/1/structure` with `X-WPilot-Token: invalid-test-token`
- Result: HTTP 500 HTML failure.

This confirms the failure is specific to the `{id}` routes and occurs before normal token refusal handling can return the WPilot envelope.

## Logging Strategy

Minimal logging was added only for environments where `WP_DEBUG` is true.

Logged fields:

- endpoint name;
- sanitized numeric page ID;
- exception class;
- sanitized exception message capped at 240 characters.

Not logged:

- tokens;
- authorization headers;
- cookies;
- raw page content;
- shortcode payloads;
- credentials;
- filesystem paths beyond what WordPress/PHP might include in the exception message.

## Security Validation Notes

- No write endpoints were introduced.
- No mutation logic was introduced.
- No arbitrary SQL was introduced.
- No filesystem manipulation was introduced.
- No autonomous behavior was introduced.
- No token logging was introduced.
- Raw fatal output exposure is reduced for handler-level failures; route-level validator fatal risk was removed for the page ID routes.

## Remaining SAFE UNKNOWN

- SAFE UNKNOWN: live WordPress runtime behavior must be verified after deploying/updating the DEV plugin files.
- SAFE UNKNOWN: exact PHP fatal log line from the original 500 was not available in the repository.
- SAFE UNKNOWN: WPBakery/The7 third-party filters may still affect `get_the_title()`, permalink generation, or content handling in ways not provable statically.
- SAFE UNKNOWN: fatal errors outside handler execution, such as unrelated plugin/theme boot failures, cannot be caught by the endpoint envelope.
