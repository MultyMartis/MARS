# LEAD DATA MODEL v1

**Product:** i-SEO Sales Manager Bot  
**Status:** documented schema target — **Sheets not mutated in Phase 2**

> **Production supersession (2026-08-17):** Canonical live RAW/CLEAN + full-source contract is [baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md](../baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md). Durable `raw_text` is full visible source (snippet is not authoritative when a body exists). This Phase 2 file remains historical design context.

---

## 1. Table strategy (minimal disruption)

**Decision (operator-approved):** keep **separate** RAW and CLEAN workbooks. Do not consolidate workbooks in v1. Historical tabs stay; **new v2 tabs only in a later implementation phase** (not Phase 2).

| Workbook | Tabs |
|----------|------|
| **RAW** | `lead-base` — historical, **preserve**; `lead_raw_v2` — future implementation |
| **CLEAN** | `lead-base-processed` — historical, **preserve**; `lead_clean_v2`; `CONFIG`; `LEAD_EVENTS`; `ERRORS`; `DEDUP_INDEX` |

**Avoid:** new workbook per feature; uncontrolled tab proliferation; mutating historical tabs in place without charter.

### Tabs required for v1 (target layout)

| Tab | Workbook | Purpose | Writer |
|-----|----------|---------|--------|
| **lead_raw_v2** | RAW | Immutable intake evidence | Operational |
| **lead_clean_v2** | CLEAN | Current manager-facing lead state | Operational (+ limited Admin notes later) |
| **CONFIG** | CLEAN | Key/value runtime config | Admin write · Operational read |
| **LEAD_EVENTS** | CLEAN | Append-only processing/admin events | Both |
| **ERRORS** | CLEAN | Last/structured errors | Both |
| **DEDUP_INDEX** | CLEAN | Bounded contact/message lookup keys | Operational |

Optional later (not approved required tab): `STATS_DAILY` may be derived or added under a separate charter.

---

## 2. RAW — immutable intake evidence

**Rule:** RAW contains **parser output only**. Do **not** store AI-derived values in RAW. Do not pre-fill AI columns.

### Columns (exact)

#### Identity

| Column | Type | Notes |
|--------|------|-------|
| `lead_id` | string | Stable UUID/ulid generated at parse |
| `gmail_message_id` | string | Required for reprocess detection |
| `gmail_thread_id` | string | Optional but preferred |
| `received_at` | ISO-8601 | From Gmail internal date |

#### Source

| Column | Type | Notes |
|--------|------|-------|
| `source` | string | e.g. `gmail_form`, `gmail_forward` |
| `email_subject` | string | |
| `sender_email` | string | Envelope From |
| `request_page` | string | Landing/form page if parsed |
| `form_name` | string | |
| `utm_source` | string | |
| `utm_medium` | string | |
| `utm_campaign` | string | |
| `utm_term` | string | |
| `utm_content` | string | |

#### Parsed client

| Column | Type | Notes |
|--------|------|-------|
| `parsed_name` | string | Empty if unknown — **never** dump message tail |
| `parsed_phone` | string | Normalized digits+plus where possible |
| `parsed_email` | string | |
| `parsed_messenger` | string | telegram/@handle etc. |
| `parsed_site` | string | Domain/URL |

#### Request

| Column | Type | Notes |
|--------|------|-------|
| `request_text` | string | Bounded length (e.g. 8000) |
| `calc_detected` | boolean/string | `true`/`false` |
| `calc_data` | string/JSON | Calculator payload if any |
| `ip` | string | If present in mail |

#### Processing

| Column | Type | Notes |
|--------|------|-------|
| `parser_version` | string | e.g. `sm-parser-v3` |
| `parse_status` | enum | `ok` \| `partial` \| `failed` |
| `parse_warnings` | string | Semicolon-separated codes |
| `workflow_version` | string | Operational graph version label |
| `raw_logged_at` | ISO-8601 | Append time |

#### Raw evidence

| Column | Type | Notes |
|--------|------|-------|
| `raw_text` | string | Full body/snippet evidence (bounded); for forensics |

