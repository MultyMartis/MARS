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
| **Implementation** | **Phase 1B complete** + **local vhost/hosts mapping complete** + **DB `iseo_report_hub_dev` created** + **DB-01/DB-02 first migration applied** + **auth persistence + local admin bootstrap implemented** + **DB-03 reporting periods migration applied** + **local fixture apply complete** + **Reporting Period CRUD Implementation 01 complete** + **Weekly Checkpoints DB-04 Charter 01 complete** + **DB-04 migration apply complete** + **Weekly Checkpoints CRUD Charter 01 complete** + **Weekly Checkpoints CRUD Implementation 01 complete** + **Monthly Report Content DB-05 Charter 01 complete** + **DB-05 migration apply complete** + **Monthly Report Content CRUD Charter 01 complete** + **Monthly Report Content CRUD Implementation 01 complete** + **Report Blocks DB-06 Charter 01 complete** + **DB-06 migration apply complete** + **Report Blocks CRUD Charter 01 complete** + **Report Blocks CRUD Implementation 01 complete** + **Report Preview / Render Charter 01 complete** + **Report Preview / Render Implementation 01 complete** + **Report Finalization Charter 01 complete** + **Report Finalization Implementation 01 complete** + **Report Snapshot Charter 01 complete** + **Report Snapshot DB-07 Migration Apply 01 complete** + **Report Snapshot Implementation 01 complete** + **Report Export / PDF Charter 01 complete** + **Report Export DB-08 Migration Apply 01 complete** — DB-backed login/logout; demo fixture + smoke period; internal reporting-period CRUD; `weekly_checkpoints` table + W1–W4; period-scoped weekly checkpoint CRUD; `monthly_report_contents` table + period-scoped monthly report content CRUD (demo id **1**, status **finalized** after finalization smoke); `report_blocks` table + monthly-scoped report block CRUD (6 local blocks under monthly id **1**); internal preview/print (`blocks_primary`); finalization workflow + readiness + locks; `report_snapshots` table (DB-07) + active snapshot v1 (`monthly-1-v1`); export/PDF policy designed; `report_exports` table (DB-08) **0** rows; **no** drag/drop / PDF/export runtime / client portal |
| **Source model** | **Model A active** — `projects/iseo-report-hub/app-source/` is versioned SoT; sync direction **source → runtime**; runtime → source only by explicit import charter |

---

## Current status

| Field | Value |
|-------|-------|
| **Status** | planned / product architecture + Phase 0 scaffold + Model A `app-source/` + Phase 1A/1B + local DB + **auth persistence implemented** + **DB-03 migration applied** + **local fixture apply complete** + **Reporting Period CRUD Implementation 01 complete** + **Weekly Checkpoints DB-04 Charter 01 complete** + **DB-04 migration apply complete** + **Weekly Checkpoints CRUD Charter 01 complete** + **Weekly Checkpoints CRUD Implementation 01 complete** + **Monthly Report Content DB-05 Charter 01 complete** + **DB-05 migration apply complete** + **Monthly Report Content CRUD Charter 01 complete** + **Monthly Report Content CRUD Implementation 01 complete** + **Report Blocks DB-06 Charter 01 complete** + **DB-06 migration apply complete** + **Report Blocks CRUD Charter 01 complete** + **Report Blocks CRUD Implementation 01 complete** + **Report Preview / Render Charter 01 complete** + **Report Preview / Render Implementation 01 complete** + **Report Finalization Charter 01 complete** + **Report Finalization Implementation 01 complete** + **Report Snapshot Charter 01 complete** + **Report Snapshot DB-07 Migration Apply 01 complete** + **Report Snapshot Implementation 01 complete** + **Report Export / PDF Charter 01 complete** + **Report Export DB-08 Migration Apply 01 complete** |
| **Lane** | Lane B — product formation and architecture |
| **Active stage** | **Report Export Template Metadata UI Implementation 01 complete** — DB-09 metadata read/display + future styled write support; DB/artifacts unchanged; next recommended: **Report Delivery / Public Share Charter 01** |
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
| **Next recommended stage** | **Monthly Report Content CRUD Charter 01** — **completed** (see section below) |

---

## Monthly Report Content CRUD Charter 01 (2026-07-26)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — documentation / policy only |
| **Baseline dependency** | DB-05 Migration Apply 01 — commits `aac9c18e` + hash-record `32674ea9`; migrations **4**; tables **12**; monthly_report_contents **1**; weekly_checkpoints **4**; reporting_periods **2** |
| **Charter** | [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-CHARTER-v0.1.md) |
| **Design** | [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-DESIGN-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-monthly-report-content-crud-charter-01.md](reports/REPORT-iseo-report-hub-monthly-report-content-crud-charter-01.md) |
| **CRUD UI / app-source** | **Not implemented** in this wave |
| **Runtime / DB** | **Unchanged** — no code sync; no DB mutation; no SQL/migration edits |
| **Planned MVP surface** | period-scoped create-if-missing / detail; flat detail/edit; status lifecycle via edit form; auth + CSRF; source weekly checkpoint refs; no DELETE |
| **Out of scope (confirmed)** | report blocks; PDF/export; Topvisor; client portal; real client data; production |
| **Next implementation candidate** | **I-SEO Report Hub — Monthly Report Content CRUD Implementation 01** — **completed** (see section below) |

---

## Monthly Report Content CRUD Implementation 01 (2026-07-26)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — source CRUD + allowlist runtime sync + smoke + docs + scoped commits |
| **Baseline dependency** | Monthly Report Content CRUD Charter 01; DB-05 apply; Weekly Checkpoints CRUD; Reporting Period CRUD; auth baseline |
| **Result doc** | [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-monthly-report-content-crud-implementation-01.md](reports/REPORT-iseo-report-hub-monthly-report-content-crud-implementation-01.md) |
| **Routes** | `GET/POST /reporting-periods/{id}/monthly-report` (+ `/create`); `GET/POST /monthly-reports/{id}` (+ `/edit`); no DELETE; no top-level index |
| **Parent period integration** | Reporting period detail shows monthly report section (view/edit or create) |
| **Source weekly checkpoints** | Checkbox selection + same-period validation; detail links to weekly checkpoint pages |
| **Smoke** | PASS — lint; unauth→login; detail/edit; update id1 → `in_progress`; duplicate create guard; invalid source IDs; period/weekly/dashboard/health regression |
| **DB row counts (after)** | migrations **4**; tables **12**; reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1** (id **1** `in_progress`, `LOCAL_FIXTURE_ONLY`) |
| **Out of scope (confirmed)** | report blocks; PDF/export; Topvisor; client portal; schema edits; DELETE |
| **Next recommended stage** | **Report Blocks DB-06 Charter 01** — **completed** (see section below) |

---

## Report Blocks DB-06 Charter 01 (2026-07-26)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — documentation / policy only |
| **Baseline dependency** | Monthly Report Content CRUD Implementation 01 (`65f64124` / hash-record `17553a55` / clarify `eb00b3f4`); DB-05 apply; Weekly Checkpoints CRUD; Reporting Period CRUD; auth baseline |
| **Charter** | [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-CHARTER-v0.1.md) |
| **Schema plan** | [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md) |
| **Lifecycle** | [I-SEO-REPORT-HUB-REPORT-BLOCKS-LIFECYCLE-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-BLOCKS-LIFECYCLE-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-IMPLEMENTATION-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-db06-report-blocks-charter-01.md](reports/REPORT-iseo-report-hub-db06-report-blocks-charter-01.md) |
| **Planned table** | `report_blocks` (ordered blocks under `monthly_report_contents`) — **created in Migration Apply 01** (see section below) |
| **Planned migration** | `2026_07_26_000005_create_report_blocks_table.sql` — **created/applied in Migration Apply 01** (see section below) |
| **DB/code/runtime this wave** | **None** — no SQL, no app-source, no runtime sync, no DB mutation |
| **Current DB (at charter time)** | migrations **4**; tables **12**; monthly_report_contents **1**; `report_blocks` **absent** |
| **Next implementation candidate** | **I-SEO Report Hub — Report Blocks DB-06 Migration Apply 01** — **completed** (see section below) |

