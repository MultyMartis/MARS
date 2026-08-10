# ADMIN WORKFLOW PATCH SPEC v1

**Target workflow name:** `i-SEO Sales Manager - Admin.dev`  
**Phase:** 3A — specification only  
**Pattern source:** MetaBOT Admin sanitized baseline (see ADMIN-SOURCE-SELECTION-v1) — **not copied yet**  
**Forbidden:** operational Gmail lead processing; client messaging; OpenRouter except optional health probe when both AI ON and probe enabled

---

## 1. Target node list

Placeholders: `<TELEGRAM_CREDENTIAL>` · `<GOOGLE_SHEETS_CREDENTIAL>` · `<ADMIN_CHAT_ID>` · `<CLEAN_WORKBOOK_ID>`  
Sandbox: Telegram send may be disabled until synthetic admin chat approved.

| # | Stable name | Source | type (expected) | typeVersion | Responsibility | Input | Output | Error behavior | Side effects | Credential | Sandbox disabled | Connection targets |
|---|-------------|--------|-----------------|-------------|----------------|-------|--------|----------------|--------------|------------|------------------|-------------------|
| 1 | Telegram Trigger | **new**/adapt | `n8n-nodes-base.telegramTrigger` (or webhook) | 1.1 / 2.1 | Admin entry | update | message | ignore non-text | Telegram receive | `<TELEGRAM_CREDENTIAL>` | false | → Normalize Command |
| 2 | Normalize Command | **new** | `n8n-nodes-base.code` | 2 | `/cmd` lower, trim args, user_id | update | cmd object | → Admin Error Handler | none | — | false | → Read Authorization Config |
| 3 | Read Authorization Config | **new** | `n8n-nodes-base.googleSheets` | 4.5+ | Read CONFIG keys | cmd | cmd+config | deny writes; reply unavailable | Sheets read | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Check User Authorization |
| 4 | Check User Authorization | **new** | `n8n-nodes-base.if` | 2.2 | Allowlist `admin_user_ids` | cmd+config | true/false | false → deny reply | none | — | false | true→Route Command; false→Safe Telegram Reply (deny) |
| 5 | Route Command | **new** | `n8n-nodes-base.switch` | 3.2 | Route 10 cmds + unknown | authorized | branch | unknown branch | none | — | false | → handlers 6–16 |
| 6 | Help | **new** | `n8n-nodes-base.code` | 2 | Static Russian help | — | text | → Error Handler | none | — | false | → Safe Telegram Reply |
| 7 | Status | **new** | `n8n-nodes-base.code` (+ Sheets if needed) | 2 | environment, AI, last_* ops | config | text | → Error Handler | Sheets read | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Safe Telegram Reply |
| 8 | AI Status | **new** | `n8n-nodes-base.code` | 2 | ai_enabled, model, probe flag | config | text | → Error Handler | none | — | false | → Safe Telegram Reply |
| 9 | AI On | **new** | Sheets update + Code | 4.5+ / 2 | Set `ai_enabled=true` | config | confirm | → Error Handler | CONFIG write + audit | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Audit Config Change → Safe Telegram Reply |
| 10 | AI Off | **new** | Sheets update + Code | 4.5+ / 2 | Set `ai_enabled=false` | config | confirm | → Error Handler | CONFIG write + audit | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Audit Config Change → Safe Telegram Reply |
| 11 | Health | **new** | Code + bounded Sheets | 2 | HEALTHCHECK-CONTRACT | config | text | FAIL lines | read-only probes; optional admin ping | sheets/tg | probe nodes gated | → Safe Telegram Reply |
| 12 | Stats | **new** | Code + bounded Sheets | 2 | Windowed counts | config/arg | text | → Error Handler | Sheets read bounded | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Safe Telegram Reply |
| 13 | Synthetic Test Lead | **new** | Code + Sheets | 2 | Fixture inject sandbox only | args | summary | refuse if prod | sandbox RAW/CLEAN write | `<GOOGLE_SHEETS_CREDENTIAL>` | **true** until approved | → Audit Config Change → Safe Telegram Reply |
| 14 | Last Error | **new** | Sheets read + Code | 4.5+ / 2 | Latest ERRORS row | — | text | empty → «нет ошибок» | Sheets read | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Safe Telegram Reply |
| 15 | Config Summary | **new** | Code | 2 | Allowlisted non-secret keys; admins as count | config | text | → Error Handler | none | — | false | → Safe Telegram Reply |
| 16 | Unknown Command | **new** | `n8n-nodes-base.code` | 2 | Fixed Russian string | — | text | — | none | — | false | → Safe Telegram Reply |
| 17 | Audit Config Change | **new** | `n8n-nodes-base.googleSheets` | 4.5+ | LEAD_EVENTS admin_* | write cmds | same | warn | Sheets append | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Safe Telegram Reply |
| 18 | Safe Telegram Reply | pattern | `n8n-nodes-base.telegram` | 1.2 | Reply to admin user/chat | text | sent | → Admin Error Handler | Telegram send | `<TELEGRAM_CREDENTIAL>` | optional | (end / success) |
| 19 | Admin Error Handler | **new** | Code + ERRORS append + Telegram | 2 | Short Russian + error_code | any | reply | last resort | ERRORS write | sheets/tg | false | → Safe Telegram Reply |

