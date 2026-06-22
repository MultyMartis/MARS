# MARS Localhost MLI-01 — Toolchain Audit v1

**Document type:** Toolchain audit report  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-01

---

## Core runtime tools

| Tool | Command | Result | Path / notes |
|------|---------|--------|--------------|
| **PHP** | `php -v` | **PASS** | `laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe` → 8.3.30 |
| **Composer** | `composer --version` | **PASS** | `tools\composer\composer.phar` → 2.10.1; Laragon bundled also present |
| **MySQL client** | `mysql --version` | **PASS** | `mysql-8.4.3-winx64\bin\mysql.exe` → 8.4.3 |
| **Git** | `git --version` | **PASS** | Laragon bundled → 2.47.1.windows.1 |
| **Node** | `node --version` | **PASS WITH LIMITATION** | System PATH → v24.13.1; Laragon node-v22 folder incomplete |
| **npm** | `npm --version` | **PASS** | System PATH → 11.8.0 |

---

## MLI shared tools

| Tool | Status | Path | Verification |
|------|--------|------|--------------|
| **WP-CLI** | **PASS** | `tools\wp-cli\wp-cli.phar` + `wp.cmd` | `wp --info` — PHP 8.3.30, WP-CLI phar |
| **PHPCS** | **PASS** | `tools\phpcs\phpcs\bin\phpcs` | v3.13.5 |
| **WPCS** | **PASS** | `tools\phpcs\wpcs\` | `phpcs -i` lists WordPress, WordPress-Core, WordPress-Docs, WordPress-Extra |
| **PHPCompatibility** | **NOT EXECUTED** | — | Deferred to MLI-02 |
| **Playwright** | **NOT EXECUTED** | `tools\playwright\` empty | Deferred to MLI-02 |

---

## Composer diagnose

| Check | Result |
|-------|--------|
| `composer diagnose` (overall) | **PASS WITH LIMITATION** |
| PHP 8.3.30 | OK |
| HTTP to Packagist | OK |
| Pubkey verification | Missing keys — MLI-02 hardening |
| zip extension | Enabled MLI-01 (`extension=zip` in php.ini) |

---

## OpenCart CLI

| Item | Status |
|------|--------|
| OpenCart-specific CLI | **NOT APPLICABLE** in MLI-01 — MLI-04 |

---

## Strategy

- **Composer:** project-local preferred; shared phar at `tools\composer\`
- **WP-CLI / PHPCS:** shared under `tools\` with session activation
- **No global Windows PATH mutation** — use [MARS-LOCALHOST-CLI-ENVIRONMENT-STANDARD-v1.md](../MARS-LOCALHOST-CLI-ENVIRONMENT-STANDARD-v1.md)

---

*Toolchain audit v1 — MLI-01.*
