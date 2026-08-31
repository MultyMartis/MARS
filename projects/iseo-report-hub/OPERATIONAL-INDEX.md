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
| **Active stage** | **Project-Centric Dashboard and IA Charter 01 complete** — operator rejected demo home (`Рабочий контур` / `Быстрые действия` / `Статус локальной системы`); project-centric IA charter + implementation plan recorded; next impl = **Project Dashboard Implementation 01**; parallel = operator manual walkthrough still pending (`LOCAL SPECIALIST MVP ACCEPTED_BY_MARS_REVIEW / OPERATOR_MANUAL_WALKTHROUGH_PENDING`); host track paused |
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
| **Next recommended stage** | **I-SEO Report Hub — Report Delivery / Public Share Charter 01** — **completed** (see section below) |

---

## Report Delivery / Public Share Charter 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — docs/policy only |
| **MVP decision** | **Option B** — tokenized public share for ready styled PDF exports only |
| **Shareable policy** | `format=pdf`, status `ready`, `template_id` not null, `render_target=pdf_export`; first local target export id **4**; **no** HTML / legacy v1 in MVP |
| **Security** | token hash only; plaintext URL once; expiry default 30d; revoke; checksum before stream; no raw path; no public listing; audit events |
| **Data model** | recommended table `report_export_shares` (DB-10) |
| **Routes (planned)** | internal create/list/revoke; public `GET /share/report/{token}`; **not implemented** this wave |
| **Deferred** | client portal; email delivery; one-time links; HTML public share |
| **Mutations this wave** | **none** — no app-source / runtime / DB / SQL / token / public route / artifact changes |
| **Charter** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md) |
| **Design** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DESIGN-v0.1.md) |
| **Security model** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-SECURITY-MODEL-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-SECURITY-MODEL-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-delivery-public-share-charter-01.md](reports/REPORT-iseo-report-hub-report-delivery-public-share-charter-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Delivery Public Share DB-10 Migration Apply 01** — **completed** (see section below) |

---

## Report Delivery Public Share DB-10 Migration Apply 01 (2026-07-27)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — local DB migration only |
| **Migration** | `2026_07_27_000009_create_report_export_shares_table.sql` |
| **Checksum** | `384fbb48cccc55989035056c899af701f0dbb49e2c362b44a23acaf656ba82d3` |
| **Table** | `report_export_shares` — 16 columns; unique `token_hash`; indexes export/status, expires/status, created_by, revoked_by |
| **FKs** | `report_export_id` → `report_exports(id)` RESTRICT; `created_by`/`revoked_by` → `users(id)` SET NULL |
| **CHECK** | `status` IN (`active`,`revoked`,`expired`) |
| **Share rows** | **0** (no tokens created) |
| **DB final** | migrations **9**; tables **16**; `report_exports` **4** unchanged; business counts unchanged |
| **Artifacts** | v1/v2 HTML/PDF checksums **unchanged**; `%PDF-` PASS; no new artifacts |
| **Smoke** | **13/13 PASS** — health; auth exports/details/downloads 1–4; `/share` 404; `/share/report/test-token` 404 |
| **Restrictions** | local DB only; no app code; no share row/token; no public route; no export/artifact mutation; no package install; no secrets |
| **Result** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DB10-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DB10-MIGRATION-APPLY-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-delivery-public-share-db10-migration-apply-01.md](reports/REPORT-iseo-report-hub-report-delivery-public-share-db10-migration-apply-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Delivery Public Share Implementation 01** — **completed** (see section below) |

---

## Report Delivery Public Share Implementation 01 (2026-07-28)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — MVP tokenized public share for ready styled PDF |
| **Routes** | internal `GET/POST /report-exports/{id}/shares`; `POST /report-export-shares/{id}/revoke`; public `GET /share/report/{token}` |
| **Token model** | `random_bytes(32)` hex; store SHA-256 hash only; plaintext URL once |
| **Eligibility** | id **4** shareable; ids **1–3** not (HTML and/or legacy metadata) |
| **DB final** | migrations **9**; tables **16**; `report_exports` **4**; `report_export_shares` **2** revoked (smoke); active **0** |
| **Artifacts** | v1/v2 checksums **unchanged**; `%PDF` PASS; no public files |
| **Smoke** | **46/46 PASS** (PHP `-S :8092`; session injection; create/access/revoke/deny) |
| **Restrictions** | local DB only; no export/artifact mutation; no portal/email; no `/r/{token}`; no secrets; no push |
| **Result** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-delivery-public-share-implementation-01.md](reports/REPORT-iseo-report-hub-report-delivery-public-share-implementation-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Delivery Public Share Hardening 01** — **completed** (see section below) |

---

## Report Delivery Public Share Hardening 01 (2026-07-28)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — hardening / safety / regression |
| **Token validation** | Exact **64 hex** before hash; reject empty/short/non-hex/path/`%`/null; `hashPublicToken()` |
| **Denial policy** | invalid/missing/ineligible/artifact → **404**; revoked/expired/max_access → **410** |
| **Public headers** | PDF attachment + length + nosniff + private/no-store + noindex + Pragma/Expires/Referrer-Policy |
| **Access tracking** | `access_count` only after stream preflight; SQL guards active/expiry/max_access |
| **UI** | no `token_hash` / IP-UA hashes in share UI; once-URL only; active blocks recreate |
| **DB final** | migrations **9**; tables **16**; `report_exports` **4**; `report_export_shares` **3** revoked (ids 1–2 preserved); active **0** |
| **Artifacts** | v1/v2 checksums **unchanged**; `%PDF` PASS; no public files |
| **Smoke** | **66/66 PASS** (`127.0.0.1:8092`; session injection; token unit 9/9) |
| **Restrictions** | local DB only; no export/artifact mutation; no prune of existing revoked rows; no portal/email; no `/r/{token}`; no secrets; no push |
| **Result** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-HARDENING-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-HARDENING-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-delivery-public-share-hardening-01.md](reports/REPORT-iseo-report-hub-report-delivery-public-share-hardening-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Delivery Public Share Visual QA 01** — **completed** (see section below) |

---

## Report Delivery Public Share Visual QA 01 (2026-07-28)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — visual / UX / public-route QA |
| **Verdict** | **PASS_WITH_MINOR_ISSUES** (BLOCKER **0** / MAJOR **0** / MINOR **2**) |
| **Evidence** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\public-share-visual-qa-01\` (STORAGE only; not Git) |
| **Internal UI** | ids **1–3** Not shareable with reasons; id **4** Shareable; revoked rows readable; once-URL once-only; no `token_hash` / IP-UA / absolute path leaks |
| **Public route** | valid token **200** PDF + hardening headers; revoked **410**; malformed/invalid **404**; `/share` + `/r/test` **404** |
| **DB final** | migrations **9**; tables **16**; `report_exports` **4**; `report_export_shares` **4** revoked (ids **1–3** preserved + id **4** QA); active **0** |
| **Artifacts** | v1/v2 checksums **unchanged**; `%PDF` PASS; no public files |
| **Smoke** | **86/86 PASS** (`127.0.0.1:8092`; session injection; token redacted) |
| **Issues** | MINOR relative storage_path on auth detail; MINOR list badge **No** vs detail **Not shareable** |
| **Restrictions** | no app-source/runtime edits; no export/artifact mutation; no prune; no long-lived active share; no secrets; no push |
| **Result** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VISUAL-QA-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VISUAL-QA-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-delivery-public-share-visual-qa-01.md](reports/REPORT-iseo-report-hub-report-delivery-public-share-visual-qa-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Delivery Client Handoff UX Charter 01** — **completed** (see section below) |

---

## Report Delivery Client Handoff UX Charter 01 (2026-07-28)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — docs/policy only |
| **MVP decision** | **Option B** — internal handoff panel + copy pack; keep public route as direct PDF token stream |
| **Deferred** | Option C public landing; Option D client portal; Option E email automation |
| **Tracking** | **No DB tracking** in immediate Implementation 01; **DB-11 `report_delivery_events` deferred** until operator confirms |
| **Copy pack** | Short Telegram/messenger; formal email; internal operator note (RU first); placeholders only; no live token |
| **Once URL** | Public URL shown once at create; lost URL → revoke + recreate; no recoverable token storage |
| **Visual QA carry-forward** | `UI-REL-STORAGE-PATH` (de-emphasize path); `UI-LIST-SHARE-LABEL` (unify to **Not shareable**) — fix in Implementation 01 |
| **DB / runtime / app-source** | **Unchanged** this wave (read-only DB check: migrations **9**; tables **16**; shares **4** revoked / active **0**) |
| **Charter** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-CHARTER-v0.1.md) |
| **Design** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-DESIGN-v0.1.md) |
| **Copy pack** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-COPY-PACK-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-COPY-PACK-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-IMPLEMENTATION-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-delivery-client-handoff-ux-charter-01.md](reports/REPORT-iseo-report-hub-report-delivery-client-handoff-ux-charter-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Delivery Client Handoff UX Implementation 01** — **completed** (see section below) |

---

## Report Delivery Client Handoff UX Implementation 01 (2026-07-28)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — app-source + runtime sync + smoke |
| **Handoff surface** | Export detail + `/report-exports/{id}/shares` readiness panel (primary) |
| **Copy pack** | RU short / formal email / internal note — shown once with plaintext URL |
| **DB tracking** | **None** (no DB-11 / no `report_delivery_events`) |
| **Visual QA minors** | `UI-REL-STORAGE-PATH` + `UI-LIST-SHARE-LABEL` **resolved** |
| **Public route** | Unchanged direct PDF stream `GET /share/report/{token}` |
| **Final DB / shares** | migrations **9**; tables **16**; exports **4**; shares **5** revoked / active **0** |
| **Smoke** | **115/115 PASS** |
| **Restrictions** | No portal/email/landing/`/r/{token}`; no plaintext token in DB/report; no artifact mutation; no push |
| **Result** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-delivery-client-handoff-ux-implementation-01.md](reports/REPORT-iseo-report-hub-report-delivery-client-handoff-ux-implementation-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Delivery Client Handoff UX Visual QA 01** — **completed** (see section below) |

---

## Report Delivery Client Handoff UX Visual QA 01 (2026-07-28)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — Visual QA / evidence / docs only |
| **Verdict** | **PASS** |
| **Evidence** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\client-handoff-ux-visual-qa-01\` (STORAGE only; not Git) |
| **Issues** | BLOCKER **0** / MAJOR **0** / MINOR **0**; prior `UI-REL-STORAGE-PATH` + `UI-LIST-SHARE-LABEL` **resolved** |
| **Handoff / copy pack** | Readiness panel on export detail + shares; once RU copy pack; revisit guidance; revoke+recreate |
| **Public route** | Unchanged direct PDF stream `GET /share/report/{token}` |
| **Final DB / shares** | migrations **9**; tables **16**; exports **4**; shares **6** revoked / active **0** |
| **Artifacts** | v1/v2 checksums unchanged; `%PDF` OK |
| **Smoke** | **129/129 PASS** |
| **Restrictions** | No app-source/runtime code edits; no portal/email/landing/`/r/{token}`; no plaintext token in DB/report; no artifact mutation; no push |
| **Result** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-VISUAL-QA-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-VISUAL-QA-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-delivery-client-handoff-ux-visual-qa-01.md](reports/REPORT-iseo-report-hub-report-delivery-client-handoff-ux-visual-qa-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Report Delivery Production Readiness Charter 01** — **completed** (see section below) |

---

## Report Delivery Production Readiness Charter 01 (2026-07-30)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — docs/policy only |
| **Definition** | Production readiness ≠ production deployment; local MVP ready; production pilot blocked until environment/secrets/DB/backup/access/monitoring/real-data gates |
| **Local MVP gates** | **A–D PASS** — functional flow; export integrity; public share security; client handoff UX |
| **Production blockers** | Gates **E–K REQUIRED_BEFORE_PRODUCTION** — environment; secrets/env; prod DB/migration; backup/rollback; access/users; monitoring/logs; real client data |
| **Deferred** | Gate **M** DB-11; Gate **N** landing/portal/email; Gate **L** retention/pruning **READY_FOR_PLAN** |
| **DB / runtime / app-source** | **Unchanged** in this wave (no mutation) |
| **Charter** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-CHARTER-v0.1.md) |
| **Gates** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-GATES-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-GATES-v0.1.md) |
| **Risk register** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-RISK-REGISTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-RISK-REGISTER-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-IMPLEMENTATION-PLAN-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-delivery-production-readiness-charter-01.md](reports/REPORT-iseo-report-hub-report-delivery-production-readiness-charter-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Production Environment Charter 01** — **completed** (see section below) |

---

## Production Environment Charter 01 (2026-07-30)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — docs/policy only |
| **Recommended candidate** | **Option C — VPS PHP-FPM/Nginx/MySQL** (advisory; not provisioned) |
| **Environment selected?** | **No** — operator Decision 01 required |
| **Open operator decisions** | Host type; domain; HTTPS; DB engine; PHP pin; PDF mode; deploy method; backup location; access model; logging policy; real client data readiness; DB-11 (still deferred unless reopened) |
| **Hard boundaries** | No hosting setup; no domain/DNS/HTTPS/server ops; no app-source/runtime/DB/artifact mutation; no share token; no deploy |
| **DB caveat** | Live MySQL re-probe during Production Readiness Charter 01 and this charter **failed** (connection refused to `127.0.0.1`); expected DB baseline from Client Handoff Visual QA 01; **re-check local DB** before future implementation if local evidence needed |
| **Charter** | [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-CHARTER-v0.1.md) |
| **Options** | [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPTIONS-v0.1.md](product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPTIONS-v0.1.md) |
| **Requirements** | [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-REQUIREMENTS-v0.1.md](product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-REQUIREMENTS-v0.1.md) |
| **Decision log** | [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-LOG-v0.1.md](product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-LOG-v0.1.md) |
| **Validation plan** | [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-VALIDATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-production-environment-charter-01.md](reports/REPORT-iseo-report-hub-production-environment-charter-01.md) |
| **Next recommended stage** | **I-SEO Report Hub — Production Environment Decision 01** — **completed** (see section below) |

---

## Production Environment Decision 01 (2026-07-30)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — docs / decision-support only |
| **Decision state** | **`RECOMMENDATION_READY`** — not `APPROVED_FOR_IMPLEMENTATION`; not `PRODUCTION_SELECTED` |
| **Recommended default** | **Option C — VPS PHP-FPM/Nginx/MySQL** (Nginx preferred; PHP 8.3; MySQL 8.x; docroot `/public`) |
| **Environment selected?** | **No** — operator must answer checklist / Operator Decision 01 |
| **Operator approval checklist** | [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPERATOR-APPROVAL-CHECKLIST-v0.1.md](product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPERATOR-APPROVAL-CHECKLIST-v0.1.md) — fields 1–14 **pending** |
| **Decision brief** | [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-BRIEF-v0.1.md](product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-BRIEF-v0.1.md) |
| **Decision matrix** | [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-MATRIX-v0.1.md](product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-MATRIX-v0.1.md) |
| **Next wave plan** | [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-NEXT-WAVE-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-NEXT-WAVE-PLAN-v0.1.md) |
| **Hard boundaries** | No server access; no deploy; no DNS/HTTPS; no DB mutation; no app-source/runtime/secrets; no production claim |
| **SAFE UNKNOWN** | Live MySQL re-probe still failed (TCP 3306 refused this wave; same as prior charters); before any implementation/deploy, re-check local DB state if local evidence needed; baseline remains latest attested Client Handoff Visual QA |
| **Closeout** | [REPORT-iseo-report-hub-production-environment-decision-01.md](reports/REPORT-iseo-report-hub-production-environment-decision-01.md) |
| **Next recommended stage (environment track)** | **I-SEO Report Hub — Production Environment Operator Decision 01** |
| **Next recommended stage (product UX track)** | **Operator manual demo visual shell click-through** — after Demo Visual Shell Alignment Implementation 02 |

---

## Russian UX and HTML Demo Alignment Charter 01 (2026-07-30)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — docs / product-UX planning only |
| **Problem** | Live PHP+SQL MVP works, but UI is English-heavy technical skeleton; not aligned with accepted HTML demo; Russian UX required before production for i-SEO managers/SEO specialists |
| **HTML demo** | **Found** — `workspaces/website-factory-operations/iseo-report-hub-prototype/` (static demo **v0.4**, INTLSEO-inspired, Russian chrome) |
| **Live UI** | Dark Phase 1A skeleton EN; stale footer «no DB · runtime not synced»; technical terms on primary surfaces |
| **Decisions** | Target language **Russian**; hide technical fields by default; manager-first flow; retain PHP+SQL engine; no production until UX accepted |
| **PDF target** | Client-facing `SEO-отчет за {месяц}` + Russian sections; strip fixture/local/tech from real reports |
| **Charter** | [I-SEO-REPORT-HUB-RUSSIAN-UX-HTML-DEMO-ALIGNMENT-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-RUSSIAN-UX-HTML-DEMO-ALIGNMENT-CHARTER-v0.1.md) |
| **Inventory** | [I-SEO-REPORT-HUB-RUSSIAN-UX-HTML-DEMO-INVENTORY-v0.1.md](product/I-SEO-REPORT-HUB-RUSSIAN-UX-HTML-DEMO-INVENTORY-v0.1.md) |
| **Copy dictionary** | [I-SEO-REPORT-HUB-RUSSIAN-UX-COPY-DICTIONARY-v0.1.md](product/I-SEO-REPORT-HUB-RUSSIAN-UX-COPY-DICTIONARY-v0.1.md) |
| **Manager flow** | [I-SEO-REPORT-HUB-RUSSIAN-UX-MANAGER-FLOW-v0.1.md](product/I-SEO-REPORT-HUB-RUSSIAN-UX-MANAGER-FLOW-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-RUSSIAN-UX-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-RUSSIAN-UX-IMPLEMENTATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-russian-ux-html-demo-alignment-charter-01.md](reports/REPORT-iseo-report-hub-russian-ux-html-demo-alignment-charter-01.md) |
| **DB / runtime / app-source** | **Unchanged** in this wave (no mutation) |
| **Next recommended stage** | **I-SEO Report Hub — Russian UX and Demo Alignment Implementation 01** |

---

## Russian UX and Demo Alignment Implementation 01 (2026-07-30)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — first practical Russian UX layer in live PHP+SQL app |
| **Result** | [I-SEO-REPORT-HUB-RUSSIAN-UX-DEMO-ALIGNMENT-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-RUSSIAN-UX-DEMO-ALIGNMENT-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-russian-ux-demo-alignment-implementation-01.md](reports/REPORT-iseo-report-hub-russian-ux-demo-alignment-implementation-01.md) |
| **Translated** | Nav, login, dashboard, periods list, exports, export detail, shares, health chrome, footer, handoff checklist/warnings |
| **Demo alignment** | Labels/IA/manager flow from static demo v0.4; **no** full CSS shell / pixel-perfect |
| **PDF artifact** | **Unchanged** (no regeneration) |
| **Runtime sync** | Exact allowlist source → Laragon runtime |
| **DB / shares** | Stable (exports 4 / shares 6 / active 0); no token created |
| **Next recommended stage** | Superseded for product UX track by **Demo Visual Alignment Charter 01** → Implementation 02 (operator click-through still useful after visual shell) |

---

## Demo Visual Alignment Charter 01 (2026-07-31)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — docs / visual specification only |
| **Problem** | Russian UX accepted for local MVP, but live PHP UI still does not visually match static demo v0.4 (dark top-nav vs light + dark sidebar shell) |
| **Operator feedback** | Full visual pull onto demo v0.4 had not been chartered before; Laragon live OK; goal = local visual alignment without breaking engine |
| **HTML demo** | `workspaces/website-factory-operations/iseo-report-hub-prototype/` (v0.4) — inventory + mapping refreshed |
| **Live UI** | Post–Russian UX: RU A–D + truthful footer; shell still `#0f1c24` + `site-header` top nav; no sidebar |
| **Decisions** | Impl 02 = close visual shell alignment (not pixel-perfect); retain routes/data/RU copy/manager flow; **exclude** client PDF/`client-report.html` alignment |
| **Charter** | [I-SEO-REPORT-HUB-DEMO-VISUAL-ALIGNMENT-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-VISUAL-ALIGNMENT-CHARTER-v0.1.md) |
| **Gap map** | [I-SEO-REPORT-HUB-DEMO-VISUAL-GAP-MAP-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-VISUAL-GAP-MAP-v0.1.md) |
| **Page mapping** | [I-SEO-REPORT-HUB-DEMO-VISUAL-PAGE-MAPPING-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-VISUAL-PAGE-MAPPING-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-DEMO-VISUAL-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-VISUAL-IMPLEMENTATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-demo-visual-alignment-charter-01.md](reports/REPORT-iseo-report-hub-demo-visual-alignment-charter-01.md) |
| **DB / runtime / app-source / demo HTML** | **Unchanged** in this wave (no mutation) |
| **Next recommended stage** | **I-SEO Report Hub — Demo Visual Shell Alignment Implementation 02** |
| **Separate later** | **I-SEO Report Hub — Client Report Template Visual Alignment Charter 01** |

---

## Demo Visual Shell Alignment Implementation 02 (2026-07-31)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — close visual shell alignment to demo v0.4 (not pixel-perfect) |
| **Result** | [I-SEO-REPORT-HUB-DEMO-VISUAL-SHELL-ALIGNMENT-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-VISUAL-SHELL-ALIGNMENT-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-demo-visual-shell-alignment-implementation-02.md](reports/REPORT-iseo-report-hub-demo-visual-shell-alignment-implementation-02.md) |
| **Shell** | Dark left sidebar + light main + white topbar + red `#c8102e` accent + ~1440px content |
| **Pages** | Dashboard, periods, exports, export detail, shares, health, login |
| **Russian UX** | Retained from Implementation 01 |
| **PDF / client-report** | **Unchanged** (no regeneration; out of scope) |
| **Runtime sync** | Exact allowlist source → Laragon runtime |
| **DB / shares** | Stable (exports 4 / shares 6 / active 0); no token created |
| **Next recommended stage** | Superseded for product UX track by **UI Screenshot QA / Brand / Nikita Discovery 01** → **Implementation 03** |
| **Separate later** | **I-SEO Report Hub — Client Report Template Visual Alignment Charter 01** |

---

## UI Screenshot QA, Brand Style and Nikita Templates Discovery 01 (2026-08-07)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — docs / discovery / QA / planning only |
| **Problem** | Shell OK after Impl 02, but secondary UI still English/technical; hub red accent ≠ live i-seo.su; report fields must align to Nikita templates |
| **UI inventory** | [I-SEO-REPORT-HUB-UI-SCREENSHOT-QA-INVENTORY-v0.1.md](product/I-SEO-REPORT-HUB-UI-SCREENSHOT-QA-INVENTORY-v0.1.md) |
| **Brand discovery** | [I-SEO-REPORT-HUB-ISEO-BRAND-STYLE-DISCOVERY-v0.1.md](product/I-SEO-REPORT-HUB-ISEO-BRAND-STYLE-DISCOVERY-v0.1.md) — accent `#facc15`, font Manrope |
| **Nikita templates** | [I-SEO-REPORT-HUB-NIKITA-REPORT-TEMPLATES-DISCOVERY-v0.1.md](product/I-SEO-REPORT-HUB-NIKITA-REPORT-TEMPLATES-DISCOVERY-v0.1.md) — 3 files under STORAGE `materials from Nikita` |
| **Gap map** | [I-SEO-REPORT-HUB-UI-BRAND-TEMPLATE-GAP-MAP-v0.1.md](product/I-SEO-REPORT-HUB-UI-BRAND-TEMPLATE-GAP-MAP-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-UI-BRAND-TEMPLATE-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-UI-BRAND-TEMPLATE-IMPLEMENTATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-ui-screenshot-qa-brand-nikita-discovery-01.md](reports/REPORT-iseo-report-hub-ui-screenshot-qa-brand-nikita-discovery-01.md) |
| **Code / runtime / DB / shares / PDF** | **Unchanged** |
| **Next recommended stage** | **Operator manual UI cleanup and i-seo brand click-through** (then **Nikita Report Template Data Model Charter 01**) |
| **Separate later** | **Nikita Report Template Data Model Charter 01**; **Client Report Template Visual Alignment Charter 01**; optional **Local Share QA Cleanup 01** |

---

## UI Russian Cleanup and i-SEO Brand Layer Implementation 03 (2026-08-07)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — view/CSS/controller titles only |
| **Result** | [I-SEO-REPORT-HUB-UI-RUSSIAN-CLEANUP-BRAND-LAYER-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-UI-RUSSIAN-CLEANUP-BRAND-LAYER-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-ui-russian-cleanup-brand-layer-implementation-03.md](reports/REPORT-iseo-report-hub-ui-russian-cleanup-brand-layer-implementation-03.md) |
| **Russian cleanup** | Secondary period/monthly/preview/blocks/weekly/snapshot chrome translated; `UiLabels` helper |
| **Brand** | `#facc15` CTA, dark `#18181B` sidebar, Manrope stack, pill buttons |
| **PDF / Nikita model** | **Unchanged / not implemented** |
| **Shares / exports** | Unmutated — exports **4**, shares **7**, active **1**, revoked **6** |
| **Runtime sync** | Exact allowlist source → Laragon |
| **Next recommended stage** | **Operator manual UI cleanup and i-seo brand click-through** |
| **Separate later** | **Nikita Report Template Data Model Charter 01**; **Client Report Template Visual Alignment Charter 01**; optional **Local Share QA Cleanup 01** |

---

## UI Cleanup Brand Fix 01 (2026-08-07)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — safe fix-pass after Implementation 03 |
| **Result** | [I-SEO-REPORT-HUB-UI-CLEANUP-BRAND-FIX-01-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-UI-CLEANUP-BRAND-FIX-01-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-ui-cleanup-brand-fix-01.md](reports/REPORT-iseo-report-hub-ui-cleanup-brand-fix-01.md) |
| **Dashboard** | Active share status from DB (`countByStatus`); no static «Активной ссылки нет» when active exists |
| **Reason/detail** | Finalization/snapshot/share eligibility messages Russianized via services + `UiLabels::message` |
| **Brand** | Verified `#facc15` / Manrope / `#18181B`; no CSS change required |
| **PDF / Nikita model** | **Unchanged / not implemented** |
| **Shares / exports** | Unmutated — exports **4**, shares **7**, active **1**, revoked **6** (active id 7 / `test-first-link`) |
| **Runtime sync** | Exact allowlist source → Laragon |
| **Next recommended stage** | **Operator manual UI cleanup brand fix click-through** (attested OK to proceed) |
| **Separate later** | **Nikita Report Template Data Model Charter 01**; **Client Report Template Visual Alignment Charter 01**; optional **Local Share QA Cleanup 01** |

---

## Nikita Report Template Data Model Charter 01 (2026-08-17)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — docs / product / data-model charter only |
| **Closeout** | [REPORT-iseo-report-hub-nikita-report-template-data-model-charter-01.md](reports/REPORT-iseo-report-hub-nikita-report-template-data-model-charter-01.md) |
| **Baseline** | [I-SEO-REPORT-HUB-CURRENT-DATA-MODEL-BASELINE-v0.1.md](product/I-SEO-REPORT-HUB-CURRENT-DATA-MODEL-BASELINE-v0.1.md) |
| **Taxonomy** | [I-SEO-REPORT-HUB-NIKITA-TAXONOMY-v0.1.md](product/I-SEO-REPORT-HUB-NIKITA-TAXONOMY-v0.1.md) |
| **Target IA** | [I-SEO-REPORT-HUB-TARGET-REPORT-INFORMATION-ARCHITECTURE-v0.1.md](product/I-SEO-REPORT-HUB-TARGET-REPORT-INFORMATION-ARCHITECTURE-v0.1.md) |
| **Block mapping** | [I-SEO-REPORT-HUB-BLOCK-FIELD-MAPPING-v0.1.md](product/I-SEO-REPORT-HUB-BLOCK-FIELD-MAPPING-v0.1.md) |
| **Options** | [I-SEO-REPORT-HUB-NIKITA-DATA-MODEL-OPTIONS-v0.1.md](product/I-SEO-REPORT-HUB-NIKITA-DATA-MODEL-OPTIONS-v0.1.md) — **Option B recommended** |
| **Migration charter** | [I-SEO-REPORT-HUB-NIKITA-MIGRATION-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-NIKITA-MIGRATION-CHARTER-v0.1.md) — shapes accepted; applied via Implementation 01 / DB-11 |
| **Sequence** | [I-SEO-REPORT-HUB-NIKITA-IMPLEMENTATION-SEQUENCE-v0.1.md](product/I-SEO-REPORT-HUB-NIKITA-IMPLEMENTATION-SEQUENCE-v0.1.md) |
| **Code / runtime / DB / share / PDF** | Charter wave itself unchanged; see Implementation 01 for DB-11 apply |
| **Next recommended stage** | **Work Entry UI Implementation 01** (after Catalogue Model Implementation 01) |
| **Separate later** | Summary Assembly → **Client Report Template Visual Alignment Charter 01** → Client Template Impl; optional **Local Share QA Cleanup 01** |

---

## Nikita Catalogue Seed and Work Entry Model Implementation 01 (2026-08-17)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — local DB-11 + seed + read repositories |
| **Closeout** | [REPORT-iseo-report-hub-nikita-catalogue-seed-work-entry-model-implementation-01.md](reports/REPORT-iseo-report-hub-nikita-catalogue-seed-work-entry-model-implementation-01.md) |
| **Result** | [I-SEO-REPORT-HUB-NIKITA-CATALOGUE-SEED-WORK-ENTRY-MODEL-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-NIKITA-CATALOGUE-SEED-WORK-ENTRY-MODEL-IMPLEMENTATION-RESULT-v0.1.md) |
| **Migration** | `2026_08_17_000010_create_nikita_seo_work_catalogue_and_monthly_work_entries.sql` (DB-11) |
| **Seed** | `tools/seed-nikita-catalogue.php` — 13 categories / 31 items / 7 monthly fixture entries (report id 1) |
| **Repositories** | `SeoWorkCategoryRepository`, `SeoWorkItemRepository`, `MonthlyReportWorkEntryRepository` |
| **6 client blocks / exports / shares / PDF** | **Unchanged** (exports 4; shares 7; active 1 id 7; PDF not regenerated) |
| **UI editor / summary assembly** | **Out of scope** |
| **Next recommended stage** | **Work Entry UI Implementation 01** → **done** (see below) |
| **Separate later** | Summary Assembly → Client Report Template Visual Alignment; optional Local Share QA Cleanup 01 |

---

## Work Entry UI Implementation 01 (2026-08-17)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — read-only monthly work entries UI |
| **Closeout** | [REPORT-iseo-report-hub-work-entry-ui-implementation-01.md](reports/REPORT-iseo-report-hub-work-entry-ui-implementation-01.md) |
| **Result** | [I-SEO-REPORT-HUB-WORK-ENTRY-UI-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-UI-IMPLEMENTATION-RESULT-v0.1.md) |
| **Page** | `/monthly-reports/1` section **Работы за месяц** (7 seeded cards) |
| **Partial** | `app/Views/partials/monthly-work-entries.php` |
| **Editor / summary assembly / PDF** | **Out of scope** — not implemented |
| **6 client blocks / exports / shares / PDF** | **Unchanged** (exports 4; shares 7; active 1 id 7; checksum prefix `a8c4d61c…`; PDF not regenerated) |
| **Next recommended stage** | **Work Entry Editor Implementation 01** (charter complete; operator click-through optional, not a blocker) |
| **Separate later** | Summary Assembly → Client Report Template Visual Alignment; optional Local Share QA Cleanup 01; screenshot QA when operator sends page shots |

---

## Work Entry Editor Charter 01 (2026-08-17)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — docs / UX / field contract / technical / safety charter only |
| **Closeout** | [REPORT-iseo-report-hub-work-entry-editor-charter-01.md](reports/REPORT-iseo-report-hub-work-entry-editor-charter-01.md) |
| **Scope** | [I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-SCOPE-v0.1.md) |
| **UX flows** | [I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-UX-FLOWS-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-UX-FLOWS-v0.1.md) |
| **Field contract** | [I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-FIELD-CONTRACT-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-FIELD-CONTRACT-v0.1.md) |
| **Technical charter** | [I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-TECHNICAL-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-TECHNICAL-CHARTER-v0.1.md) |
| **Safety policy** | [I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-SAFETY-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-SAFETY-POLICY-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-IMPLEMENTATION-PLAN-v0.1.md) |
| **MVP** | Embedded list CTAs on `/monthly-reports/{id}`; separate create/edit forms; no physical delete (`cancelled`/`deferred`); catalogue + manual entries; finalized report remains editable with PDF warning |
| **Code / runtime / DB / share / PDF** | **Unchanged** in this charter wave |
| **Next recommended stage** | **Work Entry Editor Implementation 01** |
| **Smoke mutation (impl)** | Option D default: +1 test entry then SQL-delete that row; final entries_r1 **7** |
| **Separate later** | Summary Assembly → Client Report Template Visual Alignment; screenshot QA when operator sends shots |

---

## Work Entry Editor Implementation 01 (2026-08-17)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `WORK ENTRY EDITOR PASS` |
| **Closeout** | [REPORT-iseo-report-hub-work-entry-editor-implementation-01.md](reports/REPORT-iseo-report-hub-work-entry-editor-implementation-01.md) |
| **Result** | [I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-IMPLEMENTATION-RESULT-v0.1.md) |
| **Routes** | GET/POST `/monthly-reports/{id}/work-entries[/create]`; GET/POST `/monthly-report-work-entries/{id}[/edit]`; **no DELETE** |
| **MVP** | Create + edit; catalogue or manual; soft remove via cancelled/deferred/internal; finalized warning |
| **Option D smoke** | Create test id 8 → update → SQL-delete test only → entries_r1 **7** |
| **Share / export / PDF** | **Unchanged** (exports 4; shares 7 active 1; checksum prefix `a8c4d61c6216e8d70b19`) |
| **Next recommended stage** | Operator manual work entry editor form click-through; then Summary Assembly |
| **Separate later** | Client Report Template Visual Alignment; screenshot QA when operator sends shots |

---

## Work Entry Editor Form UI Fix 01 (2026-08-17)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `WORK ENTRY FORM UI FIX PASS` |
| **Closeout** | [REPORT-iseo-report-hub-work-entry-editor-form-ui-fix-01.md](reports/REPORT-iseo-report-hub-work-entry-editor-form-ui-fix-01.md) |
| **Result** | [I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-FORM-UI-FIX-01-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-FORM-UI-FIX-01-RESULT-v0.1.md) |
| **Issue** | Operator screenshot: create/edit fields had insufficient border/contrast against white card |
| **Fix** | CSS borders `#cbd5e1`; yellow focus `#facc15` + ring; textarea/select visibility; `form-grid` / `field` spacing |
| **Share / export / PDF / DB** | **Unchanged** (entries_r1 **7**; exports **4**; shares **7** active **1** revoked **6**) |
| **Next recommended stage** | Operator manual work entry editor form click-through; then Summary Assembly |
| **Separate later** | Client Report Template Visual Alignment; screenshot QA of all pages |

---

## Summary Assembly Charter 01 (2026-08-17)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `SUMMARY ASSEMBLY CHARTER COMPLETE` |
| **Closeout** | [REPORT-iseo-report-hub-summary-assembly-charter-01.md](reports/REPORT-iseo-report-hub-summary-assembly-charter-01.md) |
| **Baseline** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-CURRENT-BLOCK-BASELINE-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-CURRENT-BLOCK-BASELINE-v0.1.md) |
| **Source rules** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SOURCE-RULES-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SOURCE-RULES-v0.1.md) |
| **Mode options** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-MODE-OPTIONS-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-MODE-OPTIONS-v0.1.md) |
| **UX flow** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-UX-FLOW-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-UX-FLOW-v0.1.md) |
| **Technical charter** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-TECHNICAL-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-TECHNICAL-CHARTER-v0.1.md) |
| **Safety policy** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFETY-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFETY-POLICY-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-IMPLEMENTATION-PLAN-v0.1.md) |
| **Recommended mode** | **Option A — preview-only** (`GET /monthly-reports/{id}/assembly-preview`); no `report_blocks` writes |
| **Mapping** | `work_completed` / `next_month_plan` / `risks_and_blockers` from entries; `executive_summary` / `results_summary` / `key_findings` manual |
| **Code / runtime / DB / share / PDF** | **Unchanged** in this charter wave |
| **Next recommended stage** | Operator manual summary assembly preview click-through |
| **Separate later** | Summary Assembly Apply Charter 01 → Client Report Template Visual Alignment; screenshot QA when operator sends shots |