### RAW anti-patterns (forbidden)

- Writing `ai_summary`, `ai_reply`, etc. into RAW.
- Letting `parsed_name` / phone absorb remaining message body.
- Formula cells that produce `#ERROR!` in contact fields — store plain values only.
- Updating RAW rows after append (immutable). Reprocess = new event + CLEAN update keyed by `gmail_message_id`.

---

## 3. CLEAN — manager-facing current state

**Rule:** one logical row per `lead_id` (update in place on reprocess). Holds AI/deterministic enrichment, quality, reply draft, dedupe, and **simple** manager lifecycle — not a full CRM.

### Columns (exact)

#### Identity and timestamps

| Column | Type |
|--------|------|
| `lead_id` | string |
| `source_message_id` | string (= gmail_message_id) |
| `created_at` | ISO-8601 |
| `processed_at` | ISO-8601 |
| `updated_at` | ISO-8601 |

#### Client

| Column | Type | Notes |
|--------|------|-------|
| `client_name` | string | Display; may be empty |
| `primary_contact` | string | Best single contact for Telegram line |
| `contact_type` | enum | `phone` \| `email` \| `messenger` \| `mixed` \| `unknown` |
| `phone` | string | Empty if none — **never** invent `44` |
| `email` | string | |
| `messenger` | string | |
| `site` | string | |

#### Request / attribution

| Column | Type |
|--------|------|
| `service` | enum | `Audit` \| `SEO` \| `Direct` \| `Site` \| `Other` |
| `summary` | string |
| `source` | string |
| `request_page` | string |
| `utm_source` | string |
| `utm_medium` | string |
| `utm_campaign` | string |

#### Processing

| Column | Type | Notes |
|--------|------|-------|
| `processing_mode` | enum | `ai_off` \| `ai_on` \| `ai_fallback` |
| `ai_enabled` | boolean | Config at process time |
| `ai_status` | enum | `skipped` \| `ok` \| `fallback` \| `error` |
| `ai_model` | string | Empty if skipped |
| `fallback_used` | boolean | |
| `parser_version` | string | |
| `message_format_version` | string | Telegram card template version |
| `reply_template_version` | string | |

#### Quality

| Column | Type | Notes |
|--------|------|-------|
| `priority` | enum | `low` \| `normal` \| `high` |
| `quality_status` | enum | `ok` \| `needs_data` \| `poor` \| `unusable` |
| `quality_comment` | string | Human Russian short |
| `missing_fields` | string | e.g. `name;site;phone` |
| `clarification_questions` | string | Numbered or ` | ` separated |
| `manager_recommendation` | string | Next step for manager |

#### Reply

| Column | Type | Notes |
|--------|------|-------|
| `first_reply_text` | string | Copy-ready; **never auto-sent** |
| `first_reply_source` | enum | `template` \| `ai` \| `ai_fallback_template` |
| `reply_review_status` | enum | `draft` \| `copied` \| `sent_manual` \| `rejected` |
| `reply_sent_manually_at` | ISO-8601 \| empty | Manager-attested later |

#### Duplicate

| Column | Type | Notes |
|--------|------|-------|
| `duplicate_status` | enum | see §5 |
| `duplicate_match_type` | enum | see §5 |
| `duplicate_lead_id` | string | Previous business lead if any |
| `previous_contact_at` | ISO-8601 \| empty | Human-format in Telegram |
| `previous_service` | string | |
| `previous_summary` | string | |

#### Manager lifecycle

| Column | Type | Notes |
|--------|------|-------|
| `manager_status` | enum | see LEAD-LIFECYCLE-v1 |
| `assigned_to` | string | Display name / PER id optional |
| `first_contact_at` | ISO-8601 \| empty | |
| `next_followup_at` | ISO-8601 \| empty | **NOT REQUIRED FOR V1 automation** |
| `closed_at` | ISO-8601 \| empty | |
| `close_reason` | string | |
| `manager_notes` | string | Short |

#### Diagnostics

