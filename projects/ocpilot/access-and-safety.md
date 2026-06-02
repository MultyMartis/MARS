# OCPilot — Access and Safety

**Status:** documented security baseline.

## Core rules

- No secrets in repo (passwords, API keys, DB passwords, session cookies, SSH keys).
- No `config.php` copies with live credentials.
- No full database dumps in git unless explicitly approved and sanitized.
- No autonomous FTP/PMA/browser/admin claims.

## Shared external access patterns (not WPilot-owned)

Human-supervised access to external CMS/ecommerce sites uses the **shared** pattern library:

**Entry:** [shared/external-access-patterns/](../../shared/external-access-patterns/README.md)

| Doc | Channel |
|-----|---------|
| [browser-admin-access-pattern.md](../../shared/external-access-patterns/browser-admin-access-pattern.md) | OpenCart admin / browser |
| [ftp-hosting-file-access-pattern.md](../../shared/external-access-patterns/ftp-hosting-file-access-pattern.md) | FTP/SFTP/hosting files |
| [pma-database-access-pattern.md](../../shared/external-access-patterns/pma-database-access-pattern.md) | phpMyAdmin / DB tools |
| [safety-boundaries.md](../../shared/external-access-patterns/safety-boundaries.md) | Common gates, risk levels, stop conditions |

This layer is shared by WPilot, OCPilot, and possible future pilots. It is **not** automation and **not** credential storage.

## OCPilot channel stance

| Channel | Typical use | OCPilot stance |
|---------|-------------|----------------|
| FTP / hosting files | Tree download, diff vs versioned baseline | Human-supervised; OpenCart paths, not `wp-content/` |
| Browser / OpenCart admin | Catalog, extensions, settings UI | Target URL confirmed by operator |
| PMA / DB tools | Schema inspect, read-only queries | No destructive SQL without approval |

OCPilot **must not** assume WordPress-specific logic (themes as WP themes, WPBakery, `wp-config.php`, WP REST) applies to OpenCart.

## Human-supervised access gate

Before any real FTP/PMA/browser/admin action:

1. **Target-confirmed** — correct host, site folder, DB name (operator verbal/written OK).
2. **Environment-confirmed** — test / staging / production.
3. **Backup-confirmed** — file and/or DB backup for write-class work; read-only pilot still needs backup **availability** fact, not necessarily fresh dump in repo.
4. **Scope-confirmed** — read-only vs write; catalog vs theme vs system.
5. **Report-driven** — start/end with `# REPORT — …`; record SAFE UNKNOWN.

See [cms-ecommerce-pilots-family.md](cms-ecommerce-pilots-family.md) for family context.

## What may be recorded (sanitized)

| Allowed | Forbidden |
|---------|-----------|
| Access *class* (FTP read-only, admin role name) | Actual passwords/tokens |
| OpenCart version string (if verified) | `config.php` secret values |
| Hosting provider name | Panel screenshots with secrets |
| Backup *confirmed yes/no* + external location label | Dump files in repo |

## Credentials location

Credentials stay **outside** repo — operator secure channel or local operator storage (policy TBD per org; do not invent paths with live secrets).

## Minimum access principle

1. Public/front inspect before admin.
2. Read-only audit before any write charter.
3. Staging clone before production when available.
4. Single catalog table/query scope before bulk import.

## Materials not allowed in `sites/` or reports

- DB exports with PII/secrets.
- Full unredacted `error.log` with credentials.
- Customer payment data samples.
- Raw production dumps unless explicitly approved and sanitized.

## Access closeout

End of run: operator confirms session closed / temp access revoked. Record outcome only, not secrets.

## SECURITY RISK

Secret exposure → halt task, operator remediation, no commit of affected files.
