# Shared External Access Patterns

**Classification:** MARS External Systems — shared pattern library (documentation only).  
**Status:** human-supervised access guidance; **not** automation, **not** a hidden hosting bot, **not** credential storage.

## Purpose

This folder defines **shared operational patterns** for human-supervised access to external CMS and ecommerce sites. Patterns apply across pilot programs — not owned by any single pilot.

## Who may reference this layer

| Pilot | CMS / platform |
|-------|----------------|
| [WPilot](../../projects/wpilot/) | WordPress |
| [OCPilot](../../projects/ocpilot/) | OpenCart / ocStore |
| MODxPilot (possible future) | MODx |
| CustomSitePilot (possible future) | Custom / static / PHP / HTML sites |

See also: [CMS / Ecommerce Pilots family](../../projects/ocpilot/cms-ecommerce-pilots-family.md).

## What this is not

- Not WPilot-specific logic.
- Not OCPilot-specific logic.
- Not autonomous FTP/PMA/browser automation.
- Not proof of live integrations or runtime adapters in-repo.
- Not a place to store credentials, tokens, or dumps.

## Pattern documents

| Doc | Channel |
|-----|---------|
| [browser-admin-access-pattern.md](browser-admin-access-pattern.md) | Admin panel / browser workflow |
| [ftp-hosting-file-access-pattern.md](ftp-hosting-file-access-pattern.md) | FTP / SFTP / hosting file access |
| [pma-database-access-pattern.md](pma-database-access-pattern.md) | phpMyAdmin / database tools |
| [safety-boundaries.md](safety-boundaries.md) | Common rules, risk levels, stop conditions |

## Universal gates (all channels)

Before any access-based operation:

1. **Human confirms target** — correct URL, host, site folder, database name.
2. **Human confirms environment** — test / staging / production; operator verbal or written OK.
3. **Human confirms backup status** — file and/or DB backup availability for write-class work; read-only still needs backup *fact*.
4. **Human controls credentials/session** — AI/Cursor never holds or commits secrets.
5. **AI/Cursor works from evidence only** — operator-provided exports, screenshots, path lists, or explicit supervised access.
6. **No destructive actions without approval** — delete, overwrite, bulk SQL, mass file move.
7. **No secrets in repo** — passwords, tokens, `config.php`, raw dumps forbidden by default.
8. **REPORT required** — every access-based operation ends with `# REPORT — …`.

## SAFE UNKNOWN

Exact hosting panel, FTP client, or PMA version per operator — unknown until task context. Do not invent access paths or credentials.
