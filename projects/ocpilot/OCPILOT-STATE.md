# OCPilot — Program State

**Status:** living state document — **not** automated router  
**Last updated:** 2026-07-06
**Evidence cutoff:** 2026-07-06 (SITE-002 Run **4.198** — information meta runtime discovery; corporate custom-controller authority mapped; checkpoint unchanged `SITE-002-STABLE-PROD-SITEMAP-01`)
**Frozen snapshot (2026-06-01):** [freeze/site-001-pre-runtime-bridge/OCPILOT-STATE-SUMMARY-v1.md](freeze/site-001-pre-runtime-bridge/OCPILOT-STATE-SUMMARY-v1.md)

---

## Program summary

| Item | State |
|------|--------|
| OCPilot phase | Runs **1** through **4.99** **DONE**; Runs **4.100–4.121** **DONE**; Run **5** initialized, **paused** |
| Implementation in repo | **None claimed** — documentation + human-operated workflows |
| First project site | **SITE-001** — Автосалон СИБКАР (TEST) |
| Second project site | **SITE-002** — ЗПМ — **PRODUCTION REGISTERED** (`https://bzpm.ru/`) · TEST history complete on `https://zpm.new-site.space/` |
| Current SITE-001 focus | **WF-V2-W2 Flat Used PDP DONE** on TEST (2026-06-10); [SITE-001-WFV2-W2-FLAT-PDP-EXECUTION-v1.md](sites/site-001/reports/SITE-001-WFV2-W2-FLAT-PDP-EXECUTION-v1.md) · [SITE-001-WFV2-W2-FLAT-PDP-DECISION-v1.md](sites/site-001/reports/SITE-001-WFV2-W2-FLAT-PDP-DECISION-v1.md); automated **PASS**; operator visual HITL **PENDING**; WF-V2-W3 **NOT AUTHORIZED**; backup `pre-wfv2-w2-flat-pdp-20260610-0304` |
| Current SITE-002 focus | **Information meta runtime discovery (Run 4.198)** — corp meta authority = custom controllers · next `SITE-002-PROD-SEO-INFORMATION-META-RUNTIME-FIX-01` · [SITE-002-PROD-SEO-INFORMATION-META-RUNTIME-DISCOVERY-01.md](sites/site-002/reports/SITE-002-PROD-SEO-INFORMATION-META-RUNTIME-DISCOVERY-01.md) |

---

## SITE-002 — current state

### Production environment (2026-07-02)

