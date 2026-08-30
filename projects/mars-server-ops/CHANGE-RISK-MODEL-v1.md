# MARS Server Ops — Change Risk Model v1

**Status:** **adapter / mapping document** — practical labels for server work  
**Not:** authoritative global risk taxonomy

---

## 1. Authority statement

**Authoritative risk model:**  
[projects/mars-survivability/contracts/agent-operation-risk-classes-v1.md](../mars-survivability/contracts/agent-operation-risk-classes-v1.md)

**Destructive operations:**  
[projects/mars-survivability/contracts/destructive-operations-policy-v1.md](../mars-survivability/contracts/destructive-operations-policy-v1.md)

This file provides **Server Ops practical labels** for operator charters and REPORT headers. When in doubt, classify **HIGH RISK** minimum. When labels conflict with Survivability, **Survivability wins**.

Server Ops **must not** create a competing repo-wide risk taxonomy.

---

## 2. Label → Survivability mapping

| Server Ops label | Typical Survivability class | Agent mutation default | Snapshot / backup | Human confirmation |
|------------------|----------------------------|------------------------|-------------------|----------------------|
| **READ-ONLY** | **SAFE** (read) | Read-only external OK if chartered | Not required | Charter for external access |
| **LOW-RISK CHANGE** | **LOW RISK** | Bounded doc/local artifact; minor config in dev | Recommended | Scope lock |
| **MEDIUM-RISK CHANGE** | **MEDIUM RISK** | Scoped change — package install, test service, DB user | **Required** checkpoint | **Required** |
| **HIGH-RISK CHANGE** | **HIGH RISK** (often **CRITICAL** if prod governance paths) | Limited — human-led preferred | **Required** | **Required** + rollback plan |
| **DESTRUCTIVE** | **FORBIDDEN** for agents; human-only with gate | **Agent: NO** | **Required** if human proceeds | **Explicit written approval** |

**Notes:**

- Production firewall, TLS, reverse proxy, production DB migration, 3X-UI inbound change → typically **HIGH-RISK CHANGE** → Survivability **HIGH RISK**.  
- Drops, volume delete, production overwrite → **DESTRUCTIVE** → Survivability **FORBIDDEN** for agents (F-01–F-14 family).  
- Read-only `status`, `list`, `inspect`, bounded GET → **READ-ONLY** → Survivability **SAFE** when truly read-only.

---

## 3. Classification examples (guidance only — not authorization)

### READ-ONLY → SAFE

- `systemctl status`, `docker ps`, `nginx -t` (test only), disk free  
- Provider panel **view** screens without save  
- SFTP LIST / bounded GET  
- PostgreSQL `SELECT`, `\dt`, explain plans (charter-bound)  
- Documentation updates in Git (Server Ops docs)

### LOW-RISK CHANGE → LOW RISK

- Git-only documentation or schema updates (Phase 1A-style)  
- Sanitized inventory row updates from verified intake  
- Creating **dev/lab** test files with no production impact  
- Single tracked file restore in Git (`git checkout -- path`)

### MEDIUM-RISK CHANGE → MEDIUM RISK

- Installing a package on non-prod or charter-scoped host  
- Creating a **test** service or container  
- Creating DB user/database (non-production)  
- Adding VPN client (non-critical) per charter  
- Multi-file doc pack under one programme folder

### HIGH-RISK CHANGE → HIGH RISK

- Firewall rule change  
- Reverse proxy route or upstream change  
- Production service restart  
- TLS certificate replace/reload on production  
- Production database migration  
- 3X-UI / Xray inbound or routing change  
- n8n host-level upgrade affecting MetaBOT uptime

### DESTRUCTIVE → FORBIDDEN (agents) / human gate

- Drop database or table production data  
- Delete Docker volume with production data  
- Remove production VPN client/user without charter  
- Overwrite production from backup (full restore)  
- Firewall reset / allow-all  
- Wipe host / reinstall OS  
- Recursive delete on server or Storage without destructive charter  

---

## 4. Escalation rules (from Survivability — restated)

1. Matches **FORBIDDEN** (Survivability §8) → agent halts; `SECURITY RISK` / `NEED HUMAN APPROVAL`.  
2. Ambiguous → **HIGH RISK** minimum.  
3. Destructive server ops require [destructive-operations-policy-v1.md](../mars-survivability/contracts/destructive-operations-policy-v1.md) gate + [BACKUP-RESTORE-MODEL-v1.md](BACKUP-RESTORE-MODEL-v1.md).  
4. Never chain destructive ops as "cleanup" after failed medium task.

---

## 5. Using labels in charters

Charter header example:

```text
risk_server_ops: HIGH-RISK CHANGE
risk_survivability: HIGH RISK
read_only: no
backup_manifest_ref: (required)
operator_approval: (name/date)
```

Both labels should appear; Survivability class is the enforcement reference.

---

## 6. External vs Git work

| Context | Label scope |
|---------|-------------|
| Git documentation (Phase 1A) | Typically **LOW-RISK CHANGE** or **MEDIUM** if large pack |
| External read-only discovery | **READ-ONLY** |
| External production change | **MEDIUM** minimum; often **HIGH** |
| External destructive | **DESTRUCTIVE** |

---

## 7. Related documents

- [SERVER-OPS-CHARTER-v1.md](SERVER-OPS-CHARTER-v1.md)  
- [ACCESS-MODEL-v1.md](ACCESS-MODEL-v1.md)  
- [projects/mars-survivability/guardrails/cursor-operational-safety-rules-v1.md](../mars-survivability/guardrails/cursor-operational-safety-rules-v1.md)  

---

*Change Risk Model v1 · adapter only · Survivability authoritative · Phase 1A.*