| Column | Type |
|--------|------|
| `processing_error` | string |
| `last_error_code` | string |

---

## 4. Supporting tabs (minimal columns)

### CONFIG

See [CONFIGURATION-MODEL-v1.md](CONFIGURATION-MODEL-v1.md).

### LEAD_EVENTS

| Column | Notes |
|--------|-------|
| `event_id` | |
| `ts` | |
| `lead_id` | nullable |
| `event_type` | `raw_logged` \| `processed` \| `ai_fallback` \| `telegram_sent` \| `admin_ai_on` \| … |
| `actor` | `operational` \| `admin:<telegram_id>` |
| `detail` | short |

### ERRORS

| Column | Notes |
|--------|-------|
| `ts` | |
| `error_code` | |
| `lead_id` | |
| `stage` | |
| `message` | no secrets |
| `workflow` | Operational/Admin |
| `resolved` | boolean |

### DEDUP_INDEX

| Column | Notes |
|--------|-------|
| `key_type` | `gmail_message_id` \| `phone` \| `email` \| `messenger` \| `site` |
| `key_value` | normalized |
| `lead_id` | |
| `last_seen_at` | |
| `is_primary_contact_key` | boolean |

**Purpose:** avoid full CLEAN sheet reads on every lead. Lookup by exact key rows.

### STATS_DAILY (optional — not in approved required layout)

May be derived later under a separate charter. Not required for v1 tabs.

---

## 5. Dedupe contract (embedded)

### 5.1 Match classes

| Case | Rule | `duplicate_status` | `duplicate_match_type` |
|------|------|--------------------|------------------------|
| Same `gmail_message_id` | Reprocessing — **not** a new business lead | `reprocessed` | `same_message` |
| Same phone **or** email **or** messenger (normalized) within window | Probable repeat client | `repeat` | `phone` / `email` / `messenger` |
| Same site only | Weak — **do not** auto exact-repeat | `possible` | `site_only` |
| ≥2 strong contact keys match same prior lead | Exact repeat | `repeat` | `multi_evidence` |
| No match | New | `new` | `none` |

### 5.2 Enums

- `duplicate_status`: `new` \| `reprocessed` \| `repeat` \| `possible`
- `duplicate_match_type`: `none` \| `same_message` \| `phone` \| `email` \| `messenger` \| `site_only` \| `multi_evidence`

### 5.3 Previous lead selection

1. Prefer strongest match type (`multi_evidence` > contact key > site).
2. Among ties: most recent `processed_at` excluding current `lead_id`.
3. Default window: **365 days** for contact keys (CONFIG override later). Site-only: informational only.

### 5.4 Reprocess handling

- Same message id: update CLEAN row for existing `lead_id` (or map message→lead); Telegram labels **«Повторная обработка»** not «Повторный клиент».
- Do **not** append duplicate CLEAN rows for same message.

### 5.5 Telegram history

- Human date (`дд.мм.гггг чч:мм`), previous service, one-line previous summary.
- No raw ISO in manager card.
- Site-only `possible`: soft wording («Возможное совпадение по сайту»).

### 5.6 Lookup performance

- Maintain `DEDUP_INDEX` on successful process.
- Query by key — **forbid** default full-sheet read each lead (MetaBOT Sheets quota lesson).

---

## 6. Migration notes (sandbox first)

1. Create `lead_raw_v2` / `lead_clean_v2` in sandbox workbook.
2. Dual-write optional only under explicit charter.
3. Do not rewrite historical RAW AI-empty columns in place without backup.
4. Parser must fix overflow (`parsed_name`/`phone` absorbing body) before CLEAN trust.

---

## 7. SAFE UNKNOWN

- Exact production spreadsheet IDs and whether RAW/CLEAN are one workbook or two.
- Historical row counts and which parser versions polluted columns.
- Whether `#ERROR!` is formula-driven in Sheets UI vs written literal.

---

*Related: LEAD-LIFECYCLE-v1 · AI-OFF-ON-CONTRACT-v1 · TELEGRAM-UX-CONTRACT-v1.*
