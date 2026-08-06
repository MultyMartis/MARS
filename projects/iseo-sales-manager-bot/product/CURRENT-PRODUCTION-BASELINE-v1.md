# CURRENT PRODUCTION BASELINE v1

**Срез:** Phase 3G.2.3, 2026-08-06. **Статус:** unified resolver live; moderator `/start` read-after-rehydrate repair deployed (Start prefers `access_upsert`); AI OFF; reminders OFF; operator Telegram acceptance pending.

| Контур | Workflow ID | Active | Nodes | Роль |
|---|---|---:|---:|---|
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | — | rollback; не активировать без отдельного решения |
| i-SEO Sales Manager - Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 | Parser 3.3; multi-recipient cards; AI OFF; `minutesInterval=2` |
| i-SEO Sales Manager - Admin.dev | `wLrLp4WQHm1VJmxz` | true | **85** | 3G.2 profiles + 3G.2.1 Help/Start/Config/Capture guard; reminders OFF; callbacks |


## Phase 3F.2 — Clean production ledger

- Production stats epoch display **05.08.2026**; exact epoch = first real lead Gmail `internalDate` (Europe/Moscow).
- Authoritative table `LEADS` (generation v2); legacy mixed corpus archived/excluded.
- Callback lookup contract v2: canonical dual-FNV token; token persisted before CLEAN write.
- External reporting workbook «i-SEO — Учёт лидов и статистика» (private); backend remains SoT.
- Reminders remain OFF; AI OFF; Sales-Manager-v2 inactive.

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



## 3F.2.1 baseline delta

Admin nodes include lead history path. Human source display active. Reporting schema reporting-v1.1 (readiness column additive). Operator acceptance pending for Telegram visuals.


## 3F.2.2 baseline delta

- Admin.dev Help rebuilt (Admin + moderator templates); pending + reminder_status listed.
- /lead_history human map includes 	elegram_sent; unknown → техническое событие.
- Operational.dev unchanged (45 nodes). Reminders OFF. AI OFF. Access unchanged.
- Phase 3F.2 closeout prepared; operator visual /help + /lead_history 1 pending.

## Phase 3G.1 additive baseline note

Pre-patch contour unchanged until live acceptance filled: Ops active 45 · Admin active 82 · Sales-Manager-v2 inactive · AI OFF · reminders OFF · stats 1/1/0/0 epoch 05.08.2026.

Target reply versions (live): `iseo-first-contact-v1.0` / `iseo-template-set-v1.0` / `iseo-sales-policy-v1.0` / `iseo-manager-assist-v1.0` / `iseo-recipient-name-v1.0`. Reply profiles **seeded** on ACCESS_CONTROL Q–V (Phase 3G.1.1). AI **OFF**. Reminders **OFF**. Admin **84** nodes. Harness 100/100 PASS + 3G.1.1 fail-closed 9/9 PASS. See `evidence/phase3g1/FINAL-WORKFLOW-STATE-v1.md` and `evidence/phase3g1-1/FINAL-WORKFLOW-STATE-v1.md`.

## Phase 3G.1.1 additive baseline note

Live profile columns repaired and seeded. T1/T3 acceptance inject delivered 4 personalized Telegram cards. Operator visual template acceptance pending (historical). Ops 45 · Admin 84 · v2 inactive · AI OFF · reminders OFF.

## Phase 3G.2 additive baseline note

- Immutable `reply_profile_number`: **1** ADMIN_A Андрей enabled active · **2** MOD_B_REVOKED Оля disabled revoked · **3** MOD_A Михаил enabled active · **4** MOD_C_REVOKED Никита disabled revoked.
- Admin mutations address profiles **by number only** (`/reply_profile N`, `/reply_name_set N …`, enable/disable). `/my_reply_profile` for Admin+moderator.
- Client-facing name **only** from `reply_sender_name`. Name commands do **not** change access role/status.
- Text: `architecture/TELEGRAM-TEXT-CONTRACT-v2.md`. Help: explicit Admin/moderator templates (`ROLE-AWARE-HELP-BUILDER-v2`). Command map: `guides/TELEGRAM-COMMAND-REFERENCE-v1.md`.
- Authoritative data: Parser **3.3**; table **`LEADS`**; events **`LEAD_EVENTS`**; stats epoch **05.08.2026** Europe/Moscow.
- Contour: Ops **45** active · Admin **~84+** after patch · Sales-Manager-v2 inactive · AI OFF · reminders OFF · no customer auto-send.
- Evidence stubs: `evidence/phase3g2/`.

## Phase 3G.2.2 additive baseline note

- Root cause: `/start`/`/my_status` last-seen upsert wrote ACCESS_CONTROL without `reply_profile_*` fields (upstream `Check User Authorization` projection had stripped them), wiping ADMIN_A and MOD_A profile columns on routine authenticated traffic. No row loss, no duplication, no renumbering — 4 authoritative profile rows, 0 duplicates confirmed.
- Fix: anti-wipe projection allowlist (`REPLY_PROFILE_ACCESS_FIELDS`) + auto-rehydrate (`buildProfileRehydratePatch` / `mergeRehydrateIntoUpsert`) deployed on the same Admin.dev workflow. Unified resolver `iseo-reply-profile-resolver-v1.0` now backs all 8 profile read paths (0 divergent paths remaining).
- CONFIG truth corrected: stale `sm-parser-v3.2` key → live `sm-parser-v3.3`; reporting sync display corrected to honest «выключена»; resolver version + active-recipient count (2) added to `/config`.
- Offline harness `phase3g22-harness.mjs` **53/53 PASS**; regression `phase3g2-harness.mjs` **42/42 PASS**. Contour unchanged: Ops 45 active · Admin 85 active · v2 inactive · AI OFF · reminders OFF · workflows created=0.
- Storage restore of ADMIN_A/MOD_A fires on the next live Telegram command from each actor that hits a rehydrate-covered path; direct Sheets API restore and Telegram webhook inject were not available to the agent this session — see `evidence/phase3g2-2/ADMIN-A-RESTORE-v1.md`.
- Evidence: `evidence/phase3g2-2/`. Architecture: `architecture/UNIFIED-REPLY-PROFILE-RESOLVER-v1.md`.

## Phase 3G.2.3 additive baseline note

- Residual defect after 3G.2.2: moderator `/start` built `Имя в ответах` from the pre-rehydrate `Read ACCESS_CONTROL` snapshot while `Check User Authorization` already held the correct post-rehydrate `access_upsert` (live exec 24097: sheet blank, upsert Михаил, Start «не задано»).
- Repair: Admin.dev **Start** node prefers `j.access_upsert.reply_sender_name` (unified contract `iseo-reply-profile-resolver-v1.0`); sheet is fallback only. Same workflow ID · **85** nodes · Start hash `7E0A13DB067254EF`.
- Single-execution invariant: `/start` must show Михаил in the same command that rehydrates — must not rely on the next command.
- Offline harness `phase3g23-harness.mjs` **30/30 PASS**. Contour unchanged: Ops 45 · Admin 85 · v2 inactive · AI OFF · reminders OFF · workflows created=0.
- Evidence: `evidence/phase3g2-3/`.
