# REPORT — ISEO SALES MANAGER BOT PHASE 3H.7.2 REOPEN ACK FIX, CALLBACK ROUTING HARDENING AND OPERATOR-APPROVED THREE-LEAD RESEND

## 1. Verdict
PHASE 3H.7.2 COMPLETE — CALLBACK ACK FIXED; THREE REAL LEADS RESURFACED; FINAL 48-HOUR SOAK RESTARTED

## 2. Operator live evidence
Phase 3H.7.1 live: reopen mutated card correctly but ack said processed. Additional spam/processed/not-found toasts observed in same window.

## 3. Starting defect
Wrong reopen acknowledgement + Aggregate overwrite risk + non-contract reopen/idempotent strings.

## 4. Pre-change backup
Completed (workflows + CONFIG/ACCESS/CLEAN/EVENTS/DELIVERIES/ERRORS). Reminder tab names absent (ledger in CONFIG/deliveries).

## 5. Wrong reopen acknowledgement forensic
Live scan: reopen_applied=2 wrong_as_processed=2.

## 6. Exact root cause
`Aggregate Card Sync Result` else-branch set processed ack for any non-spam applied, including reopen `new_status=pending`.

## 7. Callback route matrix
See `architecture/CALLBACK-ACKNOWLEDGEMENT-CONTRACT-v1.md` / evidence CALLBACK-ROUTE-MATRIX.

## 8. One-callback-one-ack repair
Deployed `iseo-lead-callback-ack-v1.0` in Aggregate + Handle text alignment.

## 9. Lead-not-found behavior
unknown_lead → one error → stop; harness PASS.

## 10. Repeated callback idempotency
Distinct already-pending / already-processed / already-spam acks.

## 11. Terminal keyboard contract
Pending: Обработано+Спам; terminal: Вернуть в обработку.

## 12. Archive batch-size verification
Limits only 3|5|10; keyboard independent of batch size.

## 13. `/leads 3`
PASS (code + simulated first/middle/last).

## 14. `/leads 5`
PASS.

## 15. `/leads 10`
PASS (simulation; production rows sufficient for command validity).

## 16. Real lead lookup
3/3 unique; ambiguous=0.

## 17. Real lead pre-state
All three prior_status=spam.

## 18. Operator-authorized reopen
3 reopened to pending; rows created=0.

## 19. Operator-authorized resurface
`operator_resurface` exception only.

## 20. REAL_REOPEN_A result
{"attempts":4,"successes":4,"recipients":["Андрей Русецкий","Ola4seo","Мопс","Никита Шваков"]}

## 21. REAL_REOPEN_B result
{"attempts":4,"successes":4,"recipients":["Андрей Русецкий","Ola4seo","Мопс","Никита Шваков"]}

## 22. REAL_REOPEN_C result
{"attempts":4,"successes":4,"recipients":["Андрей Русецкий","Ola4seo","Мопс","Никита Шваков"]}

## 23. Four-recipient delivery
attempts=12 successes=12

## 24. Fresh card keyboard
Pending Обработано/Спам on all fresh cards.

## 25. Live button acceptance
Operator acceptance pending on resurfaced cards (packet issued).

## 26. Four-recipient status synchronization
Shared tokens; Aggregate sync path retained.

## 27. Old/new card coexistence
Stale callbacks resolve against current CLEAN status; idempotent; no new lead.

## 28. Statistics reconciliation
See COUNTER-RECONCILIATION evidence. pending_production_approx=37

## 29. Pending list
Includes reopened REAL_REOPEN_* (suffixes in private forensic).

## 30. Lead history
Terminal spam events preserved + manager_reopened appended.

## 31. Reminder eligibility
true for pending genuine leads; next 10:00 MSK window recorded.

## 32. Gmail health
last_poll_state=success

## 33. Production invariants
AI OFF; customer auto-send OFF; v2 inactive; no new durable workflows.

## 34. Harness
mandatory_pass=true

## 35. Post-change backup
Complete.

## 36. Canonical Git state
Commits/push performed in follow-up git wave from clean worktree.

## 37. New soak T+0
`2026-08-10T09:25:53.878Z`

## 38. New T+48
`2026-08-12T09:25:53.878Z`

## 39. Final workflow state
Admin nodes=87; Operational nodes=45

## 40. Final profile state
Four active recipients retained.

## 41. Final reminder state
enabled=true; recipients_cfg=4

## 42. Final AI state
ai_enabled=false

## 43. Safety counters
- wrong reopen acks before fix (scan window): 2
- wrong reopen acks after fix: 0 (code path)
- callback fallthrough executions: 0 after repair
- duplicate acknowledgement executions: 0 (contract)
- lead-not-found fallthroughs: 0
- archive batch sizes tested: 3
- requested real leads: 3
- uniquely resolved: 3
- ambiguous: 0
- real leads reopened: 3
- real lead rows created: 0
- fresh Telegram attempts: 12
- fresh Telegram successes: 12
- fresh Telegram duplicates: 0
- recipient count: 4
- AI state: OFF
- OpenRouter calls: 0
- customer auto-messages: 0
- workflows created (durable): 0
- Gmail intakes: 1
- Phase 3I.1 started: false

## 44. Files changed
projects/iseo-sales-manager-bot/** (docs/evidence/contracts) + live Admin node patches

## 45. Commits
See git log on agent/iseo-sm-phase3h72-reopen-ack

## 46. Push
origin/mars/canonical-post-recovery (no force)

## 47. SAFE UNKNOWN
Exact operator Telegram screenshots not attached; live acceptance of button clicks after resurface awaits operator.

## 48. Operator acceptance actions
Test resurfaced cards; confirm reopen ack text; archive `/leads 3|5|10` optional.

## 49. Phase 3I.1 gate
Blocked until soak completes.

## 50. Stop condition
Met for engineering completion; soak running; PASS not claimed.
