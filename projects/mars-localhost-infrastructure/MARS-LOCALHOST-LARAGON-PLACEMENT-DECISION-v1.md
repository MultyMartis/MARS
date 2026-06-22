# MARS Localhost — Laragon Placement Decision v1

**Document type:** Architecture decision record  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-00  
**Status:** **DECIDED** — install deferred to **MLI-01** (operator action)

---

## Decision summary

| Item | Value |
|------|-------|
| **Stack** | Laragon (portable or full) as shared Windows local web runtime |
| **Install path (preferred)** | `D:\MARS-Localhost\runtime\laragon` |
| **Document root (preferred)** | `D:\MARS-Localhost\sites` |
| **Install in MLI-00** | **NO** — enablement input only |

---

## Rationale

| Factor | Choice |
|--------|--------|
| Operator zone model | D: dedicated runtime disk; C: brain untouched |
| Multi-consumer | Single stack serves WordPress, OpenCart, PHP profiles |
| Windows-first | Aligns with Forge WordPress and OCPilot constraints |
| vs Local by Flywheel | Shared root under operator control; not per-user `Local Sites` silo |
| vs Docker/WSL | Lower friction for default studio profile |

**Supersedes for shared infra:** Forge WordPress FW-03 default of Local by Flywheel as **primary shared** runtime — Forge now **consumes** MLI Laragon profile. Historical FW-03 doc retains point-in-time record with superseded note.

---

## Custom document root

Laragon supports custom `www` / document root path.

**Target configuration (MLI-01):**

```text
Document root: D:\MARS-Localhost\sites
Virtual host:  {slug}.test → sites\{platform}\{class}\{slug}\public
```

| Layout | WordPress | OpenCart |
|--------|-----------|----------|
| Docroot | `...\public` or `...\` per install | `...\` catalog root |

**SAFE UNKNOWN until MLI-01:** exact Laragon version UI steps; verify portable install allows path outside `laragon\www`.

---

## Component placement

| Component | Path (post MLI-01) |
|-----------|-------------------|
| Laragon binaries | `D:\MARS-Localhost\runtime\laragon\` |
| PHP binaries | `runtime\laragon\bin\php\` (Laragon default) |
| MariaDB/MySQL data | `runtime\laragon\data\mysql\` or Laragon default data dir under install root |
| Web server config | `runtime\laragon\etc\apache2\` or `etc\nginx\` |
| Composer | Global or `D:\MARS-Localhost\tools\composer\` |
| WP-CLI | `D:\MARS-Localhost\tools\wp-cli\` |
| PHPCS | `D:\MARS-Localhost\tools\phpcs\` |
| Playwright | Project-local or `tools\playwright\` |
| Local certificates | `D:\MARS-Localhost\certificates\` |
| Logs | `D:\MARS-Localhost\logs\` (symlink or Laragon log redirect if supported) |
| Temp | `D:\MARS-Localhost\temp\` |

---

## Pre-existing path deviation

Operator created `D:\MARS-Localhost\laragon\` at **root** before this standard.

| Action in MLI-00 | Action in MLI-01 |
|------------------|------------------|
| Do not delete | Choose install into `runtime\laragon\` OR migrate root `laragon\` with operator approval |
| Document deviation | Record final path in enablement report |

---

## Enablement plan (MLI-01 — not executed here)

1. Operator downloads Laragon from official source (checksum verify)
2. Install to `D:\MARS-Localhost\runtime\laragon`
3. Set document root to `D:\MARS-Localhost\sites`
4. Disable Windows autostart
5. Select PHP 8.2+ and MariaDB 10.11+ (or equivalent)
6. Configure first vhost smoke test (`fws-0001.test` placeholder)
7. Document ports, PATH additions, rollback snapshot
8. Run smoke test per [MLI-01 input](reports/MARS-LOCALHOST-MLI-01-LARAGON-ENABLEMENT-INPUT-v1.md)

---

## Related

- [MARS-LOCALHOST-DIRECTORY-STANDARD-v1.md](MARS-LOCALHOST-DIRECTORY-STANDARD-v1.md)
- [MARS-LOCALHOST-SERVICE-CONTROL-POLICY-v1.md](MARS-LOCALHOST-SERVICE-CONTROL-POLICY-v1.md)
- [reports/MARS-LOCALHOST-MLI-01-LARAGON-ENABLEMENT-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-01-LARAGON-ENABLEMENT-INPUT-v1.md)

---

*Laragon placement decision v1 — MLI-00.*