| Field | Value |
|-------|--------|
| SITE-002 Production environment | **REGISTERED** |
| Production URL | https://bzpm.ru/ |
| Environment ID | `site-002-prod` |
| Production Profile | [sites/site-002/production-profile.md](sites/site-002/production-profile.md) |
| Production capture (Run 4.171 / 4.171-R1) | **COMPLETE** — [SITE-002-FIRST-PRODUCTION-CAPTURE.md](sites/site-002/reports/SITE-002-FIRST-PRODUCTION-CAPTURE.md) |
| FTP/SFTP connection | **VERIFIED** (read-only) — application `/bzpm.ru/`; FTP chroot `/` → `/public_html/` + `/storage/` |
| HTTP verification | **VERIFIED** (homepage + corp pages) |
| OpenCart admin read-only | **VERIFIED** — version 3.0.3.9 |
| Historical TEST | **preserved** — https://zpm.new-site.space/ |
| First Production baseline | **SUPERSEDED BY CONTROLLED TEXT CHANGE** — parent [SITE-002-STABLE-PROD-INITIAL-01.md](sites/site-002/baselines/SITE-002-STABLE-PROD-INITIAL-01.md) |
| Current Production checkpoint | **ISSUED** — [SITE-002-STABLE-PROD-NEUTRAL-CATEGORY-IMAGES-WHITE-BG-01.md](sites/site-002/baselines/SITE-002-STABLE-PROD-NEUTRAL-CATEGORY-IMAGES-WHITE-BG-01.md) (parent [SITE-002-STABLE-PROD-NEUTRAL-PARENT-CATEGORIES-01.md](sites/site-002/baselines/SITE-002-STABLE-PROD-NEUTRAL-PARENT-CATEGORIES-01.md); cron [SITE-002-STABLE-PROD-CRON-SCHEDULED-RUN-01.md](sites/site-002/baselines/SITE-002-STABLE-PROD-CRON-SCHEDULED-RUN-01.md); SEO [SITE-002-STABLE-PROD-SITEMAP-01.md](sites/site-002/baselines/SITE-002-STABLE-PROD-SITEMAP-01.md)) |
| First Production test / operation | **COMPLETE** — single-file text-only FTP deploy verified (Run 4.173) |
| Second Production operation | **COMPLETE** — single-controller catalog sort deploy verified (Run 4.176) |
| Third Production operation | **COMPLETE** — single-Twig catalog sort menu deploy verified (Run 4.177) |
| Fourth Production operation | **COMPLETE** — parallel MARS 1C cron wrapper prepared (Run 4.178) — **cron not activated** |
| Fifth Production operation | **COMPLETE** — MARS 1C wrapper TXT reports (Run 4.179) — **cron not activated** |
| Sixth Production operation | **PARTIAL** — MARS 1C cron activation preflight (Run 4.180) — token config ready; manual run pending; **cron not activated** |
| Seventh Production operation | **COMPLETE** — MARS 1C cron manual run (Run 4.181) — first wrapper import **SUCCESS**; Beget cron **not activated**; activation **ready** |
| Eighth Production operation | **READY** — Beget 1C cron activation (Run 4.182) — wrapper gates PASS; operator panel action required; cron row **not created** |
| Ninth Production operation | **COMPLETE** — Beget 1C cron active confirmation (Run 4.183) — operator cron row confirmed; daily schedule active; next run monitoring pending; **no import in operation** |
| Tenth Production operation | **COMPLETE** — 1C cron reports cleanup (Run 4.184) — 19 redundant setup-date TXT reports deleted; manual run SUCCESS + latest status + index guard preserved; **no import in operation** |
| Eleventh Production operation | **COMPLETE** — catalog load more (Run 4.185) — 4-file deploy; append UX + counter verified; cron/import/mail **untouched** |
| Twelfth Production operation | **COMPLETE** — mail recipients discovery (Run 4.186) — read-only FTP map; handler `checkout/anketa.php`; recipients via `config_mail_alert_email`; **no Production mutation** |
| Thirteenth Production operation | **COMPLETE** — mail recipients admin add confirmation (Run 4.187) — operator updated `config_mail_alert_email` in OpenCart admin; delivery verified; **no code deploy**; `anketa.php` + SMTP unchanged |
| Fourteenth Production operation | **PARTIAL** — SEO readiness and robots (Run 4.188) — non-product meta audit; robots.txt single-file deploy verified; sitemap not found; Yandex Twig **SAFE UNKNOWN** at audit time; meta fix plan ready |
| Fifteenth Production operation | **COMPLETE** — Yandex codes verification (Run 4.189) — read-only FTP + HTTP; Metrika + Webmaster **VERIFIED** on live; operator Twig WIP protected; **no Production mutation** |
| Sixteenth Production operation | **COMPLETE** — HTML body duplicate fix (Run 4.190) — single-file `header.twig` deploy; duplicate body/preloader/overlay removed; Yandex preserved; 4-URL HTML validation **PASS** |
| Seventeenth Production operation | **COMPLETE** — sitemap enable (Run 4.191) — OpenCart Google Sitemap feed enabled; valid XML at `/sitemap.xml` (1320 URLs); robots.txt `Sitemap:` directive deployed; Yandex + single body preserved |
| Eighteenth Production operation | **COMPLETE** — first scheduled Beget 1C cron run verification (Run 4.194) — automatic run SUCCESS at 08:00 Moscow; report `mars_1c_import_2026-07-06_080007.txt`; daily 1C import **OPERATIONAL**; checkpoint `SITE-002-STABLE-PROD-CRON-SCHEDULED-RUN-01`; **no import in operation** |
| Nineteenth Production operation | **COMPLETE** — neutral parent categories rollout (Run 4.195) — 4 new branches + WebP images; `category_visibility.php` 5→9 IDs; homepage/hub tiles verified; admin image fields only; **COMPOSER_ONLY_NO_API**; SEO/cron/header untouched |
| Twentieth Production operation | **COMPLETE** — neutral category images white-bg refresh (Run 4.196) — 3 images refreshed (354/358/86); ID 331 kept; master+cache FTP overwrite; **COMPOSER_ONLY_NO_API**; layout/SEO/cron/Yandex untouched |
| Twenty-first Production operation | **COMPLETE** — polki category image fix (Run 4.197) — ID 331 refreshed; master+cache FTP overwrite; stale dark cache replaced; **COMPOSER_ONLY_NO_API**; layout/SEO/cron/Yandex untouched |
| Capture storage | `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\captures\SITE-002-PROD-INITIAL-CAPTURE-01\` |

Production tooling remains scoped and site-specific. Verified deploy classes: **single-file text-only FTP deploy** (Run 4.173), **single-controller-file FTP deploy** (Run 4.176), **single-Twig-file FTP deploy** (Run 4.177, 4.190), **multi-file catalog frontend FTP deploy** (Run 4.185), **single-file robots.txt FTP deploy** (Run 4.188, 4.191), and **OpenCart admin single-setting enable** (Run 4.191 — Google Sitemap feed). File-level Production checkpoint is `SITE-002-STABLE-PROD-SITEMAP-01`.

### BZPM UX REDESIGN — project banner

| Field | Value |
|-------|--------|
| **Recovery status** | **CLOSED** (2026-06-28) |
| **Production status** | **READY AFTER OPERATOR GATES** |
| **Current phase** | **PRODUCTION PREPARATION** |
| **Next phase** | **Production Development** — Corporate Pages after operator gates |
| **Implementation (M9.14+)** | **M9.14–M9.18 IMPLEMENTED** (2026-06-28) — Corporate Pages Program implementation phase **COMPLETE on TEST** (pending operator B6/B8) |
| **Closeout** | [sites/site-002/reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md](sites/site-002/reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md) |

**Lifecycle:** Research → Corporate Pages Program → Recovery (**CLOSED**) → Production Development

| Field | Value |
|-------|--------|
| Site ID | SITE-002 |
| Environment | **PRODUCTION** (registered) · historical TEST preserved |
| Production URL | https://bzpm.ru/ |
| Historical TEST URL | https://zpm.new-site.space/ |
| Platform (operator-recorded) | ocStore / OpenCart |
| Version | **SAFE UNKNOWN** |
| Baseline | TEST-proven checkpoints preserved · Production baseline **pending** |
| Knowledge map | [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) |
| Authority policy | TEST-era manual UI canonical on historical TEST; **Production parity unverified** |
| Registry | Active OCPilot-managed site — TEST history complete · Production registered · Production connection pending |
| Completed | M7.1–M9.7 · Manual UI · M9.8.1/2/5 · operator PLP polish · **product reset** · **fresh 1C import** · **price index recovery (06D/06F)** · **filter hotfixes (06H/06J/06M)** · **filter UX (04–08A)** · **tooltips (01)** · **Commercial Trust (03B/03C + operator polish)** · **catalog state persistence (09A–09C)** · **hub cleanup (10)** · **M9.13 About redesign (re-activated 2026-06-29)** · **Home Commercial Trust CTA (2026-06-29)** |
| Active stage | **PRODUCTION BASELINE ISSUED** — ready for first controlled Production test |
| Open bugs | **EC-01** — mitigated by subcategories hide (07); M9.8.7 deferred |
| Next planned | **Production parity / rollout** for corp pages · operator gates B6/B8/B1 · Visual Design **NOT OPEN** · deferred M9.8.3/4/6/8 · **M10** not authorized |
| Active blockers | **B6** charter approval · **B8** copy sign-off · **B1** МО address · **B3** PLP vs `/dealers` (**governance-only** — does not block corp `/dealers` implementation) — recovery **not** a blocker |
| Corporate Pages Program | **OPEN** — [Program](../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-PROGRAM-v1.md) · [IA map](../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-IA-MAP-v1.md) · [Design program](../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md) · [Charters](../website-factory/execution-cases/bzpm-roadmap/charters/README.md) · M9.13 **RE-ACTIVATED on TEST** (2026-06-29) · M9.14+ charters **Draft complete / approval open** · Visual design **NOT OPEN** · Contacts **Delivered** (separate workstream) |
| Run 5 | **NO** — not applicable to current operational lane |
| Writes (this checkpoint) | **NO** — documentation only |
| Rollback source | Beget full backup + current live TEST + file-level pass backups |
| External secrets | External storage only — not in repo |

**Authority evidence:** [sites/site-002/baselines/SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01.md) · [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02.md) · [sites/site-002/baselines/SITE-002-STABLE-LIVE-LOCAL-FONTS-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-LOCAL-FONTS-01.md) · [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) · [sites/site-002/site-passport.md](sites/site-002/site-passport.md)

**Home Commercial Trust:** [sites/site-002/reports/SITE-002-HOME-COMMERCIAL-TRUST-REPLACEMENT.md](sites/site-002/reports/SITE-002-HOME-COMMERCIAL-TRUST-REPLACEMENT.md)

**M9.13 About re-activation:** [sites/site-002/reports/SITE-002-ABOUT-COMPANY-REDESIGN-RESTORE-V2.md](sites/site-002/reports/SITE-002-ABOUT-COMPANY-REDESIGN-RESTORE-V2.md) · [sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-M9.13-ABOUT-REDESIGN-02.md](sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-M9.13-ABOUT-REDESIGN-02.md)

**State freeze report:** [sites/site-002/reports/REPORT-BZPM-STATE-FREEZE-ROADMAP-UPDATE.md](sites/site-002/reports/REPORT-BZPM-STATE-FREEZE-ROADMAP-UPDATE.md)

**CRO backlog (input to M9.8):** [sites/site-002/reports/REPORT-BZPM-CATALOG-IMPROVEMENT-BACKLOG.md](sites/site-002/reports/REPORT-BZPM-CATALOG-IMPROVEMENT-BACKLOG.md)

**M9.8.9 registration:** [sites/site-002/reports/SITE-002-M9.8.9-MINOR-FIXES-PACK-01-REGISTRATION.md](sites/site-002/reports/SITE-002-M9.8.9-MINOR-FIXES-PACK-01-REGISTRATION.md)

**Corporate Pages Program:** [BZPM-CORPORATE-PAGES-PROGRAM-v1.md](../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-PROGRAM-v1.md) · [IA map](../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-IA-MAP-v1.md) · [Design program](../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md) · [Phase gate](../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-FINAL-PHASE-GATE-v1.md) · [Reconciliation](../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-PROGRAM-RECONCILIATION-v1.md) · [Charters](../website-factory/execution-cases/bzpm-roadmap/charters/README.md) · M9.13–M9.18 [forensic index](sites/site-002/reports/) · [copy index](sites/site-002/copy/) · [program registration](sites/site-002/reports/REPORT-BZPM-CORPORATE-PAGES-PROGRAM-REGISTRATION.md) · [copy system registration](sites/site-002/reports/REPORT-BZPM-COPY-SYSTEM-REGISTRATION.md) · [post-recovery completeness reconciliation](sites/site-002/reports/SITE-002-BZPM-POST-RECOVERY-COMPLETENESS-RECONCILIATION.md) · [recovery closeout](sites/site-002/reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md)

**Prior checkpoint (historical):** [sites/site-002/reports/SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE.md](sites/site-002/reports/SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE.md) · [sites/site-002/reports/SITE-002-STABLE-M9-COMPLETE.md](sites/site-002/reports/SITE-002-STABLE-M9-COMPLETE.md)

**Registration evidence:** [sites/site-002/reports/SITE-002-REGISTRATION-v1.md](sites/site-002/reports/SITE-002-REGISTRATION-v1.md) · [logs/ocpilot/site-002-registration-v1.md](../../logs/ocpilot/site-002-registration-v1.md)

---

## SITE-001 — current state

| Field | Value |
|-------|--------|
| Site ID | SITE-001 |
| Environment | **TEST** — `https://sibcar.new-site.space/` |
| Platform (operator-recorded) | ocStore **3.0.3.8 (rs.2)** |
| Baseline | `ocstore-3038-rs2` |
| Active theme | **`auto`** (W0.5 confirmed) |
| Registry | **READY FOR AUDIT** |
| Run 5 | Read-only audit — **paused** (EAR acquisition path) |
| W0 Discovery | **COMPLETE** |
| W0.5 Admin Discovery | **COMPLETE** |
| W1 Execution Pack | **COMPLETE** |
| W1 Pre-Execution Package | **COMPLETE** (2026-06-08) |

### Phase 1 W1 authorization (2026-06-08)

