# MARS Localhost MLI-02 — Shared Toolchain Hardening Input v1

**Document type:** Stage input (not executed)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02 — **NEXT** (not executed in MLI-01)

---

## Purpose

Harden shared CLI toolchain after MLI-01 baseline enablement. MLI-01 delivered **partial** enablement; MLI-02 closes gaps without re-provisioning Laragon.

---

## Scope

| Area | MLI-01 state | MLI-02 target |
|------|--------------|---------------|
| **PHP version management** | Single 8.3.30 active | Pin policy; optional 8.2 side-by-side for compatibility matrix |
| **Composer** | phar 2.10.1 working | `self-update --update-keys`; global vs project-local policy doc |
| **WP-CLI** | phar + wrapper | Pin version; `wp cli verify-checksums`; MySQL client path in `wp --info` |
| **PHPCS / WPCS** | Installed | PHPCompatibility install; pin versions; smoke scan on fixture only |
| **Node / npm** | System Node 24.x | Laragon node-v22 reconcile or document canonical Node source |
| **Playwright** | Empty `tools\playwright\` | Install shared or document project-local-only policy |
| **Certificates** | HTTP baseline | Laragon SSL trust chain; `certificates\` layout; HTTPS smoke |
| **PATH / session** | `activate-mli.cmd` | PowerShell equivalent; Cursor task snippet |
| **Version pinning** | Ad hoc | Tool registry file in brain |
| **Upgrade policy** | Undefined | Operator approval gate before PHP/MySQL major bumps |
| **Tool registry** | Partial | `registries/MARS-LOCALHOST-TOOL-REGISTRY-v1.md` |
| **Smoke commands** | Documented in audit | Single `mli-toolchain-smoke.cmd` |
| **Rollback** | Per-tool delete | Snapshot `backups\runtime\` before upgrades |

---

## MLI-01 carry-over items

1. Hosts file elevation for `.test` domains without Host-header workaround.
2. `laragon.cmd` stale path cleanup or official Laragon repair.
3. Apache graceful stop without `Stop-Process`.
4. Composer pubkey verification.
5. PHPCompatibility standard installation.
6. HTTPS smoke for `mli-smoke-001.test`.
7. MySQL root password policy (local secrets file).

---

## Non-goals (MLI-02)

- WordPress site creation (MLI-03)
- OpenCart site creation (MLI-04)
- Production access

---

## Related

- [MARS-LOCALHOST-CLI-ENVIRONMENT-STANDARD-v1.md](../MARS-LOCALHOST-CLI-ENVIRONMENT-STANDARD-v1.md)
- [reports/MARS-LOCALHOST-MLI-01-TOOLCHAIN-AUDIT-v1.md](MARS-LOCALHOST-MLI-01-TOOLCHAIN-AUDIT-v1.md)

---

*MLI-02 input v1 — prepared at MLI-01 closeout.*
