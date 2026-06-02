# FTP / Hosting File Access Pattern

**Scope:** shared pattern for FTP, SFTP, and hosting file-manager supervised access.  
**Applies to:** WPilot, OCPilot, future MODxPilot, CustomSitePilot.

## Purpose

Human-supervised workflow for reading or modifying site files on remote hosting.

## Pre-access gates

| Gate | Operator confirms |
|------|-------------------|
| Target | Correct host, account, root folder |
| Environment | test / staging / production |
| Backup | Full file backup before any write |
| Scope | read-only inspect vs scoped file change |
| Credentials | Operator holds FTP/SFTP session; not in repo |

## Workflow — read-only first

1. **Read-only inspection first** — tree listing, selective download, diff vs baseline or passport.
2. Operator provides path lists, sanitized tree exports, or selective file excerpts — not necessarily full binary tree in git.
3. AI/Cursor analyzes from **provided evidence**; does not assume blind FTP automation exists.

## Workflow — write-class (requires charter)

1. Backup confirmed before any file change.
2. Scoped change only — single file or explicit folder; no mass delete/move.
3. No blind overwrite of `dist/`, vendor core, or generated caches without explicit approval.
4. Rollback path documented before change.

## Forbidden in repo

| Forbidden | Reason |
|-----------|--------|
| `config.php`, `wp-config.php`, `admin/config.php` with live values | Secrets |
| Storage configs, `.env`, credentials files | Secrets |
| Full production tree with customer uploads | PII / size / policy |
| SSH/FTP passwords or keys | Secrets |

## Platform path awareness

| Platform | Typical roots (examples — verify per site) |
|----------|---------------------------------------------|
| OpenCart / ocStore | `catalog/`, `admin/`, `system/`, `image/` |
| WordPress | `wp-content/`, `wp-admin/`, themes, plugins |
| Custom/static | operator-defined; SAFE UNKNOWN until passport |

## Stop conditions

- Backup not confirmed for write → halt.
- Mass delete/move requested without explicit approval → refuse.
- Config or credential file would be committed → halt; operator remediation.

## REPORT requirement

Every FTP/hosting access session must produce: `# REPORT — <pilot> FTP/hosting — <site>` with scope, files touched (if any), backup status, SAFE UNKNOWN.
