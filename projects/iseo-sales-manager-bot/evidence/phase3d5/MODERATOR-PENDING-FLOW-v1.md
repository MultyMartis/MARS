# MODERATOR PENDING FLOW v1

1. Unknown user `/start` → ACCESS_CONTROL row role=public status=pending (upsert by telegram_user_id).
2. Refresh username / last_seen_at; preserve first_seen_at.
3. No automatic Admin notification storm on repeated `/start`.
4. Admin `/moderator_pending` lists bounded pending with opaque **Код заявки**.
5. Empty state: `Новых заявок на рабочий доступ нет.`
