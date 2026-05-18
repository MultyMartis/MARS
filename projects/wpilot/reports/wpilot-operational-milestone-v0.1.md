# WPilot Operational Milestone v0.1

## Current Operational Capabilities

WPilot v0.1 is an installable DEV/test WordPress plugin with an authenticated REST bridge and deterministic JSON response envelopes.

Operational capabilities at this checkpoint:

- Disabled-by-default plugin activation state.
- Admin-controlled DEV/test confirmation, bridge enablement, emergency disable, token generation, and token revocation.
- Header-token authentication using `X-WPilot-Token`.
- Protected read endpoints for site info, active theme, active plugins, page list, page detail, page structure, and indexing state.
- Deterministic refusal responses for disabled bridge, missing DEV confirmation, emergency disable, missing/invalid/revoked token, invalid request shape, unsupported target, unsafe content, and dry-run refusal cases.
- WPBakery detection and conservative structure signals for page content.
- Phase 2A exact-text replacement dry-run endpoint with no content mutation, no backup execution, and no rollback execution.
- Dry-run write-readiness persistence gated by DEV confirmation, bridge enablement, and explicit admin save.

## What Is Live-Tested

Live DEV validation confirmed:

- The plugin can be packaged as a WordPress ZIP with POSIX archive paths and installed on the DEV site.
- Public ping responds with bridge state.
- Authenticated read bridge accepts the current DEV token.
- Page-read and page-structure routes no longer fail through the prior route validator issue.
- WPBakery/The7 page content can be inspected through read-only endpoints.
- Dry-run readiness persists after admin save when DEV confirmation and bridge enablement are both true.
- Phase 2A dry-run endpoint returns deterministic JSON refusals for `ZERO_MATCHES` and `INVALID_REQUEST`.
- Phase 2A dry-run endpoint can return `ok=true` for one safe, single-occurrence text fragment.
- Invalid token dry-run request returns JSON `AUTH_INVALID` with HTTP 401.
- Page content checksum remained unchanged before and after dry-run validation.

## What Is Intentionally Excluded

This milestone intentionally excludes:

- Real content mutation endpoints.
- Calls to `wp_update_post`, `wp_insert_post`, `wp_delete_post`, or post meta mutation APIs.
- Backup creation execution.
- Rollback execution.
- Audit-log persistence for real writes.
- Browser automation.
- Background jobs.
- Autonomous operation.
- Production enablement.
- Direct SQL mutation.

## Security Boundaries

Security boundaries at this checkpoint:

- The bridge is disabled by default on activation and deactivation.
- Token generation is allowed only after DEV/test confirmation and bridge enablement.
- Plaintext tokens are shown only once in admin UI and are not stored by the plugin.
- REST data endpoints require the documented token header except public ping.
- Dry-run write readiness is not a real write permission; it only allows the dry-run analyzer to run.
- Emergency disable turns bridge and write readiness off.
- Responses are deterministic JSON envelopes and are designed not to include tokens, auth headers, SQL, stack traces, or raw debug dumps.
- Live validation did not print or store the current DEV token.

## DEV-Only Constraints

WPilot v0.1 remains DEV/test only.

- Operators must not enable the bridge on production or production-like WordPress sites.
- Page detail can expose raw page content for inspection and must be used only on approved DEV content.
- Dry-run readiness is a controlled pre-write signal, not authorization for real mutation.
- Valid-token tests depend on the current DEV token and approved local operator handling.

## WPBakery/The7 Validation Status

WPBakery/The7 validation status:

- Page content inspection and page structure routes are operational in DEV.
- WPBakery detection is available through page detail and structure responses.
- The dry-run analyzer performs conservative shortcode, raw block, HTML tag, and script/style safety checks.
- Live dry-run validation confirmed a safe-zone result for one single-occurrence fragment on the DEV target page.

## Dry-Run Validation Status

Phase 2A dry-run validation status:

- `ZERO_MATCHES` returned deterministic JSON refusal.
- `INVALID_REQUEST` returned deterministic JSON refusal.
- A valid single-occurrence dry-run returned `ok=true`, `dry_run=true`, `would_replace=true`, and `match_count=1`.
- Response checksums were present for content-before, find, and replace values.
- No content mutation occurred.
- Before/after page content checksum remained stable.

## Remaining SAFE UNKNOWN

Remaining SAFE UNKNOWN:

- Live behavior is confirmed only for the tested DEV site, token, endpoint set, and page content available during validation.
- Third-party theme/plugin runtime filters may still affect page metadata or content shape outside the tested cases.
- Hosting-level fatal behavior outside WPilot handler execution cannot be fully controlled by the plugin.
- Real write safety, backup execution, rollback execution, and audit persistence remain unimplemented and unvalidated.
- Production behavior is intentionally untested and unsupported.

## Next Planned Phase

The next planned phase is a separately gated safe-write design and implementation phase.

Before any real mutation endpoint exists, the project should define and review:

- Exact write endpoint contract.
- Backup creation and retention behavior.
- Rollback execution semantics.
- Audit trail shape.
- Human approval workflow.
- Expanded live validation matrix.
- Additional WPBakery/The7 mutation safety checks.

## Known Limitations

Known limitations:

- No real write endpoint exists.
- No backup or rollback execution exists.
- No durable audit log exists for write operations.
- The plugin stores operational state in WordPress options only.
- The read page endpoint intentionally exposes raw content to authenticated DEV operators.
- Dry-run candidate safety is conservative and may refuse content that requires deeper parser awareness.
- PHP CLI validation was not available in the local shell environment during the readiness fix.