---

## Report Blocks DB-06 Migration Apply 01 (2026-07-26)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — migration applied + local fixture blocks; **no** CRUD/UI/code |
| **Result doc** | [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-MIGRATION-APPLY-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-db06-report-blocks-migration-apply-01.md](reports/REPORT-iseo-report-hub-db06-report-blocks-migration-apply-01.md) |
| **Migration filename** | `2026_07_26_000005_create_report_blocks_table.sql` |
| **Checksum (SHA-256)** | `951bc88826a6155a624377b43851f1d6f7eadb8fdf7d229cb5bffe952eee3236` |
| **Batch** | **5** |
| **Table** | `report_blocks` — InnoDB/utf8mb4; unique parent+`block_key`; non-unique parent+`sort_order`; status + block_type CHECK; JSON fields; parent FK RESTRICT |
| **DB counts** | migrations **4 → 5**; tables **12 → 13**; reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1**; report_blocks **5** |
| **Fixture blocks** | 5 rows under monthly report content id **1** / period `2026-07`; keys `executive_summary`…`next_month_plan`; status `draft`; `LOCAL_FIXTURE_ONLY`; sources `[1,2,3,7]` |
| **Validation** | FK/unique/CHECK/JSON rolled-back probes **pass expected**; parent linkage **pass**; idempotent second apply; app GET regression **pass** |
| **CRUD/UI/code this wave** | **None** |
| **Next recommended stage** | **Report Blocks CRUD Charter 01** — **completed** (see section below) |

---

## Report Blocks CRUD Charter 01 (2026-07-26)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — documentation / policy only |
| **Baseline dependency** | DB-06 Migration Apply 01 (`1b71a021` / hash-record `7393d7c1` / clarify `86338d66`); Monthly Report Content CRUD Implementation 01; Weekly Checkpoints CRUD; Reporting Period CRUD; auth baseline |
| **Charter** | [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-CHARTER-v0.1.md) |
| **Design** | [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-DESIGN-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-blocks-crud-charter-01.md](reports/REPORT-iseo-report-hub-report-blocks-crud-charter-01.md) |
| **DB/code/runtime this wave** | **None** — no app-source, no runtime sync, no DB mutation, no SQL/migration edits |
| **Current DB (read-only this wave)** | migrations **5**; tables **13**; report_blocks **5**; monthly_report_contents **1** (`in_progress`); weekly_checkpoints **4**; reporting_periods **2** |
| **Designed surface** | Monthly-scoped block list/create; flat detail/edit; manual `sort_order`; status lifecycle; source weekly refs; auth+CSRF; **no** DELETE; **no** drag/drop |
| **Next implementation candidate** | **I-SEO Report Hub — Report Blocks CRUD Implementation 01** — **completed** (see section below) |

---

## Report Blocks CRUD Implementation 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — source CRUD + runtime allowlist sync + smoke + docs |
| **Baseline dependency** | Report Blocks CRUD Charter 01 (`a8f3f6df` / hash-record `7b20b8b8` / clarify `38001d61`); DB-06 Migration Apply 01; Monthly Report Content CRUD Implementation 01 |
| **Routes** | `GET/POST /monthly-reports/{id}/blocks` (+ `/create`); `GET/POST /report-blocks/{id}` (+ `/edit`); no DELETE; no top-level index |
| **DB final counts** | reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1**; report_blocks **6** (fixture 5 + smoke `risks_and_blockers`) |
| **Smoke** | PASS — list/detail/edit/update/create; duplicate + invalid JSON/source guards; manual sort_order; monthly show blocks section; regression; auth session injection |
| **Restrictions** | no schema edits; no DELETE; no drag/drop; no monthly/weekly/period mutations; no secrets; no push |
| **Result** | [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-blocks-crud-implementation-01.md](reports/REPORT-iseo-report-hub-report-blocks-crud-implementation-01.md) |
| **Next recommended stage** | **Report Preview / Render Charter 01** — **completed** (see section below) |

---

## Report Preview / Render Charter 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — documentation / policy only |
| **Baseline dependency** | Report Blocks CRUD Implementation 01 (`135da213…` / hash-record `5c65ac88…`); Monthly Report Content CRUD; DB-05 + DB-06 tables |
| **Designed surface** | Internal authenticated monthly preview; blocks primary (`sort_order`/`id`); archived excluded; DB-05 flat fallback/diagnostics; source weekly links; optional print-friendly route; **no** public/PDF |
| **Code / runtime / DB this wave** | **None** — no app-source; no runtime sync; no DB mutation |
| **Next implementation candidate** | **I-SEO Report Hub — Report Preview / Render Implementation 01** — **completed** (see section below) |
| **Charter** | [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-CHARTER-v0.1.md) |
| **Design** | [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-DESIGN-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-preview-render-charter-01.md](reports/REPORT-iseo-report-hub-report-preview-render-charter-01.md) |

---

## Report Preview / Render Implementation 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — source preview/render + runtime allowlist sync + smoke + docs |
| **Baseline dependency** | Report Preview / Render Charter 01 (`f9604d4b…` / hash-record `34e7d9d0…` / clarify `65ab3a97…`); Report Blocks CRUD Implementation 01 |
| **Routes** | `GET /monthly-reports/{id}/preview`; `GET /monthly-reports/{id}/preview/print`; **no** public/PDF/export/share |
| **Render** | `blocks_primary` / `flat_fallback` / `empty`; order `sort_order ASC`, `id ASC`; archived excluded; HTML escape + newlines; internal diagnostics |
| **DB final counts** | migrations **5**; tables **13**; reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1**; report_blocks **6** — **unchanged** by this wave |
| **Smoke** | PASS — unauth redirect; auth preview/print 200; 6 blocks + order; W1–W4; Preview links; regression; DB fingerprint unchanged; session injection |
| **Restrictions** | no schema edits; no business-row mutation; no PDF/export/public share; no secrets; no push |
| **Result** | [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-preview-render-implementation-01.md](reports/REPORT-iseo-report-hub-report-preview-render-implementation-01.md) |
| **Next recommended stage** | **Report Finalization Charter 01** — **completed** (see section below) |

---

## Report Finalization Charter 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — documentation / policy only |
| **Baseline dependency** | Report Preview / Render Implementation 01 (`4334b4a8…` / hash-record `52bd58a9…` / clarify `11a4f232…`); smoke 22/22 PASS; DB unchanged by preview |
| **Designed surface** | Internal monthly finalization; readiness gates; staged status transitions; parent→block locks; explicit submit/review/finalize/reopen routes; audit events; **no** public/PDF/snapshot |
| **Code / runtime / DB this wave** | **None** — no app-source; no runtime sync; no DB mutation |
| **Next implementation candidate** | **I-SEO Report Hub — Report Finalization Implementation 01** — **completed** (see section below) |
| **Charter** | [I-SEO-REPORT-HUB-REPORT-FINALIZATION-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-FINALIZATION-CHARTER-v0.1.md) |
| **Design** | [I-SEO-REPORT-HUB-REPORT-FINALIZATION-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-FINALIZATION-DESIGN-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-REPORT-FINALIZATION-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-FINALIZATION-IMPLEMENTATION-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-REPORT-FINALIZATION-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-FINALIZATION-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-finalization-charter-01.md](reports/REPORT-iseo-report-hub-report-finalization-charter-01.md) |

---

