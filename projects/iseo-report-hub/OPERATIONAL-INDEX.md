# i-SEO Report Hub — Operational Index

**project_id:** `iseo-report-hub`  
**Classification:** documentation-first product locus (Lane B)  
**Domain root:** [README.md](README.md)

---

## Programme identity

| Field | Value |
|-------|-------|
| **Programme name** | i-SEO Report Hub |
| **Slug** | `iseo-report-hub` |
| **Owner / product architect** | Андрей |
| **Business owner / vision source** | Никита / i-SEO |
| **Developer** | Антон |
| **Platform direction** | **Decided** — custom **PHP + SQL/MySQL**; **no WordPress runtime**; Laragon local runtime **verified** (preflight 01); see [I-SEO-REPORT-HUB-PLATFORM-DECISION-v0.1.md](product/I-SEO-REPORT-HUB-PLATFORM-DECISION-v0.1.md) |
| **Implementation** | **Phase 1B complete** + **local vhost/hosts mapping complete** + **DB `iseo_report_hub_dev` created** + **DB-01/DB-02 first migration applied** + **auth persistence + local admin bootstrap implemented** + **DB-03 reporting periods migration applied** — DB-backed login/logout; local admin user present; `/health` shows safe DB status; table `reporting_periods` present (0 rows); clients/projects still **0/0** |
| **Source model** | **Model A active** — `projects/iseo-report-hub/app-source/` is versioned SoT; sync direction **source → runtime**; runtime → source only by explicit import charter |

---

## Current status

| Field | Value |
|-------|-------|
| **Status** | planned / product architecture + Phase 0 scaffold + Model A `app-source/` + Phase 1A/1B + local DB + **auth persistence implemented** + **DB-03 migration applied** |
| **Lane** | Lane B — product formation and architecture |
| **Active stage** | **DB-03 Reporting Periods Migration Apply 01 complete** — next recommended: **Project/Client Local Fixture Charter 01** |
| **Registry** | Row added 2026-07-10 — `project_id` **iseo-report-hub** · status **planned** |

---

## Source corpus location

**Path:** `X:\AI MARS STORAGE\incoming\iseo-report-hub\`

**Known structure:**
- materials from Nikita
- reports from Denis
- reports from Ilya

**Known corpus (attested, not re-audited in this task):** 33 files — 30 PDF reports (15 Denis, 15 Ilya), 3 Nikita materials.

**Security exclusion:** Nikita XLSX Лист2 содержит access/credential-related material — **исключён** из product corpus и reporting exports.

---

## Operator review — static demo v0.1 (2026-07-10)

| Decision | Status |
|----------|--------|
| Workflow mechanics (admin → weekly → monthly → review → client) | **Accepted** — demo v0.1 sufficient for mechanical demonstration |
| Report structure fidelity | **Not accepted** — generic fields; does not match intended SEO report structure |
| SEO specialist feedback | **Deferred** — do **not** show v0.1 to SEO specialists as report prototype |
| Platform | **Pivot** — WordPress/i-seo.su no longer sole production assumption; PHP + MySQL custom system is accepted candidate |
| Next stage | **Report Structure Demo v0.2** — inject real report structure + 3 demo projects into static demo |

**Demo workspace (unchanged in pivot task):** `workspaces/website-factory-operations/iseo-report-hub-prototype/` — v0.1 localized static HTML.

---

## Operator review — static demo v0.2 (2026-07-10)

| Decision | Status |
|----------|--------|
| Direction / mechanics / structure | **Accepted** — v0.2 closer to intended SEO report workflow |
| Report block **content depth** | **Not sufficient** — blocks need full content architecture before next demo iteration |
| Full block lists by site/project type | **Required** — documented in Report Type Block Matrix v0.1 |
| Project type selection model | **Required for demo v0.3** — specified in Report Content Architecture v0.1 |
| Staged demo reports (complete / W3 / W1) | **Required for demo v0.3** — specified in Demo Report States v0.1 |
| SEO specialist feedback | **Deferred** — do **not** schedule until operator approves demo v0.3 |
| Next stage | **Static Demo v0.3** — project type selector + full report content architecture + staged demo states |

**Demo workspace:** `workspaces/website-factory-operations/iseo-report-hub-prototype/` — v0.2 static HTML exists; **not modified** in report content architecture task.

---

## Operator review — static demo v0.4 + Product Architecture Layer 02 (2026-07-24)

| Decision | Status |
|----------|--------|
| Static demo v0.4 | **Accepted** as useful **raw** prototype / UX reference (specialist workspace + i-seo style direction) |
| Demo polishing | **Not next** — some panels will later be removed/added; corrections → v0.5 backlog only |
| SEO specialist feedback | **Deferred** — still premature; informal viewers did not produce meaningful notes |
| Product Architecture Layer 02 | **Completed** (documentation) — modules, roles, data model, lifecycle, publishing/snapshots, implementation decision frame |
| Demo workspace in Layer 02 task | **Unchanged** — no HTML/CSS/JS edits |
| Implementation | **Not started** |
| Platform decision (2026-07-24) | **Custom PHP + SQL/MySQL**; WordPress **rejected** as runtime/SoT; Laragon local candidate |
| Next stage | **Operator review** of PHP/MySQL technical brief package, then **scoped commit** |

**Demo workspace:** `workspaces/website-factory-operations/iseo-report-hub-prototype/` — v0.4 exists (commit `66d651a2`); **not modified** in platform decision / technical brief task.

---

## Operator decision — platform + PHP/MySQL MVP technical brief (2026-07-24)

| Decision | Status |
|----------|--------|
| Platform | **Custom PHP + SQL/MySQL** — WordPress **not** runtime / not DB SoT / not admin backend |
| Laragon | **Available** as local dev/runtime candidate (exact path/versions **SAFE UNKNOWN** until Phase 0) |
| WordPress / i-seo.su residual | Visual style reference; optional future embed/link; marketing pages — **not** required for MVP |
| Static demo v0.4 | UX reference only |
| Technical brief package | Created (platform decision, brief, Laragon plan, phases, schema draft, route map) |
| Implementation | **Not started** |
| Next stage | Operator review of PHP/MySQL MVP Technical Brief, then scoped commit |

---

## Laragon runtime preflight 01 (2026-07-24)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — read-only preflight only |
| **Result doc** | [I-SEO-REPORT-HUB-LARAGON-PREFLIGHT-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-LARAGON-PREFLIGHT-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-laragon-runtime-preflight-01.md](reports/REPORT-iseo-report-hub-laragon-runtime-preflight-01.md) |
| **Laragon** | **Found** — `X:\MARS-Localhost\laragon\` (v8.6.1); process running |
| **PHP** | **8.3.30** active (Apache `mod_php` + profile); MVP extensions verified (`pdo_mysql`, `mbstring`, `json`, `openssl`, `fileinfo`, …); not on system PATH |
| **MySQL** | **8.4.3** client + server; port **3306** listening; `SELECT VERSION()` only; **no** DB created |
| **Web server** | Apache **2.4.66** on port **80**; Nginx present, not running |
| **Runtime changes** | **None** — no scaffold, SQL, DB, vhost/hosts, Laragon config, or service restart |
| **Phase 0 readiness** | **Inputs applied** — operator approved runtime path / domain / DB candidate / PHP pin |
| **Next stage (after Phase 0)** | Operator review of Phase 0 scaffold, then **Phase 1** app skeleton / config / auth baseline |

---

## MVP Phase 0 runtime scaffold 01 (2026-07-24)

| Field | Value |
|-------|-------|
| **Status** | **Created** — scaffold only |
| **Result doc** | [I-SEO-REPORT-HUB-MVP-PHASE-0-SCAFFOLD-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-MVP-PHASE-0-SCAFFOLD-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-mvp-phase-0-runtime-scaffold-01.md](reports/REPORT-iseo-report-hub-mvp-phase-0-runtime-scaffold-01.md) |
| **Runtime path** | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub` |
| **Domain (intended)** | `iseo-report-hub.test` — **not** mapped by this task |
| **DB candidate** | `iseo_report_hub_dev` — **not** created |
| **PHP** | 8.3.30 |
| **Secrets** | **None** — `.env.example` placeholders only |
| **What exists** | `public/index.php`, `public/health.php`, folder placeholders, config/env examples |
| **What does not exist** | Auth, DB, migrations, vhost/hosts, product features |
| **Source / runtime** | Runtime outside Active Brain Git; see [SOURCE-RUNTIME-POLICY-v0.1](product/I-SEO-REPORT-HUB-SOURCE-RUNTIME-POLICY-v0.1.md) |
| **Next stage** | Create and commit `app-source/` mirror from Phase 0 scaffold; Phase 1 **blocked** until mirror exists |

