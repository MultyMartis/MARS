# KNOWN LIMITATIONS v1

- Original lead action buttons: **repaired in Phase 3D.8**; Phase **3D.8.1** COMPLETE (Admin processed + moderator spam live). Phase **3D.8.2** adds actor display attribution and revoked-moderator visibility in `/moderator_pending`. Phase **3D.8.3** short pending labels.
- Blocked-user administration is **not** exposed via `/moderator_pending` (future backlog if needed).
- Parser **`sm-parser-v3.3`** + Lead Semantic Model **COMPLETE** (Phase 3E.1 operator visual A–F PASS).
- First Reply Engine **`sm-reply-v2.1`** + Human Reply Style **`sm-human-v1.0`** + card **`sm-msg-v2.4`** remain operator-accepted; Phase 3E.2.3 does not redesign copy.
- **Google Sheets has no atomic CAS** — claim → send → stamp is best-effort sequential; `claimed`/`uncertain` rows require reconciliation, not blind resend ([DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md](../architecture/DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md)).
- Sheets quota remains an operational risk, but Phase 3E.2.3 live proof passed with zero quota errors: zero-write empty polls, `minutesInterval=2`, bounded reads/retries, two claims/two sends/two stamps and five-poll zero resend. Fail-closed remains mandatory.
- Additive Sheets columns for semantic / first-reply v2 fields may still be interim-packed into `quality_comment` until migration apply (deferred while quota recovers).
- Pending-lead reminders **not implemented** — next phase after dual delivery + First Reply human-copy acceptance.
- Reusable multi-client deployment / automatic client rollout **not implemented**.
- AI ON **not approved**.
- Archive `/leads` cards remain intentionally buttonless.
- Google Sheets still has no atomic CAS; static-data single-flight is not a distributed transaction. A crashed post-send path can require reconciliation, and blind resend remains forbidden.
- Full Sheets PII cell dumps are not part of backup packages (structure only).

## Phase 3E.2.3 pending limitations

Live call counts, safe real-lead recount, final two-recipient proof and five-poll zero-resend are captured. Remaining gate: operator visual confirmation. Google Sheets still lacks atomic CAS; synthetic Gmail finalization required a continue-regular-output patch and guard reconciliation.
