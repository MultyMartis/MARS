# I-SEO Report Hub — Production Environment Decision Log v0.1

**Status:** OPEN DECISIONS — no production environment selected yet  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Authority:** Operator I-SEO Report Hub Production Environment Charter 01  
**Related:** [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-CHARTER-v0.1.md)

---

## 1. Current decision status

| Topic | Status |
|-------|--------|
| Production environment selected | **No** |
| Production domain selected | **No** |
| HTTPS method selected | **No** |
| PDF production mode selected | **No** |
| Deployment method selected | **No** |
| Backup location selected | **No** |
| Recommended default (advisory only) | **Option C — VPS PHP-FPM/Nginx/MySQL** |
| Binding operator decision wave | **I-SEO Report Hub — Production Environment Decision 01** (next) |

This log records **open** decisions. Advisory recommendations are **not** operator approvals.

---

## 2. Open operator decisions (1–12)

| # | Decision | Options / notes | Blocking for deploy? |
|---|----------|-----------------|----------------------|
| 1 | Production host type | VPS preferred; shared hosting only if PDF/constraints validated; containers later | **Yes** |
| 2 | Production domain/subdomain | Operator-approved FQDN (example shape only: `reports.…`) | **Yes** |
| 3 | HTTPS / certificate method | Let’s Encrypt / hosting panel / reverse proxy | **Yes** |
| 4 | DB engine | MySQL 8.x preferred or MariaDB compatible | **Yes** |
| 5 | PHP version | Target 8.3 if available; document acceptable minimum | **Yes** |
| 6 | PDF generation mode | Headless on prod; or generate elsewhere + upload; or serve pre-generated only | **Yes** (if exports must be created in prod) |
| 7 | Deployment method | Git-based deploy; SFTP exact sync; release archive | **Yes** |
| 8 | Backup location | DB dumps + artifact storage; encrypted/access-restricted | **Yes** |
| 9 | Access model | Who can login; password policy; VPN/IP allowlist/basic auth for admin | **Yes** |
| 10 | Logging policy | Token URL sensitivity; log protection/rotation | **Yes** (policy) |
| 11 | Real client data readiness | Internal test client vs real client data for first pilot | **Yes** for real clients |
| 12 | DB-11 delivery events | Remain deferred unless operator reopens before pilot | No (unless policy requires) |

---

## 3. Recommended defaults (advisory)

| Topic | Advisory default | Binding? |
|-------|------------------|----------|
| Host topology | Option C VPS | **No** — needs Decision 01 |
| Webserver | Nginx + PHP-FPM (Apache OK) | No |
| PHP | 8.3.x | No |
| DB | MySQL 8.x utf8mb4 | No |
| Public surface | Direct PDF share only | Carry existing product decision |
| Next wave | Production Environment Decision 01 | Charter recommendation |

---

## 4. Rejected / deferred

| Item | Classification | Reason |
|------|----------------|--------|
| Local workstation as production | **Rejected** | No production uptime/HTTPS/client delivery posture |
| Public tunnel as production | **Rejected** | Unstable URLs; security/ops debt |
| Option E managed platform as first path | **Deferred** | Headless PDF / MARS fit unproven |
| Option D containers as mandatory first | **Deferred** | Complexity; optional later |
| Client portal / email / public landing | **Deferred (product Gates M/N)** | Not environment selection prerequisites for minimal pilot |
| Immediate production deployment | **Rejected for this wave** | Docs/policy only; Decision + validation required |

---

## 5. Linked readiness gates

From Production Readiness Gates v0.1:

| Gate | Relation to this log |
|------|----------------------|
| **E** Environment | Primary — host/domain/HTTPS/topology |
| **F** Secrets/env | Contour depends on host choice |
| **G** Prod DB/migration | Engine + empty prod DB |
| **H** Backup/rollback | Backup location + restore drill |
| **I** Access/users | Access model |
| **J** Monitoring/logs | Logging policy |
| **K** Real client data | Pilot data readiness |
| **M** DB-11 | Decision 12 |

---

## 6. Decision meeting / next wave

**Next:** `I-SEO Report Hub — Production Environment Decision 01`

Expected outputs of Decision 01:

1. Selected option (A/B/C/D/E) with explicit production vs non-production label
2. Domain + HTTPS method
3. PHP/DB pins
4. PDF mode
5. Deploy + backup choices
6. Access + logging policy summaries
7. Whether Validation 01 can start on a real target

Until Decision 01 closes items 1–11 as needed, **no** production implementation charter should claim environment ready.
