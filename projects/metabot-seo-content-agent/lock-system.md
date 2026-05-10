# Lock system

**Purpose:** Prevent concurrent MetaBOT operations from corrupting overlapping work (same user, same resource, or global worker capacity — **exact scope SAFE UNKNOWN**).

---

## Behaviors (documented)

- **Locks** are acquired around sensitive pipeline sections (generation, Sheets writes, QA — **SAFE UNKNOWN** which steps).
- **Lock cleanup** exists to recover from stuck or abandoned operations.
- User-visible **`/locks`** surfaces current lock state (format **SAFE UNKNOWN**).

---

## Known interaction with tasks

- **Issue:** During `/run`, a **lock** may **close correctly** while the corresponding **`seo_active_jobs`** row remains **pending**. Operators should treat lock display and job table as **eventually consistent**, not always synchronized — [known-issues.md](known-issues.md).

---

## Design notes

- **JS enforcement** is acceptable **only** for **runtime consistency** (e.g. lock tokens, idempotent writes) — aligns with architectural decision: avoid massive refactors; use small deterministic checks where they help.

---

## SAFE UNKNOWN

- Lock **granularity** (per user, per task, per chat, global).
- **TTL** and automatic expiry.
- Whether locks are stored in **Sheets**, **n8n static data**, or **Redis** — **not** evidenced in this repo.

---

*See [task-lifecycle.md](task-lifecycle.md), [admin-operations.md](admin-operations.md).*
