# MARS Bot Data Platform (`mars-data-layer`)

**project_id:** `mars-data-layer`  
**Canonical name:** MARS Bot Data Platform  
**Status:** `LOCAL SCHEMA DESIGN`  
**Authority model:** Hybrid **B + D-lite** (one PostgreSQL cluster/database `mars`, schema-per-app, least-privilege roles, MARS DB Toolkit as controlled contract layer)

---

## What this is

Source authority in Git for the future **PostgreSQL-backed runtime data plane** of MARS bots (starting with i-SEO Sales Manager and MetaBOT SEO Content Agent).

This pack owns:

- architecture and naming standards;
- migration and security contracts;
- n8n ↔ PostgreSQL data contracts;
- schema/migration source trees;
- MARS DB Toolkit design (contract layer — not yet a full product);
- cutover / rollback / Sheets-projection models;
- Server Ops handoff for PostgreSQL foundation on `VEESP-N8N-01`.

---

## What this is NOT

- Not a live PostgreSQL installation.
- Not a claim that production bots already use PostgreSQL.
- Not an n8n SQLite migration.
- Not a full HTTP Data Gateway.
- Not permission to mutate `VEESP-N8N-01`, n8n, Docker, nginx, or Google credentials in this pack alone.

---

## Source authority vs runtime

| Layer | Path | Role |
|-------|------|------|
| **Source authority (Git)** | `X:\AI MARS\projects\mars-data-layer\` | Specs, SQL migrations, fixtures, toolkit source |
| **Local disposable runtime** | `X:\MARS-Localhost\databases\mars-bot-data\` | Reproducible local PostgreSQL/dev data — **not** Git authority |
| **Production target (future)** | PostgreSQL container on `VEESP-N8N-01` | Runtime SoT after controlled cutover — Server Ops owns install |

MLI already uses `X:\MARS-Localhost\databases\` for dumps/baselines (MySQL/WordPress). Bot-data local contour is a **sibling subdirectory** under that root; it does not replace MLI MySQL conventions.

---

## Current stage

**LOCAL SCHEMA DESIGN** — `mars_core` + `app_iseo_sales` V1 migrations, roles, fixtures, and local apply/test scripts are in-tree. `app_seo_content` remains an empty placeholder schema. Still **no** production server mutation from this pack.

Roadmap: [ROADMAP.md](ROADMAP.md)

---

## Responsibility split

| Owner | Owns |
|-------|------|
| **This project / this chat line** | Architecture, schemas, migrations, Toolkit contracts, workflow data contracts, mapping, cutover design |
| **Pro: MARS Server Ops pt.2** | PostgreSQL install on VPS, Docker/volume/network, health, backup plumbing, Beget off-host DR infrastructure |
| **Bot product packs** | Business semantics: `iseo-sales-manager-bot`, `metabot-seo-content-agent` |
| **n8n** | Workflow execution truth (unchanged SQLite for n8n internals) |

Handoff: [runbooks/SERVER-OPS-POSTGRES-FOUNDATION-HANDOFF-v1.md](runbooks/SERVER-OPS-POSTGRES-FOUNDATION-HANDOFF-v1.md)

---

## Document map

| Doc | Path |
|-----|------|
| Architecture V1 | [architecture/MARS-BOT-DATA-ARCHITECTURE-v1.md](architecture/MARS-BOT-DATA-ARCHITECTURE-v1.md) |
| Local DB contract | [architecture/LOCAL-DB-DEVELOPMENT-CONTRACT-v1.md](architecture/LOCAL-DB-DEVELOPMENT-CONTRACT-v1.md) |
| Naming | [architecture/DATABASE-NAMING-STANDARD-v1.md](architecture/DATABASE-NAMING-STANDARD-v1.md) |
| Migrations | [architecture/MIGRATION-STANDARD-v1.md](architecture/MIGRATION-STANDARD-v1.md) |
| n8n data contract | [architecture/N8N-DATA-CONTRACT-STANDARD-v1.md](architecture/N8N-DATA-CONTRACT-STANDARD-v1.md) |
| Security | [architecture/POSTGRES-SECURITY-STANDARD-v1.md](architecture/POSTGRES-SECURITY-STANDARD-v1.md) |
| Backup/DR | [architecture/BACKUP-DR-STANDARD-v1.md](architecture/BACKUP-DR-STANDARD-v1.md) |
| `mars_core` scope | [architecture/MARS-CORE-SCOPE-v1.md](architecture/MARS-CORE-SCOPE-v1.md) |
| i-SEO data model v1 | [architecture/ISEO-SALES-DATA-MODEL-v1.md](architecture/ISEO-SALES-DATA-MODEL-v1.md) |
| i-SEO mapping v1 | [architecture/ISEO-SALES-DATA-MAPPING-v1.md](architecture/ISEO-SALES-DATA-MAPPING-v1.md) |
| i-SEO mapping v0 (superseded) | [architecture/ISEO-SALES-DATA-MAPPING-v0.md](architecture/ISEO-SALES-DATA-MAPPING-v0.md) |
| i-SEO migration validation | [architecture/ISEO-SALES-MIGRATION-VALIDATION-v1.md](architecture/ISEO-SALES-MIGRATION-VALIDATION-v1.md) |
| i-SEO open questions | [architecture/ISEO-SALES-DATA-OPEN-QUESTIONS-v1.md](architecture/ISEO-SALES-DATA-OPEN-QUESTIONS-v1.md) |
| SEO Content mapping v0 | [architecture/SEO-CONTENT-DATA-MAPPING-v0.md](architecture/SEO-CONTENT-DATA-MAPPING-v0.md) |
| Architecture report | [reports/REPORT-mars-bot-data-platform-architecture-v1.md](reports/REPORT-mars-bot-data-platform-architecture-v1.md) |
| Schema report | [reports/REPORT-mars-data-layer-iseo-sales-schema-v1.md](reports/REPORT-mars-data-layer-iseo-sales-schema-v1.md) |
| Roles (no passwords) | [database/roles/README.md](database/roles/README.md) |
| Core migrations | [database/core/migrations/](database/core/migrations/) |
| iSEO Sales migrations | [database/app_iseo_sales/migrations/](database/app_iseo_sales/migrations/) |
| Synthetic fixtures | [fixtures/iseo_sales/README.md](fixtures/iseo_sales/README.md) |
| Local schema tests | [tests/iseo_sales/README.md](tests/iseo_sales/README.md) |

---

## Dependencies (documented)

- n8n (external execution)
- `VEESP-N8N-01` (host target for future PG)
- i-SEO Sales Manager Bot (`projects/iseo-sales-manager-bot/`)
- MetaBOT SEO Content Agent (`projects/metabot-seo-content-agent/`)

---

## Next gate

**LOCAL SCHEMA DESIGN in progress / ready for local apply validation** — run `tests/iseo_sales/01_schema_apply.sh` against disposable local PG when available; still no VPS PostgreSQL install or production cutover from this wave.
