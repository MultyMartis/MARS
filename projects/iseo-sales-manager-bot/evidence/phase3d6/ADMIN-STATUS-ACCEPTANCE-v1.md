# ADMIN STATUS ACCEPTANCE v1

## Контракт
Единственный активный Admin в ACCESS_CONTROL (Андрей) получает:

```text
Ваш статус

Роль: администратор
Статус: активен

Доступны административные команды и управление модераторами.
```

При техническом сбое чтения ACCESS_CONTROL допустим только recovery-only Admin bootstrap для ограниченного набора команд, включая `/my_status`; он не даёт полномочий модератору и не отменяет explicit revoked/blocked записи.

## Результат
Harness case 04 (`admin_my_status`) PASS. Registry read подтвердил одного active Admin без публикации raw Telegram ID.
