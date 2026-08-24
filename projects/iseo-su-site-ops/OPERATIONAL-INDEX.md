# ISEO-SU SITE OPS — Operational Index

**Lane:** A — Existing Site Operations / Integration  
**Classification:** documentation-first programme locus  
**Domain root:** [README.md](README.md)  
**Project brain:** [ISEO-SU-CURRENT-STATE-v1.md](ISEO-SU-CURRENT-STATE-v1.md)

---

## Start here — current authority order

1. [Current State](ISEO-SU-CURRENT-STATE-v1.md)
2. [Production Architecture Knowledge Base](ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md)
3. [Task Routing Guide](ISEO-SU-TASK-ROUTING-GUIDE-v1.md)
4. [Route Ownership Matrix](ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md)
5. [Protected Zones](ISEO-SU-PROTECTED-ZONES-v1.md)
6. Feature baselines:
   - [Forms / anti-spam / recipient](ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md)
   - [Metrika visitor IP](ISEO-SU-METRIKA-VISITOR-IP-PARAM-BASELINE-v1.md)
   - [Glossary final production](ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md)
   - [Sitemap architecture/current state](ISEO-SU-SITEMAP-ARCHITECTURE-AND-CURRENT-STATE-v1.md)
   - [Latest technical/SEO audit](ISEO-SU-TECH-SEO-AUDIT-EVIDENCE-v1.md)
7. [Artifact Register](ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md)
8. Historical evidence/REPORTs only after current authorities.

## Current open work

1. `SM-CHILD-404`: repair `/sitemap.xml` as a valid two-child index for `/sitemap-static.xml` and `/wp-sitemap.xml`; remove obsolete 404 children; then verify robots.
2. Decide/implement `/sitemap-static.xml` maintenance: safe automation preferred, manual rebuild/procedure fallback.
3. `IMG-BROKEN`: repair relative blog `img/...` paths (≈96 sampled broken URLs) and regression-crawl.
4. Review/route the remaining 6 MEDIUM, 8 LOW, and 14 REVIEW audit signals using the findings CSV.

**Not implemented:** sitemap repair, static sitemap maintenance, blog image repair, and remaining audit fixes.
**Deferred optional:** mobile glossary offcanvas, archive Yoast description, MERGED alias polish, unnecessary sitemap duplication, WPilot 6D.

---

## Programme identity

| Field | Value |
|-------|-------|
| **Programme name** | ISEO-SU-SITE-OPS |
| **project_id (intended)** | `iseo-su-site-ops` — **not yet registered** in `registry/project-registry.md` (registry mutation **NOT AUTHORIZED**) |
| **Site / domain** | `https://i-seo.su/` |
| **Organization** | i-SEO |
| **Operator** | Andrey |
| **Canonical locus** | `X:\AI MARS\projects\iseo-su-site-ops\` |
| **Primary lane** | Lane A — Existing Site Operations / Integration |

---

## Current state

| Field | Value |
|-------|-------|
| **Lifecycle** | **COMPLETE — FORMS HARDENED / OPERATOR RECIPIENT REMOVED / TECH-SEO AUDIT COMPLETE / METRIKA IP PARAM ADDON ON** |
| **Project status** | Glossary public: **184** published eligible; **57** non-eligible; `/glossary/` **200**; final hero/menu/title/overflow baseline complete; mobile offcanvas deferred. Forms hardened; production recipient `nikel007i33@yandex.ru` only. Metrika visitor-IP addon **ON** (`ipaddress`, counter **54287016**, no auto-ban). Tech/SEO audit has two HIGH open defects: root `/sitemap.xml` advertises three 404 children and ≈96 sampled relative blog image URLs are broken. |
| **Architecture knowledge** | **COMPLETE** — knowledge base + route matrix + task routing guide |
| **Glossary** | Foundation + Batches 01–04 content + **controlled public launch 2026-07-26** + final integration/post-launch closeout **2026-08-18** |
| **Current phase (WPilot)** | **PHASE 6D — BLOCKED** (bridge/smoke awaiting exact approval + backup lines) — **not required** for ordinary site content/file tasks |
| **Accepted WPilot baseline** | **PHASE 6C — TOKEN CREATED / RC6 SAFE DEFAULTS** |
| **Access files** | **LOCAL-ONLY FILLED / VALIDATED** (Git-ignored) |
| **WPilot** | **ACTIVE** RC6; bridge **DISABLED**; writes **DISABLED**; token **LOCAL-ONLY**; REST **NOT RUN** |
| **Open blockers / open required task groups** | **0 / 4** |
| **Next operator action (site work)** | Review SEO audit report; charter Site Ops fix wave for sitemap children 404 + blog image relative paths. Forms: operator mailbox removed from production recipients (`ISEO-SU-FORM-OPERATOR-RECIPIENT-REMOVAL-EVIDENCE-v1.md`). Metrika IP addon: disable via one config flag if needed (`ISEO-SU-METRIKA-VISITOR-IP-PARAM-BASELINE-v1.md`) |
| **Next operator action (WPilot 6D)** | Exact lines `APPROVE ISEO-SU WPILOT BRIDGE AND READ-ONLY SMOKE 6D` + `CONFIRM ISEO-SU FRESH BEGET BACKUP FOR WPILOT 6D` |

Hosting: **Beget**. WordPress Admin: `https://i-seo.su/wp-admin/`. Staging: **absent**. Architecture: **hybrid** — see knowledge base.

