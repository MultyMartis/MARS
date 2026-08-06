# REPORT — ISEO SALES MANAGER BOT PHASE 3H.6 FOUR-RECIPIENT BASELINE, REMINDER ALIGNMENT AND SOAK RE-CHARTER

## 1. Verdict

`PHASE 3H.6 COMPLETE — FOUR-RECIPIENT BASELINE ALIGNED; FINAL 48-HOUR SOAK RESTARTED`

## 2. Operator decision

MOD_C / Никита intentionally restored; must remain active card recipient with name Никита and personalization enabled; approved set = four.

## 3. Obsolete emergency interpretation

Revoked-recipient reactivation incident remediation prompt was **not executed** and is obsolete.

## 4. Historical T+0 erratum

Original STOP preserved. Corrected to `SOAK T+0 INVALIDATED — OPERATOR-APPROVED RECIPIENT SET CHANGED FROM 3 TO 4`. See erratum report.

## 5. Starting contour

Ops 45 active · Admin 85 active · v2 inactive · AI OFF · reminders ON · CONFIG recipients display cache 3 · live ACCESS 4.

## 6. Pre-change backup

Complete (private Storage). Manifest committed sanitized.

## 7. MOD_C restore authorization

ACCESS_EVENTS `moderator_approved` / `moderator_add` at 06.08.2026 16:54:29 МСК (revoked→active). Then `/reply_name_enable 4`.

## 8. Four-profile state

1 Андрей · 2 Оля · 3 Михаил · 4 Никита — all active/enabled.

## 9. Profile number integrity

Numbers 1–4 · blank 0 · duplicates 0.

## 10. MOD_C personalization

Enabled; intro Никита / INTLSEO.

## 11. Card recipient selector

Dynamic Expand Delivery Recipients → 4.

## 12. Four-profile renderer proof

4/4 intros PASS; Мопс=0.

## 13. Four-recipient Telegram proof

4/4 successes; label `🧪 Проверка четырёх получателей`.

## 14. Personalized names

Андрей / Оля / Михаил / Никита correct.

## 15. Reminder starting discrepancy

`/config`=4 · `/reminder_status`=3.

## 16. Reminder recipient forensic

Send path dynamic ACCESS; status path stale CONFIG cache.

## 17. Count-three root cause

`pending_reminder_active_recipients_count=3` stale after MOD_C restore.

## 18. Unified recipient count contract

`iseo-four-recipient-baseline-v1.0` + live ACCESS preference for status.

## 19. Reminder repair

CONFIG→4; Reminder Commands Phase 3H.6 live ACCESS count; time unchanged.

## 20. `/reminder_status` result

Получателей: **4** · включены · 10:00 · Europe/Moscow · tests/archives excluded · once-per-day excluded.

## 21. Four-recipient reminder proof

4/4 isolated test window PASS.

## 22. Exactly-once reminder proof

Pass2 additional sends = 0.

## 23. Partial failure behavior

Recipient-scoped claims; harness PASS.

## 24. Command acceptance

Admin battery PASS for required commands (reminder_status proven on patched live code).

## 25. MOD_C acceptance

Technical PASS; native visual battery may be operator-confirmed.

## 26. Genuine production lead reconciliation

PROD_LEAD_1 processed preserved; lost/duplicated=0.

## 27. Production statistics

Pending 0 · clean LEADS business row 1 · events/deliveries historical retained.

## 28. Production invariants

All required final-state invariants PASS.

## 29. Harness

80/80 PASS.

## 30. Post-change backup

Complete (private).

## 31. Four-recipient production baseline

`product/PRODUCTION-BASELINE-PRE-AI-SOAK-FOUR-RECIPIENT-v1.md`

## 32. Previous soak attempts

1 observability repair · 2 last-processed repair · 3 **INVALIDATED — OPERATOR-APPROVED BASELINE CHANGE**

## 33. New soak start

**2026-08-06 20:28 Europe/Moscow**

## 34. Earliest valid completion

