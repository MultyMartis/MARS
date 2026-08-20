# DIGEST RENDERER PROOF — Phase 3H.10

Contract: `iseo-pending-digest-renderer-v1.0`

Harness results:

```json
{
  "zero_skip": true,
  "one_total": 1,
  "one_buttons": 1,
  "multi_total": 8,
  "multi_body_len": 413,
  "multi_under_budget": true,
  "multi_has_categories": true,
  "no_phone_email": true,
  "no_raw_lead_ids": true,
  "dup_button_tokens_unique": true,
  "overflow_true": true,
  "overflow_buttons_le_cap": true,
  "has_all_pending_button": true,
  "mapping": {
    "audit": "Аудит",
    "seo": "SEO",
    "ads": "Реклама",
    "website": "Разработка сайта",
    "other": "Другое",
    "empty": "Требует уточнения"
  },
  "compact_pending_has_status": true,
  "compact_spam_truthful": true,
  "button_cap": 25
}
```

Body sample (sanitized aliases):

```
🔔 Необработанные лиды — 8

На 10:00 МСК
Самый старый: 4 дня

🔍 Аудит — 2
• A1 · Irina · ⚠️ 4 дня
• A2 · Alexander · ⚠️ 3 дня

📈 SEO — 2
• A3 · Dmitry · 2 дня
• A7 · Viktor · сегодня

📣 Реклама — 1
• A8 · example.ru · сегодня

🌐 Разработка сайта — 1
• A6 · Anna · 1 день

📦 Другое — 1
• A4 · Лид без имени · 2 дня

❓ Требует уточнения — 1
• A5 · Лид без имени · 2 дня

Всего: 8 · сегодня: 2 · старше суток: 6
```
