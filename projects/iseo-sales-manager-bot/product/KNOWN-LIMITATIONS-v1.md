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
