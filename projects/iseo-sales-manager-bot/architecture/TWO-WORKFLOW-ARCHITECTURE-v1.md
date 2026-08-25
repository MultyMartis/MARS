# TWO-WORKFLOW ARCHITECTURE v1

**Product:** i-SEO Sales Manager Bot  
**Status:** documented architecture — **not** live n8n proof  
**Authority:** Phase 2 operator decisions (exactly two workflows)

---

## 1. Verdict

v1 uses **exactly two** n8n workflows:

| ID | Working name | Role analogue |
|----|--------------|---------------|
| **WF-A** | `i-SEO Sales Manager - Operational.dev` | MetaBOT **Worker**-like processing + scheduled intake |
| **WF-B** | `i-SEO Sales Manager - Admin.dev` | MetaBOT **Admin**-like ops surface |

**No Intake workflow** as a third graph: Operational owns Gmail schedule intake; Admin owns Telegram command entry. This deliberately **does not** clone MetaBOT’s three-workflow SEO Agent set.

---

## 2. Communication model (preferred)

**Prefer: shared Sheets/config state only — no direct inter-workflow Execute Workflow / webhook dependency for v1.**

| Channel | Direction | Purpose |
|---------|-----------|---------|
| **CONFIG tab** | Admin writes · Operational reads | `ai_enabled`, chat IDs, versions, probe flags |
| **CLEAN / RAW / ERRORS / LEAD_EVENTS** | Operational writes · Admin reads | Status, stats, last error, health signals |
| **Telegram** | Separate entry points | Manager cards (Operational) · Admin replies (Admin) |

**Webhook between A↔B:** **NOT REQUIRED FOR V1** unless a later evidence wave proves schedule+admin race conditions that Sheets cannot resolve. Avoid Execute Workflow chains that create skipped-branch reference failures (MetaBOT known failure mode).

---

## 3. WORKFLOW A — Operational.dev

### 3.1 Responsibilities (mandatory)

1. Scheduled Gmail intake (bounded query: label + limit + time window).
2. Lead mail parser (`parser_version` stamped).
3. **Immutable RAW append** (parser evidence only — no fake AI columns).
4. CONFIG read (fail-closed AI → OFF if unread).
5. AI mode gate.
6. Deterministic processing (always runs; is also the fallback).
7. Optional **single** structured AI call when AI ON.
8. Deterministic validation of AI output.
9. Fallback to AI OFF result on any AI failure.
10. Dedupe (message-id vs contact vs weak site).
11. CLEAN append or update (manager-facing state).
12. Manager Telegram card (human Russian; copy-ready reply).
13. Gmail label finalization (PROCESSED / error; remove incoming only after safe gate).
14. Error event logging.
15. Last-processed timestamp write (ops signal for `/status` / `/health`).

### 3.2 Logical pipeline (target)

```
Schedule Trigger
  → Gmail Get Many (bounded)
  → Split / Loop items
  → Lead-Mail-Parser
  → RAW Append (immutable)
  → Read CONFIG
  → Deterministic Process (AI OFF core)
  → IF ai_enabled
       → Prepare single OpenRouter JSON request
       → HTTP AI #1 (only AI call)
       → Validate AI JSON
       → IF invalid/timeout/forbidden → mark fallback; keep deterministic result
       → ELSE merge validated AI fields onto deterministic base
  → Dedupe Lookup (index / bounded query — not full sheet dump if avoidable)
  → Compose CLEAN record
  → CLEAN Append or Update
  → Format Telegram card
  → Send Telegram (manager chat)
  → LEAD_EVENTS append
  → Gmail labels (PROCESSED + remove incoming)  [success gate only]
  → Update last_processed_* ops keys / ERRORS on failure branch
```

### 3.3 Explicit removals vs Sales-Manager-v2

| Current | Decision |
|---------|----------|
| AI #2 Normalizer | **REMOVE** — one AI call max |
| Prepare AI normalizer request | **REMOVE** |
| Writing AI columns into RAW before AI | **REMOVE** |
| Showing raw enums in Telegram | **REPLACE** with UX contract |
| Broad duplicate match treating same `lead_id` as repeat | **REPLACE** with dedupe contract |

### 3.4 Success / error gates

