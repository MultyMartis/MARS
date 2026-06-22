# Forge WordPress FW-05 — Local Capability Audit v1

**Document type:** Read-only tooling audit  
**Version:** v1  
**Date:** 2026-06-22  
**Host:** Windows 10 (operator machine)  
**Stage:** FW-05 STEP 1

---

## Summary

| Category | Result |
|----------|--------|
| Frontend build toolchain | **AVAILABLE** |
| PHP / Composer / WP-CLI | **NOT AVAILABLE** |
| PHPCS / WPCS | **NOT AVAILABLE** |
| Local / Laragon | **NOT DETECTED** |
| Docker / DDEV | **NOT AVAILABLE** |
| WordPress Playground CLI | **PARTIAL** (`npx @wp-playground/cli` responds; version string `unknown`) |
| Playwright | **NOT VERIFIED** (project-local install planned in synthetic workspace) |
| ACF Pro | **NOT AVAILABLE** (operator license — SAFE UNKNOWN) |
| MySQL/MariaDB (host) | **NOT DETECTED** |

**Overall local WordPress profile:** Profile B fallback executable for disposable runtime; full Profile A stack not installed.

---

## Tool inventory

| Tool | Status | Version / evidence | FW-05 use |
|------|--------|-------------------|-----------|
| Git | PASS | Branch `mars/post-cycle8-live-tests`; FW-04 commit `6945ab6` | Checkpoint complete |
| Node.js | PASS | v24.13.1 | Gulp frontend, Playwright, Playground CLI |
| npm | PASS | 11.8.0 | Project-local deps |
| Gulp CLI | PASS | CLI 3.1.0 | Synthetic frontend build |
| PHP | NOT AVAILABLE | Command not found on PATH | WV2 `php -l` blocked |
| Composer | NOT AVAILABLE | Command not found | PHPCS project-local blocked without PHP |
| WP-CLI | NOT AVAILABLE | Command not found | Runtime population limited |
| PHPCS / WPCS | NOT AVAILABLE | Not installed | WV2 coding standards NOT EXECUTED |
| Docker | NOT AVAILABLE | Command not found | Profile C blocked |
| DDEV | NOT AVAILABLE | Command not found | Profile C blocked |
| Local (Flywheel) | NOT DETECTED | Path not found under `%LOCALAPPDATA%\Programs\Local` | Profile A blocked |
| Laragon | NOT DETECTED | `C:\laragon` absent | Profile A blocked |
| WordPress Playground CLI | PARTIAL | `npx @wp-playground/cli --version` → `unknown` | Profile B candidate |
| Playwright | PENDING | Install in FWS-0001 validation package | Visual capture |
| ACF Pro | NOT AVAILABLE | No operator-provided license in scope | Compatibility profile required |
| Disk space | PASS | Sufficient for synthetic workspace | — |

---

## Security / privacy

- No usernames, secrets, tokens, or full sensitive system paths recorded.
- No production credentials probed.
- No client site connections attempted.

---

## Implications for FW-05

1. Synthetic **frontend baseline** can be proven (Node/Gulp).
2. **WordPress code** can be authored and statically reviewed without host PHP.
3. **Disposable runtime** via Playground CLI is the only safe profile without system-wide install.
4. PHPCS/WPCS, WP-CLI population, and full shared-hosting parity require operator enablement before client pilot.

---

## Related

- [FORGE-WORDPRESS-FW-05-EXECUTION-ENVIRONMENT-DECISION-v1.md](FORGE-WORDPRESS-FW-05-EXECUTION-ENVIRONMENT-DECISION-v1.md)
- [../../FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md](../../FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md)

---

*FW-05 local capability audit v1 — evidence from read-only probe 2026-06-22.*
