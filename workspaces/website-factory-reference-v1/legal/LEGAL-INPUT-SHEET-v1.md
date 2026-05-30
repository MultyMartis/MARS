# Website Factory — Legal Input Sheet v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/legal/`  
**Статус:** канонический input contract для генерации legal pages — **documentation only**  
**Не является:** автоматической формой, CI-validator, юридической экспертизой

---

## Назначение

Legal Input Sheet v1 — **единый источник правды** для подстановки переменных и принятия решений при генерации Core Legal Pack (L1–L4).

Обязательный input contract для:

| Документ | Шаблон |
|----------|--------|
| L1 — Политика конфиденциальности | `privacy-policy-template.md` |
| L2 — Согласие на обработку персональных данных | `consent-personal-data-template.md` |
| L3 — Пользовательское соглашение | `user-agreement-template.md` |
| L4 — Политика Cookie-файлов | `cookie-files-policy-template.md` |

**FUTURE (не в scope v1):** Extension Packs для ECOMMERCE, SAAS, MARKETPLACE — отдельные input addendum по charter.

**Связанные документы:**

| Документ | Назначение |
|----------|------------|
| [LEGAL-INPUT-SHEET-TEMPLATE-v1.md](LEGAL-INPUT-SHEET-TEMPLATE-v1.md) | Заполняемый шаблон |
| [LEGAL-INPUT-INSTRUCTIONS-v1.md](LEGAL-INPUT-INSTRUCTIONS-v1.md) | Инструкции оператора |
| [LEGAL-GENERATION-WORKFLOW-v1.md](LEGAL-GENERATION-WORKFLOW-v1.md) | Production workflow |
| [LEGAL-VARIABLE-REGISTRY.md](LEGAL-VARIABLE-REGISTRY.md) | Реестр переменных подстановки |
| [LEGAL-GENERATION-CONTRACT-v1.md](LEGAL-GENERATION-CONTRACT-v1.md) | Production gate |
| [LEGAL-IMPLEMENTATION-RULES.md](LEGAL-IMPLEMENTATION-RULES.md) | Footer Rule, Consent Rule, H1 |
| [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) | Approved site types (8) |
| [SITE-TYPE-LEGAL-MAPPING-v2.md](SITE-TYPE-LEGAL-MAPPING-v2.md) | Требования по site type |
| [LEGAL-ENTITY-CARD-v1.md](../legal-entity/LEGAL-ENTITY-CARD-v1.md) | **Upstream** — identity/entity fields |
| [LEGAL-ENTITY-WORKFLOW-v1.md](../legal-entity/LEGAL-ENTITY-WORKFLOW-v1.md) | Discovery → card → this sheet |

---

## Upstream: Legal Entity Card (обязательный поток v1)

Legal Input Sheet **не выполняет discovery**. Поля Identity и Legal Entity Block **потребляют** подтверждённый [LEGAL-ENTITY-CARD-v1.md](../legal-entity/LEGAL-ENTITY-CARD-v1.md) (`operator_verified = true`, `card_status = READY`).

```text
Discovery
        ↓
Legal Entity Card
        ↓
Legal Input Sheet   ← этот документ
        ↓
Legal Generation
```

| Правило | Действие |
|---------|----------|
| Заполнение identity из footer/content без card | **Запрещено** как primary path |
| Card `NOT_READY` / UNKNOWN `company_name` / `legal_name` | Input Sheet **не подписывается**; generation **STOP** |
| Traceability | В `notes` указать `card_id` |

Прямое копирование из website footer допустимо **только** как этап extraction в card (P4) с последующим P6 — см. [LEGAL-ENTITY-DISCOVERY-RULES-v1.md](../legal-entity/LEGAL-ENTITY-DISCOVERY-RULES-v1.md).

---

## Правила заполнения

1. Один Legal Input Sheet — **на один production deploy target** (один домен / одна property).
2. Identity / Legal Entity fields — **из verified Legal Entity Card**, не из ad-hoc discovery.
3. Значения **не выдумываются**. Если данные не подтверждены оператором — поле = `UNKNOWN` с пояснением в `notes`.
4. После заполнения оператор ставит **sign-off** (см. шаблон).
5. Лист хранится в project workspace или pilot folder; **не** копируется в canonical templates.
6. **Mobile App Factory** — **OUT OF SCOPE**; отдельная FUTURE factory.

---

## Схема полей

### Meta

