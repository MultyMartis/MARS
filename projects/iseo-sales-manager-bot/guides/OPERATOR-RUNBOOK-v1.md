> **Phase 3H.10 (2026-08-20):** Daily reminder is an actionable digest. Active staff for reminders: **3** (MOD_A intentionally off). Do not manually fire production 10:00. Check `/reminder_status` after natural window. Tests only to ADMIN_A.

> **Phase 3H.9.2 (2026-08-17):** ACCESS live drifted to 3 after an incomplete 2026-08-16 `/moderator_remove`/`/moderator_add` cycle left MOD_A revoked. Classified `UNAUTHORIZED_STATE_DRIFT`. Restored MOD_A via existing `/moderator_add` (same profile_no 3). Live ACCESS=4 · CONFIG=4 · Operational resolver=4 · reminder resolver=4. Next natural 10:00: **2026-08-18 Europe/Moscow**. Soak not restarted. Phase 3I.1 blocked. AI OFF. No four-recipient test sends.

> **Phase 3H.9 (2026-08-17):** False «Недостаточно прав» on raw lead was ACCESS/CONFIG Google Sheets `invalid_grant` mislabeled as a permission deny. Reminder 10:00 windows 15–17 Aug failed at CONFIG read with the same credential error before evaluation; 429 retry path was not applicable. Admin deny text + Sheets error classifier patched. Live Sheets OAuth reconnect by operator is still required before ADMIN_A raw retest and the next natural 4-recipient 10:00. Soak not restarted. Phase 3I.1 blocked. AI OFF.

> **Phase 3H.8.2.2 (2026-08-14):** Reminder pending eligibility uses `iseo-reminder-current-state-selector-v1.0` — unique `lead_id` → authoritative current status → eligibility. First CLEAN pending row no longer wins. Production Reminder Build Claims adds no per-lead Sheets calls. Duplicate CLEAN row source forensic is deferred. Real 10:00 acceptance still pending.

<!-- Phase 3H.8.2 addendum 2026-08-14 -->
## Phase 3H.8.2 addendum

- Contract: `iseo-sheets-429-retry-v1.0` on reminder-critical Sheets reads (Admin.dev only).
- ACCESS_CONTROL 429: explicit Wait 5s/15s/30s loop (max 4 attempts); fail closed `ERROR_SHEETS_429_ACCESS`; no stale ACCESS send fallback.
- `/reminder_status` exposes ERROR + stage + quota reason + retry count.
- Soak remains: **INTERRUPTED — REAL REMINDER WINDOW FAILED ON SHEETS 429** (not restarted).
- Next live acceptance: **2026-08-15 10:00 Europe/Moscow** with `REMINDER_ACCEPTANCE_LEAD_2` left pending.
- Do not claim REMINDER LIVE PASS until that scheduled window succeeds.
- Phase 3I.1 blocked; AI OFF; Admin **92** nodes; Ops **45**; v2 inactive.
- Evidence: [evidence/phase3h82/](evidence/phase3h82/) · Report: [reports/REPORT-iseo-sales-manager-bot-phase3h82-reminder-sheets429-resilience-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3h82-reminder-sheets429-resilience-v1.md)

<!-- Phase 3H.8 addendum 2026-08-13 -->
## Phase 3H.8 addendum

- Reminder/pending CLEAN source of truth: `lead_clean_v2` (not obsolete `LEADS`).
- Observability contract: `iseo-reminder-observability-v1.1`.
- Soak: **INTERRUPTED — REAL PENDING LEAD MISSED DAILY REMINDER WINDOW**.
- Next live acceptance window: **2026-08-14 10:00 Europe/Moscow** with `REMINDER_PROD_LEAD_A` left pending.
- Phase 3I.1 blocked; AI OFF; do not artificially invoke production reminder.

---

## Phase 3H.7.3.1 (2026-08-10)
- Verdict baseline: acceptance-card canonicalization + authoritative instance v1.1
- Root cause: callback status sync used reduced `buildFinalCard`; fixed to full canonical body
- Contract: `iseo-authoritative-card-instance-v1.1`
- Soak: new final 48h restarted (does not reuse 3H.7.3 T+0); Phase 3I.1 blocked; AI OFF
- Evidence: `evidence/phase3h731/`
<!-- Phase 3H.7.3 operator resurface production-parity repair 2026-08-10 -->
## Phase 3H.7.3 (current)

