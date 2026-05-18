# WPilot Live DEV Validation Plan v0

**Status:** CORE / OPERATIONAL / DEV-ONLY.
**Scope:** first live DEV installation validation for the installable MetaCODE WPilot plugin foundation.

This plan validates the read-only plugin foundation in a real WordPress DEV environment. It does not validate mutation, rollback execution, browser automation, autonomous repair, arbitrary SQL, or filesystem management.

## 1. ZIP Packaging Process

1. Start from `projects/wpilot/plugin/metacode-wpilot/`.
2. Confirm the folder name inside the ZIP is exactly `metacode-wpilot`.
3. Package the folder as `metacode-wpilot.zip`.
4. Do not include repo metadata, local credentials, screenshots, logs, cache files, or parent directories.
5. Expected ZIP root:

```text
metacode-wpilot/
```

Operational check:

- CORE: ZIP installs through WordPress plugin upload.
- EXCLUDED: build pipeline, dist artifact, composer/npm packaging.

## 2. Expected Plugin Folder Structure

Expected after extraction:

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

Validation passes only if all PHP files remain under this plugin folder.

## 3. WordPress Version Assumptions

- CORE: WordPress with REST API support.
- OPERATIONAL: WordPress 6.x DEV install preferred.
- SAFE UNKNOWN: exact lower bound is not validated until live install.
- EXCLUDED: production installation claim.

## 4. PHP Assumptions

- CORE: PHP version supported by the target WordPress install.
- OPERATIONAL: PHP 8.x DEV runtime preferred.
- SAFE UNKNOWN: PHP CLI may not be available on the operator machine; syntax checks may need hosting/WordPress validation.
- EXCLUDED: custom runtime or standalone PHP execution outside WordPress.

## 5. Installation Steps

1. Log in as a WordPress administrator.
2. Open `Plugins > Add New > Upload Plugin`.
3. Upload `metacode-wpilot.zip`.
4. Install but do not assume bridge is enabled.
5. Confirm the plugin appears as `MetaCODE WPilot`.

Expected:

- Plugin installs without writing site content.
- No external service connection is requested.
- No token is generated during install.

## 6. Activation Steps

1. Activate `MetaCODE WPilot`.
2. Open `Settings > MetaCODE WPilot`.
3. Confirm state is disabled by default.
4. Confirm write state says unavailable in this phase.
5. Confirm REST namespace is `wpilot/v1`.

Expected:

- `bridge_enabled = false`.
- `write_enabled = false`.
- `emergency_disabled = false`.
- `token_hash` absent/empty until manual generation.

Rollback expectation for failed activation:

- Deactivate the plugin if WordPress allows it.
- Remove the plugin through WordPress plugin management if needed.
- No content rollback is expected because activation must not mutate content.

## 7. DEV Enablement Flow

1. On `Settings > MetaCODE WPilot`, check `I confirm this is DEV/test use`.
2. Check `Enable read-only bridge`.
3. Save bridge state.
4. Confirm state becomes enabled but still read-only.

Expected:

- Bridge is explicit operator action.
- DEV confirmation is required before token generation.
- Writes remain EXCLUDED.

## 8. Token Generation Flow

1. With DEV confirmed and bridge enabled, click `Generate / Rotate Token`.
2. Copy the generated token immediately.
3. Refresh the admin page.
4. Confirm the plaintext token is not shown again.

Expected:

- Plaintext token appears once.
- Stored state shows token generated.
- No token appears in files, logs, or repo artifacts.

## 9. Endpoint Validation Sequence

Recommended order:

1. `GET /wp-json/wpilot/v1/ping` without token.
2. `GET /wp-json/wpilot/v1/site-info` without token.
3. `GET /wp-json/wpilot/v1/site-info` with invalid token.
4. `GET /wp-json/wpilot/v1/site-info` with valid token.
5. `GET /wp-json/wpilot/v1/themes` with valid token.
6. `GET /wp-json/wpilot/v1/plugins` with valid token.
7. `GET /wp-json/wpilot/v1/pages` with valid token.
8. Select a safe DEV test page ID.
9. `GET /wp-json/wpilot/v1/pages/{id}` with valid token.
10. `GET /wp-json/wpilot/v1/pages/{id}/structure` with valid token.
11. `GET /wp-json/wpilot/v1/indexing-state` with valid token.

Expected:

- Success envelope: `ok: true`, `data`, `meta`.
- Error envelope: `ok: false`, `error.code`, `error.message`, `meta`.
- No endpoint mutates content.

## 10. Refusal Validation Sequence

1. Bridge disabled: all data endpoints refuse with `BRIDGE_DISABLED`.
2. Missing token: enabled bridge data endpoints refuse with `AUTH_MISSING` when token exists.
3. Invalid token: refuse with `AUTH_INVALID`.
4. Token revoked or absent: refuse with `TOKEN_REVOKED`.
5. DEV not confirmed: refuse with `DEV_NOT_CONFIRMED`.
6. Emergency disabled: refuse with `EMERGENCY_DISABLED`.
7. Invalid page ID: refuse with `TARGET_NOT_FOUND`.
8. Unsupported route/method: WordPress REST 404 or method refusal.

## 11. Emergency-disable Validation

1. Enable bridge and generate token.
2. Verify one authenticated read endpoint succeeds.
3. Click `Emergency Disable`.
4. Retry the same endpoint with valid token.
5. Confirm refusal with `EMERGENCY_DISABLED`.
6. Clear emergency state.
7. Confirm bridge remains disabled after clearing emergency.

Expected:

- Emergency disable overrides bridge/token state.
- Clearing emergency does not silently re-enable bridge.

## 12. Rollback Expectations For Failed Activation

- PARTIALLY OPERATIONAL: WordPress plugin deactivation/removal is the expected recovery path.
- CORE: no page/post content rollback is needed because this phase must not mutate content.
- SAFE UNKNOWN: hosting-specific fatal error recovery may require file manager or WP-CLI access by the human operator.
- EXCLUDED: automated rollback execution.

## 13. SAFE UNKNOWN Areas

- Exact WordPress/PHP minimum versions until tested on target hosting.
- Hosting/security plugin behavior around REST headers.
- Whether active plugin metadata is fully readable on all hosts.
- Whether private/draft page visibility needs stricter capability policy.
- Full The7/WPBakery compatibility beyond shortcode signal detection.
- External robots.txt behavior; current validation is local signal only.
