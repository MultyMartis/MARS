# SHEETS MIGRATION SPEC v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A — specification only  
**Decision:** RAW and CLEAN remain **separate** workbooks  
**Phase 3A / 3A.1 action:** **do not** create tabs or modify Sheets  
**Historical evidence (Phase 3A.1):** RAW sheet `lead-base` (20 headers, 19 rows); CLEAN sheet `lead-base-processed` (14 headers, 19 rows) — see baselines schema docs.

---

## 1. Workbook layout

| Workbook | Historical (preserve) | Future v1 tabs |
|----------|----------------------|----------------|
| **RAW** `<RAW_WORKBOOK_ID>` | `lead-base` untouched | `lead_raw_v2` |
| **CLEAN** `<CLEAN_WORKBOOK_ID>` | `lead-base-processed` untouched | `lead_clean_v2`, `CONFIG`, `LEAD_EVENTS`, `ERRORS`, `DEDUP_INDEX` |

No bulk migration of historical rows into v2 for v1. Historical = evidence only. Do not mix malformed old contacts into DEDUP_INDEX without normalization charter.

---

## 2. Tab: `lead_raw_v2` (RAW)

**Writer:** Operational · **Reader:** Admin health / forensics · **Behavior:** append-only · **Retention:** forensic intake

| # | Header | Type | Required | Default | Notes |
|---|--------|------|----------|---------|-------|
| 1 | `lead_id` | string | yes | generated | UUID/ulid |
| 2 | `gmail_message_id` | string | yes | — | reprocess key |
| 3 | `gmail_thread_id` | string | no | empty | |
| 4 | `received_at` | ISO-8601 | yes | — | |
| 5 | `source` | string | no | empty | |
| 6 | `email_subject` | string | no | empty | |
| 7 | `sender_email` | string | no | empty | |
| 8 | `request_page` | string | no | empty | |
| 9 | `form_name` | string | no | empty | |
| 10 | `utm_source` | string | no | empty | |
| 11 | `utm_medium` | string | no | empty | |
| 12 | `utm_campaign` | string | no | empty | |
| 13 | `utm_term` | string | no | empty | |
| 14 | `utm_content` | string | no | empty | |
| 15 | `parsed_name` | string | no | empty | never message tail |
| 16 | `parsed_phone` | string | no | empty | plain value |
| 17 | `parsed_email` | string | no | empty | |
| 18 | `parsed_messenger` | string | no | empty | |
| 19 | `parsed_site` | string | no | empty | |
| 20 | `request_text` | string | no | empty | bounded |
| 21 | `calc_detected` | string | no | `false` | |
| 22 | `calc_data` | string | no | empty | |
| 23 | `ip` | string | no | empty | |
| 24 | `parser_version` | string | yes | `sm-parser-v3` | |
| 25 | `parse_status` | enum | yes | — | ok\|partial\|failed |
| 26 | `parse_warnings` | string | no | empty | |
| 27 | `workflow_version` | string | yes | — | |
| 28 | `raw_logged_at` | ISO-8601 | yes | now | |
| 29 | `raw_text` | string | no | empty | bounded evidence |

**Migration:** create empty tab with header row only. No AI columns.

---

## 3. Tab: `lead_clean_v2` (CLEAN)

**Writer:** Operational (primary) · **Reader:** Admin · **Behavior:** upsert by `lead_id` / `source_message_id` · **Retention:** current manager state

Ordered headers (exact, v1 — 52 columns):

`lead_id`, `source_message_id`, `created_at`, `processed_at`, `updated_at`, `client_name`, `primary_contact`, `contact_type`, `phone`, `email`, `messenger`, `site`, `service`, `summary`, `source`, `request_page`, `utm_source`, `utm_medium`, `utm_campaign`, `processing_mode`, `ai_enabled`, `ai_status`, `ai_model`, `fallback_used`, `parser_version`, `message_format_version`, `reply_template_version`, `priority`, `quality_status`, `quality_comment`, `missing_fields`, `clarification_questions`, `manager_recommendation`, `first_reply_text`, `first_reply_source`, `reply_review_status`, `reply_sent_manually_at`, `duplicate_status`, `duplicate_match_type`, `duplicate_lead_id`, `previous_contact_at`, `previous_service`, `previous_summary`, `manager_status`, `assigned_to`, `first_contact_at`, `next_followup_at`, `closed_at`, `close_reason`, `manager_notes`, `processing_error`, `last_error_code`

