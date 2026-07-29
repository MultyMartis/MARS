# CONFIGURATION MODEL v1

**Product:** i-SEO Sales Manager Bot  
**Storage:** Google Sheets tab `CONFIG` (auditable)  
**Status:** documented — Sheets not mutated in Phase 2

---

## 1. Why Sheets CONFIG

MetaBOT production pattern: operational state in Google Sheets, human-auditable, Admin-writable, Worker/Operational-readable. No stronger proven in-repo pattern exists for this product line without inventing a new config service (**out of scope**).

---

## 2. Schema

| Column | Type | Notes |
|--------|------|-------|
| `key` | string | Unique |
| `value` | string | Serialized per `type` |
| `type` | enum | `boolean` \| `string` \| `number` \| `string_list` \| `json` |
| `updated_at` | ISO-8601 | |
| `updated_by` | string | `admin:<telegram_id>` or `system` |
| `description` | string | Human |

---

## 3. Minimum keys

| key | type | Default | Description |
|-----|------|---------|-------------|
| `ai_enabled` | boolean | **`false`** | Master AI gate |
| `ai_model` | string | operator-chosen model id | Used only when AI ON |
| `environment` | string | `dev` | `dev` \| `prod` |
| `telegram_manager_chat_id` | string | *(required)* | Manager card destination |
| `telegram_admin_chat_id` | string | *(required)* | Admin replies / alerts |
| `admin_user_ids` | string_list | *(required)* | Telegram user IDs allowed for Admin |
| `message_format_version` | string | `sm-msg-v1` | Telegram card formatter |
| `reply_template_version` | string | `sm-reply-v1` | Deterministic templates |
| `parser_version` | string | `sm-parser-v3` | Expected parser stamp |
| `health_ai_probe_enabled` | boolean | **`false`** | Allow AI ping in `/health` |
| `stats_days_default` | number | `7` | `/stats` window |
| `dedupe_contact_window_days` | number | `365` | Contact match window |
| `gmail_query_limit` | number | `10` | Bounded intake |
| `last_processed_at` | string | empty | Ops signal (Operational write) |
| `last_processed_lead_id` | string | empty | Ops signal |
| `last_success_at` | string | empty | Ops signal |
| `last_error_at` | string | empty | Ops signal |
| `last_error_code` | string | empty | Ops signal |

Optional later (not blocking v1): `openrouter_timeout_ms`, `raw_tab_name`, `clean_tab_name`.

---

## 4. Read failure behavior

If CONFIG cannot be read:

| Setting | Behavior |
|---------|----------|
| `ai_enabled` | **Treat as OFF** — no OpenRouter call |
| Chat IDs | Fail processing after RAW if manager chat unknown — log ERRORS; do not invent destinations |
| `admin_user_ids` | Admin denies all write commands; may reply “config unavailable” |
| Versions | Use hard-coded safe defaults in Code node (`sm-msg-v1`, `sm-reply-v1`) |
| Environment | Assume `dev` for safety (prefer no prod side effects) |

**Principle:** fail closed on AI and external fan-out; keep deterministic path able to run when chat IDs known via n8n static fallback **only if operator explicitly documents static fallback IDs in .dev** (prefer CONFIG).

---

## 5. Write rules

- Only Admin.dev allowlisted commands mutate CONFIG.
- Every write updates `updated_at` + `updated_by`.
- Append `LEAD_EVENTS` / audit row for `ai_on` / `ai_off` and other writes.
- Operational may update **ops signal keys only** (`last_processed_*`, `last_success_at`, `last_error_*`) — not `ai_enabled`.

---

## 6. Caching

- Operational: read CONFIG **once per schedule tick** (or once per batch), not per node spam.
- Admin `/health`: single CONFIG read.
- Avoid MetaBOT-style quota storms from repeated full-sheet health reads.

---

## 7. Secrets

- **Never** store OpenRouter API keys, Gmail OAuth, or Telegram bot tokens in CONFIG.
- Credentials remain in n8n credential store only.
- Docs and Sheets must not contain key material.

---

*Related: ADMIN-COMMAND-CONTRACT-v1 · HEALTHCHECK-CONTRACT-v1 · AI-OFF-ON-CONTRACT-v1.*
