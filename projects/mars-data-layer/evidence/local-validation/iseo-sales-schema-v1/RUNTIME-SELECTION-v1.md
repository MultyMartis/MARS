# RUNTIME-SELECTION-v1

**Date:** 2026-09-03  
**Preferred order evaluated:** A existing PG → B container → C portable → D system-wide

## Choice: **C — Portable/local PostgreSQL** under MARS-Localhost

| Option | Result |
|--------|--------|
| A Existing PostgreSQL | Not present |
| B Docker/Podman | Not present |
| C Portable binaries | **Selected** |
| D System-wide install | Not performed (would require operator approval) |

## Runtime contract (non-authoritative)

| Item | Value |
|------|--------|
| Runtime root | `X:\MARS-Localhost\databases\mars-bot-data\` |
| Layout | `data\`, `logs\`, `backups\`, `tmp\`, `README-runtime.md` |
| Binaries | `X:\MARS-Localhost\tools\postgresql\17.11\pgsql\` |
| Listen | `127.0.0.1:5433` |
| Database | `mars` |
| Superuser / owner | `mars_owner` (local-only) |
| Auth | scram-sha-256; secrets under `X:\AI MARS\local\mars-bot-data\` (**not committed**) |
| Migrations source | `X:\AI MARS\...\projects\mars-data-layer\database\` (Git) |

## Server Ops delta (documented, not executed)

Server handoff targets **PostgreSQL 18** on VEESP. Local validation used portable **17.11**. Migrations are standard SQL and applied cleanly; production foundation remains PG 18 per handoff.
