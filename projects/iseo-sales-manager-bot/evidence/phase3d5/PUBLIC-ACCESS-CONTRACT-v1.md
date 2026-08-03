# PUBLIC ACCESS CONTRACT v1

**Phase:** 3D.5  
**Status:** accepted (harness + structural live acceptance)

## Roles

| Role | Telegram surface |
|------|------------------|
| **public** | `/start`, `/help` only |
| **moderator** | public + manager start/help + processed/spam callbacks |
| **admin** | all moderator + Admin commands + moderator registry |
| **blocked** | `Доступ к боту ограничен.` |

## Public guarantees

- Bot is publicly reachable for informational commands.
- Public users never receive production/archive lead cards.
- Public users cannot use lifecycle callbacks.
- Public users do not see moderator/Admin lists, CONFIG internals, health, stats, or AI controls.
- Unknown privileged commands → `Команда доступна только сотрудникам с рабочими правами.`
- Unknown text → `Команда не найдена. Используйте /help.`

## Source of truth

**ACCESS_CONTROL** is the operational access registry.  
`admin_user_ids` remains emergency/bootstrap Admin authority.  
`manager_action_user_ids` is legacy migration fallback only when no ACCESS_CONTROL row exists.
