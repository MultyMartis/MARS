# PILOT-001 — Stop Conditions v1

**Pilot ID:** `PILOT-001`  
**Effect:** **Immediate halt** — no further acquisition, implementation, or publish until human review and charter amendment or termination.

**Relation:** [EAR-FAILURE-MODELS-v1.md](../../EAR-FAILURE-MODELS-v1.md), [EAR-CONNECTOR-FAILURES-v1.md](../../EAR-CONNECTOR-FAILURES-v1.md), [STOP-CONDITIONS-v1.md](STOP-CONDITIONS-v1.md) (this file)

---

## 1. Halt protocol

| Step | Action |
|------|--------|
| 1 | **Stop** all connector / operator acquisition activity |
| 2 | **Do not** Publish snapshot |
| 3 | Record incident in operator session log (not git secrets) |
| 4 | Update [STATUS.md](STATUS.md) — stage frozen or reverted to Charter |
| 5 | Human review — charter authority decides: amend, terminate, or escalate |
| 6 | If credentials may be exposed — rotate per operator security policy (**outside** MARS repo) |

---

## 2. Immediate halt conditions

### 2.1 Access and scope

| ID | Condition | Why halt |
|----|-----------|----------|
| ST-01 | **Any write access requirement** discovered (filesystem, DB, admin, config) | Violates Mode 2 and pilot charter |
| ST-02 | **SSH escalation** required to complete scoped SFTP path (shell, sudo, mutating commands) | Outside SFTP Read-Only class; scope expansion |
| ST-03 | **Database writes** or data mutation required | Forbidden |
| ST-04 | **OpenCart Admin write** or install/upgrade actions required | Forbidden |
| ST-05 | **Scope expansion** without charter amendment (full tree dump, production paths, PII export) | Governance violation |
| ST-06 | **Mode 3** or operational deploy requested | EAR v1 forbidden |

### 2.2 Environment and identity

| ID | Condition | Why halt |
|----|-----------|----------|
| ST-07 | **Production environment drift** — acquisition targets PROD or unknown environment | TEST-only charter |
| ST-08 | **Wrong site** — `site_id` mismatch vs SITE-001 | Identity error |
| ST-09 | **Environment confusion** — operator cannot confirm TEST vs PROD | Fail closed |

### 2.3 Security and credentials

| ID | Condition | Why halt |
|----|-----------|----------|
| ST-10 | **Credential boundary violation** — secrets committed to git, snapshot, or consumer package | [EAR-CREDENTIAL-BOUNDARY-v1.md](../../EAR-CREDENTIAL-BOUNDARY-v1.md) |
| ST-11 | **Credential exposure** suspected (logged password, shared dump with secrets) | Security incident |
| ST-12 | **Missing `credential_ref`** with pressure to embed secrets in repo | Fail closed |
| ST-13 | **SFTP account has write permissions** and connector cannot restrict to read-only | Cannot maintain read-only claim |

### 2.4 Quality and honesty

| ID | Condition | Why halt |
|----|-----------|----------|
| ST-14 | **Inflated publish** — Level 2+ claimed from SFTP-only leg | Honesty violation |
| ST-15 | **Missing manifest integrity** — cannot support version proof but publish attempted at Level 1 | [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../EAR-OPENCART-QUALITY-MAPPING-v1.md) |
| ST-16 | **Partial evidence hidden** — gaps not recorded in `safe-unknown` | Consumer trust failure |

### 2.5 Governance

| ID | Condition | Why halt |
|----|-----------|----------|
| ST-17 | **Implementation started** without Implementation Sub-Charter approval | Phase boundary violation |
| ST-18 | **Live access** without Execution authorization | Charter stage violation |
| ST-19 | **Pilot-to-runtime confusion** — stakeholders treat charter as shipped product | Stop and clarify per [PILOT-GOVERNANCE-v1.md](../../PILOT-GOVERNANCE-v1.md) |
| ST-20 | **Consumer bypass** — OCPilot receives unpublished or unvalidated package | Workflow violation |

### 2.6 Technical blockers (connected-specific)

| ID | Condition | Why halt |
|----|-----------|----------|
| ST-21 | **SFTP unavailable** after operator-confirmed channel check | Cannot execute CON-L1-A; reassess Offline track |
| ST-22 | **Host prohibits listing** scoped paths — cannot produce file-manifest | Honest fail; no inflated Level 1 |
| ST-23 | **Symlink / chroot escape** outside approved scope | Scope safety |
| ST-24 | **Bulk exfiltration** beyond charter byte/path limits | Scope expansion |

---

## 3. Stop vs pause

| Signal | Action |
|--------|--------|
| **Pause** | Operator needs HITL decision (e.g. defer `database-metadata` with `safe-unknown`) — documented, may continue |
| **Stop** | Any condition in §2 — no publish until human charter review |

---

## 4. Post-stop outcomes

| Outcome | Next step |
|---------|-----------|
| **Terminate pilot** | Mark STATUS; archive folder; Lessons Learned |
| **Amend charter** | New version; re-Approval |
| **Switch track** | Offline acquisition separate charter — not automatic fallback |
| **Escalate security** | Operator incident response — outside MARS |

---

## 5. Charter-stage stops (no live access)

Even without Execution, halt **progression** if:

| Condition | Action |
|-----------|--------|
| Human authority revokes pilot | Freeze at Charter; do not approve |
| Phase 5 Implementation Readiness Review = NO-GO | Do not author Implementation Sub-Charter |
| Architectural contradiction found in assessment plan review | Fix architecture or terminate pilot |

---

## 6. Current status

**No stop conditions triggered** — pilot has not entered Execution.
