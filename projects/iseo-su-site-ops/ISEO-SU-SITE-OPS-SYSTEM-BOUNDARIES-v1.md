# ISEO-SU-SITE-OPS System Boundaries v1

**Status:** ACCEPTED (Phase 1.5)  
**Decision date:** 2026-07-22  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`

---

## Purpose

Define ownership and non-ownership between this site-ops programme and sibling/supporting MARS surfaces so hybrid operations do not drift into WPilot, Report Hub, Forge, or ATLAS as false SoT.

---

## Boundary matrix

| Surface | Owns | Does not own | Relationship to site-ops |
|---------|------|--------------|---------------------------|
| **ISEO-SU-SITE-OPS** (`projects/iseo-su-site-ops/`) | Hybrid site ops docs for i-seo.su: charter, passport (planned), access, SoT matrix, FTP plan, runbook, smoke plans | WPilot plugin source; Report Hub product; ATLAS IDs; Localhost runtime | **Main SoT** |
| **WPilot** (`projects/wpilot/`) | WPilot programme, RC5 authority, plugin contracts, DEV proof, local token **policy** | Full i-seo.su passport; static HTML ownership; hybrid runbook | Supporting WordPress-only methodology; may later hold a **connection profile reference**, not complete site SoT |
| **WPilot Plugin** (`projects/wpilot/plugin/…`) | Plugin implementation & REST contracts (DEV proven) | Static files; hosting; production deploy authority | Optional future WordPress channel for this site — **PRODUCTION HOLD** |
| **Static HTML / files** | File-level public surfaces outside WP content model | WP post_content / ACF entity model | Owned **documentary** by site-ops; channel likely FTP/static — **NOT CONFIGURED** |
| **WordPress** (on i-seo.su) | WP runtime entities when mapped | Static file tree unless proven otherwise | Hybrid half — facts still **SAFE UNKNOWN** / OPERATOR-CONTEXT |
| **Report Hub** (`projects/iseo-report-hub/`) | Reporting product architecture & demos | General site operations; hybrid passport | **Sibling product** — must not become site-ops SoT |
| **Forge WordPress** (`…/forge-wordpress/`) | WP engineering safety methodology; FP-0002 pilot lessons | i-seo.su project ownership; production architecture copy | Methodology-only; **FP-0002 architecture must not be copied** |
| **Website Factory** (`projects/mars-website-factory/`) | Static page/component/QA methodology | Runtime deployment engine for i-seo.su | Methodology-only |
| **ATLAS** (`projects/atlas/`) | Business identity/relationship registry docs | Operational runbooks; site technical SoT | Registry only; **no mint** this task; does **not** own operational documentation |
| **MLI** (`projects/mars-localhost-infrastructure/`) | Shared local runtime authority (`X:\MARS-Localhost`) | Production hosting; site-ops docs | Optional future local mirror — **NOT DECIDED**; Localhost is **not** production |
| **Survivability / GitGuard** (`projects/mars-survivability/`) | Safety, backup/rollback patterns, protected zones methodology | Site-specific passport facts | Supporting methodology |
| **Remote Operations Layer** (`projects/remote-operations-layer/`) | Remote-ops charter/checklists | Connector; credentials; authorization to access live systems | Supporting discipline — **not** authorization source |
| **Firefox Developer Edition Browser Workstation** | Future dedicated browser QA workstation (deferred record) | Production authorization; credential vault; automation | Separate deferred programme surface — **not** authorization for external access |

---

## Explicit statements (normative)

1. **WPilot does not own static HTML** for i-seo.su. Static/file ownership belongs to site-ops planning (and later FTP/static procedures).
2. **Forge does not own the project.** Forge/FP-0002 patterns may inform safety; they are not the architecture template for i-seo.su.
3. **Report Hub is a sibling.** Product decisions there do not redefine site-ops ownership.
4. **ATLAS does not own operational documentation.** Identity mint is deferred; operational docs stay in this locus.
5. **Localhost is not production.** Any future mirror under `X:\MARS-Localhost` is local execution only.
6. **Browser Workstation is not authorization** for external access, FTP, WordPress admin, or REST.

---

## Authority on conflict

For i-seo.su hybrid site operations documentation:

```text
AGENTS.md / .cursorrules / X-drive authority
  → projects/iseo-su-site-ops/
    → supporting methodology (WPilot, Forge, Survivability, ROL, MLI, Factory, ATLAS)
      → chat handoffs (supporting evidence only)
```

Do **not** create a second full site passport under `projects/wpilot/sites/` for this production programme.

---

## Current access posture

| Channel | State |
|---------|-------|
| Production web mutation | NOT AUTHORIZED |
| FTP/SFTP | NOT CONFIGURED / NOT AUTHORIZED |
| WPilot REST | DOCUMENTARY ONLY / PRODUCTION HOLD |
| Local mirror | NOT DECIDED |
| Browser Workstation | IMPLEMENTATION DEFERRED |

---

*System Boundaries v1 · 2026-07-22.*
