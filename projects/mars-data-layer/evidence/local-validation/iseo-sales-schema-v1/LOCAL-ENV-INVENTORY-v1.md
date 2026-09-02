# LOCAL-ENV-INVENTORY-v1

**Date:** 2026-09-03  
**Scope:** read-only inventory before disposable PostgreSQL runtime for MARS Bot Data Platform  
**Workstation volume:** `X:` label `AI WS`

| Capability | Present | Version | Path | Notes |
|---|---|---|---|---|
| PostgreSQL (before task) | No | — | — | No system `psql` / Windows service on 5432 |
| PostgreSQL (after Option C) | Yes | 17.11 | `X:\MARS-Localhost\tools\postgresql\17.11\pgsql\bin` | Portable EDB binaries; not a Windows service |
| psql | Yes | 17.11 | same `bin\` | Used for all apply/test |
| Docker | No | — | — | Docker Desktop not available |
| Podman | No | — | — | — |
| WSL | No | — | — | `wsl` only offers install help; not used |
| Laragon | Yes | (MLI contour) | `X:\MARS-Localhost\laragon\` | MySQL/MariaDB on **3306** — untouched |
| Existing 5432 listener | No | — | — | Port free; local PG uses **5433** |
| Git bash | Yes | — | `X:\MARS-Localhost\laragon\bin\git\bin\bash.exe` | Available; PowerShell runner preferred on Windows |
| MARS-Localhost layout | Yes | — | `X:\MARS-Localhost\` | databases / tools / sites conventions present |

**Laragon / website DB:** not modified. PostgreSQL is an independent local-only service.
