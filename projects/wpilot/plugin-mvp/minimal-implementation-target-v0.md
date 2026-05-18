# WPilot Minimal Implementation Target v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** first realistic coding milestone for the installable plugin MVP.

This target answers: what is the smallest real plugin version considered operationally successful?

## Milestone Definition

The first successful implementation is a local ZIP-installable WordPress plugin that can:

1. Activate disabled by default.
2. Let an administrator explicitly confirm DEV use and enable the bridge.
3. Generate, rotate, and revoke a per-site token.
4. Serve authenticated read-only endpoints.
5. Create a plugin-owned backup for one page.
6. Dry-run one exact scoped replacement.
7. Execute one approved exact scoped replacement after backup.
8. Roll back that page from the plugin-created backup.
9. Log all accepted/refused/failed/succeeded write-relevant events.
10. Refuse unsafe or ambiguous operations with stable error codes.

## Minimal File Count

Target implementation should stay near this minimum:

- 1 bootstrap file.
- 1 uninstall file.
- 2 admin files.
- 4 API/auth/permission/request files.
- 4 storage/schema files.
- 3 rollback/checksum files.
- 3 parser/replacement files.
- 2 logging files.
- 2 shared helper files.
- 1 minimal admin CSS file.

Approximate target: 20-22 source files, not counting readme/license.

This is a ceiling guideline, not a requirement to split files prematurely. Fewer files are acceptable if boundaries remain clear.

## Minimal Endpoint Set

Required for first operational milestone:

Read:

- `GET /wp-json/wpilot/v1/ping`
- `GET /wp-json/wpilot/v1/site-info`
- `GET /wp-json/wpilot/v1/themes`
- `GET /wp-json/wpilot/v1/plugins`
- `GET /wp-json/wpilot/v1/pages`
- `GET /wp-json/wpilot/v1/pages/{id}`
- `GET /wp-json/wpilot/v1/pages/{id}/structure`

Write:

- `POST /wp-json/wpilot/v1/pages/{id}/backups`
- `POST /wp-json/wpilot/v1/pages/{id}/scoped-replace`
- `POST /wp-json/wpilot/v1/pages/{id}/rollback`

Optional for first milestone:

- `GET /wp-json/wpilot/v1/indexing-state`

## Minimal Admin UI

Required admin UI:

- DEV-only warning.
- Bridge state display.
- DEV confirmation checkbox/control.
- Enable/disable bridge control.
- Token generate/rotate/revoke controls.
- Storage/schema status.
- Emergency disable control.
- Link or compact view for latest audit events.

Not required:

- Rich dashboards.
- Charts.
- External exports.
- Background jobs.
- SaaS settings.

## Minimal DB Requirements

Required:

- Backup table.
- Audit log table.
- Option storage for enabled/dev/schema/token state.
- Token hash storage.
- Schema version tracking.

Not required:

- External log export.
- Full retention automation.
- Multi-site schema support.
- Full backup archive management.

## Minimal Write Support

Supported write:

- One exact text replacement.
- One target page.
- One exact occurrence.
- WordPress API write only.
- Backup created first.
- Human approval reference required.
- WPBakery structure check required.
- Post-write validation required.

Not supported:

- Regex.
- Wildcards.
- Fuzzy matching.
- Multiple replacements.
- HTML restructuring.
- Shortcode attribute edits.
- Raw HTML edits.
- SQL fallback.
- Filesystem fallback.

## Minimal Rollback Support

Supported rollback:

- Restore `post_content` from plugin-created backup.
- Backup target must match page ID.
- WordPress API write only.
- Post-rollback checksum required.
- Manual frontend verification required.

Not supported:

- Full-site restore.
- Database restore.
- Filesystem restore.
- Rollback from external backup archive.
- Automatic rollback after failed write unless explicitly requested by human.

## Minimal Validation Requirements

Before write:

- Bridge enabled.
- DEV confirmed.
- Token valid.
- Approval reference present.
- Target exists.
- Target post type allowed.
- Content checksum generated.
- Target text appears exactly once.
- WPBakery boundary map is safe enough.
- Backup created.
- Audit preflight created.

After write:

- New content read back.
- Replacement count verified.
- Checksum generated.
- Audit outcome written.
- Response includes manual verification reminder.

## Operational Success Criteria

The milestone is successful when a human operator can perform this sequence on a confirmed DEV site:

1. Install ZIP.
2. Activate plugin and see disabled state.
3. Enable DEV bridge.
4. Generate token.
5. Call read-only endpoints.
6. Select test page.
7. Create backup.
8. Dry-run exact replacement.
9. Execute approved replacement.
10. Verify page manually.
11. Roll back from backup.
12. Verify rollback manually.
13. Review audit log.
14. Disable bridge or revoke token.

## Non-Success Conditions

The milestone is not successful if:

- Plugin enables bridge by default.
- Unauthenticated operational endpoint works.
- Token cannot be revoked.
- Write can occur without backup.
- Write can occur without approval reference.
- Ambiguous match is modified.
- WPBakery boundary corruption occurs.
- Rollback target can mismatch.
- Audit log misses write-relevant events.
- Any EXCLUDED capability is present.

## First Coding Milestone Name

Recommended milestone label:

- `WPilot Plugin DEV MVP v0.1`

Classification:

- **CORE / PLANNED / DEV-ONLY** until implemented and validated.

