# FIRST REPLY ENGINE v2

**Product:** i-SEO Sales Manager Bot  
**Version:** `sm-reply-v2.1` (Human Reply Style **`sm-human-v1.0`** layered in Phase 3E.2.1)  
**Status:** IMPLEMENTED and operator-accepted; Phase 3E.2.3 changes delivery call-budget only, with no reply redesign
**Runtime lib:** `implementation/runtime-libs/first-reply-engine-v2.mjs`  
**AI:** OFF — deterministic templates only  
**Delivery:** manager draft for manual copy — never auto-sent to customer

## Purpose

Produce a concise, natural, service-aware first reply from Lead Semantic Model v1 fields, without asking for information already known.

## Inputs (authoritative)

- `client_name_normalized`
- `contact_method_normalized` / phone / email / messenger
- `website_state`, `website_normalized`
- `alternative_contact_type`, `alternative_contact_value`
- `comment_normalized`, `explicit_client_intent`
- `resolved_service`, `secondary_service`
- `request_summary`, `lead_quality`, `missing_information`
- `is_probable_test`, `source_topic`

## Outputs

| Field | Meaning |
|-------|---------|
| `first_reply_version` | `sm-reply-v2.1` |
| `human_reply_style_version` | `sm-human-v1.0` |
| `meaningful_theme` | theme code — see [MEANINGFUL-COMMENT-BRANCHING-v1.md](MEANINGFUL-COMMENT-BRANCHING-v1.md) |
| `quality_linter_ok` | boolean — see [FIRST-REPLY-QUALITY-LINTER-v1.md](FIRST-REPLY-QUALITY-LINTER-v1.md) |
| `quality_linter_failures` | linter failure codes when blocked |
| `first_reply_mode` | `normal` / `test_suppressed` / `contact_suppressed` |
| `first_reply_subject` | short topic label |
| `first_reply_text` | copy-ready draft |
| `first_reply_questions` | asked question groups |
| `first_reply_reason_codes` | suppressed-question codes |
| `first_reply_omitted_reason` | why draft omitted |
| `first_reply_ready` | boolean |
| `first_reply_warnings` | length / promise scrub notes |
| `first_reply_source` | compat: `template` / `test_omitted` / `none` |
| `reply_template_version` | same as version |

## Global invariants

1. Natural greeting (`Здравствуйте, <Имя>!` or `Здравствуйте!`)
2. Acknowledge real request
3. No work-started / pricing / ranking guarantees
4. ≤3 compact question groups
5. Never re-ask known data
6. Closing: `С уважением,` / `команда i-SEO`
7. Card disclaimer outside copy block: `Ответ клиенту автоматически не отправляется.`

## Suppression

- `is_probable_test` → `test_suppressed`, no customer draft
- Missing/damaged critical contact → `contact_suppressed`, manager warning

## v2.1 / Human Reply Style (Phase 3E.2.1)

v2.1 keeps v2.0 invariants but adds:

- **Human Reply Style v1** — natural Оля voice; no system narration ([HUMAN-REPLY-STYLE-v1.md](HUMAN-REPLY-STYLE-v1.md))
- **Meaningful comment branching** — deterministic theme codes change ack/questions ([MEANINGFUL-COMMENT-BRANCHING-v1.md](MEANINGFUL-COMMENT-BRANCHING-v1.md))
- **Quality linter** — fail → `first_reply_ready=false` ([FIRST-REPLY-QUALITY-LINTER-v1.md](FIRST-REPLY-QUALITY-LINTER-v1.md))
- **Silent known-info guard** — suppress questions without telling the customer ([KNOWN-INFORMATION-GUARD-v1.md](KNOWN-INFORMATION-GUARD-v1.md))

Harness: `evidence/phase3e2-1/` — 64/64 PASS (includes reply + delivery fail-closed models).

## Related

- [HUMAN-REPLY-STYLE-v1.md](HUMAN-REPLY-STYLE-v1.md)
- [MEANINGFUL-COMMENT-BRANCHING-v1.md](MEANINGFUL-COMMENT-BRANCHING-v1.md)
- [FIRST-REPLY-QUALITY-LINTER-v1.md](FIRST-REPLY-QUALITY-LINTER-v1.md)
- [KNOWN-INFORMATION-GUARD-v1.md](KNOWN-INFORMATION-GUARD-v1.md)
- [MANAGER-CARD-v2.4-CONTRACT-v1.md](MANAGER-CARD-v2.4-CONTRACT-v1.md)
- [FIRST-REPLY-RULES-v1.md](FIRST-REPLY-RULES-v1.md) (extended by this engine)

## Phase 3E.2.3 non-change note

Proof fixture `PHASE_3E2_3_FINAL_EXACTLY_ONCE_PROOF` on `final-proof.example` is allowed to produce a draft for offline/live acceptance. Human regression text covers traffic decline after a site update. Reply rules, AI OFF behavior and customer auto-send prohibition are unchanged.