---

## Source / runtime policy 01 (2026-07-24)

| Field | Value |
|-------|-------|
| **Status** | **Defined** — policy v0.1 |
| **Policy doc** | [I-SEO-REPORT-HUB-SOURCE-RUNTIME-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-SOURCE-RUNTIME-POLICY-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-phase-0-runtime-review-source-runtime-policy-01.md](reports/REPORT-iseo-report-hub-phase-0-runtime-review-source-runtime-policy-01.md) |
| **Active Brain** | `X:\AI MARS\projects\iseo-report-hub\` — committed docs/specs authority |
| **Runtime** | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` — local runnable workspace; **not** a separate Git repo |
| **Versioning issue** | Runtime outside monorepo — not committed by normal Active Brain commits |
| **Recommended model** | **Model A** — versioned `app-source/` under Active Brain + sync/deploy to Localhost runtime |
| **Not done in this wave** | No `app-source/` created; no runtime Git repo; no DB/vhost/hosts |
| **Phase 1** | **Blocked** until source preservation model approved |
| **Recommended next** | Create source mirror + deploy/sync charter for Model A |

---

## Model A source mirror + deploy/sync charter 01 (2026-07-24)

| Field | Value |
|-------|-------|
| **Status** | **Charter complete** — documentation only; no mirror/sync executed |
| **Model** | **Model A selected for planning** |
| **Source path (planned)** | `X:\AI MARS\projects\iseo-report-hub\app-source\` — **does not exist yet** |
| **Runtime target** | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |
| **Sync direction** | **source → runtime** (default); runtime → source only via explicit import charter |
| **Charter** | [I-SEO-REPORT-HUB-MODEL-A-SOURCE-MIRROR-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-MODEL-A-SOURCE-MIRROR-CHARTER-v0.1.md) |
| **Deploy/sync policy** | [I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md) |
| **File map** | [I-SEO-REPORT-HUB-SOURCE-MIRROR-FILE-MAP-v0.1.md](product/I-SEO-REPORT-HUB-SOURCE-MIRROR-FILE-MAP-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-model-a-source-mirror-deploy-sync-charter-01.md](reports/REPORT-iseo-report-hub-model-a-source-mirror-deploy-sync-charter-01.md) |
| **Not done** | No `app-source/` creation; no runtime copy; no sync; no runtime edits; no DB/vhost/hosts |
| **Phase 1** | **Blocked** until `app-source/` mirror exists, is committed, and sync/deploy policy is accepted |
| **Next stage** | Create and commit `app-source/` mirror from Phase 0 scaffold using the approved file map |

---

## App-source mirror create 01 (2026-07-24)

| Field | Value |
|-------|-------|
| **Status** | **Created** — versioned Active Brain source mirror |
| **Result doc** | [I-SEO-REPORT-HUB-APP-SOURCE-MIRROR-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-APP-SOURCE-MIRROR-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-create-app-source-mirror-from-phase-0-scaffold-01.md](reports/REPORT-iseo-report-hub-create-app-source-mirror-from-phase-0-scaffold-01.md) |
| **Source path** | `X:\AI MARS\projects\iseo-report-hub\app-source\` |
| **Runtime path** | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |
| **Sync policy** | Ongoing direction **source → runtime**; this wave was one-time allowlist copy **runtime → app-source** (bootstrap import); **no** source → runtime sync executed |
| **Copied** | Phase 0 source-safe allowlist (26 files) per file map |
| **Not done** | No runtime overwrite; no DB; no vhost/hosts; no `.env` / `.env.local`; no secrets |
| **Phase 1** | May be **chartered after operator review** of this mirror; DB / vhost / hosts remain separate charters |

---

## MVP Phase 1A app skeleton + config baseline 01 (2026-07-24)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — source-only Phase 1A skeleton |
| **Result doc** | [I-SEO-REPORT-HUB-MVP-PHASE-1A-APP-SKELETON-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-MVP-PHASE-1A-APP-SKELETON-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-mvp-phase-1a-app-skeleton-config-baseline-01.md](reports/REPORT-iseo-report-hub-mvp-phase-1a-app-skeleton-config-baseline-01.md) |
| **Source path** | `X:\AI MARS\projects\iseo-report-hub\app-source\` |
| **What exists** | Front controller, bootstrap, router, layout/views, controllers, Config/Auth/Csrf services, helpers, health/login/dashboard stubs |
| **Runtime** | **Not synced** — Localhost runtime untouched |
| **DB** | **Not created** · no connection |
| **Secrets** | **None** — no `.env` / `.env.local` |
| **Next stage** | **Phase 1B** — source → runtime sync + local smoke |

---

## MVP Phase 1B source → runtime sync + local smoke 01 (2026-07-24)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — allowlist source → runtime sync + local smoke |
| **Result doc** | [I-SEO-REPORT-HUB-MVP-PHASE-1B-RUNTIME-SYNC-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-MVP-PHASE-1B-RUNTIME-SYNC-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-mvp-phase-1b-source-to-runtime-sync-local-smoke-01.md](reports/REPORT-iseo-report-hub-mvp-phase-1b-source-to-runtime-sync-local-smoke-01.md) |
| **Source path** | `X:\AI MARS\projects\iseo-report-hub\app-source\` |
| **Runtime path** | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |
| **Sync** | Allowlist copy — **44** files; missing **0**; no wipe |
| **Smoke** | `php -l` PASS (25 files); CLI routes PASS; built-in server `127.0.0.1:8088` PASS then stopped |
| **DB** | **Not created** · not tested |
| **vhost / hosts** | **Not configured** |
| **Secrets** | **None** — no `.env` / `.env.local` |
| **Next stage** | **Local vhost/hosts mapping charter** for `iseo-report-hub.test` |

---

## Local vhost / hosts mapping 01 (2026-07-24)

| Field | Value |
|-------|-------|
| **Status** | **Partial** — Option B vhost + Option C hosts manual |
| **Result doc** | [I-SEO-REPORT-HUB-LOCAL-VHOST-HOSTS-MAPPING-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-VHOST-HOSTS-MAPPING-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-local-vhost-hosts-mapping-01.md](reports/REPORT-iseo-report-hub-local-vhost-hosts-mapping-01.md) |
| **Domain** | `iseo-report-hub.test` |
| **DocumentRoot** | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\public` |
| **Vhost file** | `X:\MARS-Localhost\laragon\etc\apache2\sites-enabled\iseo-report-hub.test.conf` (**created**) |
| **Hosts entry** | **Not added** — elevated write denied; manual: `127.0.0.1 iseo-report-hub.test` |
| **HTTP smoke** | Host-header against `127.0.0.1`: `/` `/health` `/login` → **200**; `/not-existing` → **404**; domain URL unresolved until hosts |
| **DB** | **Not created** · not tested |
| **Secrets** | **None** — no `.env` / `.env.local` |
| **App code** | **Unchanged** |
| **Next stage** | **Fix mapping** (add hosts line + domain smoke); then **DB creation + schema migration charter** |