| Document | Outcome |
|----------|---------|
| [sites/site-001/reports/SITE-001-W1-EXECUTION-PACK-v1.md](sites/site-001/reports/SITE-001-W1-EXECUTION-PACK-v1.md) | Target map; waves W1A–W1F |
| [sites/site-001/reports/SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md](sites/site-001/reports/SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md) | **AUTHORIZED WITH NOTES** — C-05/C-06/C-08 **SATISFIED** (2026-06-08) |
| [sites/site-001/reports/SITE-001-W1A-AUTHORIZATION-REVIEW-v1.md](sites/site-001/reports/SITE-001-W1A-AUTHORIZATION-REVIEW-v1.md) | **AUTHORIZED WITH NOTES** — W1A may begin |
| [sites/site-001/reports/SITE-001-W1A-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W1A-EXECUTION-v1.md) | W1A execution report — **DONE** 2026-06-08 |
| [sites/site-001/reports/SITE-001-W1A-DECISION-v1.md](sites/site-001/reports/SITE-001-W1A-DECISION-v1.md) | W1A verdict — **PASS WITH NOTES** |
| [sites/site-001/reports/SITE-001-W1A-POST-AUDIT-v1.md](sites/site-001/reports/SITE-001-W1A-POST-AUDIT-v1.md) | W1A post-audit — **PASS** (Unicode / mixed-script check) |
| [sites/site-001/reports/SITE-001-W1B-THEME-BRANDING-MAP-v1.md](sites/site-001/reports/SITE-001-W1B-THEME-BRANDING-MAP-v1.md) | W1B theme branding map — discovery **DONE** 2026-06-08 |
| [sites/site-001/reports/SITE-001-W1B-AUTHORIZATION-REVIEW-v1.md](sites/site-001/reports/SITE-001-W1B-AUTHORIZATION-REVIEW-v1.md) | W1B authorization — **AUTHORIZED WITH NOTES** |
| [sites/site-001/reports/SITE-001-W1A-EXECUTION-SPEC-v1.md](sites/site-001/reports/SITE-001-W1A-EXECUTION-SPEC-v1.md) | W1A Store Settings execution table |
| [sites/site-001/reports/SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md](sites/site-001/reports/SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md) | Superseded for **planning** by W1 pack; execution still operator-gated |
| [sites/site-001/reports/SITE-001-PHASE1-STABLE-SNAPSHOT-v1.md](sites/site-001/reports/SITE-001-PHASE1-STABLE-SNAPSHOT-v1.md) | Phase 1 stable checkpoint — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-PHASE1-FINAL-AUDIT-v1.md](sites/site-001/reports/SITE-001-PHASE1-FINAL-AUDIT-v1.md) | Final audit — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-PHASE1-FINAL-AUDIT-DECISION-v1.md](sites/site-001/reports/SITE-001-PHASE1-FINAL-AUDIT-DECISION-v1.md) | Interim decision — **COMPLETE WITH NOTES** (pre-W1G) |
| [sites/site-001/reports/SITE-001-W1G-SEO-DB-CLEANUP-v1.md](sites/site-001/reports/SITE-001-W1G-SEO-DB-CLEANUP-v1.md) | W1G DB SEO cleanup — **DONE** 2026-06-09 — **PASS WITH NOTES** |
| [sites/site-001/reports/SITE-001-PHASE1-FINAL-ACCEPTANCE-v1.md](sites/site-001/reports/SITE-001-PHASE1-FINAL-ACCEPTANCE-v1.md) | Phase 1 final acceptance — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-PHASE1-FINAL-DECISION-v1.md](sites/site-001/reports/SITE-001-PHASE1-FINAL-DECISION-v1.md) | Final decision — **PHASE 1 ACCEPTED WITH NOTES** |
| [sites/site-001/reports/SITE-001-PHASE1-STABLE-CHECKPOINT-v1.md](sites/site-001/reports/SITE-001-PHASE1-STABLE-CHECKPOINT-v1.md) | Phase 1 stable checkpoint — **ACTIVE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-PHASE1-STABLE-CHECKPOINT-DECISION-v1.md](sites/site-001/reports/SITE-001-PHASE1-STABLE-CHECKPOINT-DECISION-v1.md) | Checkpoint decision — **APPROVED** |
| [knowledge/OCPILOT-RULE-CONTROLLER-META-GENERATORS-v1.md](knowledge/OCPILOT-RULE-CONTROLLER-META-GENERATORS-v1.md) | Controller meta inspection rule — **ACTIVE** |
| [sites/site-001/reports/SITE-001-W2-VISUAL-REFRESH-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W2-VISUAL-REFRESH-DISCOVERY-v1.md) | W2 visual/UI discovery — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W2-VISUAL-REFRESH-DECISION-v1.md](sites/site-001/reports/SITE-001-W2-VISUAL-REFRESH-DECISION-v1.md) | W2 discovery gate — **DISCOVERY COMPLETE** |
| [sites/site-001/reports/SITE-001-W2-VISUAL-SPECIFICATION-v1.md](sites/site-001/reports/SITE-001-W2-VISUAL-SPECIFICATION-v1.md) | W2.1 visual specification — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W2-IMPLEMENTATION-ROADMAP-v1.md](sites/site-001/reports/SITE-001-W2-IMPLEMENTATION-ROADMAP-v1.md) | W2.1 W3 roadmap — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W2-DECISION-v1.md](sites/site-001/reports/SITE-001-W2-DECISION-v1.md) | W2.1 gate — **READY FOR PHASE 2 IMPLEMENTATION** |
| [sites/site-001/reports/SITE-001-W2-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W2-WRITE-CHARTER-v1.md) | Phase 2 write charter — **ACTIVE** (2026-06-09) |
| [sites/site-001/reports/SITE-001-W2-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-W2-CHANGE-REQUEST-v1.md) | Phase 2 CR — CR-SITE-001-W3C-2026-06-09 |
| [sites/site-001/reports/SITE-001-W3C-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3C-DISCOVERY-v1.md) | W3-C discovery — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W3C-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3C-EXECUTION-v1.md) | W3-C execution — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W3C-DECISION-v1.md](sites/site-001/reports/SITE-001-W3C-DECISION-v1.md) | W3-C decision — **PASS WITH NOTES** |
| [sites/site-001/reports/SITE-001-W3C-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-W3C-ROLLBACK-PLAN-v1.md) | W3-C rollback instance |
| [sites/site-001/reports/SITE-001-W3C-ROLLBACK-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3C-ROLLBACK-EXECUTION-v1.md) | W3-C T1 rollback — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W3C-ROLLBACK-DECISION-v1.md](sites/site-001/reports/SITE-001-W3C-ROLLBACK-DECISION-v1.md) | W3-C rollback verdict — **PASS** |
| [sites/site-001/reports/SITE-001-W3V-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W3V-WRITE-CHARTER-v1.md) | W3-V write charter — **ACTIVE** |
| [sites/site-001/reports/SITE-001-W3V-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-W3V-CHANGE-REQUEST-v1.md) | W3-V CR — CR-SITE-001-W3V-2026-06-09 |
| [sites/site-001/reports/SITE-001-W3V-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-W3V-ROLLBACK-PLAN-v1.md) | W3-V rollback instance |
| [sites/site-001/reports/SITE-001-W3V-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3V-DISCOVERY-v1.md) | W3-V discovery — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W3V-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3V-EXECUTION-v1.md) | W3-V execution — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W3V-DECISION-v1.md](sites/site-001/reports/SITE-001-W3V-DECISION-v1.md) | W3-V decision — **PASS WITH NOTES** |
| [sites/site-001/reports/SITE-001-W3UX-DENSITY-AUDIT-v1.md](sites/site-001/reports/SITE-001-W3UX-DENSITY-AUDIT-v1.md) | W3-UX density audit — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W3UX-DENSITY-DECISION-v1.md](sites/site-001/reports/SITE-001-W3UX-DENSITY-DECISION-v1.md) | W3-UX discovery gate — **DISCOVERY COMPLETE** |
| [sites/site-001/reports/SITE-001-W3UX-C1-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W3UX-C1-WRITE-CHARTER-v1.md) | W3UX-C1 write charter — **ACTIVE** |
| [sites/site-001/reports/SITE-001-W3UX-C1-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-W3UX-C1-CHANGE-REQUEST-v1.md) | W3UX-C1 CR — CR-SITE-001-W3UX-C1-2026-06 |
| [sites/site-001/reports/SITE-001-W3UX-C1-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3UX-C1-DISCOVERY-v1.md) | W3UX-C1 discovery — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W3UX-C1-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3UX-C1-EXECUTION-v1.md) | W3UX-C1 execution — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W3UX-C1-DECISION-v1.md](sites/site-001/reports/SITE-001-W3UX-C1-DECISION-v1.md) | W3UX-C1 decision — **PASS WITH NOTES** |
| [sites/site-001/reports/SITE-001-W3V2-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W3V2-WRITE-CHARTER-v1.md) | W3V2 write charter — **ACTIVE** |
| [sites/site-001/reports/SITE-001-W3V2-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-W3V2-CHANGE-REQUEST-v1.md) | W3V2 CR — CR-SITE-001-W3V2-2026-06-09 |
| [sites/site-001/reports/SITE-001-W3V2-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-W3V2-ROLLBACK-PLAN-v1.md) | W3V2 rollback instance |
| [sites/site-001/reports/SITE-001-W3V2-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3V2-DISCOVERY-v1.md) | W3V2 discovery — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W3V2-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3V2-EXECUTION-v1.md) | W3V2 execution — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W3V2-DECISION-v1.md](sites/site-001/reports/SITE-001-W3V2-DECISION-v1.md) | W3V2 decision — **PASS WITH NOTES** |
| [sites/site-001/reports/SITE-001-W3VIS-01-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3VIS-01-DISCOVERY-v1.md) | W3VIS-01 discovery — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W3VIS-01-DECISION-v1.md](sites/site-001/reports/SITE-001-W3VIS-01-DECISION-v1.md) | W3VIS-01 gate — **DISCOVERY COMPLETE** |
| [sites/site-001/reports/SITE-001-W3VIS-01A-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3VIS-01A-EXECUTION-v1.md) | W3VIS-01A execution — **DONE** then **ROLLED BACK** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W3VIS-01B-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3VIS-01B-EXECUTION-v1.md) | W3VIS-01B execution — **DONE** then **ROLLED BACK** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W3VIS-ROLLBACK-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3VIS-ROLLBACK-EXECUTION-v1.md) | W3VIS T1 rollback — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W3VIS-ROLLBACK-DECISION-v1.md](sites/site-001/reports/SITE-001-W3VIS-ROLLBACK-DECISION-v1.md) | W3VIS rollback verdict — **PASS** |
| [sites/site-001/reports/SITE-001-W3COLOR-01-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3COLOR-01-DISCOVERY-v1.md) | W3COLOR-01 discovery — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W3ATMOSPHERE-01A-VISUAL-PREVIEW-v1.md](sites/site-001/reports/SITE-001-W3ATMOSPHERE-01A-VISUAL-PREVIEW-v1.md) | W3ATMOSPHERE-01A visual preview — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md) | Website Factory design direction «Graphite Salon» — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-WEBSITE-FACTORY-IMPLEMENTATION-BRIEF-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-IMPLEMENTATION-BRIEF-v1.md) | Website Factory OCPilot brief — W3WF-01 — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-WEBSITE-FACTORY-DECISION-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-DECISION-v1.md) | Website Factory decision — **READY FOR OCPILOT IMPLEMENTATION** (superseded by Concept Workshop) |
| [sites/site-001/reports/SITE-001-WEBSITE-FACTORY-CONCEPT-WORKSHOP-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-CONCEPT-WORKSHOP-v1.md) | Website Factory concept workshop — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md) | Website Factory concept decision — **Concept B selected** |
| [sites/site-001/reports/SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1.md](sites/site-001/reports/SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1.md) | W5 first impression blueprint — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W5-FIRST-IMPRESSION-DECISION-v1.md](sites/site-001/reports/SITE-001-W5-FIRST-IMPRESSION-DECISION-v1.md) | W5 blueprint decision — **APPROVED**; 3→7/10 **YES** |
| [sites/site-001/reports/SITE-001-W5A-HEADER-SHELL-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W5A-HEADER-SHELL-EXECUTION-v1.md) | W5-A header shell — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W5A-HEADER-SHELL-DECISION-v1.md](sites/site-001/reports/SITE-001-W5A-HEADER-SHELL-DECISION-v1.md) | W5-A decision — **PASS WITH NOTES**; HITL **PENDING** |
| [sites/site-001/reports/SITE-001-W5A-STABILIZATION-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W5A-STABILIZATION-EXECUTION-v1.md) | W5-A-S stabilization — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W5A-STABILIZATION-DECISION-v1.md](sites/site-001/reports/SITE-001-W5A-STABILIZATION-DECISION-v1.md) | W5-A-S decision — **PASS WITH NOTES**; W5-A COMPLETE **NO** |
| [sites/site-001/reports/SITE-001-W5-STABLE-BACKUP-v1.md](sites/site-001/reports/SITE-001-W5-STABLE-BACKUP-v1.md) | W5 pre-W5-C stable backup — **DONE** 2026-06-10 |
| [sites/site-001/reports/SITE-001-W5C-USED-PDP-COMMERCIAL-STAGE-DESIGN-PLAN-v1.md](sites/site-001/reports/SITE-001-W5C-USED-PDP-COMMERCIAL-STAGE-DESIGN-PLAN-v1.md) | W5-C design plan — **DONE** 2026-06-10 |
| [sites/site-001/reports/SITE-001-W5C-USED-PDP-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W5C-USED-PDP-EXECUTION-v1.md) | W5-C execution — **DONE** 2026-06-10 |
| [sites/site-001/reports/SITE-001-W5C-USED-PDP-DECISION-v1.md](sites/site-001/reports/SITE-001-W5C-USED-PDP-DECISION-v1.md) | W5-C decision — **PASS WITH NOTES**; HITL **PENDING** |
| [sites/site-001/reports/SITE-001-WF-V2-GAP-ANALYSIS-v1.md](sites/site-001/reports/SITE-001-WF-V2-GAP-ANALYSIS-v1.md) | WF V2 gap analysis — **DONE** 2026-06-10 |
| [sites/site-001/reports/SITE-001-WF-V2-IMPLEMENTATION-PLAN-v1.md](sites/site-001/reports/SITE-001-WF-V2-IMPLEMENTATION-PLAN-v1.md) | WF V2 implementation plan — **APPROVED** 2026-06-10 |
| [sites/site-001/reports/SITE-001-WFV2-W1-HEADER-EXECUTION-v1.md](sites/site-001/reports/SITE-001-WFV2-W1-HEADER-EXECUTION-v1.md) | WF-V2-W1 hybrid header — **DONE** 2026-06-10 |
| [sites/site-001/reports/SITE-001-WFV2-W1-HEADER-DECISION-v1.md](sites/site-001/reports/SITE-001-WFV2-W1-HEADER-DECISION-v1.md) | WF-V2-W1 decision — **PASS WITH NOTES**; HITL **PENDING** |
| [sites/site-001/reports/SITE-001-WFV2-W2-FLAT-PDP-EXECUTION-v1.md](sites/site-001/reports/SITE-001-WFV2-W2-FLAT-PDP-EXECUTION-v1.md) | WF-V2-W2 flat used PDP — **DONE** 2026-06-10 |
| [sites/site-001/reports/SITE-001-WFV2-W2-FLAT-PDP-DECISION-v1.md](sites/site-001/reports/SITE-001-WFV2-W2-FLAT-PDP-DECISION-v1.md) | WF-V2-W2 decision — **PASS WITH NOTES**; HITL **PENDING** |
| [sites/site-001/reports/SITE-001-W3WF-01-VISUAL-IMPACT-MAP-v1.md](sites/site-001/reports/SITE-001-W3WF-01-VISUAL-IMPACT-MAP-v1.md) | W3WF-01 visual impact map — **DONE** 2026-06-09 |
| [sites/site-001/reports/SITE-001-W3WF-01-VISUAL-IMPACT-DECISION-v1.md](sites/site-001/reports/SITE-001-W3WF-01-VISUAL-IMPACT-DECISION-v1.md) | W3WF-01 visual impact decision — **READY FOR W3WF-01 IMPLEMENTATION** |
| [sites/site-001/reports/SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md](sites/site-001/reports/SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md) | Visual change failure audit — **DONE** 2026-06-09 — **mixed cause**; CSS live on TEST |

