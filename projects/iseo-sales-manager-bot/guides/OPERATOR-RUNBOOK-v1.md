# Operator runbook — i-SEO Sales Manager (v1)

## Contour

- Operational.dev `xSnXPy8cEHoZw6xG` — Gmail → CLEAN → multi-recipient Telegram
- Admin.dev `wLrLp4WQHm1VJmxz` — commands + callbacks
- Sales-Manager-v2 must stay **inactive**

## Delivery health

- `/delivery_status` — counts
- `/delivery_users` — eligible recipients (no raw IDs)

## ACCESS_CONTROL

Primary authority for roles and delivery eligibility. Moderators need a prior private bot chat (`/start`).

## Incidents

If only one person receives leads: verify OPS Send nodes use `telegram_delivery_chat_id` and Expand Delivery Recipients is on the path after Format.

## Phase 3D.8 — missing action buttons

If a new pending card has no buttons, inspect Format output before changing Admin or Parser: `telegram_has_buttons` must be true, callback fields must be `sm:p:<token12>` / `sm:s:<token12>`, and `telegram_reply_markup` must survive recipient expansion and claim restore. `/leads` archive cards are intentionally buttonless. Keep AI OFF and do not restore revoked staff roles during diagnosis.

## Phase 3D.8.1 — action buttons visible but click feels stuck

1. Confirm Admin.dev active and Telegram Trigger includes `callback_query`.
2. Expect immediate toast `Обрабатываю…`; then durable reply + both card copies updated.
3. If only one card updates: check `LEAD_DELIVERIES` tab exists and has delivered rows for the lead.
4. Do not replay clicks on already-processed leads; use fresh synthetic markers for acceptance.
5. Acceptance cards: `PHASE_3D8_1_ADMIN_PROCESSED` (Андрей → processed) and `PHASE_3D8_1_MODERATOR_SPAM` (Мопс → spam) — **confirmed COMPLETE** in Phase 3D.8.1 closeout.

## Phase 3D.8.2 — attribution and revoked moderators

1. Final cards should show `Кем: <safe name>` from ACCESS_CONTROL (not generic `сотрудник` when display name exists).
2. `/moderator_pending` lists pending requests and **Права временно отозваны** with stable codes (Olya/Nikita intentionally remain revoked).
3. `/moderators` stays active-only.
4. Do not run `/moderator_add` during revoked-list acceptance.
5. **COMPLETE** — operator confirmed Admin→spam and moderator→processed attribution on live fixtures.

## Phase 3D.8.3 — shorter pending action buttons

1. Pending cards show **✅ Обработано** and **🚫 Спам** (not the older long «Отметить…» captions).
2. Final processed card still reads **✅ Обработан**; spam final still **🚫 Спам**.
3. Callbacks remain `sm:p:` / `sm:s:` — do not diagnose by button text alone.
4. Durable feedback strings unchanged (`Лид отмечен как обработанный.` / `Лид отмечен как спам.`).

## Phase 3E.1 — Parser 3.3 / semantic cards

1. Phase 3E.1 is **COMPLETE** (operator visual A–F PASS).
2. Card **Сайт**: valid URL vs «сайта нет» / messenger-as-contact — messenger never as website.
3. Do not activate Sales-Manager-v2 (`h8I2Tl2yl4uzhUnB`) without charter; Ops `xSnXPy8cEHoZw6xG` / Admin `wLrLp4WQHm1VJmxz` remain the active pair.

## Phase 3E.2 — First Reply Engine v2 / card v2.4

1. CONFIG: `parser_version=sm-parser-v3.3`, `message_format_version=sm-msg-v2.4`, `reply_template_version=sm-reply-v2.0`, `ai_enabled=false`.
2. Copy block: `✉️ Ответ клиенту — нажмите, чтобы скопировать` + `<pre>`; disclaimer outside the block.
3. Test leads: no customer draft — `Черновик ответа не сформирован: тестовая заявка.`
4. Damaged contact: `Контактные данные требуют проверки.` — draft not ready.
5. Local check: `node implementation/harness/phase3e2-harness.mjs` → **59/59 PASS**.
6. Operator copy acceptance may still be PENDING — see `evidence/phase3e2/LIVE-FIRST-REPLY-ACCEPTANCE-v1.md`.
7. Pending-lead reminders are **not** in this phase.