## Report Finalization Implementation 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — source finalization workflow + runtime allowlist sync + smoke + docs |
| **Baseline dependency** | Report Finalization Charter 01 (`68f7fe3c…` / hash-record `86ee4589…` / clarify `2e93900a…`); Report Preview / Render Implementation 01 |
| **Routes** | `POST /monthly-reports/{id}/submit-review`; `POST …/mark-reviewed`; `POST …/finalize`; `POST …/reopen`; auth+CSRF; **no** public/PDF |
| **DB final counts** | migrations **5**; tables **13**; reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1** (`finalized`); report_blocks **6** (all non-archived `reviewed`) |
| **Smoke** | **52/52 PASS** — readiness fail→prep→submit→review→finalize→locks→reopen→re-finalize; preview/print 200; regression; session injection |
| **Restrictions** | no schema edits; no DELETE; no period/weekly mutation; no PDF/export/public share; no secrets; no push |
| **Result** | [I-SEO-REPORT-HUB-REPORT-FINALIZATION-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-FINALIZATION-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-finalization-implementation-01.md](reports/REPORT-iseo-report-hub-report-finalization-implementation-01.md) |
| **Next recommended stage** | **Report Snapshot Charter 01** — **completed** (see section below) |

---

## Report Snapshot Charter 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — documentation / policy only |
| **Baseline dependency** | Report Finalization Implementation 01 (`4bda84e5…` / hash-record `f2234453…` / clarify `10882e24…`); smoke 52/52 PASS; monthly id **1** `finalized`; report_blocks **6** `reviewed` |
| **Designed surface** | Internal immutable/semi-immutable snapshot after finalization; DB-backed `report_snapshots` (DB-07 proposed); payload JSON + checksum; versioning/idempotency; gates; routes/service/UI/audit design; **no** public/PDF/export |
| **Proposed table** | `report_snapshots` — parent `monthly_report_content_id` + `reporting_period_id`; unique `(monthly_report_content_id, version)` + `snapshot_key` |
| **Code / runtime / DB this wave** | **None** — no app-source; no runtime sync; no DB mutation; no SQL migration file |
| **Next implementation candidate** | **I-SEO Report Hub — Report Snapshot DB-07 Migration Apply 01** — **completed** (see section below) |
| **Charter** | [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md) |
| **Design** | [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-DESIGN-v0.1.md) |
| **Schema plan** | [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-SCHEMA-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-SCHEMA-PLAN-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-snapshot-charter-01.md](reports/REPORT-iseo-report-hub-report-snapshot-charter-01.md) |

---

## Report Snapshot DB-07 Migration Apply 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — schema only; **no** snapshot rows; **no** snapshot service/routes/UI |
| **Baseline dependency** | Report Snapshot Charter 01 (`a84e871d…` / hash-record `04a4206c…` / clarify `4c3a69dc…` / git-actions `6cb66b54…`); Finalization Implementation 01; monthly id **1** `finalized`; report_blocks **6** `reviewed` |
| **Result doc** | [I-SEO-REPORT-HUB-DB-07-REPORT-SNAPSHOTS-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DB-07-REPORT-SNAPSHOTS-MIGRATION-APPLY-RESULT-v0.1.md) |
| **Migration file** | `app-source/database/migrations/2026_07_27_000006_create_report_snapshots_table.sql` |
| **Checksum** | `8f1890f6595f5f9fedb3f1366a5207fad9eca55f94dbcc549406313d192c6ab0` |
| **DB target** | `iseo_report_hub_dev` @ `127.0.0.1` only |
| **DB counts** | migrations **5 → 6**; tables **13 → 14**; `report_snapshots` **0** rows; reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1** (`finalized`); report_blocks **6** (all `reviewed`) — business rows unchanged |
| **Next recommended stage** | **I-SEO Report Hub — Report Snapshot Implementation 01** — **completed** (see section below) |
| **Closeout** | [REPORT-iseo-report-hub-db07-report-snapshots-migration-apply-01.md](reports/REPORT-iseo-report-hub-db07-report-snapshots-migration-apply-01.md) |

---

## Report Snapshot Implementation 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — source snapshot workflow + runtime allowlist sync + smoke + docs |
| **Baseline dependency** | DB-07 Migration Apply 01 (`eb1d0ce5…` / hash-record `e290a29c…` / clarify `a9b3c8e8…`); Finalization Implementation 01; monthly id **1** `finalized`; report_blocks **6** `reviewed` |
| **Routes** | `GET/POST /monthly-reports/{id}/snapshot`; `GET /report-snapshots/{id}`; auth; CSRF on POST; **no** public/PDF/export |
| **Snapshot** | id **1**; key `monthly-1-v1`; version **1**; status `active`; checksum short `0d0c863c5c28…`; render_mode `blocks_primary`; 6 blocks; weekly `[1,2,3,7]` |
| **DB final counts** | migrations **6**; tables **14**; `report_snapshots` **1**; reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1** (`finalized`); report_blocks **6** (all `reviewed`) |
| **Smoke** | **64/64 PASS** — create v1; payload/checksum; idempotent second POST; monthly card; preview cue; regression; session injection |
| **Restrictions** | no schema edits; no monthly/block/period/weekly mutation; no DELETE; no PDF/export/public share; no secrets; no push |
| **Result** | [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-snapshot-implementation-01.md](reports/REPORT-iseo-report-hub-report-snapshot-implementation-01.md) |
| **Next recommended stage** | **Report Export / PDF Charter 01** — **completed** (see section below) |

---