### SITE-001 Visual Change Failure Audit (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **DONE** — read-only technical audit; **no site modifications** |
| Report | [SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md](sites/site-001/reports/SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md) |
| Verdict | **Mixed cause** — CSS **is loaded and applied** on TEST; operator perception gap = **changes too weak** (incremental W3-V→W3V2→W3ATMOSPHERE) + **expectation mismatch**; secondary: **browser cache risk** (`max-age=604800`) |
| Ruled out | Wrong CSS file · CSS not loaded · post-main override · extra CSS after theme · global selector failure on catalog |
| Operator directive | **STOP** new design / atmosphere CSS until hard-refresh verification + expectation workshop |
| W3WF-01 | **ON HOLD** — superseded by Concept Workshop; do not implement |
| Evidence (local) | `.recovery-temp/site-001-visual-failure-audit*.py` outputs |

### SITE-001 W3WF-01 — visual impact map (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **DONE** — documentation only; **no site modifications** |
| Purpose | Pre-execution operator preview — what W3WF-01 will look like vs **current TEST** (W3ATMOSPHERE active) |
| Decision | **READY FOR W3WF-01 IMPLEMENTATION** — perceptual delta **LOW–MEDIUM** vs live TEST; finishing/consolidation wave |
| Honest verdict | W3ATMOSPHERE already delivered ~70–80% «Graphite Salon»; W3WF-01 = `--wf-*` governance + legacy purge + patchy-zone closure |
| Operator risk | **MEDIUM–HIGH** «это опять косметика» if expectation = second transformation |
| Next | **ON HOLD** — blocked by Visual Change Failure Audit until operator expectation reset |