| Поле | Тип | Обязательность | Описание |
|------|-----|:--------------:|----------|
| `sheet_id` | string | Required | Уникальный ID листа, напр. `triumph-manipulator-v6-2026-05` |
| `project_name` | string | Required | Рабочее имя проекта |
| `workspace_path` | string | Recommended | Путь к workspace, напр. `workspaces/triumph-manipulator-landing-v6/` |
| `operator_sign_off` | boolean + date + name | Required before generation | Подтверждение оператора |
| `notes` | text | Optional | Пояснения, HITL-решения, источники данных |

---

### Site Type Block

| Поле | Тип | Обязательность | Описание |
|------|-----|:--------------:|----------|
| `site_type` | enum | **Required** | Код из [SITE-TYPE-REGISTRY-v1](../registry/SITE-TYPE-REGISTRY-v1.md) |

**Allowed values (только эти 8):**

| `site_type` | Группа |
|-------------|--------|
| `LANDING` | CORE |
| `PROMO` | CORE |
| `CATALOG` | CORE |
| `ECOMMERCE` | CORE |
| `CORPORATE` | CORE |
| `SAAS` | EXTENDED |
| `WEB_APPLICATION` | EXTENDED |
| `MARKETPLACE` | EXTENDED |

**Запрещено:** любые другие значения, lowercase aliases, composite codes без human charter.

**Поведение:** `site_type` определяет applicable mapping из [SITE-TYPE-LEGAL-MAPPING-v2.md](SITE-TYPE-LEGAL-MAPPING-v2.md) — какие документы L1–L4 обязательны, footer links, consent texts.

---

### Identity Block (Required)

| Поле | Тип | Обязательность | Maps to | Описание |
|------|-----|:--------------:|---------|----------|
| `company_name` | string | **Required** | `{{company_name}}` | Наименование для подстановки в шаблоны (Оператор / Администрация сайта) |
| `legal_name` | string | **Required** | — | Полное юридическое наименование по учредительным документам |
| `domain` | string | **Required** | `{{domain}}` | Production hostname без протокола, напр. `example.ru` |
| `email` | string | **Required** | `{{email}}` | Контактный email для обращений и отзыва согласия |
| `phone` | string | **Required** | `{{phone}}` | Контактный телефон в production-формате |

**Правило `company_name` vs `legal_name`:**

- Обычно совпадают для RU юрлица / ИП.
- Если маркетинговое имя отличается от юридического — в шаблоны идёт **подтверждённое оператором** значение `company_name`; `legal_name` фиксирует юридическую форму для audit trail.
- Любое из полей = `UNKNOWN` **блокирует generation** до operator sign-off.

---

### Legal Entity Block

| Поле | Тип | Обязательность | Maps to | Описание |
|------|-----|:--------------:|---------|----------|
| `entity_type` | enum | Required | — | `LEGAL_ENTITY` \| `INDIVIDUAL_ENTREPRENEUR` \| `SELF_EMPLOYED` \| `UNKNOWN` |
| `inn` | string | **Required** for `LEGAL_ENTITY`, `INDIVIDUAL_ENTREPRENEUR` | `{{inn}}` | ИНН |
| `ogrn` | string | **Required** for `LEGAL_ENTITY` | `{{ogrn}}` | ОГРН |
| `ogrnip` | string | **Required** for `INDIVIDUAL_ENTREPRENEUR` | `{{ogrn}}` | ОГРНИП (записывается в поле `ogrn` для подстановки) |

**Примечание:** Core templates v1 **не содержат** `{{inn}}` / `{{ogrn}}` в теле — поля обязательны в Input Sheet для audit и footer/requisites; при вставке в project-specific pages подчиняются [LEGAL-GENERATION-CONTRACT-v1.md](LEGAL-GENERATION-CONTRACT-v1.md) FAIL gate.

---

### Address Block

| Поле | Тип | Обязательность | Maps to | Описание |
|------|-----|:--------------:|---------|----------|
| `address_status` | enum | **Required** | — | `PROVIDED` \| `NOT_PROVIDED` |
| `address` | string | Conditional | `{{address}}` | Юридический или почтовый адрес — **только** при `address_status = PROVIDED` |

#### Поведение при отсутствии адреса

| `address_status` | Поведение generation system |
|------------------|----------------------------|
| `NOT_PROVIDED` | Core templates L1–L4 **генерируются as-is** — шаблоны v1 **не содержат** `{{address}}` в теле. Generation **не блокируется** отсутствием адреса. |
| `PROVIDED` | Значение `address` подставляется во все места, где оператор/project charter добавляет адрес (footer requisites, custom sections). |
| `PROVIDED` + пустой `address` | **Validation FAIL** — несогласованное состояние. |
| Любой `{{address}}` в production output | **Production Release FAIL** per LEGAL-GENERATION-CONTRACT |

