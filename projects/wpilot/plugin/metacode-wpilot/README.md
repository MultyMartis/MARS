# MetaCODE WPilot

MetaCODE WPilot is a DEV/test WordPress plugin foundation for a read-only WPilot bridge.

## Phase

- Phase 0: installable plugin skeleton, activation/deactivation, admin settings, disabled-by-default bridge state, token generation foundation.
- Phase 1: authenticated read-only REST endpoints under `wpilot/v1`.

No write endpoints are implemented in this phase.

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

## Safety Boundaries

This plugin does not implement write operations, arbitrary SQL, filesystem management, code execution, plugin/theme/core modification, browser automation, background jobs, or autonomous behavior.
