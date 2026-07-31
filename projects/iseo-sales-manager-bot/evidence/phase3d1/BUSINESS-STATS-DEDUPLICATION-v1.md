# BUSINESS-STATS-DEDUPLICATION-v1

**Phase:** 3D.1  
**Surface:** Admin.dev `/stats`

## Problem

Retry/flood incident created many CLEAN rows for one Gmail message. Old `/stats` counted each row as `Всего заявок` / `Повторных обработок`, inflating business totals.

## Fix

Unique business identity = `gmail_message_id` || `source_message_id` || `lead_id`.

Production output shape:

```text
Статистика за 7 дней

Уникальных заявок: N
Новых: N
Повторных: N
Возможных повторов: N
Повторных обработок сообщений: N

Технических повторных попыток: N
Карточек доставлено: N
Ошибок обработки: N

Без ИИ: N
С ИИ: N
Использован шаблон: N
```

## Live acceptance (sanitized)

Observed after patch:

- Уникальных заявок: **2**
- Повторных обработок сообщений: **23**
- Технических повторных попыток: **22**
- Карточек доставлено: **2** (unique CLEAN identities; historical TG flood duplicates remain in evidence, not as extra unique leads)
- Без ИИ / С ИИ / шаблон: AI OFF counts only

Historical incident rows were **not** deleted.
