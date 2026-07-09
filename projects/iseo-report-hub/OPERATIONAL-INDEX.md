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
| **Platform direction** | WordPress-based internal tool on i-seo.su |
| **Implementation** | **Not started** — no plugin, no runtime, no n8n workflow |

---

## Current status

| Field | Value |
|-------|-------|
| **Status** | planned / product architecture |
| **Lane** | Lane B — product formation and architecture |
| **Active stage** | Website Factory prototype charter (v0.1) |
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

## Current approved decisions (summary)

1. Report Hub — **операционная система отчётности**, не PDF-only tool.
2. **WordPress / i-seo.su** — source of truth для reports и workflow.
3. **n8n** — external helper (AI, reminders, notifications); **не** SoT.
4. **Primary client output** — web report pages на i-seo.su; PDF optional later.
5. **Reporting period** — 1 month; 3 weekly checkpoints + 1 monthly final.
6. **MVP** — internal WP admin, manual data, evidence, Topvisor external link, approval/publish.
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

1. **Operator review** of Website Factory prototype charter + demo brief (v0.1)
2. **Choose next path:** authorize **Website Factory demo build charter** (static HTML workspace) **OR** revise prototype screens/scope before build
3. Work dictionary extraction/sanitization (из Nikita materials; **exclude** credential sheet)
4. Report block model refinement (if needed post-review)
5. MVP implementation charter (HITL) for Anton / i-seo.su
6. **Website Factory demo build (operator charter only):** workspace candidate `workspaces/website-factory-operations/iseo-report-hub-prototype/` — **not created until separate build task**; see [I-SEO-REPORT-HUB-WEBSITE-FACTORY-DEMO-BRIEF-v0.1.md](product/I-SEO-REPORT-HUB-WEBSITE-FACTORY-DEMO-BRIEF-v0.1.md)
7. Later: n8n/API/AI integration (events only; human approval gates)

---

## Boundaries (do not overclaim)

- **No implementation started**
- **No WordPress plugin exists**
- **No API integration exists**
- **No n8n workflow exists**
- **No client portal exists**
- **No autonomous publication**
- **Website Factory is not runtime owner** — methodology + prototype lane only; WordPress on i-seo.su remains production/report SoT
