# Website Factory — правила внедрения юридических страниц

**Версия:** v1.1  
**Область:** `workspaces/website-factory-reference-v1/legal/`  
**Статус:** канонический справочник для production-сборок Website Factory

**Legal Architecture v1 (связанные документы):**

| Документ | Назначение |
|----------|------------|
| [LEGAL-PACK-ARCHITECTURE-v1.md](LEGAL-PACK-ARCHITECTURE-v1.md) | Core Pack + Extension Packs |
| [SITE-TYPE-LEGAL-MAPPING-v2.md](SITE-TYPE-LEGAL-MAPPING-v2.md) | Матрица требований по site type |
| [LEGAL-GENERATION-CONTRACT-v1.md](LEGAL-GENERATION-CONTRACT-v1.md) | Production gate — запрет плейсхолдеров |
| [LEGAL-TEMPLATE-REVIEW-v1.md](LEGAL-TEMPLATE-REVIEW-v1.md) | Audit шаблонов (без rewrite) |

---

## 1. Когда юридические страницы обязательны

Юридические страницы **требуются**, если выполняется **хотя бы одно** из условий:

- Website Factory собирает **полный сайт**;
- Website Factory собирает **полный лендинг**;
- проект **выводится в production**;
- на сайте **собираются персональные данные** (формы, callback, регистрация и т. п.).

В этих случаях используются канонические шаблоны из данной папки с подстановкой переменных клиента.

---

## 2. Когда юридические страницы не обязательны

Юридические страницы **не требуются**, если работа ограничена:

- частичной реализацией страниц;
- изолированной разработкой секции;
- автономным frontend-блоком;
- design-only работой;
- внедрением center-content в **существующий** сайт клиента (без полной Factory-сборки и без production-релиза Factory).

---

## 3. Правило футера (Footer Rule)

На **всех production-сайтах**, собранных Website Factory, в футере **обязательны** ссылки на четыре юридические страницы.

| Текст ссылки (строго как H1) | Канонический URL |
|------------------------------|------------------|
| Политика конфиденциальности | `/privacy-policy/` |
| Согласие на обработку персональных данных | `/consent-personal-data/` |
| Пользовательское соглашение | `/user-agreement/` |
| Политика Cookie-файлов | `/cookie-files-policy/` |

**Требования:**

- текст ссылки **должен совпадать** с H1 соответствующей страницы;
- URL **не подлежат замене** на альтернативные пути;
- альтернативные формулировки ссылок запрещены.

---

## 4. Правило согласия в формах (Consent Rule)

Для чекбокса / текста согласия в формах сбора персональных данных используется **только** следующий канонический HTML (без перефразирования):

```html
Я&nbsp;даю согласие на&nbsp;обработку персональных данных в&nbsp;соответствии с&nbsp;<a href="/consent-personal-data/" target="_blank">Согласием на&nbsp;обработку персональных данных</a> и&nbsp;соглашаюсь с&nbsp;<a href="/privacy-policy/" target="_blank">Политикой конфиденциальности</a>.
```

**Запрещено:**

- менять формулировку;
- менять целевые URL;
- заменять `&nbsp;` на обычные пробелы в production-разметке без явного решения оператора (канон — как выше).

---

## 5. Канонические H1

| Страница | H1 |
|----------|-----|
| Privacy | Политика конфиденциальности |
| Consent | Согласие на обработку персональных данных |
| User Agreement | Пользовательское соглашение |
| Cookie | Политика Cookie-файлов |

Контент шаблона **начинается** с соответствующего H1 (`#` в Markdown).

---

## 6. Шаблоны и переменные

| Файл шаблона | Назначение |
|--------------|------------|
| `privacy-policy-template.md` | Политика конфиденциальности |
| `consent-personal-data-template.md` | Согласие на обработку ПДн |
| `user-agreement-template.md` | Пользовательское соглашение |
| `cookie-files-policy-template.md` | Политика Cookie-файлов |

Переменные подстановки — см. [LEGAL-VARIABLE-REGISTRY.md](LEGAL-VARIABLE-REGISTRY.md).

Перед production release — обязательная проверка по [LEGAL-GENERATION-CONTRACT-v1.md](LEGAL-GENERATION-CONTRACT-v1.md): наличие `{{company_name}}`, `{{domain}}`, `{{email}}`, `{{phone}}`, `{{address}}`, `{{inn}}`, `{{ogrn}}` или иных необработанных `{{...}}` в опубликованных legal pages = **Production Release FAIL**.

---

## 7. Site types и Extension Packs

Approved site types (8) — см. [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md). Core Legal Pack (L1–L4) покрывает все типы; Extension Packs — см. [LEGAL-PACK-ARCHITECTURE-v1.md](LEGAL-PACK-ARCHITECTURE-v1.md).

**Mobile App Factory** — **OUT OF SCOPE**; FUTURE separate factory.

---

## 8. Связанные документы MARS

- Website Factory workflow: `projects/mars-website-factory/`
- Survivability / Factory enforcement: `projects/mars-survivability/contracts/website-factory-enforcement-v1.md`

## 9. Legal Content Layout Rule

Юридические страницы **не вводят** изолированную типографику или узкую legal-only колонку. Они используют **контейнер контента проекта** и **стили контента по умолчанию** того сайта, где внедрены.

| Требование | Правило |
|----------|--------|
| Контейнер | Legal body размещается в **project content container** (типовой `section-shell` / page template), на **полную рабочую ширину** контейнера |
| Узкая колонка | **Запрещено** искусственно сужать legal text (`max-width` только для legal body), если шаблон контента проекта этого не задаёт |
| Типографика | Наследует **project content-page typography** — класс `.content-page` (или эквивалентный reusable project layer) для семантических тегов контента |
| Content-page layer | Если в проекте **нет** `.content-page` (или эквивалента), Website Factory **создаёт** reusable project-level content typography layer **до** подключения legal shell; **не** создавать legal-only typography |
| HTML | Чистый семантический контент: `h1`, `h2`, `h3`, `p`, `ul`, `ol`, `li`, `a`, `table`, `thead`, `tbody`, `tr`, `th`, `td` |
| Изоляция | **Запрещены** отдельные legal font-size / line-height / paragraph overrides, отдельная legal typography system; legal shell — только layout, dark shell, nav, spacing, table overflow wrappers |
| Классы в body | Генератор **не** добавляет визуальные utility-классы в legal body, кроме wrapper hooks шаблона проекта (например, shell body, table overflow wrap) |
| Shell | Допустимы только structural/layout правила shell: spacing, nav, section padding, table overflow, dark-theme **color** (без per-tag font-size) |

См. также production gate: [LEGAL-GENERATION-CONTRACT-v1.md](LEGAL-GENERATION-CONTRACT-v1.md) — layout validation.

---

**Не является:** автоматической проверкой в CI, юридической экспертизой, заменой консультации юриста.
