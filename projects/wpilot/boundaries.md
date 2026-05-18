# WPilot Boundaries

**Status:** documented boundary rules.

## Entity Classification

WPilot is a **Program / Operational System** under the MARS System Entity Model. It belongs in `projects/wpilot/` because it is a large human-supervised operational direction that may contain workflows, templates, reports, and future agent roles.

WPilot is not itself an agent. Future specialist roles may be documented under `agents/` if they become bounded agent cards.

## External Systems

The following systems remain external:

- WordPress site and admin dashboard.
- Beget hosting, panel, file manager, FTP/SFTP, backups, and database tools.
- WordPress database.
- WordPress plugins, themes, The7, WPBakery, and vendor licenses.
- GitHub or other external storage if later used.

MARS may document interaction with those systems, but does not own their runtime truth, credentials, schedules, backups, or permissions.

## Ownership Rules

- Human operator owns final authority.
- Beget and WordPress remain sources of live execution truth.
- Repo documentation is a sanitized operating guide, not proof that access exists.
- Registry or README presence does not prove WPilot runtime implementation.

## Forbidden Claims

Do not claim:

- WPilot autonomously administers WordPress.
- WPilot deploys changes.
- WPilot stores credentials.
- WPilot updates plugins, themes, or WordPress core in MVP.
- WPilot can restore a site unless a human-verified backup and restore path are documented for the run.
- MARS owns the Beget account, WordPress site, or database.

## Forbidden Paths And Materials

Do not place WPilot work in:

- `mars-runtime/**`
- `workspaces/**`
- `shared/**`
- `dist/**`
- `node_modules/**`
- client production files
- any file containing secrets

Do not commit or store:

- passwords, tokens, cookies, SSH keys, API keys
- `wp-config.php`
- database dumps
- hosting panel exports with secrets
- screenshots exposing credentials or PII

## Production Rule

Phase 1 is test-site only. Any live production request is outside MVP and requires a new explicit task, backup evidence, rollback plan, and human approval.
