# MARS Bot Data Architecture v1

**Document:** `MARS-BOT-DATA-ARCHITECTURE-v1`  
**project_id:** `mars-data-layer`  
**Status:** Normative architecture (documentation)  
**Date:** 2026-09-03  
**Recommended model:** Hybrid **B + D-lite**

---

## 1. Purpose

Define the authoritative architecture for a **PostgreSQL-backed application data plane** shared by MARS bots, without claiming that the plane is already deployed or that n8n internals move off SQLite.

PostgreSQL becomes the **runtime Source of Truth** for bot business and operational data after controlled cutover. Google Sheets becomes a **secondary projection / manual UI**. n8n remains the workflow engine; its internal SQLite is unchanged.

---

## 2. Scope

In scope:

- one PostgreSQL cluster/container;
- one database `mars`;
- schema-per-bot/application isolation;
- least-privilege roles;
- small `mars_core` + optional `mars_shared`;
- MARS DB Toolkit as controlled contract layer;
- migration, security, cutover, rollback, backup concepts;
- local development source ↔ runtime contract;
- first consumers: i-SEO Sales Manager, SEO Content Agent.

Out of physical execution in this document wave: VPS install, live credentials, Sheets migration, production workflow edits.

---

## 3. Non-goals

Explicitly **out of scope** for V1 / this foundation:

- migrating **n8n internal SQLite**;
- building a full HTTP **Data Gateway**;
- **pgvector** / semantic search memory;
- **PgBouncer**;
- **Redis / RabbitMQ / Kafka**;
- **Kubernetes**;
- granting AI agents **arbitrary SQL** (especially writes);
- multi-tenant “giant `app_id` on every table” mega-schema;
- treating Google Sheets redesign as the long-term platform.

---

## 4. Target physical architecture

**Host:** `VEESP-N8N-01`

| Component | Role |
|-----------|------|
| **n8n** | Workflow execution |
| **n8n SQLite** | n8n internal state only — **unchanged** |
| **PostgreSQL container** | Application/bot data (`mars`) |
| **Docker internal network** | n8n ↔ PostgreSQL connectivity |
| **Public exposure** | **None** for PostgreSQL (`5432` not published) |

Install/volume/network/health/backup plumbing: **Server Ops pt.2** per handoff runbook. This architecture pack does not mutate the server.

---

## 5. Logical PostgreSQL architecture

**Database:** `mars`

| Schema | Purpose |
|--------|---------|
| `mars_core` | Tiny platform metadata (apps, releases, cutover/contract versions) |
| `mars_shared` | **Optional** — only genuinely shared domains |
| `app_iseo_sales` | i-SEO Sales Manager business + runtime data |
| `app_seo_content` | SEO Content Agent business + runtime data |
| `app_*` | Future bot/application schemas |

---

## 6. Isolation model

- **Schema-per-application** — primary isolation boundary.
- **Separate roles** per app and privilege band (runtime / agent / reader).
- **Schema-qualified SQL** in Toolkit and migrations.
- **Controlled `search_path`** — never rely on ambient public defaults for app logic.
- **No** shared giant `app_id` multi-tenant soup as the default model.

Shared tables belong in `mars_shared` only when two+ apps share a true domain; otherwise duplicate primitives per app schema.

---

## 7. Role model (conceptual)

Passwords/secrets are **never** stored in this repository.

| Role | Intent |
|------|--------|
| `mars_owner` | Break-glass ownership (not used by runtime workflows) |
| `mars_migrator` | DDL / migrations only |
| `iseo_runtime` | Sales Manager workflow DB ops (DML on `app_iseo_sales` as granted) |
| `iseo_agent` | Narrower than runtime — Toolkit-mediated agent ops only |
| `iseo_reader` | Read-only reporting/debug |
| `content_runtime` | SEO Content workflow DB ops |
| `content_agent` | Narrower agent ops |
| `content_reader` | Read-only |

Runtime roles **must not** be superuser and **must not** hold DDL.

---

## 8. AI access model

**Hard rule:** AI production agents must **not** receive arbitrary SQL write capability.

```text
AI Agent
  → MARS DB Toolkit
    → validated narrow function / sub-workflow
      → PostgreSQL
```

Agents may trigger **named operations** with typed parameters. They do not compose free-form mutating SQL.

---

## 9. MARS DB Toolkit

Responsibilities:

- expose a **closed catalog** of operations (enqueue job, record event, mark delivery, claim lease, …);
- validate inputs (types, enums, size limits, required correlation/idempotency keys);
- execute **parameterized** SQL or `SECURITY DEFINER` functions with least privilege;
- enforce schema qualification and role selection;
- emit structured errors without leaking secrets;
- remain callable from n8n (sub-workflow / code node contracts) without becoming a public HTTP gateway in V1.

Non-responsibilities (V1): arbitrary query console, ORM mega-framework, multi-cloud sync engine.

---

## 10. Standard data primitives

Per application schema, prefer these **patterns** (not identical forced business tables):

| Primitive | Use |
|-----------|-----|
| `jobs` | Work queue / deferred work |
| `events` | Domain events |
| `errors` | Structured failure records |
| `idempotency_keys` | Exactly-once / at-least-once control |
| `audit_log` | Who/what/when for operator actions |
| `deliveries` / outbox | Durable outbound intents (Telegram/Gmail/…) |
| `config` | Only where justified (typed config, not dumping Sheets) |
| `agent_memory` | Only where justified; **no** pgvector in V1 |

