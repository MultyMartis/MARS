# WPilot DEV Install Checklist v0

**Status:** CORE / OPERATIONAL / DEV-ONLY.
**Scope:** operator checklist for first live DEV install of MetaCODE WPilot.

Use this checklist on a disposable or clearly DEV WordPress environment only.

## Preflight

- [ ] Confirm target site is DEV/test, not production.
- [ ] Confirm administrator access is available.
- [ ] Confirm REST API is enabled.
- [ ] Confirm recovery access exists if plugin activation fails.
- [ ] Confirm no token will be pasted into repo files or public logs.

## ZIP Build

- [ ] Start from `projects/wpilot/plugin/metacode-wpilot/`.
- [ ] Confirm root folder is `metacode-wpilot`.
- [ ] Create `metacode-wpilot.zip`.
- [ ] Confirm ZIP does not include `.git`, parent repo folders, local logs, screenshots, or credentials.

## Plugin Upload

- [ ] Open `Plugins > Add New > Upload Plugin`.
- [ ] Upload `metacode-wpilot.zip`.
- [ ] Confirm WordPress recognizes `MetaCODE WPilot`.
- [ ] Confirm no external service connection is requested.

## Activation

- [ ] Activate plugin.
- [ ] Confirm activation does not edit content.
- [ ] Open `Settings > MetaCODE WPilot`.
- [ ] Confirm admin page is visible.
- [ ] Confirm REST namespace shows `wpilot/v1`.

## Default State

- [ ] Confirm bridge is disabled by default.
- [ ] Confirm write state is disabled/unavailable.
- [ ] Confirm emergency disabled is false.
- [ ] Confirm token is not generated automatically.
- [ ] Call `GET /wp-json/wpilot/v1/ping` and confirm minimal success.

## DEV Enablement

- [ ] Check DEV/test confirmation.
- [ ] Enable read-only bridge.
- [ ] Save bridge state.
- [ ] Confirm bridge enabled state is visible.
- [ ] Confirm writes remain unavailable.

## Token Generation

- [ ] Click `Generate / Rotate Token`.
- [ ] Copy token immediately.
- [ ] Refresh admin page.
- [ ] Confirm plaintext token is no longer shown.
- [ ] Store token only in approved local operator secret storage.

## Endpoint Auth Validation

- [ ] Call data endpoint without token and confirm refusal.
- [ ] Call data endpoint with invalid token and confirm refusal.
- [ ] Call data endpoint with valid token and confirm success.
- [ ] Confirm success envelope uses `ok`, `data`, `meta`.
- [ ] Confirm error envelope uses `ok`, `error`, `meta`.

## Read-only Endpoint Validation

- [ ] Validate `GET /site-info`.
- [ ] Validate `GET /themes`.
- [ ] Validate `GET /plugins`.
- [ ] Validate `GET /pages`.
- [ ] Validate `GET /pages/{id}` on a safe DEV page.
- [ ] Validate `GET /pages/{id}/structure` on a safe DEV page.
- [ ] Validate `GET /indexing-state`.
- [ ] Confirm no endpoint mutates content.

## WPBakery Detection

- [ ] Test one plain page.
- [ ] Test one simple WPBakery page.
- [ ] Test one nested WPBakery page if available.
- [ ] Confirm `has_wpbakery` is false for plain page.
- [ ] Confirm `has_wpbakery` is true for WPBakery page.
- [ ] Confirm `shortcode_counts` is stable across repeated reads.
- [ ] Confirm malformed/disposable shortcode page produces warnings, not repair.

## Refusal Validation

- [ ] Bridge disabled returns `BRIDGE_DISABLED`.
- [ ] Missing token returns `AUTH_MISSING`.
- [ ] Invalid token returns `AUTH_INVALID`.
- [ ] Revoked or absent token returns `TOKEN_REVOKED`.
- [ ] Emergency disabled returns `EMERGENCY_DISABLED`.
- [ ] DEV not confirmed blocks token generation or endpoint use.
- [ ] Invalid page ID returns `TARGET_NOT_FOUND`.
- [ ] Unsupported write-like endpoints are absent.

## Emergency Disable

- [ ] Confirm a read endpoint succeeds with valid token.
- [ ] Click `Emergency Disable`.
- [ ] Retry the same endpoint.
- [ ] Confirm `EMERGENCY_DISABLED`.
- [ ] Clear emergency state.
- [ ] Confirm bridge remains disabled after clearing emergency.

## Uninstall Expectations

- [ ] Deactivate plugin through WordPress if validation is complete.
- [ ] Confirm deactivation disables bridge behavior.
- [ ] Remove plugin only if operator intends cleanup.
- [ ] Confirm no content rollback is expected because no content mutation is implemented.
- [ ] Confirm no token is retained outside approved local secret storage.

## Stop Conditions

Stop validation if:

- Site appears to be production.
- Token is exposed.
- Any endpoint mutates content.
- Any write-like endpoint responds as implemented behavior.
- Admin page exposes token hash or secrets.
- WordPress shows fatal activation errors.

## Completion Criteria

- [ ] Plugin installs and activates in DEV.
- [ ] Admin page is visible.
- [ ] Bridge is disabled by default.
- [ ] Token generation is explicit and one-time display only.
- [ ] Read-only endpoints work only under expected auth/state conditions.
- [ ] WPBakery detection is observable and non-mutating.
- [ ] Refusals are deterministic.
- [ ] Emergency disable overrides operational access.
- [ ] No write operations are implemented or observed.
