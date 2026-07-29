# TELEGRAM UX CONTRACT v1

**Product:** i-SEO Sales Manager Bot  
**Audience:** managers (Оля v1)  
**Format:** safe plain text **or** carefully escaped HTML — **not** fragile Markdown

---

## 1. Goals

- One scannable card per processed lead.
- Human Russian labels only.
- Copy-ready first reply block.
- Clear new / repeat / reprocessed.
- No technical enums, ISO dumps, raw AI JSON, credentials, or internal stack traces.

---

## 2. Required blocks (order)

1. **Header** — Новый лид / Повторный лид / Повторная обработка
2. **Клиент**
3. **Контакты**
4. **Сайт**
5. **Услуга**
6. **Источник** (source + page + campaign if present)
7. **Кратко** (summary)
8. **Чего не хватает** (missing)
9. **Качество** (human label + short comment)
10. **Следующий шаг** (manager_recommendation)
11. **Уточняющие вопросы**
12. **История** (only if repeat/possible/reprocessed)
13. **Режим обработки** (Без AI / AI / AI→резерв)
14. **Готовый ответ клиенту** (copy-ready; fenced by clear separators)

Optional footer: `lead_id` short form for support (monospace HTML if HTML mode).

---

## 3. Label maps

| Internal | Telegram |
|----------|----------|
| `new` | Новый лид |
| `repeat` | Повторный лид |
| `reprocessed` | Повторная обработка |
| `possible` | Возможный повтор (сайт) |
| `Audit` | Аудит |
| `SEO` | SEO |
| `Direct` | Директ |
| `Site` | Сайт |
| `Other` | Другое |
| `ok` | Данные в порядке |
| `needs_data` | Нужны уточнения |
| `poor` | Слабые данные |
| `unusable` | Недостаточно для связи |
| `ai_off` | Без AI |
| `ai_on` | AI |
| `ai_fallback` | AI недоступен → шаблон |

Empty values → `—` (not `UNKNOWN`, not blank multi-newlines).

---

## 4. Formatting rules

- Prefer **plain text** with blank lines between blocks.
- If HTML: escape `<`, `>`, `&`; use `<b>` sparingly; no nested entities that Telegram rejects.
- Do not use Markdown `*` `_` `` ` `` as primary (entity parse failures — MetaBOT lesson).
- Collapse multiple empty lines.
- Dates: `дд.мм.гггг чч:мм`.
- Reply block delimited:

```
——— Скопировать ответ клиенту ———
...text...
——— Конец ответа ———
```

- Explicit note under reply: `Отправляется только вручную. Бот клиенту не пишет.`

---

## 5. Examples

### 5.1 AI OFF — new lead without name

```
Новый лид

Клиент: —
Контакты: +7… (телефон)
Сайт: —
Услуга: Аудит
Источник: форма /audit · utm: yandex / cpc / brand

Кратко: Заявка на аудит без имени и сайта; указан телефон.

Чего не хватает: имя; сайт
Качество: Нужны уточнения — нет имени и сайта
Следующий шаг: Уточнить имя и сайт перед КП; использовать вопросы ниже.

Уточняющие вопросы:
1) Как к вам обращаться?
2) Укажите, пожалуйста, адрес сайта.

Режим обработки: Без AI

——— Скопировать ответ клиенту ———
Здравствуйте!

Спасибо, ваша заявка получена (запрос по аудиту сайта).
Менеджер свяжется с вами, чтобы уточнить задачу.

С уважением,
команда i-SEO
——— Конец ответа ———
Отправляется только вручную. Бот клиенту не пишет.
```

### 5.2 AI ON — new lead with site

```
Новый лид

Клиент: Иван
Контакты: ivan@example.com (email)
Сайт: example.ru
Услуга: SEO
Источник: форма /seo

Кратко: Интерес к продвижению example.ru; нужен контакт для брифа.

Чего не хватает: телефон
Качество: Данные в порядке — можно начинать диалог
Следующий шаг: Подтвердить получение; уточнить регион и текущий трафик.

Уточняющие вопросы:
1) Есть ли удобный телефон для связи?

Режим обработки: AI

——— Скопировать ответ клиенту ———
Здравствуйте, Иван!

Спасибо, ваша заявка получена (запрос по SEO).
Специалист свяжется с вами, чтобы уточнить задачу.

С уважением,
команда i-SEO
——— Конец ответа ———
Отправляется только вручную. Бот клиенту не пишет.
```

### 5.3 Repeat lead

```
Повторный лид

Клиент: Мария
Контакты: +7… · @maria
Сайт: shop.ru
Услуга: Директ
Источник: письмо

Кратко: Повторный интерес к Директу по shop.ru.

Чего не хватает: —
Качество: Данные в порядке
Следующий шаг: Сверить прошлую переписку; не начинать с нуля.

Уточняющие вопросы: —

История:
Был контакт 12.03.2026 14:20 · услуга SEO · кратко: Запрос по продвижению shop.ru

Режим обработки: Без AI
…
```

### 5.4 AI fallback

```
Новый лид
…
Режим обработки: AI недоступен → шаблон
…
```

(Use deterministic summary/reply; no error stack in card. Details go to ERRORS tab.)

---

## 6. Forbidden in manager card

- Raw enums: `UNKNOWN`, `ok`, `Audit` as code, `ai_status=…`
- Raw AI JSON
- OpenRouter / credential hints
- Full Gmail message id unless truncated support footer
- `#ERROR!`
- ISO-8601 history strings
- “Ответ пока не сформирован” when template always fills reply

---

## 7. Destination

- Manager cards → `telegram_manager_chat_id`
- Admin command replies → admin chat / requesting user per Admin contract
- Never client Telegram/email auto-send

---

*Related: AI-OFF-ON-CONTRACT-v1 · LEAD-DATA-MODEL-v1 · ADMIN-COMMAND-CONTRACT-v1.*