---

## Summary Assembly Preview Implementation 01 (2026-08-17)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `SUMMARY ASSEMBLY PREVIEW PASS` |
| **Closeout** | [REPORT-iseo-report-hub-summary-assembly-preview-implementation-01.md](reports/REPORT-iseo-report-hub-summary-assembly-preview-implementation-01.md) |
| **Result** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-PREVIEW-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-PREVIEW-IMPLEMENTATION-RESULT-v0.1.md) |
| **Route** | `GET /monthly-reports/{id}/assembly-preview` — **no POST** |
| **Mapping** | `work_completed` **4** / `next_month_plan` **2** / `risks_and_blockers` **1**; manual `executive_summary` / `results_summary` / `key_findings` |
| **Share / export / PDF / DB** | **Unchanged** (entries_r1 **7**; blocks **6**; exports **4**; shares **7** active **1** revoked **6**; checksum prefix `a8c4d61c6216e8d70b19`) |
| **Next recommended stage** | Summary Assembly Apply Implementation 01 (after this apply charter) |
| **Separate later** | Client Report Template Visual Alignment; screenshot QA when operator sends shots |

---

## Summary Assembly Apply Charter 01 (2026-08-17)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `SUMMARY ASSEMBLY APPLY CHARTER COMPLETE` |
| **Closeout** | [REPORT-iseo-report-hub-summary-assembly-apply-charter-01.md](reports/REPORT-iseo-report-hub-summary-assembly-apply-charter-01.md) |
| **Scope** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-SCOPE-v0.1.md) |
| **Finalized policy** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-FINALIZED-REPORT-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-FINALIZED-REPORT-POLICY-v0.1.md) |
| **Block text contract** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-BLOCK-TEXT-CONTRACT-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-BLOCK-TEXT-CONTRACT-v0.1.md) |
| **Apply UX** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-UX-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-UX-v0.1.md) |
| **Technical charter** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-TECHNICAL-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-TECHNICAL-CHARTER-v0.1.md) |
| **Test strategy** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-TEST-STRATEGY-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-TEST-STRATEGY-v0.1.md) |
| **Safety policy** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-SAFETY-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-SAFETY-POLICY-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-IMPLEMENTATION-PLAN-v0.1.md) |
| **Writable keys** | `work_completed` / `next_month_plan` / `risks_and_blockers` (per-block + confirm); manual keys excluded |
| **Report 1** | Apply **disabled** (finalized + issued snapshot/export/share); no reopen in next impl |
| **Code / runtime / DB / share / PDF** | **Unchanged** in this charter wave (read-only SELECT probe only) |
| **Next recommended stage** | Summary Assembly Apply Implementation 01 |
| **Separate later** | Client Report Template Visual Alignment; screenshot QA when operator sends shots; fixture seed only if write-proof required |