---

## Local hosts re-smoke 01 (2026-07-24)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — direct domain smoke **PASS** |
| **Result doc** | [I-SEO-REPORT-HUB-LOCAL-HOSTS-RESMOKE-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-HOSTS-RESMOKE-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-local-hosts-resmoke-01.md](reports/REPORT-iseo-report-hub-local-hosts-resmoke-01.md) |
| **Domain** | `iseo-report-hub.test` |
| **Hosts entry** | **Present** — `127.0.0.1 iseo-report-hub.test` (operator manual; no agent hosts edit) |
| **DNS** | Resolves to **127.0.0.1** |
| **Vhost** | Unchanged — already present from mapping 01 |
| **Direct HTTP** | `/` `/health` `/login` → **200**; `/not-existing` → **404** |
| **Markers** | `i-SEO Report Hub`; `data-phase="1a"`; DB negation; no SQL error |
| **DB** | **Not created** · not tested |
| **Secrets** | **None** — no `.env` / `.env.local` |
| **App code** | **Unchanged** |
| **Apache restart** | **Not performed** |
| **Next stage** | **DB creation + schema migration charter** |

---

## DB creation + schema migration charter 01 (2026-07-24)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — documentation / policy only |
| **DB charter** | [I-SEO-REPORT-HUB-DB-CREATION-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-DB-CREATION-CHARTER-v0.1.md) |
| **Migration policy** | [I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md) |
| **Initial schema plan** | [I-SEO-REPORT-HUB-INITIAL-SCHEMA-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-INITIAL-SCHEMA-PLAN-v0.1.md) |
| **Local env / secrets policy** | [I-SEO-REPORT-HUB-LOCAL-ENV-DB-SECRETS-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-ENV-DB-SECRETS-POLICY-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-db-creation-schema-migration-charter-01.md](reports/REPORT-iseo-report-hub-db-creation-schema-migration-charter-01.md) |
| **DB target** | `iseo_report_hub_dev` @ `127.0.0.1:3306` (MySQL 8.4.3) |
| **DB created** | **No** |
| **SQL executed** | **No** |
| **Migration files** | **None** (planned under `app-source/database/migrations/`) |
| **`.env.local`** | **Not created** |
| **First migration scope (planned)** | DB-01 + minimal DB-02 (`schema_migrations`, auth, clients/projects/sites/profiles) |
| **App-source / runtime** | **Unchanged** |
| **Next stage** | **DB creation + DB-01/DB-02 migration files/apply charter** |

---

