# MARS Localhost — CLI Environment Standard v1

**Document type:** CLI environment standard  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-01

---

## Principle

**Do not** add full Laragon tree to global Windows PATH.

Use **session-local activation** for Cursor terminals and operator shells.

---

## Activation script (canonical)

```text
E:\MARS-Localhost\tools\activate-mli.cmd
```

### Behavior

1. Prepends to **current session PATH only:**
   - PHP 8.3.30
   - MySQL client
   - Git (Laragon)
   - Composer wrapper directory
   - WP-CLI directory
   - PHPCS bin
   - Laragon utils
2. Prints active versions (PHP, Composer, MySQL, Git, WP-CLI, PHPCS).
3. Contains **no secrets**.
4. Does **not** modify system environment permanently.

### Usage (Cursor terminal)

```bat
E:\MARS-Localhost\tools\activate-mli.cmd
php -v
composer --version
wp --info
phpcs --version
```

---

## Wrapper commands

| Tool | Wrapper |
|------|---------|
| Composer | `E:\MARS-Localhost\tools\composer\composer.cmd` |
| WP-CLI | `E:\MARS-Localhost\tools\wp-cli\wp.cmd` |
| PHPCS | `E:\MARS-Localhost\tools\phpcs\phpcs.cmd` |

---

## PHP binary (explicit)

```text
E:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe
```

---

## Known limitations

| Item | Note |
|------|------|
| Laragon `bin\laragon\laragon.cmd` | Stale paths from prior install location — **do not use** for MLI |
| Node | Use system Node or install Laragon node-v22 in MLI-02 |
| MySQL server | Not on PATH by default — start via Laragon or documented `mysqld` |

---

## Related

- [reports/MARS-LOCALHOST-MLI-01-TOOLCHAIN-AUDIT-v1.md](reports/MARS-LOCALHOST-MLI-01-TOOLCHAIN-AUDIT-v1.md)
- [reports/MARS-LOCALHOST-MLI-02-SHARED-TOOLCHAIN-HARDENING-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-02-SHARED-TOOLCHAIN-HARDENING-INPUT-v1.md)

---

*CLI environment standard v1 — MLI-01.*