| Field group | Defaults on first write |
|-------------|-------------------------|
| `manager_status` | `new` |
| `reply_review_status` | `draft` |
| `ai_enabled` | from CONFIG at process time |
| `message_format_version` | `sm-msg-v2` (Phase 3D.3; was `sm-msg-v1`) |
| lifecycle optional dates | empty |

**Migration:** header-only; no import of malformed historical processed rows into dedupe.

### 3.1 Phase 3D.3 — lifecycle columns (v2 — 65 columns)

CLEAN extended `+13` headers (52→65) to support inline manager lead actions and callback-driven lifecycle. Appended (order after `last_error_code`):

`lifecycle_status`, `manager_action_token`, `manager_action_user_id`, `manager_action_processed_at`, `manager_action_spam_at`, `manager_action_last_event_id`, `telegram_chat_id`, `telegram_message_id`, `telegram_card_sent_at`, `telegram_card_edited_at`, `card_keyboard_state`, `lead_visual_indicator`, `lead_lifecycle_indicator`

| Header | Type | Required | Default | Notes |
|--------|------|----------|---------|-------|
| `lifecycle_status` | enum | yes | `pending` | `pending`\|`processed`\|`spam` |
| `manager_action_token` | string | yes | generated | opaque 12-char callback token; no PII |
| `manager_action_user_id` | string | no | empty | Telegram id of acting manager/admin |
| `manager_action_processed_at` | ISO-8601 | no | empty | set on `pending→processed` |
| `manager_action_spam_at` | ISO-8601 | no | empty | set on `pending→spam` |
| `manager_action_last_event_id` | string | no | empty | last `LEAD_EVENTS` row id for this lead |
| `telegram_chat_id` | string | no | empty | destination chat for the delivered card (manager chat) |
| `telegram_message_id` | string | no | empty | needed to edit the card on lifecycle change |
| `telegram_card_sent_at` | ISO-8601 | no | empty | |
| `telegram_card_edited_at` | ISO-8601 | no | empty | set after successful keyboard-clear edit |
| `card_keyboard_state` | enum | no | `attached` | `attached`\|`cleared`\|`none` (archive/service cards) |
| `lead_visual_indicator` | string | no | empty | last-rendered lead-type emoji class (audit trail only) |
| `lead_lifecycle_indicator` | string | no | empty | last-rendered lifecycle emoji class |

Existing `processed_at` is unchanged and remains **bot processing time** (Operational finalize); `manager_action_processed_at` / `closed_at` are the distinct **manager** lifecycle stamps. No RAW/CLEAN row deletion on `spam` — lifecycle is a status column change plus an append-only `LEAD_EVENTS` record, never a delete.

---

## 4. Tab: `CONFIG` (CLEAN)

| Header | Type | Required |
|--------|------|----------|
| `key` | string | yes |
| `value` | string | yes |
| `type` | enum | yes |
| `updated_at` | ISO-8601 | yes |
| `updated_by` | string | yes |
| `description` | string | no |

### Initial rows (safe defaults)

| key | value | type | description |
|-----|-------|------|-------------|
| `ai_enabled` | `false` | boolean | Master AI gate — **OFF** |
| `ai_model` | *(operator model id later)* | string | Used only when AI ON |
| `environment` | `dev` | string | dev\|prod |
| `telegram_manager_chat_id` | `<MANAGER_CHAT_ID>` | string | Manager cards |
| `telegram_admin_chat_id` | `<ADMIN_CHAT_ID>` | string | Admin replies |
| `admin_user_ids` | *(operator list)* | string_list | Allowlist |
| `manager_action_user_ids` | *(seeded from `admin_user_ids`; Phase 3D.3)* | string_list | Inline lead-action callback allowlist — falls back to admin list until Olya (or another manager) is explicitly enrolled |
| `message_format_version` | `sm-msg-v2` (Phase 3D.3; was `sm-msg-v1`) | string | Card formatter |
| `reply_template_version` | `sm-reply-v1` | string | Templates |
| `parser_version` | `sm-parser-v3` | string | Parser stamp |
| `health_ai_probe_enabled` | `false` | boolean | /health AI ping |
| `stats_days_default` | `7` | number | /stats window |
| `dedupe_contact_window_days` | `365` | number | Contact window |
| `gmail_query_limit` | `10` | number | Bounded intake |
| `last_processed_at` | empty | string | Ops signal |
| `last_processed_lead_id` | empty | string | Ops signal |
| `last_success_at` | empty | string | Ops signal |
| `last_error_at` | empty | string | Ops signal |
| `last_error_code` | empty | string | Ops signal |

