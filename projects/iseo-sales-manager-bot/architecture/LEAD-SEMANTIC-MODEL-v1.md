# LEAD SEMANTIC MODEL v1

**Product:** i-SEO Sales Manager Bot  
**Status:** **IMPLEMENTED** in Phase 3E.1 (`sm-parser-v3.3`, semantic model `lead-semantic-v1`)  
**Supersedes draft:** [research/parser-3.3/LEAD-SEMANTIC-MODEL-v1-DRAFT.md](../research/parser-3.3/LEAD-SEMANTIC-MODEL-v1-DRAFT.md)  
**Related:** [PARSER-3.3-CONTRACT-v1.md](PARSER-3.3-CONTRACT-v1.md) · [FIRST-REPLY-RULES-v1.md](FIRST-REPLY-RULES-v1.md) · [FIRST-REPLY-ENGINE-v2.md](FIRST-REPLY-ENGINE-v2.md) (Phase 3E.2 consumer)

---

## Purpose

Единая детерминированная семантика лида между Parse → Process → Format → Sheets/Telegram.  
Model **не** хранит raw secrets и **не** требует unsanitized body в документации.

---

## Required semantic fields

| Group | Fields |
|-------|--------|
| **Identity / contact** | `client_name`, `phone`, `email`, `messenger`, `primary_contact`, `contact_type` |
| **Site** | `site_value` / `site`, `website_state` (`provided` \| `explicitly_absent` \| `alternative_contact` \| `invalid_or_placeholder` \| `missing`), `site_evidence_source` |
| **Intent** | `resolved_intent`, `selected_service`, `intent_confidence`, `intent_evidence_source`, `intent_conflict` |
| **Request** | `client_comment` / `comment_normalized`, `request_summary`, `explicit_constraints`, `preferred_contact_method` |
| **Origin** | `form_name`, `source_page`, `email_subject_class`, `source_type` |
| **Quality** | `missing_fields`, `invalid_fields`, `quality_status`, `clarification_questions` |
| **Reply** | `first_reply_text`, `reply_fact_sources`, `reply_consistency_status` |
| **Trace** | `parser_version`, `semantic_model_version`, `field_provenance`, `warnings` |

Compat aliases from Parser 3.2 (`parsed_*`, `site`, `summary`, …) remain populated for CLEAN / archive / `/leads`.

---

## Precedence (intent & facts)

`explicit client comment → structured fields → explicit selected service → source-page context → email subject / form title`

- Более слабый источник **не** перезаписывает более сильный.
- Конфликт → `intent_conflict=true` + краткая sanitized reason (не усреднение).
- Отсутствие сигнала → `Other` / unknown — **не** выдуманная услуга.
- Explicit absence (`explicitly_absent`) **отличается** от `missing`.

---

## Website states (summary)

| State | Meaning |
|-------|---------|
| `provided` | пригодный site/domain |
| `explicitly_absent` | клиент явно сказал, что сайта нет / нужен сайт |
| `alternative_contact` | messenger/handle, не сайт |
| `invalid_or_placeholder` | мусор / шаблон / `#ERROR!` |
| `missing` | поля нет и явного утверждения нет |

---

## Quality & reply coupling

- Quality учитывает service-aware missing information (см. evidence `LEAD-QUALITY-MODEL-v1`).
- First reply строится **только** из resolved facts (см. `FIRST-REPLY-RULES-v1`).
- AI OFF template — baseline; AI ON (будущий) обязан тем же consistency checks.

---

## Not claimed

- Runtime orchestration inside MARS.
- AI ON in production.
- Automatic client send.
