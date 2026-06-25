# FP-0002 — WordPress Foundation Preflight v1

**Document type:** FW-06A preflight  
**Version:** v1  
**Date:** 2026-06-23  
**Project:** FP-0002 — Шпиговский  
**Runtime ID:** MLI-WP-FP0002-LOCAL  
**Stage class:** Pre-integration project preparation

---

## Stage classification

```text
FW-06A: FP-0002 WordPress Foundation Preparation
Class: Pre-integration project preparation
Client runtime: LOCAL ONLY
Frontend authority: NOT YET ADMITTED
Theme integration: HOLD
Production: NONE
```

---

## Operator decision (2026-06-23)

Prepare local WordPress foundation **in parallel** with unfinished frontend polishing. **Forbidden:** integrate unfinished `src/`, declare frontend approved, production deploy.

---

## Project authority sources reviewed

| Source | Path | Use |
|--------|------|-----|
| V6 operational status | `workspaces/fp-0002-shpigovsky-v6/foundation/FP-0002-V6-OPERATIONAL-STATUS.md` | Frontend state — Foundation, not Production Pass |
| Page inventory | `workspaces/fp-0002-shpigovsky-v6/foundation/FP-0002-V6-PAGE-INVENTORY.md` | Page skeleton only |
| URL map | `workspaces/fp-0002-shpigovsky-v6/foundation/FP-0002-V6-URL-MAP.md` | Slug policy |
| Operations passport | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PROJECT-PASSPORT.md` | Project identity |
| Modal/forms review | `workspaces/fp-0002-shpigovsky-v6/reviews/modals/` | Documented only — no WP forms |
| Forge intake contract | `projects/mars-website-factory/subsystems/forge-wordpress/contracts/` | Architecture boundaries |
| MLI WordPress profile | `projects/mars-localhost-infrastructure/MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md` | Runtime layout |

---

## Frontend state (not admitted)

| Field | Value |
|-------|-------|
| Workspace | `workspaces/fp-0002-shpigovsky-v6/` |
| Production Pass | **NOT ISSUED** |
| Operator final visual approval | **NOT ISSUED** |
| Approved Forge handoff | **NOT AVAILABLE** |
| `src/` changes in FW-06A | **NONE** |

---

## Page inventory authority (skeleton scope)

Top-level routes from approved inventory: Home, `/uslugi/` hub + confirmed L2 sections, `/specyalisty/`, `/o-centre/` + subpages, `/otzyvy/`, `/blog/`, `/kontakty/`, legal hub + discrete legal slugs.

**Not created:** leaf service URLs (~52 XLSX nodes), article singles, 404 template integration.

---

## Hard boundaries confirmed

- No `dist/` or `src/` copy into theme
- No section ACF / flexible content
- No WPilot production credentials
- No random plugins / page builders
- FWS-0001 synthetic runtime untouched

---

## Preflight Git state

| Check | Result |
|-------|--------|
| Branch | `mars/post-cycle8-live-tests` |
| HEAD | `114b064` (newer than referenced `55850b7`) |
| Commit `55850b7` | **EXISTS** in history |
| MLI uncommitted diff | 5 MLI docs — **not pre-committed** (FW-06A updates same lane) |
| FP-0002 `src/` | **Unmodified** by this task |
| Pre-checkpoint commit | **NOT PERFORMED** |

---

## Runtime target

| Field | Value |
|-------|-------|
| Physical root | `D:\MARS-Localhost\sites\wordpress\projects\shpigovsky` |
| Junction | `D:\MARS-Localhost\laragon\www\shpigovsky` |
| URL | `http://shpigovsky.test` |
| Database | `mars_wp_fp0002` |
| Secrets | `C:\AI MARS\local\mli\fp-0002\runtime.env` |

---

## Related artifacts

- [FP-0002-WORDPRESS-FOUNDATION-REPORT-v1.md](FP-0002-WORDPRESS-FOUNDATION-REPORT-v1.md)
- [MLI-WP-FP0002-LOCAL-RUNTIME-MANIFEST-v1.md](../../../../mars-localhost-infrastructure/manifests/MLI-WP-FP0002-LOCAL-RUNTIME-MANIFEST-v1.md)

---

*FW-06A preflight — FP-0002.*