## DB creation + DB-01/DB-02 migration files apply 01 (2026-07-24)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — local DB created + first migration applied |
| **Result doc** | [I-SEO-REPORT-HUB-DB-01-DB-02-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DB-01-DB-02-MIGRATION-APPLY-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-db-creation-db01-db02-migration-files-apply-01.md](reports/REPORT-iseo-report-hub-db-creation-db01-db02-migration-files-apply-01.md) |
| **DB** | `iseo_report_hub_dev` @ `127.0.0.1:3306` — **created** (`utf8mb4` / `utf8mb4_0900_ai_ci`) |
| **Migration file** | `app-source/database/migrations/2026_07_24_000001_create_core_tables.sql` |
| **Migration tool** | `app-source/tools/db-migrate.php` (`status` / `apply`) |
| **Apply** | **PASS** — ledger row present; checksum `71dd22d0…be722bb4` |
| **DB smoke** | 9 expected tables; roles **6**; users **0**; idempotent re-apply OK |
| **`.env.local`** | **Runtime-only** created; **not** in Git; source keeps `.env.example` |
| **HTTP** | `/health` still **200** (app health code unchanged) |
| **App code** | **Unchanged** (`app/` / `public/` / `config/`) |
| **Next stage (at apply close)** | Auth persistence + local admin bootstrap charter — **completed** in charter 01; then **Auth Persistence + Local Admin Bootstrap Implementation 01** |

---

## Auth persistence + local admin bootstrap charter 01 (2026-07-24)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — documentation / policy only |
| **Auth persistence charter** | [I-SEO-REPORT-HUB-AUTH-PERSISTENCE-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-AUTH-PERSISTENCE-CHARTER-v0.1.md) |
| **Local admin bootstrap policy** | [I-SEO-REPORT-HUB-LOCAL-ADMIN-BOOTSTRAP-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-ADMIN-BOOTSTRAP-POLICY-v0.1.md) |
| **DB connection / health policy** | [I-SEO-REPORT-HUB-DB-CONNECTION-HEALTH-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-DB-CONNECTION-HEALTH-POLICY-v0.1.md) |
| **Auth implementation plan** | [I-SEO-REPORT-HUB-AUTH-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-AUTH-IMPLEMENTATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-auth-persistence-local-admin-bootstrap-charter-01.md](reports/REPORT-iseo-report-hub-auth-persistence-local-admin-bootstrap-charter-01.md) |
| **App-source / runtime** | **Unchanged** |
| **DB mutation** | **No** |
| **Admin user** | **Not created** |
| **Password / hash** | **Not generated** |
| **`.env` / `.env.local`** | **Unchanged** |
| **SQL executed** | **No** |
| **Auth code** | Still **stub** (`AuthService::login` → `not_implemented`) |
| **Next stage** | **Auth Persistence + Local Admin Bootstrap Implementation 01** — **completed** (see implementation section below) |

---

## Auth persistence + local admin bootstrap implementation 01 (2026-07-25)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — DB-backed auth + local admin + smoke |
| **Result doc** | [I-SEO-REPORT-HUB-AUTH-PERSISTENCE-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-AUTH-PERSISTENCE-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-auth-persistence-local-admin-bootstrap-implementation-01.md](reports/REPORT-iseo-report-hub-auth-persistence-local-admin-bootstrap-implementation-01.md) |
| **Auth** | **DB-backed** login/logout/session/roles/audit (stub replaced) |
| **Local admin** | **Created** — `admin@iseo-report-hub.test` / role `admin_owner` (password not stored in docs) |
| **Users / roles** | users **1** · roles **6** |
| **DB health on `/health`** | Safe status **PASS** (configured/connection/name/migrations/tables/counts; no secrets) |
| **Smoke** | lint PASS; failed login / success login / dashboard / logout / health / 404 PASS; duplicate admin refused |
| **Secrets** | No password/hash/credentials in Git or reports; runtime `.env.local` unchanged/outside Git |
| **Schema** | **No** migration edits |
| **Next stage** | **DB-03 reporting periods migration apply** — **completed** (see DB-03 apply section below) |

---

## DB-03 reporting periods migration charter 01 (2026-07-25)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — documentation / policy only |
| **Auth baseline dependency** | Auth persistence implemented (`d4b3b2e2` + hash-record `0cd2cfb7`); users **1**; roles **6**; local admin present |
| **DB baseline** | First migration applied; checksum `71dd22d0…be722bb4`; tables **9**; `reporting_periods` **absent** |
| **Charter** | [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-CHARTER-v0.1.md) |
| **Schema plan** | [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md) |
| **Migration plan** | [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-PLAN-v0.1.md) |
| **Period lifecycle** | [I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md](product/I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-DB-03-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-03-IMPLEMENTATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-db03-reporting-periods-migration-charter-01.md](reports/REPORT-iseo-report-hub-db03-reporting-periods-migration-charter-01.md) |
| **Planned SQL filename** | `2026_07_25_000002_create_reporting_periods_table.sql` — later applied (see apply section below) |
| **App-source / runtime / DB** | Charter wave docs only; apply completed in separate wave |

---

## DB-03 reporting periods migration apply 01 (2026-07-25)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — migration authored, synced, applied, validated |
| **Migration file** | `2026_07_25_000002_create_reporting_periods_table.sql` |
| **Checksum (SHA-256)** | `5bc50e53ab20a347c8a278d1726be6c71d835b572f369a14d2256e3e986e3be9` |
| **Batch** | **2** |
| **Table created** | `reporting_periods` |
| **Migration count** | **1 → 2** |
| **Table count** | **9 → 10** |
| **Validation** | columns/indexes/FKs/CHECKs present; idempotent re-apply PASS; clients/projects remain **0/0**; reporting_periods rows **0** |
| **Unique/FK row smoke** | structural only (no project fixture) |
| **Result doc** | [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-APPLY-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-db03-reporting-periods-migration-apply-01.md](reports/REPORT-iseo-report-hub-db03-reporting-periods-migration-apply-01.md) |
| **App / auth code** | **unchanged** |
| **Next recommended stage** | **Project/Client Local Fixture Charter 01** |

---

## Current approved decisions (summary)

