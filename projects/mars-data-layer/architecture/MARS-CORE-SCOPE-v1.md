# mars_core Scope v1

**Document:** `MARS-CORE-SCOPE-v1`  
**project_id:** `mars-data-layer`  
**Date:** 2026-09-03

---

## 1. Intent

Keep schema **`mars_core` small**. It is platform metadata for the bot data plane — **not** a dumping ground for bot business data.

---

## 2. Candidate contents (V1)

| Area | Examples (conceptual) |
|------|------------------------|
| Apps registry | Registered application/schema ids (`app_iseo_sales`, …) |
| Workflow releases | Known workflow_version ↔ app bindings (documentation-grade records) |
| Deployment / cutover metadata | Current cutover state per app (`SHEETS_PRIMARY`, `PG_SHADOW`, …) |
| Schema / contract versions | Migrator tip / data-contract version labels |

Exact tables land in a later schema-design wave.

---

## 3. Explicit prohibitions

Do **not** put into `mars_core`:

- leads, raw emails, CLEAN rows;
- content jobs, generated articles, conversation blobs;
- Telegram delivery bodies as primary store;
- per-bot config that is app-specific (belongs in `app_*`);
- vector embeddings;
- “temporary” business tables “just for convenience.”

---

## 4. Relationship to `mars_shared`

`mars_shared` is optional and **also** not a business dumping ground. Use only for domains proven shared by ≥2 apps. Prefer duplication of primitives inside each `app_*` until sharing is real.
