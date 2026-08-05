# KNOWN LIMITATIONS v1

- Original lead action buttons: **repaired in Phase 3D.8**; Phase **3D.8.1** COMPLETE (Admin processed + moderator spam live). Phase **3D.8.2** adds actor display attribution and revoked-moderator visibility in `/moderator_pending`. Phase **3D.8.3** short pending labels.
- Blocked-user administration is **not** exposed via `/moderator_pending` (future backlog if needed).
- Parser **`sm-parser-v3.3`** + Lead Semantic Model **COMPLETE** (Phase 3E.1 operator visual A–F PASS).
- First Reply Engine **`sm-reply-v2.1`** + Human Reply Style **`sm-human-v1.0`** + card **`sm-msg-v2.4`** shipped (Phase 3E.2.1); harness 64/64 PASS; **operator copy acceptance ATTENTION**.
- **Google Sheets has no atomic CAS** — claim → send → stamp is best-effort sequential; `claimed`/`uncertain` rows require reconciliation, not blind resend ([DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md](../architecture/DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md)).
- Sheets rate-limit / quota (429) risk mitigated by **fail-closed ledger read** (send zero cards on read error) and claim-before-send; not eliminated under all failure modes.
- Additive Sheets columns for semantic / first-reply v2 fields may still be interim-packed into `quality_comment` until migration apply.
- Pending-lead reminders **not implemented** — next phase after First Reply v2 acceptance.
- Reusable multi-client deployment / automatic client rollout **not implemented**.
- AI ON **not approved**.
- Archive `/leads` cards remain intentionally buttonless.
- Main `X:\AI MARS` workspace is dirty with foreign WIP — commits must use clean worktrees.
- Full Sheets PII cell dumps are not part of backup packages (structure only).
