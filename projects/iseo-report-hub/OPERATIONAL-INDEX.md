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
| **Implementation** | **Phase 1B complete** + **local vhost/hosts mapping complete** + **DB `iseo_report_hub_dev` created** + **DB-01/DB-02 first migration applied** + **auth persistence + local admin bootstrap implemented** + **DB-03 reporting periods migration applied** + **local fixture apply complete** + **Reporting Period CRUD Implementation 01 complete** + **Weekly Checkpoints DB-04 Charter 01 complete** + **DB-04 migration apply complete** + **Weekly Checkpoints CRUD Charter 01 complete** + **Weekly Checkpoints CRUD Implementation 01 complete** + **Monthly Report Content DB-05 Charter 01 complete** + **DB-05 migration apply complete** — DB-backed login/logout; demo fixture + smoke period; internal reporting-period CRUD; `weekly_checkpoints` table + W1–W4; period-scoped weekly checkpoint CRUD; `monthly_report_contents` table + 1 local demo row for `2026-07`; **no** monthly content CRUD/editor / client portal |
| **Source model** | **Model A active** — `projects/iseo-report-hub/app-source/` is versioned SoT; sync direction **source → runtime**; runtime → source only by explicit import charter |

---

## Current status

| Field | Value |
|-------|-------|
| **Status** | planned / product architecture + Phase 0 scaffold + Model A `app-source/` + Phase 1A/1B + local DB + **auth persistence implemented** + **DB-03 migration applied** + **local fixture apply complete** + **Reporting Period CRUD Implementation 01 complete** + **Weekly Checkpoints DB-04 Charter 01 complete** + **DB-04 migration apply complete** + **Weekly Checkpoints CRUD Charter 01 complete** + **Weekly Checkpoints CRUD Implementation 01 complete** + **Monthly Report Content DB-05 Charter 01 complete** + **DB-05 migration apply complete** |
| **Lane** | Lane B — product formation and architecture |
| **Active stage** | **Monthly Report Content DB-05 Migration Apply 01 complete** — next recommended: **Monthly Report Content CRUD Charter 01** |
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
| **Unique/FK row smoke** | was structural-only at apply time; **superseded** by Local Fixture Apply 01 (non-structural) |
| **Result doc** | [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-APPLY-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-db03-reporting-periods-migration-apply-01.md](reports/REPORT-iseo-report-hub-db03-reporting-periods-migration-apply-01.md) |
| **App / auth code** | **unchanged** |
| **Next recommended stage** | **Reporting Period CRUD Charter 01** (after Local Fixture Apply 01) |

---

## Project/Client Local Fixture Charter 01 (2026-07-25)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — documentation / policy only |
| **Reason** | DB-03 FK/unique smoke for `reporting_periods` requires a demo project; clients/projects/sites remain **0/0/0** |
| **Fixture rows created** | **No** — charter only; no DB mutation |
| **Charter** | [I-SEO-REPORT-HUB-LOCAL-FIXTURE-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-CHARTER-v0.1.md) |
| **Data plan** | [I-SEO-REPORT-HUB-LOCAL-FIXTURE-DATA-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-DATA-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-LOCAL-FIXTURE-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-VALIDATION-PLAN-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-LOCAL-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-project-client-local-fixture-charter-01.md](reports/REPORT-iseo-report-hub-project-client-local-fixture-charter-01.md) |
| **Preferred next tool** | `tools/create-local-fixture.php` (local-only; idempotent; not a schema seed migration) |
| **Planned demo set** | `Demo Client` / `Demo SEO Project` / `demo.example.test` / period `2026-07` — all marked `LOCAL_FIXTURE_ONLY` |
| **App-source / runtime / DB** | **Unchanged** in this wave |
| **Next apply candidate** | **Project/Client Local Fixture Apply 01** — **completed** (see section below) |

---

