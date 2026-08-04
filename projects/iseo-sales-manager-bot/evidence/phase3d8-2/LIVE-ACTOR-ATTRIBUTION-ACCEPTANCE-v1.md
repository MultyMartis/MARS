# LIVE ACTOR ATTRIBUTION ACCEPTANCE v1

## Patch evidence

Admin.dev wLrLp4WQHm1VJmxz patched in place (59 nodes). Markers verified live:

- actor_display_snapshot present in Handle Callback Action
- ACCESS_CONTROL access_display_name / access_username exported from Check User Authorization

## Operator-confirmed live results (2026-08-05)

Operator intentionally used inverted action assignment vs original instructions (stronger cross-role evidence).

### Synthetic Lead A — Admin → Spam

- Actor: Андрей (admin / active)
- Final: `🚫 Спам` + safe `Кем:` (display name · @username)
- Durable feedback: `Лид отмечен как спам.`
- Callback completed; buttons removed

### Synthetic Lead B — Moderator → Processed

- Actor: Мопс (moderator / active)
- Final: `✅ Обработан` + safe `Кем:` matching ACCESS_CONTROL
- Callback completed

## Matrix

| Check | Result |
|-------|--------|
| Admin actor attribution | PASS |
| Moderator actor attribution | PASS |
| Display-name + username precedence | PASS |
| Processed / spam transitions | PASS |
| Callback acknowledgement + durable feedback | PASS |
| Actor snapshot | PASS |
| No raw IDs on cards | PASS |
| No client messages / no new workflows | PASS |

## Closeout

**PHASE 3D.8.2 COMPLETE — ACTOR ATTRIBUTION AND REVOKED MODERATOR VISIBILITY READY**

See also `evidence/phase3d8-3/PHASE3D8-2-LIVE-CLOSEOUT-v1.md`.