**2026-08-08 20:28 Europe/Moscow**

## 35. Checkpoint schedule

T+6 07.08.2026 02:28 · first 10:00 07.08.2026 10:00 · T+24 07.08.2026 20:28 · T+36 08.08.2026 08:28 · T+48 08.08.2026 20:28

## 36. Final workflow state

Ops 45 · Admin 85 · v2 inactive · net workflows created 0.

## 37. Final profile state

Four complete active profiles 1–4.

## 38. Final access state

Revoked staff recipients 0 among approved set.

## 39. Final card recipient state

4/4.

## 40. Final reminder state

ON · 10:00 Europe/Moscow · recipients 4 · ledger test rows 0.

## 41. Final reporting state

Manual.

## 42. Final AI state

OFF.

## 43. Safety counters

| Counter | Value |
|---|---:|
| operator-authorized recipient restorations | 1 |
| historical incident classifications corrected | 1 |
| profile rows | 4 |
| profile numbers present | 4 |
| blank profile numbers | 0 |
| duplicate profile rows | 0 |
| active profiles | 4 |
| revoked profiles | 0 |
| active card recipients | 4 |
| active reminder recipients | 4 |
| card test leads | 1 |
| card drafts | 4 |
| card delivery attempts | 4 |
| card delivery successes | 4 |
| card duplicates | 0 |
| reminder test fixtures | 1 |
| reminder claims | 4 |
| reminder delivery attempts | 4 |
| reminder delivery successes | 4 |
| reminder duplicates | 0 |
| repeated reminder checks with zero sends | 1 |
| production pending count | 0 |
| genuine production leads inspected | ≥1 |
| genuine production leads lost | 0 |
| genuine production leads duplicated | 0 |
| historical deliveries rewritten | 0 |
| reporting mode | manual |
| reminders enabled | true |
| reminder time | 10:00 |
| AI state | OFF |
| OpenRouter calls | 0 |
| customer auto-messages | 0 |
| Operational node count | 45 |
| Admin node count | 85 |
| workflows created (net) | 0 |
| Gmail intake workflows | 1 |
| pre-change backup complete | yes |
| post-change backup complete | yes |
| previous soak status | INVALIDATED — OPERATOR-APPROVED BASELINE CHANGE |
| new soak start | 2026-08-06 20:28 Europe/Moscow |
| earliest valid completion | 2026-08-08 20:28 Europe/Moscow |
| Phase 3I.1 started | 0 |


## 44. Files created

evidence/phase3h6-four-recipient/* · architecture/FOUR-RECIPIENT-* · UNIFIED-STAFF-* · implementation/FOUR-RECIPIENT-REMINDER-ALIGNMENT-v1.md · product/PRODUCTION-BASELINE-PRE-AI-SOAK-FOUR-RECIPIENT-v1.md · reports/ERRATUM-* · this report

## 45. Files changed

OPERATIONAL-INDEX · README · CURRENT/PRE-AI baselines · contracts · runbooks · original T+0 report (erratum banner only) · Admin Reminder Commands (live)

## 46. Security validation

No credentials, Telegram IDs, customer PII, workbook IDs, or raw exports committed.

## 47. Commits

See git log on `agent/iseo-sm-phase3h6-four-recipient` (four planned commits).

## 48. Push

`origin/mars/canonical-post-recovery` fast-forward (no force).

## 49. Risks

CONFIG cache can drift again if ACCESS changes without refresh — mitigated by live ACCESS preference in `/reminder_status`.

## 50. SAFE UNKNOWN

Exact native MOD_C Telegram visual transcript not captured in this agent session; operator live commands cited as authoritative for enablement.

## 51. Remaining operator actions

Optional: visual MOD_C command battery; observe soak checkpoints; do not enable AI.

## 52. Phase 3I.1 gate

**Blocked** until four-recipient soak PASS + explicit approval.

## 53. Stop condition

Stop after four-recipient baseline aligned, erratum committed, proofs PASS, soak restarted, Phase 3I.1 not started — **met**.
