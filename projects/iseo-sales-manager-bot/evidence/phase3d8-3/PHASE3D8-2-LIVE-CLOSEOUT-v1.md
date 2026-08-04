# PHASE 3D.8.2 LIVE CLOSEOUT v1

## Verdict

`PHASE 3D.8.2 COMPLETE — ACTOR ATTRIBUTION AND REVOKED MODERATOR VISIBILITY READY`

## Operator approval

Operator confirmed Phase 3D.8.2 live actor-attribution acceptance succeeded (2026-08-05).

## Access state (unchanged)

| Actor | Role | Status |
|-------|------|--------|
| Андрей | admin | active |
| Мопс | moderator | active |
| Оля | moderator | revoked (intentional) |
| Никита | moderator | revoked (intentional) |

No role restores. No ACCESS_CONTROL mutations in this closeout packet.

## `/moderator_pending` revoked section

| Check | Result |
|-------|--------|
| Revoked section live PASS | PASS (operator-confirmed; prior runtime formatter+live rows PASS) |
| Оля visible with stable code | PASS |
| Никита visible with stable code | PASS |
| Roles unchanged | PASS |
| `/moderators` active-only | PASS (regression preserved) |

## Actor attribution — real actions

Operator intentionally inverted the original action assignment (stronger cross-role evidence):

### Synthetic Lead A

- Actor: Андрей (Admin / active)
- Action: Spam
- Final card: `🚫 Спам` + `Кем: Андрей Русецкий · @<redacted>`
- Callback completed; durable feedback `Лид отмечен как спам.`
- **Admin spam attribution PASS**

### Synthetic Lead B

- Actor: Мопс (moderator / active)
- Action: Processed
- Final card: `✅ Обработан` + `Кем: Мопс · @<redacted>`
- Callback completed; attribution matched ACCESS_CONTROL
- **Moderator processed attribution PASS**

## Matrix

| Check | Result |
|-------|--------|
| Admin actor attribution | PASS |
| Moderator actor attribution | PASS |
| Display-name + username precedence | PASS |
| Processed transition | PASS |
| Spam transition | PASS |
| Callback acknowledgement | PASS |
| Durable feedback | PASS |
| Actor snapshot | PASS |
| Action buttons removed after transition | PASS |
| No duplicate deliveries observed | PASS |
| Safe names displayed (no raw IDs) | PASS |
| No client messages | PASS |
| No new workflows | PASS |

## Both recipient copies — honesty note

Operator confirmed final card text and feedback on the acted cards for both fixtures. Multi-copy edit/removal of buttons was previously proven in 3D.8.1 and remains in the Admin graph. **Independent runtime attachment of the second recipient copy for each of these two specific 3D.8.2 fixtures was not separately re-exported in this closeout packet** — recorded as operator-attested on the acted copies; multi-copy sync contract unchanged.

## Contour at closeout

- Sales-Manager-v2 inactive
- Operational.dev `xSnXPy8cEHoZw6xG` active (45)
- Admin.dev `wLrLp4WQHm1VJmxz` active (59)
- AI OFF; parser `sm-parser-v3.2`; format `sm-msg-v2.2`
