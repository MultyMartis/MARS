# MARS Localhost — Service Control Policy v1

**Document type:** Service control policy  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-00

---

## Purpose

Ensure local web services run **only when needed**, with operator awareness and no silent background production risk.

---

## Default posture

| Rule | Policy |
|------|--------|
| **Autostart** | Laragon does **not** autostart with Windows by default |
| **On-demand** | Services start only when operator or chartered task requires them |
| **After work** | Stop services when not required (operator habit) |
| **Docker/WSL** | **Not** required for default MLI profile |
| **Background services** | **No** services without operator awareness |
| **Production** | Production ports/endpoints **forbidden** as MLI targets |

---

## Ports (documented at MLI-01)

| Service | Typical port | Notes |
|---------|--------------|-------|
| HTTP | 80 | Conflicts checked before start |
| HTTPS | 443 | Optional local TLS |
| MySQL/MariaDB | 3306 | Local bind preferred |
| Apache alt | 8080 | If 80 blocked |

Exact port map finalized in [MARS-LOCALHOST-MLI-01-LARAGON-ENABLEMENT-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-01-LARAGON-ENABLEMENT-INPUT-v1.md).

---

## Conflict detection

Before starting stack:

1. Check if ports 80/443/3306 are in use
2. Document conflict resolution in enablement report
3. Do not hijack production-facing bindings

---

## Cursor boundaries

| Allowed | Forbidden |
|---------|-----------|
| Start/stop via **approved** operator commands in chartered tasks | Silent install of system services |
| Document commands in task reports | Production API calls through MLI |
| Reference paths in manifests | Autostart policy changes without operator |

---

## Laragon-specific

- Use Laragon GUI or documented CLI for start/stop
- **Quit All** after sessions when practical
- Disable "Start All at Windows startup" during MLI-01 setup

---

## Related

- [MARS-LOCALHOST-LARAGON-PLACEMENT-DECISION-v1.md](MARS-LOCALHOST-LARAGON-PLACEMENT-DECISION-v1.md)
- [reports/MARS-LOCALHOST-MLI-01-LARAGON-ENABLEMENT-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-01-LARAGON-ENABLEMENT-INPUT-v1.md)

---

*Service control policy v1 — MLI-00.*
