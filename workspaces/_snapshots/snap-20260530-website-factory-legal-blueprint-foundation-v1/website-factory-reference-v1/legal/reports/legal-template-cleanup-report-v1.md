# Legal Template Cleanup Report v1

**Task:** Website Factory Legal Template Canonicalization v1  
**Date:** 2026-05-30  
**Target:** `workspaces/website-factory-reference-v1/legal/`

---

## Source files found

| Expected name | Actual file | Status |
|---------------|-------------|--------|
| Политика конфиденциальности.docx | `Политика конфиденциальности.docx` | Found |
| Согласие на обработку персональных данных.docx | `Согласие на обработку персональных данных.docx` | Found |
| Пользовательское соглашение.docx | `Пользовательское соглашение.docx` | Found |
| Политика Cookie-файлов.docx | `Политика Cookie файлов.docx` | Found (filename без дефиса в «Cookie файлов») |

**Input folder:** `C:\AI MARS\incoming\website-factory-legal-cleanup\`

**Extraction method:** Python 3 (`zipfile` + `word/document.xml`), промежуточные `.extracted.txt` в incoming (не часть канона).

---

## Variables introduced

| Variable | Introduced in templates |
|----------|-------------------------|
| `{{company_name}}` | privacy, consent, user-agreement, cookie |
| `{{domain}}` | privacy, consent, user-agreement, cookie |
| `{{email}}` | privacy, consent, cookie |
| `{{privacy_policy_url}}` | privacy |
| `{{consent_personal_data_url}}` | consent |
| `{{phone}}` | — (только реестр; в шаблонах v1 не используется) |
| `{{address}}` | — (только реестр) |
| `{{inn}}` | — (только реестр) |
| `{{ogrn}}` | — (только реестр) |

---

## Client data removed

| Type | Source value (removed) | Replacement |
|------|------------------------|-------------|
| Company | ООО «Триумф», Транспортная компания «Триумф» | `{{company_name}}` |
| Domain | gruzotaxi-triumph.ru | `{{domain}}` |
| Email | info@gktriumph.ru | `{{email}}` |
| Date | редакция от 04.05.2026 | удалена (клиентская дата) |
| Meta lines | `URL страницы всегда такой: domain.ru/...` | удалены из всех исходников |
| Industry-specific wording | «транспортная компания», «Сайт транспортной компании» | нейтральные формулировки + переменные |

**Not present in source (nothing to remove):** INN, OGRN, phone, postal address, personal names of individuals.

---

## Sections normalized

| Document | Normalization |
|----------|----------------|
| Privacy | Плоские строки → `##` / списки Markdown; удалён дубль URL-мета; добавлены канонические перекрёстные ссылки на consent и cookie |
| Consent | Структура разделов `##`; ссылка на `/privacy-policy/` |
| User Agreement | Иерархия `##` / `###`; унификация «учётная запись»; удалены отсылки к транспортной нише |
| Cookie | H1 «Политика Cookie-файлов»; исправлена опечатка «Содержащиеся»; нейтрализация «Яндекс» в примере сохранена; добавлен блок связанных документов |

---

## URL rules applied

| Page | Canonical path | Applied in |
|------|----------------|------------|
| Privacy | `/privacy-policy/` | consent link, cookie link, LEGAL-IMPLEMENTATION-RULES |
| Consent | `/consent-personal-data/` | privacy cross-ref, form consent rule |
| User Agreement | `/user-agreement/` | user-agreement template footer line |
| Cookie | `/cookie-files-policy/` | privacy cross-ref |

**No alternative paths** introduced.

---

## Validation results (post-generation)

Поиск по `workspaces/website-factory-reference-v1/legal/`:

| Check | Result |
|-------|--------|
| Client company names (Триумф, triumph) | **PASS** — не найдено |
| Client domains (gruzotaxi, gktriumph) | **PASS** — не найдено |
| Client emails (info@gktriumph.ru) | **PASS** — не найдено |
| Client phones | **PASS** — не найдено |
| Client addresses | **PASS** — не найдено |
| Client INN / OGRN | **PASS** — не найдено |
| Client date 04.05.2026 | **PASS** — не найдено |
| H1 canonical | **PASS** — все 4 шаблона |
| Allowed `{{variables}}` only | **PASS** — только реестр v1 |

**Note:** совпадения по `152-ФЗ` — ссылка на закон, не клиентские данные.

---

## Warnings

1. **Юридическая экспертиза не выполнялась** — шаблоны нормализованы по структуре и дехидратации клиента; правовая полнота остаётся на операторе / юристе клиента.
2. **Cookie-исходник** короче остальных и содержит разговорный тон; смысл сохранён, добавлены нейтральные связки без сокращения правовых блоков других документов.
3. **Переменные `{{phone}}`, `{{address}}`, `{{inn}}`, `{{ogrn}}`** зарезервированы в реестре, но не вставлены в тело шаблонов v1 (отсутствовали в incoming).
4. **Имя файла cookie в incoming:** `Политика Cookie файлов.docx` — расхождение с каноническим H1 «Cookie-файлов» (с дефисом) учтено только в output.
5. **Промежуточные `.extracted.txt`** в `incoming/` — артефакты извлечения; не удалялись (нет явной инструкции на удаление).

---

## SAFE UNKNOWN

1. **Полные реквизиты клиента** (ИНН, ОГРН, телефон, адрес) в исходных DOCX **не обнаружены** при текстовом извлечении — возможно отсутствие в теле или размещение в колонтитулах/таблицах, не попавших в plain extract.
2. **Скрытый текст / комментарии Word** — не анализировались; валидация по plain text + grep.
3. **Соответствие текстов актуальному законодательству РФ** на дату сборки — **UNKNOWN** без юридического review.
4. **Автоматическая генерация HTML-страниц** из Markdown в reference workspace — **не реализована** в рамках этой задачи (только шаблоны `.md`).

---

## Output artifacts

| File |
|------|
| `legal/privacy-policy-template.md` |
| `legal/consent-personal-data-template.md` |
| `legal/user-agreement-template.md` |
| `legal/cookie-files-policy-template.md` |
| `legal/LEGAL-IMPLEMENTATION-RULES.md` |
| `legal/LEGAL-VARIABLE-REGISTRY.md` |
| `legal/reports/legal-template-cleanup-report-v1.md` |
