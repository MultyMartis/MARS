# REMINDER OBSERVABILITY v1

On pre-decision ERROR the evaluator persists (when CONFIG write is possible):

- last_evaluation_at
- last_decision=`ERROR`
- last_error_class / last_error_stage / last_error_at
- retry_attempts
- business_date
- pending_count=`not_computed` if ACCESS/CLEAN did not complete

Not stamped: last_successful_send, sent_date, sent recipient count.

If CONFIG write is itself 429: `Append ERRORS Reminder 429` (`continueRegularOutput`) is the fallback. Do not pretend CONFIG was updated.

`/reminder_status` ERROR example semantics:

- Состояние: включены
- Время: 10:00
- Часовой пояс: Europe/Moscow
- Получателей: 4
- Последняя проверка: \<time\>
- Последнее решение: Ошибка
- Этап: ACCESS_CONTROL
- Причина: лимит Google Sheets API
- Повторные попытки: N
- Последняя успешная отправка: truthful or none

No secrets / raw Google payloads.
