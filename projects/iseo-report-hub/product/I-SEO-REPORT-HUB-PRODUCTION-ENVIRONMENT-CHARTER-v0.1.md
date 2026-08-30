# I-SEO Report Hub — Production Environment Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no app-source; no runtime; no DB mutation; no SQL/migration; no share token; no public route change; no artifact regeneration; no production hosting setup; no domain/DNS/HTTPS/server operations; no deployment  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Authority:** Operator I-SEO Report Hub Production Environment Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPTIONS-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPTIONS-v0.1.md)
- [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-REQUIREMENTS-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-REQUIREMENTS-v0.1.md)
- [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-LOG-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-LOG-v0.1.md)
- [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-VALIDATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-GATES-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-GATES-v0.1.md)

---

## 1. Purpose

Определить **environment / deployment topology** для следующего production path i-SEO Report Hub.

Эта волна — **docs/policy only**. Она **не** provision’ит сервер, **не** покупает домен, **не** настраивает HTTPS и **не** деплоит приложение.

Charter должен ответить:

1. Где и как приложение может быть размещено для production / pilot.
2. Какие environment options подходят под текущий custom PHP + MySQL + headless PDF stack.
3. Что оператор должен выбрать до любой production implementation.
4. Какие runtime constraints критичны (PHP, MySQL, webserver, storage, HTTPS, domain, secrets, deploy, backup).
5. Какие production blockers закрываются выбором среды (часть Gate E и смежные F/G/H/J).
6. Какой следующий wave идёт после charter.

**Production Environment Charter ≠ production deployment.**  
Charter фиксирует варианты и требования. Deployment — только после operator Decision wave и отдельного implementation charter.

---

## 2. Current State

### Local MVP (attested)

| Item | State |
|------|-------|
| Report Delivery Production Readiness Charter 01 | **COMPLETE** — primary `fd99ce7d…`; hash-record `677d07fa…`; tip at charter start `07505b97…` |
| Local MVP readiness | **Ready** for controlled local / workstation use |
| Production deployment | **NOT ready** |
| Gates **A–D** | **PASS** — functional flow; export integrity; public share security; client handoff UX |
| Gates **E–K** | **REQUIRED_BEFORE_PRODUCTION** |
| Gate **L** | **READY_FOR_PLAN** (retention/pruning) |
| Gates **M–N** | **DEFERRED** (DB-11; landing/portal/email) |

### Client Handoff / Public Share baseline

| Item | State |
|------|-------|
| Client Handoff Visual QA 01 | **PASS**; smoke **129/129**; BLOCKER/MAJOR/MINOR **0** |
| Public route | `GET /share/report/{token}` — direct PDF stream only |
| Token model | hash only in DB; plaintext URL once; exact 64-hex; 404/410 policy |
| Not present | public landing; `/r/{token}`; email; client portal |

### Expected local DB state (latest attested Visual QA; not re-mutated)

| Metric | Expected |
|--------|----------|
| schema_migrations | **9** |
| tables | **16** |
| report_exports | **4** |
| report_export_shares | **6** revoked; active **0** |
| users / roles | **1** / **6** |
| clients / projects / sites | **1** / **1** / **1** |
| reporting_periods / weekly / monthly / blocks / snapshots | **2** / **4** / **1** / **6** / **1** |

Data classification: **LOCAL_FIXTURE_ONLY** — not production client data.

### Local runtime (non-production)

| Item | Value |
|------|-------|
| Source model | Model A — `projects/iseo-report-hub/app-source/` → Localhost runtime |
| Runtime | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |
| Public docroot | `…\public` |
| Local domain | `iseo-report-hub.test` (HTTP) |
| Local DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| PDF engine (local) | Edge headless (Chrome alternate) |

### DB live re-probe caveat

Во время Production Readiness Charter 01 live MySQL read-only re-probe к `127.0.0.1` завершился **connection refused**.  
В этой волне optional read-only probe снова **failed** (PDOException / connection refused).

**SAFE UNKNOWN:** текущий live DB state не подтверждён в этой сессии.  
Ожидаемый baseline берётся из Client Handoff Visual QA 01. Перед будущей implementation-волной local DB state нужно re-check’нуть, если он снова используется как evidence.

Artifact checksums (optional read-only filesystem check this wave):

