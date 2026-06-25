# MLI-02 Runtime Config Baseline Manifest v1

**Document type:** Runtime backup manifest (brain pointer)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02  
**Backup location:** `E:\MARS-Localhost\backups\runtime\MLI-02-BASELINE\` (**outside Git**)

---

## Purpose

Point-in-time copy of MLI configuration files before further toolchain or profile work.

---

## Included (MLI-02)

| Category | Runtime paths |
|----------|---------------|
| Laragon preferences | `laragon\usr\laragon.ini` |
| MySQL config | `laragon\data\my.ini` |
| Apache main | `laragon\bin\apache\...\conf\httpd.conf` |
| Apache MLI includes | `laragon\etc\apache2\mod_php.conf`, `httpd-ssl.conf` |
| Vhosts | `sites-enabled\mli-smoke-001.test*.conf` |
| Activation | `tools\activate-mli.cmd`, `activate-mli.ps1` |
| Hosts scripts | `tools\hosts\*.ps1` |

---

## Excluded

- Database data directories
- Private keys (referenced only)
- Logs, cache, `node_modules`, browser binaries
- Unrelated operator sites

---

## Restore

Operator copies files back from backup path; restart Apache/MySQL; verify smoke suite.

---

## Related

- [MARS-LOCALHOST-TOOLCHAIN-VERSION-AND-UPGRADE-POLICY-v1.md](../MARS-LOCALHOST-TOOLCHAIN-VERSION-AND-UPGRADE-POLICY-v1.md)

---

*MLI-02 runtime config baseline manifest v1.*