---

## Current authority order (start here)

1. [ISEO-SU-CURRENT-STATE-v1.md](ISEO-SU-CURRENT-STATE-v1.md) — project brain  
2. [ISEO-SU-FINAL-LAUNCH-CLOSEOUT-v1.md](ISEO-SU-FINAL-LAUNCH-CLOSEOUT-v1.md)  
3. [ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md](ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md)  
4. [ISEO-SU-TASK-ROUTING-GUIDE-v1.md](ISEO-SU-TASK-ROUTING-GUIDE-v1.md)  
5. [ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md](ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md) + [route matrix](ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md)  
6. [ISEO-SU-PROTECTED-ZONES-v1.md](ISEO-SU-PROTECTED-ZONES-v1.md)  
7. [ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md](ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md)  
8. Historical REPORTs (immutable evidence only)

Stabilization closeout: [ISEO-SU-STABILIZATION-CLOSEOUT-v1.md](ISEO-SU-STABILIZATION-CLOSEOUT-v1.md)

Form security: [ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md](ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md) · evidence [ISEO-SU-FORM-ANTISPAM-VALIDATION-EVIDENCE-v1.md](ISEO-SU-FORM-ANTISPAM-VALIDATION-EVIDENCE-v1.md) · operator recipient removal [ISEO-SU-FORM-OPERATOR-RECIPIENT-REMOVAL-EVIDENCE-v1.md](ISEO-SU-FORM-OPERATOR-RECIPIENT-REMOVAL-EVIDENCE-v1.md) · tech/SEO audit evidence [ISEO-SU-TECH-SEO-AUDIT-EVIDENCE-v1.md](ISEO-SU-TECH-SEO-AUDIT-EVIDENCE-v1.md) · SEO-team report [reports/ISEO-SU-TECH-SEO-AUDIT-FOR-SEO-TEAM-v1.md](reports/ISEO-SU-TECH-SEO-AUDIT-FOR-SEO-TEAM-v1.md) · task REPORT [reports/REPORT-ISEO-SU-SITE-OPS-RECIPIENT-REMOVE-AND-TECH-SEO-AUDIT-01.md](reports/REPORT-ISEO-SU-SITE-OPS-RECIPIENT-REMOVE-AND-TECH-SEO-AUDIT-01.md) · recipient restore verification (historical) [ISEO-SU-FORM-RECIPIENT-RESTORATION-EVIDENCE-v1.md](ISEO-SU-FORM-RECIPIENT-RESTORATION-EVIDENCE-v1.md) · all-forms isolated mail acceptance (historical current for acceptance) [ISEO-SU-FORM-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-EVIDENCE-v2.md](ISEO-SU-FORM-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-EVIDENCE-v2.md) · REPORT [reports/REPORT-ISEO-SU-SITE-OPS-FORM-ANTISPAM-AND-VALIDATION-01.md](reports/REPORT-ISEO-SU-SITE-OPS-FORM-ANTISPAM-AND-VALIDATION-01.md) · acceptance REPORT [reports/REPORT-ISEO-SU-SITE-OPS-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-02.md](reports/REPORT-ISEO-SU-SITE-OPS-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-02.md) · Acceptance 01 recipient evidence [SUPERSEDED](reports/REPORT-ISEO-SU-SITE-OPS-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-01.md)

