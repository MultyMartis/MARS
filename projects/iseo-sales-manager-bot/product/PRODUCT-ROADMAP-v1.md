# PRODUCT ROADMAP v1

Порядок утверждён как направление; каждый пункт требует отдельного implementation charter.

1. **Product baseline + recovery** — зафиксировать live state, backups, Git tail и rollback evidence.
2. **Lifecycle button restoration** — Format fields + Send keyboard + Admin FNV token (3D.8); live callback ack/feedback + LEAD_DELIVERIES multi-copy (3D.8.1) — **COMPLETE** (operator Admin processed + moderator spam confirmed).
3. **Actor attribution + revoked moderator visibility (3D.8.2)** — ACCESS_CONTROL safe actor labels on final cards; `/moderator_pending` lists revoked former moderators with stable codes.
4. **Parser 3.3 / Lead Semantic Model (3E.1)** — **IMPLEMENTED** locally (`sm-parser-v3.3`, `lead-semantic-v1`, `sm-msg-v2.3`, harness 46/46); live semantic acceptance pending.
5. **Improved Telegram card** — дальнейшие UX polish после live semantic closeout.
6. **Generated first reply improvements** — baseline consistency shipped in 3E.1; further copy polish optional.
7. **Pending-lead reminders** — daily window, dedupe, pagination и staff eligibility.
8. **AI ON pilot** — только отдельный reference pilot с fallback и cost/safety evidence.
9. **Reusable client profile** — schema для изолированных config/source/storage/staff boundaries.
10. **Deployment automation** — versioned package, compatibility, migration и rollback tooling.
11. **Centralized controlled rollout** — fleet visibility и staged cohort control.

Phase 3D.8.x completed buttons/attribution/labels. Phase 3E.1 shipped Parser 3.3 semantics (AI OFF). Reminders / AI ON pilot / fleet deployment remain unimplemented.
