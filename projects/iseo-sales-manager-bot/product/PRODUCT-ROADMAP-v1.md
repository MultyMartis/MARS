# PRODUCT ROADMAP v1

Порядок утверждён как направление; каждый пункт требует отдельного implementation charter.

1. **Product baseline + recovery** — зафиксировать live state, backups, Git tail и rollback evidence.
2. **Lifecycle button restoration** — Format fields + Send keyboard + Admin FNV token (3D.8); live callback ack/feedback + LEAD_DELIVERIES multi-copy (3D.8.1) — **COMPLETE** (operator Admin processed + moderator spam confirmed).
3. **Actor attribution + revoked moderator visibility (3D.8.2)** — ACCESS_CONTROL safe actor labels on final cards; `/moderator_pending` lists revoked former moderators with stable codes.
4. **Parser 3.3 / Lead Semantic Model (3E.1)** — **COMPLETE** — operator visual acceptance A–F PASS; verdict `PHASE 3E.1 COMPLETE — PARSER 3.3 AND LEAD SEMANTIC MODEL READY`.
5. **First Reply Engine v2 + Human Reply Style v1 (3E.2.x)** — copy layer operator-accepted; Phase 3E.2.3 call-budget and exactly-once proof COMPLETE: two claims/two sends/two stamps, five-poll zero resend. Operator visual confirmation **received** — Phase 3E.2 closed `COMPLETE — HUMAN FIRST REPLY ENGINE READY`.
6. **Pending-lead reminders (3F.1)** — engine ready historically; **activated in Phase 3H.3** (`pending_reminders_enabled=true`, 10:00 Europe/Moscow, source LEADS, tests excluded).
6b. **Phase 3H production hardening** — **IMPLEMENTATION COMPLETE — 48-HOUR SOAK STARTED** (2026-08-06): fixture cleanup, reporting MANUAL truth, Olya onboarded, three-recipient delivery proven, reminders ON. Phase 3I.1 blocked until soak PASS + explicit approval.
6c. **Phase 3H.4 soak observability repair** — **COMPLETE — SOAK RESTARTED** (2026-08-06 19:15 МСК T+0): `/reminder_status` SyntaxError fix, empty-poll heartbeat, `/status` production truth, health/status separation. Soak attempt 1 invalidated. Earliest PASS **2026-08-08 19:15 МСК**.
7. **AI ON pilot (Phase 3I.1+)** — blocked until pre-AI soak PASS and separate operator charter; AI remains OFF.
8. **Reusable client profile** — schema для изолированных config/source/storage/staff boundaries.
9. **Deployment automation** — versioned package, compatibility, migration и rollback tooling.
10. **Centralized controlled rollout** — fleet visibility и staged cohort control.

Phase 3D.8.x completed buttons/attribution/labels. Phase 3E.1 closed. Phase 3E.2 closed with operator visual confirmation. Phase 3F.1 reached the verdict: `COMPLETE — COMMANDS AND REMINDER ENGINE READY; OPERATOR ACTIVATION PENDING`.

### 3E.2 closeout

Harness, real-lead recount, quiet window, exactly-once proof, five-poll zero resend and operator visual confirmation are all complete. Phase 3E.2 is closed.

### 3F.1 acceptance order

Pending source forensic, view contract, command implementation, reminder schedule/idempotency, command authorization and a controlled live acceptance window are complete. The remaining gate before production reminders send automatically is an explicit operator activation decision (`pending_reminders_enabled=true`).

### Phase 3G.1 — INTLSEO first-contact standard

**Package ready (historical):** approved template corpus + recipient personalization + manager assist contract. Offline harness **100/100 PASS**. Live seed repaired in 3G.1.1. AI ON pilot remains a later separate charter (item 7).

### Phase 3G.2 — Profile numbers + Telegram text hygiene

**Current documentation / contract wave:** immutable `reply_profile_number`, number-based Admin commands, explicit role-aware help templates, TELEGRAM-TEXT-CONTRACT-v2, command reference, text registry. Contour unchanged: AI OFF, reminders OFF, no auto-send. Live acceptance evidence to fill under `evidence/phase3g2/`.

## Phase 3H.4.1

Complete. Last production processed `/status` readback repaired; final 48-hour soak restarted (T+0 2026-08-06 16:20 Europe/Moscow). Phase 3I.1 remains blocked until soak PASS.

## Phase 3H.5 T+0 observation

Executed 2026-08-06 19:52 Europe/Moscow. Verdict: `SOAK T+0 STOP — PRODUCTION INVARIANT VIOLATION` (MOD_C reactivation + revoked delivery). Phase 3I.1 remains blocked. No AI enablement.

## Phase 3H.6

Four-recipient baseline + reminder alignment complete. Final 48-hour pre-AI soak restarted 2026-08-06 20:28 Europe/Moscow. Phase 3I.1 blocked until soak PASS.


## Phase 3H.7

Missed-lead forensic + terminal reopen. Phase 3I.1 still blocked.
