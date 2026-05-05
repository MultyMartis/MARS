# SEO Content Agent — Telegram commands

**Status:** **specification** — command names and examples. Bot implementation is **not** in this repository.

**Convention:** Commands are shown with leading `/`. Argument style (reply chains vs inline JSON) is **SAFE UNKNOWN** until n8n design is fixed.

---

## `/outline`

**Description:** Generate an SEO outline / copywriter brief from a brief and optional sources.

**Usage (plan):** Send command followed by brief text and optional URLs on following lines.

**Example (Russian):**

```text
/outline
Тема: корпоративный портал для отдела закупок
Интент: коммерческий, B2B
Ключи: автоматизация закупок, единый каталог поставщиков
Аудитория: руководители закупок, средний+ бизнес
Ограничения: без цен и сроков внедрения — данных нет
Источники: (вставлю текст с сайта ниже)
...
```

---

## `/text`

**Description:** Write a full draft from an **approved** outline.

**Usage (plan):** Reference the approved outline (e.g. reply to outline message or pass `outline_id` if the bot supports it — **SAFE UNKNOWN**).

**Example (Russian):**

```text
/text
Используй утверждённый аутлайн из сообщения выше. Объём ~2500 знаков без пробелов. Тон: деловой, без воды.
```

---

## `/factcheck`

**Description:** Run fact-check on a draft.

**Usage (plan):** Reply to the draft message or paste `text_id`.

**Example (Russian):**

```text
/factcheck
Проверь черновик в ответ на это сообщение. Источники — только бриф и то, что я прикреплял к /outline.
```

---

## `/seoqa`

**Description:** SEO quality review (structure, intent, spam, FAQ).

**Example (Russian):**

```text
/seoqa
Оцени SEO-качество текста из предыдущего сообщения по чеклисту проекта.
```

---

## `/freshness`

**Description:** **Phase 6** — stale facts and outdated stats (**optional**; corpus required).

**Example (Russian):**

```text
/freshness
Проверь актуальность цифр и формулировок в тексте выше. Справочник фактов — таблица Facts_2026_Q2 (если подключена).
```

**Note:** Until freshness corpus exists, bot should respond with “not configured” — behavior **SAFE UNKNOWN** pre-implementation.

---

## `/help`

**Description:** Short help and links to internal docs (if configured).

**Example (Russian):**

```text
/help
```

**Expected reply (plan, illustrative):**

- Список команд: `/outline`, `/text`, `/factcheck`, `/seoqa`, `/freshness`, `/help`
- Напоминание: факты только из брифа и приложенных источников; не публиковать без проверки человеком.

---

## Error messages (plan)

| Situation | User-facing tone (example RU) |
|-----------|-------------------------------|
| Outline not approved | «Черновик статьи можно запросить только после утверждения структуры. Сначала согласуйте /outline.» |
| Missing evidence | «Недостаточно данных для проверки. Добавьте источник или уточните бриф (поля: …).» |
| Model failure | «Сервис генерации временно недоступен. Повторите позже или обратитесь к администратору.» |

---

## SAFE UNKNOWN

- Exact Telegram Bot API webhook layout, rate limits, and message length chunking.
- Whether inline keyboards are used for “Approve outline” / “Reject”.
