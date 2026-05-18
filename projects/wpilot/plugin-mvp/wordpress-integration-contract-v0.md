# WPilot WordPress Integration Contract v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** WordPress integration rules for first plugin implementation.

The MVP must behave like a small WordPress plugin, not a runtime orchestrator, deployment tool, browser automation system, file manager, or SQL console.

## Bootstrap Lifecycle

Bootstrap file:

- `metacode-wpilot.php`

Responsibilities:

- Define plugin constants.
- Load required classes.
- Register activation/deactivation hooks.
- Initialize admin page hooks.
- Register REST routes on WordPress REST initialization.

Rules:

- Do not process external input during file load.
- Do not expose operational behavior before WordPress hooks run.
- Do not enable bridge during bootstrap.
- Do not generate token during bootstrap.

## Activation Hook

Activation must:

- Create or validate plugin-owned tables.
- Set `wpilot_enabled = false`.
- Set `wpilot_dev_confirmed = false`.
- Set plugin/schema version options.
- Leave token absent unless already present from previous install and policy allows reuse.
- Report visible admin error if storage setup fails.

Activation must not:

- Modify site content.
- Modify plugins/themes/core.
- Edit files.
- Generate background jobs.
- Contact external SaaS/cloud services.
- Enable bridge automatically.

## Deactivation Behavior

Deactivation must:

- Disable bridge operation.
- Preserve plugin-owned audit and backup records.
- Preserve options unless WordPress removes plugin state separately.

Deactivation must not:

- Delete backups automatically.
- Roll back content automatically.
- Delete pages/posts.
- Revoke external credentials, because the plugin must not own them.

## Uninstall Behavior

Uninstall may:

- Remove plugin-owned options.
- Remove plugin-owned tables.

Uninstall must not:

- Modify page content.
- Delete WordPress content.
- Delete users.
- Delete uploads.
- Delete plugins/themes/core.
- Touch external backups.

## Admin Page Strategy

Admin page must provide:

- DEV-only warning.
- Current bridge state.
- Storage/schema status.
- Enable/disable bridge control.
- DEV confirmation control.
- Token generate/rotate/revoke controls.
- Emergency disable control.
- Minimal audit/backup status summary or links.

Admin actions must require:

- `manage_options` or implementation-selected administrator capability.
- WordPress nonce validation.
- Sanitized form input.
- Audit event without secrets.

## REST Registration Strategy

Register routes under:

- `wpilot/v1`

Route registration must:

- Use explicit allowlist.
- Provide permission callbacks.
- Reject disabled/emergency/invalid-config states.
- Return standardized response envelopes.
- Avoid registering broad catch-all mutation endpoints.

No route may:

- Execute arbitrary SQL.
- Read arbitrary filesystem paths.
- Write arbitrary filesystem paths.
- Execute code.
- Update plugins/themes/core.
- Trigger browser automation.

## Capability Checks

Minimum capability model:

- Admin configuration: `manage_options`.
- Read endpoints: token auth plus allowed operation state.
- Write endpoints: token auth, DEV confirmed, bridge enabled, approval reference, backup/audit checks.
- Rollback endpoint: token auth, DEV confirmed, bridge enabled, valid plugin-created backup.

SAFE UNKNOWN:

- Exact capability names may be adjusted during implementation for least privilege, but MVP must not broaden access silently.

## Nonce Usage

Use WordPress nonces for:

- Admin enable/disable actions.
- DEV confirmation save.
- Token generate/rotate/revoke.
- Emergency disable.
- Manual cleanup if implemented.

REST token-authenticated API calls do not rely on admin nonces as the primary auth model, but must still validate all request fields.

## Permission Callback Rules

Every REST route must have a permission callback.

Permission callback should verify:

- Plugin state allows route.
- Token is present and valid where required.
- Token is not revoked.
- Operation is allowlisted.
- DEV confirmation is present for write-like endpoints.
- Emergency disabled is false.
- Config/schema state is valid.

Permission callback must not:

- Mutate content.
- Create backups.
- Perform write validation side effects beyond safe audit/refusal logging.

## Allowed WordPress APIs

**CORE / PLANNED allowed APIs:**

- Plugin activation/deactivation hook APIs.
- Options APIs for plugin options.
- WordPress database APIs only for plugin-owned tables.
- REST API route registration.
- Capability and nonce APIs.
- `get_post`, `get_posts`, `WP_Query` for allowed read operations.
- `wp_update_post` or equivalent WordPress content API for approved page content writes.
- Theme/plugin metadata read APIs.
- WordPress site option read for indexing visibility.

## Forbidden Direct Manipulation Patterns

**EXCLUDED:**

- Direct SQL update of `wp_posts.post_content` for scoped replace.
- SQL supplied by request.
- Filesystem writes to themes/plugins/core/uploads.
- `eval`, dynamic PHP execution, shell execution.
- Direct editing of `wp-config.php`.
- Direct plugin/theme/core updates.
- Direct option writes for SEO plugins except future separately approved contracts.
- Browser automation.
- External deployment/update calls.

## WP API Usage Requirements

For content writes:

- Read current content through WordPress APIs.
- Create plugin backup before mutation.
- Validate checksum before write.
- Write through WordPress content API.
- Read back after write.
- Validate expected result.
- Log outcome.

For rollback:

- Validate plugin-created backup.
- Write through WordPress content API.
- Read back after rollback.
- Validate checksum.
- Log outcome.

## Admin Security Notes

- Admin pages must escape output.
- Admin forms must sanitize input.
- Token value is shown only once.
- Audit displays must not reveal raw content dumps by default.
- Error output must be sanitized.

