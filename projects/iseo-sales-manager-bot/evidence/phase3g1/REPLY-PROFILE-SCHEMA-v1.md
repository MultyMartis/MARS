# REPLY PROFILE SCHEMA v1

Additive ACCESS_CONTROL fields — see architecture `REPLY-PROFILE-CONTRACT-v1.md`.

Sanitized example rows (no Telegram IDs):

| Label | reply_sender_name | enabled | access |
|-------|-------------------|---------|--------|
| ADMIN_A | Андрей | true | active admin |
| MOD_A | Михаил | true | active moderator |
| (prepared) Оля | Оля | prepared | revoked — not recipient |
| (prepared) Никита | Никита | prepared | revoked — not recipient |

Validation rejects display/username fallbacks and full-name auto-shorten.
