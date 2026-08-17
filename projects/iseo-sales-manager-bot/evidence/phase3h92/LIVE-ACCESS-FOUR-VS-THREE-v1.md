# LIVE ACCESS FOUR VS THREE — Phase 3H.9.2

Captured from Admin `Read ACCESS_CONTROL` exec `33554` (2026-08-17 15:49 Europe/Moscow) and confirmed on restore-day reads.

| Predicate | Before restore | After restore (exec `33573`) |
|---|---|---|
| ACCESS rows | 4 | 4 |
| Live staff (`admin\|moderator` + `active` + Telegram destination) | **3** | **4** |
| CONFIG `pending_reminder_active_recipients_count` | 4 | 4 |
| Operational resolver | 3 | 4 |
| Reminder resolver | 3 | 4 |

Do not treat CONFIG=4 as authority while ACCESS live was 3. ACCESS_CONTROL is SoT.