- **Do not** send “success” Telegram before CLEAN write + formatter succeed (MetaBOT anti-pattern: success before final gate).
- **Telegram failure after CLEAN (approved):** do **not** add Gmail PROCESSED; add Gmail ERROR; **preserve** incoming lead label until a successful retry; record in ERRORS / diagnostics; same Gmail message on retry = `reprocessed` (not a new business repeat). After successful Telegram: add PROCESSED and remove incoming.
- On hard failure after RAW: write ERRORS + error Gmail label branch; **do not** remove incoming label until error path completes per label-safety rules.
- Client-facing channels: **none**. First reply text is Telegram/Sheets only.

---

## 4. WORKFLOW B — Admin.dev

### 4.1 Responsibilities (mandatory)

1. Telegram admin entry (webhook or Telegram Trigger).
2. Operator authorization (`admin_user_ids`).
3. Command normalization (`/cmd` lowercase, trim args).
4. CONFIG read/write for allowlisted keys.
5. Commands: `/help` `/status` `/ai_status` `/ai_on` `/ai_off` `/health` `/stats` `/test_lead` `/last_error` `/config`.
6. Explicit unknown-command response.
7. Health probes (non-destructive).
8. Synthetic test lead injection path (sandbox Sheets or flagged rows — never real client mail).
9. Audit log of admin writes (LEAD_EVENTS or ADMIN_AUDIT).

### 4.2 Pattern source

Reuse MetaBOT Admin **patterns**:

- command routing + allowlist;
- health without production side effects;
- Sheets-backed operational state;
- sandbox-first patches;
- evidence + REPORT discipline.

Do **not** import SEO locks, `/run`, content pipeline, or `seo_active_jobs`.

### 4.3 Logical pipeline (target)

```
Telegram Trigger
  → Normalize command
  → Auth gate (admin_user_ids)
  → Switch command
       → read-only handlers (help/status/ai_status/health/stats/last_error/config)
       → write handlers (ai_on/ai_off) + audit
       → /test_lead synthetic fixture runner (Operational-compatible payload → sandbox tabs OR Operational webhook only if later approved)
  → Reply Telegram
  → Unknown → fixed Russian string
```

**v1 preference for `/test_lead`:** Admin writes a **synthetic** payload into a sandbox RAW/CLEAN path or invokes a **documented** Operational test entry **only in .dev**. Do not process unread production Gmail from Admin.

---

## 5. Environment naming

| Suffix | Meaning |
|--------|---------|
| `.dev` | Persistent sandbox / development copy (max one Operational + one Admin) |
| production names (later) | Separate charter; target-only diff; never clone per hotfix |

`CONFIG.environment` ∈ {`dev`,`prod`} must match credential/sheet targets.

---

## 6. Credential and side-effect boundaries

| Resource | Operational | Admin |
|----------|-------------|-------|
| Gmail lead mailbox | Yes | No (except health “credential available” probe if safe) |
| Manager Telegram chat | Send cards | No (unless status mirrors) |
| Admin Telegram chat | Optional alerts | Primary |
| OpenRouter | Only if AI ON | Only if `/health` AI probe explicitly enabled **and** AI ON |
| Sheets RAW/CLEAN | Write | Read (+ synthetic test write in sandbox) |
| CONFIG | Read | Read/Write allowlisted keys |

---

## 7. Anti-proliferation rules

1. No third workflow for hotfixes — patch Operational.dev or Admin.dev.
2. No per-iteration clones.
3. Do not clone all three MetaBOT SEO workflows.
4. Disposable test graphs must be deleted or clearly labeled temporary after evidence (MetaBOT sandbox discipline).
5. Never copy `active: false` / disabled sandbox state into production accidentally.

---

## 8. SAFE UNKNOWN

- Exact live Sales-Manager-v2 node IDs and credentials.
- Whether one Telegram bot or two bots serve manager vs admin.
- Exact current spreadsheet IDs / workbook split (see LEAD-DATA-MODEL table strategy).
- Whether production schedule is already running despite export `active: false`.

---

*Related: LEAD-DATA-MODEL-v1 · CONFIGURATION-MODEL-v1 · ADMIN-COMMAND-CONTRACT-v1 · N8N-CHANGE-PLAN-v1.*
