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
| **Platform direction** | **Reopened** — WordPress on i-seo.su remains option; custom PHP + MySQL candidate; see [I-SEO-REPORT-HUB-PLATFORM-OPTIONS-v0.1.md](product/I-SEO-REPORT-HUB-PLATFORM-OPTIONS-v0.1.md) |
| **Implementation** | **Not started** — no plugin, no runtime, no n8n workflow |

---

## Current status

| Field | Value |
|-------|-------|
| **Status** | planned / product architecture |
| **Lane** | Lane B — product formation and architecture |
| **Active stage** | Product Architecture Layer 02 complete (docs); static demo v0.4 accepted as raw baseline; SEO feedback deferred |
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
| Next after Layer 02 review | Scoped **commit** of architecture docs; then choose **v0.5 demo corrections** **or** **MVP technical brief** |

**Demo workspace:** `workspaces/website-factory-operations/iseo-report-hub-prototype/` — v0.4 exists (commit `66d651a2`); **not modified** in Product Architecture Layer 02 task.

---

## Current approved decisions (summary)

1. Report Hub — **операционная система отчётности**, не PDF-only tool.
2. **Platform** — **platform-neutral until decision gate**; WordPress on i-seo.su **or** custom PHP + MySQL — see platform options v0.1.
3. **n8n** — external helper (AI, reminders, notifications); **не** SoT.
4. **Primary client output** — web report pages (hosting TBD by platform choice); PDF optional later.
5. **Reporting period** — 1 month; 3 weekly checkpoints + 1 monthly final.
6. **MVP direction** — internal admin, manual data, evidence, Topvisor external link, approval/publish (implementation platform TBD).
7. **Credentials/secrets** — отдельный secure integration concern; **не** в report content.

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

1. **Operator review** of Product Architecture Layer 02 docs
2. **Scoped commit** of Layer 02 architecture documentation (operator-chartered; selective paths only)
3. Then choose: **v0.5 demo corrections** (from backlog) **or** **MVP technical brief** (platform/hosting/auth/ownership)
4. **SEO specialist feedback** — still **deferred** until operator opens feedback charter
5. **Platform decision gate** — after Layer 02 + technical brief (+ feedback when ready); see platform options + implementation decision frame
6. Work dictionary extraction/sanitization (из Nikita materials; **exclude** credential sheet)
7. MVP implementation charter (HITL) — platform TBD (Anton / i-SEO)
8. Later: n8n/API/AI integration (events only; human approval gates)

**Historical note:** Static demos v0.1–v0.4 and report content architecture are complete as documentation/demo baselines; see operator review sections above.

---

## Boundaries (do not overclaim)

- **No implementation started**
- **No WordPress plugin exists**
- **No API integration exists**
- **No n8n workflow exists**
- **No client portal exists**
- **No autonomous publication**
- **Website Factory is not runtime owner** — methodology + prototype lane only; production platform **not decided** (see platform options v0.1)
- **Static demo v0.1 is not SEO specialist-ready** — workflow mechanics only