### SITE-001 W5 — First Impression Blueprint (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **DONE** — documentation only; **no site modifications** |
| Design owner | **Website Factory** |
| Blueprint | [SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1.md](sites/site-001/reports/SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1.md) — architecture for header · homepage · used PDP |
| Decision | [SITE-001-W5-FIRST-IMPRESSION-DECISION-v1.md](sites/site-001/reports/SITE-001-W5-FIRST-IMPRESSION-DECISION-v1.md) — **BLUEPRINT APPROVED** |
| Final verdict | Concept B can move **3/10 → 7/10+** without full redesign — **YES** |
| Operator HITL | **PENDING** — confirm or override blueprint |
| Implementation | **STOPPED** — no OCPilot writes until W5 implementation charter |
| Phases (planning) | W5-A header shell · W5-B homepage showroom · W5-C magazine PDP · W5-D integration HITL |
| Rejected in blueprint | CSS-only waves · atmosphere tokens · W4.1 sticky continuation |
| Preserve | W3UX-C1 density · Phase 1 branding · W4 `w4-used-*` wrappers (re-group in W5-C) |

### SITE-001 W5-A — Header Shell Recomposition (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **DONE** on TEST — header DOM regroup + W5-A CSS block |
| Charter | [SITE-001-W5A-HEADER-SHELL-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W5A-HEADER-SHELL-WRITE-CHARTER-v1.md) |
| Execution | [SITE-001-W5A-HEADER-SHELL-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W5A-HEADER-SHELL-EXECUTION-v1.md) |
| Decision | [SITE-001-W5A-HEADER-SHELL-DECISION-v1.md](sites/site-001/reports/SITE-001-W5A-HEADER-SHELL-DECISION-v1.md) — **PASS WITH NOTES** |
| Backup | `pre-w5a-header-shell-20260609-2251` |
| QA | `sites/site-001/qa/w5a-header-shell-screenshots/` |
| Verify | **8/8 PASS** · W4 markers preserved · sticky removed |
| Operator HITL | **PENDING** — confirm visual acceptance after W5-A-S |
| Next | W5-B homepage showroom — **NOT AUTHORIZED** until W5-A operator COMPLETE |

### SITE-001 W5-A-S — Header Shell Stabilization (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **DONE** on TEST — promo fix · dropdown recovery · nav density · responsive audits |
| Charter | [SITE-001-W5A-STABILIZATION-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W5A-STABILIZATION-WRITE-CHARTER-v1.md) |
| Execution | [SITE-001-W5A-STABILIZATION-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W5A-STABILIZATION-EXECUTION-v1.md) |
| Decision | [SITE-001-W5A-STABILIZATION-DECISION-v1.md](sites/site-001/reports/SITE-001-W5A-STABILIZATION-DECISION-v1.md) — **PASS WITH NOTES** |
| Backup | `pre-w5a-stabilization-20260609-2325` |
| QA | `sites/site-001/qa/w5a-stabilization-screenshots/` |
| Verify | **8/8 PASS** · interactions **PASS** · responsive 1920–768 **PASS** |
| W5-A COMPLETE | **NO** — operator HITL criterion 5 **PENDING** |
| Next | Operator W5-A sign-off → W5-B charter |

### SITE-001 Website Factory — Concept Workshop (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **DONE** — documentation only; **no site modifications** |
| Design owner | **Website Factory** (visual director / UX strategist) |
| Implementation owner | **OCPilot** — execution only; design invention **FORBIDDEN** |
| Workshop | [SITE-001-WEBSITE-FACTORY-CONCEPT-WORKSHOP-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-CONCEPT-WORKSHOP-v1.md) — 3 concepts (A/B/C) |
| Decision | [SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md) — **Concept B «Современный Дилер 2026»** |
| Operator HITL | **PENDING** — confirm or override Concept B (superseded by W5 blueprint HITL) |
| Implementation | **STOPPED** — no OCPilot writes until W5 implementation charter |
| 3-second test | Concept B **PASS** (modern dealership); baseline **3/10** → target **7/10** |
| Rejected | Concept A (too incremental) · Concept C (brand mismatch) · sticky header · W3WF-01 atmosphere |
| Scope | Header · homepage first screen · used PDP first screen only |
| Preserve | W3UX-C1 density · Phase 1 branding · W4 twig wrappers (re-skin in B) |

### SITE-001 Website Factory — design direction «Graphite Salon» (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **SUPERSEDED** for first-impression scope by Concept Workshop |
| Prior direction | **«Graphite Salon»** — [SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md) |
| Prior decision | **READY FOR OCPILOT IMPLEMENTATION** → **ON HOLD** |
| W3WF-01 | **ON HOLD** — do not implement |
| Note | Atmosphere tokens may inform future waves; not first-impression driver |

### SITE-001 W3ATMOSPHERE — atmosphere refresh (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **DONE** — **PASS WITH NOTES** (2026-06-09) |
| Discovery | [SITE-001-W3COLOR-01-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3COLOR-01-DISCOVERY-v1.md) — **DONE** |
| Visual preview | [SITE-001-W3ATMOSPHERE-01A-VISUAL-PREVIEW-v1.md](sites/site-001/reports/SITE-001-W3ATMOSPHERE-01A-VISUAL-PREVIEW-v1.md) — **DONE** |
| Execution | [SITE-001-W3ATMOSPHERE-01-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3ATMOSPHERE-01-EXECUTION-v1.md) — **DONE** |
| Decision | [SITE-001-W3ATMOSPHERE-01-DECISION-v1.md](sites/site-001/reports/SITE-001-W3ATMOSPHERE-01-DECISION-v1.md) — **PASS WITH NOTES** |
| Scope | Site-wide atmosphere — canvas, header/footer shell, card language, forms, depth — CSS-only |
| Backup | `pre-w3atmosphere-01-20260609-1156` (external storage) |
| Superseded for design authority | Website Factory «Graphite Salon» — W3WF-01 consolidates |
| Preserve on write | W3UX-C1 `.used_catalog` density · W3-V · Phase 1 checkpoint · no PDP hero/CTA hierarchy |
| Expected user-visible change | **YES** — ~6/10 sitewide; catalog/footer/header strongest |

### SITE-001 W3VIS-01A / W3VIS-01B (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **ROLLED BACK** — T1 restore 2026-06-09 (operator: task drift — PDP hero hierarchy not requested) |
| Original execution | W3VIS-01A **DONE** · W3VIS-01B **DONE** 2026-06-09 on TEST |
| Scope (reverted) | PDP hero surface system (01A) · commercial hierarchy / CTA order (01B) — CSS-only |
| Rollback verdict | **PASS** — 9/9 URLs verified post-restore |
| Backup used | `pre-w3vis-01a-20260609-0517` (external storage) — removes both 01A and 01B blocks |
| W3UX-C1 | **PRESERVED** — marker confirmed live post-rollback |
| Evidence (local) | `.recovery-temp/site-001-w3vis-rollback-result.json` |

### SITE-001 W3VIS-01 Visual Hierarchy & Surface System (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **DISCOVERY DONE** — reference only; execution direction superseded by Global Palette Refresh |
| Scope | Hierarchy failures · surface levels · PDP hero · CTA tiers · catalog/home analysis |
| Verdict | **DISCOVERY COMPLETE** — W3VIS-01A/01B execution **ROLLED BACK** |
| Evidence (local) | `.recovery-temp/site-001-w3vis-01-probe.json` |

