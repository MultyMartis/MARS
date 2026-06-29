# WPilot Access Safety

**Status:** documented security baseline.

## Core Rules

- No secrets in repo.
- No credentials in markdown, reports, templates, screenshots, commits, or chat transcripts intended for repo use.
- No passwords, tokens, cookies, SSH keys, API keys, recovery codes, database passwords, or panel secrets.
- No `wp-config.php` copies.
- No database dumps.
- No autonomous access or autonomous editing claims.

## Access Handling

The operator may provide access only through a secure external channel. WPilot docs may record the access class, not the secret:

- WordPress admin role name.
- Beget panel access type.
- FTP/SFTP access type.
- Database panel visibility.
- Read-only versus write-capable scope.

Never record the actual credential value.

For local-only WPilot token handling, use [local-storage-policy.md](local-storage-policy.md). Real token values may be stored only in approved local operator storage such as `X:\AI MARS\local\tokens\`, which is excluded from git and source-pack/export workflows.

## Minimum Access Principle

Use the least access needed for the current test:

- Public inspection before authenticated inspection.
- Read-only inspection before write-like tests.
- Test page before production page.
- Child theme or approved custom CSS before parent theme or plugin files.

## Materials Not Allowed In Repo

- Hosting panel screenshots that expose account IDs, tokens, email addresses, or secrets.
- WordPress user lists with personal data.
- Database exports.
- Logs containing IP addresses, emails, cookies, auth headers, or tokens.
- Full copies of client production files unless explicitly sanitized and approved outside MVP.
- Any contents from `X:\AI MARS\local\` or `X:\AI MARS\backups\`, except sanitized tracked examples under `projects/wpilot/runtime-local.example/`.

## Access Revocation Check

At the end of a run, the operator should confirm whether temporary access must be revoked, password changed, session closed, or test account disabled. Record only the confirmation result, not the secret.

## SECURITY RISK

Any accidental secret exposure is a security incident. Stop work, avoid copying the secret further, notify the operator, and follow their remediation instructions.
