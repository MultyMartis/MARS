# ISEO-SU SITE OPS — README

**Programme:** ISEO-SU-SITE-OPS  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  
**Fast entry:** [ISEO-SU-CURRENT-STATE-v1.md](ISEO-SU-CURRENT-STATE-v1.md) → [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)

---

## What this programme is

Human-supervised MARS programme for **existing production site operations** of **https://i-seo.su/** (organization **i-SEO**, operator **Andrey**).

It is the **main source of truth** for hybrid site operations documentation: charter, phase reports, site passport (planned), access model, static/WordPress boundary, source-of-truth matrix, FTP/static planning, custom tools mapping, backup/rollback model, smoke plans, and operational runbook.

**Current lifecycle:** OPERATIONS / DOCUMENTATION-STABILIZED.

Production is live and has been operated through separately chartered, human-supervised tasks. This document does **not** itself authorize production access or mutation.

---

## What it owns

- Project charter and phase model
- OPERATIONAL-INDEX and decision / SAFE UNKNOWN registers
- Current State, production architecture knowledge base, route ownership, task routing and feature baselines
- Local-only access model and SFTP/WordPress operational boundaries
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
| Live production systems | External runtime authority; access only under an exact task charter |

---

## Hybrid site context

Accepted production evidence confirms that the site is a **hybrid** of static/PHP-capable HTML files and WordPress.

Implications:

- WPilot RC6 is active with bridge/writes disabled and does not gate ordinary operations.
- Static HTML/file surfaces and theme files are operated through scoped SFTP tasks.
- Report Hub may later live on or near i-seo.su WordPress, but remains a **sibling product**, not the site-ops SoT.

Use the current Knowledge Base and Route Ownership Matrix; historical intake assumptions are not current authority.

---

## Why separate from WPilot and Report Hub

- **WPilot** is the CMS Pilot reference for WordPress (RC5 proven on DEV only). It must not become the full passport/runbook for a hybrid production site.
- **Report Hub** is a product programme for reporting tooling. It must not become the source of truth for general i-seo.su operations.
- **This locus** owns the complete hybrid operations story for i-seo.su.

---

## How to navigate

1. Read [ISEO-SU-CURRENT-STATE-v1.md](ISEO-SU-CURRENT-STATE-v1.md).
2. Use [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) for the current authority order.
3. Classify the task through the Task Routing Guide, Route Ownership Matrix and Protected Zones.
4. Open only the relevant specialized baseline (forms, Metrika IP, glossary, sitemap or tech/SEO audit).
5. Treat chronological REPORT files as historical evidence, not as the first entry point.

---

## Current safety posture

| Control | State |
|---------|-------|
| Production / external access | Exact charter + operator approval + scoped backup required |
| Secrets in repo docs | **FORBIDDEN** |
| WPilot on production | RC6 active; token local-only; bridge/writes/DEV confirmation off; 6D deferred |
| SFTP / WordPress access | Local-only profile authority; never copy secrets into tracked docs |
| Local mirror | No canonical full-site mirror claimed; scoped `production-source/` mirrors exist |
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

## Current operational rule

Historical Phase 1.5/2 intake documents remain evidence. For current work, start from Current State. Before replacing any production/runtime file from MARS, first reconcile bounded runtime changes into the matching canonical `production-source/` or theme package. Production mutation is never implied by reading this README.