---

## Knowledge authority order (site tasks)

1. Task-specific accepted production evidence  
2. [ISEO-SU-CURRENT-STATE-v1.md](ISEO-SU-CURRENT-STATE-v1.md)  
3. [ISEO-SU-TASK-ROUTING-GUIDE-v1.md](ISEO-SU-TASK-ROUTING-GUIDE-v1.md)  
4. [ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md](ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md)  
5. [ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md](ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md)  
6. Component maps (page/source, WP objects, static PHP, forms/web-KP, global components)  
7. Historical intake / Phase 0–6C-P / launch REPORTs (immutable)

---

## Sibling / supporting programmes

| Programme | Path | Role relative to this locus |
|-----------|------|-----------------------------|
| **WPilot** | `projects/wpilot/` | WordPress pilot programme + plugin contracts |
| **i-SEO Report Hub** | `projects/iseo-report-hub/` | Sibling product; `/report-hub/` on site |
| **Website Factory** | `projects/mars-website-factory/` | Methodology only |
| **Forge WordPress** | `projects/mars-website-factory/subsystems/forge-wordpress/` | Safety methodology |
| **ATLAS** | `projects/atlas/` | Identity registry — mint deferred |
| **Survivability / GitGuard** | `projects/mars-survivability/` | Safety methodology |
| **MLI** | `projects/mars-localhost-infrastructure/` | Mirror deferred |
| **Remote Operations Layer** | `projects/remote-operations-layer/` | Methodology only |

---

## Current authority order (programme)

1. `AGENTS.md` / `.cursorrules` / `governance/mars-x-drive-root-authority-v1.md`
2. This programme locus: `projects/iseo-su-site-ops/`
3. Supporting methodology from siblings — patterns only
4. Operator decisions in Decision Register
5. Chat handoffs — supporting evidence only

---

## Core Run (ordinary site task)

| Step | Action |
|------|--------|
| 1 | Read [CURRENT STATE](ISEO-SU-CURRENT-STATE-v1.md) then this OPERATIONAL-INDEX |
| 2 | Confirm fresh Beget backup for mutation tasks |
| 3 | Open Task Routing Guide + Route Ownership Matrix |
| 4 | Classify target; identify SoT and protected deps |
| 5 | Credentials only from local-only files — never paste secrets |
| 6 | Execute only the authorized concrete task |
| 7 | Validate public routes; close with REPORT if tasked |

**No additional generic onboarding phase is required.**

---

## Active HOLDs

| HOLD | Status |
|------|--------|
| Production **write** without exact charter + backup | **HOLD** |
| Beget panel login by agent | **HOLD** |
| Unchartered SFTP / WP Admin mutation | **HOLD** |
| WPilot bridge / writes / REST smoke | **HOLD** (6D) |
| Database / phpMyAdmin | **HOLD** |
| ATLAS mint | **DEFERRED** |
| Local mirror | **DEFAULT DEFER** |
| Firefox Browser Workstation implementation | **DEFERRED** |

---

## Next authorized task

**Glossary programme:** **closed and stabilized**. No open glossary launch work. Do not publish non-eligible without a new charter.

**Ordinary site work:** select one of the four current open task groups or another exact operator-chartered task after fresh Beget backup; start from Current State + Knowledge Base + Task Routing Guide.

**Optional parallel gate:** Phase 6D WPilot bridge + read-only smoke — only after both exact approval lines (does not block site-content tasks).

---

## Artifact navigation (current first)