| Artifact | SHA-256 |
|----------|---------|
| v1 HTML | `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` |
| v1 PDF | `707e72d65f253de17070980e2be36b91f59c4e6faf4352e73d3b1849880d0320` |
| v2 HTML | `27a6eee6f6729f5a081865a24aa1e4ca1f94554ff38d4a1278682f16f95f6ffe` |
| v2 PDF | `a8c4d61c6216e8d70b193115faeab345c0c61ed25ee97a96b740f5f041a56b6b` |

---

## 3. Environment Options

Сравнение подробно: [OPTIONS](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPTIONS-v0.1.md).

| Option | Short name | Production suitability |
|--------|------------|------------------------|
| **A** | Local workstation pilot only | **Not production** — internal demo / local MVP only |
| **B** | Shared hosting PHP + MySQL | **Conditional** — only if PDF strategy validated under host limits |
| **C** | VPS PHP-FPM / Nginx (or Apache) / MySQL | **Recommended candidate** for first real production pilot |
| **D** | Containerized VPS | **Later** — strong, usually overkill for first pilot |
| **E** | Managed app platform | **Deferred** — fit with headless PDF / MARS flow unproven |

**Rejected as production:**

- Local-only as “production”
- Public tunnel / ad-hoc proxy as production topology
- Client portal / email / public landing as environment prerequisites (product deferred, Gates M/N)

---

## 4. Recommended Candidate

**Option C — VPS PHP-FPM/Nginx/MySQL** (Apache acceptable if operator prefers).

Reasons:

1. Current app is custom plain PHP + MySQL (no Composer framework product claim required for deploy topology).
2. Public share requires **HTTPS** + stable domain for client-facing URLs.
3. Export storage must remain **outside** public webroot.
4. Headers, rate-limiting posture, log policy, and least-privilege DB are easier to control on VPS.
5. Headless browser PDF generation is more realistic than on typical shared hosting.
6. Release layout (current/releases/shared) supports backup/rollback discipline for Gates G/H.

**This charter does not provision Option C.** Operator must confirm hosting/domain/PDF/deploy choices in Decision 01.

---

## 5. Required Operator Decisions

Точный список (см. также [DECISION-LOG](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-LOG-v0.1.md)):

1. **Production host type** — VPS preferred; shared hosting only if constraints validated.
2. **Production domain / subdomain** — e.g. operator-approved `reports.…` or equivalent.
3. **HTTPS / certificate method** — Let’s Encrypt / panel / reverse proxy.
4. **DB engine** — MySQL 8.x preferred or MariaDB compatible.
5. **PHP version** — target **8.3** if available; acceptable minimum must be decided.
6. **PDF generation mode** — headless on prod; or generate internally and upload; or serve pre-generated only.
7. **Deployment method** — Git-based deploy; SFTP exact sync; or release archive.
8. **Backup location** — DB dumps + artifact storage; encrypted / access-restricted.
9. **Access model** — who can login; password policy; VPN / IP allowlist / basic auth for admin initially.
10. **Logging policy** — token URL sensitivity; protection/rotation of access logs.
11. **Real client data readiness** — internal test client vs real client data for first pilot.
12. **DB-11 delivery events** — still deferred unless operator reopens before pilot.

---

## 6. Hard Boundaries

This charter **must not**:

- provision VPS / shared hosting / containers;
- purchase or configure domain / DNS;
- request or install TLS certificates;
- SSH / FTP / SFTP / server login;
- mutate app-source, runtime, DB, artifacts;
- create share tokens or change public routes;
- change `.env` / `.env.local`;
- sync source → runtime;
- install packages;
- implement portal / email / landing;
- recommend immediate production deployment.

STOP conditions for **future** production implementation (preview; enforced in later charters):

- no chosen production host/domain/HTTPS;
- docroot not restricted to `/public`;
- storage/logs under public webroot;
- secrets in Git;
- `APP_ENV` not production / debug on;
- fixture DB reused as production DB;
- no pre-migration backup / no restore drill evidence;
- headless PDF claimed but unvalidated on host when production generation is in scope;
- push/deploy without explicit operator deploy charter.

Requirements detail: [REQUIREMENTS](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-REQUIREMENTS-v0.1.md).  
Future validation (no server access now): [VALIDATION-PLAN](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-VALIDATION-PLAN-v0.1.md).

---

## 7. Next Action

**I-SEO Report Hub — Production Environment Decision 01**

Purpose: operator selects hosting / domain / deploy / PDF strategy.  
After decision: create implementation charter for the chosen path.

Alternative (only if operator already supplies target server/domain):  
**I-SEO Report Hub — Production Environment Validation 01**.

Do **not** recommend production deployment immediately.
