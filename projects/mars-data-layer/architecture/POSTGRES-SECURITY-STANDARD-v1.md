# PostgreSQL Security Standard v1

**Document:** `POSTGRES-SECURITY-STANDARD-v1`  
**project_id:** `mars-data-layer`  
**Date:** 2026-09-03  
**Note:** Standards only — **no server changes** in Architecture V1 wave.

---

## 1. Network

- **No public `5432`.**
- PostgreSQL listens on Docker/internal network only (production target: `VEESP-N8N-01`).
- Localhost bind acceptable for local MLI contour; still no WAN exposure.

---

## 2. Least privilege

| Band | May |
|------|-----|
| Owner | Break-glass only |
| Migrator | DDL + grant management for migrations |
| Runtime | DML on own app schema as granted; execute approved functions |
| Agent | Subset of runtime ops via Toolkit |
| Reader | `SELECT` only |

- **No runtime superuser.**
- **No runtime DDL.**
- Agent roles **narrower** than runtime roles.

---

## 3. SQL surface

- Schema-qualified names in Toolkit/migrations.
- Safe `search_path` per role (avoid writable `public` surprise).
- Revoke unnecessary **PUBLIC** privileges on schemas/tables/functions.
- `EXECUTE` grants only on approved functions.
- `SECURITY DEFINER` only where justified, with fixed `search_path`, owner locked down, and audited.

---

## 4. AI

- No arbitrary AI SQL write.
- Named Toolkit operations only.
- Credentials for agent paths must not unlock migrator/owner.

---

## 5. Credentials

- Outside Git.
- Local: `X:\AI MARS\local\…` conventions.
- Production: Server Ops secret handoff (env/secret store) — values never in markdown.

---

## 6. Audit expectations

- Privileged DDL via migrator only with evidence.
- Operator actions in app `audit_logs` / equivalent.
- Failed auth / connection anomalies handled in Server Ops logging — not claimed automated here.
