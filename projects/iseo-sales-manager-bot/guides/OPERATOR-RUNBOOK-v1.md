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
6. Human Reply Style is operator-accepted; Phase 3E.2.3 does not redesign copy.
7. Pending-lead reminders are **not** in this phase.

## Phase 3E.2.1 — delivery fail-closed + Human Reply Style v1

1. If managers receive **identical** cards repeatedly for one lead: deactivate Operational.dev immediately; keep Admin active; keep v2 inactive; do **not** treat Sheets quota as permission to resend.
2. Post-patch: ledger read error / claim failure → **zero** Telegram sends; CONFIG secondary `tg_delivered:*` guards exist.
3. Versions: `sm-reply-v2.1` + `sm-human-v1.0`; drafts must not narrate parser/guard logic.
4. Local: `node implementation/harness/phase3e21-harness.mjs` → **64/64 PASS**.
5. Evidence: `evidence/phase3e2-1/`; Human Reply Style is now operator-accepted.
6. Under Sheets quota, claim path correctly blocks send; wait for API recovery before re-proving dual-card live delivery.
7. Do not restore Olya/Nikita; do not enable AI; do not create workflows; do not implement reminders in this phase.

## Phase 3E.2.2 — Sheets recovery / dual-card proof / human copy packet

1. Isolated Sheets probes may report healthy while the **full** delivery path still fails on ACCESS_CONTROL/claim under quota — treat full-path claim failure as fail-closed (zero cards), not as permission to bypass ledger.
2. Marker `PHASE_3E2_2_DUAL_CARD_DELIVERY_PROOF` is an internal acceptance fixture (drafts allowed; excluded from prod stats).
3. Local: `node implementation/harness/phase3e22-harness.mjs` → **59/59 PASS**.
4. Evidence: `evidence/phase3e2-2/`; report: `reports/REPORT-iseo-sales-manager-bot-phase3e2-2-final-acceptance-v1.md`.
5. Until dual-card `sendOk=2` is proved after Sheets recovery, status remains **`ATTENTION — SHEETS DELIVERY PATH STILL RATE-LIMITED`**.
6. Historical draft-acceptance gate is closed; 3E.2.3 still requires visual confirmation of the final proof card.

## Phase 3E.2.3 — quiet-window reactivation gate

1. Offline harness is **83/83 PASS**; keep Operational.dev inactive until the pending real-lead recount is complete.
2. Confirm 45 nodes, final `minutesInterval=2` schedule and 4-minute single-flight TTL; do not restore rejected `secondsInterval=120`.
3. Do not bypass ACCESS_CONTROL, ledger or claim after quota errors; exhausted retry means zero cards.
4. Final proof is complete: two eligible claims/sends/stamps and five polls with zero resend.
5. A post-send Sheets failure means `reconciliation_required`; do not replay blindly.
6. Do not enable AI, change access, activate rollback workflow or implement reminders.
7. Closed: operator visual confirmation received. Final verdict `PHASE 3E.2 COMPLETE — HUMAN FIRST REPLY ENGINE READY` (see `evidence/phase3f1/PHASE3E2-FINAL-CLOSEOUT-v1.md`).

## Phase 3F.1 — pending-lead commands and daily reminder engine

1. Admin.dev is the same workflow ID (`wLrLp4WQHm1VJmxz`), now **79 nodes** (was 59). Operational.dev is unchanged (45 nodes).
2. New staff-read commands: `/pending_count`, `/pending_leads [page] [test]`, `/reminder_status`. New Admin-only commands: `/pending_leads_test`, `/reminder_on`, `/reminder_off`, `/reminder_time HH:MM`, `/reminder_timezone <IANA>`, `/reminder_min <n>`.
3. Pending resolution is `manager_status` primary, `lifecycle_status` secondary; legacy rows without either default to pending unless already closed.
4. The reminder engine runs on an **internal 15-minute Schedule Trigger inside Admin.dev** — it is not a separate workflow and does not touch Operational.dev.
5. Reminders are **OFF in production** (`pending_reminders_enabled=false`, default `10:00` `Europe/Moscow`). Do not flip this to `true` without explicit operator authorization.
6. A controlled reminder schedule exercise reached the ACCESS_CONTROL read step and correctly failed closed under a live Sheets quota condition — zero sends is the expected, correct outcome, not an incident.
7. `REMINDER_DELIVERIES` is a new, currently empty Sheets tab; no other tab schema changed.
8. Offline harness: `node implementation/harness/phase3f1-harness.mjs` → **73/73 PASS**.
9. Do not restore Оля/Никита, enable AI, or activate the rollback workflow as part of this phase.
10. Current stop verdict: `COMPLETE — COMMANDS AND REMINDER ENGINE READY; OPERATOR ACTIVATION PENDING`.
