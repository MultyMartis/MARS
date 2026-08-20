# MetaCODE WPilot

MetaCODE WPilot is a DEV/test WordPress plugin foundation for the WPilot bridge: read-only inspection plus backup/rollback recovery for page `post_content`.

## Phase

- Phase 0: installable plugin skeleton, activation/deactivation, admin settings, disabled-by-default bridge state, token generation foundation.
- Phase 1: authenticated read-only REST endpoints under `wpilot/v1`.
- Sprint 1 (v0.2.0): plugin-owned backup storage, audit log, `POST /pages/{id}/backups`, `POST /pages/{id}/rollback`.
- Sprint 2 (v0.3.0): `POST /pages/{id}/scoped-replace` execute for `apply_content_change` (exact once, page `post_content` only).

No arbitrary SQL, filesystem writes, or production scope in this phase.

## Install

1. Copy or zip the `metacode-wpilot` folder.
2. Install it through WordPress admin plugins.
3. Activate the plugin.
4. Open `Settings > MetaCODE WPilot`.
5. Confirm DEV/test use and enable the read-only bridge.
6. Generate a token and copy it immediately. The plaintext token is shown only once.

## REST Auth

All endpoints except `GET /wp-json/wpilot/v1/ping` require:

```http
X-WPilot-Token: <generated token>
```

**Do not** use `Authorization: Bearer` for MetaCODE WPilot. That is a different auth model. Wrong-header probes that time out or return 401 are **INVALID EVIDENCE** of site health — classify `AUTH_ERROR` / `TRANSPORT_ERROR` separately from `VALID_RUNTIME_RESPONSE` (see Forge anti-patterns **WPILOT-001…003**).

Only the token hash is stored in WordPress options.

## Read-only Endpoints

- `GET /wp-json/wpilot/v1/ping`
- `GET /wp-json/wpilot/v1/site-info`
- `GET /wp-json/wpilot/v1/themes`
- `GET /wp-json/wpilot/v1/plugins`
- `GET /wp-json/wpilot/v1/pages`
- `GET /wp-json/wpilot/v1/pages/{id}`
- `GET /wp-json/wpilot/v1/pages/{id}/structure`
- `GET /wp-json/wpilot/v1/indexing-state`
- `POST /wp-json/wpilot/v1/pages/{id}/replace-text/dry-run` (requires write_enabled)
- `POST /wp-json/wpilot/v1/pages/{id}/backups`
- `POST /wp-json/wpilot/v1/pages/{id}/scoped-replace` (requires write_enabled)
- `POST /wp-json/wpilot/v1/pages/{id}/rollback` (requires write_enabled)

## Safety Boundaries

This plugin does not implement arbitrary SQL, filesystem management, code execution, plugin/theme/core modification, browser automation, background jobs, or autonomous behavior.