### SITE-001 W3V2 Visual Identity Refresh (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **DONE** — CSS-only visual identity layer on TEST |
| Scope | Color tokens, depth, cards, buttons, header/footer visuals, forms |
| Verdict | **PASS WITH NOTES** — operator browser sign-off **PENDING** |
| Verification | **7/7** URLs PASS · live CSS W3V2 block confirmed |
| Backup | `pre-w3v2-20260609-0451` (external storage) |
| Evidence (local) | `.recovery-temp/site-001-w3v2-result.json` · `sites/site-001/qa/w3v2-screenshots/` |
| Structural changes | **NONE** · W3UX-C1 density **preserved** |

### SITE-001 W3UX-C1 Used Catalog Card Density (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **DONE** — CSS-only density optimization on TEST |
| Scope | `.used_catalog` — used catalog cards on `/cars/` route family only |
| Verdict | **PASS WITH NOTES** — desktop/tablet −24%; mobile +7% (N-W3UX-C1-02) |
| Verification | **5/5** URLs PASS · live CSS W3UX-C1 block confirmed |
| Backup | `pre-w3ux-c1-20260609-0416` (external storage) |
| Evidence (local) | `.recovery-temp/site-001-w3ux-c1-result.json` · `sites/site-001/qa/w3ux-c1-screenshots/` |
| Structural changes | **NONE** |

### SITE-001 W3-UX Density Discovery (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **DONE** — discovery only; no site modifications |
| Scope | Catalog/card/PDP/homepage density audit — spacing & hierarchy |
| Verdict | **DISCOVERY COMPLETE** — ready for W3-UX execution charter |
| Root cause | Visual density / hierarchy — not W3-V colors/radius/shadows |
| Evidence (local) | `.recovery-temp/site-001-w3ux-density-probe.json` |
| Implementation | **NOT AUTHORIZED** (superseded by W3UX-C1 execution) |

### SITE-001 W3-V Visual Layer Refresh (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **DONE** — CSS-only visual refresh on TEST |
| Scope | `css/main.css` + `css/media.css` — tokens, buttons, forms, cards, shadows, hierarchy |
| Verdict | **PASS WITH NOTES** — operator browser sign-off **PENDING** |
| Verification | **7/7** URLs PASS · live CSS W3-V block confirmed |
| Backup | `pre-w3v-20260609-0327` (external storage) |
| Evidence (local) | `.recovery-temp/site-001-w3v-result.json` |
| Structural changes | **NONE** — lesson from W3-C rollback applied |

### SITE-001 W3-C Footer Reduction (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **ROLLED BACK** — T1 restore 2026-06-09 (operator: visual direction not accepted) |
| Original execution | **DONE** 2026-06-09 — first Phase 2 write on TEST; verdict was **PASS WITH NOTES** |
| Scope (reverted) | Footer spacing compression · legal `<details>` collapse · catalog link density |
| Rollback verdict | **PASS** — 7/7 URLs verified post-restore |
| Backup | `pre-w3c-20260609-0259` (external storage) — used for T1 restore |
| Evidence (local) | `.recovery-temp/site-001-w3c-rollback-result.json` |

### SITE-001 W2.1 Visual Specification (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **COMPLETE** — documentation only |
| Scope | Visual spec · W3-A…F roadmap · implementation gate |
| Verdict | **READY FOR PHASE 2 IMPLEMENTATION** — W3 execution **NOT AUTHORIZED** until Phase 2 write charter |
| Recommended first write | **W2-PRE** (CSS tokens) → **W3-A** (catalog) |

### SITE-001 W2 Visual Refresh Discovery (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **COMPLETE** — read-only |
| Scope | Theme map · CSS inventory · visual audit · component registry · technical risks · readiness |
| Verdict | **READY FOR PHASE 2 PLANNING** — execution **NOT AUTHORIZED** |
| Evidence (local) | `.recovery-temp/site-001-w2-visual-discovery.json` |
| Recommended first write wave | **W2-COLORS** — CSS `:root` tokens on TEST (after operator charter) |

### SITE-001 Phase 1 Stable Checkpoint

| Field | Value |
|-------|--------|
| Status | **ACTIVE** |
| Date | 2026-06-09 |
| Purpose | Official rollback and recovery point before Phase 2 (UX, style, layout, catalog, vehicle, production prep) |
| Verification | **13/13** public URLs CLEAN · legacy dictionary hits = **0** |
| Supersedes (recovery) | [SITE-001-PHASE1-STABLE-SNAPSHOT-v1.md](sites/site-001/reports/SITE-001-PHASE1-STABLE-SNAPSHOT-v1.md) |
| Recommended git tag | `site-001-phase1-stable-2026-06` |

**Operator next action:** Treat this checkpoint as baseline before any Phase 2 work. Authorize **W1F-D** (SMTP + `anketa.php`) and **W1F-E** (backup YML/templates) per [SITE-001-PHASE1-FINAL-DECISION-v1.md](sites/site-001/reports/SITE-001-PHASE1-FINAL-DECISION-v1.md); operator HITL sign-off **PENDING**. Resolve **C-04** WhatsApp when ready.

---

## W1 pre-execution artefacts (Run 4.101)

| Document | Role |
|----------|------|
| [SITE-001-W1-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W1-WRITE-CHARTER-v1.md) | C-05 write charter |
| [SITE-001-W1-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-W1-CHANGE-REQUEST-v1.md) | C-06 change request |
| [SITE-001-W1-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-W1-ROLLBACK-PLAN-v1.md) | C-06 rollback plan |
| [SITE-001-W1-BACKUP-PROCEDURE-v1.md](sites/site-001/reports/SITE-001-W1-BACKUP-PROCEDURE-v1.md) | C-08 backup procedure |
| [SITE-001-W1A-EXECUTION-SPEC-v1.md](sites/site-001/reports/SITE-001-W1A-EXECUTION-SPEC-v1.md) | W1A execution spec |
| [SITE-001-W1A-AUTHORIZATION-REVIEW-v1.md](sites/site-001/reports/SITE-001-W1A-AUTHORIZATION-REVIEW-v1.md) | W1A authorization review |

---

## Run 5 (unchanged by W1 pre-execution)

| Item | State |
|------|--------|
| Charter | Read-only — [sites/site-001/AUDIT-CHARTER.md](sites/site-001/AUDIT-CHARTER.md) |
| Execution | **Paused** — artifact acquisition bottleneck |
| Blockers | [freeze/site-001-pre-runtime-bridge/AUDIT-BLOCKERS-v1.md](freeze/site-001-pre-runtime-bridge/AUDIT-BLOCKERS-v1.md) |
| Initialization artefacts | [sites/site-001/reports/RUN-5-FIRST-FINDINGS.md](sites/site-001/reports/RUN-5-FIRST-FINDINGS.md) |

W1 write charter applies to Phase 1 waves only; does not resume Run 5 automatically.

---

## Write authorization (SITE-001)

| Gate | Status |
|------|--------|
| W1 Write Charter document | **ACTIVE** — approver **Андрей** |
| [project-access-brief.md](sites/site-001/project-access-brief.md) write flags | **YES** — TEST only; **PRODUCTION WRITES FORBIDDEN** |
| Change Request instance | **APPROVED** — CR-SITE-001-W1-2026-06-08; **READY FOR EXECUTION** |
| Rollback plan instance | **CREATED** |
| Backup procedure | **EXECUTED** — operator confirmed 2026-06-08 |
| Fresh pre-W1 backup | **EXECUTED** — operator-confirmed (Beget; files + DB) |
| W1 execution authorization | **AUTHORIZED WITH NOTES** |
| W1A authorization | **AUTHORIZED WITH NOTES** |
| W1A execution | **DONE** — 2026-06-08 — **PASS WITH NOTES** |
| W1A post-audit | **DONE** — 2026-06-08 — **PASS** (no corrections) |
| W1B execution | **DONE** — **PASS** |
| W1C execution | **DONE** — **PASS** |
| W1D execution | **DONE** — **PASS WITH NOTES** |
| W1F-C1 / W1F-B / W1F-A | **DONE** — all **PASS WITH NOTES** |
| Phase 1 final audit | **DONE** — 2026-06-09 |
| W1G (DB SEO) | **DONE** — 2026-06-09 — **PASS WITH NOTES** |
| Phase 1 final acceptance | **DONE** — 2026-06-09 — **ACCEPTED WITH NOTES** |
| Phase 1 stable checkpoint | **ACTIVE** — 2026-06-09 — decision **APPROVED** |
| W1F-D / W1F-E | **NOT AUTHORIZED** |
| Phase 2 write charter | **ACTIVE** — W3UX-C1 charter [SITE-001-W3UX-C1-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W3UX-C1-WRITE-CHARTER-v1.md) |
| W3-V execution | **DONE** — 2026-06-09 — **PASS WITH NOTES** |
| W3-UX density discovery | **DONE** — 2026-06-09 — **DISCOVERY COMPLETE** |
| W3UX-C1 execution | **DONE** — 2026-06-09 — **PASS WITH NOTES** |
| W3UX-C2…QA | **NOT AUTHORIZED** |
| W3-C execution | **ROLLED BACK** — 2026-06-09 — T1 restore **PASS** |
| W3WF-01 Visual Impact Map | **DONE** — decision **READY** (implementation **ON HOLD** per audit 4.127) |
| W4 Used PDP slice | **DONE** — 2026-06-09 — **PASS WITH NOTES** — operator visual HITL **PENDING** |
| W4.1 Header & Hero Authority | **DONE** — 2026-06-09 — **PASS WITH NOTES** — visual proof pack **DONE** — operator HITL **READY** |
| Production deployment | **NOT AUTHORIZED** |

