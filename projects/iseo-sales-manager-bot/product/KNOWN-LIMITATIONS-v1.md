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

# KNOWN LIMITATIONS v1

- Original lead action buttons: **repaired in Phase 3D.8**; Phase **3D.8.1** COMPLETE (Admin processed + moderator spam live). Phase **3D.8.2** adds actor display attribution and revoked-moderator visibility in `/moderator_pending`. Phase **3D.8.3** short pending labels.
- Blocked-user administration is **not** exposed via `/moderator_pending` (future backlog if needed).
- Parser **`sm-parser-v3.3`** + Lead Semantic Model **COMPLETE** (Phase 3E.1 operator visual A–F PASS).
- First Reply Engine **`sm-reply-v2.1`** + Human Reply Style **`sm-human-v1.0`** + card **`sm-msg-v2.4`** remain operator-accepted; Phase 3E.2.3 does not redesign copy.
- **Google Sheets has no atomic CAS** — claim → send → stamp is best-effort sequential; `claimed`/`uncertain` rows require reconciliation, not blind resend ([DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md](../architecture/DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md)).
- Sheets quota remains an operational risk, but Phase 3E.2.3 live proof passed with zero quota errors: zero-write empty polls, `minutesInterval=2`, bounded reads/retries, two claims/two sends/two stamps and five-poll zero resend. Fail-closed remains mandatory.
- Additive Sheets columns for semantic / first-reply v2 fields may still be interim-packed into `quality_comment` until migration apply (deferred while quota recovers).
- Pending-lead reminders are **implemented** (Phase 3F.1: `/pending_count`, `/pending_leads`, `/pending_leads_test`, `sm-pending-reminder-v1.0` daily engine) but **not activated in production** — `pending_reminders_enabled=false` until the operator explicitly turns them on. A full live dual-recipient reminder send under normal (non-quota) conditions has not yet been observed; the controlled live window reached ACCESS_CONTROL and correctly failed closed under a Sheets quota condition.
- Reusable multi-client deployment / automatic client rollout **not implemented**.
- AI ON **not approved**.
- Archive `/leads` cards remain intentionally buttonless.
- Google Sheets still has no atomic CAS; static-data single-flight is not a distributed transaction. A crashed post-send path can require reconciliation, and blind resend remains forbidden.
- Reminder ACCESS_CONTROL HTTP 429 is retried under `iseo-sheets-429-retry-v1.0`; exhaustion fails closed and does not mark the business date sent. Sustained project quota around 10:00 remains an operational risk.

- Full Sheets PII cell dumps are not part of backup packages (structure only).

## Phase 3E.2.3 pending limitations

Live call counts, safe real-lead recount, final two-recipient proof and five-poll zero-resend are captured. Operator visual confirmation is now received (see `evidence/phase3f1/PHASE3E2-FINAL-CLOSEOUT-v1.md`). Google Sheets still lacks atomic CAS; synthetic Gmail finalization required a continue-regular-output patch and guard reconciliation.

## Phase 3F.1 pending limitations

- Reminder engine implemented and command-accepted; `pending_reminders_enabled=false` in production — no automatic reminder message has been sent to real staff.
- The controlled live acceptance window reached ACCESS_CONTROL and hit the same Sheets quota class documented since Phase 3E.2.2, correctly producing zero sends rather than a partial delivery. A full non-quota dual-recipient live send remains outstanding for a future operator-authorized activation window.
- Fixture harness counters (business pending=4, tests excluded=1) reflect the offline fixture set, not the live production pending count at any given moment — see `evidence/phase3f1/PENDING-COUNT-ACCEPTANCE-v1.md`.
- `REMINDER_DELIVERIES` is a new, currently empty production tab — no historical reminder data exists to migrate.


## 3F.2.1

- Continuous automatic reporting sync on every new lead remains partial; targeted keyed resync proven for CLIENT_A.
- Operational dual-write CLEAN vs LEADS unification remains a known follow-up (not redesigned in 3F.2.1).
- Operator live Telegram acceptance still required.

## 3F.2.2

- Human event labels and Admin/moderator help rebuild are live on Admin.dev; operator visual `/help` + `/lead_history 1` after polish deploy remains the final Telegram confirmation step.
- Reminders remain OFF; no activation in this polish.

## Phase 3G.1 limitations

- ~~Live Operational/Admin patch and operator visual acceptance are **not** asserted complete~~ → live patch applied; profile seed defect **closed in 3G.1.1**
- AI assist contract is documented/tested offline but **not** globally enabled; production remains AI OFF.
- Оля/Никита may have prepared reply names but remain revoked/ineligible recipients.
- Reporting must not gain per-recipient rows; `RECIPIENT_REPLIES` / `LEAD_DELIVERIES` extension live per 3G.1 patch.

## Phase 3G.1.1 limitations

- **Seed defect closed** — ACCESS_CONTROL Q–V columns live; Admin readback matches contract.
- **Operator visual acceptance pending** (historical gate) for latest T1/T3 personalized cards (Андрей / Михаил).
- Earlier exploratory inject batches may exist in Telegram history with **empty client copy** (pre-repair); do not treat as regression.
- Do not clean acceptance fixtures until operator records visual sign-off.

## Phase 3G.2 limitations

- Username/token addressing of reply profiles is **obsolete**; number addressing is current — see `REPLY-PROFILE-ADMIN-COMMANDS-v2.md`.
- Access restoration for MOD_B_REVOKED / MOD_C_REVOKED remains **out of scope** for name/number commands.
- AI ON and reminder activation remain separate operator charters.

