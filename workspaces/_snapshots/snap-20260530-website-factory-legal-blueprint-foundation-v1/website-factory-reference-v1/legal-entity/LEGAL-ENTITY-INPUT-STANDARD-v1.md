# Website Factory — Legal Entity Input Standard v1

**Версия:** v1  
**Статус:** канонический стандарт размещения исходников — **documentation only**

---

## Канонический путь

В **каждом** client production workspace Website Factory:

```text
<project-workspace>/
└── project-input/
    └── legal-entity/
```

**Пример (Triumph — illustrative only, no workspace edits in this task):**

```text
workspaces/triumph-manipulator-landing-v6/
└── project-input/
    └── legal-entity/
        ├── company-card.pdf
        ├── requisites.docx
        ├── egrul.pdf
        └── bank-details.jpg
```

---

## Назначение каталога

| Цель | Описание |
|------|----------|
| Single inbox | Все первичные документы о юрлице в одном месте |
| Priority P1 | Высший приоритет discovery — см. [LEGAL-ENTITY-DISCOVERY-RULES-v1.md](LEGAL-ENTITY-DISCOVERY-RULES-v1.md) |
| Audit trail | Исходники сохраняются после extraction |
| Operator clarity | Клиент и оператор знают, **куда** класть файлы |

---

## Допустимое содержимое

### Документы

| Тип | Форматы | Примеры имён |
|-----|---------|--------------|
| Учредительные / реквизиты | PDF, DOCX | `requisites.docx`, `company-details.pdf` |
| ЕГРЮЛ / выписка | PDF | `egrul-2026-05-30.pdf` |
| Банковские реквизиты | PDF, DOCX, XLSX | `bank-details.pdf`, `payment-details.xlsx` |
| Договор / оферта (копия) | PDF, DOCX | `public-offer-draft.pdf` |

### Изображения и сканы

| Тип | Форматы |
|-----|---------|
| Визитка / company card | JPG, PNG, WEBP, PDF |
| Скан реквизитов | JPG, PNG, PDF |
| Фото банковской карты (реквизиты на обороте) | JPG, PNG — **без** PAN/CVV в repo |

### Таблицы

| Тип | Форматы |
|-----|---------|
| Реквизиты в таблице | XLSX, DOCX |

---

## Правила именования

1. **Латиница или кириллица** — согласованно в рамках проекта.
2. **Дата в имени** для выписк ЕГРЮЛ: `egrul-YYYY-MM-DD.pdf`.
3. **Без** пробелов в критичных CI-путях — предпочтительно `bank-details.jpg` vs `bank details.jpg`.
4. **Версии:** при обновлении документа — новый файл или суффикс `-v2`, не silent overwrite без operator note.

---

## Что **не** класть в `project-input/legal-entity/`

| Item | Куда вместо |
|------|-------------|
| Legal Entity Card (filled) | `legal/<project>-LEGAL-ENTITY-CARD-v1.md` или charter path |
| Legal Input Sheet | Project `legal/` или pilot folder |
| Сгенерированные L1–L4 HTML | `src/pages/` per generation workflow |
| Canonical templates | `website-factory-reference-v1/legal/` only |
| Секреты (API keys, passwords) | **Запрещено** — SECURITY RISK |

---

## Минимальный набор для production-ready card (рекомендация)

| Документ | Зачем |
|----------|-------|
| ЕГРЮЛ или выписка | `legal_name`, `inn`, `ogrn`, `address` |
| Карточка реквизитов / письмо с реквизитами | Banking block, контакты |
| Operator brief (optional MD) | Контекст, не замена ЕГРЮЛ |

**SAFE UNKNOWN:** юридически достаточный минимум для отрасли — **не** определён в v1; решает оператор + HITL.

---

## Связь с extraction

1. Оператор кладёт файлы в `project-input/legal-entity/`.
2. Agent/оператор извлекает поля по [LEGAL-ENTITY-EXTRACTION-GUIDE-v1.md](LEGAL-ENTITY-EXTRACTION-GUIDE-v1.md).
3. Результат — **только** Legal Entity Card.

---

## SAFE UNKNOWN

- Git LFS для крупных PDF — **per project**; не стандартизировано в reference v1.
- Шифрование at-rest для `project-input/` — **не** описано в Website Factory v1.

---

*Standard version: v1. Canonical location: `workspaces/website-factory-reference-v1/legal-entity/`.*
