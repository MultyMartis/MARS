# MARS Localhost — Tool Registry v1

**Document type:** Tool registry (human-maintained)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Registry

| Tool ID | Tool | Version | Source | Physical path | Activation | Consumers | Status | Update policy | Risk | Last verified |
|---------|------|---------|--------|---------------|------------|-----------|--------|---------------|------|---------------|
| MLI-TOOL-001 | Laragon | 8.6.1.60301 | Installer | `D:\MARS-Localhost\laragon` | Laragon UI / Procfile | MLI | ACTIVE | Operator approval | Medium | 2026-06-22 |
| MLI-TOOL-002 | Apache | 2.4.66 | Laragon | `laragon\bin\apache\httpd-2.4.66-*` | Laragon / httpd.exe | MLI, PHP sites | ACTIVE | No auto major | Medium | 2026-06-22 |
| MLI-TOOL-003 | Nginx | 1.28.2 | Laragon | `laragon\bin\nginx\nginx-1.28.2` | Laragon profile | OPTIONAL | OPTIONAL | — | Low | 2026-06-22 |
| MLI-TOOL-004 | PHP | 8.3.30 | Laragon | `laragon\bin\php\php-8.3.30-*` | activate-mli | Forge, OCPilot | ACTIVE | Pin 8.3 profile | Medium | 2026-06-22 |
| MLI-TOOL-005 | MySQL | 8.4.3 | Laragon | `laragon\bin\mysql\mysql-8.4.3-*` | Laragon / mysqld | Forge, OCPilot | ACTIVE | No auto major | High | 2026-06-22 |
| MLI-TOOL-006 | Composer | 2.10.1 | MLI phar | `tools\composer\` | activate-mli | Forge, PHP | ACTIVE | diagnose after update | Low | 2026-06-22 |
| MLI-TOOL-007 | WP-CLI | 2.12.0 | MLI phar | `tools\wp-cli\` | activate-mli | Forge WP | ACTIVE | Operator approval | Low | 2026-06-22 |
| MLI-TOOL-008 | PHPCS | 3.13.5 | MLI wpcs vendor | `tools\phpcs\wpcs\vendor\bin` | activate-mli | Forge WP | ACTIVE | Composer in tools | Low | 2026-06-22 |
| MLI-TOOL-009 | WPCS | bundled | MLI wpcs | `tools\phpcs\wpcs\` | phpcs -i | Forge WP | ACTIVE | With PHPCS | Low | 2026-06-22 |
| MLI-TOOL-010 | PHPCompatibility | 9.3.5 | MLI phpcompat | `tools\phpcs\phpcompat\` | phpcs -i | Forge WP | ACTIVE | Composer require | Low | 2026-06-22 |
| MLI-TOOL-011 | Git | 2.47.1 | Laragon | `laragon\bin\git\` | activate-mli | MLI | ACTIVE | Laragon bundle | Low | 2026-06-22 |
| MLI-TOOL-012 | Node | 24.13.1 | **System** | OS install | system PATH | WF, Playwright | ACTIVE | System operator | Medium | 2026-06-22 |
| MLI-TOOL-013 | npm | 11.8.0 | **System** | OS install | system PATH | WF, Playwright | ACTIVE | With Node | Low | 2026-06-22 |
| MLI-TOOL-014 | Playwright | 1.61.0 | Project-local | `tools\playwright-smoke\` | npm run smoke | MLI, Forge | ACTIVE | Project lockfile | Low | 2026-06-22 |
| MLI-TOOL-015 | MLI activation | v1 | MLI script | `tools\activate-mli.cmd` | manual | All MLI CLI | ACTIVE | With toolchain | Low | 2026-06-22 |
| MLI-TOOL-016 | Hosts scripts | v1 | MLI script | `tools\hosts\` | elevated PS | MLI vhosts | ACTIVE | Manual | Low | 2026-06-22 |
| MLI-TOOL-017 | laragon.cmd | stale | Laragon | `laragon\bin\laragon\` | — | — | DEPRECATED | Do not use | High | 2026-06-22 |

---

## Status legend

`ACTIVE` | `OPTIONAL` | `PARTIAL` | `DEFERRED` | `DEPRECATED`

---

## Related

- [MARS-LOCALHOST-TOOLCHAIN-VERSION-AND-UPGRADE-POLICY-v1.md](../MARS-LOCALHOST-TOOLCHAIN-VERSION-AND-UPGRADE-POLICY-v1.md)

---

*Tool registry v1 — MLI-02.*
