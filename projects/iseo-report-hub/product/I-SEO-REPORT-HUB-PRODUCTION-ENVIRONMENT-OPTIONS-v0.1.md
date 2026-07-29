# I-SEO Report Hub — Production Environment Options v0.1

**Status:** POLICY / COMPARISON ONLY — no provisioning; no deployment  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Authority:** Operator I-SEO Report Hub Production Environment Charter 01  
**Related:** [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-CHARTER-v0.1.md)

---

## Summary table

| Option | Name | App compatibility | PDF compatibility | Public share compatibility | Status |
|--------|------|-------------------|-------------------|----------------------------|--------|
| **A** | Local workstation pilot | High (current) | High (Edge headless local) | Local/internal only; external client URLs not production | **Not recommended as production** |
| **B** | Shared hosting PHP + MySQL | Medium | **Risk** — process/exec often restricted | Possible with HTTPS + `/public` if host allows | **Conditional** — validate first |
| **C** | VPS PHP-FPM/Nginx/MySQL | High | High (if Chromium/Chrome/Edge installed & validated) | High with stable domain + HTTPS | **Recommended candidate** |
| **D** | Containerized VPS | High | High (dedicated PDF service possible) | High | **Later / optional** |
| **E** | Managed app platform | Unknown / variable | Often poor for headless browser | Variable | **Deferred** |

---

## Option A — Local workstation pilot only

### Description

Continue using `X:\MARS-Localhost\sites\php\projects\iseo-report-hub`.  
Local / internal use only. No external client public URLs unless manual file send or separate tunnel/proxy.

### Pros

- Zero hosting work
- Fastest internal-only pilot
- No production exposure
- Matches current Model A local MVP evidence

### Cons

- Not production
- Workstation availability / uptime risk
- Public share links unusable externally as production delivery
- Local secrets/data concentration risk
- No real HTTPS/domain posture for clients

### Compatibility

| Concern | Assessment |
|---------|------------|
| Current app | Compatible (already running) |
| PDF | Compatible locally (Edge headless attested) |
| Public share | Compatible only for local QA; **not** client production delivery |

### Verdict

**OK** for internal development and operator demo only.  
**Not production.**

---

## Option B — Shared hosting PHP + MySQL

### Description

Classic PHP hosting with MySQL. Public docroot points to `/public`. HTTPS via panel certificate.

### Pros

- Cheap
- Familiar
- Simple day-to-day ops for low traffic
- May be enough for low-traffic internal reporting **if** constraints fit

### Cons

- Headless Edge/Chrome PDF generation often unavailable
- Process execution may be restricted
- Storage permissions may be constrained
- Deployment/backup more manual
- Cron/logging limitations
- Less control over headers / rate limiting

### Compatibility

| Concern | Assessment |
|---------|------------|
| Current app | Possible if PHP 8.3+ (or operator-approved minimum), PDO MySQL, docroot=`public` |
| PDF | **Blocker risk** unless PDF strategy changes (pre-generate elsewhere / serve only) |
| Public share | Possible if HTTPS + stable domain + storage outside webroot enforceable |

### Verdict

**Possible only if** PDF generation strategy is adjusted or PDF generation runs elsewhere.  
Must validate before choosing.

---

## Option C — VPS PHP-FPM/Nginx/MySQL

### Description

VPS with Nginx or Apache + PHP-FPM + MySQL/MariaDB.  
Storage outside webroot. HTTPS via Let’s Encrypt or provider certificate.  
Headless browser PDF generation possible if installed and validated.

### Pros

- Controlled runtime
- Supports storage, backups, logs, headers, rate limiting
- Best fit for current custom PHP app and headless PDF path
- Scalable enough for MVP / first pilot
- Release symlink / shared storage layout supports rollback

### Cons

- Server administration responsibility
- Backup / monitoring / security must be configured deliberately
- Deployment pipeline needed (even if simple)

### Compatibility

| Concern | Assessment |
|---------|------------|
| Current app | **Best fit** |
| PDF | Realistic if Chromium/Chrome/Edge headless validated |
| Public share | Strong — HTTPS domain + controlled headers + protected logs |

### Verdict

**Recommended candidate** for first real production pilot.  
Not provisioned by this charter.

---

## Option D — Containerized VPS

### Description

Docker/Compose deployment with app, DB, webserver, optional worker/PDF service.

### Pros

- More reproducible
- Clean separation of concerns
- Easier future portability
- Optional dedicated PDF sidecar

### Cons

- Higher setup complexity
- May be overkill for first pilot
- Needs container image/maintenance discipline
- Extra operational surface vs bare VPS for small team

### Compatibility

| Concern | Assessment |
|---------|------------|
| Current app | Compatible with packaging effort |
| PDF | Compatible (often better isolation) |
| Public share | Compatible |

### Verdict

**Strong later option.** Not first unless operator explicitly wants containerization now.

---

## Option E — Managed app platform

### Description

Cloud managed PHP/app platform + managed DB.

### Pros

- Managed infra; backups sometimes included
- Less OS administration

### Cons

- May not fit PHP + headless PDF assumptions
- Pricing / vendor complexity
- Current MARS Model A flow not designed around it
- Docroot / storage layout constraints vary by vendor

### Compatibility

| Concern | Assessment |
|---------|------------|
| Current app | **SAFE UNKNOWN** until specific platform chosen |
| PDF | Often weak |
| Public share | Depends on custom domain + HTTPS + log controls |

### Verdict

**Deferred.**

---

## Explicitly rejected / deferred topologies

| Topology | Status | Reason |
|----------|--------|--------|
| Local-only as production | **Rejected** | No uptime/HTTPS/client delivery posture |
| Public tunnel (ngrok-like) as production | **Rejected** | Unstable URLs, trust/security/ops debt |
| Client portal / email / landing as env prerequisite | **Deferred (product)** | Gates M/N; not environment blockers for minimal PDF share pilot |
| Containers as mandatory first step | **Deferred** | Optional later unless operator chooses D |

---

## Recommendation

For first production pilot: **Option C**.  
Operator confirmation required in **Production Environment Decision 01**.
