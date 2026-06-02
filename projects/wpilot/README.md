# WPilot

**Classification:** Program / Operational System.
**Chat type:** External Systems.
**Status:** documented Phase 1 base.
**Model reference:** [System Entity Model](../../governance/system-entity-model.md).

WPilot is a human-supervised AI-assisted WordPress administration system for testing whether a Cursor/operator workflow can safely inspect and make tightly scoped changes on a Beget-hosted test WordPress site.

Strategic direction: WPilot's preferred long-term target is **Factory-native WordPress** created through MARS Website Factory contracts. Legacy/external WordPress support remains a secondary compatibility bridge for existing sites with unknown builders, themes, plugins, and content shape.

## What WPilot Is

- A documentation-first operational system under `projects/`.
- A safe Phase 1 MVP for Beget-hosted WordPress test-site work.
- A human-supervised workflow pack for inspection, backup confirmation, rollback planning, low-risk file-level tests, WP admin copy/create tests, WPBakery/The7 structure inspection, child theme CSS patch tests, QA, and reporting.
- A future bridge candidate for Website Factory-approved WordPress drafts, templates, structured content payloads, and human-approved publishing workflows.
- An External Systems lane because WordPress, Beget, hosting panels, databases, plugins, themes, and admin dashboards remain outside MARS ownership.

## What WPilot Is Not

- Not an autonomous WordPress admin.
- Not a MARS runtime component.
- Not a deploy bot.
- Not a universal autonomous WordPress AI runtime.
- Not credential storage.
- Not a plugin/theme updater.
- Not proof that MARS owns or controls any WordPress site.

## Strategic Modes

- **Mode A - Factory-native controlled sites:** primary target. Known stack, approved plugins/themes, approved templates, structured Website Factory content contracts, predictable layouts, known mutation zones, and human-approved publishing gates.
- **Mode B - legacy/external compatibility:** secondary target. WPBakery, The7, Elementor, unknown plugins/themes, historical HTML/content chaos, refusal-first inspection, dry-run-heavy validation, and conservative mutation policy.

WPBakery/The7 handling belongs to Mode B compatibility. It is valuable for the current DEV/testing baseline and existing site support, but it is not the ideal long-term WPilot target.

## Ecosystem Relationships (canonical visibility)

| System | Relationship |
|--------|--------------|
| **MARS Website Factory** | Planned upstream source for Factory-native WordPress payloads and controlled publishing handoffs (future direction, not runtime claim). |
| **OCPilot** | **Sibling** in CMS/Ecommerce Pilots family; shared safety/access patterns only, no parent-child ownership. |
| **EAR Runtime** | Future provider candidate for published acquisition snapshots; relationship is planned and bounded by separate charters. |
| **ORCA** | Strategy/semantic upstream context when WordPress implementation is part of broader marketing workflow; no ORCA runtime ownership of WPilot. |

## Phase 1 Document Map

- [phase-1-mvp.md](phase-1-mvp.md) - MVP scope and workflow sequence.
- [boundaries.md](boundaries.md) - ownership, external-system, and forbidden-claim boundaries.
- [beget-test-plan.md](beget-test-plan.md) - Beget-hosted test-site run plan.
- [backup-rollback-rules.md](backup-rollback-rules.md) - backup confirmation and rollback discipline.
- [access-safety.md](access-safety.md) - credential and access handling rules.
- [local-storage-policy.md](local-storage-policy.md) - local-only `C:\AI MARS\backups\` and `C:\AI MARS\local\` policy, token handoff workflow, rollback snapshot storage, and no-secret-in-git rules.
- [qa-checklist.md](qa-checklist.md) - Phase 1 QA gates.
- [reports/test-report-template.md](reports/test-report-template.md) - operator report template.
- [templates/site-passport-template.md](templates/site-passport-template.md) - sanitized site facts template.
- [templates/change-request-template.md](templates/change-request-template.md) - scoped change request template.
- [templates/rollback-plan-template.md](templates/rollback-plan-template.md) - rollback plan template.

## Plugin MVP Planning Pack

- [plugin-mvp/reconciliation-map-v0.md](plugin-mvp/reconciliation-map-v0.md) - CORE reconciliation map; start here before changing plugin planning docs.
- [metacode-wpilot-plugin-concept.md](metacode-wpilot-plugin-concept.md) - PLANNED canonical plugin concept, MVP boundaries, REST surface, auth, audit, rollback, scoped replacement, and WPBakery strategy.
- [metacode-wpilot-plugin-mvp-roadmap.md](metacode-wpilot-plugin-mvp-roadmap.md) - PLANNED DEV-only plugin MVP sequence, strategic modes, Factory-native integration direction, and exclusions.

The plugin MVP planning pack is documentation only. It does not prove a WordPress plugin, runtime bridge, autonomous admin layer, production integration, or deployed code exists.

## Security Baseline

- No secrets in repo.
- No credentials, passwords, tokens, cookies, SSH keys, API keys, or hosting panel secrets.
- No `wp-config.php` copies or database dumps.
- No committed `C:\AI MARS\local\` or `C:\AI MARS\backups\` contents; those folders are local-only operational support if created on an operator machine.
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
