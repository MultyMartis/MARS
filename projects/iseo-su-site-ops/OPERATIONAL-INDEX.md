# ISEO-SU SITE OPS — Operational Index

**Lane:** A — Existing Site Operations / Integration  
**Classification:** documentation-first programme locus  
**Domain root:** [README.md](README.md)

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
| **Lifecycle** | **WPILOT ACTIVE / SAFE DEFAULTS** |
| **Project status** | Active documentation + bounded production activation programme; token / bridge / writes **NOT AUTHORIZED** |
| **Current phase** | **PHASE 6B — WPILOT ACTIVE / SAFE DEFAULTS** |
| **Phase 2B status** | **COMPLETE / READ-ONLY PRODUCTION ARCHITECTURE CAPTURED** |
| **Phase 4B status** | **COMPLETE / PRE-INSTALL CONDITIONAL GO** (static package + compatibility only) |
| **Phase 6A status** | **COMPLETE / WPILOT INSTALLED INACTIVE** |
| **Phase 6B status** | **COMPLETE / WPILOT ACTIVE SAFE DEFAULTS** |
| **Production connection** | Phase 6B used WP Admin activation under activation-only charter |
| **Access files** | **LOCAL-ONLY FILLED / VALIDATED** (Git-ignored) |
| **WPilot** | **ACTIVE** on production / package **0.3.0-RC5 / accepted hash** |
| **Activation** | **DONE (6B)** |
| **FTP/SFTP** | Used under Phase 6A; further use charter-gated |
| **Local mirror** | **NOT DECIDED** |
| **ATLAS** | **MINT DEFERRED** |
| **Token creation** | **BLOCKED on RC5 (6C)**; RC6 remediation **PACKAGED** (4C) — **NOT CREATED** on production |
| **Bridge** | **DISABLED** |
| **Writes** | **DISABLED** |
| **REST smoke (WPilot)** | **NOT AUTHORIZED** / **NOT RUN** |
| **Controlled write smoke** | **NOT AUTHORIZED** |
| **Phase 6C status** | **BLOCKED / NO TOKEN** (live product gate conflict on RC5) |
| **Phase 4C status** | **COMPLETE / RC6 PACKAGE READY** — production unchanged |
| **Remediation package** | `metacode-wpilot-v0.3.0-rc6.zip` · SHA-256 `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` |
| **Next operator action** | Approve **PHASE 6C-R WPILOT REMEDIATION UPDATE-ONLY** (fresh Beget backup; update plugin only; keep bridge/writes off; no token; no REST) |
| **Next gate** | **ISEO-SU-SITE-OPS — PHASE 6C-R WPILOT REMEDIATION UPDATE-ONLY** |

Hosting: **Beget**. WordPress Admin: `https://i-seo.su/wp-admin/`. Staging: **absent**. Architecture: **hybrid** (root WP + physical PHP-capable HTML + shared assets) — see boundary map.

Installed production package (current): `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc5.zip`  
SHA-256: `43c71a561872a037f294a12d5194d0925e988392599f02c1eeb2d8b1c52e1577`  
Remediation package (not deployed): `…\metacode-wpilot-v0.3.0-rc6.zip` · `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6`

---

## Sibling / supporting programmes

| Programme | Path | Role relative to this locus |
|-----------|------|-----------------------------|
| **WPilot** | `projects/wpilot/` | WordPress pilot programme + plugin contracts; **does not** own full i-seo.su passport / hybrid runbook |
| **i-SEO Report Hub** | `projects/iseo-report-hub/` | Sibling product; production `report-hub/` tree observed on site |
| **Website Factory** | `projects/mars-website-factory/` | Methodology for static page/component/QA — **not** deployment engine |
| **Forge WordPress** | `projects/mars-website-factory/subsystems/forge-wordpress/` | WordPress engineering safety methodology — **not** project owner |
| **ATLAS** | `projects/atlas/` | Identity/relationship registry only; **no mint** until chartered |
| **Survivability / GitGuard** | `projects/mars-survivability/` | Safety, backup, rollback, protected-zone methodology |
| **MLI** | `projects/mars-localhost-infrastructure/` | Optional future local mirror/runtime authority; **no mirror now** |
| **Remote Operations Layer** | `projects/remote-operations-layer/` | Remote-ops methodology; **not** connector or authorization source |

---

## Current authority order

1. `AGENTS.md` / `.cursorrules` / `governance/mars-x-drive-root-authority-v1.md`
2. This programme locus: `projects/iseo-su-site-ops/`
3. Supporting methodology from sibling programmes — **consume patterns only**
4. Operator decisions recorded in Decision Register
5. Chat handoffs — **supporting evidence only**