| Field | Value |
|-------|-------|
| **Phase** | 3H.7.3 — Operator resurface production-parity, contact error fix, multi-card sync hardening |
| **Verdict** | `COMPLETE — RESURFACE PARITY REPAIRED; OPERATOR ACCEPTANCE PENDING` |
| **Repairs** | Canonical renderer for resurface · formula-error contact filter · authoritative card registry · semantic ack ≠ sync warning |
| **Acceptance leads** | REAL_REOPEN_A/B/C pending · 12 parity cards · no new LEADS rows |
| **Runtime** | Ops **45** active · Admin **87** active · v2 inactive · AI **OFF** · reminders recipients=4 |
| **Soak** | 3H.7.2 interrupted · Fresh T+0 **2026-08-10 12:44 Europe/Moscow** · earliest T+48 **2026-08-12 12:44 Europe/Moscow** |
| **Evidence** | [evidence/phase3h73/](evidence/phase3h73/) |
| **Report** | [REPORT-iseo-sales-manager-bot-phase3h73-resurface-production-parity-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3h73-resurface-production-parity-v1.md) |
| **Gate** | Phase 3I.1 blocked until soak PASS + operator acceptance |

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


## 3F.2.1 acceptance commands

As Admin: `/leads`, `/lead_history 1`, `/pending_count`, `/pending_leads`, `/reminder_status`, `/help`. Confirm source display, processed status, actor, reply text, reminders OFF.

## 3F.2.2 polish acceptance

As Admin after deploy: `/lead_history 1` (no `telegram_sent`; human delivery phrase), `/help` (intact `/ai_on`, `/lead_history <номер>`, pending + reminder_status). As moderator: `/help` without config/AI/reminder-config commands. Do **not** enable reminders.

## Phase 3G.1 — first-contact + reply profiles

1. Offline gate: `node implementation/harness/phase3g1-harness.mjs` → 100/100 PASS.
2. Approved names: ADMIN_A→Андрей; MOD_A→Михаил (never Мопс in client copy). Prepared Оля/Никита stay revoked/ineligible.
3. Admin commands for names: historically token-based in 3G.1 — **superseded in 3G.2 by number** (`/reply_profile N`, `/reply_name_set N …`); moderators use `/my_reply_profile` only.
4. AI stays OFF; reminders OFF; Sales-Manager-v2 inactive; no customer auto-send.
5. Live patch applied (3G.1); profile seed repair complete (3G.1.1). Operator **T1/T3 visual acceptance** was a historical gate — see Phase 3G.1.1 below.
6. Evidence: `evidence/phase3g1/` · `evidence/phase3g1-1/`.

## Phase 3G.1.1 — operator visual template acceptance

**Verdict target:** `COMPLETE — LIVE PROFILES SEEDED; OPERATOR TEMPLATE ACCEPTANCE PENDING`

### Checklist (do not press lifecycle buttons)

1. Locate **latest** acceptance-set cards (not earlier empty-copy exploratory batches).
2. **T1** as ADMIN_A — confirm `Меня зовут Андрей, компания INTLSEO` + site line + audit CTA; guidance outside `<pre>`.
3. **T1** as MOD_A — confirm `Меня зовут Михаил, компания INTLSEO`; **`Мопс` must not appear** in client copy.
4. **T3** as ADMIN_A — traffic-decline task summary + Андрей intro.
5. **T3** as MOD_A — traffic-decline task summary + Михаил intro; **`Мопс`=0**.
6. Admin: `/reply_profiles` — ADMIN_A/MOD_A enabled; revoked rows disabled.
7. `/my_reply_profile` as ADMIN_A and MOD_A — names match seeded values.
8. `/ai_status` — **OFF**.
9. Do **not** press Обработано/Спам buttons on acceptance cards.
10. Do **not** clean TEST_LEADS fixtures until visual sign-off recorded.