## Report Export / PDF Charter 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — documentation / policy only |
| **Baseline dependency** | Report Snapshot Implementation 01 (`7d199791…` / hash-record `040586fe…` / clarify `c6b5d841…` / closeout-hashes `7c3dbf1c…`); smoke 64/64 PASS; snapshot id **1** `monthly-1-v1` `active`; checksum `0d0c863c5c28…`; DB-07 applied (migrations **6**; tables **14**) |
| **Designed surface** | Internal export from **snapshot** (not live monthly/blocks); HTML artifact first; PDF deferred; storage outside public webroot; filename/export_key; access/audit; validation plan |
| **Recommended table** | `report_exports` (DB-08) — metadata for HTML/PDF artifacts; FK snapshot + monthly; unique `export_key` |
| **Storage root (planned)** | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\` |
| **Code / runtime / DB this wave** | **None** — no app-source; no runtime sync; no DB mutation; no SQL migration file; no file/PDF generation |
| **Next implementation candidate** | **I-SEO Report Hub — Report Export DB-08 Migration Apply 01** — **completed** (see section below) |
| **Charter** | [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-CHARTER-v0.1.md) |
| **Design** | [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-DESIGN-v0.1.md) |
| **Storage plan** | [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-STORAGE-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-STORAGE-PLAN-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-export-pdf-charter-01.md](reports/REPORT-iseo-report-hub-report-export-pdf-charter-01.md) |

---

## Report Export DB-08 Migration Apply 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — schema only; **no** export rows; **no** export service/routes/UI |
| **Baseline dependency** | Report Export / PDF Charter 01 (`5cf22391…` / hash-record `0ef4ffbd…` / clarify `f2c03787…` / closeout git-actions `19742518…` / closeout-hashes `ca1fe129…`); Report Snapshot Implementation 01; snapshot id **1** `monthly-1-v1` `active`; checksum `0d0c863c5c28…`; migrations **6**; tables **14** |
| **Result doc** | [I-SEO-REPORT-HUB-DB-08-REPORT-EXPORTS-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DB-08-REPORT-EXPORTS-MIGRATION-APPLY-RESULT-v0.1.md) |
| **Migration file** | `app-source/database/migrations/2026_07_27_000007_create_report_exports_table.sql` |
| **Checksum** | `130e1b2f0a58a5661f0be99aa254e628186c1df6e6252acabbdf97ffe5877baa` |
| **DB target** | `iseo_report_hub_dev` @ `127.0.0.1` only |
| **DB counts** | migrations **6 → 7**; tables **14 → 15**; `report_exports` **0** rows; reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1** (`finalized`); report_blocks **6** (all `reviewed`); report_snapshots **1** (`active`) — business rows unchanged |
| **Next recommended stage** | **I-SEO Report Hub — Report Export HTML Artifact Implementation 01** — **completed** (see section below) |
| **Closeout** | [REPORT-iseo-report-hub-db08-report-exports-migration-apply-01.md](reports/REPORT-iseo-report-hub-db08-report-exports-migration-apply-01.md) |

---

## Report Export HTML Artifact Implementation 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — HTML export service/routes/UI + runtime artifact + smoke + docs |
| **Baseline dependency** | DB-08 Migration Apply 01 (`7b059bb2…` / hash-record `e0a13795…` / clarify `3b35673f…`); Snapshot Implementation 01; snapshot id **1** `monthly-1-v1` `active`; checksum `0d0c863c5c28…` |
| **Routes** | `GET /report-snapshots/{id}/exports`; `POST /report-snapshots/{id}/exports/html`; `GET /report-exports/{id}`; `GET /report-exports/{id}/download`; auth; CSRF on POST; **no** PDF/public/share |
| **Export** | id **1**; key `snapshot-1-html-v1`; format `html`; status `ready`; file checksum short `c194c62b81c6…`; source snapshot checksum `0d0c863c5c28…` |
| **Artifact** | `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.html` (5360 B; outside public; not in Git) |
| **DB final counts** | migrations **7**; tables **15**; `report_exports` **1**; `report_snapshots` **1**; monthly/blocks/periods/weekly unchanged |
| **Smoke** | **47/47 PASS** — create HTML; idempotent repeat; download; snapshot card; regression; session injection |
| **Restrictions** | no schema edits; no business row mutations; no PDF/public; no secrets; no push |
| **Result** | [I-SEO-REPORT-HUB-REPORT-EXPORT-HTML-ARTIFACT-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-HTML-ARTIFACT-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-export-html-artifact-implementation-01.md](reports/REPORT-iseo-report-hub-report-export-html-artifact-implementation-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Export PDF Engine Charter 01** — **completed** (see section below) |

---

## Report Export PDF Engine Charter 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — documentation / policy only |
| **Baseline dependency** | Report Export HTML Artifact Implementation 01 (`25cf8d42…` / hash-record `ce1c095a…`); DB-08 Apply; Snapshot Implementation; HTML export id **1** `snapshot-1-html-v1` ready; artifact outside public; **no** PDF |
| **Decision** | **Do not** implement server PDF yet; run read-only **PDF Engine Probe 01** first; prefer headless/local browser only if already available; otherwise STOP for operator install approval |
| **Preferred PDF source** | Existing ready HTML export artifact (checksum-aligned to snapshot) |
| **Code / runtime / DB / PDF this wave** | **None** — no app-source; no runtime sync; no DB mutation; no engine/package install; no PDF file |
| **Charter** | [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-CHARTER-v0.1.md) |
| **Comparison** | [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-COMPARISON-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-COMPARISON-v0.1.md) |
| **Decision doc** | [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.2.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.2.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.2.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.2.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-export-pdf-engine-charter-01.md](reports/REPORT-iseo-report-hub-report-export-pdf-engine-charter-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Export PDF Engine Probe 01** — **completed** (see section below) |

---

## Report Export PDF Engine Probe 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — read-only environment probe; docs only |
| **Baseline dependency** | PDF Engine Charter 01 (`e16fc414…` / hash-record `22f2f80e…` / tip `4883cd39…`); HTML Artifact Implementation 01; DB-08; HTML export id **1** ready |
| **Probe findings** | Edge **AVAILABLE_READY** (`msedge.exe` **150.0.4078.99**); Chrome **AVAILABLE_READY** (**150.0.7871.182**); Chromium standalone **MISSING**; Firefox/Firefox Dev **present** but **NOT_RECOMMENDED_FOR_MVP**; wkhtmltopdf **MISSING**; Composer **2.10.1** present / no project `composer.json`; PHP **8.3.30** + mbstring/gd/intl/dom/xml/iconv/openssl (zip **off**) |
| **Selected candidate** | **Microsoft Edge** — `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` (Chrome alternate) |
| **HTML / PDF state** | HTML artifact checksum match; **no** `.pdf` under export storage; DB pdf rows **0**; report_exports **1** |
| **Code / runtime / DB / PDF this wave** | **None** — no app-source; no runtime sync; no DB mutation; no install/download; no PDF file |
| **Probe result** | [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-PROBE-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-PROBE-RESULT-v0.1.md) |
| **Decision v0.2** | [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.2.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.2.md) |
| **Implementation plan v0.3** | [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.3.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.3.md) |
| **Validation plan v0.3** | [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.3.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.3.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-export-pdf-engine-probe-01.md](reports/REPORT-iseo-report-hub-report-export-pdf-engine-probe-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Export PDF Browser Implementation 01** — **completed** (see section below) |

---

## Report Export PDF Browser Implementation 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — Edge headless PDF from ready HTML artifact |
| **Engine used** | Microsoft Edge `msedge.exe` **150.0.4078.99** (Chrome fallback available; **not** used) |
| **Routes** | `POST /report-snapshots/{id}/exports/pdf`; existing export detail/download support `format=pdf` |
| **DB final** | migrations **7**; tables **15**; `report_exports` **2**; pdf id **2** key `snapshot-1-pdf-v1` checksum `707e72d65f253de1…`; HTML id **1** unchanged |
| **Artifact** | `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.pdf` (133005 B; `%PDF`; outside public/Git) |
| **Smoke** | lint PASS; service create+idempotent PASS; HTTP **39/39** PASS (`127.0.0.1:8088`, admin_owner session injection) |
| **Restrictions** | no public/share; no package install; no schema/db-migrate; no HTML/snapshot/monthly/block mutations |
| **Result** | [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-BROWSER-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-BROWSER-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-export-pdf-browser-implementation-01.md](reports/REPORT-iseo-report-hub-report-export-pdf-browser-implementation-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Export PDF Hardening 01** — **completed** (see section below) |

---

## Report Export PDF Hardening 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — non-destructive PDF export workflow hardening |
| **Validation coverage** | path (relative/anti-traversal/storage-root); MIME/format/extension; size; checksum; PDF `%PDF` magic; idempotent no-rewrite; download safe headers |
| **DB final** | migrations **7**; tables **15**; `report_exports` **2** unchanged; HTML id **1**; PDF id **2** key `snapshot-1-pdf-v1` checksum `707e72d65f253de1…` |
| **Artifact** | PDF unchanged (133005 B; checksum match; outside public/Git); no new/duplicate artifacts |
| **Smoke** | lint PASS; service failure-mode suite PASS; HTTP **67/67** PASS (`127.0.0.1:8091`) |
| **Restrictions** | no schema/db-migrate; no export/business row mutation; no HTML/PDF regeneration; no public/share; no package install; no push |
| **Result** | [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-HARDENING-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-HARDENING-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-export-pdf-hardening-01.md](reports/REPORT-iseo-report-hub-report-export-pdf-hardening-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Styling / Client Template Charter 01** — **completed** (see section below) |

---

## Report Styling / Client Template Charter 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — docs/policy only |
| **MVP template** | code-first `iseo_default_v1` version **1** (no DB registry yet) |
| **Branding MVP** | i-SEO default text brand only; no logo upload / client CSS DB |
| **Immutability** | snapshot content immutable; existing HTML id **1** / PDF id **2** not silently overwritten |
| **Charter mutations** | **none** — no app-source; no runtime; no DB; no artifact regeneration; no new export rows |
| **Charter** | [I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-CHARTER-v0.1.md) |
| **Design** | [I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-DESIGN-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-IMPLEMENTATION-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-styling-client-template-charter-01.md](reports/REPORT-iseo-report-hub-report-styling-client-template-charter-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Styling Default Template Implementation 01** — **completed** (see section below) |

---

## Report Styling Default Template Implementation 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** |
| **Template** | code-first `iseo_default_v1` version **1** |
| **Dry-render** | **17/17 PASS** (temp sample under STORAGE incoming; removed after validation) |
| **HTTP / regression** | **40/40 PASS** (`127.0.0.1:8091` temporary PHP built-in) |
| **DB final** | migrations **7**; tables **15**; `report_exports` **2** unchanged |
| **Artifacts** | HTML id **1** + PDF id **2** checksums unchanged; no overwrite; no new export rows |
| **UI** | legacy template “not recorded”; future default shown as `iseo_default_v1` v1 |
| **Restrictions** | no schema/DB mutation; no public share; no package install; no push |
| **Result** | [I-SEO-REPORT-HUB-REPORT-STYLING-DEFAULT-TEMPLATE-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-STYLING-DEFAULT-TEMPLATE-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-styling-default-template-implementation-01.md](reports/REPORT-iseo-report-hub-report-styling-default-template-implementation-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Styling Export Version Apply 01** — **completed** (see section below) |

---

## Report Styling Export Version Apply 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** |
| **Template** | `iseo_default_v1` version **1** applied to new export version |
| **Styled HTML v2** | id **3** · `snapshot-1-html-v2` · size **8562** · checksum `27a6eee6…f95f6ffe` |
| **Styled PDF v2** | id **4** · `snapshot-1-pdf-v2` · size **117055** · checksum `a8c4d61c…41a56b6b` · `%PDF` · Edge **150.0.4078.99** |
| **Historical v1** | ids **1**/**2** unchanged (HTML `c194c62b…` / PDF `707e72d6…`) |
| **DB final** | migrations **7**; tables **15**; `report_exports` **4** (html **2**, pdf **2**) |
| **Idempotency** | repeat create returns ids 3/4; checksums stable; no v3 |
| **Smoke** | lint PASS; service create/idempotency PASS; HTTP **55/55** (`127.0.0.1:8091`) |
| **Restrictions** | no schema change; no v1 overwrite; no public share; no package install; no push |
| **Result** | [I-SEO-REPORT-HUB-REPORT-STYLING-EXPORT-VERSION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-STYLING-EXPORT-VERSION-APPLY-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-styling-export-version-apply-01.md](reports/REPORT-iseo-report-hub-report-styling-export-version-apply-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Styling Visual QA 01** — **completed** (see section below) |

---

## Report Styling Visual QA 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** |
| **Verdict** | **PASS_WITH_MINOR_ISSUES** |
| **Styled HTML v2** | inspected — structural PASS; Edge screenshot under STORAGE |
| **Styled PDF v2** | inspected — `%PDF` PASS; **3** pages; `pypdf` text PASS; pixel screenshot inconclusive |
| **Artifact checksums** | **unchanged** (v1 HTML `c194c62b…` / v1 PDF `707e72d6…` / v2 HTML `27a6eee6…` / v2 PDF `a8c4d61c…`) |
| **DB** | **unchanged** — migrations **7**; tables **15**; `report_exports` **4** (html **2**, pdf **2**); no new rows |
| **HTTP** | read-only smoke **35/35 PASS** (`127.0.0.1:8091` temporary PHP built-in) |
| **Issues** | MINOR: Edge PDF print footer leaks local `file:///X:/...` path; PDF badge still “HTML ARTIFACT”; some raw block keys — no BLOCKER/MAJOR |
| **Evidence (STORAGE only)** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\styling-visual-qa-01\` |
| **Result** | [I-SEO-REPORT-HUB-REPORT-STYLING-VISUAL-QA-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-STYLING-VISUAL-QA-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-styling-visual-qa-01.md](reports/REPORT-iseo-report-hub-report-styling-visual-qa-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Export Template Metadata DB-09 Charter 01** — **completed** (see section below) |

---

## Report Export Template Metadata DB-09 Charter 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** (docs/policy only) |
| **Decision** | **Option A** — nullable template/render metadata columns on `report_exports`; defer `report_templates` registry / client assignment |
| **Planned columns** | `template_id`, `template_version`, `render_target`, `render_engine`, `render_options_json`, `source_html_export_id`, `metadata_json` (all NULL-able) |
| **FK** | `source_html_export_id` → `report_exports(id)` **ON DELETE SET NULL** |
| **Backfill policy** | ids **1–2** remain NULL / not recorded; ids **3–4** may be backfilled to `iseo_default_v1` v**1** (PDF **4** → HTML **3**) only in Apply wave with exact-id/key gates |
| **Suggested migration file** | `2026_07_27_000008_add_template_metadata_to_report_exports_table.sql` (Apply must verify sequence) |
| **Mutations this charter** | **none** — no app-source; no runtime; no DB; no SQL/migration file; no artifact change |
| **DB baseline (read-only)** | migrations **7**; tables **15**; `report_exports` **4** (html **2**, pdf **2**) |
| **Charter** | [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-CHARTER-v0.1.md) |
| **Design** | [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-DESIGN-v0.1.md) |
| **Migration plan** | [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-export-template-metadata-db09-charter-01.md](reports/REPORT-iseo-report-hub-report-export-template-metadata-db09-charter-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Export Template Metadata DB-09 Migration Apply 01** — **completed** (see section below) |

---

## Report Export Template Metadata DB-09 Migration Apply 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** |
| **Migration file** | `2026_07_27_000008_add_template_metadata_to_report_exports_table.sql` |
| **Checksum (SHA-256)** | `75202829747e4a15138e2a89760fc68995e5e2cc56f1b20b80664f7a08eb37d0` |
| **Columns** | `template_id`, `template_version`, `render_target`, `render_engine`, `render_options_json`, `source_html_export_id`, `metadata_json` (all nullable) |
| **Indexes** | `idx_report_exports_template` (`template_id`, `template_version`); `idx_report_exports_source_html` (`source_html_export_id`) |
| **FK** | `fk_report_exports_source_html_export` — `source_html_export_id` → `report_exports(id)` **ON DELETE SET NULL** |
| **Backfill matrix** | id **1–2** metadata **NULL**; id **3** `iseo_default_v1` / `1` / `html_export` / `php_template_renderer`; id **4** same template + `pdf_export` / `edge_headless_pdf` / `source_html_export_id=3` |
| **DB final** | migrations **8**; tables **15**; `report_exports` **4** (html **2**, pdf **2**); snapshots/monthly/blocks/periods/weekly unchanged |
| **Artifacts** | v1/v2 HTML/PDF checksums **unchanged**; `%PDF` PASS; no new artifacts |
| **Smoke** | HTTP **12/12 PASS** (`/health`, exports list, details 1–4, downloads 1–4, `/share` 404) via temp PHP `-S` `:8092` |
| **Restrictions** | local DB only; no app code; no new export rows; no artifact mutation; no public/share; no package install; no secrets |
| **Result** | [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-APPLY-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-export-template-metadata-db09-migration-apply-01.md](reports/REPORT-iseo-report-hub-report-export-template-metadata-db09-migration-apply-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Export Template Metadata UI Implementation 01** — **completed** (see section below) |

---

## Report Export Template Metadata UI Implementation 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** |
| **DB metadata read** | yes — repository SELECT includes DB-09 columns + source HTML join |
| **UI display** | export list/detail, snapshot cards, monthly note |
| **Display matrix** | ids **1–2**: `not recorded / legacy` (source HTML unknown for PDF id **2**); ids **3–4**: `iseo_default_v1 v1`; id **4** source `#3 snapshot-1-html-v2` |
| **Future write support** | styled HTML/PDF create paths write DB-09 metadata; **create not invoked** this wave |
| **DB unchanged** | migrations **8**; tables **15**; `report_exports` **4**; row metadata unchanged |
| **Artifacts** | v1/v2 HTML/PDF checksums **unchanged** |
| **Smoke** | HTTP read-only **27/27 PASS** (`127.0.0.1:8092`) |
| **Restrictions** | no schema/migration; no export row mutation; no artifact regen; no public/share; no secrets |
| **Result** | [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-UI-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-UI-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-export-template-metadata-ui-implementation-01.md](reports/REPORT-iseo-report-hub-report-export-template-metadata-ui-implementation-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Delivery / Public Share Charter 01** |

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
| 123 | [product/I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-CHARTER-v0.1.md) | Monthly Report Content CRUD charter (planning) |
| 124 | [product/I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-DESIGN-v0.1.md) | Monthly Report Content CRUD design (routes/forms/validation) |
| 125 | [product/I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-PLAN-v0.1.md) | Monthly Report Content CRUD implementation plan (next wave) |
| 126 | [product/I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-VALIDATION-PLAN-v0.1.md) | Monthly Report Content CRUD validation/smoke plan |
| 127 | [reports/REPORT-iseo-report-hub-monthly-report-content-crud-charter-01.md](reports/REPORT-iseo-report-hub-monthly-report-content-crud-charter-01.md) | Monthly Report Content CRUD charter closeout |
| 128 | [product/I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-RESULT-v0.1.md) | Monthly Report Content CRUD implementation result |
| 129 | [reports/REPORT-iseo-report-hub-monthly-report-content-crud-implementation-01.md](reports/REPORT-iseo-report-hub-monthly-report-content-crud-implementation-01.md) | Monthly Report Content CRUD implementation closeout |
| 130 | [product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-CHARTER-v0.1.md) | DB-06 report blocks charter (planning) |
| 131 | [product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md) | DB-06 `report_blocks` schema plan |
| 132 | [product/I-SEO-REPORT-HUB-REPORT-BLOCKS-LIFECYCLE-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-BLOCKS-LIFECYCLE-v0.1.md) | Report block status lifecycle for DB-06 |
| 133 | [product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-IMPLEMENTATION-PLAN-v0.1.md) | DB-06 migration apply implementation plan |
| 134 | [product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-VALIDATION-PLAN-v0.1.md) | DB-06 validation/smoke plan |
| 135 | [reports/REPORT-iseo-report-hub-db06-report-blocks-charter-01.md](reports/REPORT-iseo-report-hub-db06-report-blocks-charter-01.md) | DB-06 report blocks charter closeout |
| 136 | [product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-MIGRATION-APPLY-RESULT-v0.1.md) | DB-06 migration apply result |
| 137 | [reports/REPORT-iseo-report-hub-db06-report-blocks-migration-apply-01.md](reports/REPORT-iseo-report-hub-db06-report-blocks-migration-apply-01.md) | DB-06 migration apply closeout |
| 138 | [app-source/database/migrations/2026_07_26_000005_create_report_blocks_table.sql](app-source/database/migrations/2026_07_26_000005_create_report_blocks_table.sql) | DB-06 `report_blocks` migration SQL |
| 139 | [product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-CHARTER-v0.1.md) | Report Blocks CRUD charter (planning) |
| 140 | [product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-DESIGN-v0.1.md) | Report Blocks CRUD design (routes/forms/validation) |
| 141 | [product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-PLAN-v0.1.md) | Report Blocks CRUD implementation plan (next wave) |
| 142 | [product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-VALIDATION-PLAN-v0.1.md) | Report Blocks CRUD validation/smoke plan |
| 143 | [reports/REPORT-iseo-report-hub-report-blocks-crud-charter-01.md](reports/REPORT-iseo-report-hub-report-blocks-crud-charter-01.md) | Report Blocks CRUD charter closeout |
| 144 | [product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-RESULT-v0.1.md) | Report Blocks CRUD implementation result |
| 145 | [reports/REPORT-iseo-report-hub-report-blocks-crud-implementation-01.md](reports/REPORT-iseo-report-hub-report-blocks-crud-implementation-01.md) | Report Blocks CRUD implementation closeout |
| 146 | [product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-CHARTER-v0.1.md) | Report Preview / Render charter (planning) |
| 147 | [product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-DESIGN-v0.1.md) | Report Preview / Render design (routes/composition) |
| 148 | [product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-PLAN-v0.1.md) | Report Preview / Render implementation plan (next wave) |
| 149 | [product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-VALIDATION-PLAN-v0.1.md) | Report Preview / Render validation/smoke plan |
| 150 | [reports/REPORT-iseo-report-hub-report-preview-render-charter-01.md](reports/REPORT-iseo-report-hub-report-preview-render-charter-01.md) | Report Preview / Render charter closeout |
| 151 | [product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-RESULT-v0.1.md) | Report Preview / Render implementation result |
| 152 | [reports/REPORT-iseo-report-hub-report-preview-render-implementation-01.md](reports/REPORT-iseo-report-hub-report-preview-render-implementation-01.md) | Report Preview / Render implementation closeout |
| 153 | [product/I-SEO-REPORT-HUB-REPORT-FINALIZATION-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-FINALIZATION-CHARTER-v0.1.md) | Report Finalization charter (planning) |
| 154 | [product/I-SEO-REPORT-HUB-REPORT-FINALIZATION-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-FINALIZATION-DESIGN-v0.1.md) | Report Finalization design (gates/locks/routes) |
| 155 | [product/I-SEO-REPORT-HUB-REPORT-FINALIZATION-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-FINALIZATION-IMPLEMENTATION-PLAN-v0.1.md) | Report Finalization implementation plan (next wave) |
| 156 | [product/I-SEO-REPORT-HUB-REPORT-FINALIZATION-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-FINALIZATION-VALIDATION-PLAN-v0.1.md) | Report Finalization validation/smoke plan |
| 157 | [reports/REPORT-iseo-report-hub-report-finalization-charter-01.md](reports/REPORT-iseo-report-hub-report-finalization-charter-01.md) | Report Finalization charter closeout |
| 158 | [product/I-SEO-REPORT-HUB-REPORT-FINALIZATION-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-FINALIZATION-IMPLEMENTATION-RESULT-v0.1.md) | Report Finalization implementation result |
| 159 | [reports/REPORT-iseo-report-hub-report-finalization-implementation-01.md](reports/REPORT-iseo-report-hub-report-finalization-implementation-01.md) | Report Finalization implementation closeout |
| 160 | [product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md) | Report Snapshot charter (planning) |
| 161 | [product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-DESIGN-v0.1.md) | Report Snapshot design (payload/gates/routes) |
| 162 | [product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-SCHEMA-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-SCHEMA-PLAN-v0.1.md) | Report Snapshot schema plan (`report_snapshots` / DB-07) |
| 163 | [product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-PLAN-v0.1.md) | Report Snapshot implementation plan (next waves) |
| 164 | [product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-VALIDATION-PLAN-v0.1.md) | Report Snapshot validation/smoke plan |
| 165 | [reports/REPORT-iseo-report-hub-report-snapshot-charter-01.md](reports/REPORT-iseo-report-hub-report-snapshot-charter-01.md) | Report Snapshot charter closeout |
| 166 | [product/I-SEO-REPORT-HUB-DB-07-REPORT-SNAPSHOTS-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DB-07-REPORT-SNAPSHOTS-MIGRATION-APPLY-RESULT-v0.1.md) | DB-07 `report_snapshots` migration apply result |
| 167 | [reports/REPORT-iseo-report-hub-db07-report-snapshots-migration-apply-01.md](reports/REPORT-iseo-report-hub-db07-report-snapshots-migration-apply-01.md) | DB-07 report snapshots migration apply closeout |
| 168 | [product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-RESULT-v0.1.md) | Report Snapshot Implementation result |
| 169 | [reports/REPORT-iseo-report-hub-report-snapshot-implementation-01.md](reports/REPORT-iseo-report-hub-report-snapshot-implementation-01.md) | Report Snapshot Implementation closeout |
| 170 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-CHARTER-v0.1.md) | Report Export / PDF charter (planning) |
| 171 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-DESIGN-v0.1.md) | Report Export / PDF design (HTML first / PDF deferred) |
| 172 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-STORAGE-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-STORAGE-PLAN-v0.1.md) | Report Export storage path / no-Git / auth serve |
| 173 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.1.md) | Report Export implementation plan (DB-08 → HTML) |
| 174 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.1.md) | Report Export validation/smoke plan |
| 175 | [reports/REPORT-iseo-report-hub-report-export-pdf-charter-01.md](reports/REPORT-iseo-report-hub-report-export-pdf-charter-01.md) | Report Export / PDF charter closeout |
| 176 | [product/I-SEO-REPORT-HUB-DB-08-REPORT-EXPORTS-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DB-08-REPORT-EXPORTS-MIGRATION-APPLY-RESULT-v0.1.md) | DB-08 `report_exports` migration apply result |
| 177 | [reports/REPORT-iseo-report-hub-db08-report-exports-migration-apply-01.md](reports/REPORT-iseo-report-hub-db08-report-exports-migration-apply-01.md) | DB-08 report exports migration apply closeout |
| 178 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-HTML-ARTIFACT-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-HTML-ARTIFACT-IMPLEMENTATION-RESULT-v0.1.md) | Report Export HTML Artifact Implementation result |
| 179 | [reports/REPORT-iseo-report-hub-report-export-html-artifact-implementation-01.md](reports/REPORT-iseo-report-hub-report-export-html-artifact-implementation-01.md) | Report Export HTML Artifact Implementation closeout |
| 180 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-CHARTER-v0.1.md) | Report Export PDF Engine charter (probe-first) |
| 181 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-COMPARISON-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-COMPARISON-v0.1.md) | PDF engine comparison (manual / Chromium / wkhtmltopdf / Dompdf / mPDF) |
| 182 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.1.md) | PDF engine decision (no implement yet; probe next) |
| 183 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.2.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.2.md) | PDF implementation plan v0.2 (probe → PDF) |
| 184 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.2.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.2.md) | PDF validation plan v0.2 (probe + future PDF smoke) |
| 185 | [reports/REPORT-iseo-report-hub-report-export-pdf-engine-charter-01.md](reports/REPORT-iseo-report-hub-report-export-pdf-engine-charter-01.md) | Report Export PDF Engine charter closeout |
| 186 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-PROBE-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-PROBE-RESULT-v0.1.md) | PDF Engine Probe result (Edge selected) |
| 187 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.2.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.2.md) | PDF engine decision v0.2 (probe-backed Edge) |
| 188 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.3.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.3.md) | PDF implementation plan v0.3 (browser path) |
| 189 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.3.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.3.md) | PDF validation plan v0.3 |
| 190 | [reports/REPORT-iseo-report-hub-report-export-pdf-engine-probe-01.md](reports/REPORT-iseo-report-hub-report-export-pdf-engine-probe-01.md) | Report Export PDF Engine Probe closeout |
| 191 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-BROWSER-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-BROWSER-IMPLEMENTATION-RESULT-v0.1.md) | Report Export PDF Browser Implementation result |
| 192 | [reports/REPORT-iseo-report-hub-report-export-pdf-browser-implementation-01.md](reports/REPORT-iseo-report-hub-report-export-pdf-browser-implementation-01.md) | Report Export PDF Browser Implementation closeout |
| 193 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-HARDENING-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-HARDENING-RESULT-v0.1.md) | Report Export PDF Hardening result |
| 194 | [reports/REPORT-iseo-report-hub-report-export-pdf-hardening-01.md](reports/REPORT-iseo-report-hub-report-export-pdf-hardening-01.md) | Report Export PDF Hardening closeout |
| 195 | [product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-CHARTER-v0.1.md) | Report Styling / Client Template charter |
| 196 | [product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-DESIGN-v0.1.md) | Report Styling / Client Template design |
| 197 | [product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-IMPLEMENTATION-PLAN-v0.1.md) | Report Styling Default Template implementation plan |
| 198 | [product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-VALIDATION-PLAN-v0.1.md) | Report Styling / Client Template validation plan |
| 199 | [reports/REPORT-iseo-report-hub-report-styling-client-template-charter-01.md](reports/REPORT-iseo-report-hub-report-styling-client-template-charter-01.md) | Report Styling / Client Template charter closeout |
| 200 | [product/I-SEO-REPORT-HUB-REPORT-STYLING-DEFAULT-TEMPLATE-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-STYLING-DEFAULT-TEMPLATE-IMPLEMENTATION-RESULT-v0.1.md) | Default template implementation result |
| 201 | [reports/REPORT-iseo-report-hub-report-styling-default-template-implementation-01.md](reports/REPORT-iseo-report-hub-report-styling-default-template-implementation-01.md) | Default template implementation closeout |
| 202 | [product/I-SEO-REPORT-HUB-REPORT-STYLING-EXPORT-VERSION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-STYLING-EXPORT-VERSION-APPLY-RESULT-v0.1.md) | Styled export version apply result |
| 203 | [reports/REPORT-iseo-report-hub-report-styling-export-version-apply-01.md](reports/REPORT-iseo-report-hub-report-styling-export-version-apply-01.md) | Styled export version apply closeout |
| 204 | [product/I-SEO-REPORT-HUB-REPORT-STYLING-VISUAL-QA-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-STYLING-VISUAL-QA-RESULT-v0.1.md) | Report Styling Visual QA result |
| 205 | [reports/REPORT-iseo-report-hub-report-styling-visual-qa-01.md](reports/REPORT-iseo-report-hub-report-styling-visual-qa-01.md) | Report Styling Visual QA closeout |
| 206 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-CHARTER-v0.1.md) | DB-09 export template metadata charter |
| 207 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-DESIGN-v0.1.md) | DB-09 design (Option A columns) |
| 208 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-PLAN-v0.1.md) | DB-09 migration plan |
| 209 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-VALIDATION-PLAN-v0.1.md) | DB-09 validation plan |
| 210 | [reports/REPORT-iseo-report-hub-report-export-template-metadata-db09-charter-01.md](reports/REPORT-iseo-report-hub-report-export-template-metadata-db09-charter-01.md) | DB-09 charter closeout |
| 211 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-APPLY-RESULT-v0.1.md) | DB-09 migration apply result |
| 212 | [reports/REPORT-iseo-report-hub-report-export-template-metadata-db09-migration-apply-01.md](reports/REPORT-iseo-report-hub-report-export-template-metadata-db09-migration-apply-01.md) | DB-09 migration apply closeout |
| 213 | [product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-UI-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-UI-IMPLEMENTATION-RESULT-v0.1.md) | Template metadata UI implementation result |
| 214 | [reports/REPORT-iseo-report-hub-report-export-template-metadata-ui-implementation-01.md](reports/REPORT-iseo-report-hub-report-export-template-metadata-ui-implementation-01.md) | Template metadata UI implementation closeout |

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

