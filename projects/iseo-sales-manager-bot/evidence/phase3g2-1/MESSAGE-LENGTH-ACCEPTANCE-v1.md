# Message-length acceptance — Phase 3G.2.1

Telegram limit: **4096** characters per message.

| Surface | Length | Split? |
|---------|-------:|--------|
| Admin `/help` | 2344 | no |
| Moderator `/help` | 799 | no |
| Admin `/start` | 401 | no |
| Moderator `/start` | 331 | no |
| Admin `/config` | 362 | no |

Split helper exists in Help footer for >4096 (parts: leads+profiles / reminders+system+AI / users+settings) but is **inactive** at current lengths.
