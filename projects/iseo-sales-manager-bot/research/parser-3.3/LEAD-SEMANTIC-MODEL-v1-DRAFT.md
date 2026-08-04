# LEAD SEMANTIC MODEL v1 — DRAFT

**IMPLEMENTED — Phase 3E.1.** Authority: [architecture/LEAD-SEMANTIC-MODEL-v1.md](../../architecture/LEAD-SEMANTIC-MODEL-v1.md). This file remains historical research notes.

## Required semantic fields

- identity/contact: `client_name`, `phone`, `email`, `messenger`, `primary_contact`, `contact_type`;
- site: `site_value`, `site_state`, `site_evidence_source`;
- intent: `resolved_intent`, `selected_service`, `intent_confidence`, `intent_evidence_source`, `intent_conflict`;
- request: `client_comment`, `request_summary`, `explicit_constraints`, `preferred_contact_method`;
- origin: `form_name`, `source_page`, `email_subject_class`, `source_type`;
- quality: `missing_fields`, `invalid_fields`, `quality_status`, `clarification_questions`;
- reply: `first_reply_text`, `reply_fact_sources`, `reply_consistency_status`;
- trace: `parser_version`, `semantic_model_version`, `field_provenance`, `warnings`.

## Precedence

`explicit client comment → structured fields → explicit selected service → source-page context → email subject/form title`.

Каждое resolved field хранит source/provenance. Explicit absence отличается от missing. Model не содержит raw secrets и не требует сохранения unsanitized body в документации.