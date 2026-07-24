# REPORT — I-SEO REPORT HUB PLATFORM DECISION + PHP MYSQL MVP TECHNICAL BRIEF 01

**project_id:** `iseo-report-hub`  
**Date:** 2026-07-24  
**Task type:** documentation-only  
**Git actions:** none (no add / commit / push)

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Staged / index | **Empty** at task start and after writes (no staging performed) |
| Foreign WIP | **Preserved** — many unrelated `M` / `??` entries across other projects/workspaces left untouched |
| Write scope | Only `projects/iseo-report-hub/product/**`, `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-platform-decision-php-mysql-technical-brief-01.md`, `projects/iseo-report-hub/OPERATIONAL-INDEX.md` |

Required i-SEO docs were present and read before writes. Preflight **PASS**.

---

## 2. Operator Decision Applied

| Decision | Applied |
|----------|---------|
| No WordPress runtime / SoT | Yes |
| Custom PHP + SQL/MySQL | Yes |
| Laragon available as local candidate | Yes (planning only; no runtime changes) |
| Docs only | Yes — no code, SQL, demo, Laragon, registry, or git mutations |

WordPress/i-seo.su residual role limited to visual reference and optional future marketing/embed — not MVP dependency. Static demo v0.4 remains UX reference only.

---

## 3. Files Created

1. `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-PLATFORM-DECISION-v0.1.md`
2. `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-PHP-MYSQL-MVP-TECHNICAL-BRIEF-v0.1.md`
3. `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LARAGON-LOCAL-RUNTIME-PLAN-v0.1.md`
4. `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MVP-IMPLEMENTATION-PHASES-v0.1.md`
5. `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MVP-SCHEMA-DRAFT-v0.1.md`
6. `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MVP-ROUTE-AND-SCREEN-MAP-v0.1.md`
7. `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-platform-decision-php-mysql-technical-brief-01.md`

---

## 4. Files Modified

1. `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 5. Platform Decision Summary

| Topic | Summary |
|-------|---------|
| **Decision** | Custom PHP + SQL/MySQL app; WordPress rejected as runtime/SoT; Laragon accepted as local candidate |
| **Reasoning** | Structured data, roles, lifecycle, snapshots, evidence, future imports need clean product logic without WP plugin/theme coupling |
| **WP residual** | Style reference; optional future embed/link; marketing pages; not DB SoT; not admin backend; not required for MVP |
| **Consequences** | Own auth, schema, file storage, renderer, client token links, backup/export, deployment |
| **Unknowns** | Exact PHP/MySQL versions; Laragon path/vhost; production hosting; file storage path; final client access hardening |

---

## 6. Technical Brief Summary

| Topic | Summary |
|-------|---------|
| **MVP objective** | Local-to-production-ready PHP/MySQL reporting app for create → fill → review → publish → version monthly SEO reports with weekly checkpoints and evidence |
| **Technical shape** | Plain PHP / light MVC; MySQL/MariaDB; server-rendered admin; progressive JS; no heavy framework unless approved; no WordPress |
| **Modules** | Auth, users/roles, clients, projects/sites, periods, weekly/monthly, blocks, workspace, review, snapshots, evidence, KPIs, templates, settings, audit |
| **Screens** | Login through settings/users as listed in brief |
| **Data flow** | Admin setup → period → specialist fill → review → snapshot publish → token URL → versioned re-publish |
| **Security baseline** | Password hash, sessions, CSRF, roles, validation, upload restrictions, private uploads, token entropy, no secrets in repo, audit publish/unpublish |
| **Non-MVP** | Topvisor API, AI, client portal, BI, CRM, billing, task manager, multi-tenant SaaS, auto PDF |
| **Risks** | Scope creep, uploads, snapshot immutability, role complexity, template overengineering, hosting/backups, demo→app migration |

---

## 7. Laragon Plan Summary

| Topic | Summary |
|-------|---------|
| **Assumed runtime** | Laragon available; exact path/PHP/MySQL/vhost **SAFE UNKNOWN** |
| **Layout options** | A: `projects/iseo-report-hub/app\`; B: `X:\MARS-Localhost\iseo-report-hub\` (preferred runtime candidate) |
| **Local domain candidates** | `iseo-report-hub.test`, `iseo-report.local` (not created) |
| **DB candidate** | `iseo_report_hub_dev` (not created) |
| **Secrets** | `.env.local` never committed; `.env.example` later without secrets |
| **Future preflight** | Confirm path, versions, web server, docroot, DB, backups, gitignore, secrets path |

No Laragon changes performed.

---

## 8. Implementation Phases Summary

Phases **0–11** documented (not executed):

0. Runtime confirmation / scaffold charter  
1. App skeleton + config + auth  
2. DB schema + seed  
3. Clients/projects/sites/periods  
4. Specialist workspace  
5. Weekly checkpoints  
6. Monthly report editor  
7. Review workflow  
8. Published snapshot / client report  
9. Evidence/files security  
10. QA / demo migration  
11. Deployment / backup decision  

Each phase has goal, deliverables, future allowed writes, validation, HITL gate.

---

## 9. Schema Draft Summary

| Topic | Summary |
|-------|---------|
| **Core tables** | users, roles, user_roles, clients, projects, sites, project_type_profiles, reporting_periods, weekly_checkpoints, monthly_reports, report_blocks, report_block_values, work_item_categories, work_items, kpi_definitions, kpi_values, evidence_items, evidence_files, evidence_links, reviewer_comments, published_snapshots, audit_log |
| **Snapshot strategy** | Client-safe payload on publish; token lookup; version/supersede/revoke; never serve live draft |
| **SQL** | **None** — conceptual draft only |

---

## 10. Route/Screen Map Summary

| Topic | Summary |
|-------|---------|
| **Admin routes** | `/login`, `/logout`, `/`, clients, projects, periods, workspace, weekly, monthly, review, preview, settings |
| **Public token route** | `/p/{token}` → published_snapshots only |
| **Permissions** | Session + role + assignment scope; CSRF on writes; public route isolated |

---

## 11. Validation

| Check | Result |
|-------|--------|
| No code | Pass |
| No SQL migrations | Pass |
| No Laragon changes | Pass |
| No demo workspace edits | Pass |
| No registry changes | Pass |
| No secrets / credentials | Pass |
| No real private metrics | Pass |
| No deprecated C:/D:/E: as current targets | Pass |
| Docs do not claim implementation exists | Pass |
| No git staging/commit | Pass |

---

## 12. SAFE UNKNOWN

- Exact PHP version (Laragon / production)
- Exact MySQL / MariaDB version
- Laragon root path, vhost name, docroot
- Final production hosting model
- Final file storage path
- Final client access model beyond MVP token URL (password layer optional)
- Exact runtime layout choice (Active Brain `app\` vs `X:\MARS-Localhost\iseo-report-hub\`)
- Whether snapshot payload is JSON-only or normalized child tables at scale

---

## 13. Recommended Next Action

**Operator review** of the PHP/MySQL MVP Technical Brief package, then **scoped commit** (selective paths only) if approved.

---

## 14. Files Changed

**Created:**

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-PLATFORM-DECISION-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-PHP-MYSQL-MVP-TECHNICAL-BRIEF-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LARAGON-LOCAL-RUNTIME-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MVP-IMPLEMENTATION-PHASES-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MVP-SCHEMA-DRAFT-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MVP-ROUTE-AND-SCREEN-MAP-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-platform-decision-php-mysql-technical-brief-01.md`

**Modified:**

- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 15. Git Actions

- No add  
- No commit  
- No push  
- No fetch  
- No checkout  
- No reset  
- No restore  
- No clean  
- No stash  