1. **Report Delivery / Public Share Charter 01** — **recommended next**
2. Optional: **Report Export Template Metadata Write Smoke 01** (exercise future create writes under controlled charter)
3. Optional: **Report Styling Visual QA Fix 01** (only if operator prioritizes minor QA issues)
3. Optional: **Report Snapshot Hardening 01** / **Report Snapshot Versioning Charter 01** if multi-role or v2 smoke needed
4. Optional: **Report Blocks CRUD Hardening 01** if multi-role HTTP smoke is needed
5. Optional: **Monthly Report Content CRUD Hardening 01** if multi-role HTTP smoke is needed
6. Optional: **Weekly Checkpoints CRUD Hardening 01** if multi-role HTTP smoke is needed
7. Optional: **Reporting Period CRUD Hardening 01** if account-manager edit / multi-role smoke is needed
8. Optional parallel: **v0.5 demo corrections** from backlog (UX only; not product runtime)
9. **SEO specialist feedback** — still **deferred** until operator opens feedback charter
10. Work dictionary extraction/sanitization (из Nikita materials; **exclude** credential sheet)
11. MVP implementation phases 2–11 per implementation charter (Anton / i-SEO)
12. Later: n8n/API/AI integration (events only; human approval gates); public publish from snapshots

**Historical note:** Static demos v0.1–v0.4, report content architecture, and Product Architecture Layer 02 are complete as documentation/demo baselines. Platform decision (PHP+MySQL) supersedes WordPress-as-runtime assumptions for forward work. Phase 0 scaffold + Phase 1A skeleton + Phase 1B source→runtime sync + Apache vhost + Windows `hosts` for `iseo-report-hub.test` are done (direct domain re-smoke PASS). Local DB `iseo_report_hub_dev` is **created**; first migration (DB-01 + minimal DB-02) is **applied**. Auth persistence + local admin bootstrap are **implemented** (DB-backed login; one local admin). DB-03 reporting periods migration is **applied**. Local fixture apply is **complete** (demo client/project/site + period `2026-07`). Reporting Period CRUD **implementation** is complete (internal list/detail/create/edit/archive-by-status; smoke period `2026-08` archived; counts clients/projects/sites/reporting_periods **1/1/1/2**). Weekly Checkpoints DB-04 **migration apply** is complete (`weekly_checkpoints` + local W1–W3 smoke). Weekly Checkpoints CRUD **implementation** is complete (period-scoped list/detail/create/edit/skip-or-archive; W4 smoke id **7** skipped; weekly_checkpoints **4**). Monthly Report Content DB-05 **migration apply** is complete (`monthly_report_contents` + 1 local demo row). Monthly Report Content CRUD **implementation** is complete (period-scoped detail/create/edit/archive-by-status; demo id **1** status `in_progress`; monthly_report_contents **1**). Report Blocks DB-06 **migration apply** is complete (`report_blocks` + 5 local fixture blocks; migrations **5** / tables **13**). Report Blocks CRUD **Charter 01** is complete (docs/policy only; next = Report Blocks CRUD Implementation 01). `app-source/` remains the versioned SoT; runtime is Localhost deploy target.

