# PRODUCT ROADMAP v1

Порядок утверждён как направление; каждый пункт требует отдельного implementation charter.

1. **Product baseline + recovery** — зафиксировать live state, backups, Git tail и rollback evidence.
2. **Lifecycle button restoration** — Format fields + Send keyboard + Admin FNV token (3D.8); live callback ack/feedback + LEAD_DELIVERIES multi-copy (3D.8.1) — **COMPLETE** (operator Admin processed + moderator spam confirmed).
3. **Actor attribution + revoked moderator visibility (3D.8.2)** — ACCESS_CONTROL safe actor labels on final cards; `/moderator_pending` lists revoked former moderators with stable codes.
4. **Parser 3.3 / Lead Semantic Model (3E.1)** — **COMPLETE** — operator visual acceptance A–F PASS; verdict `PHASE 3E.1 COMPLETE — PARSER 3.3 AND LEAD SEMANTIC MODEL READY`.
5. **First Reply Engine v2 + Human Reply Style v1 (3E.2.x)** — copy layer operator-accepted; Phase 3E.2.3 call-budget and exactly-once proof COMPLETE: two claims/two sends/two stamps, five-poll zero resend. Operator visual confirmation **received** — Phase 3E.2 closed `COMPLETE — HUMAN FIRST REPLY ENGINE READY`.
6. **Pending-lead reminders (3F.1)** — **COMPLETE — COMMANDS AND REMINDER ENGINE READY; OPERATOR ACTIVATION PENDING**: `/pending_leads`, `/pending_count`, `/pending_leads_test`, configurable daily reminder (`sm-pending-reminder-v1.0`, default 10:00 Europe/Moscow), active recipients only, pending lifecycle only, deduplicated reminder windows (`REMINDER_DELIVERIES` ledger). Implemented and live-command-accepted; `pending_reminders_enabled=false` until explicit operator activation.
7. **AI ON pilot** — только отдельный reference pilot с fallback и cost/safety evidence.
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
