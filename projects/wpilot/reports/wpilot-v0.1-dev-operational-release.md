# WPilot v0.1 DEV Operational Release

## Release Identity

WPilot v0.1 is frozen as the DEV operational baseline before Phase 2B mutation implementation.

This release represents an installable WordPress plugin with a protected REST bridge, read-only inspection, WPBakery/The7 structure awareness, and Phase 2A dry-run validation. It does not include real mutation endpoints.

## 1. Operational Capabilities

- Installable WordPress plugin package under `metacode-wpilot/`.
- Disabled-by-default activation and deactivation behavior.
- Admin-controlled DEV/test confirmation, bridge enablement, dry-run readiness, token generation, token revocation, and emergency disable.
- Header-token authentication through `X-WPilot-Token`.
- Public bridge ping endpoint with no token exposure.
- Protected read endpoints for site info, active theme, active plugins, page list, page detail, page structure, and indexing state.
- Deterministic JSON success and refusal envelopes.
- Page content checksum reporting for read and dry-run validation.
- WPBakery shortcode detection and conservative structure signals.
- Phase 2A exact-text replacement dry-run analyzer with explicit `mutation_performed=false` refusal details.

## 2. Live-Tested Capabilities

Live DEV validation has confirmed:

- Plugin ZIP can be packaged with POSIX archive paths and installed on the DEV site.
- Public ping responds with bridge state.
- Authenticated REST bridge accepts the current DEV token.
- Page-read and page-structure routes operate without the prior route validator failure.
- WPBakery/The7 page content can be inspected through read-only endpoints.
- Dry-run readiness persists after admin save when DEV confirmation and bridge enablement are both true.
- Phase 2A dry-run returns deterministic JSON refusals for `ZERO_MATCHES`, `INVALID_REQUEST`, and invalid-token auth cases.
- A safe single-occurrence dry-run can return `ok=true`, `dry_run=true`, `would_replace=true`, and `match_count=1`.
- Before/after page content checksum remained stable during dry-run validation.

## 3. Security Boundaries

- The bridge is disabled by default on activation and deactivation.
- REST data endpoints require the documented token header except for public ping.
- Token generation is gated by DEV/test confirmation and bridge enablement.
- Plaintext tokens are shown once in the admin UI and are not stored by the plugin.
- Stored token state is hash-based.
- Emergency disable turns off the bridge and dry-run readiness.
- Dry-run readiness is not write authorization; it only allows the analyzer route to run.
- Response envelopes are designed not to expose plaintext tokens, auth headers, SQL, stack traces, or raw debug dumps.
- Page detail intentionally exposes raw page content only to authenticated DEV operators.

## 4. WPBakery/The7 Compatibility Status

- The release supports conservative inspection of WPBakery shortcode presence and basic structure signals.
- Page detail reports whether content appears to contain WPBakery shortcodes.
- Page structure reports known shortcode counts, basic `vc_row` balance, and warning signals.
- Dry-run validation refuses unsafe shortcode zones, raw WPBakery blocks, HTML tag spans, and script/style regions.
- The7 compatibility is validated only through the tested DEV site behavior and available WPBakery content shape.

## 5. Dry-Run Validation Status

Phase 2A dry-run validation is frozen as dry-run only:

- Only exact single-occurrence replacement analysis is supported.
- Request scope is limited to `content_raw`.
- `expected_occurrences` must be exactly `1`.
- Unknown request fields are refused.
- Oversized content, oversized values, invalid UTF-8, shortcode-like replacement syntax, script/style replacement content, unsafe WPBakery zones, and ambiguous match counts are refused.
- The analyzer returns checksums and would-replace metadata but does not write content, create backups, persist audit logs, or execute rollback.

## 6. Explicit Exclusions

This release intentionally excludes:

- Real content mutation endpoints.
- Calls to `wp_update_post`, `wp_insert_post`, `wp_delete_post`, or post meta mutation APIs.
- Direct SQL mutation.
- Backup creation execution.
- Rollback execution.
- Durable audit-log persistence for real writes.
- Browser automation.
- Background jobs.
- Autonomous operation.
- Production enablement.
- AI-generated edits or AI decision logic.

## 7. Remaining SAFE UNKNOWN

- Live behavior is confirmed only for the tested DEV site, token, endpoint set, and page content available during validation.
- Third-party theme/plugin runtime filters may affect page metadata or content shape outside tested cases.
- Hosting-level fatal behavior outside WPilot handler execution cannot be fully controlled by the plugin.
- Production behavior is intentionally untested and unsupported.
- Real write safety, backup execution, rollback execution, and audit persistence remain unimplemented and unvalidated.
- Broader WPBakery/The7 content variants may require additional parser-aware safety checks before mutation.

## 8. Recommended Operational Usage

- Use only on approved DEV/test WordPress sites.
- Keep the bridge disabled unless an operator is actively validating or inspecting the DEV site.
- Generate or rotate tokens only after confirming DEV/test status and bridge readiness.
- Store plaintext tokens only in approved local operator secret storage.
- Prefer emergency disable after any unexpected behavior or after a validation window closes.
- Treat raw page content returned by read endpoints as sensitive DEV inspection data.
- Use dry-run output only as a pre-write signal; do not treat it as proof that mutation is safe.

## 9. Known Limitations

- No real write endpoint exists.
- No backup or rollback execution exists.
- No durable audit log exists for write operations.
- Operational state is stored in WordPress options.
- Read endpoint access depends on the current WordPress runtime and active plugins/theme.
- Dry-run safety is intentionally conservative and may refuse content requiring deeper parser awareness.
- Local PHP CLI validation availability was not proven during the prior readiness work.

## 10. Next Planned Phase

The next planned phase is Phase 2B: separately gated mutation sandbox design and implementation.

Before Phase 2B introduces any real mutation endpoint, the project should define and review:

- Exact mutation endpoint contract.
- Backup creation and retention behavior.
- Rollback execution semantics.
- Audit trail shape.
- Human approval workflow.
- Expanded live validation matrix.
- WPBakery/The7 mutation safety checks.
- Branch isolation strategy for mutation work.
