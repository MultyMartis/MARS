# COMMENT BOUNDARY REQUIREMENTS v1

**IMPLEMENTED — Phase 3E.1.** See architecture specs under `architecture/` and evidence `evidence/phase3e1/`.

1. Начало комментария задаётся распознанным label, окончание — только следующим валидным top-level label.
2. Слова «телефон», «сайт», «email» внутри естественного текста не завершают комментарий без синтаксического label-pattern.
3. Поддерживаются newline, CRLF, NBSP и collapsed single-line variants.
4. Повторный label обрабатывается детерминированно; provenance всех кандидатов сохраняется.
5. Quoted previous message/signature не смешивается с current form body.
6. Максимальные длины ограничены; truncation отмечается, а не скрывается.
7. Sanitized fixtures включают label-like words, punctuation, Unicode и пустые значения.