## Project/Client Local Fixture Apply 01 (2026-07-25)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — local-only fixture tool + rows applied |
| **Tool (source)** | `app-source/tools/create-local-fixture.php` |
| **Tool (runtime)** | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\tools\create-local-fixture.php` |
| **Demo fixture counts** | clients/projects/sites/reporting_periods = **1/1/1/1** |
| **IDs (local)** | client **1**, project **1**, site **1**, reporting_period **1** |
| **Markers** | `LOCAL_FIXTURE_ONLY` on client notes / site label / period summary; slugs `demo-client` / `demo-seo-project`; site `https://demo.example.test`; period `2026-07` |
| **Idempotency** | second run `already-present` exit 0 |
| **FK/unique validation** | joins **ok**; duplicate `(project_id, period_key)` rejected + rolled back |
| **Audit** | `local_fixture.created` |
| **Result doc** | [I-SEO-REPORT-HUB-LOCAL-FIXTURE-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-APPLY-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-project-client-local-fixture-apply-01.md](reports/REPORT-iseo-report-hub-project-client-local-fixture-apply-01.md) |
| **Schema / auth / app UI** | **unchanged** |
| **Next recommended stage** | **Reporting Period CRUD Charter 01** — **completed** (see section below) |

---

## Reporting Period CRUD Charter 01 (2026-07-25)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — documentation / policy only |
| **Baseline dependency** | Local Fixture Apply 01 — demo counts **1/1/1/1**; period `2026-07`; auth + DB-03 present |
| **Charter** | [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-CHARTER-v0.1.md) |
| **Design** | [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-DESIGN-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-reporting-period-crud-charter-01.md](reports/REPORT-iseo-report-hub-reporting-period-crud-charter-01.md) |
| **CRUD UI / app-source** | **Not implemented** in this wave |
| **Runtime / DB** | **Unchanged** — no code sync; no DB mutation |
| **Planned MVP surface** | list/detail/create/edit + archive-by-status; auth + CSRF; no DELETE |
| **Out of scope (confirmed)** | weekly checkpoint editor; monthly report content; client portal; real client data; production |
| **Next implementation candidate** | **I-SEO Report Hub — Reporting Period CRUD Implementation 01** |

---

## Reporting Period CRUD Implementation 01 (2026-07-25)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — source CRUD + runtime sync + smoke |
| **Routes** | `GET/POST /reporting-periods`, `GET /reporting-periods/create`, `GET/POST /reporting-periods/{id}`, `GET /reporting-periods/{id}/edit` |
| **Auth** | Required (internal roles); CSRF on POST; no DELETE |
| **Smoke** | **PASS** — create `2026-08` (id **3**), duplicate refuse, edit→active, archive; fixture `2026-07` intact |
| **DB counts after** | clients/projects/sites/reporting_periods = **1/1/1/2** |
| **Result doc** | [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-reporting-period-crud-implementation-01.md](reports/REPORT-iseo-report-hub-reporting-period-crud-implementation-01.md) |
| **SAFE SIMPLIFICATION** | `account_client_manager` read-only (title/summary-only deferred) |
| **Next recommended stage** | **Weekly Checkpoints DB-04 Charter 01** — **completed** (see section below) |

---

## Weekly Checkpoints DB-04 Charter 01 (2026-07-26)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — documentation / policy only |
| **Baseline dependency** | Reporting Period CRUD Implementation 01 — commits `392258fc` + hash-record `f1d8a17e`; DB counts clients/projects/sites/reporting_periods **1/1/1/2**; migrations **2**; tables **10** |
| **Charter** | [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-CHARTER-v0.1.md) |
| **Schema plan** | [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md) |
| **Lifecycle** | [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md](product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-IMPLEMENTATION-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-db04-weekly-checkpoints-charter-01.md](reports/REPORT-iseo-report-hub-db04-weekly-checkpoints-charter-01.md) |
| **Planned table** | `weekly_checkpoints` (child of `reporting_periods`) |
| **Planned SQL filename** | `2026_07_26_000003_create_weekly_checkpoints_table.sql` — **not** created in this wave |
| **App-source / runtime / DB** | **Unchanged** — no SQL; no migration; no code sync; no DB mutation |
| **No seed in migration** | Confirmed — demo W1/W2/W3 smoke deferred to apply wave |
| **Out of scope (confirmed)** | weekly CRUD UI; monthly editor; report blocks; real client data; production |
| **Next apply candidate** | **I-SEO Report Hub — Weekly Checkpoints DB-04 Migration Apply 01** — **completed** (see section below) |

---