**HITL:** если оператор требует адрес в legal body, но `address_status = NOT_PROVIDED` — generation **блокируется** до получения адреса или явного решения об опускании секции.

---

### Derived URLs Block

| Поле | Тип | Обязательность | Maps to | Правило вычисления |
|------|-----|:--------------:|---------|-------------------|
| `privacy_policy_url` | string | **Required** | `{{privacy_policy_url}}` | `https://{{domain}}/privacy-policy/` |
| `consent_personal_data_url` | string | **Required** | `{{consent_personal_data_url}}` | `https://{{domain}}/consent-personal-data/` |

Канонические пути (не переменные): `/user-agreement/`, `/cookie-files-policy/` — фиксированы в шаблонах и footer.

---

### Cookie Inventory Block (Optional)

Опциональная секция для **будущей** точной генерации L4 и audit tracking. **Не блокирует** Core generation v1, если не заполнена.

#### Analytics systems

| Поле | Тип | Значения |
|------|-----|----------|
| `analytics.yandex_metrika` | boolean | Активна на production |
| `analytics.google_analytics` | boolean | Активна на production |
| `analytics.other` | string[] | Прочие системы, напр. `["VK Pixel"]` |

#### Tracking systems

| Поле | Тип | Значения |
|------|-----|----------|
| `tracking.recaptcha` | boolean | Google reCAPTCHA / аналог |
| `tracking.chat_widgets` | string[] | Виджеты чата, напр. `["JivoSite"]` |
| `tracking.call_tracking` | boolean | Call tracking |
| `tracking.other` | string[] | Прочие tracker-сервисы |

**Поведение v1:** Core L4 template использует **типовые категории** cookie; cookie inventory фиксирует фактический production stack для operator review. Полная auto-customization L4 по inventory — **FUTURE**.

---

### Footer Block (Canonical — Reference Only)

Production footer **обязан** содержать четыре ссылки. Полная спецификация — [LEGAL-IMPLEMENTATION-RULES.md §3](LEGAL-IMPLEMENTATION-RULES.md).

| Текст ссылки (= H1) | URL |
|---------------------|-----|
| Политика конфиденциальности | `/privacy-policy/` |
| Согласие на обработку персональных данных | `/consent-personal-data/` |
| Пользовательское соглашение | `/user-agreement/` |
| Политика Cookie-файлов | `/cookie-files-policy/` |

**Input Sheet фиксирует:** подтверждение, что footer partials проекта будут приведены к этому канону перед production sign-off.

| Поле | Тип | Обязательность |
|------|-----|:--------------:|
| `footer.canonical_links_confirmed` | boolean | Required before sign-off |

---

### Consent Block (Canonical — Reference Only)

Единственный допустимый текст согласия в формах — [LEGAL-IMPLEMENTATION-RULES.md §4](LEGAL-IMPLEMENTATION-RULES.md).

**Не дублировать** альтернативные формулировки в Input Sheet. Input Sheet фиксирует только:

| Поле | Тип | Обязательность |
|------|-----|:--------------:|
| `consent.canonical_text_confirmed` | boolean | Required before sign-off |
| `consent.forms_with_pd_collection` | string[] | Recommended — список partials/форм с ПДн |

---

## Validation Rules (Input Sheet)

| Check | Pass | Fail |
|-------|------|------|
| `site_type` in approved 8 | ✓ | Unknown site type |
| Required identity fields filled or explicitly `UNKNOWN` with notes | ✓ | Empty required field without explanation |
| `entity_type` + inn/ogrn consistency | ✓ | INN/OGRN missing for legal entity |
| `address_status` consistency | ✓ | PROVIDED with empty address |
| Derived URLs match domain | ✓ | Mismatch |
| Operator sign-off | ✓ | Missing sign-off |
| No new legal document types | ✓ | Request for non-L1–L4 doc without Extension charter |

---

## Relationship to Generation Contract

| Phase | Input Sheet role |
|-------|------------------|
| Pre-generation | Operator completes and signs Input Sheet |
| Generation | All `{{variables}}` sourced **only** from signed Input Sheet |
| Post-generation | LEGAL-GENERATION-CONTRACT Phase 3 scan — zero forbidden placeholders |
| Sign-off | Input Sheet ID recorded in production release log |

---

## SAFE UNKNOWN

- Machine-readable JSON Schema for Input Sheet — **not defined** v1; canon = Markdown template.
- Multi-environment variable sets (staging vs prod) — **per charter**; v1 assumes single production domain per sheet.
- Automated Input Sheet validator script — **not implemented**.

---

*Schema version: v1. Canonical location: `workspaces/website-factory-reference-v1/legal/`.*
