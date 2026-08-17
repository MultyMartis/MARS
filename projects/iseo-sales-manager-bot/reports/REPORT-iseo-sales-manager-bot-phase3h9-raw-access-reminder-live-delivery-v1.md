# REPORT — ISEO-SALES-MANAGER-BOT PHASE 3H.9 RAW ACCESS AND REMINDER LIVE-DELIVERY

**Process-line:** ISEO-SALES-MANAGER-BOT — PHASE 3H.9 RAW-LEAD ACCESS REPAIR AND REMINDER LIVE-DELIVERY FORENSIC  
**Captured:** 2026-08-17 Europe/Moscow  

## 1. Verdict

`ATTENTION — RAW ACCESS FIXED BUT REMINDER ROOT CAUSE STILL ACTIVE`

False permission deny on raw lead is patched (registry/credential failure now has a distinct operator text). Reminder 10:00 still cannot send until the operator reconnects Google Sheets OAuth (`invalid_grant`). Soak not restarted. Phase 3I.1 blocked.

## 2. Operator evidence

- One ADMIN_A raw button worked (08:41 MSK).
- Later ADMIN_A raw button returned a permission deny (14:26 MSK) while ACCESS/CONFIG were unreadable.
- ADMIN_A and MOD_B did not receive 15–17 Aug 10:00 reminders; live traces show **zero Telegram reminder attempts**.

## 3. Raw access PASS case

RAW_ACCESS_PASS_LEAD — exec **33304**, 2026-08-17 08:41 MSK, ADMIN_A, `sm:i:`, authorized admin, `manager_raw_source_viewed`.

## 4. Raw access DENIED case

RAW_ACCESS_DENIED_LEAD — exec **33500** (33501/33502 same burst), 2026-08-17 14:26 MSK, same ADMIN_A, `sm:i:`, `deny_reason=registry_unavailable`, Handle not reached, Answer Callback Deny hardcoded permission text.

## 5. Raw access root cause

Sheets OAuth `invalid_grant` on ACCESS+CONFIG, then **wrong operator-facing deny string**. Not a staff-set hole and not missing-payload-as-permission.

## 6. Raw access repair

`deny_reply` + Answer Callback Deny expression; unauthorized = `Недостаточно прав.`; registry down = service unavailable; missing raw = distinct not-found copy.

## 7. Raw access live ADMIN_A proof

Historical PASS proven. Post-patch live retest **blocked** by the same OAuth failure (would now show service unavailable, not permission). Isolated harness 21/21. Moderator tests 0.

## 8. Reminder Aug 15 window

Saturday. Trigger 10:00 and 10:15 ran. CONFIG invalid_grant. ERROR_BEFORE_EVALUATION. Weekend skip not evaluated. SHOULD_SKIP_ZERO_PENDING not applicable; class **INCONCLUSIVE** on pending + **ERROR_BEFORE_EVALUATION**. No send.

## 9. Reminder Aug 16 window

Sunday. Same as Aug 15.

## 10. Reminder Aug 17 window

Monday SHOULD_SEND if pending≥1 (pending not_computed). Exec 33349/33358: CONFIG invalid_grant, claims 0, Telegram 0, last_window not marked. Operator non-receipt matches traces.

## 11. Schedule executions

All listed 10:00/10:15 slots **TRIGGER_RAN**. No missing trigger. No wrong time.

## 12. Pending state by window

Authoritative pending_count = **not_computed** for 15–17 Aug 10:00 (CLEAN unread). Do not use today's statuses retroactively.

## 13. 429 retry live behavior

Retry Wait **not executed**. 429 events in these windows: **0**. Classifier called the OAuth error SHEETS_PERMANENT.

## 14. Current-state selector live behavior

Selector node **not entered** in these windows. Source still has `iseo-reminder-current-state-selector-v1.0`.

## 15. Recipient resolution

Not reached. Production set remains 4; ADMIN_A/MOD_B not proven included in-window.

## 16. Claims

Never created on these windows.

## 17. Telegram sends

Attempts 0, successes 0, failed recipient deliveries 0 (no attempts).

## 18. Mark-window ordering

Complete flag false. last_window not written. Observability writes attempted and failed on OAuth.

