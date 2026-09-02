# Backup / DR Standard v1

**Document:** `BACKUP-DR-STANDARD-v1`  
**project_id:** `mars-data-layer`  
**Date:** 2026-09-03

---

## 1. Initial target (after production rollout)

| Control | Requirement |
|---------|-------------|
| Nightly logical backup | `pg_dump` (or equivalent) of `mars` |
| Pre-migration dump | Mandatory before production DDL |
| Pre-cutover dump | Mandatory before SoT flip |
| Off-VPS copy | Required — do not keep sole copy on `VEESP-N8N-01` |
| Retention | Define in Server Ops runbook (minimum: ≥ 7 daily; longer for pre-cutover artifacts) |
| Restore test | Periodic proven restore to non-prod/local — **required**, not optional folklore |

---

## 2. Beget posture

**Beget = `FUTURE OFF-HOST BACKUP / DR TARGET`**

- Candidate for off-host dump storage and/or future DR host.
- **Not** defined as hot replica in V1.
- No live replication approved by this standard alone.

---

## 3. Decision gates (future)

| Mode | Gate questions |
|------|----------------|
| Periodic dump target only | Latency tolerance? Encryption at rest? Retention legal? |
| Logical replication | Need near-real-time copy? Acceptable failover complexity? |
| Hot standby | RPO/RTO numbers written and funded? |
| Separate PG host | Resource isolation evidence? |

Do not skip from “nightly dump” to “hot standby” without written RPO/RTO and Server Ops charter.

---

## 4. Ownership

- **Server Ops:** install backup plumbing, off-host transport, restore drills on infra.
- **mars-data-layer:** what must be consistent (schemas, cutover dumps, validation).
- **Bot packs:** business acceptance of restored data samples.
