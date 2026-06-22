# MARS Localhost MLI-01 — Laragon Enablement Input v1

**Document type:** Stage enablement input  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-01 — **NOT EXECUTED** in MLI-00  
**Authority:** Operator-controlled installation required

---

## Purpose

Define exact operator actions to enable Laragon as the shared MLI web runtime on `D:\MARS-Localhost` without production access or autonomous system changes by Cursor.

---

## Approved roots

| Item | Path |
|------|------|
| **MLI runtime root** | `D:\MARS-Localhost` |
| **Laragon install** | `D:\MARS-Localhost\runtime\laragon` |
| **Document root** | `D:\MARS-Localhost\sites` |
| **MARS brain** | `C:\AI MARS` (manifests only) |

---

## Installation source

| Requirement | Detail |
|-------------|--------|
| **Source** | Official Laragon release (laragon.org or verified mirror) |
| **Edition** | Full or portable — operator choice; portable preferred for D: isolation |
| **Verification** | SHA checksum if published; virus scan per operator policy |
| **Version** | Record exact version in post-install report |
| **MLI-00** | **No install performed** |

---

## Install steps (operator)

```text
1. Download Laragon installer/archive
2. Install to D:\MARS-Localhost\runtime\laragon
3. Reconcile pre-existing D:\MARS-Localhost\laragon\ if present (migrate or deprecate — operator decision)
4. Open Laragon → Preferences → set document root to D:\MARS-Localhost\sites
5. Select PHP 8.2+ (8.1 minimum per Forge baseline)
6. Select MariaDB 10.11+ or MySQL 8.0 compatible
7. Choose Apache or Nginx — document choice
8. Disable "Run at Windows startup" / autostart
9. Add tools paths (see PATH section)
10. Create smoke vhost: fws-0001.test → sites\wordpress\synthetic\fws-0001 (empty OK)
11. Record ports, versions, paths in MLI-01 completion report
12. Snapshot config to backups\runtime\ before first site work
```

---

## PHP

| Item | Target |
|------|--------|
| Version | 8.2 preferred; 8.1+ minimum |
| Location | Laragon `bin\php\php-{version}` |
| Extensions | mysqli, curl, gd, mbstring, zip, intl (verify for WordPress + OpenCart) |

---

## MariaDB / MySQL

| Item | Target |
|------|--------|
| Version | MariaDB 10.11+ or equivalent |
| Data dir | Under Laragon install or documented custom path on D: |
| Local user | Operator-defined (e.g. `mars_local`) — secrets in `C:\AI MARS\local\` |
| Root password | Local only; never in Git |

---

## Apache / Nginx

| Item | Policy |
|------|--------|
| Default | Operator picks one primary for MLI-01 |
| Vhosts | `{slug}.test` per domain standard |
| Logs | Redirect or copy policy to `D:\MARS-Localhost\logs\` |

---

## Composer

| Item | Path |
|------|------|
| Preferred | `D:\MARS-Localhost\tools\composer\` or Laragon bundled |
| Verify | `composer --version` from Laragon terminal |

---

## WP-CLI

| Item | Path |
|------|------|
| Install | `D:\MARS-Localhost\tools\wp-cli\wp-cli.phar` |
| Verify | `wp --info` against smoke site |

---

## PHPCS

| Item | Path |
|------|------|
| Install | `D:\MARS-Localhost\tools\phpcs\` project-global or per-consumer |
| Standards | WordPress Coding Standards for Forge profile |

---

## Certificates

| Item | Policy |
|------|--------|
| Storage | `D:\MARS-Localhost\certificates\` |
| Tool | mkcert or Laragon SSL if used |
| Production reuse | **Forbidden** |

---

## PATH

Document additions for operator shell:

- PHP
- Composer
- WP-CLI
- Optional: PHPCS, Node (if not global)

Prefer Laragon **Terminal** as canonical MLI shell.

---

## Service control

- Autostart: **OFF**
- Start only for enablement session and chartered work
- Stop after session when practical
- See [MARS-LOCALHOST-SERVICE-CONTROL-POLICY-v1.md](../MARS-LOCALHOST-SERVICE-CONTROL-POLICY-v1.md)

---

## Version verification checklist

```text
[ ] php -v
[ ] mysql --version (or mariadb)
[ ] httpd -v OR nginx -v
[ ] composer --version
[ ] wp --info
[ ] phpcs --version (if installed in MLI-01 scope)
```

---

## Rollback

| Step | Action |
|------|--------|
| Pre-install | Note existing D: state (MLI-00 tree only) |
| Post-config | Zip `runtime\laragon\etc\` + vhost list to `backups\runtime\` |
| Failure | Remove install dir; restore documented ports; no brain Git rollback needed |

---

## Smoke test (MLI-01 minimum)

1. Start Laragon stack manually
2. Create `sites\wordpress\synthetic\fws-0001\` with `index.php` phpinfo or static OK page
3. Map `fws-0001.test` in hosts + Laragon vhost
4. HTTP GET returns 200
5. Create empty DB `mars_wp_fws0001`
6. Stop stack
7. Write short report under `projects/mars-localhost-infrastructure/reports/`

**Not in MLI-01 scope:** Full WordPress core install (MLI-03).

---

## Production access

**Forbidden.** No production credentials, hosts, or DB endpoints in enablement.

---

## Related

- [MARS-LOCALHOST-LARAGON-PLACEMENT-DECISION-v1.md](../MARS-LOCALHOST-LARAGON-PLACEMENT-DECISION-v1.md)
- [roadmap.md](../roadmap.md)

---

*MLI-01 enablement input v1 — prepared in MLI-00; execution deferred.*
