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
8. **Качество** (human label only — do not duplicate the label in a trailing comment)
9. **Не хватает** (missing fields; omit when empty)
10. **Следующий шаг** (manager_recommendation)

For complete leads (quality ok, contact present), prefer service-aware guidance:

- Audit → `Связаться с клиентом и уточнить детали аудита.`
- SEO → `Связаться с клиентом и уточнить задачи по продвижению.`
- Other → `Связаться с клиентом и уточнить задачу.`

Do **not** use tautological wording such as `Можно готовить следующий шаг.`
Preserve missing-data / no-contact guidance when fields are incomplete.
11. **Уточняющие вопросы**
12. **История** (only if repeat/possible/reprocessed; human Russian text only)
13. **Режим обработки** (Без ИИ / С ИИ / ИИ не сработал, использован шаблон)
14. **Готовый ответ клиенту** (copy-ready; or no-contact notice when reply cannot be formed)

Optional footer in **development synthetic** cards only: `Тестовая заявка · PHASE 3B.3`  
Production cards: **no** synthetic footer / hashtags.

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
| `ok` | Данных достаточно |
| `needs_data` | Нужны уточнения |
| `poor` | Слабые данные |
| `unusable` / `bad` | Недостаточно для связи |
| `ai_off` / template | Без ИИ |
| `ai_on` / ai | С ИИ |
| `ai_fallback` / fallback | ИИ не сработал, использован шаблон |

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
──────── Ответ клиенту ────────

...text...

───────────────────────────────
Ответ клиенту автоматически не отправляется.
```

- No-contact / empty reply:

```
Готовый ответ не сформирован: нет контактных данных для связи.
Ответ клиенту автоматически не отправляется.
```

- Do not use raw Markdown fences.
- Do not expose match keys, lead IDs, dedupe keys, or technical enums in История.

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

- Raw enums: `UNKNOWN`, `ok`, `Audit` as code, `ai_status=…`, `match=`, `prior=`
- Raw AI JSON
- OpenRouter / credential hints
- Full Gmail message id unless truncated support footer
- `#ERROR!`
- ISO-8601 history strings as the only history line
- Synthetic hashtags (`#leadmsgsyn`, `#lead_msg_syn`, `#lead_…`)
- “Менеджер свяжется с вами” when no usable contact exists
- Duplicate quality labels (`Качество: X — X`)

---

## 7. Destination

- Manager cards → `telegram_manager_chat_id`
- Admin command replies → admin chat / requesting user per Admin contract
- Never client Telegram/email auto-send

---

*Related: AI-OFF-ON-CONTRACT-v1 · LEAD-DATA-MODEL-v1 · ADMIN-COMMAND-CONTRACT-v1 · Phase 3B.3 evidence.*

---

## 8. Phase 3D.3 — `sm-msg-v2` (emoji indicators, copy blocks, inline actions)

**CONFIG `message_format_version` = `sm-msg-v2`.**

### 8.1 Emoji indicators

Primary indicator sits in the card title only; avoid stacking multiple emoji per line.

**Lead type:** 🟢 Новый лид · 🟡 Повторный лид · 🟠 Возможный повтор (сайт) · 🔵 Повторная обработка  
**Lifecycle:** 🕓 Ожидает обработки (pending) · ✅ Обработан (processed) · 🚫 Спам (spam)  
**System:** ✅ success · ⚠️ warning · ❌ error · ℹ️ info · ⚙️ service · 🤖 AI · 📊 stats · 📋 config · 📨 Gmail · 📁 archive

### 8.2 Copy-friendly fields and reply block (`parse_mode=HTML`)

- Contact fields (name / phone / email / messenger / site), when present, render as separate `<code>` inline blocks so managers can tap-to-copy a single value without selecting surrounding text.
- The prepared client reply renders as a single `<pre>` block placed after a manager-only instruction line — copying it yields **only** client-facing text (no internal labels leak into the copied string).
- Tap-to-copy on `<code>`/`<pre>` is a current Telegram mobile/desktop client behavior; long-press copy remains the fallback where tap-to-copy is unavailable.
- Truncation (long cards) prefers preserving manager-facing sections over the reply block.

### 8.3 Inline lifecycle buttons (lead cards only)

Actionable **pending** lead cards carry two inline buttons: **✅ Отметить обработанным** and **🚫 Отметить как спам**. Callback data is an opaque per-lead token (`sm:p:<token12>` / `sm:s:<token12>`) — no PII, no raw `lead_id` in the visible button. Archive, admin, and service cards carry **no** lifecycle buttons. After a successful action the source card message is edited (buttons cleared) rather than a new message sent; see [ADMIN-COMMAND-CONTRACT-v1.md](ADMIN-COMMAND-CONTRACT-v1.md) §7 for callback routing and idempotency.

### 8.4 Forbidden (unchanged, reasserted for 3D.3)

No opaque token collisions surfaced as PII; no raw `lead_id`/dedupe keys in button labels or answer toasts; no automatic client-facing send triggered by a manager button.

### 8.5 Phase 3D.3.1 — invalid contact suppression + archive multi-card

- Never render Sheets formula errors or placeholders (`#ERROR!`, `#VALUE!`, `#REF!`, `#N/A`, `Formula parse error`, `UNKNOWN`, bare `44`) as phone/email/messenger/site.
- Omit the invalid field; archive cards may show `⚠️ Контакт в архивной записи повреждён` when useful.
- `/leads` must emit **one Telegram message per selected archive card** with correct ordinals; do not collapse to the first item.
- Archive footer: `ℹ️ Архивная копия. Статус меняется только в исходной карточке.`
