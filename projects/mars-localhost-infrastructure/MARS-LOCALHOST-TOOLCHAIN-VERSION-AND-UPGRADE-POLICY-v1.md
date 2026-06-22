# MARS Localhost — Toolchain Version and Upgrade Policy v1

**Document type:** Version and upgrade policy  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Core rules

1. **No automatic major upgrades** for PHP, MySQL, Apache, or Laragon.
2. **Verify versions** before starting consumer work (`registries/MARS-LOCALHOST-TOOL-REGISTRY-v1.md`).
3. **Backup** runtime configs to `D:\MARS-Localhost\backups\runtime\` before component changes.
4. **Rollback** via backup restore + prior binary if upgrade fails.
5. **Notify** consumers (Forge, OCPilot) when shared toolchain versions change.

---

## Component policies

| Component | Policy |
|-----------|--------|
| Laragon | Operator-initiated; do not auto-replace active PHP/DB without validation |
| PHP | Profile 8.3.x baseline; side-by-side only with explicit matrix update |
| MySQL | 8.4.x baseline; major bump requires dump + restore plan |
| Composer | `self-update` minor/patch with diagnose; keys via official process |
| WP-CLI | Pin verify after update; no production targets |
| PHPCS/WPCS | Update via Composer in `tools\phpcs\`; re-run fixture smoke |
| Node | System-managed; per-project lockfile compatibility |
| Playwright | Project-local in `tools\playwright-smoke\` |

---

## Evidence

Update `Last verified` in tool registry after each controlled upgrade.

---

## Related

- [manifests/MLI-02-RUNTIME-CONFIG-BASELINE-MANIFEST-v1.md](manifests/MLI-02-RUNTIME-CONFIG-BASELINE-MANIFEST-v1.md)

---

*Toolchain version and upgrade policy v1 — MLI-02.*
