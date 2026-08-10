# REPORT — ISEO Sales Manager Bot — Phase 3H.7.3.2 Live Telegram Card Edit

## 1. Verdict

`PHASE 3H.7.3.2 TECHNICAL REPAIR COMPLETE — OPERATOR LIVE CARD-EDIT ACCEPTANCE REQUIRED`

Allowed semantic alias: technical repair proven; operator-visible COMPLETE deferred per Task R.

## 2. Live operator defect

Status mutation + semantic acknowledgements succeeded; the Telegram card the operator was looking at did **not** change after Spam / Reopen.

## 3. Exact one-card trace

LIVE_CARD_PROOF_1 · exec `27669` (Spam): callback → applied → LEADS spam → Expand selected stale MSG_883 → editMessageText → initiator `message to edit not found` → ack still spam. Full step list: `evidence/phase3h732/ONE-CARD-MESSAGE-REFERENCE-TRACE-v1.md`.

## 4. Operator-visible message reference

CHAT_A · MSG_898 · acceptance_canonical · 2026-08-10T10:24:43Z · clicked by operator.

## 5. Workflow-selected message reference (pre-repair)

CHAT_A · MSG_883 · operator_resurface_parity · 2026-08-10T09:42:57Z · selected by Expand v1.1.

## 6. Root cause

Exclusive-scoring bug in authoritative selection: `operator_resurface_parity` matched both the parity (+120) and substring `operator_resurface` (+100) → score 220, beating `acceptance_canonical` (160). Newer operator-visible cards lost to older parity rows. Secondary: Aggregate could report partial ok while initiator visible card untouched.

## 7. Message-reference persistence

MSG_898 was persisted correctly for the initiator acceptance_canonical row. Defect was selection, not missing send persistence for that visible card.

## 8. Authoritative-instance selection

Deployed `iseo-authoritative-card-instance-v1.2`: exclusive delivery-class scores, stronger recency, archive exclusion, callback-initiator message preference. Post-fix simulation targets MSG_898 for initiator.

## 9. Telegram edit operation

`editMessageText` via n8n Telegram nodes `Edit Lead Card Message` / `Edit Lead Card Message Pending` with HTML + inline keyboard.

## 10. Telegram API response

Pre-repair initiator: failure class `message_to_edit_not_found`. Other three: `ok=true` on stale message IDs (not operator-visible initiator card).

## 11. Single-card Spam proof

PENDING — operator visual acceptance required after repair deploy.

## 12. Single-card Reopen proof

PENDING — operator visual acceptance required.

## 13. Same-message-ID proof

PENDING live. Pre-repair proved mismatch MSG_898 vs MSG_883. Post-repair sim: same-ID targeting restored for initiator.

## 14. Four-card Spam proof

BLOCKED until single-card PASS (Task J/K).

## 15. Four-card Reopen proof

BLOCKED until single-card PASS.

## 16. Archive/current separation

Archive / pending-view deliveries excluded in Expand v1.2.

## 17. Full-body preservation

Handle Callback Action remains on Phase 3H.7.3.1 full canonical status body (interest/quality/reply + attribution). No renderer redesign this phase.

## 18. No-new-fanout proof

No new LEADS rows · no new delivery fanout · no workflows created · edits only.

## 19. Harness

`implementation/harness/phase3h732-card-edit-targeting-harness.mjs` → **17/17 PASS** (static). Live tests 16–25 pending operator.

## 20. Post-change backup

`evidence/phase3h732/POST-CHANGE-BACKUP-MANIFEST-v1.md` (Admin.dev post SHA recorded).

## 21. Canonical Git

Worktree from `origin/mars/canonical-post-recovery` @ `4b6ac0ad` containing `ecfee9f7`. Scope: `projects/iseo-sales-manager-bot/**`. Dirty `X:\AI MARS` not used for mutations.

## 22. Operator acceptance required

Operator must confirm on LIVE_CARD_PROOF_1:
1. Spam → same message body+keyboard change to Reopen
2. Reopen → same message restores pending keyboard

Until then soak must not restart.

## 23. Soak status

All prior soak timing invalidated. **Soak NOT restarted** this phase.

## 24. Phase 3I.1 gate

Blocked. AI remains OFF.

## Counters

| Counter | Value |
|---|---|
| live callbacks inspected | 5 (27669,27668,27551,27535,27534) |
| status mutations successful | ≥4 in inspected set |
| authoritative current cards discovered | 4 / lead (post-repair sim) |
| invalid current references | 1 initiator stale target pre-repair |
| Telegram edits attempted (27669) | 4 |
| Telegram edits API-success (27669) | 3 (stale) + 1 fail |
| operator-visible cards proven changed | 0 (this agent session) |
| stale instances excluded | scoring fix excludes parity when acceptance exists |
| archive instances excluded | yes (v1.2 filter) |
| new Telegram cards sent | 0 |
| new LEADS rows | 0 |
| duplicate events | 0 known |
| active recipients | 4 |
| AI state | OFF |
| OpenRouter calls | 0 |
| workflows created | 0 |
| soak restarted | 0 |
| Phase 3I.1 started | 0 |
