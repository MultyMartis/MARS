# MODERATOR / ADMIN ROLE MATRIX v1

| Capability | public | moderator | admin | blocked |
|------------|--------|-----------|-------|---------|
| /start /help | yes (public text) | yes (manager text) | yes (admin text) | deny limited |
| Lifecycle callbacks | no | yes | yes | no |
| /leads /config /health /stats /ai_* | no | no | yes | no |
| /moderators* registry | no | no | yes | no |
| Lead cards with buttons | never | manager destination only | manager destination only | never |

Auth role strings in runtime: `public` | `moderator` | `admin` | `blocked`.
