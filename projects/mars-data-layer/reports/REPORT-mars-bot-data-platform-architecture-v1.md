# REPORT — MARS Bot Data Platform Architecture V1

**Date:** 2026-09-03  
**project_id:** `mars-data-layer`  
**Wave:** Architecture V1 + Local Development Foundation  
**Mode:** Documentation + source skeleton only

---

## 1. Verdict

**MARS BOT DATA PLATFORM ARCHITECTURE V1 ESTABLISHED — READY FOR LOCAL SCHEMA DESIGN**

No VPS/n8n/Docker/nginx mutation. No live credentials. No Sheets migration. No production workflow changes.

---

## 2. Project registration

| Field | Value |
|-------|-------|
| **project_id** | `mars-data-layer` |
| **Canonical name** | MARS Bot Data Platform |
| **Registry** | `registry/project-registry.md` |
| **status** | `planned` (documentation foundation; not production PG runtime) |
| **phase** | **ARCHITECTURE / FOUNDATION** — Hybrid B+D-lite; specs + skeleton only |
| **Dependencies (documented)** | n8n, VEESP-N8N-01, i-SEO Sales Manager Bot, MetaBOT SEO Content Agent |

---

## 3. Source authority

`X:\AI MARS\projects\mars-data-layer\` is Git source authority for architecture, migrations, fixtures, and future Toolkit.

Local runtime contour (disposable): `X:\MARS-Localhost\databases\mars-bot-data\` per LOCAL-DB contract (directory **not** created/installed in this wave).

---

## 4. Target architecture

Hybrid **B + D-lite** on `VEESP-N8N-01`: n8n + existing SQLite unchanged; one PostgreSQL 18 container; internal Docker connectivity; no public `5432`.

---

## 5. Database / schema model

- Database: `mars`
- Schemas: `mars_core`, optional `mars_shared`, `app_iseo_sales`, `app_seo_content`, future `app_*`
- Skeleton migration folders created (empty `.gitkeep` only)

---

## 6. Roles / security

Conceptual roles: `mars_owner`, `mars_migrator`, `iseo_*`, `content_*`.  
Standards: least privilege, no runtime DDL/superuser, no public port, credentials outside Git.  
See `architecture/POSTGRES-SECURITY-STANDARD-v1.md`.

---

## 7. MARS DB Toolkit

Defined as controlled contract layer (named ops, validation, parameterized SQL/functions).  
**Not implemented** in this wave (`toolkit/README.md` placeholder).

---

## 8. Standard primitives

Per-app patterns: jobs, events, errors, idempotency_keys, audit_logs, deliveries/outbox, optional config/agent_memory. Business tables remain app-specific.

---

## 9. AI access model

`AI Agent → MARS DB Toolkit → validated narrow function/sub-workflow → PostgreSQL`.  
Arbitrary AI SQL write **forbidden**.

---

## 10. Workflow versioning / cutover

Production frozen; candidate new ID/version; cutover states through `PG_PRIMARY` / `SHEETS_PROJECTION`.  
Post-cutover: old Sheets-primary workflow is **not** valid SoT rollback.

---

## 11. Google Sheets migration model

Sheets primary → shadow → cutover → PG primary → Sheets projection only.

---

## 12. Local DB development model

Git source vs `X:\MARS-Localhost\databases\mars-bot-data\` runtime.  
Evidence: existing MLI `databases\` zone (MySQL dumps/baselines) — bot-data is sibling contour.  
PostgreSQL **not** installed in this wave.

---

## 13. Sales Manager mapping status

`architecture/ISEO-SALES-DATA-MAPPING-v0.md` — concept classification only; **not** final schema.

---

## 14. SEO Content mapping status

`architecture/SEO-CONTENT-DATA-MAPPING-v0.md` — concept classification only; **not** final schema.

---

## 15. Server Ops handoff

`runbooks/SERVER-OPS-POSTGRES-FOUNDATION-HANDOFF-v1.md` ready for `Pro: MARS Server Ops pt.2`.  
**Not executed.**

---

## 16. Git

| Item | Value |
|------|-------|
| Worktree base | `origin/mars/canonical-post-recovery` |
| Worktree path | `X:\AI MARS STORAGE\git-sync-mars-data-layer-architecture-v1-20260903-010429\repo` |
| Allowlisted paths | `projects/mars-data-layer/**`, `registry/project-registry.md` |
| Foreign WIP | Untouched in primary working tree |

*(Commit hashes filled at closeout.)*

---

## 17. Next gate

**Local schema design** for `mars_core` + refined `app_iseo_sales` mapping v1 — still no production server mutation unless Server Ops charter runs Phase 1 separately.
