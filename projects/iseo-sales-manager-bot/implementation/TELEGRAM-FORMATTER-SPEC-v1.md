# TELEGRAM FORMATTER SPEC v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A  
**Format:** plain text **or** safe HTML — **not** fragile MarkdownV2 unless MetaBOT evidence later proves required  
**Authority:** TELEGRAM-UX-CONTRACT-v1 + Phase 3A operator maps

**Phase 3B.2 accepted runtime setting:** Telegram send nodes use `parse_mode=HTML`. This closes the observed Markdown underscore/entity failure mode; dynamic card and Admin text must remain HTML-escaped.

---

## 1. Rendering maps (Russian)

| Internal | Manager card |
|----------|--------------|
| `new` | новый / Новый лид |
| `repeat` | повторный / Повторный лид |
| `possible` | возможный повтор / Возможный повтор (сайт) |
| `reprocessed` | повторная обработка сообщения / Повторная обработка |
| `ok` | данных достаточно / Данных достаточно |
| `needs_data` | нужно уточнение / Нужны уточнения |
| `poor` | слабые данные / Слабые данные |
| `unusable` / `bad` | недостаточно данных / Недостаточно для связи |
| `ai_off` / template path | без ИИ / Без ИИ |
| `ai_on` / ai | с ИИ / С ИИ |
| `ai_fallback` | ИИ не сработал, использован шаблон |
| `Audit` | Аудит |
| `SEO` | SEO |
| `Direct` | Директ |
| `Site` | Сайт |
| `Other` | Другое |

Empty → `—`.

**Phase 3B.3:** do not append a quality comment that repeats the quality label. Render missing fields on a separate `Не хватает:` line.

---

## 2. Card block order

1. Header (duplicate class)  
2. Клиент  
3. Контакты  
4. Сайт  
5. Услуга  
6. Источник  
7. Кратко  
8. Чего не хватает  
9. Качество  
10. Следующий шаг  
11. Уточняющие вопросы  
12. История (if repeat/possible/reprocessed)  
13. Режим обработки  
14. Готовый ответ клиенту (copy-ready separators)  
15. Manual-send notice  
16. Optional truncated `lead_id` footer

### Separation rule

- Blocks 1–13 = **internal manager information**.  
- Block 14 = **copy-ready client reply only** (no internal notes).  
- Never auto-send block 14 to client channels.

Separators (Phase 3B.3):

```
──────── Ответ клиенту ────────

...
───────────────────────────────
Ответ клиенту автоматически не отправляется.
```

No-contact:

```
Готовый ответ не сформирован: нет контактных данных для связи.
Ответ клиенту автоматически не отправляется.
```

Development synthetic footer only: `Тестовая заявка · PHASE 3B.3`  
Production: no synthetic footer / hashtags.
---

## 3. Synthetic examples

### 3.1 AI OFF — unnamed Audit

```
Новый лид

Клиент: —
Контакты: +79001234567 (телефон)
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

### 3.2 AI ON — named SEO with site

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

### 3.3 Repeat phone lead

```
Повторный лид

Клиент: Мария
Контакты: +79007654321 (телефон)
Сайт: shop.ru
Услуга: Директ
Источник: форма

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

### 3.4 Same site, different contact

```
Возможный повтор (сайт)

Клиент: Пётр
Контакты: petr@example.com (email)
Сайт: shop.ru
Услуга: SEO
…

История:
Возможное совпадение по сайту · прошлый лид … · другой контакт

Режим обработки: Без AI
```

(Must still deliver card; not suppressed.)

### 3.5 AI fallback

```
Новый лид
…
Режим обработки: AI недоступен → шаблон
…
```

(Deterministic summary/reply; no stack traces.)

### 3.6 Telegram failure diagnostic (Admin `/last_error` / health)

```
Last error

code: tg_send
stage: Send Telegram Lead Card
lead: lead_synth_001
ts: 30.07.2026 12:41
workflow: Operational.dev
note: CLEAN записан; PROCESSED не ставился; incoming сохранён
```

No secrets, no raw webhook URLs, no customer dump beyond synthetic ids.

---

## 4. Forbidden in manager card

Raw enums as codes · raw AI JSON · credentials · `#ERROR!` · ISO history · “Ответ пока не сформирован” when template fills reply · client auto-send language.

---

## 5. Destination

Manager cards → `telegram_manager_chat_id` / `<MANAGER_CHAT_ID>`  
Admin replies → admin chat / requesting user  
Never client Telegram/email auto-send.

---

*Related: TELEGRAM-UX-CONTRACT-v1 · OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.*
