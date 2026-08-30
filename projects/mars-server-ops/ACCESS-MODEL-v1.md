# MARS Server Ops — Access Model v1

**Status:** **generalized capability model** for server infrastructure  
**Not:** credential store, connection config, or proof of current access

**Pattern source:** Site Ops access models (e.g. polygon-ws, driveavenue) — generalized for VPS/Linux/Docker/VPN/n8n/DB surfaces.

```text
DEFAULT: WRITE AUTHORIZED = NO on all external surfaces
Cursor/agents: NO standing credentials implied
```

---

## 1. Purpose

For each **access surface**, document:

- purpose  
- access type  
- expected privilege level  
- human approval requirement  
- secret reference model  
- read-only capability  
- change capability  
- risk class (Server Ops label + Survivability)  
- audit / evidence requirement  

**Never** store credential values in this model.

---

## 2. Global rules

| Rule | Detail |
|------|--------|
| **Read-only default** | Discovery and status unless charter authorizes change |
| **secret_ref only** | Point to local-only files — see [SECRET-HANDLING-MODEL-v1.md](SECRET-HANDLING-MODEL-v1.md) |
| **No agent credentials** | Cursor does not currently hold production SSH/panel/API secrets |
| **Per-charter authorization** | `WRITE AUTHORIZED = YES` only when explicit charter says so |
| **Session hygiene** | Destroy sessions after read-only discovery where applicable |
| **Survivability** | External mutation minimum **MEDIUM RISK**; destructive per gate |

---

## 3. Surface templates

Copy and fill one block per surface on a server-specific access doc (future phase).

---

### Hosting provider panel

| Field | Value |
|-------|-------|
| **Purpose** | Billing, VPS lifecycle, DNS, firewall UI, backups UI |
| **Access type** | Web panel |
| **Expected privilege** | Operator account — **UNKNOWN** until intake |
| **Human approval** | Required before any mutation |
| **secret_ref** | `local/infrastructure/<ref>/secrets.local.md` → Provider panel section |
| **Read-only capability** | **UNKNOWN** — charter-defined |
| **Change capability** | Typically yes (create/destroy VPS, firewall) — **NOT AUTHORIZED** by default |
| **Server Ops label** | READ-ONLY or HIGH-RISK CHANGE |
| **Survivability** | SAFE (read docs) / HIGH RISK (mutations) |
| **Evidence** | REPORT + screenshots to Storage if chartered |

---

### SSH

| Field | Value |
|-------|-------|
| **Purpose** | Shell access, service inspection, log review |
| **Access type** | SSH |
| **Expected privilege** | **UNKNOWN** — least-privilege target |
| **Human approval** | Required for session; read-only charter for discovery |
| **secret_ref** | local → SSH section or key path reference (not key content) |
| **Read-only capability** | Possible if account restricted — **VERIFY** |
| **Change capability** | Full shell if privileged — treat as HIGH RISK |
| **Server Ops label** | READ-ONLY (status) / MEDIUM–HIGH (package install, config edit) |
| **Survivability** | SAFE–MEDIUM (read) / HIGH (privileged write) |
| **Evidence** | Command **classes** in REPORT — no secret output |

---

### SFTP

| Field | Value |
|-------|-------|
| **Purpose** | File listing, bounded download/upload |
| **Access type** | SFTP / FTP |
| **Expected privilege** | Chroot or path-scoped account preferred |
| **Human approval** | Required |
| **secret_ref** | local → SFTP/FTP section |
| **Read-only capability** | LIST + GET — default for discovery |
| **Change capability** | PUT/DELETE — **NOT AUTHORIZED** by default |
| **Server Ops label** | READ-ONLY / MEDIUM-RISK CHANGE |
| **Survivability** | SAFE (list) / MEDIUM (bounded write) |
| **Evidence** | Path list sanitized; no file contents with secrets in Git |

---

### VPN / admin panel (3X-UI)

| Field | Value |
|-------|-------|
| **Purpose** | VPN user/inbound management, Xray config |
| **Access type** | Web panel |
| **Expected privilege** | Admin |
| **Human approval** | **Required** — inbound changes are HIGH RISK |
| **secret_ref** | local → VPN/3X-UI section |
| **Read-only capability** | View settings — if panel supports without save |
| **Change capability** | Add/remove clients, change inbounds — HIGH RISK |
| **Server Ops label** | READ-ONLY / HIGH-RISK CHANGE |
| **Survivability** | MEDIUM (read) / HIGH (inbound change) |
| **Evidence** | Sanitized export refs in Storage — not client private keys in Git |

---

### Docker host