## Weekly Checkpoints DB-04 Migration Apply 01 (2026-07-26)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — migration applied + local W1–W3 smoke |
| **Baseline dependency** | DB-04 Charter 01; Reporting Period CRUD; fixture period `2026-07`; migrations **2** / tables **10** before apply |
| **Migration file** | `2026_07_26_000003_create_weekly_checkpoints_table.sql` |
| **Checksum (SHA-256)** | `8ab9c0e84a262ab9c8662cd502ab18943810dc6a034d2cd25a89935e2ddaacd3` |
| **Batch** | **3** |
| **DB counts after** | migrations **3**; tables **11**; weekly_checkpoints **3**; reporting_periods **2** (unchanged) |
| **Demo rows** | W1 `completed`, W2 `reviewed`, W3 `draft` — all `LOCAL_FIXTURE_ONLY` under period `2026-07` |
| **Validation** | FK / unique / CHECK violations expected+rolled back; idempotent second apply; HTTP regression PASS |
| **Result doc** | [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-MIGRATION-APPLY-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-db04-weekly-checkpoints-migration-apply-01.md](reports/REPORT-iseo-report-hub-db04-weekly-checkpoints-migration-apply-01.md) |
| **Out of scope (confirmed)** | weekly CRUD UI; monthly editor; report blocks; app/auth/health edits; production |
| **Next recommended stage** | **Weekly Checkpoints CRUD Charter 01** — **completed** (see section below) |

---

## Weekly Checkpoints CRUD Charter 01 (2026-07-26)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — documentation / policy only |
| **Baseline dependency** | DB-04 Migration Apply 01 — commits `f7a26aa3` + hash-record `228965d7` + clarify `e18c537d`; migrations **3**; tables **11**; weekly_checkpoints **3** (W1–W3); reporting_periods **2** |
| **Charter** | [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-CHARTER-v0.1.md) |
| **Design** | [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-DESIGN-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-weekly-checkpoints-crud-charter-01.md](reports/REPORT-iseo-report-hub-weekly-checkpoints-crud-charter-01.md) |
| **CRUD UI / app-source** | **Not implemented** in this wave |
| **Runtime / DB** | **Unchanged** — no code sync; no DB mutation; no SQL/migration edits |
| **Planned MVP surface** | nested list/create under period; flat detail/edit; archive/skip-by-status; auth + CSRF; no DELETE |
| **Out of scope (confirmed)** | monthly editor; report blocks; Topvisor; client portal; real client data; production |
| **Next implementation candidate** | **I-SEO Report Hub — Weekly Checkpoints CRUD Implementation 01** — **completed** (see section below) |

---

## Weekly Checkpoints CRUD Implementation 01 (2026-07-26)

| Field | Value |
|-------|--------|
| **Status** | **Complete** — source CRUD + allowlist runtime sync + smoke + docs + scoped commits |
| **Baseline dependency** | Weekly Checkpoints CRUD Charter 01; DB-04 apply; Reporting Period CRUD; auth baseline |
| **Result doc** | [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-weekly-checkpoints-crud-implementation-01.md](reports/REPORT-iseo-report-hub-weekly-checkpoints-crud-implementation-01.md) |
| **Routes** | nested list/create/store under period; flat detail/edit/update; **no DELETE** |
| **Parent period integration** | period show embeds weekly table/count + links |
| **Nav decision** | no top-level weekly header link — period-scoped only |
| **Smoke** | **PASS** — create W4 id **7** `2026-07-W4` → edit → `skipped`; duplicate refused; W1–W3 unchanged |
| **DB after** | weekly_checkpoints **4**; reporting_periods **2**; migrations **3**; tables **11** |
| **Auth / CSRF** | required; CSRF on POST; session-injection smoke (password env unset) |
| **Out of scope (confirmed)** | monthly editor; report blocks; Topvisor; client portal; schema edits; DELETE |
| **Next recommended stage** | **Monthly Report Content DB-05 Charter 01** — **completed** (see section below) |

---

