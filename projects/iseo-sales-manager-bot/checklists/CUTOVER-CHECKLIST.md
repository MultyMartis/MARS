# Cutover Checklist

- [ ] Confirm production n8n host.
- [ ] Confirm exactly which workflows will be active.
- [ ] Confirm inactive reference/legacy workflows remain inactive.
- [ ] Confirm credentials exist in n8n and no secret values are copied to docs.
- [ ] Confirm CONFIG keys for AI, reminders, timezone, and authorization.
- [ ] Confirm persistence target and backup/export posture.
- [ ] Confirm Gmail full body fetch.
- [ ] Confirm RAW and CLEAN writes on safe test input.
- [ ] Confirm Telegram card delivery.
- [ ] Confirm `✅ Обработано` callback.
- [ ] Confirm `🚫 Спам` callback.
- [ ] Confirm `📄 Исходная заявка` callback.
- [ ] Confirm reminder schedule gate without forcing natural acceptance.
- [ ] Confirm events/errors are observable.
- [ ] Confirm rollback action: deactivate new workflow or restore prior active workflow.
- [ ] Record evidence and operator acceptance.