---

## Summary Assembly Apply Implementation 01 (2026-08-17)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `SUMMARY ASSEMBLY APPLY PASS_WITH_LIMITED_WRITE_PROOF` |
| **Closeout** | [REPORT-iseo-report-hub-summary-assembly-apply-implementation-01.md](reports/REPORT-iseo-report-hub-summary-assembly-apply-implementation-01.md) |
| **Result** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-IMPLEMENTATION-RESULT-v0.1.md) |
| **Route** | `POST /monthly-reports/{id}/assembly-apply` + disabled apply UI on GET preview |
| **Report 1** | Apply controls **disabled**; POST **302** refuse; no block/PDF/share/export mutation |
| **Write proof** | **No** — id 1 finalized; id 5 draft with 0 blocks / 0 entries; no safe target |
| **Share / export / PDF / DB** | **Unchanged** (entries_r1 **7**; blocks **6**; exports **4**; shares **7** active **1** revoked **6**; checksum prefix `a8c4d61c6216e8d70b19`) |
| **Next recommended stage** | Summary Assembly Safe Fixture Charter 01 |
| **Separate later** | Client Report Template Visual Alignment; screenshot QA when operator sends shots; metrics model |

---

## Summary Assembly Safe Fixture Charter 01 (2026-08-17)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `SUMMARY ASSEMBLY SAFE FIXTURE CHARTER COMPLETE` |
| **Closeout** | [REPORT-iseo-report-hub-summary-assembly-safe-fixture-charter-01.md](reports/REPORT-iseo-report-hub-summary-assembly-safe-fixture-charter-01.md) |
| **Scope** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-SCOPE-v0.1.md) |
| **Data model** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-DATA-MODEL-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-DATA-MODEL-v0.1.md) |
| **Creation / cleanup** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-CREATION-CLEANUP-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-CREATION-CLEANUP-v0.1.md) |
| **Write proof** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-WRITE-PROOF-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-WRITE-PROOF-v0.1.md) |
| **Safety policy** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-SAFETY-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-SAFETY-POLICY-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md) |
| **Option** | **D** — dedicated marked local fixture; not id 1; not id 5; rows temporary |
| **Write target** | apply `next_month_plan` only on the fixture monthly |
| **Code / runtime / DB / share / PDF** | **Unchanged** in this charter wave (read-only SELECT probe only) |
| **Next recommended stage** | Summary Assembly Safe Fixture Implementation 01 |
| **Separate later** | Client Report Template Visual Alignment; screenshot QA when operator sends shots; metrics model; multi-block apply proof |

---

## Summary Assembly Safe Fixture Implementation 01 (2026-08-17)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `SUMMARY ASSEMBLY SAFE FIXTURE PASS` |
| **Closeout** | [REPORT-iseo-report-hub-summary-assembly-safe-fixture-implementation-01.md](reports/REPORT-iseo-report-hub-summary-assembly-safe-fixture-implementation-01.md) |
| **Result** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-IMPLEMENTATION-RESULT-v0.1.md) |
| **Tool** | `app-source/tools/summary-assembly-safe-fixture.php` (`--create` / `--cleanup` / `--confirm-local-fixture`) |
| **Write proof** | fixture monthly id **6** / period **4** `2099-01`; POST apply `next_month_plan` only; body matched Block Text Contract |
| **Cleanup** | exact ids + marker; fixture rows gone; core counts restored |
| **Report 1 / 5** | **unchanged** / **untouched** |
| **Share / export / PDF** | **Unchanged** (exports **4**; shares **7** active **1** revoked **6**; checksum prefix `a8c4d61c6216e8d70b19`) |
| **Residual** | `audit_log` 54→56; AUTO_INCREMENT gaps |
| **Next recommended stage** | Operator manual summary apply UI click-through |
| **Separate later** | Client Report Template Visual Alignment; screenshot QA when operator sends shots; metrics model; multi-block apply proof |

---

## Summary Assembly Apply UI Cleanup 01 (2026-08-17)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `SUMMARY ASSEMBLY APPLY UI CLEANUP PASS` |
| **Closeout** | [REPORT-iseo-report-hub-summary-assembly-apply-ui-cleanup-01.md](reports/REPORT-iseo-report-hub-summary-assembly-apply-ui-cleanup-01.md) |
| **Result** | [I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-UI-CLEANUP-01-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-UI-CLEANUP-01-RESULT-v0.1.md) |
| **Operator issue** | Screenshot of `/monthly-reports/1/assembly-preview`: apply lock correct, page too engineering/red, fixture markers too visible |
| **UI** | One amber finalized banner; draft primary; current/source `<details>` collapsed; muted locked apply panel |
| **Apply logic** | **Unchanged** — report 1 POST still refuses; no working form |
| **Report 1 / 5** | **unchanged** / **untouched** |
| **Share / export / PDF** | **Unchanged** (exports **4**; shares **7** active **1** revoked **6**; checksum prefix `a8c4d61c6216e8d70b19`) |
| **Next recommended stage** | Client Report Template Visual Alignment Implementation 01 |
| **Separate later** | Screenshot QA when operator sends shots; metrics model; optional non-finalized apply click-through |

---

## Client Report Template Visual Alignment Charter 01 (2026-08-17)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `CLIENT REPORT VISUAL CHARTER COMPLETE` |
| **Closeout** | [REPORT-iseo-report-hub-client-report-template-visual-alignment-charter-01.md](reports/REPORT-iseo-report-hub-client-report-template-visual-alignment-charter-01.md) |
| **Audit** | [I-SEO-REPORT-HUB-CLIENT-REPORT-SURFACE-AUDIT-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-SURFACE-AUDIT-v0.1.md) |
| **Target IA** | [I-SEO-REPORT-HUB-CLIENT-REPORT-TARGET-IA-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-TARGET-IA-v0.1.md) |
| **Visual** | [I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-DIRECTION-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-DIRECTION-v0.1.md) |
| **Architecture** | [I-SEO-REPORT-HUB-CLIENT-REPORT-TEMPLATE-ARCHITECTURE-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-TEMPLATE-ARCHITECTURE-v0.1.md) — Option B |
| **Safety** | [I-SEO-REPORT-HUB-CLIENT-REPORT-PDF-EXPORT-SHARE-SAFETY-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-PDF-EXPORT-SHARE-SAFETY-v0.1.md) |
| **Sequence** | [I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-IMPLEMENTATION-SEQUENCE-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-IMPLEMENTATION-SEQUENCE-v0.1.md) |
| **Acceptance** | [I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-ACCEPTANCE-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-ACCEPTANCE-v0.1.md) |
| **Decision** | Dedicated client document template; first apply to `/monthly-reports/{id}/preview`; public share stays PDF stream of export **4** |
| **Code / runtime / DB** | **None** in this charter |
| **Share / export / PDF** | **Unchanged** (exports **4**; checksum prefix `a8c4d61c6216e8d70b19`) |
| **Next recommended stage** | Client Report Template Visual Alignment Implementation 01 |
| **Separate later** | Export HTML alignment; PDF Regeneration Proof 01 (new export id); screenshot QA all pages |

---

## Client Report Template Visual Alignment Implementation 01 (2026-08-17)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `CLIENT REPORT PREVIEW TEMPLATE PASS` |
| **Closeout** | [REPORT-iseo-report-hub-client-report-template-visual-alignment-implementation-01.md](reports/REPORT-iseo-report-hub-client-report-template-visual-alignment-implementation-01.md) |
| **Result** | [I-SEO-REPORT-HUB-CLIENT-REPORT-TEMPLATE-VISUAL-ALIGNMENT-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-TEMPLATE-VISUAL-ALIGNMENT-IMPLEMENTATION-RESULT-v0.1.md) |
| **Route** | `GET /monthly-reports/{id}/preview` (+ print twin) uses dedicated client document |
| **Template** | `layout-client-report.php` + `partials/client-report/document.php` + `client-report.css` |
| **IA** | cover → резюме → результаты → что сделали → выводы → риски → план → footer |
| **Admin chrome** | Removed from this route (sidebar / edit / apply / keys / checksums) |
| **Code / runtime** | Preview views/CSS/mapper synced source → runtime |
| **DB / report 1 / 5** | **Unchanged** |
| **Share / export / PDF** | **Unchanged** (exports **4**; shares **7** active **1** revoked **6**; checksum prefix `a8c4d61c6216e8d70b19`; size 117055) |
| **Renderer** | `ReportTemplateRenderer` **untouched** |
| **Next recommended stage** | Operator manual client report preview click-through |
| **Separate later** | Export HTML alignment; PDF Regeneration Proof 01 (new export id); metrics model; screenshot QA all pages |

---

## Client Report Export HTML Alignment Charter 01 (2026-08-20)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `CLIENT REPORT EXPORT HTML CHARTER COMPLETE` |
| **Closeout** | [REPORT-iseo-report-hub-client-report-export-html-alignment-charter-01.md](reports/REPORT-iseo-report-hub-client-report-export-html-alignment-charter-01.md) |
| **Pipeline audit** | [I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-PIPELINE-AUDIT-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-PIPELINE-AUDIT-v0.1.md) |
| **Options** | [I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-ALIGNMENT-OPTIONS-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-ALIGNMENT-OPTIONS-v0.1.md) — **Option B** recommended |
| **Impl scope** | [I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-HTML-IMPLEMENTATION-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-HTML-IMPLEMENTATION-SCOPE-v0.1.md) |
| **CSS/PDF safety** | [I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-DATA-CSS-PDF-SAFETY-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-DATA-CSS-PDF-SAFETY-v0.1.md) |
| **Immutability** | [I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-IMMUTABILITY-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-IMMUTABILITY-POLICY-v0.1.md) |
| **Acceptance** | [I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-HTML-ACCEPTANCE-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-HTML-ACCEPTANCE-v0.1.md) |
| **Sequence** | [I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-SEQUENCE-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-SEQUENCE-v0.1.md) |
| **Code / runtime / DB** | **Unchanged** (docs only) |
| **Share / export / PDF** | **Unchanged** — export **4** frozen |
| **Next recommended stage** | **Client Report Export HTML Alignment Implementation 01** — **parked** until after UI polish + operator confirm |
| **Separate later** | PDF Regeneration Proof 01 (new export id); Share Handoff Update 01; metrics model |

