# AG-WP-001 — Filesystem Scope Contract v1

**Document type:** Filesystem scope contract  
**Version:** v1  
**Stage:** FW-07B  
**Date:** 2026-06-24

**Extends:** [FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md](../FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md), [capability/protocols/FORGE-WORDPRESS-FILESYSTEM-SCOPE-CONTRACT-v1.md](../capability/protocols/FORGE-WORDPRESS-FILESYSTEM-SCOPE-CONTRACT-v1.md)

---

## Zones

### Brain authority — `C:\AI MARS`

| Allowed class | Examples |
|---------------|----------|
| Architecture / contracts | `projects/mars-website-factory/subsystems/forge-wordpress/` |
| Theme/plugin source | project workspace under forge-wordpress when chartered |
| Tests / reports / manifests | `operations/`, `bindings/`, `fixtures/`, agent reports |
| Approved project workspace | FP-0002 foundation docs — **not** frontend implementation |

### Runtime authority — `E:\MARS-Localhost`

| Allowed class | Examples |
|---------------|----------|
| WordPress runtime | Laragon www roots per MLI manifest |
| DB runtime | MySQL datadir (indirect via WP-CLI only) |
| Generated logs | MLI reports, smoke output |
| Local backups | operator-created backup dirs |
| Test artifacts | Playwright output |

### Forbidden classes (all operations)

- Unrelated workspaces (OCPilot, ORCA, PPC, BZPM, `.recovery-temp/`)
- Credential files (`.env`, `runtime.env`, production secrets)
- Production mounts / remote SSH paths
- Arbitrary user directories
- Vendor binaries unless MLI-approved
- WordPress **core** source changes
- Live DB file direct manipulation

---

## Per-operation scope (allowlist)

| Operation class | Read | Write |
|-----------------|------|-------|
| `wp.inspect.*` (brain) | `C:\AI MARS` project paths | none |
| `wp.inspect.*` (runtime) | MLI manifest paths, theme/plugin in runtime | none |
| `wp.plan.*` | brain docs | brain draft artifacts only |
| `wp.validate.*` (source) | project PHP/theme paths | report artifacts only |
| `wp.validate.*` (runtime) | runtime via WP-CLI indirect | report artifacts only |
| `wp.scaffold.*` / `wp.generate.*` / `wp.change.*` | approved source tree | **NOT AUTHORIZED** until charter + approval |
| `wp.checkpoint.create` | git repo scope | git commit selective — **NOT AUTHORIZED** until approval |
| `wp.backup.create` | runtime | backup dir — **NOT AUTHORIZED** until R3 approval |

**Rule:** Allowlists per operation in FW-07C harness; no broad root access.

---

*Filesystem scope contract v1.*