## Phase 3G.2.1 limitations

- Phase 3G.2 Help/Start/Config Code-node syntax defects caused **silent** Telegram failures; repaired in-place on Admin.dev (85 nodes).
- Offline silent-command harness **PASS**; **operator visual Telegram acceptance** for `/help` `/start` `/config` (Admin + moderator) remains **pending** (webhook secret blocks agent-side inject).
- No-silent recognized-command guard is live (builder try/catch + Capture fallback); does not replace operator visual confirmation.

## Phase 3G.2.2 limitations

- Root cause was a **write-side wipe**, not a display bug: routine `/start`/`/my_status` traffic rewrote ACCESS_CONTROL without carrying `reply_profile_*` fields forward. Any authenticated actor's own row could be affected the next time they send `/start`/`/my_status` before the rehydrate patch runs against it.
- **Storage restore for ADMIN_A/MOD_A is fire-on-next-command, not yet operator-confirmed live** — the agent has no direct Google Sheets API credential from the n8n management API in this session, and a Telegram webhook inject attempt returned 404. The correct values are re-derived deterministically from the approved seed the first time either actor sends a rehydrate-covered command.
- CONFIG parser-version display had drifted stale (`sm-parser-v3.2`) versus the live `Parse Lead` stamp (`sm-parser-v3.3`) since Phase 3E.1; no automatic re-sync exists for this CONFIG cell — corrected on display in this phase, but the underlying manual-sync gap for this specific cell is not eliminated as a class of risk for future parser-version bumps.
- Operator live Telegram acceptance for ADMIN_A and MOD_A restored profiles, and for the corrected `/config` output, remains **pending**.

## Phase 3G.2.3 limitations

- After 3G.2.2, `/my_reply_profile` could show the restored name while `/start` in a wiped-sheet execution still rendered `Имя в ответах: не задано` because Start read the pre-rehydrate sheet snapshot instead of `access_upsert` (proven exec 24097).
- **Repaired in-place on Admin.dev Start** (read-after-rehydrate). Offline harness **30/30 PASS**. Operator post-deploy visual `/start` as MOD_A remains **pending** (agent cannot inject Telegram updates).
- Do not treat pre-repair Telegram history (stale Start) as acceptance of 3G.2.3.

## Phase 3H.4 limitations

- Soak attempt 1 (06.08.2026 14:20 МСК) **invalidated** — 48h clock restarted at **2026-08-06 19:15 Europe/Moscow**; soak PASS unavailable until **2026-08-08 19:15 Europe/Moscow** minimum.
- Pre-repair `/reminder_status` could go **silent** for Admin due to Reminder Commands SyntaxError (exec 24194/24196) — **repaired**; offline `node --check` PASS.
- Pre-repair `/status` could show stale Gmail poll time when inbox empty (`POLLING_ACTIVE_BUT_HEARTBEAT_NOT_WRITTEN_ON_EMPTY_RUNS`) — **repaired** via `iseo-gmail-poll-heartbeat-v1.0`.
- Pre-repair `/status` could show synthetic test last-lead time (22:23 МСК) instead of production `lead_19fd2052066e18b7` (17:22 МСК) — **repaired** via `last_production_processed_*` keys.
- `/health` Gmail probe must not be interpreted as scheduled poll heartbeat — documented in `HEALTH-SEMANTIC-SEPARATION-v1.md`.
- Phase 3I.1 remains blocked until soak PASS + explicit approval.

## Phase 3H.4.1 — `/status` empty production cache

- After 3H.4, `/status` could show `нет данных` while `/stats`/`/leads` showed processed@17:22 because CONFIG `last_production_processed_*` values were empty (backfill webhook nesting). **Repaired** in 3H.4.1: cache rewritten from LEADS; Status uses `iseo-last-production-processed-v1.0`.
- Synthetic `last_lead_success_at` (22:23) remains in CONFIG as a technical stamp but must not drive the production `/status` line.

## Phase 3H.6 note

- CONFIG `pending_reminder_active_recipients_count` is a cache; `/reminder_status` now prefers live ACCESS. Refresh cache when the approved staff set changes.
- Three-recipient contract is historical; production baseline is four recipients.


## Phase 3H.7

- Gmail OAuth refresh token can invalidate and stop all intake; errors must surface as `gmail_read_failed`.
- Reopen does not resend Telegram cards automatically.
- Exact missed Gmail message recovery requires live mailbox access.


## Phase 3H.7.1 note
Gmail OAuth recovery closed; original terminal cards now expose `↩️ Вернуть в обработку`; MISSED_PROD_LEAD_1 resolved without replay (no absent genuine form lead); soak restarted; Phase 3I.1 blocked.

## Phase 3H.7.2 note
Callback acknowledgement contract `iseo-lead-callback-ack-v1.0` deployed. Reopen ack is «Лид возвращён в обработку.». Aggregate no longer maps pending applied→processed. Operator-approved resurface of three genuine leads completed for acceptance; global reopen still does not fan out. Soak restarted; Phase 3I.1 blocked. See `evidence/phase3h72/`.



- **KNOWN FOLLOW-UP — CLEAN DUPLICATE ROW PRODUCTION SOURCE FORENSIC** (Phase 3H.8.2.2 deferred): duplicate CLEAN rows inflate naive counts; reminder selector now resolves authoritative unique pending without deleting historical copies.

