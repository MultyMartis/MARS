# Forge WordPress FWS-0001 — Source Persistence Decision v1

**Document type:** Source persistence decision record  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** FW-05R closure checkpoint  
**Case:** FWS-0001

---

## Problem

FWS-0001 synthetic implementation currently lives under `workspaces/*`, which is globally gitignored. Proven Forge capability without Git persistence loses:

- Theme source (`fws-synthetic`)
- Functionality plugin source (`fws-synthetic-core`)
- ACF JSON field groups
- Architecture / project docs
- Validation scripts and textual reports
- Issue history and reproducibility evidence

Runtime on `D:\MARS-Localhost` is intentionally outside Git and cannot substitute for source authority.

---

## Decision

```text
Track a narrowly whitelisted FWS-0001 source-and-evidence subset
inside the main MARS repository.
```

| Option | Decision |
|--------|----------|
| Leave all synthetic source outside Git | **Rejected** — reproducibility loss |
| Separate repository for FWS-0001 | **Deferred** — not at this stage |
| Narrow whitelist in main MARS repo | **Selected** |

---

## Tracked scope (source authority)

| Path | Content |
|------|---------|
| `workspaces/forge-wordpress-synthetic/FWS-0001/README.md` | Case identity |
| `workspaces/forge-wordpress-synthetic/FWS-0001/PROJECT-STATUS.md` | Status pointer |
| `workspaces/forge-wordpress-synthetic/FWS-0001/.gitignore` | Workspace-local ignores |
| `workspaces/forge-wordpress-synthetic/FWS-0001/FRONTEND/src/` | Static reference source |
| `workspaces/forge-wordpress-synthetic/FWS-0001/FRONTEND/gulpfile.js` | Build entry |
| `workspaces/forge-wordpress-synthetic/FWS-0001/FRONTEND/package.json` | Dependencies manifest |
| `workspaces/forge-wordpress-synthetic/FWS-0001/FRONTEND/package-lock.json` | Lock file |
| `workspaces/forge-wordpress-synthetic/FWS-0001/WORDPRESS/theme-source/` | Theme source authority |
| `workspaces/forge-wordpress-synthetic/FWS-0001/WORDPRESS/functionality-plugin/` | Plugin source authority |
| `workspaces/forge-wordpress-synthetic/FWS-0001/WORDPRESS/acf-json/` | ACF JSON exports |
| `workspaces/forge-wordpress-synthetic/FWS-0001/WORDPRESS/project-docs/` | Architecture docs |
| `workspaces/forge-wordpress-synthetic/FWS-0001/VALIDATION/reports/` | Textual validation evidence (`.md` only enforced via ignore rules) |
| `workspaces/forge-wordpress-synthetic/FWS-0001/VALIDATION/scripts/` | Validation scripts |
| `workspaces/forge-wordpress-synthetic/FWS-0001/VALIDATION/package.json` | Validation tooling manifest |
| `workspaces/forge-wordpress-synthetic/FWS-0001/VALIDATION/package-lock.json` | Validation lock |
| `workspaces/forge-wordpress-synthetic/FWS-0001/RELEASE/FWS-0001-RC2/` | Source manifests, handoff sim, acf-json copies (text/json/md — no zips) |

**Path note:** Task spec referenced `RELEASE/source-manifests/`; actual RC2 layout uses `RELEASE/FWS-0001-RC2/` — equivalent source manifest role.

---

## Explicitly excluded (never tracked)

| Category | Examples |
|----------|----------|
| Runtime WordPress tree | `D:\MARS-Localhost\sites\wordpress\synthetic\fws-0001\` |
| Credentials | `.env`, `runtime.env`, `wp-config.php`, `credentials*` |
| Database | `*.sql`, dumps |
| Generated frontend | `FRONTEND/dist/` |
| Node vendor | `node_modules/` |
| Visual artifacts | `*.png`, `*.jpg`, `screenshots/`, `rendered/`, `reference/`, `diff/` |
| Release binaries | `*.zip` |
| PHPCS raw output | `_phpcs-live-output.txt` |
| WordPress core | Not in workspace — on D: only |
| Uploads / media runtime | D: only |

---

## Source authority rule

| Rule | Detail |
|------|--------|
| **SoT** | `C:\AI MARS\workspaces\forge-wordpress-synthetic\FWS-0001\WORDPRESS\` |
| **Runtime copy** | D: deploy target — fixes must be backported to C: source before commit |
| **RC2 manifests** | Must reflect current tracked source at checkpoint |

---

## Implementation

Root `.gitignore` updated with narrow allow-list pattern (mirrors Triumph landing workspace model). See FW-05R closure checkpoint commit.

---

## Related

- [FORGE-WORDPRESS-FW-05R-LIVE-SYNTHETIC-VALIDATION-REPORT-v1.md](FORGE-WORDPRESS-FW-05R-LIVE-SYNTHETIC-VALIDATION-REPORT-v1.md)
- [FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md](../../FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md)

---

*Source persistence decision v1 — FW-05R checkpoint.*