---

## Screenshot QA Fix Charter 01 (2026-08-21)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `SCREENSHOT QA FIX CHARTER COMPLETE` |
| **Evidence** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\automated-screenshot-capture-01\20260821-010501` (16 PNG) |
| **Findings** | [I-SEO-REPORT-HUB-SCREENSHOT-QA-FINDINGS-v0.1.md](product/I-SEO-REPORT-HUB-SCREENSHOT-QA-FINDINGS-v0.1.md) |
| **P0 strategy** | [I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-FIX-STRATEGY-v0.1.md](product/I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-FIX-STRATEGY-v0.1.md) |
| **Impl scope** | [I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-IMPLEMENTATION-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-IMPLEMENTATION-SCOPE-v0.1.md) |
| **Safety / acceptance** | [I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-SAFETY-ACCEPTANCE-v0.1.md](product/I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-SAFETY-ACCEPTANCE-v0.1.md) |
| **Triage result** | [I-SEO-REPORT-HUB-SCREENSHOT-QA-TRIAGE-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-SCREENSHOT-QA-TRIAGE-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-screenshot-qa-fix-charter-01.md](reports/REPORT-iseo-report-hub-screenshot-qa-fix-charter-01.md) |
| **Code / runtime / DB** | **Unchanged** (docs only) |
| **Share / export / PDF** | **Unchanged** — export **4** frozen; PDF deferred |
| **Next recommended stage** | Superseded by **Screenshot QA P0 Fix Implementation 01** (complete) |
| **Parked** | Export HTML Alignment Implementation; PDF regen; mobile QA; report 5 deeper DB cleanup |

---

## Screenshot QA P0 Fix Implementation 01 (2026-08-21)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `SCREENSHOT QA P0 FIX PASS_WITH_MINOR_ISSUES` |
| **Result** | [I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-FIX-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-FIX-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-screenshot-qa-p0-fix-implementation-01.md](reports/REPORT-iseo-report-hub-screenshot-qa-p0-fix-implementation-01.md) |
| **Before evidence** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\automated-screenshot-capture-01\20260821-010501` |
| **After evidence** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\screenshot-qa-p0-fix-implementation-01\20260821-023143` |
| **Code / runtime** | app-source P0 views/helpers/CSS + exact runtime sync |
| **DB / export / share / PDF** | **Unchanged** (no mutation) |
| **Next recommended stage** | Superseded by **Monthly Report Detail UX Collapse Charter 01** (complete) |
| **Parked** | Export HTML Alignment Implementation; PDF regen; mobile QA; report 5 deeper DB cleanup |

---

## Monthly Report Detail UX Collapse Charter 01 (2026-08-21)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `MONTHLY DETAIL UX COLLAPSE CHARTER COMPLETE` |
| **Findings** | [I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-FINDINGS-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-FINDINGS-v0.1.md) |
| **Target IA** | [I-SEO-REPORT-HUB-MONTHLY-DETAIL-TARGET-IA-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-TARGET-IA-v0.1.md) |
| **Collapse policy** | [I-SEO-REPORT-HUB-MONTHLY-DETAIL-COLLAPSE-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-COLLAPSE-POLICY-v0.1.md) |
| **Action safety UX** | [I-SEO-REPORT-HUB-MONTHLY-DETAIL-ACTION-SAFETY-UX-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-ACTION-SAFETY-UX-v0.1.md) |
| **Implementation scope** | [I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-COLLAPSE-IMPLEMENTATION-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-COLLAPSE-IMPLEMENTATION-SCOPE-v0.1.md) |
| **Acceptance** | [I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-COLLAPSE-ACCEPTANCE-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-COLLAPSE-ACCEPTANCE-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-monthly-report-detail-ux-collapse-charter-01.md](reports/REPORT-iseo-report-hub-monthly-report-detail-ux-collapse-charter-01.md) |
| **Evidence** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\screenshot-qa-p0-fix-implementation-01\20260821-023143\04_monthly_report_1_detail_after.png` |
| **Code / runtime / DB** | **Unchanged** (docs-only charter) |
| **Next recommended stage** | **Monthly Report Detail UX Collapse Implementation 01** *(done — see Implementation 01 below)* |
| **Parked** | Export HTML Alignment Implementation; PDF regen; export 4 / share mutation |

---

## Monthly Report Detail UX Collapse Implementation 01 (2026-08-21)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `MONTHLY DETAIL UX COLLAPSE PASS` |
| **Result** | [I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-COLLAPSE-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-COLLAPSE-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-monthly-report-detail-ux-collapse-implementation-01.md](reports/REPORT-iseo-report-hub-monthly-report-detail-ux-collapse-implementation-01.md) |
| **Before evidence** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\screenshot-qa-p0-fix-implementation-01\20260821-023143\04_monthly_report_1_detail_after.png` |
| **After evidence** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\monthly-report-detail-ux-collapse-implementation-01\20260821-033238` |
| **Runtime sync** | Exact allowlist: `show.php`, `monthly-work-entries.php`, `MonthlyReportContentController.php`, `app.css` |
| **DB / export / share / PDF** | **Unchanged** (export 4 size `117055`, checksum prefix `a8c4d61c6216`) |
| **Next recommended stage** | Superseded by **Report 5 Draft Path Cleanup Charter 01** (complete) |
| **Parked** | Export HTML Alignment Implementation; PDF regen; export 4 / share mutation |

---

## Report 5 Draft Path Cleanup Charter 01 (2026-08-21)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `REPORT 5 DRAFT PATH CLEANUP CHARTER COMPLETE` |
| **Current-state audit** | [I-SEO-REPORT-HUB-REPORT-5-CURRENT-STATE-AUDIT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-5-CURRENT-STATE-AUDIT-v0.1.md) |
| **Product decision** | [I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-DECISION-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-DECISION-v0.1.md) |
| **Target empty draft UX** | [I-SEO-REPORT-HUB-REPORT-5-TARGET-EMPTY-DRAFT-UX-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-5-TARGET-EMPTY-DRAFT-UX-v0.1.md) |
| **Implementation scope** | [I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-CLEANUP-IMPLEMENTATION-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-CLEANUP-IMPLEMENTATION-SCOPE-v0.1.md) |
| **Safety / acceptance** | [I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-CLEANUP-SAFETY-ACCEPTANCE-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-CLEANUP-SAFETY-ACCEPTANCE-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-5-draft-path-cleanup-charter-01.md](reports/REPORT-iseo-report-hub-report-5-draft-path-cleanup-charter-01.md) |
| **Evidence** | P0 after preview `...\screenshot-qa-p0-fix-implementation-01\20260821-023143\15_monthly_report_5_preview_after.png`; pre-P0 empty/preview under `automated-screenshot-capture-01\20260821-010501`; local DB read-only: report 5 draft 0 blocks / 0 entries |
| **Code / runtime / DB** | **Unchanged** (docs-only charter) |
| **Decision** | Option **A + light demotion** — keep empty draft; demote in period UI; no seed/delete |
| **Next recommended stage** | **Report 5 Draft Path Cleanup + Health Refresh Implementation 01** (complete — see below) |
| **Parked** | Export HTML Alignment Implementation; PDF regen; export 4 / share mutation; Option C seed (separate data wave) |

---

## Report 5 Draft Path Cleanup + Health Refresh Implementation 01 (2026-08-21)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `REPORT 5 DRAFT PATH + HEALTH REFRESH PASS` |
| **Implementation result** | [I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-CLEANUP-HEALTH-REFRESH-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-CLEANUP-HEALTH-REFRESH-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-report-5-draft-path-cleanup-health-refresh-implementation-01.md](reports/REPORT-iseo-report-hub-report-5-draft-path-cleanup-health-refresh-implementation-01.md) |
| **After screenshots** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\report-5-draft-path-cleanup-health-refresh-implementation-01\20260821-041956` |
| **Code** | Empty-draft manager/period UX + health refresh (view/render + display-only flags) |
| **Runtime sync** | Exact allowlist only |
| **DB / export / share / PDF** | **Unchanged** (export 4 size/checksum unchanged) |
| **Next recommended stage** | Superseded by **Client Preview Show-ready Content Charter 01** (complete — see below) |
| **Parked** | Export HTML Alignment Implementation; PDF regen; export 4 / share mutation; Option C seed (separate data wave) |

---

## Client Preview Show-ready Content Charter 01 (2026-08-21)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `CLIENT PREVIEW SHOW-READY CONTENT CHARTER COMPLETE` |
| **Content audit** | [I-SEO-REPORT-HUB-CLIENT-PREVIEW-CONTENT-AUDIT-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-CONTENT-AUDIT-v0.1.md) |
| **Strategy** | [I-SEO-REPORT-HUB-CLIENT-PREVIEW-SHOW-READY-CONTENT-STRATEGY-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-SHOW-READY-CONTENT-STRATEGY-v0.1.md) — **Option A** (render-layer local demo fallback) |
| **Demo copy** | [I-SEO-REPORT-HUB-CLIENT-PREVIEW-REPORT-1-DEMO-COPY-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-REPORT-1-DEMO-COPY-v0.1.md) |
| **Implementation scope** | [I-SEO-REPORT-HUB-CLIENT-PREVIEW-SHOW-READY-CONTENT-IMPLEMENTATION-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-SHOW-READY-CONTENT-IMPLEMENTATION-SCOPE-v0.1.md) |
| **Safety / acceptance** | [I-SEO-REPORT-HUB-CLIENT-PREVIEW-SHOW-READY-CONTENT-SAFETY-ACCEPTANCE-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-SHOW-READY-CONTENT-SAFETY-ACCEPTANCE-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-client-preview-show-ready-content-charter-01.md](reports/REPORT-iseo-report-hub-client-preview-show-ready-content-charter-01.md) |
| **Code / runtime / DB** | **None** — docs charter only |
| **Next recommended stage** | Superseded by **Client Preview Show-ready Content Implementation 01** (complete — see below) |
| **Deferred** | Option B DB content update; Option C separate demo report; PDF/export/share mutation; fake KPIs |

---

## Client Preview Show-ready Content Implementation 01 (2026-08-21)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `CLIENT PREVIEW SHOW-READY CONTENT PASS` |
| **Result** | [I-SEO-REPORT-HUB-CLIENT-PREVIEW-SHOW-READY-CONTENT-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-SHOW-READY-CONTENT-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-client-preview-show-ready-content-implementation-01.md](reports/REPORT-iseo-report-hub-client-preview-show-ready-content-implementation-01.md) |
| **Approach** | Option A render-layer fallback; gate = local + report id 1 + not empty draft |
| **Runtime sync** | Exact: `ClientReportDocument.php`, `ReportPreviewController.php`, `routes.php` |
| **Evidence** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\client-preview-show-ready-content-implementation-01\20260821-121108` |
| **DB / export 4 / shares / PDF** | Unchanged |
| **Next recommended stage** | Superseded as primary next by **Pre-hosting Demo Scenario and Field Help Charter 01** (complete — see below); show-ready review remains accepted baseline |
| **Parked** | Option B/C; Export HTML Alignment Implementation; PDF regen; export 4 / share mutation |

---

## Pre-hosting Demo Scenario and Field Help Charter 01 (2026-08-21)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `PRE-HOSTING DEMO SCENARIO FIELD HELP CHARTER COMPLETE` |
| **Pre-hosting tech** | [I-SEO-REPORT-HUB-PREHOSTING-TECH-DECISION-v0.1.md](product/I-SEO-REPORT-HUB-PREHOSTING-TECH-DECISION-v0.1.md) — `reports.i-seo.su`, SSL done (operator), **PHP 8.3**, host checks; **no upload** |
| **Demo user plan** | [I-SEO-REPORT-HUB-DEMO-USER-TEST-PROVEROCHNOV-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-USER-TEST-PROVEROCHNOV-PLAN-v0.1.md) — `Тест Проверочнов` / email `test@reports.i-seo.local` / role **`seo_specialist`** |
| **Demo scenario** | [I-SEO-REPORT-HUB-REALISTIC-DEMO-SCENARIO-PROVERKA-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REALISTIC-DEMO-SCENARIO-PROVERKA-PLAN-v0.1.md) — literal `ПРОВЕРКА.рa` (mixed-script `р`+`a`); July complete + August in-progress |
| **Browser fill** | [I-SEO-REPORT-HUB-BROWSER-FILLING-STRATEGY-v0.1.md](product/I-SEO-REPORT-HUB-BROWSER-FILLING-STRATEGY-v0.1.md) — Firefox Developer `mars-research`; hybrid seed + UI fill |
| **Field help design** | [I-SEO-REPORT-HUB-FIELD-HELP-QUESTION-ICON-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-FIELD-HELP-QUESTION-ICON-DESIGN-v0.1.md) |
| **Field help copy** | [I-SEO-REPORT-HUB-FIELD-HELP-COPY-PACK-v0.1.md](product/I-SEO-REPORT-HUB-FIELD-HELP-COPY-PACK-v0.1.md) |
| **Sequence** | [I-SEO-REPORT-HUB-DEMO-SCENARIO-FIELD-HELP-IMPLEMENTATION-SEQUENCE-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-SCENARIO-FIELD-HELP-IMPLEMENTATION-SEQUENCE-v0.1.md) — Field Help Implementation 01 **done** |
| **Safety / acceptance** | [I-SEO-REPORT-HUB-PREHOSTING-DEMO-FIELD-HELP-SAFETY-ACCEPTANCE-v0.1.md](product/I-SEO-REPORT-HUB-PREHOSTING-DEMO-FIELD-HELP-SAFETY-ACCEPTANCE-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-prehosting-demo-scenario-field-help-charter-01.md](reports/REPORT-iseo-report-hub-prehosting-demo-scenario-field-help-charter-01.md) |
| **Code / runtime / DB** | **None** — docs charter only |
| **Next recommended stage** | Superseded by **Field Help Question Icon Implementation 01** (complete — see below) |
| **Deferred** | Demo seed / browser fill / host upload / PDF/export/share until later authorized waves |

---