On conflict: **this locus wins** for i-seo.su hybrid site operations documentation.

---

## Core Run

| Step | Action |
|------|--------|
| 1 | Read this OPERATIONAL-INDEX |
| 2 | Confirm phase and HOLDs below |
| 3 | Read charter + system boundaries + Phase 2B audit + Phase 4B WPilot gate + Phase 6B evidence |
| 4 | Check Decision / SAFE UNKNOWN / protected zones |
| 5 | For credentials: local-only files — never paste secrets into chat |
| 6 | Execute only the **next authorized task** after operator acceptance |
| 7 | Close with REPORT under `reports/` — no secrets, no unauthorized production mutation |

---

## Active HOLDs

| HOLD | Status |
|------|--------|
| Production **write** outside exact activation/rollback charters | **HOLD** |
| Beget / hosting **panel** login by agent | **HOLD** |
| Unchartered SFTP reuse | **HOLD** |
| Unchartered WP Admin reuse | **HOLD** |
| WPilot plugin **activation** | **DONE (6B)** — do not re-activate / re-configure without charter |
| Token / profile creation for i-seo.su (WPilot token) | **HOLD** until after **6C-R**; 6C blocked on RC5; RC6 packaged |
| Bridge enable / write enable | **HOLD** |
| WPilot REST smoke | **HOLD** |
| Controlled write smoke | **HOLD** |
| Database / phpMyAdmin | **HOLD** |
| ATLAS WEB/DOM/PRJ mint | **DEFERRED** |
| Local mirror creation | **DEFAULT DEFER** |
| Firefox Browser Workstation implementation | **DEFERRED** |

---

## Next authorized task

**ISEO-SU-SITE-OPS — PHASE 6C-R WPILOT REMEDIATION UPDATE-ONLY**

Requires fresh Beget backup; update only WPilot to RC6; preserve bridge/writes/`dev_confirmed` off; create **no** token; run **no** REST.

After 6C-R acceptance: **PHASE 6C TOKEN CREATION-ONLY RETRY**.

See [reports/REPORT-ISEO-SU-SITE-OPS-PHASE-4C-WPILOT-TOKEN-GATING-REMEDIATION.md](reports/REPORT-ISEO-SU-SITE-OPS-PHASE-4C-WPILOT-TOKEN-GATING-REMEDIATION.md) and Phase 6C blocked REPORT.

---

## Forbidden actions (current)

- Production writes / uploads / chmod / deletes outside exact rollback/token charters
- WordPress settings saves, core/theme updates, unrelated plugin changes
- WPilot **token** / bridge enable / write enable / REST (until separately gated)
- Database / phpMyAdmin access; copying DB credentials
- ATLAS mint; registry mutation
- Localhost mirror / Storage writes (unless separately chartered)
- Credentials in docs / chat / REPORT
- Git stage/commit/push unless separately chartered

---

## Artifact navigation

