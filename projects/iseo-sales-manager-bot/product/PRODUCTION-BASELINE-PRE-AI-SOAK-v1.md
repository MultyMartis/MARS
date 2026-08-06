# PRODUCTION BASELINE PRE-AI SOAK v1

**Date/time (attempt 1):** 06.08.2026 14:20 МСК — **INVALIDATED** by Phase 3H.4  
**Soak restart T+0:** 2026-08-06 19:15 Europe/Moscow · earliest PASS 2026-08-08 19:15 Europe/Moscow

| Contour | ID | Active | Nodes |
|---|---|---:|---:|
| Operational.dev | xSnXPy8cEHoZw6xG | true | 45 |
| Admin.dev | wLrLp4WQHm1VJmxz | true | 85 |
| Sales-Manager-v2 | h8I2Tl2yl4uzhUnB | false | 19 |

- Parser: sm-parser-v3.3
- Templates: iseo-first-contact / template-set v1
- Personalization: iseo-recipient-name-v1.1
- Resolver: iseo-reply-profile-resolver-v1.0
- Active profiles: 1 Андрей, 2 Оля, 3 Михаил
- Revoked: 4 Никита
- Reporting mode: manual
- Reminders: ON 10:00 Europe/Moscow
- Stats epoch: 05.08.2026 16:02 МСК · received=1 pending=0 processed=1 spam=0
- AI OFF · automatic client send OFF
- Rollback backups: Storage `git-sync-iseo-sm-phase3h-20260806-175957\runtime\backups\`
- Canonical tip at program start: `d76a68f7` (origin/mars/canonical-post-recovery)
- Phase 3H.4: observability repair — poll heartbeat `iseo-gmail-poll-heartbeat-v1.0`; `/status` production truth keys; evidence `evidence/phase3h4/`