Deny path from node 4 may jump directly to Safe Telegram Reply with `Доступ запрещён.` without Route Command.

---

## 2. Command router outcomes

| Command | Handler | Write? |
|---------|---------|--------|
| `/start` | Start | no |
| `/help` | Help | no |
| `/status` | Status | no |
| `/ai_status` | AI Status | no |
| `/ai_on` | AI On + Audit | yes |
| `/ai_off` | AI Off + Audit | yes |
| `/health` | Health | no (optional admin ping) |
| `/stats` | Stats | no |
| `/test_lead` | Synthetic Test Lead + Audit | sandbox write |
| `/last_error` | Last Error | no |
| `/config` | Config Summary | no |
| other | Unknown Command | no |

---

## 3. Explicit non-goals

- No Gmail fetch / label mutate.  
- No production unread lead processing.  
- No auto client reply.  
- No SEO locks / stop-all-flow.  
- No Execute Workflow to Operational unless later charter.

---

## 4. `/test_lead` policy

- Default fixture: unnamed Audit phone-only.  
- Optional arg: fixture id from TEST-HARNESS-SPEC.  
- Allowed when `environment=dev` or explicit test flag.  
- Prod: refuse unless `allow_prod_synthetic=true` (default false).

---

## 5. SAFE UNKNOWN

Telegram Trigger vs Webhook; shared bot with manager cards vs separate admin bot; exact Switch typeVersion on instance.

---

*Related: ADMIN-SOURCE-SELECTION-v1 · ADMIN-COMMAND-CONTRACT-v1 · HEALTHCHECK-CONTRACT-v1.*


## Phase 3B.4 patch notes

- Enable Telegram Trigger (`disabled=false`) for acceptance windows only; final active=false.
- Stats: Route → Read CLEAN for Stats → Stats (bounded SYNTHETIC_TEST).
- AI on/off: AI On/Off → Prepare Config Write → Apply CONFIG Write (appendOrUpdate) → Restore Reply → Capture → Safe Telegram Reply.
- Normalize Command accepts Telegram Trigger root updates and webhook `body` wrappers.


## Phase 3B.4.1 patch notes

- Keep Telegram Trigger `disabled=false` for future controlled acceptance windows; Admin final active=false.
- Normalize Command: trim, lowercase, strip `@bot`, map optional aliases to canonical commands; args excluded from privileged matching.

## Phase 3C.1 patch notes

- `/health` → Gmail Health Probe (bounded production incoming-label query) → Health formatter.
- Production wording: `Gmail: доступен, запрос выполнен` + `Найдено подходящих писем: N`.
- `/status` production lines: последний опрос Gmail / последний обработанный лид / последняя ошибка.
- `/last_error` stage vocabulary includes `gmail_read` / `schedule_trigger`.

## Phase 3B.5 patch notes

- Admin.dev may remain **active** after polish.
- Safe patch: deactivate → code-only PUT → reactivate; restore backup if Trigger registration fails.
- Operator UX: Moscow time render; Russian terminology; synthetic/production status separation.
- `/test_lead`: deferred reply; omit from `/help` until Operational synthetic entry is chartered.
- `/start` (Phase 3D.2): authorized greeting with dynamic contour + AI wording; unauthorized → `Доступ запрещён.`
- Phase 3D.2.1: all Telegram send nodes must set `additionalFields.appendAttribution=false`; Help/readiness advertise canonical commands only; no Admin update-id idempotency table (duplicate `/start` was harness overlap).

## Phase 3D.3 patch notes — callback graph + `/leads`

**Callback graph (added to Route Command upstream branch in Normalize Command):**

