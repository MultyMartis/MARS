# AI MANAGER ASSIST v1

**Phase:** 3G.1  
**Version:** `manager_assist_version` = `iseo-manager-assist-v1.0`  
**Default:** AI OFF (`DETERMINISTIC_TEMPLATE`)  
**Status:** constrained contract documented; **not** globally enabled

## Role

AI assist (when someday enabled) может заполнять **только** structured manager-assist поля. Шаблон, CTA, имя отправителя и компания выбираются **до** AI и остаются immutable.

## Allowed AI fields (structured JSON only)

- `task_summary`
- `manager_note`
- `follow_up_after_positive_reply`
- `risk_flags`
- `confidence`

## Forbidden

- Rewrite of full customer message / CTA
- Change of sender name or company
- Guarantees, prices, deadlines, unsupported site-review claims
- HTML / injection artifacts
- Auto-send to customers

## Fallback

Любой validation reject → deterministic template path. Delivery лида не блокируется.

## Production posture

- `ai_enabled=false`
- Harness: provider calls = 0
- Live AI ON pilot requires separate charter (roadmap item)

## Phase 3G.2 note

AI assist still **OFF**. User-visible AI strings follow [TELEGRAM-TEXT-CONTRACT-v2.md](TELEGRAM-TEXT-CONTRACT-v2.md). Sender name / company remain immutable even if assist is later enabled — never derived from Telegram nicknames. Profile addressing is by number; access roles unchanged by name commands.

## Related

- [implementation/AI-ASSIST-VALIDATOR-v1.md](../implementation/AI-ASSIST-VALIDATOR-v1.md)
- Evidence: `AI-OFF-ACCEPTANCE-v1.md`, `AI-ASSIST-CONTRACT-v1.md`, `AI-VALIDATION-v1.md`
- Phase 3G.2 stub: `evidence/phase3g2/AI-TEXT-ACCEPTANCE-v1.md`
