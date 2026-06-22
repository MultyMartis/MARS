# FWS-0001 — Forge WordPress Synthetic Validation Case

**ID:** FWS-0001  
**Name:** Forge WordPress Synthetic Service Site  
**Class:** Synthetic validation case  
**Client:** NONE  
**Production target:** NONE  
**WPilot target:** SIMULATION ONLY

## Purpose

Isolated synthetic workspace for FW-05 capability validation. Not a client project. Not registered in global project registry.

## Structure

| Path | Role |
|------|------|
| `FRONTEND/` | Gulp static reference build |
| `WORDPRESS/` | Theme, functionality plugin, project docs |
| `VALIDATION/` | Reference captures, diffs, validator reports |
| `RELEASE/` | RC packages |
| `TEMP/` | Disposable runtime scratch (gitignored) |

## Boundaries

- No client data
- No production credentials
- No FP-0002 assets
- WordPress runtime stored outside Git or in ignored paths

## Status

See [PROJECT-STATUS.md](PROJECT-STATUS.md).
