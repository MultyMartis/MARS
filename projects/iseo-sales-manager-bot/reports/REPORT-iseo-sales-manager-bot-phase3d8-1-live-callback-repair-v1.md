# REPORT — ISEO SALES MANAGER BOT PHASE 3D.8.1 LIVE CALLBACK REPAIR, ACTION FEEDBACK, AND TWO-ROLE ACCEPTANCE

**Date:** 2026-08-05  
**Project:** `iseo-sales-manager-bot`  
**Contour:** Operational.dev `xSnXPy8cEHoZw6xG` · Admin.dev `wLrLp4WQHm1VJmxz` · Sales-Manager-v2 inactive

## 1. Verdict

**PHASE 3D.8.1 COMPLETE — ADMIN AND MODERATOR ACTIONS READY**

*(Closeout amended in Phase 3D.8.2 using operator-confirmed live Admin processed + moderator spam clicks.)*

### Original interim verdict (superseded)

**COMPLETE — CALLBACK REPAIR READY; TWO OPERATOR CLICKS PENDING**

## 2. Operator observation

Buttons appeared after 3D.8 repair; moderator click showed loading without reliable final UX; earlier `✅ Обработан` was not proof of real Telegram callback E2E.

## 3. Real callback execution

Real Telegram Trigger callbacks from test moderator: **21584**, **21585** (~20:56 UTC). Authorized; callback `sm:p:<token>`; outcome **idempotent** (lead already processed by prior harness). AnswerCallback + Safe Reply ran. Multi-copy edit did not (LEAD_DELIVERIES missing; idempotent path pre-repair).

## 4. Earlier synthetic demo provenance

Execution **21551** — **not** a real user callback. Provenance: `P3D8 Callback Harness WH` webhook injection. Applied CLEAN processed + 1 card edit; `answerCallbackQuery` failed (fake query id).  
- real user callback: **no**  
- actor authorization path used: **yes** (injected as admin operator identity)  
- answerCallbackQuery used: **attempted / failed**  
- multi-copy update used: **no** (1 initiator fallback)

## 5. Root cause

1. **Late / fragile acknowledgement UX** — toast after Sheets path; harness fake ids failed AnswerCallback.  
2. **LEAD_DELIVERIES tab missing** — ledger read/write returned “sheet not found”; Expand fell back to single initiator card.  
3. Operator-window clicks coincided with harness Admin reconfiguration; first real clicks hit already-processed lead.

## 6. Callback acknowledgement

Admin.dev: early `Prepare Early Callback Ack` → `Answer Callback Early` (`Обрабатываю…` / malformed). Deny path text aligned. Late Answer bypassed after early ack.

## 7. Callback token resolution

`sm:p:` / `sm:s:` + FNV 12-char token; actor SHA-256 unchanged. Harness PASS.

## 8. Actor authorization

ACCESS_CONTROL by Telegram user id: admin/moderator active allowed; public/pending/revoked/blocked/missing denied.

## 9. Lifecycle transition

pending→processed / pending→spam only; idempotent + conflict texts per contract; no reversal.

## 10. CLEAN mutation

Exactly one update on applied; none on idempotent/conflict/deny.

## 11. LEAD_EVENTS

Append only on mutate-true branch (applied). Non-applied skips Append.

## 12. Initiator feedback

Early toast + durable Safe Reply / card status (`Кем: сотрудник` + Moscow time).

## 13. Multi-copy lookup

LEAD_DELIVERIES tab created + headers written; Expand ignores error items; matches `stable_lead_ref` + delivered + message refs.

## 14. Multi-copy edit

Edit node continues on fail; Aggregate reports partial vs full success.

## 15. Failure isolation

No CLEAN rollback after edit failure; partial initiator text.

## 16. Current affected lead

Prior clicked lead remains **processed** (harness mutation). Not blindly replayed. New synthetics used for acceptance.

## 17. Harness

**34/34 PASS** (local pure simulation).

## 18. Synthetic Lead A

`PHASE_3D8_1_ADMIN_PROCESSED` — Ops exec **21639** — 2 sends with buttons — 0 duplicates — LEAD_DELIVERIES append OK.

## 19. Synthetic Lead B

`PHASE_3D8_1_MODERATOR_SPAM` — Ops exec **21642** — 2 sends with buttons — 0 duplicates — LEAD_DELIVERIES append OK.

## 20. Admin processed acceptance

**PASS** — operator Андрей live click confirmed (Phase 3D.8.2 closeout).

## 21. Moderator spam acceptance

**PASS** — operator Мопс live click confirmed (Phase 3D.8.2 closeout).

## 22. Moderator lifecycle UX backlog

Draft preserved: `product/MODERATOR-LIFECYCLE-UX-SPEC-v1-DRAFT.md` (not implemented this phase).

## 23. Current access state

Андрей admin/active · Мопс moderator/active · Оля revoked · Никита revoked (unchanged).

## 24. Workflow states

Ops active 45 · Admin active **59** · Sales-Manager-v2 inactive · workflows created=0.

## 25. Safety counters

AI provider calls=0 · automatic client messages=0 · workflows created=0 · new synthetic leads sent=2 · parser runtime changes=0 · semantic runtime changes=0 · Olya role changes=0 · Nikita role changes=0.

## 26. Files created

`evidence/phase3d8-1/*` · `product/MODERATOR-LIFECYCLE-UX-SPEC-v1-DRAFT.md` · this report.

## 27. Files changed

README · OPERATIONAL-INDEX · TELEGRAM-UX / ADMIN-COMMAND contracts · ADMIN/OPS patch specs · TEST-HARNESS · OPERATOR-RUNBOOK · KNOWN-LIMITATIONS · PRODUCT-ROADMAP (scoped).

## 28. Security validation

No Telegram IDs, chat IDs, usernames, phones, emails, workbook IDs, raw callbacks, or unsanitized exports in git evidence.

## 29. Commit

`fix(iseo-sales-manager-bot): complete live lifecycle callbacks` (worktree → canonical).

## 30. Push

`origin/mars/canonical-post-recovery` (no force).

## 31. SAFE UNKNOWN

Exact human wall-clock of first unsuccessful moderator press vs harness window overlap (no Telegram Trigger callback found in 20:30–20:50 UTC).

## 32. Remaining operator actions

None for Phase 3D.8.1. Attribution naming (`Кем: сотрудник`) deferred to Phase 3D.8.2.

## 33. Stop condition

Phase 3D.8.1 closed after operator-confirmed Admin processed + moderator spam live actions.
