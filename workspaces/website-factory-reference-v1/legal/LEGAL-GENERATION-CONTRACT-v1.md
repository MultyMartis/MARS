# Website Factory — Legal Generation Contract v1

**Версия:** v1  
**Область:** production release gate для legal pages Website Factory  
**Статус:** канонический контракт — **documentation only**  
**Не является:** автоматическим CI-check, юридической экспертизой, runtime validator

**Связанные документы:**

- [LEGAL-VARIABLE-REGISTRY.md](LEGAL-VARIABLE-REGISTRY.md)
- [LEGAL-IMPLEMENTATION-RULES.md](LEGAL-IMPLEMENTATION-RULES.md)
- [LEGAL-PACK-ARCHITECTURE-v1.md](LEGAL-PACK-ARCHITECTURE-v1.md)
- [SITE-TYPE-LEGAL-MAPPING-v2.md](SITE-TYPE-LEGAL-MAPPING-v2.md)

---

## Назначение

Legal Generation Contract v1 определяет **обязательные условия** перед production release legal pages: какие плейсхолдеры запрещены, как выполняется валидация, и когда release считается **FAIL**.

Контракт применяется ко **всем** Website Factory production-сборкам с Core Legal Pack (L1–L4).

---

## Production Release Gate

### Правило FAIL

**Production Release = FAIL**, если в опубликованных legal pages (HTML/Markdown production output) остаётся **хотя бы один** необработанный forbidden placeholder.

### FORBIDDEN placeholders (production)

Следующие плейсхолдеры **запрещены** в production output:

| Placeholder | Описание |
|-------------|----------|
| `{{company_name}}` | Наименование оператора |
| `{{domain}}` | Домен сайта |
| `{{email}}` | Контактный email |
| `{{phone}}` | Телефон |
| `{{address}}` | Адрес |
| `{{inn}}` | ИНН |
| `{{ogrn}}` | ОГРН / ОГРНИП |

### Дополнительные placeholders (реестр v1)

| Placeholder | Production status |
|-------------|-------------------|
| `{{privacy_policy_url}}` | **FAIL** if unresolved at production |
| `{{consent_personal_data_url}}` | **FAIL** if unresolved at production |
| Любой `{{...}}` не из реестра | **FAIL** — unauthorized placeholder |

**Исключение:** явно задокументированное HITL-отложение с operator sign-off и blocked production flag — **не** стандартный path; по умолчанию **FAIL**.

---

## Обязательные подстановки (minimum production set)

Для типичного RU commercial site (LANDING / PROMO / CATALOG baseline):

| Variable | Обязательность |
|----------|----------------|
| `{{company_name}}` | **Required** |
| `{{domain}}` | **Required** |
| `{{email}}` | **Required** (сбор ПДn) |
| `{{privacy_policy_url}}` | **Required** (рекомендуется → production Required) |
| `{{consent_personal_data_url}}` | **Required** (рекомендуется → production Required) |
| `{{phone}}` | По charter проекта |
| `{{address}}` | По charter проекта |
| `{{inn}}` | По charter проекта |
| `{{ogrn}}` | По charter проекта |

Переменные `phone`, `address`, `inn`, `ogrn` **не в теле** Core templates v1 — но если оператор добавляет их в project-specific pages, они **подчиняются** тому же FAIL gate.

---

## Validation Process

### Phase 1 — Pre-generation (operator input)

1. Оператор заполняет **Legal Input Sheet** (project charter) — все required variables для site type.
2. Подтверждается `site_type_code` из [SITE-TYPE-REGISTRY-v1](../registry/SITE-TYPE-REGISTRY-v1.md).
3. Проверяется applicable mapping из [SITE-TYPE-LEGAL-MAPPING-v2.md](SITE-TYPE-LEGAL-MAPPING-v2.md).

### Phase 2 — Generation (human-operated)

1. Копирование / рендер из канонических templates L1–L4.
2. Подстановка всех variables из [LEGAL-VARIABLE-REGISTRY.md](LEGAL-VARIABLE-REGISTRY.md).
3. **Запрещено:** AI paraphrasing legal text, alternative consent wording, alternative URLs.

### Phase 3 — Post-generation scan (mandatory before production)

Human-operated scan (grep / manual review) по **production output**:

| Check | Pass criteria |
|-------|---------------|
| Forbidden placeholders | Zero matches for `{{company_name}}`, `{{domain}}`, `{{email}}`, `{{phone}}`, `{{address}}`, `{{inn}}`, `{{ogrn}}` |
| All placeholders | Zero unresolved `{{...}}` |
| H1 canonical | Four pages match LEGAL-IMPLEMENTATION-RULES §5 |
| Footer links | Four links match Footer Rule §3 |
| Consent text | Exact match Consent Rule §4 on all forms |
| Cross-links | Internal legal URLs = canonical paths |
| Client data leak | No other project's company/domain/email in output |
| Legal layout — container | Legal body uses project content container full working width; no legal-only narrow column unless project template defines it |
| Legal layout — typography | Legal pages use project `.content-page` (or equivalent) layer; no legal-specific font-size / line-height / paragraph typography overrides in production output |
| Legal layout — inline styles | Zero `style=` attributes for typography in legal body |
| Legal layout — HTML classes | No presentational typography classes inside legal body (wrapper hooks from project template only) |
| Legal layout — placeholders | Zero unresolved `{{...}}`; zero client leftovers from other projects |

### Phase 4 — Production sign-off

| Result | Action |
|--------|--------|
| **PASS** | All Phase 3 checks green → production release allowed |
| **FAIL** | Any forbidden placeholder or rule violation → **block release**, fix and re-scan |

---

## Scan commands (reference — human-operated)

Пример проверки unresolved placeholders в каталоге проекта (PowerShell / bash — оператор выбирает):

```powershell
# Forbidden placeholders — any match = FAIL
Select-String -Path ".\src\pages\legal\*" -Pattern '\{\{(company_name|domain|email|phone|address|inn|ogrn)\}\}'

# Any remaining placeholders — any match = FAIL (unless HITL exception)
Select-String -Path ".\src\pages\legal\*" -Pattern '\{\{[^}]+\}\}'
```

**Note:** paths depend on project structure; contract defines **semantics**, not project layout.

---

## Relationship to templates vs output

| Layer | Placeholders allowed? |
|-------|----------------------|
| Canonical templates (`legal/*-template.md`) | **Yes** — templates retain `{{variables}}` |
| Production pages (deployed HTML/MD) | **No** — zero forbidden placeholders |

---

## Extension Pack documents (FUTURE)

When Extension Pack templates appear, they **inherit** the same FAIL gate for all registered variables plus any extension-specific placeholders defined in future registry addendum.

---

## SAFE UNKNOWN

- Automated CI integration for this contract — **not implemented** in Website Factory v1.
- Machine-readable validation manifest (JSON) — **not defined**.
- Multi-locale placeholder sets — **not in scope** v1.

---

*Contract version: v1. Canonical location: `workspaces/website-factory-reference-v1/legal/`.*