```
Admin Telegram Trigger (message + callback_query)
  → Normalize Command (branch: text command | callback_query)
       callback_query →
         Read Authorization Config → Check Manager Action Authorization
           (deny → Answer Callback Query "Доступ запрещён.")
           (allow) → Resolve Lead by Token (opaque token → lead_id)
             → Lifecycle State Machine
                  pending→processed | pending→spam → applied
                  same-status repeat → idempotent
                  processed↔spam → conflict
             → Update CLEAN Lifecycle (Sheets, update-by-lead_id)
             → Append LEAD_EVENTS Callback (immutable; records applied/idempotent/conflict/unauthorized)
             → Edit Lead Card Message (clear keyboard on applied; on edit failure, log Callback Edit Result but keep Sheets mutation)
             → Answer Callback Query (confirms outcome to the tapping manager)
```

- `Check Manager Action Authorization` reads `manager_action_user_ids`, falling back to `admin_user_ids` while the manager allowlist is empty (Phase 3D.3 state — Olya not enrolled).
- `Resolve Lead by Token` reads `lead_clean_v2` by the opaque per-lead token stamped at CLEAN write time; unknown/expired token → treated as unauthorized-shaped safe failure (no Sheets mutation, generic answer).
- No Execute Workflow call to Operational.dev; Admin.dev owns the full callback path against `lead_clean_v2` directly (see SHEETS-LIFECYCLE-MAPPING evidence).

**`/leads` handler (added to Route Command):**

- New handler node reads `lead_clean_v2` (bounded, most-recent-first), validates count arg against exact `{3,5,10}` (default 5; other values → usage message), selects unique business leads, renders each as a read-only archive card (no inline keyboard), excludes `SYNTHETIC_TEST` / technical-retry-only rows from business-facing recovery use.
- Authorization: `admin_user_ids` only (same gate as other read commands) — **not** the manager-action allowlist.

## Phase 3D.3.1 patch notes — archive multi-card + contact safety

- **Capture Admin Reply:** must map `$input.all()` (passthrough). Do **not** use `$input.first()` — that collapses `/leads` multi-card output to a single Telegram send.
- **Recent Leads:** exact arg parse; newest-first unique selection; ordinals from selected count; suppress invalid contacts; lifecycle status line; one `lead_card_recovered` event per command.
- **Read CLEAN for Leads:** bounded A1 range (`A1:ZZ250`).
- Callback edit path: same invalid-contact suppression on contact fields.

## Phase 3D.4 patch notes — role-aware start/help + Olya enrollment

- **Check User Authorization** unchanged — `admin_user_ids` for text commands only.
- **Check Manager Action Authorization** reads populated `manager_action_user_ids` (**2** entries: operator + Olya hash E6714550214106BA) — **no fallback** to admin list when populated.
- **Route Command** `/start` and `/help` branch: admin → existing handlers; manager-only → new **Manager Start** / **Manager Help** code nodes; unauthorized → deny.
- **Manager Start / Manager Help** — Russian role-aware texts per `evidence/phase3d4/MANAGER-START-HELP-ACCEPTANCE-v1.md`; must not expose Admin commands.
- CONFIG enrollment: add Olya identity to `manager_action_user_ids` **only** after identity resolution (`evidence/phase3d4/OLYA-IDENTITY-RESOLUTION-v1.md`).
- `/config` summary adds manager count line (count only, no raw IDs).


---

## Phase 3D.5 note

See `evidence/phase3d5/` for ACCESS_CONTROL / ACCESS_EVENTS, public auth routing, moderator registry Admin commands, and harness coverage (30+ checks). ACCESS_CONTROL is access SoT; do not edit workflow code to enroll moderators.


## Phase 3D.5.1 — Access registry population and SoT repair

- **ACCESS_CONTROL** is the primary authorization authority (Telegram user ID keyed; username informational only).
- `manager_action_user_ids` is legacy and is **not** an active moderator authority after registry acceptance.
- `admin_user_ids` remains recovery-only Admin bootstrap when ACCESS_CONTROL cannot be read technically.
- A revoked/blocked ACCESS_CONTROL row always overrides CONFIG allowlists.
- ACCESS_EVENTS append mapping must reference Prepare Access Upsert fields (never post-Upsert `` metadata).
- Evidence: `evidence/phase3d51/` · Report: `reports/REPORT-iseo-sales-manager-bot-phase3d51-access-registry-repair-v1.md`.

## Phase 3D.5.2 — Silence recovery graph notes

