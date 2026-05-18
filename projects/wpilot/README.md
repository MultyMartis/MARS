# WPilot

**Classification:** Program / Operational System.
**Chat type:** External Systems.
**Status:** documented Phase 1 base.
**Model reference:** [System Entity Model](../../governance/system-entity-model.md).

WPilot is a human-supervised AI-assisted WordPress administration system for testing whether a Cursor/operator workflow can safely inspect and make tightly scoped changes on a Beget-hosted test WordPress site.

## What WPilot Is

- A documentation-first operational system under `projects/`.
- A safe Phase 1 MVP for Beget-hosted WordPress test-site work.
- A human-supervised workflow pack for inspection, backup confirmation, rollback planning, low-risk file-level tests, WP admin copy/create tests, WPBakery/The7 structure inspection, child theme CSS patch tests, QA, and reporting.
- An External Systems lane because WordPress, Beget, hosting panels, databases, plugins, themes, and admin dashboards remain outside MARS ownership.

## What WPilot Is Not

- Not an autonomous WordPress admin.
- Not a MARS runtime component.
- Not a deploy bot.
- Not credential storage.
- Not a plugin/theme updater.
- Not proof that MARS owns or controls any WordPress site.

## Phase 1 Document Map

- [phase-1-mvp.md](phase-1-mvp.md) - MVP scope and workflow sequence.
- [boundaries.md](boundaries.md) - ownership, external-system, and forbidden-claim boundaries.
- [beget-test-plan.md](beget-test-plan.md) - Beget-hosted test-site run plan.
- [backup-rollback-rules.md](backup-rollback-rules.md) - backup confirmation and rollback discipline.
- [access-safety.md](access-safety.md) - credential and access handling rules.
- [qa-checklist.md](qa-checklist.md) - Phase 1 QA gates.
- [reports/test-report-template.md](reports/test-report-template.md) - operator report template.
- [templates/site-passport-template.md](templates/site-passport-template.md) - sanitized site facts template.
- [templates/change-request-template.md](templates/change-request-template.md) - scoped change request template.
- [templates/rollback-plan-template.md](templates/rollback-plan-template.md) - rollback plan template.

## Plugin MVP Planning Pack

- [plugin-mvp/reconciliation-map-v0.md](plugin-mvp/reconciliation-map-v0.md) - CORE reconciliation map; start here before changing plugin planning docs.
- [metacode-wpilot-plugin-concept.md](metacode-wpilot-plugin-concept.md) - PLANNED canonical plugin concept, MVP boundaries, REST surface, auth, audit, rollback, scoped replacement, and WPBakery strategy.
- [metacode-wpilot-plugin-mvp-roadmap.md](metacode-wpilot-plugin-mvp-roadmap.md) - PLANNED DEV-only plugin MVP sequence and exclusions.

The plugin MVP planning pack is documentation only. It does not prove a WordPress plugin, runtime bridge, autonomous admin layer, production integration, or deployed code exists.

## Security Baseline

- No secrets in repo.
- No credentials, passwords, tokens, cookies, SSH keys, API keys, or hosting panel secrets.
- No `wp-config.php` copies or database dumps.
- No destructive SQL.
- No live production changes in MVP.
- No plugin or theme updates in MVP.
- No autonomous editing claims.

## Future Agent Candidates

Future WPilot roles may later belong in `agents/` only if the operator chooses to define bounded agent cards. Candidate roles include `wp-audit-agent`, `css-patch-agent`, `backup-rollback-agent`, `wp-admin-copy-agent`, and `qa-report-agent`.

Until then, they are candidate roles only, not running agents.

## SAFE UNKNOWN

- Exact Beget panel permissions, WordPress admin roles, FTP/SFTP access, and database visibility are unknown until the operator provides verified external evidence.
- The target site theme, child theme state, WPBakery usage, plugin list, and backup tooling are unknown until read-only inspection.
- Production safety is unknown unless the operator confirms the environment is a test site.