---

### SITE-001 W4.1 — Header & Hero Authority (2026-06-09)

| Field | Value |
|-------|--------|
| Status | **DONE** — **PASS WITH NOTES** (2026-06-09) |
| Design plan | [SITE-001-W4-1-HEADER-HERO-DESIGN-PLAN-v1.md](sites/site-001/reports/SITE-001-W4-1-HEADER-HERO-DESIGN-PLAN-v1.md) — **DONE** |
| Stable backup | [SITE-001-W4-STABLE-BACKUP-v1.md](sites/site-001/reports/SITE-001-W4-STABLE-BACKUP-v1.md) · `pre-w4-1-stable-20260609-1506` |
| Execution | [SITE-001-W4-1-HEADER-HERO-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W4-1-HEADER-HERO-EXECUTION-v1.md) — **DONE** |
| Decision | [SITE-001-W4-1-HEADER-HERO-DECISION-v1.md](sites/site-001/reports/SITE-001-W4-1-HEADER-HERO-DECISION-v1.md) — **PASS WITH NOTES** |
| Scope | Header shell, red discipline, promo strip, used PDP top — twig classes + CSS |
| Verification | **9/9** URLs PASS · W4 Used PDP **preserved** |
| Evidence (local) | `.recovery-temp/site-001-w4-1-result.json` · `qa/w4-1-header-hero-screenshots/` |
| Visual proof pack | [SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md](sites/site-001/reports/SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md) — **DONE** — verdict **PARTIAL SUCCESS** |
| Rollback | T1 from `pre-w4-1-stable-20260609-1506` |

---

## Remaining blockers before first write session (W1A)

| ID | Blocker | Owner | Status |
|----|---------|-------|--------|
| C-08-exec | Execute fresh file + DB backup per procedure | Operator | **CLOSED** — 2026-06-08 |
| C-05-act | Update access brief — write YES on TEST + named approver | Operator | **CLOSED** — approver **Андрей** |
| C-06-sign | Sign Change Request CR-SITE-001-W1-2026-06-08 | Write approver | **CLOSED** — **Андрей** |
| C-04 | WhatsApp link decision before W1B-D URL edits | Operator | **OPEN** — W1B text/phone may proceed; WhatsApp hold-or-skip |
| C-03 | Logo assets staged — blocks W1D only | Operator | **CLOSED** — W1D executed 2026-06-08 |
| C-10 | Admin URL confirmation on access brief | Operator *(recommended)* | **OPEN** |

**W1A–W1G:** **COMPLETE** (2026-06-08–09). **Phase 1 acceptance:** **ACCEPTED WITH NOTES** (2026-06-09). Residual: product detail HTTP unverified + deferred W1F-D/E (SMTP, `anketa.php`, `backup_yml`).

---

## Remaining blockers (later waves)

| ID | Blocker | Wave | Owner |
|----|---------|------|-------|
| C-04 | WhatsApp link decision | W1B | Operator |
| C-03 | Logo assets staged | W1D | Operator | **CLOSED** |
| C-10 | Admin URL on access brief | All *(recommended)* | Operator |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Named write approver | **Андрей** |
| Backup restore drill on Beget | **SAFE UNKNOWN** |
| Admin URL (non-secret) | **SAFE UNKNOWN** on access brief |
| Date of first W1A session | **2026-06-08** — executed on TEST |
| Run 5 execution resume date | **Not specified** |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-07 | **CREATED** — OCPilot program state; SITE-001 Phase 1 **NOT AUTHORIZED** |
| 2026-06-08 | **UPDATED** — W1A pre-execution authorization package; C-08/C-05/C-06 closed; W1A **AUTHORIZED WITH NOTES** |
| 2026-06-08 | **UPDATED** — W1A Store Settings **EXECUTED** on TEST; verdict **PASS WITH NOTES** |
| 2026-06-08 | **UPDATED** — W1A post-execution audit **PASS**; mixed-script concern **not confirmed** |
| 2026-06-08 | **UPDATED** — W1B theme branding discovery **COMPLETE**; authorization **AUTHORIZED WITH NOTES** |
| 2026-06-08 | **UPDATED** — W1B/C/D and W1F-C1/B/A execution **COMPLETE** on TEST |
| 2026-06-09 | **UPDATED** — Phase 1 stable snapshot + final audit; decision **COMPLETE WITH NOTES**; controller meta generator rule **ACTIVE** |
| 2026-06-09 | **UPDATED** — W1G DB SEO **DONE**; Phase 1 final acceptance; decision **ACCEPTED WITH NOTES** |
| 2026-06-09 | **UPDATED** — Phase 1 stable checkpoint **ACTIVE**; Run **4.110**; decision **APPROVED** |
| 2026-06-09 | **UPDATED** — W2 Visual Refresh Discovery **COMPLETE**; Run **4.111**; decision **DISCOVERY COMPLETE** |
| 2026-06-09 | **UPDATED** — W2.1 Visual Specification **COMPLETE**; Run **4.112**; decision **READY FOR PHASE 2 IMPLEMENTATION** |
| 2026-06-09 | **UPDATED** — SITE-002 (ЗПМ) **REGISTERED**; Run **4.113**; status **AWAITING INTAKE**; external secrets placeholders prepared |
| 2026-06-09 | **UPDATED** — W3-C T1 rollback **DONE** on TEST; Run **4.115**; verdict **PASS**; site restored to pre-W3C baseline |
| 2026-06-09 | **UPDATED** — W3-V Visual Layer Refresh **DONE** on TEST; Run **4.116**; CSS-only; verdict **PASS WITH NOTES**; backup `pre-w3v-20260609-0327` |
| 2026-06-09 | **UPDATED** — W3UX-C1 Used Catalog Card Density **DONE** on TEST; Run **4.118**; CSS-only `.used_catalog`; verdict **PASS WITH NOTES**; backup `pre-w3ux-c1-20260609-0416` |
| 2026-06-09 | **UPDATED** — W3COLOR-01 discovery **DONE**; W3ATMOSPHERE-01A visual preview **DONE**; verdict **READY FOR W3ATMOSPHERE-01 EXECUTION** (charter not authorized) |
| 2026-06-09 | **UPDATED** — W3ATMOSPHERE-01 execution **DONE**; verdict **PASS WITH NOTES** |
| 2026-06-09 | **UPDATED** — Website Factory Design Direction Pack **DONE**; direction «Graphite Salon»; decision **READY FOR OCPILOT IMPLEMENTATION**; next wave **W3WF-01** |
| 2026-06-09 | **UPDATED** — W3WF-01 Visual Impact Map **DONE**; decision **READY FOR W3WF-01 IMPLEMENTATION** (LOW–MEDIUM delta vs current TEST) |
| 2026-06-09 | **UPDATED** — W4 Used PDP Structural Visual Slice **DONE** on TEST; verdict **PASS WITH NOTES**; backup `pre-w4-20260609`; W3 cosmetic waves **STOPPED** for PDP |
| 2026-06-09 | **UPDATED** — W4.1 stable backup **DONE** (`pre-w4-1-stable-20260609-1506`); W4.1 Header & Hero Authority **DONE** on TEST; verdict **PASS WITH NOTES**; backup active as rollback baseline |
| 2026-06-09 | **UPDATED** — W4.1 Visual Proof Pack **DONE**; operator verdict **PARTIAL SUCCESS** (promo strip YES; homepage NO; header MAYBE) |
| 2026-06-09 | **UPDATED** — Website Factory Concept Workshop **DONE**; **Concept B — Modern Dealer** selected; implementation **STOPPED**; Graphite Salon / W3WF-01 superseded for first impression; sticky header **REJECTED** |
| 2026-06-09 | **UPDATED** — W5 First Impression Blueprint **DONE**; decision **APPROVED**; 3→7/10 without full redesign **YES**; phases W5-A…D defined; operator HITL **PENDING** |
| 2026-06-09 | **UPDATED** — W5-A Header Shell Recomposition **DONE** on TEST; 8/8 verify **PASS**; sticky removed; backup `pre-w5a-header-shell-20260609-2251`; operator visual HITL **PENDING** |
| 2026-06-09 | **UPDATED** — W5-A-S Stabilization Pass **DONE** on TEST; promo/dropdown/density/responsive fixes; backup `pre-w5a-stabilization-20260609-2325`; stabilization **PASS WITH NOTES**; W5-A operator COMPLETE **NO** (HITL **PENDING**) |

