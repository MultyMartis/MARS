# AG-WP-001 — Tool Capability Matrix v1

**Document type:** Tool capability audit  
**Version:** v1  
**Stage:** FW-07B  
**Date:** 2026-06-24

**Sources:** [FORGE-WORDPRESS-TOOL-REGISTRY-v1.md](../registries/FORGE-WORDPRESS-TOOL-REGISTRY-v1.md), [MARS-LOCALHOST-TOOL-REGISTRY-v1.md](../../../mars-localhost-infrastructure/registries/MARS-LOCALHOST-TOOL-REGISTRY-v1.md)

**Honesty:** Status reflects repository evidence only. No fake MCP/WPilot bindings.

---

## Classification legend

`PROVEN` · `AVAILABLE_NOT_VALIDATED` · `PLANNED` · `EXPERIMENTAL` · `NOT AVAILABLE` · `NOT APPROVED`

---

## Matrix

| tool_id | Tool | Availability | Location | Proven version | Environment | Supported operation classes | Unsupported classes | Risk limits | Secret boundary | Audit output | Rollback | Authorization |
|---------|------|--------------|----------|----------------|-------------|----------------------------|---------------------|-------------|-----------------|--------------|----------|---------------|
| `MLI-TOOL-007` | WP-CLI | PROVEN | `D:\MARS-Localhost\tools\wp-cli\` | 2.12.0 | LOCAL_RUNTIME | inspect, validate read-only | prod write, arbitrary SQL | R0–R2 local | INDIRECT | CLI JSON stdout | DB restore | MLI activate |
| `MLI-TOOL-004` | PHP CLI | PROVEN | Laragon `php-8.3.30` | 8.3.30 | LOCAL_SOURCE/RUNTIME | `php -l`, WP execution | prod execution | R0–R2 | INDIRECT | lint report | reinstall | MLI activate |
| `MLI-TOOL-008` | PHPCS | PROVEN | MLI wpcs vendor | 3.13.5 | LOCAL_SOURCE | WPCS scan | — | R0 | NO_ACCESS | phpcs report | fix code | MLI activate |
| `MLI-TOOL-009` | WPCS | PROVEN | bundled with PHPCS | bundled | LOCAL_SOURCE | WP coding standard | — | R0 | NO_ACCESS | phpcs report | fix code | MLI activate |
| `MLI-TOOL-005` | MySQL | PROVEN | Laragon mysql-8.4.3 | 8.4.3 | LOCAL_RUNTIME | `wp db check` indirect | DROP/TRUNCATE, prod | R0 read; R3 write | INDIRECT | db check log | restore dump | operator |
| `MLI-TOOL-011` | Git | PROVEN | Laragon git | 2.47.1 | BRAIN + LOCAL_SOURCE | status, diff, log, selective commit | force push, hard reset | R0–R2 | NO_ACCESS | diff/commit sha | revert | operator |
| `MLI-TOOL-014` | Playwright | PROVEN | `tools\playwright-smoke\` | 1.61.0 | LOCAL_RUNTIME | route/render smoke | prod crawl | R0 | NO_ACCESS | test report | discard run | project npm |
| `MLI-TOOL-006` | Composer | PROVEN | MLI phar | 2.10.1 | LOCAL_SOURCE | validate, install approved | unvetted packages | R1 | NO_ACCESS | composer output | lock restore | MLI activate |
| `MLI-TOOL-015` | MLI activation | PROVEN | `tools\activate-mli.cmd` | v1 | LOCAL | toolchain PATH | — | R0 | NO_ACCESS | activation log | — | operator |
| `FW-TOL-001` | Git (Forge registry) | AVAILABLE_NOT_VALIDATED | system/Laragon | 2.54.0 audit | BRAIN | same as MLI Git | force push | R0–R2 | NO_ACCESS | git output | revert | operator |
| `FW-TOL-010` | WP-CLI (Forge registry) | AVAILABLE_NOT_VALIDATED | MLI path | defers MLI | LOCAL | defers MLI-TOOL-007 | prod | R0–R2 | INDIRECT | defers MLI | defers MLI | MLI |
| `FW-TOL-011` | PHPCS (Forge) | AVAILABLE_NOT_VALIDATED | MLI path | defers MLI | LOCAL_SOURCE | defers MLI-TOOL-008 | — | R0 | NO_ACCESS | defers MLI | — | MLI |
| `FW-TOL-015` | Playwright (Forge) | AVAILABLE_NOT_VALIDATED | project | 1.61.0 npx | LOCAL | E2E, screenshots | prod | R0 | NO_ACCESS | playwright report | discard | project |
| `FW-TOL-005` | PHP (Forge) | NOT AVAILABLE | — | not detected in FW audit | — | lint when MLI active | — | — | — | — | — | MLI defers |
| `CURSOR-AGENT` | Cursor Agent | PROVEN | IDE | — | BRAIN_ONLY | planning drafts, review | unrestricted shell, prod | R1 brain only | NO_ACCESS | task report | discard draft | operator session |
| `HTTP-PROBE` | HTTP read-only | PROVEN | curl/fetch | — | LOCAL_RUNTIME | route inspect/validate | authenticated prod | R0 | NO_ACCESS | status log | — | operator |
| `WPILOT` | WPilot | NOT APPROVED | external | — | — | — | all AG-WP-001 ops | — | PROHIBITED | handoff only | — | **NOT BOUND / HOLD** |
| `MCP-ADAPTER` | MCP WordPress bridge | EXPERIMENTAL | — | — | — | — | all until charter | — | PROHIBITED | — | — | **NOT APPROVED** |
| `WP-ABILITIES-API` | WordPress Abilities API | EXPERIMENTAL | — | — | — | — | all until charter | — | PROHIBITED | — | — | **NOT APPROVED** |

---

## WPilot / MCP / Abilities

| Interface | AG-WP-001 binding | Status |
|-----------|-------------------|--------|
| WPilot | Handoff contract only (FW-07A) | **NOT BOUND / HOLD** |
| MCP adapters | Boundary doc only | **NOT APPROVED** |
| Abilities API | Boundary doc only | **EXPERIMENTAL / NOT APPROVED** |

---

*Tool capability matrix v1 — evidence-aligned.*
