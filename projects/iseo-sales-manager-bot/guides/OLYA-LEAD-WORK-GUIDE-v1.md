# Руководство Оли — работа с лидами (v1)

**Статус доступа (Phase 3H.2):** активный модератор · имя в ответах клиенту — **Оля**.

## Что присылает бот

В личный чат приходит карточка заявки с контактом и блоком **✉️ Ответ клиенту**.

## Как читать карточку

1. Посмотрите имя клиента, контакт, сайт/услугу и комментарий.
2. Готовый первый ответ уже персонализирован: `Меня зовут Оля, компания INTLSEO.`
3. Скопируйте ответ и отправьте клиенту **вручную** (бот клиенту сам не пишет).

## Кнопки

- `✅ Обработано` — после того, как связались с клиентом.
- `🚫 Спам` — если заявка мусорная/нецелевая.
- Статус общий на всю команду; повторный клик безопасен (идемпотентность).

## Команды

- `/start` · `/help` · `/my_status` · `/my_reply_profile`
- `/pending_count` · `/pending_leads` — что ещё ждёт обработки
- `/leads` — архивные карточки
- `/lead_history <номер>` — история по номеру из `/leads`
- `/reminder_status` — статус ежедневных напоминаний (без права менять настройки)

## Напоминания

Если есть необработанные заявки, около **10:00 МСК** бот может напомнить. Это не новые заявки.

## Если ответ выглядит странно

Не отправляйте клиенту. Напишите Андрею. Не обещайте сроки, цены и «гарантии в топ».

## Ошибки бота

Сообщите Андрею: что увидели, время (МСК), текст команды/кнопки. Не пересылайте секреты и чужие чаты.


### Phase 3H.7

See evidence/phase3h7 and architecture/LEAD-REOPEN-CONTRACT-v1.md. Soak interrupted pending Gmail reauth + missed-lead recovery. Reopen: processed|spam -> pending via sm:r:.



## Phase 3H.7.1 note
Gmail OAuth recovery closed; original terminal cards now expose `↩️ Вернуть в обработку`; MISSED_PROD_LEAD_1 resolved without replay (no absent genuine form lead); soak restarted; Phase 3I.1 blocked.

## Phase 3H.7.2 note
Callback acknowledgement contract `iseo-lead-callback-ack-v1.0` deployed. Reopen ack is «Лид возвращён в обработку.». Aggregate no longer maps pending applied→processed. Operator-approved resurface of three genuine leads completed for acceptance; global reopen still does not fan out. Soak restarted; Phase 3I.1 blocked. See `evidence/phase3h72/`.
