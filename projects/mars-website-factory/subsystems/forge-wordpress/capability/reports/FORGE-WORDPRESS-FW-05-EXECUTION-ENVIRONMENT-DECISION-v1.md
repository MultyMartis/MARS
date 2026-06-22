# Forge WordPress FW-05 — Execution Environment Decision v1

**Document type:** FW-05 runtime decision record  
**Version:** v1  
**Date:** 2026-06-22  
**Case:** FWS-0001

---

## Decision

**Selected profile: B — Disposable WordPress Playground CLI**

| Attribute | Value |
|-----------|-------|
| Profile | B (Playground CLI fallback) |
| Rationale | Profile A (Local/Laragon) not installed; Profile C (Docker/DDEV) not available; Node toolchain available |
| Runtime location | `FWS-0001/TEMP/playground/` (gitignored) |
| Persistent mount | Theme + plugin source from `WORDPRESS/` only |
| Frontend reference | Static `FRONTEND/dist/` served separately for WV6 |
| Production | NONE |
| System-wide install | **NOT PERFORMED** |

---

## Rejected profiles

| Profile | Decision | Reason |
|---------|----------|--------|
| A — Local / Laragon | REJECTED for FW-05 | Not detected; would require operator install |
| C — Docker / DDEV | REJECTED | Not installed |
| D — Blocked | NOT SELECTED | Profile B executable without system install |

---

## Known limitations (Profile B)

| Limitation | Impact |
|------------|--------|
| Limited WP-CLI | Runtime population partially manual / scripted via Playground |
| No host PHP | `php -l`, PHPCS runners NOT EXECUTED on host |
| ACF Pro unavailable | ACF Free + Settings API fallback |
| In-memory DB | Shared-hosting parity partial |
| Playground plugin install | ACF Free via official source if Playground allows |

---

## Implementation mode

**Mode A** — Custom theme + functionality plugin + curated fields (ACF Free / native options fallback).

---

## Operator actions deferred (pre–client pilot)

1. Install Local or Laragon (Profile A) for full WV2–WV5 parity
2. Install PHP + Composer + PHPCS/WPCS project-local
3. Provide ACF Pro license for synthetic local environment if Pro workflow must be proven

---

## Related

- [FORGE-WORDPRESS-FW-05-LOCAL-CAPABILITY-AUDIT-v1.md](FORGE-WORDPRESS-FW-05-LOCAL-CAPABILITY-AUDIT-v1.md)
- [../../FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md](../../FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md)

---

*Execution environment decision v1 — FW-05 FWS-0001.*