<details>
<summary>Expanded artifact navigation (historical and specialized)</summary>

| Artifact | Path |
|----------|------|
| **Current state (brain)** | [ISEO-SU-CURRENT-STATE-v1.md](ISEO-SU-CURRENT-STATE-v1.md) |
| **Stabilization closeout** | [ISEO-SU-STABILIZATION-CLOSEOUT-v1.md](ISEO-SU-STABILIZATION-CLOSEOUT-v1.md) |
| Final launch closeout | [ISEO-SU-FINAL-LAUNCH-CLOSEOUT-v1.md](ISEO-SU-FINAL-LAUNCH-CLOSEOUT-v1.md) |
| Glossary final production baseline | [ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md](ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md) |
| Glossary architecture / content model | [ISEO-SU-GLOSSARY-ARCHITECTURE-AND-CONTENT-MODEL-v1.md](ISEO-SU-GLOSSARY-ARCHITECTURE-AND-CONTENT-MODEL-v1.md) |
| Glossary final corpus | [ISEO-SU-GLOSSARY-FINAL-CORPUS-v1.md](ISEO-SU-GLOSSARY-FINAL-CORPUS-v1.md) |
| Glossary Batch 01 manifest | [ISEO-SU-GLOSSARY-BATCH-01-MANIFEST-v1.md](ISEO-SU-GLOSSARY-BATCH-01-MANIFEST-v1.md) |
| Glossary Batch 02 manifest | [ISEO-SU-GLOSSARY-BATCH-02-MANIFEST-v1.md](ISEO-SU-GLOSSARY-BATCH-02-MANIFEST-v1.md) |
| Glossary Batch 03 manifest | [ISEO-SU-GLOSSARY-BATCH-03-MANIFEST-v1.md](ISEO-SU-GLOSSARY-BATCH-03-MANIFEST-v1.md) |
| Glossary Batch 04 manifest | [ISEO-SU-GLOSSARY-BATCH-04-MANIFEST-v1.md](ISEO-SU-GLOSSARY-BATCH-04-MANIFEST-v1.md) |
| Glossary publication eligibility | [ISEO-SU-GLOSSARY-PUBLICATION-ELIGIBILITY-v1.md](ISEO-SU-GLOSSARY-PUBLICATION-ELIGIBILITY-v1.md) |
| Glossary publication launch manifest | [ISEO-SU-GLOSSARY-PUBLICATION-LAUNCH-MANIFEST-v1.md](ISEO-SU-GLOSSARY-PUBLICATION-LAUNCH-MANIFEST-v1.md) |
| Glossary publication backup/rollback | [ISEO-SU-GLOSSARY-PUBLICATION-BACKUP-AND-ROLLBACK-v1.md](ISEO-SU-GLOSSARY-PUBLICATION-BACKUP-AND-ROLLBACK-v1.md) |
| Glossary publication launch CSV | [data/glossary-editorial/ISEO-SU-GLOSSARY-PUBLICATION-LAUNCH-v1.csv](data/glossary-editorial/ISEO-SU-GLOSSARY-PUBLICATION-LAUNCH-v1.csv) |
| Glossary research register | [ISEO-SU-GLOSSARY-RESEARCH-REGISTER-v1.md](ISEO-SU-GLOSSARY-RESEARCH-REGISTER-v1.md) |
| Glossary term audit summary | [ISEO-SU-GLOSSARY-TERM-AUDIT-v1.md](ISEO-SU-GLOSSARY-TERM-AUDIT-v1.md) |
| Glossary term audit CSV | [data/glossary-editorial/ISEO-SU-GLOSSARY-TERM-AUDIT-v1.csv](data/glossary-editorial/ISEO-SU-GLOSSARY-TERM-AUDIT-v1.csv) |
| Glossary pilot batch | [ISEO-SU-GLOSSARY-PILOT-BATCH-v1.md](ISEO-SU-GLOSSARY-PILOT-BATCH-v1.md) |
| Glossary SEO / linking model | [ISEO-SU-GLOSSARY-SEO-AND-INTERNAL-LINKING-MODEL-v1.md](ISEO-SU-GLOSSARY-SEO-AND-INTERNAL-LINKING-MODEL-v1.md) |
| Glossary intake register | [ISEO-SU-GLOSSARY-TERM-INTAKE-REGISTER-v1.md](ISEO-SU-GLOSSARY-TERM-INTAKE-REGISTER-v1.md) |
| Glossary source material register | [ISEO-SU-GLOSSARY-SOURCE-MATERIAL-REGISTER-v1.md](ISEO-SU-GLOSSARY-SOURCE-MATERIAL-REGISTER-v1.md) |
| Glossary canonical source (Nikita v1) | [materials/glossary/ISEO-SU-GLOSSARY-SOURCE-NIKITA-v1.xlsx](materials/glossary/ISEO-SU-GLOSSARY-SOURCE-NIKITA-v1.xlsx) · SHA-256 `f7651cffc5d03c497062ac6ee5b6288d9397ae5abede43fbd19f1a3ea26699de` |
| Glossary materials README | [materials/glossary/README.md](materials/glossary/README.md) |
| Glossary template component map | [ISEO-SU-GLOSSARY-TEMPLATE-COMPONENT-MAP-v1.md](ISEO-SU-GLOSSARY-TEMPLATE-COMPONENT-MAP-v1.md) |
| Glossary page_scene services alignment evidence | [ISEO-SU-GLOSSARY-PAGE-SCENE-SERVICES-ALIGNMENT-EVIDENCE-v1.md](ISEO-SU-GLOSSARY-PAGE-SCENE-SERVICES-ALIGNMENT-EVIDENCE-v1.md) |
| Glossary manual CSS promotion evidence | [ISEO-SU-GLOSSARY-MANUAL-CSS-PROMOTION-EVIDENCE-v1.md](ISEO-SU-GLOSSARY-MANUAL-CSS-PROMOTION-EVIDENCE-v1.md) |
| Glossary archive layout fix evidence | [ISEO-SU-GLOSSARY-ARCHIVE-LAYOUT-FIX-EVIDENCE-v1.md](ISEO-SU-GLOSSARY-ARCHIVE-LAYOUT-FIX-EVIDENCE-v1.md) |
| Task routing guide | [ISEO-SU-TASK-ROUTING-GUIDE-v1.md](ISEO-SU-TASK-ROUTING-GUIDE-v1.md) |
| Route ownership matrix | [ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md](ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md) |
| Knowledge base | [ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md](ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md) |
| Site route register | [ISEO-SU-SITE-ROUTE-REGISTER-v1.md](ISEO-SU-SITE-ROUTE-REGISTER-v1.md) |
| Page-to-source map | [ISEO-SU-PAGE-TO-SOURCE-MAP-v1.md](ISEO-SU-PAGE-TO-SOURCE-MAP-v1.md) |
| WP object/template map | [ISEO-SU-WORDPRESS-OBJECT-AND-TEMPLATE-MAP-v1.md](ISEO-SU-WORDPRESS-OBJECT-AND-TEMPLATE-MAP-v1.md) |
| Static PHP ownership | [ISEO-SU-STATIC-PHP-FILE-OWNERSHIP-MAP-v1.md](ISEO-SU-STATIC-PHP-FILE-OWNERSHIP-MAP-v1.md) |
| Forms/calc/web-KP | [ISEO-SU-FORMS-CALCULATORS-AND-WEB-KP-MAP-v1.md](ISEO-SU-FORMS-CALCULATORS-AND-WEB-KP-MAP-v1.md) |
| Global components | [ISEO-SU-GLOBAL-COMPONENT-DEPENDENCY-MAP-v1.md](ISEO-SU-GLOBAL-COMPONENT-DEPENDENCY-MAP-v1.md) |
| Protected zones | [ISEO-SU-PROTECTED-ZONES-v1.md](ISEO-SU-PROTECTED-ZONES-v1.md) |
| SAFE UNKNOWN | [ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md](ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md) |
| Artifact register | [ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md](ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md) |

