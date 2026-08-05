# PRODUCT ROADMAP v1

Порядок утверждён как направление; каждый пункт требует отдельного implementation charter.

1. **Product baseline + recovery** — зафиксировать live state, backups, Git tail и rollback evidence.
2. **Lifecycle button restoration** — Format fields + Send keyboard + Admin FNV token (3D.8); live callback ack/feedback + LEAD_DELIVERIES multi-copy (3D.8.1) — **COMPLETE** (operator Admin processed + moderator spam confirmed).
3. **Actor attribution + revoked moderator visibility (3D.8.2)** — ACCESS_CONTROL safe actor labels on final cards; `/moderator_pending` lists revoked former moderators with stable codes.
4. **Parser 3.3 / Lead Semantic Model (3E.1)** — **COMPLETE** — operator visual acceptance A–F PASS; verdict `PHASE 3E.1 COMPLETE — PARSER 3.3 AND LEAD SEMANTIC MODEL READY`.
5. **First Reply Engine v2 + Human Reply Style v1 (3E.2.x)** — copy layer operator-accepted; Phase 3E.2.3 call-budget and exactly-once proof COMPLETE: two claims/two sends/two stamps, five-poll zero resend. Operator visual confirmation pending.
6. **Pending-lead reminders** — **next product phase after 3E.2.3 exactly-once + visual confirmation**: `/pending_leads`, `/pending_count`, configurable daily reminder (default 10:00), timezone, active recipients only, pending lifecycle only, deduplicated reminder windows. **Not implemented in 3E.2.3.**
7. **AI ON pilot** — только отдельный reference pilot с fallback и cost/safety evidence.
8. **Reusable client profile** — schema для изолированных config/source/storage/staff boundaries.
9. **Deployment automation** — versioned package, compatibility, migration и rollback tooling.
10. **Centralized controlled rollout** — fleet visibility и staged cohort control.

Phase 3D.8.x completed buttons/attribution/labels. Phase 3E.1 closed. Phase 3E.2.3 reached the pre-visual verdict: `COMPLETE — EXACTLY-ONCE PROOF DELIVERED; OPERATOR VISUAL CONFIRMATION PENDING`.

### 3E.2.3 acceptance order

Harness, real-lead recount, quiet window, exactly-once proof and five-poll zero resend are complete. Operator visual confirmation is the stop gate. Reminders remain a separate later charter.
