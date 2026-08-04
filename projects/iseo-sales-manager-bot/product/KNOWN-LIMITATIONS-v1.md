# KNOWN LIMITATIONS v1

- Original lead action buttons: **repaired in Phase 3D.8**; Phase **3D.8.1** COMPLETE (Admin processed + moderator spam live). Phase **3D.8.2** adds actor display attribution and revoked-moderator visibility in `/moderator_pending`. Phase **3D.8.3** short pending labels.
- Blocked-user administration is **not** exposed via `/moderator_pending` (future backlog if needed).
- Parser **`sm-parser-v3.3`** + Lead Semantic Model **implemented** (Phase 3E.1); local harness 46/46 PASS. **Live semantic acceptance PENDING**.
- Additive Sheets columns for semantic fields may still be interim-packed into `quality_comment` until migration apply.
- Pending-lead reminders **not implemented** (draft only).
- Reusable multi-client deployment / automatic client rollout **not implemented**.
- AI ON **not approved**.
- Archive `/leads` cards remain intentionally buttonless.
- Main `X:\AI MARS` workspace is dirty with foreign WIP — commits must use clean worktrees.
- Full Sheets PII cell dumps are not part of backup packages (structure only).
