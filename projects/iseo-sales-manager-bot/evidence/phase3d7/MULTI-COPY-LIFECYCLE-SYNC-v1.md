# MULTI-COPY LIFECYCLE SYNC v1

When any active Admin/moderator marks processed/spam:

1. Validate lifecycle (pending → processed|spam).
2. Update CLEAN exactly once.
3. Append LEAD_EVENTS once.
4. Resolve delivered copies from LEAD_DELIVERIES.
5. Edit every known Telegram copy; remove buttons; show final status.
6. Record per-copy success/failure.

Callback initiator answer:

- success: `Статус лида сохранён.`
- partial card edit failure: `Статус сохранён. Не все копии карточки удалось обновить.`

Do not reveal which private users failed. Do not auto-resend full duplicate cards.
