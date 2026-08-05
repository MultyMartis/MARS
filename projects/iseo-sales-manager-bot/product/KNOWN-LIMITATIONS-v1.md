# KNOWN LIMITATIONS v1

- Original lead action buttons: **repaired in Phase 3D.8**; Phase **3D.8.1** COMPLETE (Admin processed + moderator spam live). Phase **3D.8.2** adds actor display attribution and revoked-moderator visibility in `/moderator_pending`. Phase **3D.8.3** short pending labels.
- Blocked-user administration is **not** exposed via `/moderator_pending` (future backlog if needed).
- Parser **`sm-parser-v3.3`** + Lead Semantic Model **COMPLETE** (Phase 3E.1 operator visual A–F PASS).
- First Reply Engine **`sm-reply-v2.1`** + Human Reply Style **`sm-human-v1.0`** + card **`sm-msg-v2.4`** shipped; harness 59/59 (3E.2.2); **operator copy acceptance PENDING**.
- **Google Sheets has no atomic CAS** — claim → send → stamp is best-effort sequential; `claimed`/`uncertain` rows require reconciliation, not blind resend ([DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md](../architecture/DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md)).
- Sheets rate-limit / quota (429): isolated probes can PASS while **full multi-op delivery path** still fails on ACCESS_CONTROL/claim under load — Phase 3E.2.2 verdict **`ATTENTION — SHEETS DELIVERY PATH STILL RATE-LIMITED`**; fail-closed (send zero) preserved; ACCESS_CONTROL now fail-closed.
- Additive Sheets columns for semantic / first-reply v2 fields may still be interim-packed into `quality_comment` until migration apply (deferred while quota recovers).
- Pending-lead reminders **not implemented** — next phase after dual delivery + First Reply human-copy acceptance.
- Reusable multi-client deployment / automatic client rollout **not implemented**.
- AI ON **not approved**.
- Archive `/leads` cards remain intentionally buttonless.
- Main `X:\AI MARS` workspace is dirty with foreign WIP — commits must use clean worktrees.
- Full Sheets PII cell dumps are not part of backup packages (structure only).
