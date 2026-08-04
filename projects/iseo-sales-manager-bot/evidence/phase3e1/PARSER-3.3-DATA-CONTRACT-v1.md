# PARSER 3.3 DATA CONTRACT v1

Sanitized field contract for Parse → Process → Format (Phase 3E.1).

## Versions

- `parser_version` = `sm-parser-v3.3`
- `semantic_model_version` = `lead-semantic-v1`
- `message_format_version` = `sm-msg-v2.3`
- `ai_enabled` = `false` → `processing_mode=ai_off`, `ai_status=skipped`

## Core outputs (no PII examples)

| Field | Notes |
|-------|-------|
| `lead_id` | stable synthetic / ulid-style |
| `gmail_message_id` | reprocess key |
| `client_name` / `parsed_name` | never message tail |
| `phone` / `email` / `messenger` | validated; placeholders → invalid |
| `site` + `website_state` | five-state model |
| `comment_normalized` | bounded; no IP/page bleed |
| `source_page` | separated from comment |
| `resolved_intent` / `selected_service` | taxonomy: Audit, SEO, WebsiteDevelopment, WebsiteDevelopmentSEO, AISearch, Other |
| `intent_conflict` | boolean + short reason |
| `quality_status` | sufficient / needs_clarification / bad (compat aliases ok/needs_data) |
| `first_reply_text` | consistency-checked |
| `missing_fields` | service-aware |

Authority docs: `architecture/PARSER-3.3-CONTRACT-v1.md`, `architecture/LEAD-SEMANTIC-MODEL-v1.md`.
