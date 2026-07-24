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
| **Implementation** | **Phase 0 scaffold only** — runtime tree at `X:\MARS-Localhost\sites\php\projects\iseo-report-hub`; **no** DB / vhost / hosts / secrets; **no** product features beyond health/index pages; Phase 1 **blocked** until `app-source/` mirror exists and sync/deploy policy is accepted |
| **Source model** | **Model A selected (planning)** — planned `projects/iseo-report-hub/app-source/`; sync direction source → runtime; mirror **not** created yet |

---

## Current status

| Field | Value |
|-------|-------|
| **Status** | planned / product architecture + Phase 0 runtime scaffold + Model A source mirror charter |
| **Lane** | Lane B — product formation and architecture |
| **Active stage** | MVP **Phase 0 scaffold reviewed**; source/runtime policy v0.1 defined; **Model A selected for planning** (charter + deploy/sync policy + file map); `app-source/` **not** created; Laragon preflight complete; platform decision + technical brief package; Layer 02 complete; static demo v0.4 UX reference; SEO feedback deferred; **Phase 1 blocked** until mirror exists and sync/deploy policy is accepted |
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

1. **Create and commit `app-source/` mirror** from Phase 0 scaffold using the approved file map (Model A)
2. **MVP Phase 1** — app skeleton + config + auth baseline — **blocked** until mirror exists and sync/deploy policy is accepted
3. Optional parallel: **v0.5 demo corrections** from backlog (UX only; not product runtime)
4. **SEO specialist feedback** — still **deferred** until operator opens feedback charter
5. Work dictionary extraction/sanitization (из Nikita materials; **exclude** credential sheet)
6. MVP implementation phases 2–11 per implementation charter (Anton / i-SEO)
7. Later: n8n/API/AI integration (events only; human approval gates)

**Historical note:** Static demos v0.1–v0.4, report content architecture, and Product Architecture Layer 02 are complete as documentation/demo baselines. Platform decision (PHP+MySQL) supersedes WordPress-as-runtime assumptions for forward work. Phase 0 scaffold exists on Localhost; Model A charter + deploy/sync policy are defined; `app-source/` mirror creation is the next gate before Phase 1.

---

## Boundaries (do not overclaim)

- **Implementation is Phase 0 scaffold only** — not a product app
- **Runtime scaffold exists** at `X:\MARS-Localhost\sites\php\projects\iseo-report-hub` — index/health pages + folders; **no** DB, **no** auth, **no** migrations
- **Runtime is outside Active Brain Git** — not versioned until `app-source/` mirror is created and committed
- **Model A selected for planning** — `app-source/` path planned; sync source → runtime; mirror **not** created yet
- **Phase 1 is blocked** until mirror exists and sync/deploy policy is accepted
- **No WordPress plugin exists** (and WP is not the chosen runtime)
- **No API integration exists**
- **No n8n workflow exists**
- **No client portal exists**
- **No autonomous publication**
- **Website Factory is not runtime owner** — methodology + prototype lane only
- **Static demo v0.4 is UX reference only** — not implementation
- **Historical WP architecture docs** remain in corpus as legacy planning — not current SoT
- **Phase 0 did not change Laragon config, hosts, vhosts, services, or databases**
- **Domain `iseo-report-hub.test` is intended only** until manually mapped
- **No separate runtime Git repository** — and none should be created without charter
