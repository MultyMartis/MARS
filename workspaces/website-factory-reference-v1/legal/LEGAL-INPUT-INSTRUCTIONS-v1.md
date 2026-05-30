# Website Factory — Legal Input Instructions v1

**Версия:** v1  
**Аудитория:** оператор, human executor, charter-approved agent  
**Схема:** [LEGAL-INPUT-SHEET-v1.md](LEGAL-INPUT-SHEET-v1.md)  
**Шаблон:** [LEGAL-INPUT-SHEET-TEMPLATE-v1.md](LEGAL-INPUT-SHEET-TEMPLATE-v1.md)  
**Workflow:** [LEGAL-GENERATION-WORKFLOW-v1.md](LEGAL-GENERATION-WORKFLOW-v1.md)

---

## 1. Когда создавать Legal Input Sheet

Создайте Input Sheet **до** генерации legal pages, если выполняется хотя бы одно:

- full Website Factory landing / site → production;
- на сайте собираются персональные данные;
- pilot или client deploy с Core Legal Pack L1–L4.

**Не требуется** для design-only, isolated section work, partial implementation без production — см. [LEGAL-IMPLEMENTATION-RULES.md §2](LEGAL-IMPLEMENTATION-RULES.md).

---

## 2. Порядок заполнения

### Шаг 1 — Копирование шаблона

1. Скопируйте [LEGAL-INPUT-SHEET-TEMPLATE-v1.md](LEGAL-INPUT-SHEET-TEMPLATE-v1.md) в project workspace или `legal/pilots/` / `legal/examples/`.
2. Переименуйте: `{project}-legal-input-{date}.md`.
3. Заполните `sheet_id` и `workspace_path`.

### Шаг 2 — Site Type

1. Выберите **один** код из [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md).
2. Проверьте требования в [SITE-TYPE-LEGAL-MAPPING-v2.md](SITE-TYPE-LEGAL-MAPPING-v2.md).
3. **Не добавляйте** новые site types.

### Шаг 3 — Identity Block

| Поле | Источник данных | Правило |
|------|-----------------|---------|
| `company_name` | Учредительные документы, договор, footer клиента | Строка для `{{company_name}}` в шаблонах |
| `legal_name` | ЕГРЮЛ / ЕГРИП / договор | Полное юридическое наименование |
| `domain` | Production DNS / canonical URL проекта | Без `https://` |
| `email` | Контактный email на сайте / договор | Должен совпадать с production |
| `phone` | Header / footer / договор | Production-формат |

**Если значение не подтверждено:** `UNKNOWN` + запись в Notes с указанием, что нужно для подтверждения.

### Шаг 4 — Legal Entity Block

1. Укажите `entity_type`.
2. Для `LEGAL_ENTITY`: заполните `inn` (10 цифр) и `ogrn` (13 цифр).
3. Для `INDIVIDUAL_ENTREPRENEUR`: `inn` (12 цифр) и `ogrnip` → поле `ogrn`.
4. Для `SELF_EMPLOYED`: inn/ogrn по charter; если не применимо — `UNKNOWN` с notes.

### Шаг 5 — Address Block

| Сценарий | Действие |
|----------|----------|
| Адрес известен и подтверждён | `address_status = PROVIDED`, заполнить `address` |
| Адрес не предоставлен клиентом | `address_status = NOT_PROVIDED`, `address` пустой |
| Адрес требуется оператором в legal body | **Не начинать generation** без PROVIDED |

**При `NOT_PROVIDED`:** Core templates v1 генерируются без адреса — это **валидный** path. Запрещено оставлять `{{address}}` в production output.

### Шаг 6 — Derived URLs

Вычислите из `domain`:

```
privacy_policy_url      = https://{domain}/privacy-policy/
consent_personal_data_url = https://{domain}/consent-personal-data/
```

Проверьте, что domain = production, не staging (или создайте отдельный sheet per environment).

### Шаг 7 — Cookie Inventory (Optional)

Заполните, если на production есть:

- Yandex Metrika, Google Analytics;
- reCAPTCHA, chat widgets, call tracking.

Используйте для operator review L4; Core template v1 **не требует** inventory для generation.

### Шаг 8 — Footer & Consent Confirmation

1. Подтвердите `footer.canonical_links_confirmed = yes`.
2. Подтвердите `consent.canonical_text_confirmed = yes`.
3. Перечислите все формы с ПДн.

**Тексты:** только канон из [LEGAL-IMPLEMENTATION-RULES.md](LEGAL-IMPLEMENTATION-RULES.md) — **не перефразировать**.

### Шаг 9 — Operator Sign-Off

Generation **запрещена** без sign-off, если любое Required поле = `UNKNOWN`.

---

## 3. Валидация Input Sheet (pre-generation)

| # | Check | Method |
|---|-------|--------|
| 1 | Site type in approved 8 | Manual compare to SITE-TYPE-REGISTRY |
| 2 | No empty Required without UNKNOWN + notes | Manual review |
| 3 | INN/OGRN format plausible | Manual / registry lookup |
| 4 | Domain = production target | Operator confirm |
| 5 | Derived URLs consistent | String match |
| 6 | No legacy client data in sheet | Search wrong domains/emails |
| 7 | Sign-off present | Checkbox + name + date |

---

## 4. Что делать после sign-off

Передайте signed Input Sheet в [LEGAL-GENERATION-WORKFLOW-v1.md](LEGAL-GENERATION-WORKFLOW-v1.md) — шаги 4–8.

---

## 5. Запреты

| Запрет | Причина |
|--------|---------|
| Выдумывать `company_name`, `legal_name`, `address` | Legal accuracy |
| Новые legal document types без Extension charter | LEGAL-PACK-ARCHITECTURE v1 |
| Новые site types | SITE-TYPE-REGISTRY v1 |
| Альтернативные consent wordings | LEGAL-IMPLEMENTATION-RULES §4 |
| Альтернативные footer URLs | LEGAL-IMPLEMENTATION-RULES §3 |
| Mobile App Factory legal flows | OUT OF SCOPE |

---

## 6. SAFE UNKNOWN

- Licensed legal review — **не входит** в Input Sheet workflow v1.
- Automated INN/OGRN verification API — **not implemented**.
- Cookie inventory → auto L4 rewrite — **FUTURE**.

---

*Instructions version: v1. Canonical location: `workspaces/website-factory-reference-v1/legal/`.*
