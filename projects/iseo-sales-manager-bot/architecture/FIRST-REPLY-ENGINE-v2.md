# FIRST REPLY ENGINE v2

**Product:** i-SEO Sales Manager Bot  
**Version:** `sm-reply-v2.0`  
**Status:** IMPLEMENTED (Phase 3E.2)  
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
| `first_reply_version` | `sm-reply-v2.0` |
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

## Related

- [KNOWN-INFORMATION-GUARD-v1.md](KNOWN-INFORMATION-GUARD-v1.md)
- [MANAGER-CARD-v2.4-CONTRACT-v1.md](MANAGER-CARD-v2.4-CONTRACT-v1.md)
- [FIRST-REPLY-RULES-v1.md](FIRST-REPLY-RULES-v1.md) (extended by this engine)
