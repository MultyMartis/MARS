# OPERATIONAL SINGLE-FLIGHT v1

**Phase:** 3E.2.3  
**Scope:** Operational.dev intake concurrency guard.

## Контракт

`Intake Gate` использует workflow static data как single-flight lock. При входе poll:

1. Проверить lock timestamp.
2. Если lock моложе 4 минут, завершить poll без обработки lead path и без Telegram send.
3. Если lock отсутствует или истёк, записать lock и продолжить.
4. Освободить lock на штатном завершении; TTL остаётся аварийным предохранителем.

## Параметры

- Schedule: `minutesInterval=2`; `secondsInterval=120` was rejected by n8n as invalid.
- Lock TTL: 4 minutes.
- Ownership: один Operational.dev execution.
- Storage: workflow static data; это runtime guard, не durable distributed lock.

## Failure semantics

- Lock ambiguity закрывает intake path для конкурирующего execution.
- Истёкший lock можно забрать только после TTL.
- Guard не заменяет claim-before-send и не доказывает exactly-once сам по себе.
- При restart/instance semantics точное поведение static data остаётся зависимым от n8n. No live overlap incident was observed; five post-proof polls produced zero resends.

## Наблюдаемость

Evidence должен фиксировать: schedule, TTL, overlap decision, lock acquire/release и отсутствие Telegram sends у blocked execution без публикации runtime identifiers.
