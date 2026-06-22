# MARS Localhost MLI-02 — Toolchain State Audit v1

**Document type:** Toolchain state audit  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Summary

| Tool | Version | Source | Session path authority |
|------|---------|--------|------------------------|
| PHP | 8.3.30 | Laragon | `laragon\bin\php\php-8.3.30-Win32-vs16-x64` |
| Composer | 2.10.1 | MLI tools | `tools\composer\composer.phar` |
| MySQL client | 8.4.3 | Laragon | `laragon\bin\mysql\mysql-8.4.3-winx64\bin` |
| Git | 2.47.1 (Laragon) / 2.54.0 (system when outside activation) | Laragon in MLI session | `laragon\bin\git\cmd` |
| WP-CLI | 2.12.0 | MLI tools | `tools\wp-cli\wp-cli.phar` |
| PHPCS | 3.13.5 | MLI wpcs vendor | `tools\phpcs\wpcs\vendor\bin\phpcs` |
| WPCS | installed | MLI wpcs | `tools\phpcs\wpcs\` |
| PHPCompatibility | 9.3.5 | MLI phpcompat | `tools\phpcs\phpcompat\` |
| Node | 24.13.1 | **System** | not Laragon node |
| npm | 11.8.0 | **System** | — |
| Playwright | 1.61.0 | Project-local smoke | `tools\playwright-smoke\` |
| Apache | 2.4.66 | Laragon | — |
| MySQL server | 8.4.3 | Laragon | — |

---

## Duplicate / stale paths

| Item | Status |
|------|--------|
| `laragon\bin\laragon\laragon.cmd` | **DEPRECATED** — stale `D:\Projects\Laragon-installer\` paths |
| `activate-mli.cmd` | **CANONICAL** session activation |
| Laragon bundled Composer | Present; MLI copy preferred |
| Laragon node-v22 | Incomplete — **not used** |

---

## Composer diagnose

**PASS** — pubkeys OK after MLI-02 verification.

---

## Session isolation

`activate-mli.cmd` / `activate-mli.ps1` modify **current session PATH only**.

---

## Related

- [registries/MARS-LOCALHOST-TOOL-REGISTRY-v1.md](../registries/MARS-LOCALHOST-TOOL-REGISTRY-v1.md)

---

*Toolchain state audit v1 — MLI-02.*