Evidence: `evidence/phase3g1-1/` · Report: `reports/REPORT-iseo-sales-manager-bot-phase3g1-1-live-profile-and-template-acceptance-v1.md`.

## Phase 3G.2 — numbered profiles + text contract

1. Profiles addressed by **number**: `/reply_profiles`, `/reply_profile 3`, `/reply_name_set 3 Михаил`, `/reply_name_enable 3`, `/reply_name_disable 3`.
2. Seed (do not renumber): **1** ADMIN_A Андрей enabled · **2** MOD_B_REVOKED Оля disabled · **3** MOD_A Михаил enabled · **4** MOD_C_REVOKED Никита disabled.
3. `/my_reply_profile` for Admin and moderator; moderators cannot mutate names.
4. Name commands **do not** change ACCESS_CONTROL role/status — use moderator add/remove for access.
5. Admin `/help` must list the full profile section; moderator `/help` only `/my_reply_profile` among profile cmds — rebuild templates, never substring-patch.
6. Contour: Ops 45 · Admin **85** · v2 inactive · Parser 3.3 · LEADS / LEAD_EVENTS · epoch 05.08.2026 MSK · AI OFF · reminders OFF.
7. Guides: [TELEGRAM-COMMAND-REFERENCE-v1.md](TELEGRAM-COMMAND-REFERENCE-v1.md) · text [TELEGRAM-TEXT-CONTRACT-v2.md](../architecture/TELEGRAM-TEXT-CONTRACT-v2.md).
8. Evidence: `evidence/phase3g2/`.

## Phase 3G.2.1 — silent `/help` `/start` `/config` repair

1. If `/help`, `/start`, or `/config` produce **no** Telegram reply while profile/AI/stats work: treat as Code-node syntax / builder failure class (see `evidence/phase3g2-1/`).
2. After 3G.2.1 patch: Admin should receive responses for `/help`, `/start`, `/config`; never silence for recognized commands.
3. Safe fallback (internal error): `Не удалось сформировать ответ команды. Ошибка зафиксирована, повторите позже.`
4. Operator acceptance packet: Admin `/help` `/start` `/config` `/ai_status` `/stats` `/reply_profiles` `/reply_profile 3`; moderator `/help` `/start` `/my_reply_profile`.
5. Do **not** re-run disable/enable on profile 3 unless necessary; keep Михаил enabled.
6. AI stays OFF; reminders stay OFF; do not activate Sales-Manager-v2.
7. Evidence: `evidence/phase3g2-1/` · Report: `reports/REPORT-iseo-sales-manager-bot-phase3g2-1-silent-command-repair-v1.md`.

## Phase 3G.2.3 — moderator `/start` read-after-rehydrate

1. Residual defect after 3G.2.2: Auth rehydrated `access_upsert` to Михаил while Start still read the blank sheet snapshot → `Имя в ответах: не задано` in the same execution.
2. Fix: Admin.dev Start prefers `access_upsert.reply_sender_name` (post-rehydrate). Same workflow ID · 85 nodes.
3. As MOD_A: `/start` → expect `Имя в ответах: Михаил` in **that same** reply; then `/my_reply_profile`; then `/start` again.
4. As ADMIN_A: `/start` stays concise; `/reply_profiles` lists 1–4 unchanged.
5. If `/start` shows «не задано» while `/my_reply_profile` shows Михаил after this patch, stop — Start stale-read regression.
6. Offline gate: `node implementation/harness/phase3g23-harness.mjs` → 30/30 PASS.
7. AI stays OFF; reminders stay OFF; do not activate Sales-Manager-v2.
8. Evidence: `evidence/phase3g2-3/` · Report: `reports/REPORT-iseo-sales-manager-bot-phase3g2-3-moderator-start-profile-repair-v1.md`.

## Phase 3G.2.2 — unified profile resolver + config truth repair

