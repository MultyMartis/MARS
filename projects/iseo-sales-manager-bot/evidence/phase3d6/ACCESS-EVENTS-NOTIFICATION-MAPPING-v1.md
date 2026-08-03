# ACCESS EVENTS NOTIFICATION MAPPING v1

| Операция | Delivery | ACCESS_EVENTS event | outcome |
|---|---|---|---|
| grant | delivered | `moderator_grant_notification_sent` | `ok` |
| grant | failed | `moderator_grant_notification_failed` | `failed` |
| revoke | delivered | `moderator_revoke_notification_sent` | `ok` |
| revoke | failed | `moderator_revoke_notification_failed` | `failed` |

Append ACCESS_EVENTS Notify берёт подготовленные поля notification event и сохраняет only opaque subject/actor references, role/status transition, source `telegram_notify`, outcome и безопасную detail. ACCESS_CONTROL mutation и access decision events остаются отдельными фактами.

Structural patch подтверждает наличие узла **Append ACCESS_EVENTS Notify**; harness notification cases PASS.