| Artifact | Path |
|----------|------|
| README | [README.md](README.md) |
| Charter | [ISEO-SU-SITE-OPS-CHARTER-v1.md](ISEO-SU-SITE-OPS-CHARTER-v1.md) |
| System boundaries | [ISEO-SU-SITE-OPS-SYSTEM-BOUNDARIES-v1.md](ISEO-SU-SITE-OPS-SYSTEM-BOUNDARIES-v1.md) |
| Phase model | [ISEO-SU-SITE-OPS-PHASE-MODEL-v1.md](ISEO-SU-SITE-OPS-PHASE-MODEL-v1.md) |
| Artifact register | [ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md](ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md) |
| Decision register | [ISEO-SU-SITE-OPS-DECISION-REGISTER-v1.md](ISEO-SU-SITE-OPS-DECISION-REGISTER-v1.md) |
| SAFE UNKNOWN register | [ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md](ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md) |
| Evidence intake ledger | [ISEO-SU-SITE-EVIDENCE-INTAKE-v1.md](ISEO-SU-SITE-EVIDENCE-INTAKE-v1.md) |
| Public route register | [ISEO-SU-PUBLIC-ROUTE-REGISTER-v1.md](ISEO-SU-PUBLIC-ROUTE-REGISTER-v1.md) |
| Access classification | [ISEO-SU-ACCESS-CLASSIFICATION-v1.md](ISEO-SU-ACCESS-CLASSIFICATION-v1.md) |
| Local access model | [ISEO-SU-LOCAL-ACCESS-MODEL-v1.md](ISEO-SU-LOCAL-ACCESS-MODEL-v1.md) |
| Read-only production audit | [ISEO-SU-READ-ONLY-PRODUCTION-AUDIT-v1.md](ISEO-SU-READ-ONLY-PRODUCTION-AUDIT-v1.md) |
| Remote filesystem inventory | [ISEO-SU-REMOTE-FILESYSTEM-INVENTORY-v1.md](ISEO-SU-REMOTE-FILESYSTEM-INVENTORY-v1.md) |
| WordPress inventory | [ISEO-SU-WORDPRESS-INVENTORY-v1.md](ISEO-SU-WORDPRESS-INVENTORY-v1.md) |
| Static/WP boundary map | [ISEO-SU-STATIC-WP-BOUNDARY-MAP-v1.md](ISEO-SU-STATIC-WP-BOUNDARY-MAP-v1.md) |
| Hybrid SoT matrix | [ISEO-SU-HYBRID-SOURCE-OF-TRUTH-MATRIX-v1.md](ISEO-SU-HYBRID-SOURCE-OF-TRUTH-MATRIX-v1.md) |
| Protected zones | [ISEO-SU-PROTECTED-ZONES-v1.md](ISEO-SU-PROTECTED-ZONES-v1.md) |
| WPilot preinstall inputs | [ISEO-SU-WPILOT-PREINSTALL-INPUTS-v1.md](ISEO-SU-WPILOT-PREINSTALL-INPUTS-v1.md) |
| WPilot package audit | [ISEO-SU-WPILOT-PACKAGE-AUDIT-v1.md](ISEO-SU-WPILOT-PACKAGE-AUDIT-v1.md) |
| WPilot source/route audit | [ISEO-SU-WPILOT-SOURCE-AND-ROUTE-AUDIT-v1.md](ISEO-SU-WPILOT-SOURCE-AND-ROUTE-AUDIT-v1.md) |
| WPilot capability matrix | [ISEO-SU-WPILOT-CAPABILITY-MATRIX-v1.md](ISEO-SU-WPILOT-CAPABILITY-MATRIX-v1.md) |
| WPilot compatibility | [ISEO-SU-WPILOT-COMPATIBILITY-ASSESSMENT-v1.md](ISEO-SU-WPILOT-COMPATIBILITY-ASSESSMENT-v1.md) |
| WPilot install/rollback plan | [ISEO-SU-WPILOT-INSTALLATION-AND-ROLLBACK-PLAN-v1.md](ISEO-SU-WPILOT-INSTALLATION-AND-ROLLBACK-PLAN-v1.md) |
| WPilot install-only evidence | [ISEO-SU-WPILOT-INSTALL-ONLY-EVIDENCE-v1.md](ISEO-SU-WPILOT-INSTALL-ONLY-EVIDENCE-v1.md) |
| WPilot activation-only evidence | [ISEO-SU-WPILOT-ACTIVATION-ONLY-EVIDENCE-v1.md](ISEO-SU-WPILOT-ACTIVATION-ONLY-EVIDENCE-v1.md) |
| WPilot token storage decision | [ISEO-SU-WPILOT-TOKEN-STORAGE-DECISION-v1.md](ISEO-SU-WPILOT-TOKEN-STORAGE-DECISION-v1.md) |
| WPilot token creation evidence | [ISEO-SU-WPILOT-TOKEN-CREATION-EVIDENCE-v1.md](ISEO-SU-WPILOT-TOKEN-CREATION-EVIDENCE-v1.md) | BLOCKED / NO TOKEN (live gate) |

---

## REPORT navigation

