# MetaCODE WPilot Plugin Concept

**Classification:** Planned WordPress bridge plugin concept.
**Chat type:** External Systems.
**Active lane:** B.
**Status:** PLANNED concept only; no plugin implementation in this repository.

## Definition

MetaCODE WPilot Plugin is a planned WordPress bridge plugin for human-supervised AI-assisted WordPress administration.

The plugin would expose controlled, authenticated, and logged operations so WPilot can inspect, and later modify, WordPress safely without relying on fragile phpMyAdmin/manual SQL workflows or repeated browser-click administration.

This document describes a future concept. It is not evidence that a plugin, runtime bridge, autonomous admin layer, or production integration currently exists.

## Strategic Target Hierarchy

WPilot should not primarily evolve into a universal autonomous WordPress AI runtime.

The preferred strategic direction is:

1. **Primary target - Factory-native controlled sites.** WordPress sites created through MARS Website Factory with known stack, approved plugins/themes, structured block schemas, predictable layouts, known mutation zones, and Website Factory contracts.
2. **Secondary target - legacy/external compatibility bridge.** Existing WordPress sites with unknown or mixed builders, themes, plugins, and historical content shape.

This hierarchy affects safety posture. Factory-native sites may later support safer structured operations because the page/template/content contracts are known. Legacy/external sites remain refusal-first and dry-run-heavy because WPilot cannot assume layout, shortcode, theme, plugin, or content safety.

## MVP Status Labels

- **CORE** - required for the DEV-only plugin MVP.
- **OPERATIONAL** - already proven in human-supervised WPilot DEV/testing workflows, outside plugin implementation.
- **PARTIALLY OPERATIONAL** - proven only as limited DEV evidence, not generalized implementation.
- **PLANNED** - intended plugin behavior without implementation evidence in this repository.
- **EXPERIMENTAL** - optional future exploration, outside MVP.
- **DEV-ONLY** - allowed only on explicitly confirmed development/test sites.
- **EXCLUDED** - not allowed in the plugin MVP.
- **SAFE UNKNOWN** - unresolved until implementation or site-specific evidence exists.

## DEV-ONLY MVP Scope

The plugin MVP is **DEV-ONLY**. It should be installed only on a development or test WordPress site by a human site owner or authorized administrator.

The MVP must start disabled, require explicit enablement in WordPress admin, and expose no operational endpoint until both plugin enablement and authentication checks pass.

## What It Is Not

MetaCODE WPilot Plugin is not:

- An autonomous admin.
- A backdoor.
- A hidden deploy bot.
- An unrestricted database shell.
- A public SaaS plugin.
- A production runtime.
- Credential storage.
- Proof that WPilot or MARS controls any WordPress site.
- Arbitrary SQL execution.
- Unrestricted filesystem access.
- PHP, shell, JavaScript, or template code execution.

## Core Idea

The plugin would act as a narrow operational bridge between a managed WordPress site and WPilot documentation/workflows.

Its role is to make site inspection and tightly scoped changes more reliable by exposing explicit operations with authentication, permission checks, backups, logs, and rollback paths. It should avoid broad administrative power and should preserve human approval as the final authority for risky writes.

## Operational Modes

WPilot has two strategic operating modes. These are planning labels and operator policy, not runtime mode switches.

| Mode | Target | Automation posture | Mutation posture |
|---|---|---|---|
| **Mode A - Factory-native controlled sites** | WordPress sites produced from Website Factory contracts, approved templates, approved content pipeline, and known implementation zones. | More predictable inspection and dry-run planning may be possible after implementation evidence exists. | Structured content operations only, bounded by template/content schemas, backup, diff preview, and human approval. |
| **Mode B - legacy/external sites** | Existing sites using WPBakery, The7, Elementor, unknown plugins/themes, legacy HTML, shortcode fragments, or unmanaged content history. | Refusal-first, read-only first, dry-run-heavy, conservative compatibility bridge. | Exact scoped edits only when safe; otherwise refuse and escalate. |

Mode A is the long-term preferred target because Website Factory can define the stack and content boundaries before WordPress publication. Mode B exists to inspect and assist legacy/external sites without pretending they are structurally safe.

WPBakery handling belongs to **Mode B legacy compatibility**. It is useful for current DEV/test validation and existing site support, but it is not the ideal long-term operational target for WPilot.

## MVP Filesystem Structure

The planned plugin should remain a small WordPress plugin, not a broad site-control framework.

Recommended compact structure:

- `metacode-wpilot.php` - plugin bootstrap, activation/deactivation hooks, route registration.
- `includes/AdminPage.php` - enablement switch, status screen, token rotation/revocation, safety warnings.
- `includes/Auth.php` - per-site token validation and administrator capability checks.
- `includes/RestController.php` - narrow REST route handlers.
- `includes/PageInspector.php` - read-only page and structure inspection.
- `includes/WPBakeryMap.php` - shortcode-aware structural map helper.
- `includes/PageBackup.php` - plugin-created page backup snapshots.
- `includes/ScopedReplace.php` - single-target replacement after approval and backup checks.
- `includes/AuditLog.php` - operation logging without secrets.

