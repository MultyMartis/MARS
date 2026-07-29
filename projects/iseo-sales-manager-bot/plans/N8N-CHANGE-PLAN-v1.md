# N8N CHANGE PLAN v1

**Product:** i-SEO Sales Manager Bot  
**Status:** node-level plan — **no JSON patch in Phase 2** · **no live n8n access**  
**Baseline:** Sales-Manager-v2 logical graph (operator-known)  
**Grammar:** MetaBOT Programmer n8n JSON grammar / safe patch protocol (apply in later phases)

---

## 1. Target copies (later live max)

| Copy | Purpose |
|------|---------|
| `i-SEO Sales Manager - Operational.dev` | Persistent sandbox ops graph |
| `i-SEO Sales Manager - Admin.dev` | Persistent sandbox admin graph |

Do not create a third product workflow. Do not clone MetaBOT Intake+Worker+Admin trio.

---

## 2. Operational.dev — node decisions

### 2.1 Retain (adapt)

| Logical node | Change |
|--------------|--------|
| Schedule Trigger | Keep; confirm interval; document |
| Gmail Get many | Keep; **bound** query (label + limit + newer_than) |
| Lead-Mail-Parser | **Rewrite** field extraction; stamp `parser_version`; stop overflow into name/phone |
| RAW Google Sheets append | Keep pattern; **new column map** (`lead_raw_v2`) |
| Find Duplicate Lead | **Replace logic** per dedupe contract; use DEDUP_INDEX |
| Mark Duplicate Status | Adapt enums |
| IF Bad Quality | Retune thresholds to quality contract (do not drop Telegram on needs_data) |
| CLEAN Google Sheets append | Prefer **append or update**; new column map |
| Telegram message | **Replace** formatter per UX contract |
| Gmail Add PROCESSED | Keep **after** success gate |
| Gmail Remove incoming label | Keep **after** success gate |
| Error label branch | Keep; ensure incoming removal rules documented |
| Error remove incoming | Keep only when error handling complete |

### 2.2 Remove

| Logical node | Reason |
|--------------|--------|
| Prepare AI normalizer request | Dual-AI eliminated |
| AI Normalizer AI #2 | Dual-AI eliminated |
| Any RAW write of AI fields pre-AI | Model violation |

### 2.3 Change heavily

| Logical node | Change |
|--------------|--------|
| Prepare OpenRouter request | Single structured schema; include deterministic context |
| HTTP Request AI #1 | Only call behind AI gate; timeouts; no key in node text docs |
| Normalize AI result | Become **deterministic validator** (not second LLM) |
| Normalize Clean Lead | Merge deterministic + validated AI |

### 2.4 Add

| Logical node / stage | Purpose |
|----------------------|---------|
| Read CONFIG | Once per batch |
| AI mode IF | Skip HTTP entirely when OFF |
| Deterministic Process Code | Service/quality/summary/reply templates |
| Fallback marker | On AI failure |
| DEDUP_INDEX lookup/upsert | Bounded dedupe |
| LEAD_EVENTS append | Processing audit |
| ERRORS append | Diagnostics |
| Update CONFIG ops keys | last_processed_*, last_success_* |
| Telegram HTML/plain escape helper | Parse safety |
| Final success gate IF | Labels + Telegram only if CLEAN ok |

### 2.5 Connections changed

- Insert CONFIG + deterministic path **before** AI.
- AI #1 → Validator → merge (remove AI #2 chain).
- Dedupe after merge, before CLEAN.
- Telegram after CLEAN.
- Gmail labels **only after successful Telegram delivery** (approved operator policy):
  - CLEAN committed → Telegram send → on Telegram **success**: add PROCESSED + remove incoming lead label;
  - if CLEAN written but Telegram **fails**: do **not** add PROCESSED; add ERROR label; **preserve** incoming lead label until successful retry; record failure in ERRORS / diagnostics; same `gmail_message_id` on retry = `reprocessed` (not a new business repeat).

### 2.6 Field / Sheets changes

- RAW: immutable parser columns only.
- CLEAN: full v1 column set including `first_reply_text`, AI stamps, dedupe, lifecycle.
- Stop writing `#ERROR!` formula contacts — plain values.

### 2.7 AI #2 removal decision

**REMOVE AI #2.** Validation is Code/deterministic. One provider call max when AI ON.

### 2.8 Gmail label safety (approved)

1. Never remove incoming before RAW append succeeds.
2. PROCESSED **only after** CLEAN write **and** Telegram delivery both succeed.
3. Telegram failure after CLEAN: ERROR label; keep incoming; no PROCESSED; ERRORS row; retry → `reprocessed`.
4. Hard process failure (no safe CLEAN / no Telegram): ERROR label path; preserve incoming until error handling complete and operator policy allows removal.
5. Reprocess same message id: dedupe `reprocessed` — not «повторный клиент»; avoid Telegram alert storm if unchanged (optional suppress — Phase 3 implementation detail).

### 2.9 Runtime pitfalls to avoid (MetaBOT)

- No `structuredClone` in Code nodes.
- No downstream refs to skipped AI branch items — always pass deterministic item forward.
- No Markdown Telegram entities by default.
- No success message before final gate.
- No unvalidated AI text.
- No full-sheet reads for dedupe/stats.

---

## 3. Admin.dev — build plan

### 3.1 Source pattern

MetaBOT Admin workflow **patterns** (command switch, auth, health, Sheets), not a copy of SEO locks/content commands.

### 3.2 Nodes (logical)

| Node | Role |
|------|------|
| Telegram Trigger | Entry |
| Normalize command | `/cmd` parse |
| Auth IF | `admin_user_ids` |
| Switch | Ten commands + unknown |
| Sheets Read CONFIG | Shared |
| Sheets Update CONFIG | ai_on/off |
| Health Code / probes | Non-destructive |
| Stats reader | STATS_DAILY / bounded |
| Synthetic test writer | Sandbox fixtures |
| ERRORS read | `/last_error` |
| Telegram reply | Always |
| Unknown reply | Fixed Russian string |
| Audit event append | Writes |

### 3.3 Commands

Implement matrix in ADMIN-COMMAND-CONTRACT-v1.

### 3.4 Authorization

Allowlist only; deny message; no silent pass.

### 3.5 Config updates

Only allowlisted keys via commands.

### 3.6 Health probes

HEALTHCHECK-CONTRACT-v1.

### 3.7 Synthetic test

Fixture library from SANDBOX-TEST-PLAN-v1; never production unread Gmail.

---

## 4. Patch protocol (later phases)

Follow MetaBOT `safe-workflow-patch-protocol-v1`:

evidence → proposal → sandbox clone → tests → approval → target-only prod diff → rollback backup → REPORT.

Phase 2 stops at documentation.

---

## 5. SAFE UNKNOWN (block live patch until known)

- Live node IDs / credential names for Sales-Manager-v2.
- Whether export `active:false` matches runtime.
- Exact spreadsheet IDs.
- One bot vs two bots for manager/admin.

---

*Related: SANDBOX-TEST-PLAN-v1 · ROLLBACK-PLAN-v1 · TWO-WORKFLOW-ARCHITECTURE-v1.*
