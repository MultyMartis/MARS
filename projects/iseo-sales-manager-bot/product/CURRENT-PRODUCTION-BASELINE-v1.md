# CURRENT PRODUCTION BASELINE v1

**Срез:** Phase 3F.1, 2026-08-05. **Статус:** `COMPLETE — COMMANDS AND REMINDER ENGINE READY; OPERATOR ACTIVATION PENDING`. Phase 3E.2 закрыт операторским подтверждением (`PHASE 3E.2 COMPLETE — HUMAN FIRST REPLY ENGINE READY`); pending-команды и reminder-движок реализованы; reminders выключены по умолчанию; AI OFF.

| Контур | Workflow ID | Active | Nodes | Роль |
|---|---|---:|---:|---|
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | — | rollback; не активировать без отдельного решения |
| i-SEO Sales Manager - Operational.dev | `[external]` | true | 45 | unchanged in 3F.1; `minutesInterval=2`; single-flight 4m; bounded ledger/access/claim retries; AI OFF |
| i-SEO Sales Manager - Admin.dev | `wLrLp4WQHm1VJmxz` | true | 79 (было 59) | `message` + `callback_query`, ACCESS_CONTROL, actor attribution, archive commands, pending-lead view (3F.1), daily reminder engine (3F.1) |

## CONFIG

`environment=production`; `ai_enabled=false`; `parser_version=sm-parser-v3.3`; `message_format_version=sm-msg-v2.4`; `reply_template_version=sm-reply-v2.1`; `human_reply_style_version=sm-human-v1.0`; semantic model `lead-semantic-v1`; `pending_reminder_version=sm-pending-reminder-v1.0`; `pending_reminders_enabled=false`; `pending_reminder_time=10:00`; `pending_reminder_timezone=Europe/Moscow`.

## Доступ

Наблюдалось без идентификаторов: active admin — 1; active moderator — 1; revoked moderators — 2. Отзыв намеренный; Olya/Nikita не восстановлены.

## Parser / reply / card baseline (3E.1 + 3E.2)

- Lead Semantic Model: website states, intent precedence, comment boundary.
- First Reply Engine v2.1 + Human Reply Style v1: silent known-info guard; meaningful comment branching; quality linter; natural Оля drafts.
- Delivery fail-closed reconciliation (3E.2.1/3E.2.2): ledger read error → zero sends; claim-before-send; ACCESS_CONTROL fail-closed; Expand poison-guard; no blind resend.
- Pending action captions: **`✅ Обработано`** / **`🚫 Спам`** (final **`✅ Обработан`** unchanged).
- Callbacks unchanged: `sm:p:<token12>` / `sm:s:<token12>`.
- Phase 3E.2.3 harness **83/83 PASS**; live proof: claims=2, sendOk=2, delivered stamps=2, five-poll extra sends=0. Operator visual confirmation remains pending.
- OpenRouter disabled; AI OFF; новые workflows не создавались.

## Prior 3D.8.x

Actor attribution (3D.8.2) and short button labels (3D.8.3) remain in force.

## Git baseline

Phase 3E.1 sync worktree `mars/iseo-sm-phase3e1-parser33`. Main workspace may contain foreign WIP — selective staging only.

## Sheets call-budget baseline (3E.2.3)

Empty poll BEFORE: one CONFIG write every 30 seconds (about 120/hour). AFTER live proof: zero Sheets writes on three empty polls. Full proof used one CONFIG snapshot, one ACCESS_CONTROL snapshot, one bounded ledger item, two claims and two delivered stamps. Final schedule: `minutesInterval=2`.

## Pending leads + daily reminder baseline (3F.1)

- Admin.dev gained a read-only pending-lead view (`/pending_count`, `/pending_leads`, `/pending_leads_test`) and a daily reminder engine (`/reminder_status`, `/reminder_on`, `/reminder_off`, `/reminder_time`, `/reminder_timezone`, `/reminder_min`) behind an internal 15-minute Schedule Trigger — not a new workflow.
- Pending resolution: `manager_status` primary, `lifecycle_status` secondary, legacy rows without either default to pending unless closed.
- New additive Sheets tab: `REMINDER_DELIVERIES` (no existing tab schema changed).
- Offline harness `73/73 PASS` (`evidence/phase3f1/HARNESS-RESULTS-v1.md`).
- Controlled reminder live exercise reached ACCESS_CONTROL and correctly failed closed under a Sheets quota condition — zero sends; production reminders remain `enabled=false`.
- Access unchanged: active admin (Андрей), active moderator (Мопс); Оля/Никита remain revoked.
