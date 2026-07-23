# ISEO-SU SITE OPS — README

**Programme:** ISEO-SU-SITE-OPS  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  
**Fast entry:** [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)

---

## What this programme is

Human-supervised MARS programme for **existing production site operations** of **https://i-seo.su/** (organization **i-SEO**, operator **Andrey**).

It is the **main source of truth** for hybrid site operations documentation: charter, phase reports, site passport (planned), access model, static/WordPress boundary, source-of-truth matrix, FTP/static planning, custom tools mapping, backup/rollback model, smoke plans, and operational runbook.

**Current lifecycle:** DOCUMENTARY INTAKE / PRE-CONNECTION.  
**Production connection:** NOT AUTHORIZED.

---

## What it owns

- Project charter and phase model
- OPERATIONAL-INDEX and decision / SAFE UNKNOWN registers
- Site passport and hybrid ownership documentation (when created)
- Access model and connection plans (FTP/static; WPilot plugin plan — planning only until authorized)
- Backup/rollback and protected-zone documentation for this site
- Smoke plans and operational runbook (when authorized to draft)
- Programme reports under `reports/`

---

## What it does not own

| Surface | Owner / note |
|---------|----------------|
| WPilot programme + plugin contracts | `projects/wpilot/` |
| Report Hub product architecture | `projects/iseo-report-hub/` (sibling) |
| Website Factory methodology | `projects/mars-website-factory/` |
| Forge WordPress methodology | `projects/mars-website-factory/subsystems/forge-wordpress/` — **not** project owner; **do not** copy FP-0002 |
| ATLAS identity mint | `projects/atlas/` — mint **DEFERRED** |
| Localhost runtime root | `X:\MARS-Localhost` via MLI — **no mirror now** |
| Remote connector / credential vault | ROL is methodology only |
| Live production systems | External; access **NOT AUTHORIZED** |

---

## Hybrid site context

Operator context (**OPERATOR-CONTEXT**, not verified technical evidence): the site is a **hybrid** of static HTML/files and WordPress.

Implications:

- WPilot covers **WordPress-only** operational surfaces when later authorized.
- Static HTML / file surfaces need a separate ownership and connection model (FTP/static planning — Phase 4A).
- Report Hub may later live on or near i-seo.su WordPress, but remains a **sibling product**, not the site-ops SoT.

Do **not** claim verified architecture until Phase 2+ evidence is accepted.

---

## Why separate from WPilot and Report Hub

- **WPilot** is the CMS Pilot reference for WordPress (RC5 proven on DEV only). It must not become the full passport/runbook for a hybrid production site.
- **Report Hub** is a product programme for reporting tooling. It must not become the source of truth for general i-seo.su operations.
- **This locus** owns the complete hybrid operations story for i-seo.su.

---

## How to navigate

1. Start at [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md).
2. Read [ISEO-SU-SITE-OPS-CHARTER-v1.md](ISEO-SU-SITE-OPS-CHARTER-v1.md) and [ISEO-SU-SITE-OPS-SYSTEM-BOUNDARIES-v1.md](ISEO-SU-SITE-OPS-SYSTEM-BOUNDARIES-v1.md).
3. Use [ISEO-SU-SITE-OPS-PHASE-MODEL-v1.md](ISEO-SU-SITE-OPS-PHASE-MODEL-v1.md) for phase gates.
4. Track decisions and unknowns in the Decision and SAFE UNKNOWN registers.
5. Close work with REPORT files under `reports/`.

---

## Current safety posture

| Control | State |
|---------|-------|
| Production / external access | **NOT AUTHORIZED** |
| Secrets in repo docs | **FORBIDDEN** |
| WPilot on production | **HOLD** (documentary / RC5 DEV reference only) |
| FTP | **NOT CONFIGURED** |
| Local mirror | **NOT DECIDED** |
| ATLAS mint | **DEFERRED** |
| Firefox Browser Workstation | Direction approved; **implementation DEFERRED** |
| Git | No stage/commit/push unless separately chartered |

---

## Source authority

- **Primary SoT for this site's operations docs:** this directory.
- **Governance:** `AGENTS.md`, `.cursorrules`, `governance/mars-x-drive-root-authority-v1.md`, `governance/mars-infrastructure-reality-v1.md`.
- **Supporting methodology:** WPilot, Forge WordPress experience pack, Survivability, ROL, MLI, Website Factory, ATLAS — read-only patterns.
- **Chat handoffs:** supporting evidence only; repository docs win on conflict after reconciliation.

---

## No production access yet

Phase 1.5 creates documentary locus only.  
Next recommended phase after operator acceptance: **PHASE 2 — NON-SECRET SITE EVIDENCE INTAKE**.
