# MARS Localhost — Laragon Placement Decision v1

**Document type:** Architecture decision record  
**Version:** v1.1  
**Date:** 2026-06-22  
**Stage:** MLI-01 (updated from MLI-00)  
**Status:** **DECIDED** — install **COMPLETE** at canonical path

---

## Decision summary

| Item | Value |
|------|-------|
| **Stack** | Laragon 8.6.1 as shared Windows local web runtime |
| **Install path (canonical)** | `E:\MARS-Localhost\laragon` |
| **Previous MLI-00 preferred path** | `E:\MARS-Localhost\runtime\laragon` — **superseded** |
| **Physical sites** | `E:\MARS-Localhost\sites` |
| **Document root model** | Junction registry + explicit vhosts — see [MARS-LOCALHOST-DOCUMENT-ROOT-DECISION-v1.md](MARS-LOCALHOST-DOCUMENT-ROOT-DECISION-v1.md) |
| **Install status** | **COMPLETE** (MLI-01) |

---

## Rationale

| Factor | Choice |
|--------|--------|
| Operator zone model | D: dedicated runtime disk; C: brain untouched |
| Multi-consumer | Single stack serves WordPress, OpenCart, PHP profiles |
| Windows-first | Aligns with Forge WordPress and OCPilot constraints |
| Evidence-based path | Existing install at `laragon\` retained — no migration |

**Supersedes for shared infra:** Forge WordPress FW-03 Local by Flywheel as **primary shared** runtime — Forge now **consumes** MLI Laragon profile.

---

## Component placement (actual)

| Component | Path |
|-----------|------|
| Laragon binaries | `E:\MARS-Localhost\laragon\` |
| PHP binaries | `laragon\bin\php\php-8.3.30-Win32-vs16-x64\` |
| MySQL data | `laragon\data\mysql-8.4.3\` |
| Web server config | `laragon\etc\apache2\`, `laragon\bin\apache\` |
| Composer (shared) | `E:\MARS-Localhost\tools\composer\` |
| WP-CLI | `E:\MARS-Localhost\tools\wp-cli\` |
| PHPCS / WPCS | `E:\MARS-Localhost\tools\phpcs\` |
| Local certificates (target) | `E:\MARS-Localhost\certificates\` |
| Logs (target) | `E:\MARS-Localhost\logs\` |
| Temp | `E:\MARS-Localhost\temp\` |

---

## `runtime\laragon` placeholder

Empty directory — **`DEPRECATED EMPTY PLACEHOLDER`**. Do not install Laragon there without operator charter. See [MARS-LOCALHOST-LARAGON-PATH-RECONCILIATION-v1.md](MARS-LOCALHOST-LARAGON-PATH-RECONCILIATION-v1.md).

---

## Related

- [MARS-LOCALHOST-DIRECTORY-STANDARD-v1.md](MARS-LOCALHOST-DIRECTORY-STANDARD-v1.md)
- [MARS-LOCALHOST-SERVICE-PROFILE-v1.md](MARS-LOCALHOST-SERVICE-PROFILE-v1.md)
- [reports/MARS-LOCALHOST-MLI-01-LARAGON-INSTALLATION-AUDIT-v1.md](reports/MARS-LOCALHOST-MLI-01-LARAGON-INSTALLATION-AUDIT-v1.md)

---

*Laragon placement decision v1.1 — MLI-01.*
