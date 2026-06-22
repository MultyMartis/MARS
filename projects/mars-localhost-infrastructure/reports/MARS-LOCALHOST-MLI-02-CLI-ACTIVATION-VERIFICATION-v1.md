# MARS Localhost MLI-02 — CLI Activation Verification v1

**Document type:** CLI activation verification  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Canonical scripts

| Script | Role |
|--------|------|
| `D:\MARS-Localhost\tools\activate-mli.cmd` | CMD session activation (canonical) |
| `D:\MARS-Localhost\tools\activate-mli.ps1` | PowerShell activation |

---

## Verified behaviour

| Check | Result |
|-------|--------|
| Session PATH only | **PASS** |
| Laragon PHP 8.3.30 | **PASS** |
| Composer, MySQL, Git, WP-CLI, PHPCS | **PASS** |
| System Node/npm surfaced | **PASS** |
| Laragon Node excluded | **PASS** |
| Version summary output | **PASS** |
| `MLI_ACTIVE=1` set | **PASS** |
| No credentials in scripts | **PASS** |
| Paths with spaces | **PASS** (quoted paths) |
| Exit code | **0** |

---

## Cursor terminal

Verified from automation session after `activate-mli.cmd`.

---

## Related

- [MARS-LOCALHOST-CLI-ENVIRONMENT-STANDARD-v1.md](../MARS-LOCALHOST-CLI-ENVIRONMENT-STANDARD-v1.md)

---

*CLI activation verification v1 — MLI-02.*