| Report | Path | Status |
|--------|------|--------|
| Phase 0 preflight closeout | [reports/REPORT-ISEO-SU-SITE-OPS-PHASE-0-PREFLIGHT-CLOSEOUT.md](reports/REPORT-ISEO-SU-SITE-OPS-PHASE-0-PREFLIGHT-CLOSEOUT.md) | COMPLETE |
| Phase 1 cross-chat intake closeout | [reports/REPORT-ISEO-SU-SITE-OPS-PHASE-1-CROSS-CHAT-INTAKE-CLOSEOUT.md](reports/REPORT-ISEO-SU-SITE-OPS-PHASE-1-CROSS-CHAT-INTAKE-CLOSEOUT.md) | COMPLETE |
| Phase 1.5 locus creation | [reports/REPORT-ISEO-SU-SITE-OPS-PHASE-1.5-LOCUS-CREATION.md](reports/REPORT-ISEO-SU-SITE-OPS-PHASE-1.5-LOCUS-CREATION.md) | COMPLETE |
| Phase 2 non-secret evidence intake | [reports/REPORT-ISEO-SU-SITE-OPS-PHASE-2-NON-SECRET-EVIDENCE-INTAKE.md](reports/REPORT-ISEO-SU-SITE-OPS-PHASE-2-NON-SECRET-EVIDENCE-INTAKE.md) | COMPLETE |
| Phase 2A Wave A + local access bootstrap | [reports/REPORT-ISEO-SU-SITE-OPS-PHASE-2A-WAVE-A-REVIEW-AND-LOCAL-ACCESS-BOOTSTRAP.md](reports/REPORT-ISEO-SU-SITE-OPS-PHASE-2A-WAVE-A-REVIEW-AND-LOCAL-ACCESS-BOOTSTRAP.md) | COMPLETE |
| Phase 2B read-only production audit | [reports/REPORT-ISEO-SU-SITE-OPS-PHASE-2B-READ-ONLY-PRODUCTION-AUDIT.md](reports/REPORT-ISEO-SU-SITE-OPS-PHASE-2B-READ-ONLY-PRODUCTION-AUDIT.md) | COMPLETE |
| Phase 4B WPilot preinstall package + compatibility gate | [reports/REPORT-ISEO-SU-SITE-OPS-PHASE-4B-WPILOT-PREINSTALL-PACKAGE-AND-COMPATIBILITY-GATE.md](reports/REPORT-ISEO-SU-SITE-OPS-PHASE-4B-WPILOT-PREINSTALL-PACKAGE-AND-COMPATIBILITY-GATE.md) | COMPLETE / CONDITIONAL GO |
| Phase 4B-P documentation persistence checkpoint | [reports/REPORT-ISEO-SU-SITE-OPS-PHASE-4B-P-DOCUMENTATION-PERSISTENCE-CHECKPOINT.md](reports/REPORT-ISEO-SU-SITE-OPS-PHASE-4B-P-DOCUMENTATION-PERSISTENCE-CHECKPOINT.md) | COMPLETE / DOCUMENTATION PERSISTED |
| Phase 6A WPilot install-only | [reports/REPORT-ISEO-SU-SITE-OPS-PHASE-6A-WPILOT-INSTALL-ONLY.md](reports/REPORT-ISEO-SU-SITE-OPS-PHASE-6A-WPILOT-INSTALL-ONLY.md) | COMPLETE / INSTALLED INACTIVE |
| Phase 6B WPilot activation-only | [reports/REPORT-ISEO-SU-SITE-OPS-PHASE-6B-WPILOT-ACTIVATION-ONLY.md](reports/REPORT-ISEO-SU-SITE-OPS-PHASE-6B-WPILOT-ACTIVATION-ONLY.md) | COMPLETE / ACTIVE SAFE DEFAULTS |
| Phase 6C WPilot token creation-only | [reports/REPORT-ISEO-SU-SITE-OPS-PHASE-6C-WPILOT-TOKEN-CREATION-ONLY.md](reports/REPORT-ISEO-SU-SITE-OPS-PHASE-6C-WPILOT-TOKEN-CREATION-ONLY.md) | **BLOCKED / NO TOKEN** (plugin requires bridge+DEV; charter forbids bridge) |

---

## SAFE UNKNOWN summary

Resolved in 2B: hybrid architecture, docroot, WP root install, WP 7.0.2, theme `iseoblog`, plugin filesystem inventory, calculator/tariffs/forms, then-WPilot-absence, SFTP model.  

Resolved in 4B (static): canonical RC5 package identity + SHA-256; exact REST route inventory from source; safe activation defaults; token local path decision (file not created).  

Resolved in 6A: RC5 package on production as inactive `metacode-wpilot/` (27/27); no public `wpilot` REST namespace while inactive; frontend baseline intact.  

Resolved in 6B: plugin **active** with bridge/writes **off**, token **absent**; Admin diagnostics schema valid; public `wpilot/v1` namespace registered but **not invoked**; frontend/admin regression PASS.

Open: PHP runtime, Beget backup object/timestamp details, ACF UI, web-KP naming, header forwarding, menus/widgets, restore proof, physical DB table existence without DB login, external SoT (U-022). Tracked in SAFE UNKNOWN register.

**Do not invent values.** Secrets stay in local-only files.

---

*ISEO-SU-SITE-OPS Operational Index · Phase 6B COMPLETE / Phase 6C BLOCKED (token needs bridge+DEV) · 2026-07-24 · bridge/writes/REST smoke NOT AUTHORIZED.*