**Writer:** Admin (allowlisted) + Operational ops keys only · **Reader:** both.

**Never store secrets in CONFIG.**

---

## 5. Tab: `LEAD_EVENTS` (CLEAN)

| Header | Type | Required | Default |
|--------|------|----------|---------|
| `event_id` | string | yes | generated |
| `ts` | ISO-8601 | yes | now |
| `lead_id` | string | no | empty |
| `event_type` | string | yes | — |
| `actor` | string | yes | `operational` / `admin:<id>` |
| `detail` | string | no | empty |

**Behavior:** append-only · **Writers:** Operational + Admin.

---

## 6. Tab: `ERRORS` (CLEAN)

| Header | Type | Required | Default |
|--------|------|----------|---------|
| `ts` | ISO-8601 | yes | now |
| `error_code` | string | yes | — |
| `lead_id` | string | no | empty |
| `stage` | string | yes | — |
| `message` | string | yes | no secrets |
| `workflow` | string | yes | Operational/Admin |
| `resolved` | boolean | yes | `false` |

**Behavior:** append (+ optional later resolve) · **Writers:** both.

---

## 7. Tab: `DEDUP_INDEX` (CLEAN)

See [DEDUP-IMPLEMENTATION-SPEC-v1.md](DEDUP-IMPLEMENTATION-SPEC-v1.md) for full rules.

| Header | Type | Required | Default |
|--------|------|----------|---------|
| `dedup_key` | string | yes | `key_type:normalized_value` |
| `key_type` | enum | yes | — |
| `lead_id` | string | yes | — |
| `gmail_message_id` | string | no | empty |
| `normalized_value` | string | yes | — |
| `created_at` | ISO-8601 | yes | now |
| `last_seen_at` | ISO-8601 | yes | now |
| `active` | boolean | yes | `true` |

**Lookup key:** `dedup_key` exact · **Writer:** Operational · **Reader:** Operational (+ Admin diagnostics).

---

## 8. Indexes / lookup keys

| Tab | Lookup |
|-----|--------|
| RAW | `gmail_message_id` (forensics) |
| CLEAN | `lead_id`, `source_message_id` |
| CONFIG | `key` |
| DEDUP_INDEX | `dedup_key` |
| ERRORS | latest by `ts` |
| LEAD_EVENTS | by `lead_id` / `ts` |

---

## 9. Migration treatment summary

| Object | Treatment |
|--------|-----------|
| Historical tabs | preserve unchanged |
| Bulk row copy to v2 | **not required** for v1 |
| Dual-write historical+v2 | only under later charter |
| Dedupe from old malformed | **forbidden** without normalize |
| Sandbox first | create tabs in sandbox / `environment=dev` book after Phase 3B approval |

---

## 10. SAFE UNKNOWN

Exact production workbook IDs; whether filenames match `MetaBOT -Leads*.xlsx`; historical `#ERROR!` prevalence.

---

*Related: LEAD-DATA-MODEL-v1 · CONFIGURATION-MODEL-v1 · DEDUP-IMPLEMENTATION-SPEC-v1.*

## Phase 3D.3 note

`lead_clean_v2` header count moved **52→65** (see §3.1) to carry manager lifecycle/callback state directly on the CLEAN row (no separate lifecycle tab). `CONFIG` gained `manager_action_user_ids` (seeded from `admin_user_ids`) and `message_format_version` moved to `sm-msg-v2`. `LEAD_EVENTS` gains no new columns — callback outcomes (`applied`/`idempotent`/`conflict`/`unauthorized`) are recorded via existing `event_type`/`actor`/`detail` fields. No new tab created; no historical row migration; sandbox/synthetic rows (`SYNTHETIC_TEST`) unaffected.

## Phase 3D.3.1 note — phone text storage

Operational.dev **Append or Update CLEAN v2** and **Append RAW v2** set Google Sheets node `options.cellFormat=RAW` (`valueInputOption=RAW`) so plus-prefixed phones are stored as text, not evaluated as formulas. Historical `#ERROR!` cells are **not** bulk-rewritten; Telegram rendering suppresses them. `LEAD_EVENTS` may record a single `lead_card_recovered` per `/leads` command (metadata only; no PII).


---

## Phase 3D.5 note

See `evidence/phase3d5/` for ACCESS_CONTROL / ACCESS_EVENTS, public auth routing, moderator registry Admin commands, and harness coverage (30+ checks). ACCESS_CONTROL is access SoT; do not edit workflow code to enroll moderators.