## Monthly Report Content DB-05 Charter 01 (2026-07-26)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — documentation / policy only |
| **Baseline dependency** | Weekly Checkpoints CRUD Implementation 01 — commits `911db07d` + hash-record `64c42cbe` + clarify `6f968ed2` / `865cd4b5`; migrations **3**; tables **11**; weekly_checkpoints **4**; reporting_periods **2** |
| **Charter** | [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-CHARTER-v0.1.md) |
| **Schema plan** | [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md) |
| **Lifecycle** | [I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-IMPLEMENTATION-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-db05-monthly-report-content-charter-01.md](reports/REPORT-iseo-report-hub-db05-monthly-report-content-charter-01.md) |
| **Planned table** | `monthly_report_contents` (at most one per `reporting_periods`) |
| **Planned SQL filename** | `2026_07_26_000004_create_monthly_report_contents_table.sql` — **created/applied in Migration Apply 01** (see section below) |
| **App-source / runtime / DB** | **Unchanged in charter wave** — apply wave created/synced/applied migration |
| **No seed in migration** | Confirmed — demo monthly smoke row deferred to apply wave |
| **Out of scope (confirmed)** | monthly CRUD UI; report blocks; PDF/export; client portal; Topvisor; real client data; production |
| **Next apply candidate** | **I-SEO Report Hub — Monthly Report Content DB-05 Migration Apply 01** — **completed** (see section below) |

---

