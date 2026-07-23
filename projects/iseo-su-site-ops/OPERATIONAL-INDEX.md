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
| **Lifecycle** | **PRE-WPILOT / PRE-INSTALL CONDITIONAL GO** |
| **Project status** | Active documentation programme; production writes **NOT AUTHORIZED** |
| **Current phase** | **PHASE 4B — COMPLETE / PRE-INSTALL CONDITIONAL GO** |
| **Phase 2B status** | **COMPLETE / READ-ONLY PRODUCTION ARCHITECTURE CAPTURED** |
| **Phase 4B status** | **COMPLETE / PRE-INSTALL CONDITIONAL GO** (static package + compatibility only) |
| **Production connection** | Read-only SFTP + limited REST/public GET **executed** under 2B charter; default reuse **NOT AUTHORIZED** without new charter |
| **Access files** | **LOCAL-ONLY FILLED / VALIDATED** (Git-ignored) |
| **WPilot** | **ABSENT on production** / package **ACCEPTED MATCH** RC5 / install **HOLD** until GATE 6A |
| **FTP/SFTP** | **SFTP read-only used in 2B**; further use charter-gated |
| **Local mirror** | **NOT DECIDED** |
| **ATLAS** | **MINT DEFERRED** |
| **Token creation** | **NOT AUTHORIZED** (path decided; file NOT CREATED) |
| **REST smoke (WPilot)** | **NOT AUTHORIZED** |
| **Controlled write smoke** | **NOT AUTHORIZED** |
| **Next operator action** | Review Phase 4B REPORT; approve 4B-1 / 4B-2 / 4B-3 before any install |
| **Next gate** | **ISEO-SU-SITE-OPS — PHASE 6A WPILOT INSTALL-ONLY** (after CONDITIONAL GO conditions satisfied); else **PHASE 4C** remediation |

Hosting: **Beget**. WordPress Admin: `https://i-seo.su/wp-admin/`. Staging: **absent**. Architecture: **hybrid** (root WP + physical PHP-capable HTML + shared assets) — see boundary map.

Canonical package: `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc5.zip`  
SHA-256: `43c71a561872a037f294a12d5194d0925e988392599f02c1eeb2d8b1c52e1577`

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
| 3 | Read charter + system boundaries + Phase 2B audit + Phase 4B WPilot gate |
| 4 | Check Decision / SAFE UNKNOWN / protected zones |
| 5 | For credentials: local-only files — never paste secrets into chat |
| 6 | Execute only the **next authorized task** after operator acceptance |
| 7 | Close with REPORT under `reports/` — no secrets, no production mutation |

---

## Active HOLDs

| HOLD | Status |
|------|--------|
| Production **write** / upload / settings save | **HOLD** |
| Beget / hosting **panel** login by agent | **HOLD** |
| Unchartered SFTP reuse | **HOLD** (2B was one-time charter) |
| Unchartered WP Admin reuse | **HOLD** |
| WPilot plugin installation on i-seo.su | **HOLD** (await GATE 6A) |
| Token / profile creation for i-seo.su (WPilot token) | **HOLD** |
| WPilot REST smoke | **HOLD** |
| Controlled write smoke | **HOLD** |
| Database / phpMyAdmin | **HOLD** |
| ATLAS WEB/DOM/PRJ mint | **DEFERRED** |
| Local mirror creation | **DEFAULT DEFER** |
| Firefox Browser Workstation implementation | **DEFERRED** |

---

## Next authorized task

After operator acceptance of CONDITIONAL GO conditions (gates 4B-1, 4B-2, 4B-3):

**ISEO-SU-SITE-OPS — PHASE 6A WPILOT INSTALL-ONLY**

Do **not** combine with activation, token, or REST.

If conditions cannot be accepted: **PHASE 4C WPILOT PREINSTALL REMEDIATION**.

---

## Forbidden actions (current)

- Production writes / uploads / chmod / deletes
- WordPress settings saves, updates, installs, activations
- WPilot install / token / REST (until separately gated)
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
| WPilot token storage decision | [ISEO-SU-WPILOT-TOKEN-STORAGE-DECISION-v1.md](ISEO-SU-WPILOT-TOKEN-STORAGE-DECISION-v1.md) |

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

---

## SAFE UNKNOWN summary

Resolved in 2B: hybrid architecture, docroot, WP root install, WP 7.0.2, theme `iseoblog`, plugin filesystem inventory, calculator/tariffs/forms, WPilot absence, SFTP model.  

Resolved in 4B (static): canonical RC5 package identity + SHA-256; exact REST route inventory from source; safe activation defaults; token local path decision (file not created).  

Open: PHP runtime, exact plugin actives, ACF UI, web-KP naming, header forwarding, menus/widgets, restore proof, external SoT (U-022). Tracked in SAFE UNKNOWN register.

**Do not invent values.** Secrets stay in local-only files.

---

*ISEO-SU-SITE-OPS Operational Index · Phase 4B COMPLETE / CONDITIONAL GO · 2026-07-24 · production writes NOT AUTHORIZED.*
