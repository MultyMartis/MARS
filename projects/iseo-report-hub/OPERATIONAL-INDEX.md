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
| **Active stage** | Report Structure Demo v0.2 planning (platform-neutral) |
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

1. **Report Structure Demo v0.2** — inject report structure model v0.2 + demo content pack (3 projects) into static demo workspace; **no platform implementation**
2. **Operator review** of demo v0.2 structure and UX
3. **SEO specialist feedback** — only after v0.2; **not** on v0.1 mechanics-only demo
4. **Platform decision gate** — after structure + feedback; see platform options v0.1
5. Work dictionary extraction/sanitization (из Nikita materials; **exclude** credential sheet)
6. MVP implementation charter (HITL) — platform TBD (Anton / i-SEO)
7. Later: n8n/API/AI integration (events only; human approval gates)

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
