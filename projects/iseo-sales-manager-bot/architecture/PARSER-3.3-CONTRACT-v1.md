# PARSER 3.3 CONTRACT v1

**Product:** i-SEO Sales Manager Bot  
**Parser version stamp:** `sm-parser-v3.3`  
**Semantic model:** `lead-semantic-v1`  
**Message format (paired):** `sm-msg-v2.3`  
**Status:** **IMPLEMENTED** Phase 3E.1 (Operational.dev Parse Lead + local harness)  
**Libs (git):** `implementation/parser-fixtures/parse-lead-lib.mjs` · `implementation/runtime-libs/processor-lib.mjs` · `implementation/runtime-libs/formatter-lib.mjs`

---

## Scope

Deterministic extraction from website-form / Gmail lead payloads:

1. HTML → plain text → labeled fields;
2. text / one-line fallback when HTML absent;
3. website state classification;
4. comment boundary isolation from form/footer/IP/page labels;
5. intent resolution with precedence;
6. quality assessment + first-reply draft (AI OFF);
7. compat fields for Parser 3.2 CLEAN / Telegram / archive.

**Out of scope:** OpenRouter / AI ON; new workflows; ACCESS_CONTROL changes; reminder system.

---

## Input surface (sanitized)

| Input | Notes |
|-------|--------|
| `html` / `textHtml` / body | preferred for labeled forms |
| `request_text` / `snippet` / `text` | fallback |
| Gmail metadata | subject, message id — no PII in committed fixtures |
| `config.ai_enabled` | must be `false` in current baseline |

Synthetic fixtures only in harness (`example.com` / `example.ru` / reserved phones).

---

## Output contract (Parse)

Must emit at least:

- identity: `client_name` / `parsed_name`, contacts, `is_probable_test`
- site: `site` / `site_value`, `website_state`, evidence source
- comment: `comment_normalized` (без page/IP/footer bleed)
- origin: `source_page`, form/title signals
- intent: `resolved_intent`, `selected_service`, conflict flags
- quality seeds: missing/invalid lists
- trace: `parser_version=sm-parser-v3.3`, `semantic_model_version`, `lead_id`, `gmail_message_id`

Process (deterministic) adds `processing_mode=ai_off`, `ai_status=skipped`, quality finalization, `first_reply_text`.  
Format stamps `message_format_version=sm-msg-v2.3` and actionable buttons (`✅ Обработано` / `🚫 Спам`).

---

## Invariants

| # | Rule |
|---|------|
| 1 | AI OFF → zero provider calls |
| 2 | Client auto-messages = 0 |
| 3 | No new workflow IDs |
| 4 | Callback contract unchanged (`sm:p:` / `sm:s:`) |
| 5 | Multi-recipient / claim-before-send unchanged |
| 6 | Messenger/handle never rendered as website |
| 7 | Explicit no-site ≠ missing; reply must not ask for «existing site» when absent for site-build intents |
| 8 | Label-like words inside comment do not end the comment without a real label pattern |
| 9 | Repeatable: same synthetic input → same semantic JSON |

---

## Acceptance

- Local harness: `node implementation/harness/phase3e1-harness.mjs` → **46/46 PASS** (see `evidence/phase3e1/`).
- Live semantic acceptance: see `LIVE-SEMANTIC-ACCEPTANCE-v1.md` (may be PENDING).
- Research backlog under `research/parser-3.3/` marked implemented / linked here.
