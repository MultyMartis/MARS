# Server Ops — PostgreSQL Foundation Handoff v1

**Document:** `SERVER-OPS-POSTGRES-FOUNDATION-HANDOFF-v1`  
**Audience:** `Pro: MARS Server Ops pt.2`  
**From:** `mars-data-layer` (architecture / data contracts)  
**Date:** 2026-09-03  
**Execution status:** **NOT EXECUTED** — requirements only

---

## 1. Purpose

Hand off **infrastructure-only** requirements to install a production-ready PostgreSQL foundation on `VEESP-N8N-01` for the future MARS Bot Data Platform.

This runbook does **not** include business schema implementation, Sheets migration, or n8n workflow edits.

---

## 2. Target summary

| Item | Requirement |
|------|-------------|
| Engine | **PostgreSQL 18** stable |
| Topology | **One** container |
| Database name (logical) | `mars` (may be created empty; schemas later by data-layer migrator) |
| Persistent volume | Required |
| Connectivity | Internal Docker network with **n8n** |
| Public port `5432` | **Forbidden** |
| Healthcheck | Required |
| Resource baseline | Document CPU/RAM/disk limits appropriate to host |
| Logs | Container logs retained per Server Ops standard |
| Backup hooks | Nightly logical dump hooks + off-VPS copy path (even if first dumps are empty DB) |
| Secrets | Handoff mechanism for roles/passwords — **not** committed to Git |
| n8n SQLite | **Do not migrate** |
| nginx | **No** nginx dependency for PostgreSQL |
| Unrelated Docker | **No** unrelated stack changes |

---

## 3. Non-goals for Server Ops wave

- Creating `app_iseo_sales` / business tables;
- Implementing MARS DB Toolkit;
- Changing Google credentials;
- Editing production n8n workflows;
- Enabling public DB access “temporarily”;
- Installing PgBouncer/Redis/Kafka;
- Declaring Beget hot standby.

---

## 4. Acceptance criteria (infra)

1. PostgreSQL 18 container healthy.
2. Persistent data survives container recreate.
3. n8n can resolve/connect on internal network (connectivity proof without publishing port).
4. `5432` not reachable from public internet.
5. Healthcheck green.
6. Backup hook dry-run produces an artifact off-box or to approved off-VPS location.
7. Secret material delivered to approved secret location; no secrets in chat logs/Git.
8. Evidence note filed under Server Ops project reports.

---

## 5. Coordination points back to data-layer

After foundation:

- Data-layer applies migrations as `mars_migrator`.
- Runtime roles created per [POSTGRES-SECURITY-STANDARD-v1.md](../architecture/POSTGRES-SECURITY-STANDARD-v1.md).
- Cutover remains blocked until Phases 2–6 of [ROADMAP.md](../ROADMAP.md).

---

## 6. References

- [MARS-BOT-DATA-ARCHITECTURE-v1.md](../architecture/MARS-BOT-DATA-ARCHITECTURE-v1.md)
- [BACKUP-DR-STANDARD-v1.md](../architecture/BACKUP-DR-STANDARD-v1.md)
- `projects/mars-server-ops/` (ops home — if present for VEESP-N8N-01 assets)