| 2026-06-14 | **UPDATED** — SITE-002 stable live manual compact checkpoint **REGISTERED**; Run **4.138**; baseline `SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14`; status **STABLE LIVE CHECKPOINT**; rollback = Beget global backup + operator live state; metadata-only — no FTP/file capture |
| 2026-06-17 | **UPDATED** — SITE-002 authority freeze → `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI`; **MANUAL UI REFINEMENTS ARE CANONICAL**; active stage **M9.8 UX Polish Pack**; [REPORT-BZPM-STATE-FREEZE-ROADMAP-UPDATE.md](sites/site-002/reports/REPORT-BZPM-STATE-FREEZE-ROADMAP-UPDATE.md) |
| 2026-06-22 | **UPDATED** — BZPM **Corporate Pages Program** registered; M9.13/M9.14 research artifacts exported; program **OPEN** |
| 2026-06-22 | **UPDATED** — Corporate Pages Research **COMPLETE** (M9.15–M9.18); IA map [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-IA-MAP-v1.md); phase gate Research → IA |
| 2026-06-22 | **UPDATED** — BZPM Copy artefact system **REGISTERED**; [BZPM-COPY-STANDARDS-v1.md](../website-factory/execution-cases/bzpm-roadmap/BZPM-COPY-STANDARDS-v1.md); M9.13–M9.18 PAGE-COPY v1 shells |
| 2026-06-28 | **RECONCILED** — BZPM post-recovery completeness audit semantics; M9.14/M9.15 **NOT_IMPLEMENTED** (not lost); distributed strategy/findings; [SITE-002-BZPM-POST-RECOVERY-COMPLETENESS-RECONCILIATION.md](sites/site-002/reports/SITE-002-BZPM-POST-RECOVERY-COMPLETENESS-RECONCILIATION.md) |
| 2026-06-28 | **CLOSED** — BZPM UX Redesign recovery phase; production transition; Run **4.148**; [SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md](sites/site-002/reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md) |
| 2026-06-28 | **REGISTERED** — M9.18 Custom Manufacturing Implementation Charter **READY**; Run **4.155**; terminal corp page charter; [SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION-CHARTER-v1.md](sites/site-002/reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION-CHARTER-v1.md); Knowledge Map §22 |
| 2026-06-28 | **DONE** — Corporate Pages Visual Polish Pass 1.2 on TEST; Run **4.160**; checkpoint `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2`; [SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md](sites/site-002/reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md); Knowledge Map §25 |
| 2026-06-29 | **DONE** — M9.13 About Company redesign re-activated on TEST; Run **4.163**; checkpoint `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02`; [SITE-002-ABOUT-COMPANY-REDESIGN-RESTORE-V2.md](sites/site-002/reports/SITE-002-ABOUT-COMPANY-REDESIGN-RESTORE-V2.md); Knowledge Map §17 |
| 2026-06-29 | **DONE** — Local Fonts Migration on TEST; Run **4.162**; checkpoint `SITE-002-STABLE-LIVE-LOCAL-FONTS-01`; [SITE-002-LOCAL-FONTS-MIGRATION.md](sites/site-002/reports/SITE-002-LOCAL-FONTS-MIGRATION.md); Knowledge Map §27 |
| 2026-06-29 | **DONE** — Operator Manual Polish Canonical Checkpoint 01; Run **4.161**; checkpoint `SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01`; FTP read-only capture; superseded by Local Fonts 01 for checkpoint authority; [SITE-002-STABLE-CHECKPOINT-OPERATOR-MANUAL-POLISH-01.md](sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-OPERATOR-MANUAL-POLISH-01.md); Knowledge Map §26 |
| 2026-06-29 | **DONE** — Custom OEM Proof Strip Commercial Trust restyle on TEST; Run **4.167**; checkpoint `SITE-002-STABLE-LIVE-CUSTOM-PROOF-STRIP-01`; [SITE-002-CUSTOM-PROOF-STRIP-RESTYLE.md](sites/site-002/reports/SITE-002-CUSTOM-PROOF-STRIP-RESTYLE.md); Knowledge Map §31 |
| 2026-06-29 | **DONE** — Delivery Summary Commercial Trust restyle on TEST; Run **4.168**; checkpoint `SITE-002-STABLE-LIVE-DELIVERY-SUMMARY-01`; [SITE-002-DELIVERY-SUMMARY-RESTYLE.md](sites/site-002/reports/SITE-002-DELIVERY-SUMMARY-RESTYLE.md); Knowledge Map §32 |
| 2026-06-29 | **DONE** — Corporate Intro Image Blocks 01 on TEST; Run **4.165**; checkpoint `SITE-002-STABLE-LIVE-CORPORATE-INTRO-BLOCKS-01`; verdict **PASS** (closeout — operator upload of `delivery-intro.jpg`; all 6 assets HTTP 200); [SITE-002-CORPORATE-INTRO-BLOCKS-01.md](sites/site-002/reports/SITE-002-CORPORATE-INTRO-BLOCKS-01.md); Knowledge Map §29 |
| 2026-06-30 | **DONE** — Documentation Closeout Scope A; Run **4.169**; Visual Polish Audit **TRACKED**; M9.17 warranty report drift fixed; authority reconciled; [SITE-002-DOCUMENTATION-CLOSEOUT-SCOPE-A.md](sites/site-002/reports/SITE-002-DOCUMENTATION-CLOSEOUT-SCOPE-A.md) |
| 2026-07-02 | **REGISTERED** — SITE-002 Production Profile; Run **4.170**; Production URL https://bzpm.ru/; profile **REGISTERED — NOT CONNECTED**; historical TEST preserved; [SITE-002-PRODUCTION-PROFILE-REGISTRATION.md](sites/site-002/reports/SITE-002-PRODUCTION-PROFILE-REGISTRATION.md) |
| 2026-07-04 | **COMPLETE** — SITE-002 First Controlled Production Change; Run **4.173**; single-file text-only FTP deploy verified; rollback readiness verified; checkpoint `SITE-002-STABLE-PROD-TEXT-CHANGE-01`; [SITE-002-FIRST-CONTROLLED-PRODUCTION-CHANGE.md](sites/site-002/reports/SITE-002-FIRST-CONTROLLED-PRODUCTION-CHANGE.md) |
| 2026-06-22 | **RECONCILED** — Corporate Pages program registry; charters + briefs; [BZPM-CORPORATE-PAGES-PROGRAM-RECONCILIATION-v1.md](../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-PROGRAM-RECONCILIATION-v1.md) |
| 2026-06-21 | **UPDATED** — SITE-002 stable live checkpoint **REGISTERED**; Run **4.145**; baseline `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`; catalog UX cluster complete; Knowledge Map §16 Catalog State Persistence |
| 2026-06-21 | **UPDATED** — SITE-002 stable live checkpoint **REGISTERED**; Run **4.144**; baseline `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01`; Commercial Trust + operator manual polish; FTP live capture; Knowledge Map §14 |
| 2026-06-19 | **UPDATED** — SITE-002 stable live checkpoint **REGISTERED**; Run **4.143**; baseline `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01`; status **STABLE LIVE CHECKPOINT**; filter recovery + filter UX polish complete; Knowledge Map §7/§8; metadata-only — no FTP/file capture |
| 2026-06-19 | **UPDATED** — SITE-002 stable live checkpoint **REGISTERED**; Run **4.140**; baseline `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`; status **STABLE LIVE CHECKPOINT**; M9.8.1 · M9.8.2 · M9.8.5 + operator PLP polish complete; rollback = Beget full backup + live TEST + file-level pass backups; metadata-only — no FTP/file capture |

*OCPilot State — documentation only; no runtime claimed.*
