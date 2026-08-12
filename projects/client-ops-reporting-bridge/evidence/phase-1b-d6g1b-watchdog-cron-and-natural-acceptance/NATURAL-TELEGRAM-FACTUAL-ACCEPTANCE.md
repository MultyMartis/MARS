# Natural Telegram Factual Acceptance

## Operator-visible messages

| Local (+07) | Claim | Server evidence |
|---|---|---|
| 2026-08-08 12:00 | ⚠️ Импорт 1С выполнен не полностью; catalog OK; no offers0 | terminal `OFFERS_INPUT_MISSING`; import0 present; offers inventory empty; dispatch SENT; DT SENT; n8n 25665 |
| 2026-08-09 12:00 | same | terminal/run `mars-20260809-080002-4eaac9f2`; n8n 26482 |
| 2026-08-10 12:00 | same | terminal/run `mars-20260810-080002-6b8c0191`; n8n 27299 |

## Additional reconciled natural days (ledger/n8n; Telegram not separately pasted by operator)

- 2026-08-11 and 2026-08-12: same `OFFERS_INPUT_MISSING` terminal + SENT dispatch + distinct event_id + n8n success

## Inbox filesystem

- `import0_1.xml` present under `public_html/1c_incoming/webdata/`
- `offers0_*.xml` **absent** in find window

## Classification

`OFFERS_INPUT_MISSING` — **not** a reporting defect. Upstream 1C offers exchange condition.

Message contract matches accepted Client Ops attention template.

Gate: `D6G1B_NATURAL_TELEGRAM_REPORTS_FACTUALLY_ACCEPTED`
