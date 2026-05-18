# WPilot Plugin Structure Validation Report v0

**Status:** CORE / PARTIALLY OPERATIONAL / DEV-ONLY.
**Scope:** static structure and safety validation for `projects/wpilot/plugin/metacode-wpilot/`.

This report validates the current plugin foundation before first live DEV installation. It is not proof of live WordPress activation.

## Validation Summary

| Check | Status | Result |
|---|---|---|
| Plugin folder exists | CORE / OPERATIONAL | `projects/wpilot/plugin/metacode-wpilot/` exists. |
| Required files exist | CORE / OPERATIONAL | Bootstrap, includes, admin page, and README are present. |
| Plugin header exists | CORE / OPERATIONAL | `metacode-wpilot.php` contains a WordPress plugin header. |
| ABSPATH guards exist | CORE / OPERATIONAL | All PHP files include an `ABSPATH` guard. |
| REST namespace consistency | CORE / OPERATIONAL | Namespace constant is `wpilot/v1`. |
| REST route consistency | CORE / OPERATIONAL | Only the Phase 1 read routes are registered. |
| Settings registration | CORE / OPERATIONAL | Admin page is registered under WordPress Settings. |
| Admin capability | CORE / OPERATIONAL | Admin page requires `manage_options`. |
| Admin nonce usage | CORE / OPERATIONAL | Admin actions use WordPress nonce validation. |
| Token storage | CORE / OPERATIONAL | Token hash is stored; plaintext is generated only for immediate display. |
| Write endpoints | EXCLUDED / OPERATIONAL | No write REST endpoints found. |
| Mutation calls | EXCLUDED / OPERATIONAL | No `wp_update_post`, `wp_insert_post`, or `wp_delete_post` calls found. |
| Direct SQL mutation | EXCLUDED / OPERATIONAL | No `$wpdb` usage found in current plugin files. |
| Filesystem manipulation features | EXCLUDED / OPERATIONAL | No file manager, arbitrary read/write, or code execution feature found. |
| Background jobs | EXCLUDED / OPERATIONAL | No cron/background worker registration found. |

## Expected Structure

```text
metacode-wpilot/
  metacode-wpilot.php
  includes/
    class-wpilot-plugin.php
    class-wpilot-settings.php
    class-wpilot-auth.php
    class-wpilot-rest-controller.php
    class-wpilot-response.php
    class-wpilot-site-reader.php
    class-wpilot-wpbakery-detector.php
  admin/
    class-wpilot-admin-page.php
  README.md
```

## REST Route Validation

Registered routes are expected to use `WP_REST_Server::READABLE` only:

- `/ping`
- `/site-info`
- `/themes`
- `/plugins`
- `/pages`
- `/pages/(?P<id>[\d]+)`
- `/pages/(?P<id>[\d]+)/structure`
- `/indexing-state`

Validation rule:

- OPERATIONAL: no `CREATABLE`, `EDITABLE`, `DELETABLE`, broad catch-all mutation route, or POST route appears in REST registration.

## Settings And Admin Validation

Admin UI expectations:

- Located under `Settings > MetaCODE WPilot`.
- Shows plugin state.
- Shows bridge enabled/disabled.
- Shows write disabled/unavailable.
- Shows token status.
- Shows REST namespace.
- Provides bridge enable/disable control.
- Provides token generate/rotate and revoke controls.
- Provides emergency disable and clear controls.

Admin POST handling is limited to option state changes and token lifecycle. It is not a content mutation feature.

## Token Storage Validation

Expected behavior:

- `wp_hash_password()` stores token hash.
- `wp_check_password()` validates submitted token.
- Plaintext token is returned only by admin generation flow.
- No static plaintext token exists in plugin files.

SAFE UNKNOWN:

- Exact password hashing algorithm is WordPress-version dependent.

## Safety Exclusions Confirmed

Current plugin structure does not provide:

- write REST endpoint
- rollback execution
- arbitrary SQL endpoint
- file manager
- arbitrary filesystem write
- shell/code execution
- plugin/theme/core modification
- browser automation
- autonomous repair
- background jobs

## Remaining Live Validation

The following require real WordPress DEV installation:

- Activation behavior.
- Admin page rendering.
- REST header behavior through hosting/security layers.
- Auth refusal payloads.
- Read payload shape with real site data.
- WPBakery shortcode detection against real pages.
