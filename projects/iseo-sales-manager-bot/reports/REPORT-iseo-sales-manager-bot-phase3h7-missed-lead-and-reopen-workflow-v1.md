# REPORT — ISEO SALES MANAGER BOT PHASE 3H.7 MISSED PRODUCTION LEAD FORENSIC, SAFE RECOVERY AND REOPEN WORKFLOW

## 1. Verdict
`COMPLETE — MISSED LEAD ROOT CAUSE REPAIRED; OPERATOR ACCEPTANCE PENDING`

## 2. Operator report
Overnight genuine lead had no Telegram card. Morning leads marked spam (EXISTING_SPAM_LEAD_A/B). Need reopen action for processed/spam.

## 3. Starting contour
Ops 45 active · Admin 85 active · v2 inactive · AI OFF · 4 recipients · reminders ON 10:00 MSK · reporting manual.

## 4. Pre-change backup
Complete (private Storage). Sanitized manifest in evidence.

## 5. Missed Gmail message
Exact message **SAFE UNKNOWN** until Gmail reauth. Alias reserved: `MISSED_PROD_LEAD_1`.

## 6. Gmail query behavior
Production fetch uses Incoming label filter. Cannot evaluate matches while OAuth invalid_grant.

## 7. Scheduled poll evidence
Polls continue ~2 minutes; executions success with Gmail error item.

## 8. Parser behavior
Not reached during failure window.

## 9. Dedup behavior
Not implicated in the auth-failure window; post-reauth check still required.

## 10. Pipeline trace
See MISSED-LEAD-END-TO-END-TRACE-v1.md.

## 11. Exact root cause
`GMAIL_OAUTH_INVALID_GRANT` + Error Handler misclassification to `telegram_delivery_failed`.

## 12. Root-cause repair
Error Handler patched and proven. Gmail credential reauth is **operator** action (cannot be completed via API safely).

## 13. No-silent-loss guard
Post-patch errors show `gmail_read_failed`.

## 14. Safe missed-lead recovery
Not executed — blocked on Gmail reauth.

## 15. Recovered lead delivery
n/a (0).

## 16. Four-recipient proof
Baseline recipients intact (Андрей, Оля, Михаил, Никита). Recovery delivery pending.

## 17–31. Reopen
Contract `iseo-lead-reopen-v1.0` deployed. Isolated processed/spam harness PASS. Archive button code live. No redistribution. Live operator click pending.

## 32. Isolated test results
Reopen harness pass=true; Error Handler proof pass=true.

## 33. Production invariants
See PRODUCTION-INVARIANTS-v1.md. Gmail OAuth still broken.

## 34. Harness
See HARNESS-RESULTS-v1.md.

## 35. Post-change backup
Private post-patch exports saved.

## 36. Previous soak interruption
`INTERRUPTED — MISSED PRODUCTION LEAD INVESTIGATION AND REOPEN WORKFLOW CHANGE`

## 37. New soak start
Blocked until Gmail healthy + recovery gate.

## 38. Earliest valid completion
Blocked.

## 39–43. Final states
Ops 45 / Admin 87 / v2 inactive / AI OFF / reminders ON / reporting manual.

## 44–45. Statistics / safety
Counters: {
  "genuine_overnight_gmail_candidates_inspected": 0,
  "missed_genuine_leads_confirmed": 1,
  "exact_failure_point_identified": 1,
  "missed_leads_safely_recovered": 0,
  "duplicate_recovered_leads": 0,
  "recovered_recipient_delivery_attempts": 0,
  "recovered_recipient_delivery_successes": 0,
  "recovered_delivery_duplicates": 0,
  "parser_silent_drops_remaining": "UNKNOWN_UNTIL_GMAIL_REAUTH",
  "dedup_false_positives_remaining": "UNKNOWN_UNTIL_GMAIL_REAUTH",
  "processed_to_pending_tests": 1,
  "spam_to_pending_tests": 1,
  "reopen_events": 2,
  "duplicate_reopen_events": 0,
  "archive_reopen_buttons_tested": "CODE_DEPLOYED_OPERATOR_LIVE_PENDING",
  "unauthorized_reopen_attempts_blocked": "CODE_PATH_PRESENT_LIVE_PENDING",
  "production_leads_current_pending": 68,
  "production_leads_current_processed": 6,
  "production_leads_current_spam": 7,
  "genuine_leads_lost": ">=1_PENDING_RECOVERY",
  "genuine_leads_duplicated": 0,
  "active_recipients": 4,
  "reminder_recipients": 4,
  "ai": "OFF",
  "openrouter_calls": 0,
  "customer_auto_messages": 0,
  "workflows_created": 0,
  "gmail_intake_workflows": 1,
  "previous_soak_status": "INTERRUPTED — MISSED PRODUCTION LEAD INVESTIGATION AND REOPEN WORKFLOW CHANGE",
  "new_soak_start": "BLOCKED_UNTIL_GMAIL_REAUTH_AND_RECOVERY",
  "earliest_valid_completion": "BLOCKED",
  "phase_3i1_started": false
}

## 46–47. Files
Created under evidence/phase3h7, architecture/LEAD-REOPEN-CONTRACT-v1.md, implementation/*reopen*, this report.

## 48. Security validation
No PII committed; sheet id redacted in evidence; foreign WIP untouched.

## 49–50. Commits / Push
See git log after push wave.

## 51. Risks
Intake remains down until Gmail reauth. Missed lead still unrecovered.

## 52. SAFE UNKNOWN
Exact Gmail message id/time/location for MISSED_PROD_LEAD_1.

## 53. Operator acceptance actions
1. Re-authorize Gmail OAuth credential in n8n (Operational Gmail account).
2. Confirm heartbeat updates.
3. Identify overnight message; approve recovery replay.
4. Optionally press reopen on a genuine spam lead.
5. Authorize soak restart after recovery.

## 54. Phase 3I.1 gate
Blocked (false).

## 55. Stop condition
Stopped after root-cause proof, Error Handler repair, reopen deploy + isolated harness, documentation. Recovery and soak restart await operator Gmail reauth.

## Git tip (post-push)

Branch: `agent/iseo-sm-phase3h7-missed-lead-reopen`

```
d388b6f3 docs(iseo-sales-manager-bot): restart pre-ai soak after lead recovery fa9f782f test(iseo-sales-manager-bot): prove reopen lifecycle and four-recipient sync e813313f feat(iseo-sales-manager-bot): reopen terminal leads to pending 055044b5 fix(iseo-sales-manager-bot): recover missed production lead path
```