## Monthly Report Content DB-05 Migration Apply 01 (2026-07-26)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — migration SQL + runtime sync + apply + demo row + validation + docs + scoped commit |
| **Baseline dependency** | DB-05 Charter 01 (`c2dae889` + hash-record `8ed5cea3` + clarify `ab51fbd0`); migrations **3**; tables **11**; weekly_checkpoints **4**; reporting_periods **2** |
| **Result doc** | [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-MIGRATION-APPLY-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-db05-monthly-report-content-migration-apply-01.md](reports/REPORT-iseo-report-hub-db05-monthly-report-content-migration-apply-01.md) |
| **Migration filename** | `2026_07_26_000004_create_monthly_report_contents_table.sql` |
| **Checksum (SHA-256)** | `91f367cdf73d1a4b1fcfa3175f190c0470cda86e5cd5706749e2d566c82430b8` |
| **Batch** | **4** |
| **DB after** | migrations **4**; tables **12**; monthly_report_contents **1**; reporting_periods **2** unchanged; weekly_checkpoints **4** unchanged |
| **Demo smoke row** | id **1**; period `2026-07`; status `draft`; title/text `LOCAL_FIXTURE_ONLY`; source ids `[1,2,3,7]` |
| **Validation** | **PASS** — FK / unique / CHECK / JSON + idempotent re-apply + app regression GET |
| **Out of scope (confirmed)** | monthly CRUD UI/code; report blocks; Topvisor; client portal; period/weekly row mutation; production |
| **Next recommended stage** | **Monthly Report Content CRUD Charter 01** |

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
| 86 | [product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-CHARTER-v0.1.md) | Local fixture charter (planning; no rows) |
| 87 | [product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-DATA-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-DATA-PLAN-v0.1.md) | Demo client/project/site/period field plan |
| 88 | [product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-VALIDATION-PLAN-v0.1.md) | FK/unique/health/auth validation gates |
| 89 | [product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md) | Local fixture apply implementation plan |
| 90 | [reports/REPORT-iseo-report-hub-project-client-local-fixture-charter-01.md](reports/REPORT-iseo-report-hub-project-client-local-fixture-charter-01.md) | Local fixture charter closeout |
| 91 | [product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-APPLY-RESULT-v0.1.md) | Local fixture apply result |
| 92 | [reports/REPORT-iseo-report-hub-project-client-local-fixture-apply-01.md](reports/REPORT-iseo-report-hub-project-client-local-fixture-apply-01.md) | Local fixture apply closeout |
| 93 | [product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-CHARTER-v0.1.md) | Reporting Period CRUD charter (planning) |
| 94 | [product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-DESIGN-v0.1.md) | Reporting Period CRUD design (routes/forms/validation) |
| 95 | [product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-PLAN-v0.1.md) | Reporting Period CRUD implementation plan (next wave) |
| 96 | [product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-VALIDATION-PLAN-v0.1.md) | Reporting Period CRUD validation/smoke plan |
| 97 | [reports/REPORT-iseo-report-hub-reporting-period-crud-charter-01.md](reports/REPORT-iseo-report-hub-reporting-period-crud-charter-01.md) | Reporting Period CRUD charter closeout |
| 98 | [product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-RESULT-v0.1.md) | Reporting Period CRUD implementation result |
| 99 | [reports/REPORT-iseo-report-hub-reporting-period-crud-implementation-01.md](reports/REPORT-iseo-report-hub-reporting-period-crud-implementation-01.md) | Reporting Period CRUD implementation closeout |
| 100 | [product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-CHARTER-v0.1.md) | DB-04 weekly checkpoints charter (planning) |
| 101 | [product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md) | DB-04 `weekly_checkpoints` schema plan |
| 102 | [product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md](product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md) | Weekly checkpoint status lifecycle for DB-04 |
| 103 | [product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-IMPLEMENTATION-PLAN-v0.1.md) | DB-04 migration apply implementation plan |
| 104 | [product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-VALIDATION-PLAN-v0.1.md) | DB-04 validation/smoke plan |
| 105 | [reports/REPORT-iseo-report-hub-db04-weekly-checkpoints-charter-01.md](reports/REPORT-iseo-report-hub-db04-weekly-checkpoints-charter-01.md) | DB-04 weekly checkpoints charter closeout |
| 106 | [product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-MIGRATION-APPLY-RESULT-v0.1.md) | DB-04 weekly checkpoints migration apply result |
| 107 | [reports/REPORT-iseo-report-hub-db04-weekly-checkpoints-migration-apply-01.md](reports/REPORT-iseo-report-hub-db04-weekly-checkpoints-migration-apply-01.md) | DB-04 weekly checkpoints migration apply closeout |
| 108 | [product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-CHARTER-v0.1.md) | Weekly Checkpoints CRUD charter (planning) |
| 109 | [product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-DESIGN-v0.1.md) | Weekly Checkpoints CRUD design (routes/forms/validation) |
| 110 | [product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-PLAN-v0.1.md) | Weekly Checkpoints CRUD implementation plan (next wave) |
| 111 | [product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-VALIDATION-PLAN-v0.1.md) | Weekly Checkpoints CRUD validation/smoke plan |
| 112 | [reports/REPORT-iseo-report-hub-weekly-checkpoints-crud-charter-01.md](reports/REPORT-iseo-report-hub-weekly-checkpoints-crud-charter-01.md) | Weekly Checkpoints CRUD charter closeout |
| 113 | [product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-RESULT-v0.1.md) | Weekly Checkpoints CRUD implementation result |
| 114 | [reports/REPORT-iseo-report-hub-weekly-checkpoints-crud-implementation-01.md](reports/REPORT-iseo-report-hub-weekly-checkpoints-crud-implementation-01.md) | Weekly Checkpoints CRUD implementation closeout |
| 115 | [product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-CHARTER-v0.1.md) | DB-05 monthly report content charter (planning) |
| 116 | [product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md) | DB-05 `monthly_report_contents` schema plan |
| 117 | [product/I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md) | Monthly report content status lifecycle for DB-05 |
| 118 | [product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-IMPLEMENTATION-PLAN-v0.1.md) | DB-05 migration apply implementation plan |
| 119 | [product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-VALIDATION-PLAN-v0.1.md) | DB-05 validation/smoke plan |
| 120 | [reports/REPORT-iseo-report-hub-db05-monthly-report-content-charter-01.md](reports/REPORT-iseo-report-hub-db05-monthly-report-content-charter-01.md) | DB-05 monthly report content charter closeout |
| 121 | [product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-MIGRATION-APPLY-RESULT-v0.1.md) | DB-05 migration apply result |
| 122 | [reports/REPORT-iseo-report-hub-db05-monthly-report-content-migration-apply-01.md](reports/REPORT-iseo-report-hub-db05-monthly-report-content-migration-apply-01.md) | DB-05 migration apply closeout |

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

1. **Monthly Report Content CRUD Charter 01** — **recommended next** (DB-05 table + demo monthly row exist)
2. Optional: **Weekly Checkpoints CRUD Hardening 01** if multi-role HTTP smoke is needed
3. Optional: **Reporting Period CRUD Hardening 01** if account-manager edit / multi-role smoke is needed
4. Optional parallel: **v0.5 demo corrections** from backlog (UX only; not product runtime)
5. **SEO specialist feedback** — still **deferred** until operator opens feedback charter
6. Work dictionary extraction/sanitization (из Nikita materials; **exclude** credential sheet)
7. MVP implementation phases 2–11 per implementation charter (Anton / i-SEO)
8. Later: n8n/API/AI integration (events only; human approval gates)

