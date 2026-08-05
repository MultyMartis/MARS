# CURRENT PRODUCTION BASELINE v1

**Срез:** Phase 3E.2.2, 2026-08-05. **Статус:** Parser 3.3 COMPLETE; First Reply Engine v2.1 + Human Reply Style v1; ACCESS_CONTROL fail-closed; isolated Sheets healthy; **ATTENTION — full dual-card path still Sheets rate-limited**; operator copy acceptance PENDING.

| Контур | Workflow ID | Active | Nodes | Роль |
|---|---|---:|---:|---|
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | — | rollback; не активировать без отдельного решения |
| i-SEO Sales Manager - Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 | sole Gmail intake; **`sm-parser-v3.3`**; **`sm-reply-v2.1`** + **`sm-human-v1.0`**; **`sm-msg-v2.4`**; multi-recipient; delivery fail-closed + ACCESS_CONTROL fail-closed (3E.2.2) |
| i-SEO Sales Manager - Admin.dev | `wLrLp4WQHm1VJmxz` | true | 59 | `message` + `callback_query`, ACCESS_CONTROL, actor attribution, archive commands |

## CONFIG

`environment=production`; `ai_enabled=false`; `parser_version=sm-parser-v3.3`; `message_format_version=sm-msg-v2.4`; `reply_template_version=sm-reply-v2.1`; `human_reply_style_version=sm-human-v1.0`; semantic model `lead-semantic-v1`.

## Доступ

Наблюдалось без идентификаторов: active admin — 1; active moderator — 1; revoked moderators — 2. Отзыв намеренный; Olya/Nikita не восстановлены.

## Parser / reply / card baseline (3E.1 + 3E.2)

- Lead Semantic Model: website states, intent precedence, comment boundary.
- First Reply Engine v2.1 + Human Reply Style v1: silent known-info guard; meaningful comment branching; quality linter; natural Оля drafts.
- Delivery fail-closed reconciliation (3E.2.1/3E.2.2): ledger read error → zero sends; claim-before-send; ACCESS_CONTROL fail-closed; Expand poison-guard; no blind resend.
- Pending action captions: **`✅ Обработано`** / **`🚫 Спам`** (final **`✅ Обработан`** unchanged).
- Callbacks unchanged: `sm:p:<token12>` / `sm:s:<token12>`.
- Local harness **59/59 PASS** (3E.2.2); dual-card live sendOk=2 **blocked by Sheets quota**; human copy packet ready; operator acceptance **PENDING**.
- OpenRouter disabled; AI OFF; новые workflows не создавались.

## Prior 3D.8.x

Actor attribution (3D.8.2) and short button labels (3D.8.3) remain in force.

## Git baseline

Phase 3E.1 sync worktree `mars/iseo-sm-phase3e1-parser33`. Main workspace may contain foreign WIP — selective staging only.
