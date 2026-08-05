# MODERATOR HELP ACCEPTANCE v1

## Template

Moderator `helpReply('moderator')` includes:

- `/start`, `/my_status`
- `/leads` (3/5/10)
- `/lead_history <номер>`
- `/pending_count`, `/pending_leads`, `/reminder_status`
- short card/lifecycle guidance

## Authorization safety

| Must not advertise | Result |
|---|---|
| `/config` | PASS (absent) |
| `/moderator_add` / user-admin commands | PASS (absent) |
| `/ai_on` / `/ai_off` | PASS (absent) |
| `/reminder_on` and other reminder config | PASS (absent) |

Staff pending/history commands remain authorized by `STAFF_PENDING_COMMANDS` in Check User Authorization (unchanged this phase).

## Sample

`help-moderator.sample.txt`
