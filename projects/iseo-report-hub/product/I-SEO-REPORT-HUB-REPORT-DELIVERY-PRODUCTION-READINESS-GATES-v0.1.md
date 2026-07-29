# I-SEO Report Hub — Report Delivery Production Readiness Gates v0.1

**Status:** POLICY / GATES ONLY — no implementation; no deployment  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Authority:** Operator I-SEO Report Hub Report Delivery Production Readiness Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-CHARTER-v0.1.md)

---

## Status vocabulary

| Status | Meaning |
|--------|---------|
| **PASS** | Proven for local MVP; not alone sufficient for production |
| **READY_FOR_PLAN** | Needs a dedicated planning charter before implementation |
| **REQUIRED_BEFORE_PRODUCTION** | Must be satisfied before production deployment |
| **DEFERRED** | Explicitly out of current production-readiness path unless operator reopens |
| **SAFE UNKNOWN** | Not verified in current evidence; must not be assumed |

---

## Gates A–N

| Gate | Topic | Status | Evidence / source | Required action | Blocker for production? | Operator decision needed? |
|------|-------|--------|-------------------|-----------------|-------------------------|---------------------------|
| **A** | Functional report flow | **PASS** (local MVP) | Finalization + snapshot + export + share + handoff Visual QA PASS; smoke 129/129 | Maintain regression smoke before any deploy | No (local); Yes if broken | No |
| **B** | Export integrity | **PASS** (local MVP) | PDF hardening; styled v2; checksums attested in QA | Re-verify checksums / `%PDF` / storage outside public on prod host | No (local) | No |
| **C** | Public share security | **PASS** (local MVP) | Security model + hardening + Visual QA; token hash only; 404/410; headers | Preserve model on prod HTTPS domain; rate-limit plan | No (local); Yes without HTTPS | Partial (expiry/max_access policy) |
| **D** | Client handoff UX | **PASS** (local MVP) | Implementation + Visual QA PASS; copy pack; once URL | Keep panel/copy; no raw paths in client copy | No (local) | No |
| **E** | Production environment | **REQUIRED_BEFORE_PRODUCTION** | Charter §6 options A–D; no host selected | Production Environment Charter 01 — choose topology/domain/HTTPS | **Yes** | **Yes** |
| **F** | Secrets / env | **REQUIRED_BEFORE_PRODUCTION** | Local `.env.local` only; not production contour | Define production secret contour outside Git; `APP_ENV=production`; debug off | **Yes** | **Yes** |
| **G** | Production DB / migration | **REQUIRED_BEFORE_PRODUCTION** | Local `iseo_report_hub_dev` only; migrations 9 | Create prod DB; migration dry-run; least-privilege user; no fixture DB reuse | **Yes** | **Yes** |
| **H** | Backup / rollback | **REQUIRED_BEFORE_PRODUCTION** | No restore test attested | Pre-deploy dump; storage backup; restore drill; rollback + share revoke procedure | **Yes** | **Yes** |
| **I** | Access control / users | **REQUIRED_BEFORE_PRODUCTION** | One local admin; no reset UI | Production users/roles; password policy; admin inventory | **Yes** | **Yes** |
| **J** | Monitoring / logs | **REQUIRED_BEFORE_PRODUCTION** | Local logs only; share access_count minimal | App/webserver/DB logs; `/health` uptime; privacy of access logs | **Yes** | Partial |
| **K** | Data import / real clients | **REQUIRED_BEFORE_PRODUCTION** | Fixture 1/1/1 only | Segregate fixtures; import real clients/projects/periods; define handoff recipients | **Yes** | **Yes** |
| **L** | Retention / pruning | **READY_FOR_PLAN** | 6 revoked smoke rows remain | Separate DB retention/pruning charter; do not ad-hoc delete | Soft (ops debt) | **Yes** (policy) |
| **M** | Delivery audit DB-11 | **DEFERRED** | Explicitly deferred in Handoff Charter | Only if operator confirms need for delivery events | No (unless required by policy) | **Yes** |
| **N** | Public landing / portal / email | **DEFERRED** | Explicit non-goals of MVP | Separate product charters if needed | No for minimal pilot | **Yes** |

---

## Gate notes

### A–D (local MVP PASS)

Carry into production **only after** E–K. Local PASS does not waive environment, secrets, backup, or real-data gates.

### E — Production environment

Must define: hosting option (B vs C recommended discussion), domain, HTTPS, PHP version pin, MySQL, docroot=`public/`, storage/logs outside webroot, Edge/headless PDF feasibility on host.

### F — Secrets / env

Must define: production env file location (not Git); DB credentials; session/cookie secure flags; `APP_URL` HTTPS base for share URLs; no debug stack traces.

### G — Production DB / migration

Must define: empty or controlled prod schema; apply migrations via dry-run then backup-gated apply; never point production at `iseo_report_hub_dev`.

### H — Backup / rollback

Must define: tagged Git hash / release; DB dump stored securely outside Git; artifact storage backup; restore test evidence; rollback steps including revoke of active shares if delivery broken.

### I — Access control

Must define: who may create/revoke shares; password change/reset process; no shared single local admin password reuse from workstation.

### J — Monitoring / logs

Minimum: app error logs; webserver access logs (token URL sensitivity); DB migration logs; share `access_count` / `last_accessed_at`; `/health` check; manual monthly audit until automation exists.

### K — Real data

Must define: fixture purge/segregation; real client import; reporting period process; roles; handoff recipients outside DB until DB-11.

### L — Retention

Six revoked smoke rows are acceptable local debt. Production needs retention policy before unbounded growth. Status **READY_FOR_PLAN**, not immediate blocker for Environment Charter.

### M / N — Deferred

DB-11, portal, landing, email remain deferred. Controlled pilot can use manual messenger/email paste of once URL.

---

## Aggregate readiness

| Scope | Verdict |
|-------|---------|
| Local / workstation MVP | **Ready** (A–D PASS) |
| Controlled production pilot | **Not ready** until E–K |
| Full product vision (portal/email/DB-11) | **Not claimed** |
