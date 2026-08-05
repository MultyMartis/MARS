# ACCESS CONTROL SNAPSHOT v1

**Phase:** 3E.2.3  
**Purpose:** один fail-closed снимок eligibility на delivery cycle.

## Implementation contract

1. `Read ACCESS_CONTROL` выполняется один раз на полный lead path.
2. Результат нормализуется в snapshot до recipient expansion.
3. Snapshot содержит только поля, необходимые для active role/status eligibility; committed evidence не содержит Telegram IDs или PII.
4. Active admin/moderator recipients допускаются; revoked/blocked/public исключаются.
5. Read использует bounded retry 3 × 30s.
6. Любая техническая ошибка или poisoned output означает 0 cards; `continueOnFail` запрещён.

## Current sanitized state

Наблюдались две активные delivery-роли и две намеренно revoked записи. Персональные данные и идентификаторы в документ не включаются. Состояние доступа патчем 3E.2.3 не изменялось.

## Acceptance

Offline harness проверяет single read, fail-closed error и exclusion revoked. Live snapshot count/eligibility proof pending.
