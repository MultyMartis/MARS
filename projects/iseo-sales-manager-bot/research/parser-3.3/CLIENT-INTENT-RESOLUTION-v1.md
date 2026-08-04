# CLIENT INTENT RESOLUTION v1

**IMPLEMENTED — Phase 3E.1.** See architecture specs under `architecture/` and evidence `evidence/phase3e1/`.

## Precedence

1. explicit client comment;
2. structured fields;
3. explicit selected service;
4. source-page context;
5. email subject / form title.

Более слабый источник не перезаписывает более сильный. Конфликт сохраняется как `intent_conflict=true` и краткая sanitized reason, а не усредняется. Отсутствие сигнала даёт `Other/unknown`, не выдуманную услугу.

## Outputs

`resolved_intent`, `intent_confidence`, `intent_evidence_source`, `intent_evidence_excerpt_redacted`, `intent_conflict`, `selected_service_raw_normalized`, `source_page_context`. Confidence не заменяет provenance.