# Forge WordPress — Local Tooling Capability Audit v1

**Document type:** Read-only environment audit  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03  
**Host:** Operator Windows workstation (audit session)

**Rule:** No tools installed during audit. No secrets published.

---

## Summary

| Category | Detected | Usable for pilot |
|----------|----------|------------------|
| Git / Node / npm / Gulp | **Yes** | **Yes** |
| Playwright (npx) | **Yes** | **Yes** |
| PHP / Composer / WP-CLI / PHPCS | **No** | **No** — install required before WV2–WV3 |
| MySQL client | **No** | **No** |
| Docker / DDEV / Local | **No** | **No** — default env not installed |
| Python | **SAFE UNKNOWN** | Auxiliary only |

**Implication:** FW-03 design is complete; **pilot tooling readiness is NOT met** on this machine without operator setup (FW-04 checklist).

---

## Tool inventory

| Tool | Detected | Version | Path | Usable | Issue | Required action |
|------|----------|---------|------|--------|-------|-----------------|
| **Git** | Yes | 2.54.0.windows.1 | `C:\Program Files\Git\cmd\git.exe` | Yes | — | None |
| **Node** | Yes | v24.13.1 | `C:\Program Files\nodejs\node.exe` | Yes | — | None |
| **npm** | Yes | 11.8.0 | `C:\Program Files\nodejs\npm.ps1` | Yes | — | None |
| **Gulp CLI** | Yes | CLI 3.1.0 | `C:\Users\WSP-ONE\AppData\Roaming\npm\gulp.ps1` | Yes | Local project gulp version not audited | Verify per `FRONTEND/package.json` |
| **Playwright** | Yes | 1.61.0 (npx) | via npx | Yes | Browsers not enumerated | Run `npx playwright install` before WV5/WV6 |
| **PHP** | No | — | — | No | Not on PATH | Install via Local or Laragon |
| **Composer** | No | — | — | No | Not on PATH | Install with PHP stack |
| **MySQL client** | No | — | — | No | Not on PATH | Bundled with Local/Laragon |
| **MariaDB client** | No | — | — | No | Not on PATH | Same as MySQL |
| **WP-CLI** | No | — | — | No | Not on PATH | Install with Local or phar |
| **PHPCS** | No | — | — | No | Not on PATH | `composer global` or project vendor |
| **WPCS** | No | — | — | No | Requires PHPCS | Install with PHPCS ruleset |
| **Docker** | No | — | — | No | Not on PATH | Optional — specialized profile only |
| **DDEV** | No | — | — | No | Not on PATH | Optional |
| **Local (Flywheel)** | No | — | — | No | CLI/app not detected | Install for default profile |
| **Laragon** | No | — | — | No | Not detected | Fallback default stack |
| **wp-env** | No | — | — | No | Not detected | Deferred |
| **Python** | SAFE UNKNOWN | Store stub may not be full install | WindowsApps alias | Unknown | Version string incomplete | Only if helper scripts adopted |

---

## Browser baseline (Playwright)

| Item | Status |
|------|--------|
| Playwright package | Detected via npx |
| Chromium/WebKit/Firefox binaries | **SAFE UNKNOWN** — not verified |
| Required action | `npx playwright install chromium` minimum before visual runs |

---

## Alignment with tool registry

Registry claims **REQUIRED** tools not present locally are marked **design required, install pending** — not falsely marked installed.

---

## Related

- [registries/FORGE-WORDPRESS-TOOL-REGISTRY-v1.md](../registries/FORGE-WORDPRESS-TOOL-REGISTRY-v1.md)
- [FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md](../FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md)
- [FORGE-WORDPRESS-PILOT-TOOLING-PROFILE-v1.md](../FORGE-WORDPRESS-PILOT-TOOLING-PROFILE-v1.md)

---

*Audit v1 — read-only; 2026-06-22 session.*
