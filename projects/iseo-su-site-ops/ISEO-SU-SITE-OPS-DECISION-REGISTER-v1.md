# ISEO-SU-SITE-OPS Decision Register v1

**Status:** ACCEPTED (Phase 1.5)  
**Decision date:** 2026-07-22  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  

Approval IDs: **not invented** — decisions recorded as operator-accepted programme decisions for Phase 0 / 1 / 1.5.

---

## Accepted decisions

| ID | Decision | Classification | Date |
|----|----------|----------------|------|
| D-001 | Dedicated locus is `X:\AI MARS\projects\iseo-su-site-ops\` — main SoT for hybrid i-seo.su site operations | CONFIRMED | 2026-07-22 |
| D-002 | Report Hub (`projects/iseo-report-hub/`) remains sibling product; not site-ops SoT | CONFIRMED | 2026-07-22 |
| D-003 | WPilot covers WordPress-only scope; does not own static HTML or full hybrid runbook | CONFIRMED | 2026-07-22 |
| D-004 | Forge WordPress is methodology-only for this programme | CONFIRMED | 2026-07-22 |
| D-005 | Website Factory is methodology-only; not a runtime deployment engine for i-seo.su | CONFIRMED | 2026-07-22 |
| D-006 | ATLAS mint for WEB/DOM/PRJ (or related) is **DEFERRED** | DEFERRED | 2026-07-22 |
| D-007 | No production connection authorized (FTP/SFTP, WP admin, WPilot REST, panel) | CONFIRMED | 2026-07-22 |
| D-008 | No credentials/secrets in project docs or Git locus | CONFIRMED | 2026-07-22 |
| D-009 | Prefer **runtime-first audit** over assuming source/repo truth for live site facts | RECOMMENDED / ACCEPTED | 2026-07-22 |
| D-010 | No broad source/runtime sync as default | CONFIRMED | 2026-07-22 |
| D-011 | Operator manual production changes must be preserved (no blind overwrite) | CONFIRMED | 2026-07-22 |
| D-012 | Bounded promote required for any future promote path | CONFIRMED | 2026-07-22 |
| D-013 | Plugin backup never replaces hosting backup | CONFIRMED | 2026-07-22 |
| D-014 | Production compatibility of WPilot with i-seo.su remains **SAFE UNKNOWN** | SAFE UNKNOWN | 2026-07-22 |
| D-015 | Firefox Developer Edition becomes a separate MARS Browser Workstation | APPROVED DIRECTION | 2026-07-22 |
| D-016 | Exact Browser Workstation profile/path/security procedures are **DEFERRED** | DEFERRED | 2026-07-22 |
| D-017 | Do not create a second full site passport under `projects/wpilot/sites/` for this programme | CONFIRMED | 2026-07-22 |
| D-018 | FP-0002 architecture must not be copied as i-seo.su blueprint | CONFIRMED | 2026-07-22 |
| D-019 | Phase 2 remains HOLD until operator accepts Phase 1.5 REPORT | CONFIRMED | 2026-07-22 |
| D-020 | `registry/project-registry.md` row for this programme may be proposed later; **not** mutated in Phase 1.5 | CONFIRMED | 2026-07-22 |

---

## Decision notes

### Locus vs siblings

Main SoT for hybrid operations is this directory. WPilot may later reference a connection profile; Report Hub remains product-only.

### WPilot posture

RC5 is a **DEV reference** (`proven_content_writes` + `proven_connection_runtime` on DEV). Production readiness for i-seo.su is **not** claimed.

### Backup posture

Heavy production evidence/backups should default toward `X:\AI MARS STORAGE\` subject to policy verification at planning time. Paths are **not** created in Phase 1.5.

### Token format

Final token/profile format for i-seo.su remains **SAFE UNKNOWN**. Preferred principle (non-binding until planning): separate token file + metadata references path only (aligned with WPilot local-storage policy patterns).

---

*Decision Register v1 · 2026-07-22 · no fake approval IDs.*