## Field Help Question Icon Implementation 01 (2026-08-21)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `FIELD HELP QUESTION ICON PASS` |
| **Result** | [I-SEO-REPORT-HUB-FIELD-HELP-QUESTION-ICON-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-FIELD-HELP-QUESTION-ICON-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-field-help-question-icon-implementation-01.md](reports/REPORT-iseo-report-hub-field-help-question-icon-implementation-01.md) |
| **What shipped** | Static `FieldHelp` copy map + reusable `?` partial; wired into work entry, report block, monthly content forms; compact help on monthly detail content rows + assembly preview; CSS + minimal JS |
| **Runtime sync** | Exact allowlist to Laragon runtime (no `.env`/storage/export/PDF/vendor/DB) |
| **DB / export / share / PDF** | **Unchanged** |
| **Evidence** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\field-help-question-icon-implementation-01\20260821-130037\` (not in git) |
| **Next recommended stage** | Superseded by **Demo User and Scenario Seed Charter 01** (complete — see below) |
| **Deferred** | Demo user/scenario seed execution; browser fill; host upload |

---

## Demo User and Scenario Seed Charter 01 (2026-08-21)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `DEMO USER SCENARIO SEED CHARTER COMPLETE` |
| **Current-state audit** | [I-SEO-REPORT-HUB-DEMO-SEED-CURRENT-STATE-AUDIT-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-SEED-CURRENT-STATE-AUDIT-v0.1.md) |
| **Demo user seed spec** | [I-SEO-REPORT-HUB-DEMO-USER-SEED-SPEC-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-USER-SEED-SPEC-v0.1.md) — `Тест Проверочнов` / `test@reports.i-seo.local` / role **`seo_specialist`** |
| **Scenario data spec** | [I-SEO-REPORT-HUB-DEMO-SCENARIO-PROVERKA-DATA-SPEC-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-SCENARIO-PROVERKA-DATA-SPEC-v0.1.md) — literal `ПРОВЕРКА.рa`; July finalized (seed status, no export/share) + August `in_progress` |
| **Content pack** | [I-SEO-REPORT-HUB-DEMO-SCENARIO-PROVERKA-CONTENT-PACK-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-SCENARIO-PROVERKA-CONTENT-PACK-v0.1.md) |
| **Seed implementation plan** | [I-SEO-REPORT-HUB-DEMO-SCENARIO-SEED-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-SCENARIO-SEED-IMPLEMENTATION-PLAN-v0.1.md) — tool `demo-proverka-seed.php`; backup + local-only guard |
| **Browser fill follow-up** | [I-SEO-REPORT-HUB-DEMO-SCENARIO-BROWSER-FILL-FOLLOWUP-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-SCENARIO-BROWSER-FILL-FOLLOWUP-PLAN-v0.1.md) |
| **Safety / acceptance** | [I-SEO-REPORT-HUB-DEMO-SCENARIO-SEED-SAFETY-ACCEPTANCE-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-SCENARIO-SEED-SAFETY-ACCEPTANCE-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-demo-user-scenario-seed-charter-01.md](reports/REPORT-iseo-report-hub-demo-user-scenario-seed-charter-01.md) |
| **Code / runtime / DB** | **None** — docs charter only |
| **Next recommended stage** | **Demo User and Scenario Seed Implementation 01** (complete — see below) |
| **Then** | **Browser Filled Demo Report Pass 01** |
| **Deferred** | Host upload to `reports.i-seo.su`; PDF/export/share; combining seed + browser fill |

---

## Demo User and Scenario Seed Implementation 01 (2026-08-21)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `DEMO USER SCENARIO SEED PASS` |
| **Seed tool** | `app-source/tools/demo-proverka-seed.php` (`--status` / `--create` / `--cleanup`; guard `--confirm-local-demo-seed`) |
| **Demo user** | `Тест Проверочнов` / `test@mail.ru` / role **`seo_specialist`** / active (password operator-approved local demo `test`; **hash not printed**) |
| **Scenario** | Client/project/site `ПРОВЕРКА.рa` / slug `proverka-demo` / marker `MARS_DEMO_PROVERKA_20260821`; July monthly **7** finalized (DB status only); August monthly **8** `in_progress` |
| **Result doc** | [I-SEO-REPORT-HUB-DEMO-USER-SCENARIO-SEED-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-USER-SCENARIO-SEED-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-demo-user-scenario-seed-implementation-01.md](reports/REPORT-iseo-report-hub-demo-user-scenario-seed-implementation-01.md) |
| **Backup** | Storage `...\demo-user-scenario-seed-implementation-01\backup\iseo_report_hub_dev-before-demo-proverka-seed-20260821-134512.sql` |
| **Evidence** | Storage `...\demo-user-scenario-seed-implementation-01\20260821-134512\` (IDs JSON + screenshots; **not** in git) |
| **Safety** | Report 1/5 unchanged; export/share/snapshot/PDF unchanged; no host upload |
| **Next recommended stage** | Superseded by **Demo Scenario Cleanup and UI Polish Fix 01** (complete — see below) |
| **Deferred** | Host upload to `reports.i-seo.su`; PDF/export/share generation for demo reports |

---

## Demo Scenario Cleanup and UI Polish Fix 01 (2026-08-21)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `DEMO SCENARIO CLEANUP UI POLISH PASS` |
| **Result doc** | [I-SEO-REPORT-HUB-DEMO-SCENARIO-CLEANUP-UI-POLISH-FIX-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-SCENARIO-CLEANUP-UI-POLISH-FIX-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-demo-scenario-cleanup-ui-polish-fix-01.md](reports/REPORT-iseo-report-hub-demo-scenario-cleanup-ui-polish-fix-01.md) |
| **Demo display** | Client/project/site `ПРОВЕРКА.рф`; July monthly **7** finalized; August monthly **8** `in_progress`; marker unchanged |
| **Removed** | Old Demo Client path (reports **1**/**5** + related periods/blocks/entries/snapshots/exports/shares + proven export files) |
| **UI** | Unicode name decode; demo-aware dashboard; periods nowrap + Russian statuses/roles |
| **Host / PDF** | **No** upload; **no** new export/share/PDF |
| **Next recommended stage** | Superseded for hosting track by **Pre-hosting Deployment Readiness 01** (below); product UX may still use **Browser Filled Demo Report Pass 01** |
| **Deferred** | Host upload; PDF/export/share for `ПРОВЕРКА.рф` |

---

## Pre-hosting Deployment Readiness 01 (2026-08-21)

| Field | Value |
|-------|-------|
| **Status** | **Complete with ATTENTION** — `PREHOSTING DEPLOYMENT READINESS ATTENTION` |
| **Operator pack** | [I-SEO-REPORT-HUB-PREHOSTING-DEPLOYMENT-READINESS-v0.1.md](product/I-SEO-REPORT-HUB-PREHOSTING-DEPLOYMENT-READINESS-v0.1.md) |
| **File map** | [I-SEO-REPORT-HUB-PREHOSTING-FILE-PACKAGE-MAP-v0.1.md](product/I-SEO-REPORT-HUB-PREHOSTING-FILE-PACKAGE-MAP-v0.1.md) |
| **DB URL/path audit** | [I-SEO-REPORT-HUB-PREHOSTING-DB-URL-PATH-AUDIT-v0.1.md](product/I-SEO-REPORT-HUB-PREHOSTING-DB-URL-PATH-AUDIT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-prehosting-deployment-readiness-01.md](reports/REPORT-iseo-report-hub-prehosting-deployment-readiness-01.md) |
| **Copy from** | `app-source` (not full runtime; exclude `tools/`, local `.env.local`) |
| **Document root** | `public` |
| **PHP** | 8.3 + pdo_mysql / mbstring / json / openssl / fileinfo / session |
| **Env file on host** | **`.env.local`** (`APP_URL=https://reports.i-seo.su`; host DB_*) |
| **DB URL replace (WP-style)** | **Not needed** |
| **ATTENTION** | No `public/.htaccess` in source — operator must add rewrite on host |
| **Host upload** | **Not performed** in this wave |
| **Next recommended stage** | Superseded for unblock by **Host DB Guard Fix 01** (below); then continue **Operator Manual Hosting Upload** / re-upload |

---

## Host DB Guard Fix 01 (2026-08-21)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `HOST DB GUARD FIX PASS` |
| **Symptom** | Host internal pages: `REFUSED: target DB must be exactly "iseo_report_hub_dev"` from `DatabaseService.php` |
| **Root cause** | Local-only exact DB name guard ran in shared web services |
| **Fix** | Guard is opt-in via `enableLocalDevDatabaseGuard()`; enforced only with `APP_ENV=local` + exact `iseo_report_hub_dev`; CLI tools enable explicitly |
| **Closeout** | [REPORT-iseo-report-hub-host-db-guard-fix-01.md](reports/REPORT-iseo-report-hub-host-db-guard-fix-01.md) |
| **Operator re-upload** | `app/Services/DatabaseService.php` only (critical); do not upload `tools/` |
| **Host env reminder** | `APP_DEBUG=false`; host `DB_DATABASE` allowed |
| **Host upload by agent** | **Not performed** |
| **DB mutation** | **None** |
| **Next recommended stage** | Operator re-upload fixed file + smoke host pages; then finish hosting rollout |
| **Optional fix charter** | Pre-hosting Readiness Fix 01 (`.htaccess` in source + HTTPS cookie_secure) |

---