No MVP file should act as a file manager, shell bridge, SQL console, code executor, plugin updater, theme updater, or WordPress core updater.

## Primary Goals

- Read WordPress structure.
- Read pages and posts.
- Parse WPBakery content.
- Expose safe structural maps.
- Create backups before changes.
- Perform scoped content edits.
- Support rollback.
- Log all operations.
- Require operator approval for risky writes.

## Security Principles

- Disabled by default.
- Explicit enablement in WordPress admin.
- Token-based authentication for REST calls.
- Per-site secret generated in WordPress admin and stored hashed where feasible.
- Token rotation and revocation.
- Administrator capability checks for configuration and risky operations.
- Optional IP allowlist.
- Operation allowlist.
- No arbitrary SQL in MVP.
- No file manager in MVP.
- No unrestricted filesystem access in MVP.
- No code execution in MVP.
- No plugin, theme, or WordPress core updates in MVP.
- Audit log for every request.
- Emergency kill switch.
- No credentials, tokens, cookies, database dumps, or `wp-config.php` copies stored in this repository.
- No plaintext token values in audit logs.
- Operator-side token files, backups, and rollback snapshots belong only in ignored local operational storage described by `local-storage-policy.md`; they are not plugin source, source-pack content, or runtime proof.

## Authentication Model

**CORE / PLANNED:** REST calls must require a per-site token and pass WordPress capability checks appropriate to the operation.

Minimum MVP rules:

- The plugin is disabled by default.
- A human administrator explicitly enables the bridge.
- A per-site token is generated in WordPress admin.
- Token values are shown only at creation/rotation time.
- Tokens can be revoked or rotated by an administrator.
- Failed authentication attempts are logged without storing the submitted token.
- Read-only routes and write-like routes share authentication, but write-like routes require stronger approval evidence.

## Approval Boundary

Read-only operations may be allowed after authentication and plugin enablement.

Write-like operations must remain scoped, logged, reversible, and operator-approved. Risky writes should require an approval token, dry-run preview, or equivalent human confirmation before execution.

The plugin should not silently edit production content, update software, install code, bypass WordPress permissions, or expand its own privileges.

For Factory-native Mode A, approval should be tied to Website Factory artifacts: approved page blueprint, approved template/content payload, approved SEO/content workflow, diff preview, and human-approved publishing decision. For legacy Mode B, approval is necessary but not sufficient; unclear structure, unsafe builder zones, raw HTML/script/style regions, or ambiguous matches must still be refused.

## Possible API Endpoints

The exact route prefix and authentication mechanism are future implementation details. Candidate endpoints:

- **CORE / PLANNED:** `GET /site-info`
- **CORE / PLANNED:** `GET /plugins`
- **CORE / PLANNED:** `GET /themes`
- **CORE / PLANNED:** `GET /pages`
- **CORE / PLANNED:** `GET /page/{id}`
- **CORE / PLANNED:** `GET /page/{id}/wpbakery-map`
- **CORE / PLANNED:** `POST /page/{id}/backup`
- **CORE / PLANNED:** `POST /page/{id}/replace-text`
- **CORE / PLANNED:** `POST /page/{id}/rollback`
- **DEV-ONLY / PLANNED:** `GET /seo/indexing-state`
- **DEV-ONLY / PLANNED:** `POST /seo/dev-isolation`
- **CORE / PLANNED:** `GET /logs`

## Endpoint Intent

`GET /site-info` would return sanitized WordPress and environment facts that are safe for operator review.

`GET /plugins` and `GET /themes` would expose plugin/theme names, versions, activation state, and child-theme status without performing updates.

`GET /pages` and `GET /page/{id}` would support read-only content inspection.

`GET /page/{id}/wpbakery-map` would parse WPBakery shortcode structure into a safer structural map for review before any edit.

`POST /page/{id}/backup` would create a reversible pre-change snapshot for the specific target page.

`POST /page/{id}/replace-text` would perform a scoped text replacement only after backup and approval requirements are satisfied.

`POST /page/{id}/rollback` would restore the target page from an approved plugin-created backup.

`GET /seo/indexing-state` would read indexing-related signals such as WordPress visibility settings, SEO plugin state where safely detectable, and frontend robots metadata.

`POST /seo/dev-isolation` would provide a controlled helper for development-site isolation only if explicitly enabled and approved.

`GET /logs` would expose operation history for audit and reporting.

## Rollback Model

**CORE / PLANNED:** every write-like operation must be rollback-first.

Minimum MVP rules:

