# CURRENT PRODUCTION BASELINE v1

**Срез:** Phase 3E.2.3, 2026-08-05. **Статус:** `COMPLETE — EXACTLY-ONCE PROOF DELIVERED; OPERATOR VISUAL CONFIRMATION PENDING`. Sheets call-budget live proof PASS; Human Reply Style operator-accepted; AI OFF.

| Контур | Workflow ID | Active | Nodes | Роль |
|---|---|---:|---:|---|
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | — | rollback; не активировать без отдельного решения |
| i-SEO Sales Manager - Operational.dev | `[external]` | true | 45 | active after quiet-window proof; `minutesInterval=2`; single-flight 4m; bounded ledger/access/claim retries; AI OFF |
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
- Phase 3E.2.3 harness **83/83 PASS**; live proof: claims=2, sendOk=2, delivered stamps=2, five-poll extra sends=0. Operator visual confirmation remains pending.
- OpenRouter disabled; AI OFF; новые workflows не создавались.

## Prior 3D.8.x

Actor attribution (3D.8.2) and short button labels (3D.8.3) remain in force.

## Git baseline

Phase 3E.1 sync worktree `mars/iseo-sm-phase3e1-parser33`. Main workspace may contain foreign WIP — selective staging only.

## Sheets call-budget baseline (3E.2.3)

Empty poll BEFORE: one CONFIG write every 30 seconds (about 120/hour). AFTER live proof: zero Sheets writes on three empty polls. Full proof used one CONFIG snapshot, one ACCESS_CONTROL snapshot, one bounded ledger item, two claims and two delivered stamps. Final schedule: `minutesInterval=2`.
