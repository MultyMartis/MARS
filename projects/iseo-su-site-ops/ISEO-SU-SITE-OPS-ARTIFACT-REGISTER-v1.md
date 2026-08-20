# ISEO-SU-SITE-OPS Artifact Register v1

**Status:** ACCEPTED (Phase 1.5); **updated architecture knowledge capture** 2026-07-24; **stabilization** 2026-08-20  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`

Status vocabulary: **CURRENT** · **CANONICAL** · **HISTORICAL** · **SUPERSEDED** · **SCRATCH_REMOVED** · **COMPLETE** · **CREATED** · **PLANNED** · **CONDITIONAL** · **DEFERRED** · **NOT AUTHORIZED** · **OPEN** · **BLOCKED**


### Form anti-spam and validation (2026-08-20) — CURRENT / CANONICAL

| Artifact | Path | Class |
|----------|------|-------|
| Form security baseline | `ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md` | CURRENT / CANONICAL |
| Form anti-spam evidence | `ISEO-SU-FORM-ANTISPAM-VALIDATION-EVIDENCE-v1.md` | CURRENT |
| Form handlers + security libs | `production-source/forms/` | CANONICAL |
| Shared forms JS | `production-source/js/common.js` | CANONICAL |
| Form anti-spam REPORT | `reports/REPORT-ISEO-SU-SITE-OPS-FORM-ANTISPAM-AND-VALIDATION-01.md` | CURRENT |

### All-forms isolated mail acceptance (2026-08-21) — CURRENT

| Artifact | Path | Class |
|----------|------|-------|
| All-forms isolated mail acceptance evidence | `ISEO-SU-FORM-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-EVIDENCE-v1.md` | CURRENT |
| All-forms isolated mail acceptance REPORT | `reports/REPORT-ISEO-SU-SITE-OPS-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-01.md` | CURRENT |

### Current brain / stabilization (2026-08-20) — CURRENT

| Artifact | Path | Class |
|----------|------|-------|
| Current state | `ISEO-SU-CURRENT-STATE-v1.md` | CURRENT / CANONICAL |
| Stabilization closeout | `ISEO-SU-STABILIZATION-CLOSEOUT-v1.md` | CURRENT / CANONICAL |
| Stabilization REPORT | `reports/REPORT-ISEO-SU-SITE-OPS-FINAL-STABILIZATION-AND-HOUSEKEEPING.md` | CURRENT |
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

## Explicit non-artifacts

Unchanged: no tokens/credentials in Git locus; no DB dumps; no Localhost mirror; no unredacted production dumps; no active `_*-scratch/` trees in the programme locus.

---

*Artifact Register v1 · updated 2026-08-20 form anti-spam harden.*
