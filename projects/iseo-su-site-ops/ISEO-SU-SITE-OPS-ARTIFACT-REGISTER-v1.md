# ISEO-SU-SITE-OPS Artifact Register v1

**Status:** CURRENT / reconciled documentation consolidation 2026-08-24
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`

Primary vocabulary: **CURRENT** · **CANONICAL** · **SPECIALIZED** · **HISTORICAL** · **SUPERSEDED**. Supporting legacy labels below describe lifecycle but do not override these classes.

## Current authority set

| Artifact | Path | Classification |
|---|---|---|
| Current State | `ISEO-SU-CURRENT-STATE-v1.md` | CURRENT / CANONICAL |
| Production Architecture Knowledge Base | `ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md` | CURRENT / CANONICAL |
| Task Routing Guide | `ISEO-SU-TASK-ROUTING-GUIDE-v1.md` | CURRENT / CANONICAL / OPERATIONAL MAP |
| Route Ownership Matrix | `ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md` | CURRENT / CANONICAL / OPERATIONAL MAP |
| Protected Zones | `ISEO-SU-PROTECTED-ZONES-v1.md` | CURRENT / CANONICAL |
| SAFE UNKNOWN Register | `ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md` | CURRENT / CANONICAL |
| Artifact Register | `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md` | CURRENT / CANONICAL |
| Operational Index | `OPERATIONAL-INDEX.md` | CURRENT / CANONICAL ENTRY |

## Specialized current authorities

| Feature | Authority/evidence | Classification |
|---|---|---|
| Forms/security/recipient | `ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md`; `ISEO-SU-FORM-OPERATOR-RECIPIENT-REMOVAL-EVIDENCE-v1.md` | CURRENT / SPECIALIZED / CANONICAL |
| Form acceptance | `ISEO-SU-FORM-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-EVIDENCE-v2.md` | SPECIALIZED / HISTORICAL ACCEPTANCE EVIDENCE |
| Metrika visitor IP | `ISEO-SU-METRIKA-VISITOR-IP-PARAM-BASELINE-v1.md`; `ISEO-SU-METRIKA-VISITOR-IP-PARAM-EVIDENCE-v1.md` | CURRENT / SPECIALIZED |
| Glossary final production | `ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md` | CURRENT / SPECIALIZED / CANONICAL |
| Sitemap architecture | `ISEO-SU-SITEMAP-ARCHITECTURE-AND-CURRENT-STATE-v1.md` | CURRENT / SPECIALIZED / OPEN IMPLEMENTATION |
| Tech SEO audit | `ISEO-SU-TECH-SEO-AUDIT-EVIDENCE-v1.md`; findings/inventory CSV; SEO-team report | CURRENT / SPECIALIZED EVIDENCE |
| Stabilization | `ISEO-SU-STABILIZATION-CLOSEOUT-v1.md` | CANONICAL CLOSEOUT |
| Documentation consolidation | `reports/REPORT-ISEO-SU-SITE-OPS-PROJECT-DOCUMENTATION-AND-KNOWLEDGE-CONSOLIDATION-01.md` | CURRENT TASK REPORT / GIT PERSISTENCE PENDING |

## Historical and superseded policy

- `reports/REPORT-*.md` from completed implementation/audit phases are **HISTORICAL EVIDENCE** even when they were “current” at creation. Their content remains unchanged.
- Feature evidence may remain specialized proof; current operating values come from Current State and the relevant current baseline.
- Acceptance v1 using typo `im.work@nail.ru` is **SUPERSEDED** for recipient evidence; v2 proves acceptance, while later removal evidence owns current routing.
- Old draft-only/404 glossary instructions, old forms-without-validation statements, healthy-Yoast-root-sitemap claims, and WPilot-onboarding requirements are **SUPERSEDED** current guidance.
- Raw/derived CSV/XLSX/source assets remain registered by family; this task did not edit them.

## Inventory scope

The recursive project inventory at task start contained **357 files**; **306 Markdown matches** include current authorities, feature evidence, historical REPORTs, content docs, and READMEs. Classification is by artifact family to avoid a 357-row duplicate catalog.

---

### Metrika visitor IP param addon (2026-08-24) — CURRENT / CANONICAL

| Artifact | Path | Class |
|----------|------|-------|
| Metrika visitor IP baseline | `ISEO-SU-METRIKA-VISITOR-IP-PARAM-BASELINE-v1.md` | CURRENT / CANONICAL |
| Metrika visitor IP evidence | `ISEO-SU-METRIKA-VISITOR-IP-PARAM-EVIDENCE-v1.md` | CURRENT |
| Addon production source | `production-source/metrika-ip/` | CANONICAL |
| Shared JS (loader hook) | `production-source/js/common.js` | CANONICAL |
| Task REPORT | `reports/REPORT-ISEO-SU-SITE-OPS-METRIKA-VISITOR-IP-PARAM-01.md` | HISTORICAL / COMPLETE |

### Form anti-spam and validation (2026-08-20) — CURRENT / CANONICAL

| Artifact | Path | Class |
|----------|------|-------|
| Form security baseline | `ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md` | CURRENT / CANONICAL |
| Form anti-spam evidence | `ISEO-SU-FORM-ANTISPAM-VALIDATION-EVIDENCE-v1.md` | HISTORICAL / SPECIALIZED EVIDENCE (recipient narrative superseded; security results retained) |
| Form handlers + security libs | `production-source/forms/` | CANONICAL |
| Shared forms JS | `production-source/js/common.js` | CANONICAL |
| Form anti-spam REPORT | `reports/REPORT-ISEO-SU-SITE-OPS-FORM-ANTISPAM-AND-VALIDATION-01.md` | HISTORICAL / COMPLETE |

### Form recipient restore verification (2026-08-21) — HISTORICAL (restore wave)

| Artifact | Path | Class |
|----------|------|-------|
| Form recipient restoration evidence | `ISEO-SU-FORM-RECIPIENT-RESTORATION-EVIDENCE-v1.md` | HISTORICAL (restore verification; pre-removal set) |
| Form recipient restore REPORT | `reports/REPORT-ISEO-SU-SITE-OPS-FORM-RECIPIENT-RESTORE-01.md` | HISTORICAL |

### Operator recipient removal + tech/SEO audit (2026-08-21) — CURRENT

| Artifact | Path | Class |
|----------|------|-------|
| Operator recipient removal evidence | `ISEO-SU-FORM-OPERATOR-RECIPIENT-REMOVAL-EVIDENCE-v1.md` | CURRENT / CANONICAL (production recipient authority) |
| Tech SEO audit evidence | `ISEO-SU-TECH-SEO-AUDIT-EVIDENCE-v1.md` | CURRENT |
| Tech SEO findings CSV | `audits/tech-seo/ISEO-SU-TECH-SEO-FINDINGS-v1.csv` | CURRENT |
| Tech SEO URL inventory CSV | `audits/tech-seo/ISEO-SU-TECH-SEO-URL-INVENTORY-v1.csv` | CURRENT |
| SEO-team audit report | `reports/ISEO-SU-TECH-SEO-AUDIT-FOR-SEO-TEAM-v1.md` | CURRENT |
| Task REPORT | `reports/REPORT-ISEO-SU-SITE-OPS-RECIPIENT-REMOVE-AND-TECH-SEO-AUDIT-01.md` | HISTORICAL / COMPLETE |
| Crawl raw (Storage) | `X:\AI MARS STORAGE\iseo-su-site-ops\tech-seo-audit-01\` | CURRENT (out of Git) |

### All-forms isolated mail acceptance — correct operator (2026-08-21) — HISTORICAL ACCEPTANCE

| Artifact | Path | Class |
|----------|------|-------|
| All-forms isolated mail acceptance evidence v2 | `ISEO-SU-FORM-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-EVIDENCE-v2.md` | HISTORICAL / SPECIALIZED ACCEPTANCE EVIDENCE |
| All-forms isolated mail acceptance REPORT 02 | `reports/REPORT-ISEO-SU-SITE-OPS-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-02.md` | HISTORICAL / COMPLETE |
| Acceptance evidence v1 (typo address) | `ISEO-SU-FORM-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-EVIDENCE-v1.md` | HISTORICAL / SUPERSEDED (recipient evidence) |
| Acceptance REPORT 01 (typo address) | `reports/REPORT-ISEO-SU-SITE-OPS-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-01.md` | HISTORICAL / SUPERSEDED (recipient evidence) |

### Current brain / stabilization (2026-08-20) — CURRENT

| Artifact | Path | Class |
|----------|------|-------|
| Current state | `ISEO-SU-CURRENT-STATE-v1.md` | CURRENT / CANONICAL |
| Stabilization closeout | `ISEO-SU-STABILIZATION-CLOSEOUT-v1.md` | CURRENT / CANONICAL |
| Stabilization REPORT | `reports/REPORT-ISEO-SU-SITE-OPS-FINAL-STABILIZATION-AND-HOUSEKEEPING.md` | HISTORICAL / COMPLETE |
| Locus scratch gitignore | `.gitignore` (`_*-scratch/`) | CURRENT |
| Scratch archive (out of Git) | `X:\AI MARS STORAGE\archives\iseo-su-site-ops-scratch-stabilization-2026-08-20\` | SCRATCH_REMOVED (retained in Storage) |

### Glossary final integration and closeout (2026-08-18) — CANONICAL

| Artifact | Path | Status |
|----------|------|--------|
| Final production baseline | `ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md` | CANONICAL |
| Manual CSS promotion evidence | `ISEO-SU-GLOSSARY-MANUAL-CSS-PROMOTION-EVIDENCE-v1.md` | CANONICAL |
| Promoted shared CSS source | `production-source/css/main.css` | CANONICAL (SHA-256 `4a1202b6…`) |
| Theme topbar package mirror | `wordpress/iseoblog-glossary/template-parts/content-topbar.php` | CANONICAL |
| Closeout REPORT | `reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-FINAL-INTEGRATION-AND-CLOSEOUT.md` | HISTORICAL / COMPLETE |
| Theme package (menu + archive title filters) | `wordpress/iseoblog-glossary/inc/glossary-cpt.php` | CANONICAL |

### Final post-launch and git sync closeout (2026-08-18) — CANONICAL

| Artifact | Path | Status |
|----------|------|--------|
| Final launch closeout | `ISEO-SU-FINAL-LAUNCH-CLOSEOUT-v1.md` | CANONICAL |
| Post-launch REPORT | `reports/REPORT-ISEO-SU-SITE-OPS-FINAL-POST-LAUNCH-AND-GIT-SYNC-CLOSEOUT.md` | HISTORICAL / COMPLETE |
| Shared CSS overflow block | `production-source/css/main.css` | CANONICAL / deployed (`20260818T101846Z`) |

### Architecture knowledge package (2026-07-24) — CANONICAL

| Artifact | Path | Status |
|----------|------|--------|
| Production architecture knowledge base | `ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md` | CANONICAL |
| Canonical route ownership matrix | `ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md` | CANONICAL |
| Page-to-source map | `ISEO-SU-PAGE-TO-SOURCE-MAP-v1.md` | CANONICAL |
| WordPress object/template map | `ISEO-SU-WORDPRESS-OBJECT-AND-TEMPLATE-MAP-v1.md` | CANONICAL |
| Static PHP file ownership map | `ISEO-SU-STATIC-PHP-FILE-OWNERSHIP-MAP-v1.md` | CANONICAL |
| Forms/calculators/web-KP map | `ISEO-SU-FORMS-CALCULATORS-AND-WEB-KP-MAP-v1.md` | CANONICAL |
| Global component dependency map | `ISEO-SU-GLOBAL-COMPONENT-DEPENDENCY-MAP-v1.md` | CANONICAL |
| Task routing guide | `ISEO-SU-TASK-ROUTING-GUIDE-v1.md` | CANONICAL |
| Site route register | `ISEO-SU-SITE-ROUTE-REGISTER-v1.md` | CANONICAL |
| Architecture capture REPORT | `reports/REPORT-ISEO-SU-SITE-OPS-COMPLETE-PRODUCTION-ARCHITECTURE-ROUTE-KNOWLEDGE-CAPTURE.md` | HISTORICAL / COMPLETE |

### Glossary foundation package (2026-07-24) — CANONICAL / HISTORICAL

| Artifact | Path | Status |
|----------|------|--------|
| Glossary architecture and content model | `ISEO-SU-GLOSSARY-ARCHITECTURE-AND-CONTENT-MODEL-v1.md` | CANONICAL |
| Glossary term intake register | `ISEO-SU-GLOSSARY-TERM-INTAKE-REGISTER-v1.md` | HISTORICAL |
| Glossary template component map | `ISEO-SU-GLOSSARY-TEMPLATE-COMPONENT-MAP-v1.md` | CANONICAL |
| Theme source package | `wordpress/iseoblog-glossary/` | CANONICAL |
| Sanitized intake inventory | `data/glossary-intake/glossary-terms-inventory-v1.json` (+ csv) | CANONICAL |
| Working intake xlsx duplicate | `data/glossary-intake/glossary-rabochiy-sait.xlsx` | SCRATCH_REMOVED (duplicate of materials canonical; archived in Storage) |
| Glossary intake REPORT | `reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-ARCHITECTURE-TEMPLATE-AND-CONTENT-INTAKE.md` | HISTORICAL / COMPLETE |

### Glossary source material (2026-07-24) — CANONICAL

| Artifact | Path | Status |
|----------|------|--------|
| Canonical Nikita workbook v1 (immutable) | `materials/glossary/ISEO-SU-GLOSSARY-SOURCE-NIKITA-v1.xlsx` | CANONICAL |
| Source SHA-256 | `f7651cffc5d03c497062ac6ee5b6288d9397ae5abede43fbd19f1a3ea26699de` | RECORDED |
| Materials provenance README | `materials/glossary/README.md` | CANONICAL |
| Glossary source material register | `ISEO-SU-GLOSSARY-SOURCE-MATERIAL-REGISTER-v1.md` | CANONICAL |
| Source material canonicalization REPORT | `reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-SOURCE-MATERIAL-CANONICALIZATION.md` | HISTORICAL / COMPLETE |

### Glossary editorial / batches / publication — CANONICAL / HISTORICAL

Editorial standard, term audit, pilot, SEO model, final corpus, Batch 01–04 manifests/content/CSVs, publication eligibility/launch/backup docs, and related REPORTs remain in locus as **CANONICAL** (live authorities) or **HISTORICAL** (wave REPORTs). Reusable tooling: `tools/glossary-batch-content-updater.py`, `tools/glossary-batch01-content-updater.py` — **CANONICAL** (keep).

### Glossary archive layout / page_scene alignment — CANONICAL / HISTORICAL

| Artifact | Path | Status |
|----------|------|--------|
| Archive layout fix evidence | `ISEO-SU-GLOSSARY-ARCHIVE-LAYOUT-FIX-EVIDENCE-v1.md` | HISTORICAL |
| Page_scene services alignment evidence | `ISEO-SU-GLOSSARY-PAGE-SCENE-SERVICES-ALIGNMENT-EVIDENCE-v1.md` | HISTORICAL |
| Related REPORTs | `reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-*.md` | HISTORICAL / COMPLETE |

---

## Programme foundation artifacts (this locus)

| Artifact | Path / note | Status |
|----------|-------------|--------|
| OPERATIONAL-INDEX | `OPERATIONAL-INDEX.md` | CURRENT |
| README | `README.md` | CURRENT |
| Charter | `ISEO-SU-SITE-OPS-CHARTER-v1.md` | CANONICAL |
| System boundaries | `ISEO-SU-SITE-OPS-SYSTEM-BOUNDARIES-v1.md` | CANONICAL |
| Phase model | `ISEO-SU-SITE-OPS-PHASE-MODEL-v1.md` | HISTORICAL |
| Artifact register | this file | CURRENT |
| Decision register | `ISEO-SU-SITE-OPS-DECISION-REGISTER-v1.md` | CANONICAL |
| SAFE UNKNOWN register | `ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md` | CURRENT |
| Cross-chat handoff closeout | `ISEO-SU-SITE-OPS-CROSS-CHAT-HANDOFF-CLOSEOUT-v1.md` | HISTORICAL |
| Firefox Browser Workstation deferred | `ISEO-SU-SITE-OPS-FIREFOX-BROWSER-WORKSTATION-DEFERRED-v1.md` | DEFERRED |
| Phase 0–2B REPORTs | `reports/REPORT-ISEO-SU-SITE-OPS-PHASE-*.md` | HISTORICAL / COMPLETE |

---

## Phase 2 / WPilot evidence artifacts

| Artifact ID | Path | Status | Notes |
|-------------|------|--------|-------|
| Protected zones | `ISEO-SU-PROTECTED-ZONES-v1.md` | CANONICAL | Updated glossary closeout |
| WPilot smoke evidence | `ISEO-SU-WPILOT-READ-ONLY-SMOKE-EVIDENCE-v1.md` | CANONICAL | 6D blocked — no smoke run; Git-persisted |
| Phase 6D REPORT | `reports/REPORT-ISEO-SU-SITE-OPS-PHASE-6D-WPILOT-BRIDGE-ENABLEMENT-AND-READ-ONLY-SMOKE.md` | BLOCKED / HISTORICAL | Missing exact approval + fresh backup lines |
| Phase 4B–6C-P package | WPilot evidence + REPORTs under locus | HISTORICAL / COMPLETE | Accepted baseline = 6C token / RC6 safe defaults |

Local-only (Git-ignored): `X:\AI MARS\local\sites\iseo-su-production\` · `X:\AI MARS\local\tokens\wpilot-prod-iseo-su.token`.

Former locus scratch (`_glossary-scratch/`, `_phase*-scratch/`, `_arch-knowledge-scratch/`): **SCRATCH_REMOVED** from Git locus; archived under Storage path above. Historical REPORTs may still name those paths as past evidence locations.

Phase status: **PHASE 6D — BLOCKED / PRODUCTION UNCHANGED**; accepted baseline remains **PHASE 6C — TOKEN CREATED / RC6 SAFE DEFAULTS**; bridge / writes / DEV / REST smoke **NOT RUN**.

---

## Explicit non-artifacts and security signal

This documentation wave introduced no token, password, cookie, session value, DB dump, Localhost mirror, unredacted production dump, or active `_*-scratch/` tree.

**SECURITY RISK (pre-existing, not modified):** tracked `production-source/forms/iseo-form-config.php` contains HMAC secret material used by the accepted form-security implementation. Its value must never be copied into documentation, chat, REPORTs, or diffs outside an explicitly authorized secret-remediation task.

---

*Artifact Register v1 · documentation consolidation 2026-08-24.*