| Node | Change |
|---|---|
| Collapse Authorization Context | **new** Code — collapse CONFIG fan-out to 1 item; preserve Normalize chat/command context |
| Read Authorization Config / Read ACCESS_CONTROL | `onError=continueRegularOutput`; `alwaysOutputData=true` |
| Check User Authorization / Start / Help / Deny / Unknown / Config / Handle Callback | Pure JS SHA-256 (no Node crypto module) |
| Capture Admin Reply | Safe success/error diagnostic stamps (no sensitive command text) |

Expected Admin.dev node count after patch: **51**. Operational.dev unchanged (36).

## Phase 3D.6 — personal status and notification patch

Admin.dev final node count: **54**. Add exactly:

| Node | Responsibility |
|---|---|
| My Status | Render caller-only `/my_status` for public/pending/moderator/Admin/revoked/blocked |
| Finalize Access Notification | Detect Telegram delivery result, preserve access mutation, choose Admin reply and build notification event |
| Append ACCESS_EVENTS Notify | Append sent/failed role-notification audit |

Route `/my_status` after registry authorization. ACCESS_CONTROL remains the source of truth matched by `telegram_user_id`. For non-idempotent add/remove, persist registry mutation before Telegram notification. On notification failure, append the `*_notification_failed` event and reply `Права изменены, но уведомление пользователю доставить не удалось.`; do not roll back. Repeated add/remove skips notification.

### Code-node mode contract (3d6b)

- `My Status` and `Finalize Access Notification` must use mode **`runOnceForAllItems`** when their jsCode calls `$input.first()` or `$input.all()`.
- Code in mode `runOnceForEachItem` must use the current item context and **must not** call `$input.first()` (n8n raises `Can't use .first() here` and returns zero items).
- Sanitized workflow acceptance must record each relevant Code node's `parameters.mode`.
- Zero-item Code failures must be detected before deployment (harness / structural checks).
- Hotfix marker for the accepted live repair: `3d6b-my-status-code-mode` (node count remains 54; connections unchanged).

---

## Phase 3D.7 addendum — card sync + delivery commands

After lifecycle mutate + LEAD_EVENTS:

1. Read LEAD_DELIVERIES for Sync
2. Expand Card Sync Copies
3. Edit Lead Card Message (each copy)
4. Aggregate Card Sync Result → answer callback

Add Admin-only `/delivery_status` and `/delivery_users`.

## Phase 3D.8 compatibility note

No Admin graph change is required for the Operational Format-only button repair if `Handle Callback` continues to accept `sm:p:<token12>` and `sm:s:<token12>`. Confirm this in harness and live two-recipient acceptance before closeout. Do not add buttons to `/leads` archive cards.

## Phase 3D.8.1 addendum — early ack + multi-copy repair

Same workflow ID `wLrLp4WQHm1VJmxz`:

1. Route `/__callback` → Prepare Early Callback Ack → Answer Callback Early → Read CLEAN for Callback
2. Handle Callback texts per lifecycle contract; idempotent/conflict may converge cards without CLEAN rewrite
3. IF Callback Mutate false → Read LEAD_DELIVERIES (skip LEAD_EVENTS)
4. Prepare Callback Answer → Capture Admin Reply (late Answer Callback Query bypassed)
5. Expand ignores Sheets error items; requires durable LEAD_DELIVERIES tab

## Phase 3D.8.2 addendum — actor attribution + revoked list

Same workflow ID `wLrLp4WQHm1VJmxz` (Admin.dev only):

1. Check User Authorization exports `access_display_name` / `access_username` from ACCESS_CONTROL row (not callback profile).
2. Handle Callback Action builds safe actor label; writes `actor_display_snapshot` into card text and LEAD_EVENTS `detail`.
3. `formatPendingList` adds revoked former-moderator section with stable codes; Admin help line updated.
4. Safe patch: deactivate Admin → PUT same ID → reactivate; keep Operational.dev active; keep Sales-Manager-v2 inactive.

## Phase 3F.1 addendum — pending-lead view + daily reminder

Same workflow ID `wLrLp4WQHm1VJmxz` (Admin.dev only). Node count **59 → 79** (+20).

