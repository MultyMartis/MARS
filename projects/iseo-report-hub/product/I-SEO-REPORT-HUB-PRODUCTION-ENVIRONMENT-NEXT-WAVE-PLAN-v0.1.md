# I-SEO Report Hub — Production Environment Next Wave Plan v0.1

**Status:** PLANNING ONLY — no deployment until Decision + Validation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Authority:** Operator I-SEO Report Hub Production Environment Decision 01  
**Related:**
- [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-BRIEF-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-BRIEF-v0.1.md)
- [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPERATOR-APPROVAL-CHECKLIST-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPERATOR-APPROVAL-CHECKLIST-v0.1.md)
- [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-VALIDATION-PLAN-v0.1.md)

---

## 1. Immediate recommended next action

**`I-SEO Report Hub — Production Environment Operator Decision 01`**

- Collect operator answers to checklist fields 1–14  
- **Not** an implementation wave  
- **Not** server access / deploy / DNS / HTTPS  

Until Operator Decision 01 records answers, stay at decision state **`RECOMMENDATION_READY`**.

---

## 2. Hard rule before any production work

No production implementation / deploy charter may claim environment ready until:

1. Operator selects topology (and labels production vs non-production), **and**
2. Required host/domain/HTTPS/PDF/deploy/backup/access answers are present for that path, **and**
3. Appropriate validation / compatibility wave completes (or explicit waiver documented), **and**
4. Separate explicit implementation / deploy charter is issued.

**No deployment** after Decision Brief alone.

---

## 3. Branching logic (after operator answers)

```text
Operator Decision 01 answers
        |
        +-- Approves VPS (C) WITH server + domain details
        |         -> Production Environment Validation 01
        |
        +-- Approves VPS (C) direction ONLY (no server/domain details)
        |         -> Production Environment Decision Follow-up 01
        |
        +-- Approves Shared hosting (B)
        |         -> Shared Hosting Compatibility Validation 01
        |
        +-- Approves Local-only demo (A) as non-production path
        |         -> Local Demo Hardening Charter 01
        |
        +-- Requires delivery audit before pilot (DB-11 = yes)
                  -> Report Delivery DB-11 Delivery Events Charter 01
                     (may run before or parallel to env validation; not a substitute for host choice)
```

Containers (D) / Managed (E): if operator selects them, open a dedicated follow-up decision/validation charter (not default path). Do not invent provider-specific steps here.

---

## 4. Wave definitions

### 4.1 Production Environment Operator Decision 01 (now)

| Item | Value |
|------|-------|
| Type | Operator answer / approval collection |
| Inputs | Decision Brief + Matrix + Checklist |
| Outputs | Filled answers 1–14; selected branch |
| Forbidden | SSH, DNS, HTTPS, deploy, DB mutation, code edits |

### 4.2 Production Environment Validation 01

**When:** Operator approves **VPS** **and** provides server + domain (and preferably HTTPS/PDF/deploy outline).

Requirements (future; see Validation Plan v0.1):

- Server access charter / least-privilege access recorded  
- OS / PHP / extensions / PHP-FPM checks  
- Docroot = `/public`; storage/logs outside public  
- DB connectivity to **dedicated prod DB** (not local `iseo_report_hub_dev`)  
- HTTPS endpoint validation  
- Headless PDF probe **or** documented serve-only / pre-generated mode  
- Logging / token sensitivity posture reviewed  
- Backup locations named; restore drill planned  

Still **no** production app deploy unless a separate deploy charter authorizes it.

### 4.3 Production Environment Decision Follow-up 01

**When:** Operator agrees VPS direction but has **not** supplied provider/server/FQDN/HTTPS details.

Purpose: collect missing binding facts; remain docs/decision-support; **no** Validation 01 against a real host yet.

### 4.4 Shared Hosting Compatibility Validation 01

**When:** Operator wants Option **B**.

Must validate at minimum:

- PHP version + required extensions  
- Ability to set docroot to `/public`  
- Storage writable outside public  
- Process/exec / headless PDF feasibility **or** forced serve-only / pre-generated PDF mode  
- HTTPS + stable domain  
- Cron / logging / backup constraints  

Fail closed: do not claim production ready if PDF or docroot constraints fail without accepted mitigation.

### 4.5 Local Demo Hardening Charter 01

**When:** Operator explicitly chooses **local-only** (non-production) path.

Focus: internal demo safety (no client-facing production shares; fixture boundaries; local HTTPS optional only if chartered). **Does not** authorize production claim.

### 4.6 Report Delivery DB-11 Delivery Events Charter 01

**When:** Operator answers checklist **13 = yes**.

Purpose: durable delivery / handoff audit events before first real client pilot.  
Does **not** replace environment selection. May precede or parallel Validation 01.

---

## 5. Mapping to Production Readiness gates

| Gate | Unblocked by |
|------|--------------|
| **E** Environment | Operator Decision + Validation/Compatibility |
| **F** Secrets/env | After host choice; secrets charter (never commit) |
| **G** Prod DB/migration | Dedicated DB after Validation |
| **H** Backup/rollback | Backup answers + restore drill |
| **I** Access/users | Access model answers + later hardening |
| **J** Monitoring/logs | Logging policy + protected logs |
| **K** Real client data | Real data mode ≠ fixture-only for clients |
| **M** DB-11 | Only if operator reopens (checklist 13) |

Gates **A–D** remain documented PASS from local MVP / Visual QA — they do **not** imply production readiness.

---

## 6. Explicit non-goals of this plan

- No server login / SSH / FTP / SFTP now  
- No DNS / certificate operations now  
- No production DB create / migrate now  
- No app-source / runtime edits now  
- No source→runtime sync now  
- No production claim now  

---

## 7. One-line summary

**Now:** Operator Decision 01 (answers).  
**Then:** branch to Validation / Follow-up / Shared Hosting Compatibility / Local Demo Hardening / DB-11 — **never** skip to silent production deploy.
