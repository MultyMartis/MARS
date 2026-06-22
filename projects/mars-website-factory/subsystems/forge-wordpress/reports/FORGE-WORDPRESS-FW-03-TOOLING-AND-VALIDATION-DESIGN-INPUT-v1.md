# Forge WordPress — FW-03 Tooling and Validation Design Input v1

**Document type:** Next-stage input package  
**Version:** v1  
**Date:** 2026-06-22  
**Authorized use:** Input to **FW-03 — Tooling and Validation Design** only

**Honesty:** Design input only — **not** FW-03 execution, **not** runtime.

---

## 1. Purpose

Enumerate decisions and tooling classes FW-03 must design to operationalize FW-02 standards. FW-03 does **not** implement pilots or register agents.

---

## 2. Local WordPress environment

| Decision area | FW-03 must resolve |
|---------------|-------------------|
| Local stack choice | Local WP, wp-env, Playground, or hybrid |
| **Windows compatibility** | Mandatory — R-DEV-01 |
| PHP version matrix | Align with intake contract |
| MySQL/MariaDB | Local vs Docker-optional |
| Multi-project isolation | Per LOC-ZONE project |
| DEV/staging sync | WPilot boundary |

---

## 3. Build integration

| Tool | FW-03 scope |
|------|-------------|
| **Gulp integration** | Factory dist → theme assets pipeline |
| npm scripts | Document standard commands |
| Watch mode | Dev workflow |
| Asset hashing / enqueue | Version bump policy |

---

## 4. CLI and quality tools

| Tool | Purpose | WV layer |
|------|---------|----------|
| **WP-CLI** | Install, plugin list, ACF sync assist | WV3 |
| **PHPCS / WPCS** | Code quality runner | WV2 |
| **PHP static analysis** | PHPStan/Psalm candidate | WV2 optional |
| Composer | Optional — proportionality | — |

---

## 5. Browser and visual tooling

| Tool | Purpose | WV layer |
|------|---------|----------|
| **Playwright** | Smoke, functional paths | WV5 |
| **Visual regression** | Screenshot diff vs Factory ref | WV6 |
| Baseline storage | Where screenshots live — STORAGE boundary |

---

## 6. Accessibility and performance

| Tool | Purpose | WV layer |
|------|---------|----------|
| **axe** (axe-playwright) | a11y checks | WV8 |
| **Lighthouse** | Perf baseline | WV8 |
| Threshold policy | Project profile — resolve SAFE UNKNOWN from FW-S-08 |

---

## 7. Security scanning

| Tool | Purpose | WV layer |
|------|---------|----------|
| PHPCS security sniffs | Already in FW-S-07 | WV4 |
| WPScan / dependency audit | Candidate | WV4 |
| Secret scan | Repo hygiene | WV4 |

---

## 8. Packaging

| Deliverable | FW-03 design |
|-------------|--------------|
| Theme ZIP | Build script |
| Plugin ZIP | Build script |
| RELEASE-MANIFEST generator | Manifest linter |
| Evidence bundle | WV report collector |

---

## 9. Safe command model

| Requirement | Source |
|-------------|--------|
| Typed operations | FORGE-WORDPRESS-TOOLING-ARCHITECTURE-v1 |
| No destructive production commands | R-ENV-01 |
| Sandbox boundary | Human control model |
| Command allowlist | Skill/tool cards |

---

## 10. Future skill / tool cards

| Card type | Candidate |
|-----------|-----------|
| Validation runners | `wv-run`, `phpcs-run` |
| Environment bootstrap | `wp-local-init` |
| Handoff packager | `release-manifest` |
| Agent hooks | AG-WP-001 seed — registration FW-05 |

---

## 11. Validation runners

FW-03 designs runner **specifications** — not necessarily full implementation:

| Runner | Layers |
|--------|--------|
| `wv0-manifest-lint` | WV0 |
| `wv2-phpcs` | WV2 |
| `wv3-acf-sync` | WV3 |
| `wv5-playwright-smoke` | WV5 |
| `wv6-visual-diff` | WV6 |
| `wv9-package-lint` | WV9 |

---

## 12. Explicit FW-03 exclusions

| Excluded | Stage |
|----------|-------|
| First pilot implementation | FW-05 |
| Agent registration | FW-05 charter |
| WPilot plugin changes | Out of scope |
| Production deployment | WPilot / operator |

---

## 13. Dependencies

| Input | Document |
|-------|----------|
| Tooling classes | [FORGE-WORDPRESS-TOOLING-ARCHITECTURE-v1.md](../FORGE-WORDPRESS-TOOLING-ARCHITECTURE-v1.md) |
| Validation layers | [FORGE-WORDPRESS-VALIDATION-STANDARD-v1.md](../standards/FORGE-WORDPRESS-VALIDATION-STANDARD-v1.md) |
| Coding standard | [FORGE-WORDPRESS-CODING-AND-SECURITY-STANDARD-v1.md](../standards/FORGE-WORDPRESS-CODING-AND-SECURITY-STANDARD-v1.md) |
| Research | AG-WP-001 research README |

---

## Related

- [FORGE-WORDPRESS-FW-02-COMPLIANCE-MATRIX-v1.md](../FORGE-WORDPRESS-FW-02-COMPLIANCE-MATRIX-v1.md)
- [roadmap.md](../roadmap.md) — FW-03 **NEXT** after FW-02

---

*FW-03 input v1 — not execution.*