1. **Pending-lead view nodes** (Route Command branch): `Read CLEAN for Pending` → `Build Pending View` (mirrors `buildPendingView()`) → count/list split → `Format Pending Count` / (`Parse Pending Args` → `Paginate Pending` → `Format Pending List`) → `Safe Telegram Reply`. Full spec: `implementation/PENDING-COMMANDS-v1.md`.
2. **Reminder command nodes**: `/reminder_status` (staff read, role-aware verbosity) plus Admin-only `/reminder_on` / `/reminder_off` / `/reminder_time` / `/reminder_timezone` / `/reminder_min` with input validation before any CONFIG write. Full spec: `implementation/REMINDER-CONFIG-COMMANDS-v1.md`.
3. **Reminder schedule branch** (separate trigger path, not the command router): internal `Reminder Schedule Trigger` (every 15 minutes) → `Read Reminder CONFIG (Gate)` → `Reminder Window Gate` (`isReminderWindowDue()`) → on due: `Read CLEAN for Reminder` → `Read ACCESS_CONTROL for Reminder` → `Read REMINDER_DELIVERIES` → per-recipient `Claim Reminder Delivery` → `Send Reminder` → `Stamp Reminder Delivery` → `Finalize Reminder Window` (CONFIG).
4. Authorization reuses the existing `Read Authorization Config` / ACCESS_CONTROL read already in the Admin graph — no second authorization read added for the new commands.
5. No change to the callback graph (§Phase 3D.3/3D.8.x), lifecycle mutation, or archive (`/leads`) commands.
6. Safe patch: deactivate Admin → PUT same ID → reactivate; keep Operational.dev unchanged (45 nodes); keep Sales-Manager-v2 inactive; keep `pending_reminders_enabled=false`.


## 3F.2.1

Patch same Admin ID: canonical `/leads` adapter, `/lead_history` route+handler+help, staff auth for archive/history, reporting lifecycle labels when Admin syncs.

## 3F.2.2

Patch same Admin ID only (`wLrLp4WQHm1VJmxz`):

1. **Lead History Handler** — complete human event-label map including `telegram_sent`; unknown → `техническое событие`.
2. **Help** — rebuild Admin + moderator `helpReply` templates ([ADMIN-HELP-BUILDER-v1.md](ADMIN-HELP-BUILDER-v1.md)); include pending + `/reminder_status`; Admin-only reminder config subsection.
3. Do not touch Operational.dev, reminder schedule CONFIG defaults, callback tokens, or Sheets schemas.


### Phase 3G.1 Admin patch note

Add reply-profile commands (`/reply_profiles`, `/reply_profile`, `/reply_name_set`, `/reply_name_enable`, `/reply_name_disable`, `/my_reply_profile`). Mutations Admin-only; moderator view-only. Help lines per role. **Historical:** live patch applied; seed repaired in 3G.1.1. Lib: `reply-profile-commands-v1.mjs`.

### Phase 3G.2 Admin patch note

Same Admin workflow (`wLrLp4WQHm1VJmxz`); expect **~84+** nodes after patch:

1. Reply-profile commands address by **`reply_profile_number`** only — [REPLY-PROFILE-ADMIN-COMMANDS-v2.md](REPLY-PROFILE-ADMIN-COMMANDS-v2.md).
2. Rebuild Admin + moderator help via **explicit templates** — [ROLE-AWARE-HELP-BUILDER-v2.md](ROLE-AWARE-HELP-BUILDER-v2.md); Admin must include profile section; moderator only `/my_reply_profile`; **no substring patch**.
3. Seed/confirm immutable numbers 1–4 ([REPLY-PROFILE-NUMBERING-v1.md](../architecture/REPLY-PROFILE-NUMBERING-v1.md)); client name only `reply_sender_name`; name commands must not change access role/status.
4. Do not enable AI or reminders; do not activate Sales-Manager-v2; do not restore revoked moderators as part of this patch.
5. Text surfaces: [TELEGRAM-TEXT-CONTRACT-v2.md](../architecture/TELEGRAM-TEXT-CONTRACT-v2.md) · registry [USER-VISIBLE-TEXT-REGISTRY-v1.md](USER-VISIBLE-TEXT-REGISTRY-v1.md).
6. Evidence: `evidence/phase3g2/`.

### Phase 3G.2.1 Admin patch note

Same Admin ID only (`wLrLp4WQHm1VJmxz`); **85** nodes retained (no new workflow):