## 19. 10:15 recovery

Ran; not suppressed by last_window; same CONFIG failure.

## 20. Reminder root cause

Primary: Sheets OAuth invalid_grant on CONFIG before evaluation. Secondary: classifier string-error gap.

## 21. Reminder repair

Classifier now SHEETS_CREDENTIALS. Cannot send until credential reconnect. 429 path, selector, 4 recipients, 10:00 MSK preserved.

## 22. ADMIN_A-only test

Isolated only. Live ADMIN_A reminder/raw tests **not sent** (Sheets down). moderator=0 customer=0.

## 23. Reminder observability

Cannot live-read CONFIG now. No proof of false SENT. Window not marked complete.

## 24. Current genuine pending state

SAFE UNKNOWN (Sheets unreadable). Genuine leads not mutated.

## 25. Next natural 10:00 acceptance

**2026-08-18 10:00 Europe/Moscow** (Tue) after operator reconnects Sheets. Do not manually fire 4-recipient production reminder. Leave genuine pending leads untouched.

## 26. Production invariants

Ops active 45 · Admin active 100 · v2 inactive · recipients design=4 · reminders 10:00 Europe/Moscow · reporting manual · AI OFF · OpenRouter 0 · customer auto-send 0 · workflows created 0.

**Gmail intake health:** SAFE UNKNOWN for post-10:00 writes — Operational uses the **same** Sheets credential; intake fetch may still run while CLEAN/RAW writes fail.

## 27. Post-change backup

See `evidence/phase3h9/POST-CHANGE-BACKUP-MANIFEST-v1.md`. Sensitive JSON in STORAGE incoming.

## 28. Git

Clean worktree from `origin/mars/canonical-post-recovery` @ `17841535`. Scope `projects/iseo-sales-manager-bot/**`. Dirty `X:\AI MARS` not used.

## 29. Soak state

**NOT RESTARTED.** Final soak only after raw production acceptance **and** a natural 10:00 4-recipient PASS.

## 30. Phase 3I.1 gate

**BLOCKED.**

### Counters

| Metric | Value |
|---|---|
| raw access live cases inspected | 5 (PASS 33304 + DENIED 33500/33501/33502 + unavailable 32669) |
| authorized raw access successes | 1 in-window ADMIN_A (33304) plus earlier Aug 16 viewed execs |
| false permission denials | 3 (33500–33502) |
| raw payload missing cases | 0 in this pair (denied path never looked up RAW) |
| reminder windows inspected | 6 (15–17 Aug × 10:00/10:15) |
| should-send windows | 1 expected (17 Aug) — pending INCONCLUSIVE |
| schedule executions | 6 |
| 429 events | 0 in these windows |
| retry recoveries | 0 |
| authoritative pending counts | not_computed |
| production recipients resolved | 0 (resolver not reached) |
| claims created | 0 |
| Telegram attempts | 0 |
| Telegram successes | 0 |
| failed recipient deliveries | 0 |
| premature window-complete events | 0 |
| ADMIN_A test messages sent | 0 |
| moderator test messages sent | 0 |
| customer test messages sent | 0 |
| current genuine pending leads | SAFE UNKNOWN |
| AI state | OFF |
| OpenRouter calls | 0 |
| workflows created | 0 |
| soak restarted | 0 |
| Phase 3I.1 started | 0 |

## Operator acceptance packet

**Raw lead:** After Google Sheets credential reconnect in n8n, on any current ADMIN_A card press `📄 Исходная заявка`. Expect the original submission (or truthful not-found / empty-body), **never** «Недостаточно прав.» if you are ADMIN_A. If Sheets is still disconnected, expect «Сервис временно недоступен. Попробуйте позже.»

**Reminder:** Real 4-recipient PASS still requires the next natural 10:00 after credential reconnect. No ADMIN_A live reminder Telegram was sent in this phase.

## Execution safety

- cwd worktree: `X:\AI MARS STORAGE\git-sync-iseo-sm-phase3h9-20260817-183611\repo`
- scope lock honored: yes (`projects/iseo-sales-manager-bot/**` + STORAGE incoming)
- destructive ops: none (`git clean` / recursive delete not used). TMP workflows created then deleted by id.
- protected zone touch: none