Business entities (leads, content artifacts, …) are **app-specific**.

---

## 11. Transaction model

- Prefer **short** transactions.
- Design for **idempotency** at intake and delivery boundaries.
- Use `INSERT ... ON CONFLICT` with unique constraints where appropriate.
- Optimistic versioning where concurrent updates are expected.
- Job claim: `FOR UPDATE SKIP LOCKED`.
- **Never** hold a DB transaction open across long LLM/API/network calls.

---

## 12. Retry / defer / job model

**Statuses:** `pending` · `running` · `retry` · `completed` · `dead` · `cancelled`

**Standard fields (conceptual):**

- `available_at`
- `attempts` / `max_attempts`
- `lease_until`
- `locked_by`
- `correlation_id`
- `dedupe_key`

Workers claim only available leased-expired/unlocked jobs; dead-letter with reason; operator cancel explicit.

---

## 13. Event / audit model

Separate concerns:

| Kind | Meaning |
|------|---------|
| **Domain events** | Business-meaningful state transitions |
| **Audit events** | Operator/admin actions and privilege-sensitive changes |
| **Errors** | Failures with classification, retryability, payload refs |

Do not overload one “log sheet” into a single undifferentiated table without type discrimination.

---

## 14. Outbox / delivery model

Outbound Telegram/Gmail (and similar) intents are **durable rows** before send:

1. write outbox/delivery intent in the same transaction as domain state change when possible;
2. sender claims intent;
3. record provider result / message id;
4. retries via job/outbox status — not silent fire-and-forget.

Sheets delivery tabs become **legacy projection concepts**, not the authority after cutover.

---

## 15. AI memory model

Separate memory classes:

| Class | Notes |
|-------|-------|
| Operational state | Jobs, leases, flags — relational |
| Conversation history | Bounded, app-owned |
| Durable facts | Explicit facts tables / typed rows |
| Semantic / vector memory | **`pgvector` NOT INCLUDED IN V1** |

---

## 16. Workflow versioning

- Current **production** workflow = **frozen** for substantial redesign.
- Candidate = **new workflow ID/version**, inactive until validation.
- No substantial in-place redesign of the live production graph.
- Record `workflow_version` on events/jobs for forensic clarity.

---

## 17. Cutover model

Ordered states:

1. `SHEETS_PRIMARY`
2. `PG_SHADOW`
3. `PG_CANDIDATE_VALIDATED`
4. `CUTOVER`
5. `PG_PRIMARY`
6. `SHEETS_PROJECTION`

Each transition requires evidence (validation report, backup, operator approval).

---

## 18. Rollback model

| Mode | When | Meaning |
|------|------|---------|
| **PRE-CUTOVER ROLLBACK** | Before PG is authoritative | Disable candidate; Sheets remains SoT; discard/ignore shadow |
| **POST-CUTOVER ROLLBACK** | After PG is authoritative | Restore/repair **PostgreSQL**; forward-fix candidate if needed |

**Hard rule:** after PostgreSQL becomes authoritative, the **old Sheets-based workflow is NOT a valid rollback** to “previous SoT.” Sheets may remain as projection/UI only.

---

## 19. Google Sheets role after migration

- **PostgreSQL** = authoritative store.
- **Sheets** = projection and/or manual command UI.
- One-way async projection preferred; dual-write only during shadow phases under charter.

---

## 20. Backup / DR concept

Initial:

- logical backups (`pg_dump` family);
- off-VPS copy;
- restore testing required.

**Beget:** future **off-host backup / DR target candidate** only.  
Live replication / hot standby is **not** approved by this V1 architecture — requires a later decision gate.

---

## 21. Scaling path

Scale **when evidence requires**, not by default:

| Trigger | Possible move |
|---------|----------------|
| Noisy-neighbor / blast radius | Separate DB per app |
| Host resource ceiling | Separate DB host |
| Connection storms | PgBouncer |
| Many non-n8n clients | Controlled Gateway |
| Semantic memory need | pgvector (chartered) |
| Heavy async fan-out | Dedicated queue |

---

## 22. Ownership boundaries

| Lane | Owns |
|------|------|
| **This chat / `mars-data-layer`** | Architecture, schemas, migrations, Toolkit, workflow data contracts, migration/cutover design |
| **Pro: MARS Server Ops pt.2** | PostgreSQL installation, Docker, volume, network, server backup plumbing, resource/health, Beget DR infrastructure |

---

## Related standards

- [LOCAL-DB-DEVELOPMENT-CONTRACT-v1.md](LOCAL-DB-DEVELOPMENT-CONTRACT-v1.md)
- [DATABASE-NAMING-STANDARD-v1.md](DATABASE-NAMING-STANDARD-v1.md)
- [MIGRATION-STANDARD-v1.md](MIGRATION-STANDARD-v1.md)
- [N8N-DATA-CONTRACT-STANDARD-v1.md](N8N-DATA-CONTRACT-STANDARD-v1.md)
- [POSTGRES-SECURITY-STANDARD-v1.md](POSTGRES-SECURITY-STANDARD-v1.md)
- [BACKUP-DR-STANDARD-v1.md](BACKUP-DR-STANDARD-v1.md)
- [MARS-CORE-SCOPE-v1.md](MARS-CORE-SCOPE-v1.md)
