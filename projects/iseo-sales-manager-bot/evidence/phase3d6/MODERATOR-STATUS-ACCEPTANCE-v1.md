# MODERATOR STATUS ACCEPTANCE v1

## Контракт
Активный moderator получает:

```text
Ваш статус

Роль: модератор
Статус: активен

Доступно:
— работа с карточками лидов;
— отметка «Обработан»;
— отметка «Спам».

Административные настройки недоступны.
```

Оля — active moderator. Тестовый модератор с opaque ref `u:518CC34C4C0F` также подтверждён как `moderator / active`. Роль определяет ACCESS_CONTROL; legacy `manager_action_user_ids` не является активным источником полномочий.

## Результат
Harness case 03 (`moderator_my_status`) и 20 (`moderator_help_my_status`) PASS; Admin registry read подтвердил итоговые состояния.