**Historical note:** Static demos v0.1–v0.4, report content architecture, and Product Architecture Layer 02 are complete as documentation/demo baselines. Platform decision (PHP+MySQL) supersedes WordPress-as-runtime assumptions for forward work. Phase 0 scaffold + Phase 1A skeleton + Phase 1B source→runtime sync + Apache vhost + Windows `hosts` for `iseo-report-hub.test` are done (direct domain re-smoke PASS). Local DB `iseo_report_hub_dev` is **created**; first migration (DB-01 + minimal DB-02) is **applied**. Auth persistence + local admin bootstrap are **implemented** (DB-backed login; one local admin). DB-03 reporting periods migration is **applied**. Local fixture apply is **complete** (demo client/project/site + period `2026-07`). Reporting Period CRUD **implementation** is complete (internal list/detail/create/edit/archive-by-status; smoke period `2026-08` archived; counts clients/projects/sites/reporting_periods **1/1/1/2**). Weekly Checkpoints DB-04 **migration apply** is complete (`weekly_checkpoints` + local W1–W3 smoke). Weekly Checkpoints CRUD **implementation** is complete (period-scoped list/detail/create/edit/skip-or-archive; W4 smoke id **7** skipped; weekly_checkpoints **4**). Monthly Report Content DB-05 **migration apply** is complete (`monthly_report_contents` + 1 local demo row; migrations **4** / tables **12**). `app-source/` remains the versioned SoT; runtime is Localhost deploy target.

---

## Boundaries (do not overclaim)

- **Auth persistence is implemented for local MVP** — login/logout/session/roles/audit; **not** production auth hardening
- **One local admin user exists** — no user management UI; no password reset
- **Reporting Period CRUD MVP is implemented** — internal list/detail/create/edit/archive-by-status; CSRF; no DELETE; demo + smoke periods only
- **Runtime has synced auth + CRUD code** at `X:\MARS-Localhost\sites\php\projects\iseo-report-hub`
- **Local MySQL DB `iseo_report_hub_dev` exists** with core auth/org tables + **`reporting_periods`** (DB-03) + **`weekly_checkpoints`** (DB-04) + **`monthly_report_contents`** (DB-05 applied)
- **Local fixture + CRUD smoke** — demo client/project/site **1/1/1**; reporting_periods **2** (`2026-07` fixture + `2026-08` smoke archived); weekly_checkpoints **4** (W1–W3 fixture + W4 smoke `skipped`, `LOCAL_FIXTURE_ONLY`); monthly_report_contents **1** (demo for `2026-07`, `LOCAL_FIXTURE_ONLY`)
- **Runtime `.env.local` exists** (outside Git); source keeps placeholders only
- **Versioned source of truth is `app-source/`** — runtime remains Localhost deploy target outside monorepo
- **Model A active** — sync direction **source → runtime**; runtime → source only by explicit import charter
- **Apache vhost + Windows `hosts` for `iseo-report-hub.test` are in place**; direct domain HTTP smoke **PASS**
- **No WordPress plugin exists** (and WP is not the chosen runtime)
- **No API integration exists**
- **No n8n workflow exists**
- **No client portal exists**
- **Weekly Checkpoints DB-04 migration is applied** — table + local W1–W3 smoke exist
- **Weekly Checkpoints CRUD MVP is implemented** — period-scoped list/detail/create/edit/skip-or-archive-by-status; CSRF; no DELETE; parent period show integration
- **Monthly Report Content DB-05 migration is applied** — table + 1 local demo row; migrations **4**; tables **12**; **no** monthly CRUD yet
- **No monthly content editor**
- **No autonomous publication**
- **Website Factory is not runtime owner** — methodology + prototype lane only
- **Static demo v0.4 is UX reference only** — not implementation
- **Historical WP architecture docs** remain in corpus as legacy planning — not current SoT
- **Domain `iseo-report-hub.test` resolves to 127.0.0.1** and serves auth-capable routes over HTTP
- **No separate runtime Git repository** — and none should be created without charter