| Field | Value |
|-------|-------|
| **Purpose** | Container lifecycle, compose, volumes |
| **Access type** | SSH + `docker` CLI or socket |
| **Expected privilege** | Often equivalent to root — treat as HIGH |
| **Human approval** | Required |
| **secret_ref** | local → Docker/SSH section |
| **Read-only capability** | `ps`, `inspect`, `logs` (bounded) |
| **Change capability** | `run`, `compose up`, volume mutations |
| **Server Ops label** | READ-ONLY / MEDIUM–HIGH-RISK CHANGE |
| **Survivability** | MEDIUM (inspect) / HIGH (production restart) |
| **Evidence** | Compose file refs sanitized; `.env` values never in Git |

---

### Reverse proxy admin

| Field | Value |
|-------|-------|
| **Purpose** | TLS, routing, upstream config |
| **Access type** | Panel or SSH + config files |
| **Expected privilege** | Admin |
| **Human approval** | Required — TLS and routing are HIGH RISK |
| **secret_ref** | local → proxy section |
| **Read-only capability** | Config read, test request |
| **Change capability** | Reload, cert change, route change |
| **Server Ops label** | READ-ONLY / HIGH-RISK CHANGE |
| **Survivability** | HIGH for production TLS/routing |
| **Evidence** | Redacted config snippet in Storage if needed |

---

### n8n

| Field | Value |
|-------|-------|
| **Purpose** | Workflow automation runtime (MetaBOT consumer) |
| **Access type** | Web UI + API |
| **Expected privilege** | Admin vs operator — **UNKNOWN** until intake |
| **Human approval** | Required for credential/workflow changes |
| **secret_ref** | local → n8n section; credential store **external to Git** |
| **Read-only capability** | View workflows (if policy allows) |
| **Change capability** | Workflow/credential/execution changes |
| **Server Ops label** | READ-ONLY (host) / product changes in MetaBOT charter |
| **Survivability** | MEDIUM–HIGH |
| **Evidence** | Host-level vs app-level split documented |

**Boundary:** MetaBOT owns workflow semantics; Server Ops owns **host** passport when chartered.

---

### PostgreSQL (and other DB)

| Field | Value |
|-------|-------|
| **Purpose** | Application data, MetaBOT/n8n backing store |
| **Access type** | `psql`, admin UI, socket |
| **Expected privilege** | App user vs superuser — document separately |
| **Human approval** | Required for schema/data mutation |
| **secret_ref** | local → Database section |
| **Read-only capability** | SELECT, `\dt`, explain — charter-bound |
| **Change capability** | DDL, migration, user create |
| **Server Ops label** | READ-ONLY / MEDIUM (user create) / HIGH (migration) / DESTRUCTIVE (drop) |
| **Survivability** | SAFE–MEDIUM (read) / HIGH / FORBIDDEN (agent drop) |
| **Evidence** | Dump refs in Storage; no live DSN in Git |

---

### Monitoring

| Field | Value |
|-------|-------|
| **Purpose** | Health, metrics, alerts |
| **Access type** | Web UI / API |
| **Expected privilege** | Read-only dashboard vs admin |
| **Human approval** | Required for alert rule changes |
| **secret_ref** | local → Monitoring section |
| **Read-only capability** | View dashboards |
| **Change capability** | Agent install, alert mutate |
| **Server Ops label** | READ-ONLY / MEDIUM-RISK CHANGE |
| **Survivability** | LOW–MEDIUM |
| **Evidence** | **Not** autonomous fleet — human-operated only |

---

### DNS / provider panel

| Field | Value |
|-------|-------|
| **Purpose** | A/AAAA/CNAME, TLS validation records |
| **Access type** | DNS panel or API |
| **Expected privilege** | Zone editor |
| **Human approval** | Required — DNS is HIGH RISK for prod |
| **secret_ref** | local → DNS section |
| **Read-only capability** | Zone read |
| **Change capability** | Record create/update/delete |
| **Server Ops label** | READ-ONLY / HIGH-RISK CHANGE |
| **Survivability** | HIGH for production cutover |
| **Evidence** | Record diff in REPORT (sanitized) |

---

## 4. Authorization summary template

| Action | Default status |
|--------|----------------|
| Read-only discovery charter | **NOT AUTHORIZED** until operator approves charter |
| Production config change | **NOT AUTHORIZED** |
| Backup creation by agent | **NOT AUTHORIZED** |
| Destructive operation | **NOT AUTHORIZED** — Survivability gate |

---

## 5. Related documents

- [SECRET-HANDLING-MODEL-v1.md](SECRET-HANDLING-MODEL-v1.md)  
- [CHANGE-RISK-MODEL-v1.md](CHANGE-RISK-MODEL-v1.md)  
- [SERVER-OPS-CHARTER-v1.md](SERVER-OPS-CHARTER-v1.md)  
- Site Ops reference: [POLYGON-WS-ACCESS-MODEL-v1.md](../polygon-ws-ru-site-ops/POLYGON-WS-ACCESS-MODEL-v1.md) (site-specific example)

---

*Access Model v1 · generalized template · Phase 1A · no credentials.*