---

## Boundaries (do not overclaim)

- **Auth persistence is implemented for local MVP** — login/logout/session/roles/audit; **not** production auth hardening
- **One local admin user exists** — no user management UI; no password reset
- **Reporting Period CRUD MVP is implemented** — internal list/detail/create/edit/archive-by-status; CSRF; no DELETE; demo + smoke periods only
- **Runtime has synced auth + CRUD code** at `X:\MARS-Localhost\sites\php\projects\iseo-report-hub`
- **Local MySQL DB `iseo_report_hub_dev` exists** with core auth/org tables + **`reporting_periods`** (DB-03) + **`weekly_checkpoints`** (DB-04) + **`monthly_report_contents`** (DB-05) + **`report_blocks`** (DB-06) + **`report_snapshots`** (DB-07) + **`report_exports`** (DB-08 + DB-09 template metadata; migrations **8**; tables **15**; active snapshot **1**; HTML exports **2**; PDF exports **2**)
- **Local fixture + CRUD smoke** — demo client/project/site **1/1/1**; reporting_periods **2** (`2026-07` fixture + `2026-08` smoke archived); weekly_checkpoints **4** (W1–W3 fixture + W4 smoke `skipped`, `LOCAL_FIXTURE_ONLY`); monthly_report_contents **1** (demo for `2026-07`, status `in_progress`, `LOCAL_FIXTURE_ONLY`); report_blocks **6** (fixture + smoke `risks_and_blockers` under monthly id **1**, `LOCAL_FIXTURE_ONLY`)
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
- **Monthly Report Content DB-05 migration is applied** — table + 1 local demo row
- **Monthly Report Content CRUD MVP is implemented** — period-scoped detail/create/edit/archive-by-status; CSRF; one row per period; source weekly checkpoint links/validation; no DELETE; parent period show integration
- **Report Blocks DB-06 migration is applied** — table + 5 local fixture blocks; migrations **5**; tables **13**; checksum `951bc888…3236`; batch **5**
- **Report Blocks CRUD Charter 01 is complete** — design/implementation/validation plans exist
- **Report Blocks CRUD Implementation 01 is complete** — monthly-scoped list/detail/create/edit; archive-by-status; no hard DELETE; report_blocks **6**
- **Report Preview / Render Charter 01 is complete** — design/implementation/validation plans exist; **no** preview code/runtime/DB changes in charter wave
- **Report Preview / Render Implementation 01 is complete** — internal preview + print routes; smoke 22/22; DB unchanged; **no** public/PDF
- **Report Finalization Charter 01 is complete** — finalization/readiness/lock/reopen design exists
- **Report Finalization Implementation 01 is complete** — staged transitions + readiness + locks; smoke 52/52; monthly id 1 left **finalized**; **no** public/PDF/snapshot
- **Report Snapshot Charter 01 is complete** — internal snapshot policy/design/schema/validation; proposed DB-07 `report_snapshots`; **no** code/runtime/DB in charter wave
- **Report Snapshot DB-07 Migration Apply 01 is complete** — `report_snapshots` table exists; migrations **6**; tables **14**
- **Report Snapshot Implementation 01 is complete** — service/routes/UI; active snapshot v1 (`monthly-1-v1`); smoke 64/64; idempotent; **no** PDF/export/public share
- **Report Export / PDF Charter 01 is complete** — HTML export first from snapshot; PDF deferred; storage outside public/Git; DB-08 `report_exports` designed
- **Report Export DB-08 Migration Apply 01 is complete** — `report_exports` table exists; migrations **7**; tables **15**
- **Report Export HTML Artifact Implementation 01 is complete** — HTML export from snapshot; artifact outside public; auth download; idempotent; smoke 47/47; **no** PDF/public share
- **Report Export PDF Engine Charter 01 is complete** — engine comparison + probe-first decision; HTML artifact preferred source; **no** code/runtime/DB/PDF/install in charter
- **Report Export PDF Engine Probe 01 is complete** — Edge selected (`msedge.exe` 150.0.4078.99); Chrome alternate; **no** code/runtime/DB/PDF/install in probe
- **Report Export PDF Browser Implementation 01 is complete** — Edge headless PDF from HTML artifact; export id **2** `snapshot-1-pdf-v1`; auth download; idempotent; smoke 39/39; **no** public/share/install
- **Report Export PDF Hardening 01 is complete** — path/MIME/size/checksum/`%PDF`/idempotency/download hardening; smoke 67/67; `report_exports` **2** unchanged; **no** public/share/install
- **Report Styling / Client Template Charter 01 is complete** — design/implementation/validation plans; MVP `iseo_default_v1` v**1**; **no** code/runtime/DB/artifact mutation in charter
- **Report Styling Default Template Implementation 01 is complete** — code-first `iseo_default_v1` v**1**; dry-render 17/17; HTTP 40/40; historical exports id **1**/**2** unchanged; **no** new export rows; **no** public/share
- **Report Styling Export Version Apply 01 is complete** — styled HTML/PDF v2 (`snapshot-1-html-v2` / `snapshot-1-pdf-v2`); ids **3**/**4**; `report_exports` **4**; v1 unchanged; idempotent; HTTP 55/55; **no** public/share
- **Report Styling Visual QA 01 is complete** — verdict **PASS_WITH_MINOR_ISSUES**; HTML screenshot + PDF text/integrity; DB/artifacts unchanged; HTTP 35/35; **no** code/runtime/DB mutation
- **Report Export Template Metadata DB-09 Charter 01 is complete** — Option A nullable columns on `report_exports`; backfill policy ids 3–4 only; **no** code/runtime/DB/SQL/artifact mutation in charter
- **Report Export Template Metadata DB-09 Migration Apply 01 is complete** — migration `000008` applied; columns/indexes/FK present; backfill ids **3–4**; ids **1–2** NULL; migrations **8**; `report_exports` **4**; artifacts unchanged; HTTP 12/12
- **Report Export Template Metadata UI Implementation 01 is complete** — repository/service/UI DB-first metadata display; future styled create writes metadata (not invoked); DB/artifacts unchanged; HTTP 27/27; **no** public/share
- **Next** = Report Delivery / Public Share Charter 01
- **No drag/drop reorder / public PDF share / rich text editor / client portal** (runtime)
- **No autonomous publication**
- **Website Factory is not runtime owner** — methodology + prototype lane only
- **Static demo v0.4 is UX reference only** — not implementation
- **Historical WP architecture docs** remain in corpus as legacy planning — not current SoT
- **Domain `iseo-report-hub.test` resolves to 127.0.0.1** and serves auth-capable routes over HTTP
- **No separate runtime Git repository** — and none should be created without charter