- A plugin-created backup snapshot is required before `replace-text`.
- Backup scope is the target page/post content only, not a full-site backup replacement.
- Rollback restores only from plugin-created backups for the approved target.
- Rollback actions are logged.
- The plugin does not replace hosting-panel backups or human rollback planning.
- Failed backup creation blocks the write.

## Audit Log Model

**CORE / PLANNED:** every request path should produce an operation log entry without storing secrets.

Minimum event fields:

- Timestamp.
- Route and operation.
- Actor class or WordPress user ID where safely available.
- Target type and target ID.
- Request outcome: accepted, rejected, failed, rolled back.
- Approval reference where applicable.
- Backup reference where applicable.
- Sanitized error code or reason.

Audit storage remains **SAFE UNKNOWN** until implementation chooses a custom table, WordPress option storage, or export-oriented format.

## Scoped Replacement Safety

**CORE / PLANNED:** replacement is limited to one approved page/post and one approved occurrence unless a human explicitly approves a different scoped operation.

The MVP should:

- Use WordPress APIs for content reads and writes, not arbitrary SQL endpoints.
- Require backup-before-write.
- Support dry-run or diff preview before mutation.
- Refuse ambiguous matches by default.
- Refuse mass replacement.
- Refuse writes to plugins, themes, WordPress core, `wp-config.php`, uploads, and arbitrary filesystem paths.
- Log accepted, rejected, failed, and rollback outcomes.

## WPBakery-Aware Parsing Strategy

**CORE / PLANNED:** WPBakery handling should be shortcode-aware, conservative, and reviewable.

The MVP parser should:

- Detect common WPBakery shortcode blocks such as `vc_row`, `vc_column`, `vc_column_text`, and `vc_raw_html`.
- Return a structural map sufficient for human review and scoped replacement planning.
- Preserve shortcode attributes and nesting when content is written back.
- Treat raw HTML, encoded fragments, unknown shortcodes, theme wrappers, and deeply nested structures as **SAFE UNKNOWN** unless tested.
- Avoid claiming full WPBakery rendering, design fidelity, or universal theme compatibility.

WPBakery support is a **legacy compatibility strategy**, not the preferred future content model. Factory-native sites should prefer approved templates, structured block/content schemas, and known mutation zones instead of reverse-engineering historical shortcode content.

## Factory-Native Structured Content Strategy

For Website Factory-created WordPress sites, future WPilot integration should prefer structured operations over page-string mutation.

Conceptual inputs may include:

- approved Website Factory page blueprints;
- approved page templates and template slots;
- section payloads mapped to known block IDs;
- approved SEO/content fields;
- known mutation zones declared by the implementation pack;
- human approval artifacts for publish/update decisions.

Conceptual operations may include:

- create or update a draft page from an approved template/content payload;
- validate that a payload matches an approved template slot before write planning;
- produce a dry-run diff between current WordPress draft content and approved Factory content;
- publish only after human approval, rollback plan, and audit record are present.

These are future integration directions only. This document does not claim that Website Factory currently exports WordPress-ready payloads or that WPilot can create, update, or publish pages.

## Future Blog/Page Agent Integration Direction

Future blog or page generation should integrate through Website Factory-style contracts, not direct autonomous CMS edits.

The intended direction:

- Blog/page content is generated as approved artifacts first, outside WordPress mutation.
- Content is mapped to approved page templates and structured content slots.
- SEO titles, descriptions, headings, internal links, schema candidates, and CTA intent are reviewed before WordPress handoff.
- WPilot receives only human-approved draft/update instructions with explicit target, diff, rollback, and publish gate.
- Publishing remains human-approved; WPilot should not self-approve, schedule, or silently publish generated content.

Until a concrete Blog Agent card, content artifact contract, and WordPress publication contract exist, this remains **SAFE UNKNOWN**.

## Operational Boundaries

- The plugin should be installed only by a human site owner or authorized administrator.
- The plugin should start disabled.
- The plugin should not expose arbitrary PHP, shell, SQL, or filesystem access.
- The plugin should not execute code supplied by WPilot, the operator, a REST request, or page content.
- The plugin should not replace hosting-panel backups or human rollback planning.
- The plugin should not be treated as a public marketplace plugin until it has a separate security review, threat model, and release process.

## SAFE UNKNOWN

- Exact WordPress permission model, endpoint routing, nonce/token design, and storage choice remain future implementation decisions.
- WPBakery parsing reliability is unknown until tested against real page content variants.
- Compatibility with specific themes, SEO plugins, cache layers, and security plugins is unknown until site-specific inspection.
- Production safety is unknown until a real implementation has authentication, authorization, logging, rollback, and security review evidence.
- Exact filesystem layout may change during implementation, but the MVP boundary must remain narrow and non-executing.
- Factory-native WordPress export format, template-slot schema, content payload schema, publish approval artifact, and Blog Agent integration contract are not defined yet.
