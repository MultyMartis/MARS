# LIFECYCLE MUTATION CONTRACT v1

## Allowed transitions

- `pending` → `processed`
- `pending` → `spam`
- No reversal in this phase

## Win conditions

| Outcome | CLEAN | LEAD_EVENTS | Cards | Initiator text |
|---------|-------|-------------|-------|----------------|
| applied processed | 1 update | 1 transition | edit all copies | `Лид отмечен как обработанный.` |
| applied spam | 1 update | 1 transition | edit all copies | `Лид отмечен как спам.` |
| idempotent | no | no | converge/remove buttons | `Этот статус уже установлен.` |
| conflict | no | no | converge to current | `Статус лида уже изменён другим сотрудником.` |
| unknown lead | no | no | no | `Не удалось найти лид…` |
| storage fail | no | no | no | `Не удалось сохранить статус…` |
| unauthorized | no | no | no | `Недостаточно прав для изменения статуса.` |

## Isolation

Edit failure after successful CLEAN mutation does **not** roll back CLEAN/EVENTS; initiator gets partial-success text.