Additional historical artifacts remain listed in the Artifact Register.

</details>

## REPORT navigation (latest)

<details>
<summary>Historical REPORT navigation</summary>

| Report | Status |
|--------|--------|
| [Final stabilization and housekeeping](reports/REPORT-ISEO-SU-SITE-OPS-FINAL-STABILIZATION-AND-HOUSEKEEPING.md) | **COMPLETE — ISEO-SU SITE OPS STABILIZED / WORKSPACE CLEAN / MARS BRAIN CURRENT / GIT CLOSED** |
| [Final post-launch and git sync closeout](reports/REPORT-ISEO-SU-SITE-OPS-FINAL-POST-LAUNCH-AND-GIT-SYNC-CLOSEOUT.md) | **COMPLETE — ISEO-SU POST-LAUNCH VERIFIED / CANONICAL REMOTE SYNCED / SITE OPS CLOSEOUT COMPLETE** |
| [Glossary final integration and closeout](reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-FINAL-INTEGRATION-AND-CLOSEOUT.md) | **COMPLETE — GLOSSARY FINAL INTEGRATION COMPLETE / PRODUCTION BASELINE FROZEN** |
| [Glossary page_scene services alignment](reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-PAGE-SCENE-SERVICES-ALIGNMENT.md) | **COMPLETE — GLOSSARY HERO ALIGNED TO SERVICES / SECOND-SCREEN CTA WORKING** |
| [Glossary publication readiness and controlled launch](reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-PUBLICATION-READINESS-AND-CONTROLLED-LAUNCH.md) | **COMPLETE — PUBLIC GLOSSARY LAUNCHED / ELIGIBLE CANONICAL CORPUS LIVE** |
| [Glossary Batch 04 final content completion](reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-BATCH-04-FINAL-CONTENT-COMPLETION.md) | **COMPLETE — GLOSSARY SAFE CONTENT CORPUS COMPLETE WITH DEFERRED EDGE CASES** |
| [Glossary Batch 03](reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-BATCH-03.md) | **COMPLETE — GLOSSARY BATCH 03 LOADED AS DRAFTS** |
| [Glossary Batch 01 refinement and Batch 02](reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-BATCH-01-REFINEMENT-AND-BATCH-02.md) | **COMPLETE — GLOSSARY BATCH 01 REFINED / BATCH 02 LOADED AS DRAFTS** |
| [Glossary final corpus and Batch 01 content](reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-FINAL-CORPUS-AND-BATCH-01-CONTENT.md) | **COMPLETE — GLOSSARY FINAL CORPUS SET / BATCH 01 LOADED AS DRAFTS** |
| [Glossary archive empty-state and layout fix](reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-ARCHIVE-EMPTY-STATE-AND-LAYOUT-FIX.md) | COMPLETE |
| [Glossary editorial audit and pilot](reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-EDITORIAL-AUDIT-AND-PILOT.md) | **COMPLETE — GLOSSARY EDITORIAL MODEL READY / PILOT PREPARED** |
| [Glossary source material canonicalization](reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-SOURCE-MATERIAL-CANONICALIZATION.md) | **COMPLETE — GLOSSARY SOURCE MATERIAL CANONICALIZED / PROJECT BRAIN PERSISTED** |
| [Glossary architecture template and content intake](reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-ARCHITECTURE-TEMPLATE-AND-CONTENT-INTAKE.md) | **COMPLETE — GLOSSARY FOUNDATION READY / TERMS IMPORTED AS DRAFTS** |
| [Architecture route knowledge capture](reports/REPORT-ISEO-SU-SITE-OPS-COMPLETE-PRODUCTION-ARCHITECTURE-ROUTE-KNOWLEDGE-CAPTURE.md) | **COMPLETE / ARCHITECTURE KNOWLEDGE READY** |
| Phase 6D WPilot bridge smoke | BLOCKED / PRODUCTION UNCHANGED |
| Phase 6C-P onboarding evidence persistence | COMPLETE |

</details>

---

*ISEO-SU-SITE-OPS Operational Index · current-state reconciliation 2026-08-24 · four open technical task groups · glossary complete · WPilot 6D optional.*