1. **Root causes (separate):** Help + Start — corrupted `startReply` splice → `Unexpected token ')'`; Config Summary — literal `\\n` inside array literal → `Invalid or unexpected token`.
2. Patch nodes: **Help**, **Start**, **Config Summary**, **Capture Admin Reply** (+ `onError=continueRegularOutput` on builders).
3. **No-silent guard:** builder try/catch + Capture empty-`reply_text` fallback → `Не удалось сформировать ответ команды. Ошибка зафиксирована, повторите позже.`
4. Moderator `/start` shows `Имя в ответах:` from ACCESS_CONTROL `reply_sender_name`.
5. Do **not** touch Reply Profile Commands (hash must stay `961F84B02AA928CE`), Operational.dev, AI, reminders, profile numbers/names.
6. Evidence: `evidence/phase3g2-1/`. Validate Code-node parse before every text deploy.

### Phase 3G.2.2 Admin patch note

Same Admin workflow (85 nodes retained, no new workflow):

1. **Root cause:** `Check User Authorization` row projection stripped `reply_profile_*` fields; the `/start`/`/my_status` last-seen upsert then wrote ACCESS_CONTROL without those fields, wiping ADMIN_A/MOD_A profile columns on routine authenticated traffic. See `evidence/phase3g2-2/ADMIN-A-PROFILE-LOSS-ROOT-CAUSE-v1.md` and `MOD-A-SELF-PROFILE-ROOT-CAUSE-v1.md`.
2. Patch nodes: **Check User Authorization** (anti-wipe allowlist `REPLY_PROFILE_ACCESS_FIELDS`), **last-seen upsert** (write mapping sourced from top-level Prepare output via `mergeRehydrateIntoUpsert`), **Reply Profile Commands** (auto-rehydrate before formatting), **Start** (fail-closed reply-name line, rehydrate applied), **Config Summary** (Moscow timestamp, live parser-version truth, resolver-version line, reporting-sync honesty, active-recipient count).
3. Unified resolver contract: `reply-profile-resolver-v1.mjs` (new), version `iseo-reply-profile-resolver-v1.0` — see [architecture/UNIFIED-REPLY-PROFILE-RESOLVER-v1.md](../architecture/UNIFIED-REPLY-PROFILE-RESOLVER-v1.md).

### Phase 3G.2.3 Admin patch note

1. **Residual root cause:** Start Reply consumed the pre-rehydrate `Read ACCESS_CONTROL` item while `access_upsert` already carried the rehydrated `reply_sender_name` in the same execution (MOD_A `/start` → «не задано» vs `/my_reply_profile` → Михаил).
2. Patch node: **Start** only — prefer `j.access_upsert` for the reply-name line; sheet fallback; fail-closed; same resolver version stamp. Do not redesign profile commands, numbering, Operational.dev, AI, or reminders.
3. Prefer same workflow ID and same node count (85). Evidence: `evidence/phase3g2-3/`.
4. Do not change ACCESS_CONTROL schema, access roles/status, or profile numbers; do not enable AI or reminders; do not activate Sales-Manager-v2.
5. Offline harness `phase3g22-harness.mjs` **53/53 PASS**; regression `phase3g2-harness.mjs` **42/42 PASS**.
6. Evidence: `evidence/phase3g2-2/`.

### Phase 3H.4 Admin patch note

Same Admin workflow (85 nodes; workflows_created=0):

1. **Reminder Commands:** fix Admin long-form `/reminder_status` SyntaxError (literal `,\n` between array elements — exec 24194/24196).
2. **Status:** read poll heartbeat + `last_production_processed_*`; decouple synthetic test stamps.
3. **Health:** clarify on-demand probe vs scheduled poll heartbeat.
4. Temporary webhook nodes during deploy removed; final count **85**.
5. Evidence: `evidence/phase3h4/` · `implementation/REMINDER-STATUS-COMMAND-REPAIR-v1.md` · `STATUS-DATA-SOURCE-REPAIR-v1.md`.

## Phase 3H.4.1 Status patch

Admin.dev Status Code updated to `iseo-last-production-processed-v1.0` resolver. Same workflow ID `wLrLp4WQHm1VJmxz`, node count 85. No Operational.dev change.

## Phase 3H.6

Same Admin ID `wLrLp4WQHm1VJmxz`, **85** nodes retained. Patch: Reminder Commands live ACCESS recipient count (Phase 3H.6 marker). No new workflows.


### Phase 3H.7 delta
See evidence/phase3h7 and LEAD-REOPEN-CONTRACT-v1.


## Phase 3H.7.1 note
Gmail OAuth recovery closed; original terminal cards now expose `↩️ Вернуть в обработку`; MISSED_PROD_LEAD_1 resolved without replay (no absent genuine form lead); soak restarted; Phase 3I.1 blocked.