1. Root cause: routine `/start`/`/my_status` traffic from ADMIN_A or MOD_A wiped their own reply-profile columns (name/enabled/company/version), because the authorization projection stripped those fields and the last-seen upsert wrote the row back without them. `reply_profile_number` was never affected.
2. Fix deployed on the same Admin.dev workflow: anti-wipe projection allowlist + auto-rehydrate on `/reply_profiles`, `/reply_profile N`, `/my_reply_profile`, and `/start`/`/my_status`. A wiped row self-corrects the next time the actor runs one of these commands — no manual Sheets edit performed by the agent.
3. As ADMIN_A: send `/start` then `/my_reply_profile` — confirm name «Андрей», «Персональный ответ: включён».
4. As MOD_A: send `/start` then `/my_reply_profile` — confirm name «Михаил», «Персональный ответ: включён», and confirm «Мопс» does not appear anywhere in the reply. **Note:** after 3G.2.3, `/start` must also show Михаил in the *same* execution as rehydrate (not only after writeback).
5. As Admin: send `/config` — confirm parser version shows `sm-parser-v3.3` (not `sm-parser-v3.2`), a resolver-version line is present, and reporting-sync state is shown explicitly (expected: «выключена»).
6. Do not manually restore ADMIN_A/MOD_A profile cells via direct Sheets edit — the rehydrate patch is the intended restore path and re-derives from the same approved seed every time.
7. Offline gate: `node implementation/harness/phase3g22-harness.mjs` → 53/53 PASS; regression `node implementation/harness/phase3g2-harness.mjs` → 42/42 PASS.
8. AI stays OFF; reminders stay OFF; do not activate Sales-Manager-v2; do not change access roles.
9. Evidence: `evidence/phase3g2-2/` · Report: `reports/REPORT-iseo-sales-manager-bot-phase3g2-2-profile-resolver-and-config-truth-v1.md`.

## Phase 3H.4 — soak observability repair

1. **Symptom:** `/reminder_status` silent for Admin; `/status` stale poll time; wrong last processed lead (22:23 МСК from synth test).
2. **Root causes:** Reminder Commands SyntaxError (exec 24194/24196); empty polls did not write heartbeat; Status read synthetic `last_lead_success_at`.
3. **Fix deployed:** Admin Reminder/Status/Health patched; Operational poll heartbeat v1.0; CONFIG backfill for production lead + recipient count=3.
4. **Soak:** attempt 1 invalidated; new T+0 **2026-08-06 19:15 Europe/Moscow**; earliest PASS **2026-08-08 19:15 Europe/Moscow**.
5. As ADMIN_A: `/reminder_status` `/status` `/health` — confirm visible replies and corrected production lead time.
6. Do not start Phase 3I.1 until soak PASS.
7. Evidence: `evidence/phase3h4/` · Report: `reports/REPORT-iseo-sales-manager-bot-phase3h4-soak-observability-repair-v1.md`.

## Phase 3H.4.1 operator check

If `/stats` processed≥1 but `/status` shows `нет данных`, treat as CONFIG cache / Status readback defect — do not rewrite LEADS. Verify `last_production_processed_at` non-empty and Moscow formatting. See `guides/PRE-AI-SOAK-RUNBOOK-v1.md`.

## Phase 3H.6 run notes

- Approved recipients: Андрей, Оля, Михаил, Никита (4)
- `/reminder_status` must show Получателей: 4
- Do not revoke Никита without a new baseline charter
- Soak T+0: 2026-08-06 20:28 Europe/Moscow · earliest PASS 2026-08-08 20:28
- AI remains OFF; Phase 3I.1 blocked


### Phase 3H.7

See evidence/phase3h7 and architecture/LEAD-REOPEN-CONTRACT-v1.md. Soak interrupted pending Gmail reauth + missed-lead recovery. Reopen: processed|spam -> pending via sm:r:.



## Phase 3H.7.1 note
Gmail OAuth recovery closed; original terminal cards now expose `↩️ Вернуть в обработку`; MISSED_PROD_LEAD_1 resolved without replay (no absent genuine form lead); soak restarted; Phase 3I.1 blocked.

## Phase 3H.7.2 note
Callback acknowledgement contract `iseo-lead-callback-ack-v1.0` deployed. Reopen ack is «Лид возвращён в обработку.». Aggregate no longer maps pending applied→processed. Operator-approved resurface of three genuine leads completed for acceptance; global reopen still does not fan out. Soak restarted; Phase 3I.1 blocked. See `evidence/phase3h72/`.