## Full Local System Status Audit 01 (2026-08-24)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `FULL LOCAL SYSTEM STATUS AUDIT ATTENTION` |
| **Type** | audit / intake / planning — **no** code/DB/runtime/host mutation |
| **Status doc** | [I-SEO-REPORT-HUB-FULL-LOCAL-SYSTEM-STATUS-v0.1.md](product/I-SEO-REPORT-HUB-FULL-LOCAL-SYSTEM-STATUS-v0.1.md) |
| **Roadmap** | [I-SEO-REPORT-HUB-LOCAL-ROADMAP-AFTER-HOST-DEMO-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-ROADMAP-AFTER-HOST-DEMO-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-full-local-system-status-audit-01.md](reports/REPORT-iseo-report-hub-full-local-system-status-audit-01.md) |
| **Local** | `/health` `/login` auth demo routes 200; DB demo counts match cleanup baseline (blocks 12 / WE 22 / exports 0) |
| **Host** | operator: demo works after `DatabaseService.php` re-upload; audit public GET 403/404 — SAFE UNKNOWN |
| **Evidence (Storage, not Git)** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\full-local-system-status-audit-01\20260824-124948\` |
| **Next recommended stage** | **Pre-hosting Readiness Fix 01** (source `.htaccess`) then **Production Config Normalization 01** / **Browser Filled Demo Report Pass 01** |

---

## Pre-hosting Readiness Fix 01 (2026-08-24)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `PREHOSTING READINESS FIX PASS` |
| **Source fix** | `app-source/public/.htaccess` — `DirectoryIndex`, `Options -Indexes`, safe front-controller rewrite |
| **Runtime sync** | exact file only: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\public\.htaccess` |
| **Result** | [I-SEO-REPORT-HUB-PREHOSTING-READINESS-FIX-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-PREHOSTING-READINESS-FIX-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-prehosting-readiness-fix-01.md](reports/REPORT-iseo-report-hub-prehosting-readiness-fix-01.md) |
| **Validation** | source/runtime SHA-256 match; local public + authenticated GET smoke PASS; DB counts unchanged; exports/shares/PDF unchanged |
| **Host action** | no upload in wave; if document root = `public`, operator may upload exact source file to host `public/.htaccess` |
| **Evidence (Storage, not Git)** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\prehosting-readiness-fix-01\20260824-140349\` |
| **Next recommended stage** | **Production Config Normalization 01** (hosting track paused) or product UX after Browser Filled Demo |

---

## Browser Demo UX Fix Implementation 01 (2026-08-24)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `BROWSER DEMO UX FIX PASS` |
| **Trigger** | Browser Filled Demo Report Pass 01 issues (stale nav, finalized edit cues, broad specialist access, overloaded August detail, technical block form) |
| **Result** | [I-SEO-REPORT-HUB-BROWSER-DEMO-UX-FIX-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-BROWSER-DEMO-UX-FIX-IMPLEMENTATION-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-browser-demo-ux-fix-implementation-01.md](reports/REPORT-iseo-report-hub-browser-demo-ux-fix-implementation-01.md) |
| **Validation** | PHP lint PASS; specialist HTTP assertions PASS; screenshots + DB before/after under Storage evidence; exports/shares/snapshots remain 0 |
| **Host / PDF** | not touched |
| **Evidence (Storage, not Git)** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\browser-demo-ux-fix-implementation-01\20260824-153712\` |
| **Next recommended stage** | **Browser Demo UX Fix Review Pass 01** |

---

## Browser Demo UX Fix Review Pass 01 (2026-08-24)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `BROWSER DEMO UX FIX REVIEW PASS_WITH_RESIDUALS` |
| **Trigger** | Verify specialist demo UX after Browser Demo UX Fix Implementation 01 |
| **Result** | [I-SEO-REPORT-HUB-BROWSER-DEMO-UX-FIX-REVIEW-PASS-v0.1.md](product/I-SEO-REPORT-HUB-BROWSER-DEMO-UX-FIX-REVIEW-PASS-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-browser-demo-ux-fix-review-pass-01.md](reports/REPORT-iseo-report-hub-browser-demo-ux-fix-review-pass-01.md) |
| **Validation** | 12 full-page screenshots @1920; route-status + assertions PASS (1 keyword false-negative visually overridden); DB content unchanged except audit_log +1; exports/shares/snapshots remain 0 |
| **Host / PDF** | not touched |
| **Evidence (Storage, not Git)** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\browser-demo-ux-fix-review-pass-01\20260824-161254\` |
| **Next recommended stage** | **Web-GPT Visual Review of UX Fix Screenshots** |

---

## Access Denied and Work Entry UX Polish 01 (2026-08-26)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `ACCESS DENIED WORK ENTRY UX POLISH PASS` |
| **Trigger** | Web-GPT visual review ACCEPTED_WITH_P2_RESIDUALS after Browser Demo UX Fix Review Pass 01 |
| **Result** | [I-SEO-REPORT-HUB-ACCESS-DENIED-WORK-ENTRY-UX-POLISH-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-ACCESS-DENIED-WORK-ENTRY-UX-POLISH-RESULT-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-access-denied-work-entry-ux-polish-01.md](reports/REPORT-iseo-report-hub-access-denied-work-entry-ux-polish-01.md) |
| **Validation** | PHP lint PASS; specialist HTTP + 87 assertions PASS; 7 screenshots @1920; DB content unchanged except audit_log; exports/shares/snapshots remain 0 |
| **Host / PDF** | not touched |
| **Evidence (Storage, not Git)** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\access-denied-work-entry-ux-polish-01\20260826-204445\` |
| **Next recommended stage** | **Work Entry Form UX Review Pass 01** — **completed** (see section below) |

---

## Work Entry Form UX Review Pass 01 (2026-08-26)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — `WORK ENTRY FORM UX REVIEW PASS_WITH_RESIDUALS` |
| **Trigger** | After Access Denied and Work Entry UX Polish 01 — density / first-glance review before optional Polish 02 |
| **Result** | [I-SEO-REPORT-HUB-WORK-ENTRY-FORM-UX-REVIEW-PASS-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-FORM-UX-REVIEW-PASS-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-work-entry-form-ux-review-pass-01.md](reports/REPORT-iseo-report-hub-work-entry-form-ux-review-pass-01.md) |
| **Validation** | Local Edge screenshots @1920 (+ optional 1366); form assertions PASS with P2 help-density soft-fail; DB content unchanged except audit_log +1; work entries 23 / July 12 / August 11; exports/shares/snapshots 0 |
| **Host / PDF / code** | not touched — review-only wave |
| **Evidence (Storage, not Git)** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\work-entry-form-ux-review-pass-01\20260826-210243\` |
| **Next recommended stage** | **Web-GPT Visual Review of Work Entry Form Screenshots**; optional **Work Entry Form UX Polish 02** if density confirmed |

---

## Storage Hygiene Loss Audit 01 (2026-08-31)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — verdict `SAFE` |
| **Closeout** | [REPORT-iseo-report-hub-storage-hygiene-loss-audit-01.md](reports/REPORT-iseo-report-hub-storage-hygiene-loss-audit-01.md) |
| **Scope** | Read-only forensic triage after broad deletion of temporary STORAGE `git-sync-*` / `git-reconcile-*` contours |
| **Result** | No confirmed loss of unpromoted i-SEO commits, docs, app-source, or listed `incoming\` evidence; canonical `projects/iseo-report-hub/` tree identical to `recovery/pre-reanchor-20260831-01` tip |
| **Restore** | **not needed** |
| **Normal work** | **may continue** — next product prompt when operator authorizes |
| **Mutations** | docs-only audit report + this index; no app-source / runtime / DB / host / cleanup / restore |

---

## Project-Centric Dashboard and IA Charter 01 (2026-08-31)

| Field | Value |
|-------|-------|
| **Status** | **Complete** — docs/charter only |
| **Charter** | [I-SEO-REPORT-HUB-PROJECT-CENTRIC-DASHBOARD-IA-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-PROJECT-CENTRIC-DASHBOARD-IA-CHARTER-v0.1.md) |
| **Implementation plan** | [I-SEO-REPORT-HUB-PROJECT-CENTRIC-DASHBOARD-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-PROJECT-CENTRIC-DASHBOARD-IMPLEMENTATION-PLAN-v0.1.md) |
| **Closeout** | [REPORT-iseo-report-hub-project-centric-dashboard-ia-charter-01.md](reports/REPORT-iseo-report-hub-project-centric-dashboard-ia-charter-01.md) |
| **Operator decision** | Current `/` demo blocks (`Рабочий контур`, `Быстрые действия`, `Статус локальной системы`) **rejected**; future home = **project dashboard** |
| **IA direction** | `Projects → Project Detail → Project Reports → Work Entries / Texts / Preview / Future Evidence` |
| **Approved sequence** | Dashboard Impl 01 → Project Detail Impl 01 → Project Creation Draft → Curator Notes/Alerts Charter → Evidence Links |
| **Not done in this wave** | No app-source / runtime / DB / host / PDF / export / share / evidence implementation |
| **Next recommended stage** | **Project Dashboard Implementation 01** |

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
| 215 | [product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md) | Report delivery / public share charter |
| 216 | [product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DESIGN-v0.1.md) | Public share design (lifecycle / routes / UI) |
| 217 | [product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-SECURITY-MODEL-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-SECURITY-MODEL-v0.1.md) | Public share security model |
| 218 | [product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-PLAN-v0.1.md) | Public share implementation plan (DB-10 then impl) |
| 219 | [product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VALIDATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VALIDATION-PLAN-v0.1.md) | Public share validation plan |
| 220 | [reports/REPORT-iseo-report-hub-report-delivery-public-share-charter-01.md](reports/REPORT-iseo-report-hub-report-delivery-public-share-charter-01.md) | Public share charter closeout |
| 221 | [product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DB10-MIGRATION-APPLY-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DB10-MIGRATION-APPLY-RESULT-v0.1.md) | DB-10 public share migration apply result |
| 222 | [reports/REPORT-iseo-report-hub-report-delivery-public-share-db10-migration-apply-01.md](reports/REPORT-iseo-report-hub-report-delivery-public-share-db10-migration-apply-01.md) | DB-10 public share migration apply closeout |
| 223 | [product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-RESULT-v0.1.md) | Public share implementation result |
| 224 | [reports/REPORT-iseo-report-hub-report-delivery-public-share-implementation-01.md](reports/REPORT-iseo-report-hub-report-delivery-public-share-implementation-01.md) | Public share implementation closeout |
| 225 | [product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-HARDENING-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-HARDENING-RESULT-v0.1.md) | Public share hardening result |
| 226 | [reports/REPORT-iseo-report-hub-report-delivery-public-share-hardening-01.md](reports/REPORT-iseo-report-hub-report-delivery-public-share-hardening-01.md) | Public share hardening closeout |
| 227 | [product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VISUAL-QA-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VISUAL-QA-RESULT-v0.1.md) | Public share Visual QA result |
| 228 | [reports/REPORT-iseo-report-hub-report-delivery-public-share-visual-qa-01.md](reports/REPORT-iseo-report-hub-report-delivery-public-share-visual-qa-01.md) | Public share Visual QA closeout |
| 229 | [product/I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-IMPLEMENTATION-RESULT-v0.1.md) | Client handoff UX implementation result |
| 230 | [reports/REPORT-iseo-report-hub-report-delivery-client-handoff-ux-implementation-01.md](reports/REPORT-iseo-report-hub-report-delivery-client-handoff-ux-implementation-01.md) | Client handoff UX implementation closeout |
| 231 | [product/I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-VISUAL-QA-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-VISUAL-QA-RESULT-v0.1.md) | Client handoff UX Visual QA result |
| 232 | [reports/REPORT-iseo-report-hub-report-delivery-client-handoff-ux-visual-qa-01.md](reports/REPORT-iseo-report-hub-report-delivery-client-handoff-ux-visual-qa-01.md) | Client handoff UX Visual QA closeout |
| 233 | [product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-SCOPE-v0.1.md) | Work Entry Editor MVP scope |
| 234 | [product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-UX-FLOWS-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-UX-FLOWS-v0.1.md) | Work Entry Editor UX flows |
| 235 | [product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-FIELD-CONTRACT-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-FIELD-CONTRACT-v0.1.md) | Work Entry Editor field contract |
| 236 | [product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-TECHNICAL-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-TECHNICAL-CHARTER-v0.1.md) | Work Entry Editor technical charter |
| 237 | [product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-SAFETY-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-SAFETY-POLICY-v0.1.md) | Work Entry Editor safety / DB mutation policy |
| 238 | [product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-IMPLEMENTATION-PLAN-v0.1.md) | Work Entry Editor Implementation 01 plan |
| 239 | [reports/REPORT-iseo-report-hub-work-entry-editor-charter-01.md](reports/REPORT-iseo-report-hub-work-entry-editor-charter-01.md) | Work Entry Editor Charter 01 closeout |
| 240 | [product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-IMPLEMENTATION-RESULT-v0.1.md) | Work Entry Editor Implementation 01 result |
| 241 | [reports/REPORT-iseo-report-hub-work-entry-editor-implementation-01.md](reports/REPORT-iseo-report-hub-work-entry-editor-implementation-01.md) | Work Entry Editor Implementation 01 closeout |
| 242 | [product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-FORM-UI-FIX-01-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-EDITOR-FORM-UI-FIX-01-RESULT-v0.1.md) | Work Entry Editor Form UI Fix 01 result |
| 243 | [reports/REPORT-iseo-report-hub-work-entry-editor-form-ui-fix-01.md](reports/REPORT-iseo-report-hub-work-entry-editor-form-ui-fix-01.md) | Work Entry Editor Form UI Fix 01 closeout |
| 244 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-CURRENT-BLOCK-BASELINE-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-CURRENT-BLOCK-BASELINE-v0.1.md) | Summary assembly current `report_blocks` baseline |
| 245 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SOURCE-RULES-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SOURCE-RULES-v0.1.md) | Work entries → client block source rules |
| 246 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-MODE-OPTIONS-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-MODE-OPTIONS-v0.1.md) | Assembly modes A/B/C; Option A recommended |
| 247 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-UX-FLOW-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-UX-FLOW-v0.1.md) | Preview-only assembly UX |
| 248 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-TECHNICAL-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-TECHNICAL-CHARTER-v0.1.md) | Preview implementation technical charter |
| 249 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFETY-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFETY-POLICY-v0.1.md) | Preview safety + future apply gates |
| 250 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-IMPLEMENTATION-PLAN-v0.1.md) | Summary Assembly Preview Implementation 01 plan |
| 251 | [reports/REPORT-iseo-report-hub-summary-assembly-charter-01.md](reports/REPORT-iseo-report-hub-summary-assembly-charter-01.md) | Summary Assembly Charter 01 closeout |
| 252 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-PREVIEW-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-PREVIEW-IMPLEMENTATION-RESULT-v0.1.md) | Summary Assembly Preview Implementation 01 result |
| 253 | [reports/REPORT-iseo-report-hub-summary-assembly-preview-implementation-01.md](reports/REPORT-iseo-report-hub-summary-assembly-preview-implementation-01.md) | Summary Assembly Preview Implementation 01 closeout |
| 254 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-SCOPE-v0.1.md) | Apply MVP writable keys + body/summary policy |
| 255 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-FINALIZED-REPORT-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-FINALIZED-REPORT-POLICY-v0.1.md) | Finalized/reopen/export apply policy |
| 256 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-BLOCK-TEXT-CONTRACT-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-BLOCK-TEXT-CONTRACT-v0.1.md) | Client-facing apply body format |
| 257 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-UX-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-UX-v0.1.md) | Overwrite / diff / confirm UX |
| 258 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-TECHNICAL-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-TECHNICAL-CHARTER-v0.1.md) | POST apply technical charter |
| 259 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-TEST-STRATEGY-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-TEST-STRATEGY-v0.1.md) | Discovery vs limited write-proof strategy |
| 260 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-SAFETY-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-SAFETY-POLICY-v0.1.md) | Apply backup / mutation / rollback gates |
| 261 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-IMPLEMENTATION-PLAN-v0.1.md) | Apply Implementation 01 plan |
| 262 | [reports/REPORT-iseo-report-hub-summary-assembly-apply-charter-01.md](reports/REPORT-iseo-report-hub-summary-assembly-apply-charter-01.md) | Summary Assembly Apply Charter 01 closeout |
| 263 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-IMPLEMENTATION-RESULT-v0.1.md) | Summary Assembly Apply Implementation 01 result |
| 264 | [reports/REPORT-iseo-report-hub-summary-assembly-apply-implementation-01.md](reports/REPORT-iseo-report-hub-summary-assembly-apply-implementation-01.md) | Summary Assembly Apply Implementation 01 closeout |
| 265 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-SCOPE-v0.1.md) | Safe fixture Option D scope |
| 266 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-DATA-MODEL-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-DATA-MODEL-v0.1.md) | Fixture parent chain / blocks / entries |
| 267 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-CREATION-CLEANUP-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-CREATION-CLEANUP-v0.1.md) | Guarded CLI create/cleanup |
| 268 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-WRITE-PROOF-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-WRITE-PROOF-v0.1.md) | One-block `next_month_plan` write proof |
| 269 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-SAFETY-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-SAFETY-POLICY-v0.1.md) | Local-only fixture safety |
| 270 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md) | Safe Fixture Implementation 01 plan |
| 271 | [reports/REPORT-iseo-report-hub-summary-assembly-safe-fixture-charter-01.md](reports/REPORT-iseo-report-hub-summary-assembly-safe-fixture-charter-01.md) | Summary Assembly Safe Fixture Charter 01 closeout |
| 272 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFE-FIXTURE-IMPLEMENTATION-RESULT-v0.1.md) | Summary Assembly Safe Fixture Implementation 01 result |
| 273 | [reports/REPORT-iseo-report-hub-summary-assembly-safe-fixture-implementation-01.md](reports/REPORT-iseo-report-hub-summary-assembly-safe-fixture-implementation-01.md) | Summary Assembly Safe Fixture Implementation 01 closeout |
| 274 | [product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-UI-CLEANUP-01-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-APPLY-UI-CLEANUP-01-RESULT-v0.1.md) | Summary Assembly Apply UI Cleanup 01 result |
| 275 | [reports/REPORT-iseo-report-hub-summary-assembly-apply-ui-cleanup-01.md](reports/REPORT-iseo-report-hub-summary-assembly-apply-ui-cleanup-01.md) | Summary Assembly Apply UI Cleanup 01 closeout |
| 276 | [product/I-SEO-REPORT-HUB-CLIENT-REPORT-SURFACE-AUDIT-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-SURFACE-AUDIT-v0.1.md) | Client report surface audit (preview / export / share / PDF) |
| 277 | [product/I-SEO-REPORT-HUB-CLIENT-REPORT-TARGET-IA-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-TARGET-IA-v0.1.md) | Client-facing report section order and empty states |
| 278 | [product/I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-DIRECTION-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-DIRECTION-v0.1.md) | Client report visual tokens and print guidance |
| 279 | [product/I-SEO-REPORT-HUB-CLIENT-REPORT-TEMPLATE-ARCHITECTURE-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-TEMPLATE-ARCHITECTURE-v0.1.md) | Option B dedicated document template |
| 280 | [product/I-SEO-REPORT-HUB-CLIENT-REPORT-PDF-EXPORT-SHARE-SAFETY-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-PDF-EXPORT-SHARE-SAFETY-v0.1.md) | No regen / no share mutation policy |
| 281 | [product/I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-IMPLEMENTATION-SEQUENCE-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-IMPLEMENTATION-SEQUENCE-v0.1.md) | Preview → export HTML → PDF proof sequence |
| 282 | [product/I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-ACCEPTANCE-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-ACCEPTANCE-v0.1.md) | Implementation 01 acceptance |
| 283 | [reports/REPORT-iseo-report-hub-client-report-template-visual-alignment-charter-01.md](reports/REPORT-iseo-report-hub-client-report-template-visual-alignment-charter-01.md) | Client Report Template Visual Alignment Charter 01 closeout |
| 284 | [product/I-SEO-REPORT-HUB-CLIENT-REPORT-TEMPLATE-VISUAL-ALIGNMENT-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-TEMPLATE-VISUAL-ALIGNMENT-IMPLEMENTATION-RESULT-v0.1.md) | Client preview template implementation result |
| 285 | [reports/REPORT-iseo-report-hub-client-report-template-visual-alignment-implementation-01.md](reports/REPORT-iseo-report-hub-client-report-template-visual-alignment-implementation-01.md) | Client Report Template Visual Alignment Implementation 01 closeout |
| 286 | [product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-PIPELINE-AUDIT-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-PIPELINE-AUDIT-v0.1.md) | Export HTML/PDF/share pipeline audit |
| 287 | [product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-ALIGNMENT-OPTIONS-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-ALIGNMENT-OPTIONS-v0.1.md) | Export HTML alignment options A–C |
| 288 | [product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-HTML-IMPLEMENTATION-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-HTML-IMPLEMENTATION-SCOPE-v0.1.md) | Export HTML Alignment Implementation 01 scope |
| 289 | [product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-DATA-CSS-PDF-SAFETY-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-DATA-CSS-PDF-SAFETY-v0.1.md) | Export data contract / CSS embed / PDF safety |
| 290 | [product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-IMMUTABILITY-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-IMMUTABILITY-POLICY-v0.1.md) | Export artifact immutability policy |
| 291 | [product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-HTML-ACCEPTANCE-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-HTML-ACCEPTANCE-v0.1.md) | Export HTML Alignment Implementation 01 acceptance |
| 292 | [product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-SEQUENCE-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-SEQUENCE-v0.1.md) | Export HTML → PDF proof → share handoff sequence |
| 293 | [reports/REPORT-iseo-report-hub-client-report-export-html-alignment-charter-01.md](reports/REPORT-iseo-report-hub-client-report-export-html-alignment-charter-01.md) | Client Report Export HTML Alignment Charter 01 closeout |
| 294 | [product/I-SEO-REPORT-HUB-SCREENSHOT-QA-FINDINGS-v0.1.md](product/I-SEO-REPORT-HUB-SCREENSHOT-QA-FINDINGS-v0.1.md) | Screenshot QA findings from Capture 01 |
| 295 | [product/I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-FIX-STRATEGY-v0.1.md](product/I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-FIX-STRATEGY-v0.1.md) | P0 fix strategy (sanitizer / content / buttons / 404) |
| 296 | [product/I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-IMPLEMENTATION-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-IMPLEMENTATION-SCOPE-v0.1.md) | Screenshot QA P0 Fix Implementation 01 scope |
| 297 | [product/I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-SAFETY-ACCEPTANCE-v0.1.md](product/I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-SAFETY-ACCEPTANCE-v0.1.md) | P0 safety and acceptance |
| 298 | [product/I-SEO-REPORT-HUB-SCREENSHOT-QA-TRIAGE-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-SCREENSHOT-QA-TRIAGE-RESULT-v0.1.md) | Screenshot QA triage result / queues |
| 299 | [reports/REPORT-iseo-report-hub-screenshot-qa-fix-charter-01.md](reports/REPORT-iseo-report-hub-screenshot-qa-fix-charter-01.md) | Screenshot QA Fix Charter 01 closeout |
| 300 | [product/I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-FIX-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-FIX-IMPLEMENTATION-RESULT-v0.1.md) | Screenshot QA P0 Fix Implementation result |
| 301 | [reports/REPORT-iseo-report-hub-screenshot-qa-p0-fix-implementation-01.md](reports/REPORT-iseo-report-hub-screenshot-qa-p0-fix-implementation-01.md) | Screenshot QA P0 Fix Implementation 01 closeout |
| 302 | [product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-FINDINGS-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-FINDINGS-v0.1.md) | Monthly detail UX findings after P0 |
| 303 | [product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-TARGET-IA-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-TARGET-IA-v0.1.md) | Manager workspace target IA |
| 304 | [product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-COLLAPSE-POLICY-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-COLLAPSE-POLICY-v0.1.md) | Open vs collapsed regions |
| 305 | [product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-ACTION-SAFETY-UX-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-ACTION-SAFETY-UX-v0.1.md) | GET vs POST action separation |
| 306 | [product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-COLLAPSE-IMPLEMENTATION-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-COLLAPSE-IMPLEMENTATION-SCOPE-v0.1.md) | UX Collapse Implementation 01 scope |
| 307 | [product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-COLLAPSE-ACCEPTANCE-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-COLLAPSE-ACCEPTANCE-v0.1.md) | UX Collapse Implementation 01 acceptance |
| 308 | [reports/REPORT-iseo-report-hub-monthly-report-detail-ux-collapse-charter-01.md](reports/REPORT-iseo-report-hub-monthly-report-detail-ux-collapse-charter-01.md) | Monthly Detail UX Collapse Charter 01 closeout |
| 309 | [product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-COLLAPSE-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-COLLAPSE-IMPLEMENTATION-RESULT-v0.1.md) | Monthly Detail UX Collapse Implementation 01 result |
| 310 | [reports/REPORT-iseo-report-hub-monthly-report-detail-ux-collapse-implementation-01.md](reports/REPORT-iseo-report-hub-monthly-report-detail-ux-collapse-implementation-01.md) | Monthly Detail UX Collapse Implementation 01 closeout |
| 311 | [product/I-SEO-REPORT-HUB-REPORT-5-CURRENT-STATE-AUDIT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-5-CURRENT-STATE-AUDIT-v0.1.md) | Report 5 current-state audit (empty draft) |
| 312 | [product/I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-DECISION-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-DECISION-v0.1.md) | Report 5 draft path product decision |
| 313 | [product/I-SEO-REPORT-HUB-REPORT-5-TARGET-EMPTY-DRAFT-UX-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-5-TARGET-EMPTY-DRAFT-UX-v0.1.md) | Target empty draft UX for report 5 |
| 314 | [product/I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-CLEANUP-IMPLEMENTATION-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-CLEANUP-IMPLEMENTATION-SCOPE-v0.1.md) | Report 5 Draft Path Cleanup Implementation 01 scope |
| 315 | [product/I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-CLEANUP-SAFETY-ACCEPTANCE-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-CLEANUP-SAFETY-ACCEPTANCE-v0.1.md) | Report 5 draft cleanup safety / acceptance |
| 316 | [reports/REPORT-iseo-report-hub-report-5-draft-path-cleanup-charter-01.md](reports/REPORT-iseo-report-hub-report-5-draft-path-cleanup-charter-01.md) | Report 5 Draft Path Cleanup Charter 01 closeout |
| 317 | [product/I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-CLEANUP-HEALTH-REFRESH-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-CLEANUP-HEALTH-REFRESH-IMPLEMENTATION-RESULT-v0.1.md) | Report 5 + health refresh implementation result |
| 318 | [reports/REPORT-iseo-report-hub-report-5-draft-path-cleanup-health-refresh-implementation-01.md](reports/REPORT-iseo-report-hub-report-5-draft-path-cleanup-health-refresh-implementation-01.md) | Report 5 + health refresh implementation closeout |
| 319 | [product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-CONTENT-AUDIT-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-CONTENT-AUDIT-v0.1.md) | Client preview content audit (show-ready gap) |
| 320 | [product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-SHOW-READY-CONTENT-STRATEGY-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-SHOW-READY-CONTENT-STRATEGY-v0.1.md) | Show-ready content strategy (Option A) |
| 321 | [product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-REPORT-1-DEMO-COPY-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-REPORT-1-DEMO-COPY-v0.1.md) | Report 1 demo copy pack (RU) |
| 322 | [product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-SHOW-READY-CONTENT-IMPLEMENTATION-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-SHOW-READY-CONTENT-IMPLEMENTATION-SCOPE-v0.1.md) | Show-ready Content Implementation 01 scope |
| 323 | [product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-SHOW-READY-CONTENT-SAFETY-ACCEPTANCE-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-SHOW-READY-CONTENT-SAFETY-ACCEPTANCE-v0.1.md) | Show-ready content safety / acceptance |
| 324 | [reports/REPORT-iseo-report-hub-client-preview-show-ready-content-charter-01.md](reports/REPORT-iseo-report-hub-client-preview-show-ready-content-charter-01.md) | Client Preview Show-ready Content Charter 01 closeout |
| 325 | [product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-SHOW-READY-CONTENT-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-SHOW-READY-CONTENT-IMPLEMENTATION-RESULT-v0.1.md) | Show-ready Content Implementation 01 result |
| 326 | [reports/REPORT-iseo-report-hub-client-preview-show-ready-content-implementation-01.md](reports/REPORT-iseo-report-hub-client-preview-show-ready-content-implementation-01.md) | Show-ready Content Implementation 01 closeout |
| 327 | [product/I-SEO-REPORT-HUB-PREHOSTING-TECH-DECISION-v0.1.md](product/I-SEO-REPORT-HUB-PREHOSTING-TECH-DECISION-v0.1.md) | Pre-hosting tech decision (PHP 8.3 / reports.i-seo.su) |
| 328 | [product/I-SEO-REPORT-HUB-DEMO-USER-TEST-PROVEROCHNOV-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-USER-TEST-PROVEROCHNOV-PLAN-v0.1.md) | Demo user Тест Проверочнов plan |
| 329 | [product/I-SEO-REPORT-HUB-REALISTIC-DEMO-SCENARIO-PROVERKA-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-REALISTIC-DEMO-SCENARIO-PROVERKA-PLAN-v0.1.md) | Realistic demo scenario ПРОВЕРКА.рa |
| 330 | [product/I-SEO-REPORT-HUB-BROWSER-FILLING-STRATEGY-v0.1.md](product/I-SEO-REPORT-HUB-BROWSER-FILLING-STRATEGY-v0.1.md) | Browser filling strategy (Firefox mars-research) |
| 331 | [product/I-SEO-REPORT-HUB-FIELD-HELP-QUESTION-ICON-DESIGN-v0.1.md](product/I-SEO-REPORT-HUB-FIELD-HELP-QUESTION-ICON-DESIGN-v0.1.md) | Field help `?` icon UX design |
| 332 | [product/I-SEO-REPORT-HUB-FIELD-HELP-COPY-PACK-v0.1.md](product/I-SEO-REPORT-HUB-FIELD-HELP-COPY-PACK-v0.1.md) | Field help Russian copy pack |
| 333 | [product/I-SEO-REPORT-HUB-DEMO-SCENARIO-FIELD-HELP-IMPLEMENTATION-SEQUENCE-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-SCENARIO-FIELD-HELP-IMPLEMENTATION-SEQUENCE-v0.1.md) | Demo + field-help implementation sequence |
| 334 | [product/I-SEO-REPORT-HUB-PREHOSTING-DEMO-FIELD-HELP-SAFETY-ACCEPTANCE-v0.1.md](product/I-SEO-REPORT-HUB-PREHOSTING-DEMO-FIELD-HELP-SAFETY-ACCEPTANCE-v0.1.md) | Pre-hosting demo / field-help safety acceptance |
| 335 | [reports/REPORT-iseo-report-hub-prehosting-demo-scenario-field-help-charter-01.md](reports/REPORT-iseo-report-hub-prehosting-demo-scenario-field-help-charter-01.md) | Pre-hosting demo scenario + field help charter closeout |
| 336 | [product/I-SEO-REPORT-HUB-FIELD-HELP-QUESTION-ICON-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-FIELD-HELP-QUESTION-ICON-IMPLEMENTATION-RESULT-v0.1.md) | Field Help Question Icon Implementation 01 result |
| 337 | [reports/REPORT-iseo-report-hub-field-help-question-icon-implementation-01.md](reports/REPORT-iseo-report-hub-field-help-question-icon-implementation-01.md) | Field Help Question Icon Implementation 01 closeout |
| 338 | [product/I-SEO-REPORT-HUB-DEMO-SEED-CURRENT-STATE-AUDIT-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-SEED-CURRENT-STATE-AUDIT-v0.1.md) | Demo seed current-state audit |
| 339 | [product/I-SEO-REPORT-HUB-DEMO-USER-SEED-SPEC-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-USER-SEED-SPEC-v0.1.md) | Demo user seed spec (Тест Проверочнов) |
| 340 | [product/I-SEO-REPORT-HUB-DEMO-SCENARIO-PROVERKA-DATA-SPEC-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-SCENARIO-PROVERKA-DATA-SPEC-v0.1.md) | ПРОВЕРКА.рa scenario data spec |
| 341 | [product/I-SEO-REPORT-HUB-DEMO-SCENARIO-PROVERKA-CONTENT-PACK-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-SCENARIO-PROVERKA-CONTENT-PACK-v0.1.md) | ПРОВЕРКА.рa content pack (July/August) |
| 342 | [product/I-SEO-REPORT-HUB-DEMO-SCENARIO-SEED-IMPLEMENTATION-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-SCENARIO-SEED-IMPLEMENTATION-PLAN-v0.1.md) | Demo scenario seed implementation plan |
| 343 | [product/I-SEO-REPORT-HUB-DEMO-SCENARIO-BROWSER-FILL-FOLLOWUP-PLAN-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-SCENARIO-BROWSER-FILL-FOLLOWUP-PLAN-v0.1.md) | Browser fill follow-up plan |
| 344 | [product/I-SEO-REPORT-HUB-DEMO-SCENARIO-SEED-SAFETY-ACCEPTANCE-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-SCENARIO-SEED-SAFETY-ACCEPTANCE-v0.1.md) | Demo scenario seed safety / acceptance |
| 345 | [reports/REPORT-iseo-report-hub-demo-user-scenario-seed-charter-01.md](reports/REPORT-iseo-report-hub-demo-user-scenario-seed-charter-01.md) | Demo User and Scenario Seed Charter 01 closeout |
| 346 | [product/I-SEO-REPORT-HUB-DEMO-USER-SCENARIO-SEED-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-USER-SCENARIO-SEED-IMPLEMENTATION-RESULT-v0.1.md) | Demo User and Scenario Seed Implementation 01 result |
| 347 | [reports/REPORT-iseo-report-hub-demo-user-scenario-seed-implementation-01.md](reports/REPORT-iseo-report-hub-demo-user-scenario-seed-implementation-01.md) | Demo User and Scenario Seed Implementation 01 closeout |
| 348 | [product/I-SEO-REPORT-HUB-DEMO-SCENARIO-CLEANUP-UI-POLISH-FIX-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-DEMO-SCENARIO-CLEANUP-UI-POLISH-FIX-RESULT-v0.1.md) | Demo Scenario Cleanup UI Polish Fix 01 result |
| 349 | [reports/REPORT-iseo-report-hub-demo-scenario-cleanup-ui-polish-fix-01.md](reports/REPORT-iseo-report-hub-demo-scenario-cleanup-ui-polish-fix-01.md) | Demo Scenario Cleanup UI Polish Fix 01 closeout |
| 350 | [product/I-SEO-REPORT-HUB-PREHOSTING-DEPLOYMENT-READINESS-v0.1.md](product/I-SEO-REPORT-HUB-PREHOSTING-DEPLOYMENT-READINESS-v0.1.md) | Pre-hosting deployment readiness (operator) |
| 351 | [product/I-SEO-REPORT-HUB-PREHOSTING-FILE-PACKAGE-MAP-v0.1.md](product/I-SEO-REPORT-HUB-PREHOSTING-FILE-PACKAGE-MAP-v0.1.md) | Pre-hosting file include/exclude map |
| 352 | [product/I-SEO-REPORT-HUB-PREHOSTING-DB-URL-PATH-AUDIT-v0.1.md](product/I-SEO-REPORT-HUB-PREHOSTING-DB-URL-PATH-AUDIT-v0.1.md) | Pre-hosting DB URL/path audit |
| 353 | [reports/REPORT-iseo-report-hub-prehosting-deployment-readiness-01.md](reports/REPORT-iseo-report-hub-prehosting-deployment-readiness-01.md) | Pre-hosting Deployment Readiness 01 closeout |
| 354 | [reports/REPORT-iseo-report-hub-host-db-guard-fix-01.md](reports/REPORT-iseo-report-hub-host-db-guard-fix-01.md) | Host DB Guard Fix 01 closeout |
| 355 | [product/I-SEO-REPORT-HUB-FULL-LOCAL-SYSTEM-STATUS-v0.1.md](product/I-SEO-REPORT-HUB-FULL-LOCAL-SYSTEM-STATUS-v0.1.md) | Full local system status after host demo |
| 356 | [product/I-SEO-REPORT-HUB-LOCAL-ROADMAP-AFTER-HOST-DEMO-v0.1.md](product/I-SEO-REPORT-HUB-LOCAL-ROADMAP-AFTER-HOST-DEMO-v0.1.md) | Local roadmap after host demo |
| 357 | [reports/REPORT-iseo-report-hub-full-local-system-status-audit-01.md](reports/REPORT-iseo-report-hub-full-local-system-status-audit-01.md) | Full Local System Status Audit 01 closeout |
| 358 | [product/I-SEO-REPORT-HUB-PREHOSTING-READINESS-FIX-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-PREHOSTING-READINESS-FIX-RESULT-v0.1.md) | Pre-hosting `.htaccess` and deployment hygiene result |
| 359 | [reports/REPORT-iseo-report-hub-prehosting-readiness-fix-01.md](reports/REPORT-iseo-report-hub-prehosting-readiness-fix-01.md) | Pre-hosting Readiness Fix 01 closeout |
| 360 | [product/I-SEO-REPORT-HUB-BROWSER-DEMO-UX-FIX-IMPLEMENTATION-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-BROWSER-DEMO-UX-FIX-IMPLEMENTATION-RESULT-v0.1.md) | Browser demo UX fix implementation result |
| 361 | [reports/REPORT-iseo-report-hub-browser-demo-ux-fix-implementation-01.md](reports/REPORT-iseo-report-hub-browser-demo-ux-fix-implementation-01.md) | Browser Demo UX Fix Implementation 01 closeout |
| 362 | [product/I-SEO-REPORT-HUB-BROWSER-DEMO-UX-FIX-REVIEW-PASS-v0.1.md](product/I-SEO-REPORT-HUB-BROWSER-DEMO-UX-FIX-REVIEW-PASS-v0.1.md) | Browser demo UX fix review pass result |
| 363 | [reports/REPORT-iseo-report-hub-browser-demo-ux-fix-review-pass-01.md](reports/REPORT-iseo-report-hub-browser-demo-ux-fix-review-pass-01.md) | Browser Demo UX Fix Review Pass 01 closeout |
| 364 | [product/I-SEO-REPORT-HUB-ACCESS-DENIED-WORK-ENTRY-UX-POLISH-RESULT-v0.1.md](product/I-SEO-REPORT-HUB-ACCESS-DENIED-WORK-ENTRY-UX-POLISH-RESULT-v0.1.md) | Access denied + work entry UX polish result |
| 365 | [reports/REPORT-iseo-report-hub-access-denied-work-entry-ux-polish-01.md](reports/REPORT-iseo-report-hub-access-denied-work-entry-ux-polish-01.md) | Access Denied and Work Entry UX Polish 01 closeout |
| 366 | [product/I-SEO-REPORT-HUB-WORK-ENTRY-FORM-UX-REVIEW-PASS-v0.1.md](product/I-SEO-REPORT-HUB-WORK-ENTRY-FORM-UX-REVIEW-PASS-v0.1.md) | Work entry form UX review pass result |
| 367 | [reports/REPORT-iseo-report-hub-work-entry-form-ux-review-pass-01.md](reports/REPORT-iseo-report-hub-work-entry-form-ux-review-pass-01.md) | Work Entry Form UX Review Pass 01 closeout |

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

1. **Operator review monthly detail after P1 screenshot** — **recommended next (product UX)** — review after evidence `monthly-report-detail-ux-collapse-implementation-01\20260821-033238`
2. **Client Report Export HTML Alignment Implementation 01** — **parked (template track)** until after operator confirm; do not overwrite export 3/4; no PDF/share mutation
3. **Production Environment Operator Decision 01** — **recommended next (environment track)** (operator fills checklist 1–14; binding answers; not implementation)
4. Branch after answers: **Production Environment Validation 01** (VPS + server/domain details) **or** **Production Environment Decision Follow-up 01** (VPS direction only) **or** **Shared Hosting Compatibility Validation 01** **or** **Local Demo Hardening Charter 01** **or** **Report Delivery DB-11 Delivery Events Charter 01** if delivery audit required first
5. Optional: **Production Backup/Restore Charter 01** (after environment chosen; before first real deploy)
6. Optional: **Real Client Data Model Charter 01** (move off LOCAL_FIXTURE_ONLY)
7. Optional later: **Report Delivery Client Handoff DB-11 Charter 01** (only if durable delivery events required / checklist 13 = yes)
8. Optional: **Revoked share retention/pruning DB charter** (Gate L)
9. Optional: **Report Export Template Metadata Write Smoke 01** (exercise future create writes under controlled charter)
10. Optional: **Report Snapshot Hardening 01** / **Report Snapshot Versioning Charter 01** if multi-role or v2 smoke needed
11. Optional: **Report Blocks CRUD Hardening 01** if multi-role HTTP smoke is needed
12. Optional: **Monthly Report Content CRUD Hardening 01** if multi-role HTTP smoke is needed
13. Optional: **Weekly Checkpoints CRUD Hardening 01** if multi-role HTTP smoke is needed
14. Optional: **Reporting Period CRUD Hardening 01** if account-manager edit / multi-role smoke is needed
15. Optional parallel: **v0.5 demo corrections** from backlog (UX only; not product runtime)
16. **SEO specialist feedback** — still **deferred** until operator opens feedback charter
17. Work dictionary extraction/sanitization (из Nikita materials; **exclude** credential sheet)
18. Later: n8n/API/AI integration (events only; human approval gates); client portal / email delivery
19. **Production deploy** — only after Environment Decision + Backup + Real Data gates and explicit operator deploy charter (**no** default push/deploy)

**Historical note:** Static demos v0.1–v0.4, report content architecture, and Product Architecture Layer 02 are complete as documentation/demo baselines. Platform decision (PHP+MySQL) supersedes WordPress-as-runtime assumptions for forward work. Phase 0 scaffold + Phase 1A skeleton + Phase 1B source→runtime sync + Apache vhost + Windows `hosts` for `iseo-report-hub.test` are done (direct domain re-smoke PASS). Local DB `iseo_report_hub_dev` is **created**; first migration (DB-01 + minimal DB-02) is **applied**. Auth persistence + local admin bootstrap are **implemented** (DB-backed login; one local admin). DB-03 reporting periods migration is **applied**. Local fixture apply is **complete** (demo client/project/site + period `2026-07`). Reporting Period CRUD **implementation** is complete (internal list/detail/create/edit/archive-by-status; smoke period `2026-08` archived; counts clients/projects/sites/reporting_periods **1/1/1/2**). Weekly Checkpoints DB-04 **migration apply** is complete (`weekly_checkpoints` + local W1–W3 smoke). Weekly Checkpoints CRUD **implementation** is complete (period-scoped list/detail/create/edit/skip-or-archive; W4 smoke id **7** skipped; weekly_checkpoints **4**). Monthly Report Content DB-05 **migration apply** is complete (`monthly_report_contents` + 1 local demo row). Monthly Report Content CRUD **implementation** is complete (period-scoped detail/create/edit/archive-by-status; demo id **1** status `in_progress`; monthly_report_contents **1**). Report Blocks DB-06 **migration apply** is complete (`report_blocks` + 5 local fixture blocks; migrations **5** / tables **13**). Report Blocks CRUD **Charter 01** is complete (docs/policy only; next = Report Blocks CRUD Implementation 01). `app-source/` remains the versioned SoT; runtime is Localhost deploy target.

---

## Boundaries (do not overclaim)

- **Auth persistence is implemented for local MVP** — login/logout/session/roles/audit; **not** production auth hardening
- **One local admin user exists** — no user management UI; no password reset
- **Reporting Period CRUD MVP is implemented** — internal list/detail/create/edit/archive-by-status; CSRF; no DELETE; demo + smoke periods only
- **Runtime has synced auth + CRUD code** at `X:\MARS-Localhost\sites\php\projects\iseo-report-hub`
- **Local MySQL DB `iseo_report_hub_dev` exists** with core auth/org tables + **`reporting_periods`** (DB-03) + **`weekly_checkpoints`** (DB-04) + **`monthly_report_contents`** (DB-05) + **`report_blocks`** (DB-06) + **`report_snapshots`** (DB-07) + **`report_exports`** (DB-08 + DB-09 template metadata) + **`report_export_shares`** (DB-10; migrations **9**; tables **16**; active snapshot **1**; HTML exports **2**; PDF exports **2**; share rows **6** revoked smoke / **0** active)
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
- **Report Delivery / Public Share Charter 01 is complete** — Option B tokenized PDF share MVP; `report_export_shares` + DB-10 then implementation planned; **no** code/runtime/DB/SQL/token/public route/artifact mutation in charter
- **Report Delivery Public Share DB-10 Migration Apply 01 is complete** — migration `000009` applied; `report_export_shares` exists; share rows **0** at apply time; migrations **9**; tables **16**; artifacts unchanged; HTTP 13/13; **no** token/public route/app code in apply wave
- **Report Delivery Public Share Implementation 01 is complete** — tokenized public PDF share for eligible export id **4**; routes/UI/service; smoke PASS; **no** portal/email/`/r/{token}`
- **Report Delivery Public Share Hardening 01 is complete** — 64-hex gate; 404/410 policy; stream headers; access after preflight; smoke **66/66**
- **Report Delivery Public Share Visual QA 01 is complete** — verdict **PASS_WITH_MINOR_ISSUES**; evidence under STORAGE; smoke **86/86**; shares **4** revoked / active **0**; artifacts unchanged; **no** app-source/runtime code edits
- **Report Delivery Client Handoff UX Charter 01 is complete** — Option B internal handoff panel + copy pack; no DB tracking yet; DB-11 deferred; Visual QA minors carried to Implementation 01; **no** code/runtime/DB/token/public route/artifact mutation in charter
- **Report Delivery Client Handoff UX Implementation 01 is complete** — readiness panel + once RU copy pack; Visual QA minors resolved; smoke **115/115**; shares **5** revoked / active **0**; public PDF stream unchanged; **no** DB-11 / portal / email
- **Report Delivery Client Handoff UX Visual QA 01 is complete** — verdict **PASS**; evidence under STORAGE; smoke **129/129**; shares **6** revoked / active **0**; artifacts unchanged; prior list/path minors resolved; **no** app-source/runtime code edits
- **Report Delivery Production Readiness Charter 01 is complete** — docs/policy only; local MVP **A–D PASS**; production **E–K** blockers; M/N deferred; L ready-for-plan; **no** app-source/runtime/DB/deploy mutation
- **Production Environment Charter 01 is complete** — docs/policy only; options A–E compared; recommended candidate **Option C VPS**; operator decisions 1–12 open; **no** hosting/domain/DNS/HTTPS/server/deploy; **no** app-source/runtime/DB mutation
- **Production Environment Decision 01 is complete** — decision state **`RECOMMENDATION_READY`**; recommended default **Option C VPS PHP-FPM/Nginx/MySQL**; checklist 1–14 pending; production **not selected**; **no** server/deploy/DNS/HTTPS/DB/secrets/code mutation
- **Demo Visual Shell Alignment Implementation 02 is complete** — live shell demo-like (sidebar/light/red); Russian UX retained; PDF/client-report still deferred
- **UI Screenshot QA / Brand / Nikita Templates Discovery 01 is complete** — secondary EN inventory; i-seo yellow `#facc15` + Manrope; Nikita work plans mapped; no code/runtime/DB mutation
- **UI Russian Cleanup and i-SEO Brand Layer Implementation 03 is complete** — secondary RU + brand tokens; shares/PDF/DB unchanged; Nikita model / client PDF deferred
- **UI Cleanup Brand Fix 01 is complete** — dashboard active-share status + reason/detail RU; brand verified; shares/PDF/DB unchanged
- **Nikita Report Template Data Model Charter 01 is complete** — Option B catalogue + monthly work entries; 6 shells kept as assembly
- **Nikita Catalogue Seed and Work Entry Model Implementation 01 is complete** — DB-11 applied locally; 13 categories / 31 items / 7 fixture entries; read repositories; exports/shares/PDF unchanged
- **Work Entry UI Implementation 01 is complete** — read-only «Работы за месяц» on monthly report show; 7 cards; no editor; exports/shares/PDF unchanged
- **Work Entry Editor Charter 01 is complete** — create/edit MVP specified; no physical delete; Option D smoke for impl; **no** code/runtime/DB mutation in charter
- **Work Entry Editor Implementation 01 is complete** — create/edit MVP live locally; no delete route; Option D net-zero; exports/shares/PDF unchanged
- **Work Entry Editor Form UI Fix 01 is complete** — visible input/select/textarea borders + yellow focus; create/edit layout microfix; no DB/share/export/PDF mutation
- **Summary Assembly Charter 01 is complete** — Option A preview-only; mapping work entries → 6 shells; no overwrite; **no** code/runtime/DB mutation in charter
- **Summary Assembly Preview Implementation 01 is complete** — GET-only `/monthly-reports/{id}/assembly-preview`; fixture 4/2/1; no DB/block/PDF/share mutation
- **Summary Assembly Apply Charter 01 is complete** — Option B MVP specified; apply blocked on finalized report 1; next = Apply Implementation 01
- **Summary Assembly Apply Implementation 01 is complete** — POST apply + disabled finalized UI; report 1 refused; no live write proof; exports/shares/PDF unchanged
- **Summary Assembly Safe Fixture Charter 01 is complete** — Option D dedicated local fixture specified; id 1/5 not used
- **Summary Assembly Safe Fixture Implementation 01 is complete** — guarded CLI + one-block `next_month_plan` write proof + cleanup; id 1/5 and PDF/export/share unchanged
- **Summary Assembly Apply UI Cleanup 01 is complete** — manager-facing preview; one amber lock banner; draft primary; current/source collapsed; apply still disabled on report 1; no DB/PDF/share mutation
- **Client Report Template Visual Alignment Charter 01 is complete** — Option B dedicated client document; preview-first; PDF 4 / share frozen
- **Client Report Template Visual Alignment Implementation 01 is complete** — live preview is a client document; export 4 / share / PDF unchanged
- **Client Report Export HTML Alignment Charter 01 is complete** — Option B dual-path designed; export 4 frozen
- **Operator decision (PDF deferred)** — PDF/export alignment and PDF regeneration postponed until after product pages polish + manual visual QA; do not run Export HTML Alignment Implementation / regenerate export 4 until explicit confirm
- **App Pages Visual QA Preparation 01 is complete** — inventory, manual route, screenshot checklist, UX criteria, issue intake, triage plan, operator short guide; no app-source/runtime/DB mutation
- **Automated Screenshot Capture 01 is complete** — 16 full-page PNG under Storage `automated-screenshot-capture-01\20260821-010501`
- **Screenshot QA Fix Charter 01 is complete** — findings + P0 strategy/scope/safety + triage result; no app-source/runtime/DB mutation
- **Screenshot QA P0 Fix Implementation 01 is complete** — sanitizer + junk fallbacks + periods button CSS + RU 404; DB/export/share/PDF unchanged; minor residual: edit-form note textareas may keep raw fixture markers
- **Monthly Report Detail UX Collapse Charter 01 is complete** — findings + target IA + collapse policy + action safety + impl scope + acceptance for `/monthly-reports/{id}`; no app-source/runtime/DB mutation
- **Monthly Report Detail UX Collapse Implementation 01 is complete** — manager summary + primary workflow + work entries high; diagnostics/admin collapsed; DB/export/share/PDF unchanged
- **Report 5 Draft Path Cleanup Charter 01 is complete** — Option A + light demotion; empty-draft target UX + impl scope/safety; no app-source/runtime/DB mutation
- **Report 5 Draft Path Cleanup + Health Refresh Implementation 01 is complete** — empty-draft UX for report 5 + `/health` Local MVP refresh; DB/export/share/PDF unchanged
- **Client Preview Show-ready Content Charter 01 is complete** — Option A render-layer demo fallback for report 1 preview; Option B/C deferred; no app-source/runtime/DB mutation in charter
- **Client Preview Show-ready Content Implementation 01 is complete** — report 1 local preview/print show-ready via render-layer fallback; report 5 empty draft preserved; DB/export/share/PDF unchanged
- **Pre-hosting Demo Scenario and Field Help Charter 01 is complete** — PHP 8.3 / `reports.i-seo.su` docs; demo user + `ПРОВЕРКА.рa` plans; field-help UX/copy; no code/DB/runtime/host upload
- **Field Help Question Icon Implementation 01 is complete** — reusable `?` help on work/block/monthly forms + detail/assembly; DB/export/share/PDF unchanged; client preview without help clutter
- **Demo User and Scenario Seed Charter 01 is complete** — audit + user/scenario/content/seed/browser-fill/safety docs; no DB/tool/browser/host mutation
- **Demo User and Scenario Seed Implementation 01 is complete** — guarded `demo-proverka-seed.php`; local user `test@mail.ru` + initial `ПРОВЕРКА.рa` July/August seeded; later renamed in Cleanup Polish Fix 01
- **Demo Scenario Cleanup and UI Polish Fix 01 is complete** — old Demo Client path removed; display `ПРОВЕРКА.рф`; dashboard/periods/status/name polish; no host upload; no new PDF/export/share
- **Pre-hosting Deployment Readiness 01 is complete (ATTENTION)** — operator pack for `reports.i-seo.su`; copy `app-source`; document root `public`; PHP 8.3; `.env.local`; no WP-like DB URL replace; no host upload in this wave; add rewrite `.htaccess` manually
- **Host DB Guard Fix 01 is complete** — web runtime no longer requires local DB name; operator re-upload `DatabaseService.php` (operator reports host demo working)
- **Full Local System Status Audit 01 is complete (ATTENTION)** — local continue-OK; missing source `.htaccess`; host public GET not independently confirmed; PDF/share parked; roadmap after host demo recorded
- **Pre-hosting Readiness Fix 01 is complete (PASS)** — source/runtime matching `public/.htaccess`; local route + DB baseline passed; no host upload
- **Browser Demo UX Fix Implementation 01 is complete (PASS)** — specialist UX cleanup; stale export/share nav removed; finalized July read-only; role/route narrowing; no host/PDF/export rows
- **Browser Demo UX Fix Review Pass 01 is complete (PASS_WITH_RESIDUALS)** — specialist screenshot/QA pack; no P1; screenshots ready for Web-GPT; P2 residuals later polished in Access Denied / Work Entry UX Polish 01
- **Access Denied and Work Entry UX Polish 01 is complete (PASS)** — branded 403 shell; sidebar parked statuses; work-entry form sections; no host/PDF/export/share rows
- **Work Entry Form UX Review Pass 01 is complete (PASS_WITH_RESIDUALS)** — create/edit screenshots + assertions; no P1; P2 help-density / long scroll; no code/DB content mutation beyond audit_log
- **Specialist Report Content Workflow Implementation 01 is complete** — Option D Hybrid MVP; route `/monthly-reports/{id}/content-workflow`; specialist save to `report_blocks.body` + flat mirror; August validation write done; no host
- **Specialist Content Workflow Review Pass 01 is complete (PASS)** — specialist screenshot/QA pack; CTA + six cards + hint fill + preview marker + July lock + raw 403; no P1; light P2 scroll; no code/DB content mutation beyond audit_log; Web-GPT visual decision: SPECIALIST CONTENT WORKFLOW VISUAL ACCEPTED
- **Local Specialist MVP Acceptance Closeout 01 is complete** — milestone status `LOCAL SPECIALIST MVP ACCEPTED_BY_MARS_REVIEW / OPERATOR_MANUAL_WALKTHROUGH_PENDING`; closeout + operator walkthrough v0.1 + SEO specialist draft instruction v0.1 + Report Evidence/Attachments/Links requirement v0.1; operator manual walkthrough **not yet done**; no code/runtime/host/DB
- **Storage Hygiene Loss Audit 01 is complete (SAFE)** — deleted temporary STORAGE git contours did not remove authoritative i-SEO Report Hub data; restore not needed; normal work may continue; see [REPORT-iseo-report-hub-storage-hygiene-loss-audit-01.md](reports/REPORT-iseo-report-hub-storage-hygiene-loss-audit-01.md)
- **Project-Centric Dashboard and IA Charter 01 is complete** — operator rejected demo home blocks; charter + implementation plan recorded; see [I-SEO-REPORT-HUB-PROJECT-CENTRIC-DASHBOARD-IA-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-PROJECT-CENTRIC-DASHBOARD-IA-CHARTER-v0.1.md)
- **Next (product UX / local)** = **Project Dashboard Implementation 01** — replace `/` with project list dashboard
- **Next (operator)** = **Manual walkthrough** — [I-SEO-REPORT-HUB-OPERATOR-MANUAL-WALKTHROUGH-v0.1.md](operator-guides/I-SEO-REPORT-HUB-OPERATOR-MANUAL-WALKTHROUGH-v0.1.md) (parallel; still pending)
- **Next (product UX)** = collect SEO-team feedback on draft instruction after walkthrough; Specialist Content Workflow UX Polish 02 optional / not urgent
- **Next (after dashboard + detail)** = Project Creation Draft → Curator Notes/Alerts Charter → **Report Evidence Links** — [I-SEO-REPORT-HUB-REPORT-EVIDENCE-ATTACHMENTS-LINKS-REQUIREMENT-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-EVIDENCE-ATTACHMENTS-LINKS-REQUIREMENT-v0.1.md)
- **Next (baseline / hosting track, paused)** = **Production Config Normalization 01**
- **Next (template/export track, parked)** = Export Share PDF Readiness Charter / Client Report Export HTML Alignment (only after operator confirm)
- **Next (hosting ops)** = host smoke checklist + optional deploy package builder; do not broad-sync `tools/` or local `.env.local`
- **Not production-ready** — local/dev only; fixture data; host subdomain/SSL noted by operator but deploy **not** authorized; no prod secrets/DB/backup/monitoring selected
- **Live DB re-probe caveat** — MySQL connection refused during Production Readiness Charter 01, Production Environment Charter 01, and Production Environment Decision 01; re-check local DB before future implementation if local evidence needed (DB reachable again during Demo Visual Shell Implementation 02 and Catalogue Model Implementation 01)
- **No drag/drop reorder / rich text editor / client portal / email delivery** (runtime public share exists for MVP PDF token links only; handoff landing page deferred)
- **No autonomous publication**
- **Website Factory is not runtime owner** — methodology + prototype lane only
- **Static demo v0.4 is UX reference only** — not implementation
- **Historical WP architecture docs** remain in corpus as legacy planning — not current SoT
- **Domain `iseo-report-hub.test` resolves to 127.0.0.1** and serves auth-capable routes over HTTP
- **No separate runtime Git repository** — and none should be created without charter