1. Report Hub — **операционная система отчётности**, не PDF-only tool.
2. **Platform** — **custom PHP + SQL/MySQL** (operator decision 2026-07-24); WordPress **rejected** as runtime/SoT; see [PLATFORM-DECISION-v0.1](product/I-SEO-REPORT-HUB-PLATFORM-DECISION-v0.1.md).
3. **Laragon** — local runtime **verified** at `X:\MARS-Localhost\laragon\` (preflight 01); PHP 8.3.30 / MySQL 8.4.3 / Apache 2.4.66; no iseo site/DB yet.
4. **n8n** — external helper (AI, reminders, notifications); **не** SoT.
5. **Primary client output** — web report from published snapshots via token URL; PDF optional later.
6. **Reporting period** — 1 month; 3 weekly checkpoints + 1 monthly final.
7. **MVP direction** — internal admin, manual data, evidence, Topvisor external link, approval/publish on custom PHP app.
8. **Credentials/secrets** — отдельный secure integration concern; **не** в report content.

---

## Canonical documents

| # | Document | Purpose |
|---|----------|---------|
| 1 | [README.md](README.md) | Programme entry |
| 2 | [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | This index |
| 3 | [product/I-SEO-REPORT-HUB-PRODUCT-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-PRODUCT-CHARTER-v0.1.md) | Approved charter |
| 4 | [product/I-SEO-REPORT-HUB-WORDPRESS-PRODUCT-ARCHITECTURE-v0.1.md](product/I-SEO-REPORT-HUB-WORDPRESS-PRODUCT-ARCHITECTURE-v0.1.md) | WordPress architecture |
| 5 | [product/I-SEO-REPORT-HUB-REPORT-MODEL-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-MODEL-v0.1.md) | Report model |
| 6 | [product/I-SEO-REPORT-HUB-MVP-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-MVP-SCOPE-v0.1.md) | MVP scope |
| 7 | [reports/REPORT-iseo-report-hub-project-charter-architecture-persist-01.md](reports/REPORT-iseo-report-hub-project-charter-architecture-persist-01.md) | Persist closeout report |
| 8 | [product/I-SEO-REPORT-HUB-WORDPRESS-DATA-MODEL-v0.1.md](product/I-SEO-REPORT-HUB-WORDPRESS-DATA-MODEL-v0.1.md) | WordPress data model planning |
| 9 | [product/I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md](product/I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md) | Admin UX flow planning |
| 10 | [product/I-SEO-REPORT-HUB-WEB-REPORT-STRUCTURE-v0.1.md](product/I-SEO-REPORT-HUB-WEB-REPORT-STRUCTURE-v0.1.md) | Client web report structure |
| 11 | [product/I-SEO-REPORT-HUB-IMPLEMENTATION-BRIEF-v0.1.md](product/I-SEO-REPORT-HUB-IMPLEMENTATION-BRIEF-v0.1.md) | Implementation brief for Anton |
| 12 | [reports/REPORT-iseo-report-hub-wordpress-data-model-admin-ux-planning-01.md](reports/REPORT-iseo-report-hub-wordpress-data-model-admin-ux-planning-01.md) | Planning closeout report |
| 13 | [product/I-SEO-REPORT-HUB-WEBSITE-FACTORY-PROTOTYPE-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-WEBSITE-FACTORY-PROTOTYPE-CHARTER-v0.1.md) | Website Factory prototype charter |
| 14 | [product/I-SEO-REPORT-HUB-WEBSITE-FACTORY-DEMO-BRIEF-v0.1.md](product/I-SEO-REPORT-HUB-WEBSITE-FACTORY-DEMO-BRIEF-v0.1.md) | Website Factory demo build brief |
| 15 | [reports/REPORT-iseo-report-hub-website-factory-prototype-charter-01.md](reports/REPORT-iseo-report-hub-website-factory-prototype-charter-01.md) | Prototype charter closeout report |
| 16 | [reports/REPORT-iseo-report-hub-website-factory-static-demo-build-01.md](reports/REPORT-iseo-report-hub-website-factory-static-demo-build-01.md) | Static demo build closeout |
| 17 | [reports/REPORT-iseo-report-hub-website-factory-demo-russian-localization-01.md](reports/REPORT-iseo-report-hub-website-factory-demo-russian-localization-01.md) | Demo Russian localization closeout |
| 18 | [product/I-SEO-REPORT-HUB-PLATFORM-OPTIONS-v0.1.md](product/I-SEO-REPORT-HUB-PLATFORM-OPTIONS-v0.1.md) | Platform options (WP vs PHP+MySQL) |
| 19 | [product/I-SEO-REPORT-HUB-REPORT-STRUCTURE-MODEL-v0.2.md](product/I-SEO-REPORT-HUB-REPORT-STRUCTURE-MODEL-v0.2.md) | Report structure model for demo v0.2 |
| 20 | [product/I-SEO-REPORT-HUB-DEMO-CONTENT-PACK-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-CONTENT-PACK-v0.1.md) | Sanitized demo content for 3 projects |
| 21 | [reports/REPORT-iseo-report-hub-platform-pivot-report-structure-modeling-01.md](reports/REPORT-iseo-report-hub-platform-pivot-report-structure-modeling-01.md) | Platform pivot + structure modeling closeout |
| 22 | [product/I-SEO-REPORT-HUB-REPORT-CONTENT-ARCHITECTURE-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-CONTENT-ARCHITECTURE-v0.1.md) | Report content architecture (philosophy, objects, flows) |
| 23 | [product/I-SEO-REPORT-HUB-REPORT-TYPE-BLOCK-MATRIX-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-TYPE-BLOCK-MATRIX-v0.1.md) | Full block matrix by project/site type |
| 24 | [product/I-SEO-REPORT-HUB-DEMO-REPORT-STATES-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-REPORT-STATES-v0.1.md) | Staged demo scenarios for v0.3 |
| 25 | [reports/REPORT-iseo-report-hub-static-demo-v0.2-report-structure-injection-01.md](reports/REPORT-iseo-report-hub-static-demo-v0.2-report-structure-injection-01.md) | Static demo v0.2 build closeout |
| 26 | [reports/REPORT-iseo-report-hub-report-content-architecture-01.md](reports/REPORT-iseo-report-hub-report-content-architecture-01.md) | Report content architecture closeout |
| 27 | [reports/REPORT-iseo-report-hub-static-demo-v0.4-iseo-style-specialist-workspace-01.md](reports/REPORT-iseo-report-hub-static-demo-v0.4-iseo-style-specialist-workspace-01.md) | Static demo v0.4 closeout |
| 28 | [product/I-SEO-REPORT-HUB-PRODUCT-ARCHITECTURE-LAYER-02-v0.1.md](product/I-SEO-REPORT-HUB-PRODUCT-ARCHITECTURE-LAYER-02-v0.1.md) | Product Architecture Layer 02 |
| 29 | [product/I-SEO-REPORT-HUB-ROLE-AND-PERMISSION-MODEL-v0.1.md](product/I-SEO-REPORT-HUB-ROLE-AND-PERMISSION-MODEL-v0.1.md) | Roles and permissions |
| 30 | [product/I-SEO-REPORT-HUB-DATA-MODEL-v0.1.md](product/I-SEO-REPORT-HUB-DATA-MODEL-v0.1.md) | Conceptual data model |
| 31 | [product/I-SEO-REPORT-HUB-REPORT-LIFECYCLE-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-LIFECYCLE-v0.1.md) | Period/weekly/monthly/block lifecycle |
| 32 | [product/I-SEO-REPORT-HUB-PUBLISHING-AND-SNAPSHOT-MODEL-v0.1.md](product/I-SEO-REPORT-HUB-PUBLISHING-AND-SNAPSHOT-MODEL-v0.1.md) | Publishing and snapshots |
| 33 | [product/I-SEO-REPORT-HUB-IMPLEMENTATION-OPTIONS-DECISION-FRAME-v0.1.md](product/I-SEO-REPORT-HUB-IMPLEMENTATION-OPTIONS-DECISION-FRAME-v0.1.md) | WP / PHP+MySQL / hybrid decision frame |
| 34 | [product/I-SEO-REPORT-HUB-V0.5-DEMO-CORRECTIONS-BACKLOG-v0.1.md](product/I-SEO-REPORT-HUB-V0.5-DEMO-CORRECTIONS-BACKLOG-v0.1.md) | Future demo v0.5 corrections backlog |
| 35 | [reports/REPORT-iseo-report-hub-product-architecture-layer-02.md](reports/REPORT-iseo-report-hub-product-architecture-layer-02.md) | Layer 02 closeout report |
| 36 | [product/I-SEO-REPORT-HUB-PLATFORM-DECISION-v0.1.md](product/I-SEO-REPORT-HUB-PLATFORM-DECISION-v0.1.md) | Platform decision: PHP + MySQL, no WP runtime |
| 37 | [product/I-SEO-REPORT-HUB-PHP-MYSQL-MVP-TECHNICAL-BRIEF-v0.1.md](product/I-SEO-REPORT-HUB-PHP-MYSQL-MVP-TECHNICAL-BRIEF-v0.1.md) | PHP/MySQL MVP technical brief |
| 38 | [product/I-SEO-REPORT-HUB-LARAGON-LOCAL-RUNTIME-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-LARAGON-LOCAL-RUNTIME-PLAN-v0.1.md) | Laragon local runtime plan |
| 39 | [product/I-SEO-REPORT-HUB-MVP-IMPLEMENTATION-PHASES-v0.1.md](product/I-SEO-REPORT-HUB-MVP-IMPLEMENTATION-PHASES-v0.1.md) | MVP implementation phases 0–11 |
| 40 | [product/I-SEO-REPORT-HUB-MVP-SCHEMA-DRAFT-v0.1.md](product/I-SEO-REPORT-HUB-MVP-SCHEMA-DRAFT-v0.1.md) | Conceptual MVP schema draft |
| 41 | [product/I-SEO-REPORT-HUB-MVP-ROUTE-AND-SCREEN-MAP-v0.1.md](product/I-SEO-REPORT-HUB-MVP-ROUTE-AND-SCREEN-MAP-v0.1.md) | Conceptual route/screen map |
| 42 | [reports/REPORT-iseo-report-hub-platform-decision-php-mysql-technical-brief-01.md](reports/REPORT-iseo-report-hub-platform-decision-php-mysql-technical-brief-01.md) | Platform decision + technical brief closeout |
| 43 | [product/I-SEO-REPORT-HUB-LARAGON-PREFLIGHT-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-LARAGON-PREFLIGHT-RESULT-v0.1.md) | Laragon/runtime preflight result (read-only) |
| 44 | [reports/REPORT-iseo-report-hub-laragon-runtime-preflight-01.md](reports/REPORT-iseo-report-hub-laragon-runtime-preflight-01.md) | Laragon runtime preflight closeout |
| 45 | [product/I-SEO-REPORT-HUB-MVP-PHASE-0-SCAFFOLD-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-MVP-PHASE-0-SCAFFOLD-RESULT-v0.1.md) | MVP Phase 0 runtime scaffold result |
| 46 | [reports/REPORT-iseo-report-hub-mvp-phase-0-runtime-scaffold-01.md](reports/REPORT-iseo-report-hub-mvp-phase-0-runtime-scaffold-01.md) | Phase 0 runtime scaffold closeout |
| 47 | [product/I-SEO-REPORT-HUB-SOURCE-RUNTIME-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-SOURCE-RUNTIME-POLICY-v0.1.md) | Source vs Localhost runtime versioning policy |
| 48 | [reports/REPORT-iseo-report-hub-phase-0-runtime-review-source-runtime-policy-01.md](reports/REPORT-iseo-report-hub-phase-0-runtime-review-source-runtime-policy-01.md) | Phase 0 runtime review + source/runtime policy closeout |
| 49 | [product/I-SEO-REPORT-HUB-MODEL-A-SOURCE-MIRROR-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-MODEL-A-SOURCE-MIRROR-CHARTER-v0.1.md) | Model A source mirror charter (planning) |
| 50 | [product/I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md) | Deploy/sync policy source → runtime |
| 51 | [product/I-SEO-REPORT-HUB-SOURCE-MIRROR-FILE-MAP-v0.1.md](product/I-SEO-REPORT-HUB-SOURCE-MIRROR-FILE-MAP-v0.1.md) | Phase 0 → app-source include/exclude map |
| 52 | [reports/REPORT-iseo-report-hub-model-a-source-mirror-deploy-sync-charter-01.md](reports/REPORT-iseo-report-hub-model-a-source-mirror-deploy-sync-charter-01.md) | Model A source mirror + deploy/sync charter closeout |
| 53 | [product/I-SEO-REPORT-HUB-APP-SOURCE-MIRROR-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-APP-SOURCE-MIRROR-RESULT-v0.1.md) | App-source mirror create result |
| 54 | [reports/REPORT-iseo-report-hub-create-app-source-mirror-from-phase-0-scaffold-01.md](reports/REPORT-iseo-report-hub-create-app-source-mirror-from-phase-0-scaffold-01.md) | App-source mirror create closeout |
| 55 | [app-source/](app-source/) | Versioned Model A PHP source mirror (Phase 1A skeleton) |
| 56 | [product/I-SEO-REPORT-HUB-MVP-PHASE-1A-APP-SKELETON-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-MVP-PHASE-1A-APP-SKELETON-RESULT-v0.1.md) | Phase 1A app skeleton result |
| 57 | [reports/REPORT-iseo-report-hub-mvp-phase-1a-app-skeleton-config-baseline-01.md](reports/REPORT-iseo-report-hub-mvp-phase-1a-app-skeleton-config-baseline-01.md) | Phase 1A closeout report |
| 58 | [product/I-SEO-REPORT-HUB-MVP-PHASE-1B-RUNTIME-SYNC-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-MVP-PHASE-1B-RUNTIME-SYNC-RESULT-v0.1.md) | Phase 1B runtime sync result |
| 59 | [reports/REPORT-iseo-report-hub-mvp-phase-1b-source-to-runtime-sync-local-smoke-01.md](reports/REPORT-iseo-report-hub-mvp-phase-1b-source-to-runtime-sync-local-smoke-01.md) | Phase 1B closeout report |
| 60 | [product/I-SEO-REPORT-HUB-LOCAL-VHOST-HOSTS-MAPPING-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-VHOST-HOSTS-MAPPING-RESULT-v0.1.md) | Local vhost/hosts mapping result |
| 61 | [reports/REPORT-iseo-report-hub-local-vhost-hosts-mapping-01.md](reports/REPORT-iseo-report-hub-local-vhost-hosts-mapping-01.md) | Local vhost/hosts mapping closeout |
| 62 | [product/I-SEO-REPORT-HUB-LOCAL-HOSTS-RESMOKE-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-HOSTS-RESMOKE-RESULT-v0.1.md) | Local hosts re-smoke result |
| 63 | [reports/REPORT-iseo-report-hub-local-hosts-resmoke-01.md](reports/REPORT-iseo-report-hub-local-hosts-resmoke-01.md) | Local hosts re-smoke closeout |
| 64 | [product/I-SEO-REPORT-HUB-DB-CREATION-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-DB-CREATION-CHARTER-v0.1.md) | Local DB creation charter (planning) |
| 65 | [product/I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md) | Migration location/format/ledger/execution policy |
| 66 | [product/I-SEO-REPORT-HUB-INITIAL-SCHEMA-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-INITIAL-SCHEMA-PLAN-v0.1.md) | DB-01…DB-05 phasing + first migration recommendation |
| 67 | [product/I-SEO-REPORT-HUB-LOCAL-ENV-DB-SECRETS-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-ENV-DB-SECRETS-POLICY-v0.1.md) | Local `.env.local` / DB secrets policy |
| 68 | [reports/REPORT-iseo-report-hub-db-creation-schema-migration-charter-01.md](reports/REPORT-iseo-report-hub-db-creation-schema-migration-charter-01.md) | DB creation + schema migration charter closeout |
| 69 | [product/I-SEO-REPORT-HUB-DB-01-DB-02-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DB-01-DB-02-MIGRATION-APPLY-RESULT-v0.1.md) | DB-01/DB-02 migration apply result |
| 70 | [reports/REPORT-iseo-report-hub-db-creation-db01-db02-migration-files-apply-01.md](reports/REPORT-iseo-report-hub-db-creation-db01-db02-migration-files-apply-01.md) | DB creation + DB-01/DB-02 migration apply closeout |
| 71 | [product/I-SEO-REPORT-HUB-AUTH-PERSISTENCE-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-AUTH-PERSISTENCE-CHARTER-v0.1.md) | Auth persistence charter (DB login / session / roles / audit) |
| 72 | [product/I-SEO-REPORT-HUB-LOCAL-ADMIN-BOOTSTRAP-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-ADMIN-BOOTSTRAP-POLICY-v0.1.md) | Local admin bootstrap policy (secure CLI; no seed password) |
| 73 | [product/I-SEO-REPORT-HUB-DB-CONNECTION-HEALTH-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-DB-CONNECTION-HEALTH-POLICY-v0.1.md) | DB connection + `/health` safe status policy |
| 74 | [product/I-SEO-REPORT-HUB-AUTH-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-AUTH-IMPLEMENTATION-PLAN-v0.1.md) | Auth + bootstrap implementation plan (next wave) |
| 75 | [reports/REPORT-iseo-report-hub-auth-persistence-local-admin-bootstrap-charter-01.md](reports/REPORT-iseo-report-hub-auth-persistence-local-admin-bootstrap-charter-01.md) | Auth persistence + local admin bootstrap charter closeout |
| 76 | [product/I-SEO-REPORT-HUB-AUTH-PERSISTENCE-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-AUTH-PERSISTENCE-IMPLEMENTATION-RESULT-v0.1.md) | Auth persistence + local admin bootstrap implementation result |
| 77 | [reports/REPORT-iseo-report-hub-auth-persistence-local-admin-bootstrap-implementation-01.md](reports/REPORT-iseo-report-hub-auth-persistence-local-admin-bootstrap-implementation-01.md) | Auth persistence + local admin bootstrap implementation closeout |
| 78 | [product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-CHARTER-v0.1.md) | DB-03 reporting periods charter (planning) |
| 79 | [product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md) | DB-03 `reporting_periods` schema plan |
| 80 | [product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-PLAN-v0.1.md) | DB-03 migration apply/rollback/idempotency plan |
| 81 | [product/I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md](product/I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md) | Period status lifecycle for DB-03 |
| 82 | [product/I-SEO-REPORT-HUB-DB-03-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-03-IMPLEMENTATION-PLAN-v0.1.md) | DB-03 migration apply implementation plan |
| 83 | [reports/REPORT-iseo-report-hub-db03-reporting-periods-migration-charter-01.md](reports/REPORT-iseo-report-hub-db03-reporting-periods-migration-charter-01.md) | DB-03 reporting periods migration charter closeout |
| 84 | [product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-APPLY-RESULT-v0.1.md) | DB-03 reporting periods migration apply result |
| 85 | [reports/REPORT-iseo-report-hub-db03-reporting-periods-migration-apply-01.md](reports/REPORT-iseo-report-hub-db03-reporting-periods-migration-apply-01.md) | DB-03 reporting periods migration apply closeout |

---

## Related MARS systems

| System | Relationship to Report Hub |
|--------|--------------------------|
| **OPS** | Process authority for business operations workflows (WF-01 Monthly Reporting и др.); **не** CRM/ERP; может **consume** report readiness signals позже — **не** owner Report Hub |
| **ATLAS** | Business identity registry; orgs, people, projects; Report Hub **may consume** ATLAS identity when available — **не** product runtime |
| **Website Factory** | **Preferred MARS methodology + future workspace lane** для HTML/static UI demos, эскизов admin/report screens, block layout prototypes (gulp starter/build approach); см. [mars-website-factory/OPERATIONAL-INDEX.md](../mars-website-factory/OPERATIONAL-INDEX.md); **не** runtime owner, **не** production engine, **не** WordPress implementation owner, **не** deployed Report Hub |
| **Forge WordPress** | Future WordPress implementation subsystem (frontend package → WP package → WPilot handoff); **не** automatic implementation Report Hub |
| **WPilot** | Possible future bridge для WordPress admin operations; **не** architecture owner Report Hub |
| **MARS Localhost Infrastructure** | Local dev runtime on `X:\MARS-Localhost`; **не** production i-seo.su hosting |
| **MetaBOT / n8n** | External automation/AI; draft assistance, reminders, delivery hooks; **не** source of truth |
| **GitGuard / Survivability** | Repository survivability layer; checkpoint discipline для MARS docs — **не** Report Hub product |

**External runtime boundaries:**
- i-seo.su WordPress hosting — external production runtime
- Operator n8n server — external automation runtime
- Topvisor, Metrika, GSC и др. — external data sources (MVP: manual/link only)

---

## Current workflow

```
Web-GPT → Cursor → Human approval → REPORT
```

Human-supervised, documentation-first. Никакой autonomous orchestration.

---

## Filesystem safety

- Writes только на **X:** внутри approved MARS roots.
- **Preserve foreign WIP** — не трогать unrelated modified/untracked files.
- **No broad git operations** — no `git add .`, no commit/push без explicit operator charter.
- **No secrets** в documentation, reports, AI prompts.

---

## Next stages

1. **Project/Client Local Fixture Charter 01** — **recommended next** (clients/projects still 0/0; needed before period insert/CRUD smoke)
2. **Reporting Period CRUD Charter 01** — after safe local fixture
3. Optional parallel: **v0.5 demo corrections** from backlog (UX only; not product runtime)
4. **SEO specialist feedback** — still **deferred** until operator opens feedback charter
5. Work dictionary extraction/sanitization (из Nikita materials; **exclude** credential sheet)
6. MVP implementation phases 2–11 per implementation charter (Anton / i-SEO); DB-04+ after period shell is usable
7. Later: n8n/API/AI integration (events only; human approval gates)

**Historical note:** Static demos v0.1–v0.4, report content architecture, and Product Architecture Layer 02 are complete as documentation/demo baselines. Platform decision (PHP+MySQL) supersedes WordPress-as-runtime assumptions for forward work. Phase 0 scaffold + Phase 1A skeleton + Phase 1B source→runtime sync + Apache vhost + Windows `hosts` for `iseo-report-hub.test` are done (direct domain re-smoke PASS). Local DB `iseo_report_hub_dev` is **created**; first migration (DB-01 + minimal DB-02) is **applied**. Auth persistence + local admin bootstrap are **implemented** (DB-backed login; one local admin). DB-03 reporting periods migration is **applied** (`reporting_periods` present; 0 rows). `app-source/` remains the versioned SoT; runtime is Localhost deploy target.

---

## Boundaries (do not overclaim)

- **Auth persistence is implemented for local MVP** — login/logout/session/roles/audit; **not** production auth hardening
- **One local admin user exists** — no user management UI; no password reset
- **Runtime has synced auth code** at `X:\MARS-Localhost\sites\php\projects\iseo-report-hub` — **no** report CRUD yet
- **Local MySQL DB `iseo_report_hub_dev` exists** with core auth/org tables + **`reporting_periods`** (DB-03 applied; **0** rows; clients/projects still **0/0**)
- **Runtime `.env.local` exists** (outside Git); source keeps placeholders only
- **Versioned source of truth is `app-source/`** — runtime remains Localhost deploy target outside monorepo
- **Model A active** — sync direction **source → runtime**; runtime → source only by explicit import charter
- **Apache vhost + Windows `hosts` for `iseo-report-hub.test` are in place**; direct domain HTTP smoke **PASS**
- **No WordPress plugin exists** (and WP is not the chosen runtime)
- **No API integration exists**
- **No n8n workflow exists**
- **No client portal exists**
- **No autonomous publication**
- **Website Factory is not runtime owner** — methodology + prototype lane only
- **Static demo v0.4 is UX reference only** — not implementation
- **Historical WP architecture docs** remain in corpus as legacy planning — not current SoT
- **Domain `iseo-report-hub.test` resolves to 127.0.0.1** and serves auth-capable routes over HTTP
- **No separate runtime Git repository** — and none should be created without charter
