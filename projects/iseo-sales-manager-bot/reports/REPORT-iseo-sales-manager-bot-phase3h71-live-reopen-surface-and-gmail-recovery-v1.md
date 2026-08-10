# REPORT — ISEO SALES MANAGER BOT PHASE 3H.7.1 LIVE REOPEN BUTTON SURFACE REPAIR AND GMAIL RECOVERY CLOSEOUT

## 1. Verdict
`COMPLETE — GMAIL HEALTHY; REOPEN BUTTON LIVE; OPERATOR ACCEPTANCE PENDING`

Live Telegram original-card reopen keyboard repaired and proven. Gmail intake healthy after operator OAuth reauth. MISSED_PROD_LEAD_1 resolved without replay. Fresh 48h soak started. Phase 3I.1 remains blocked. Operator should confirm reopen on `/leads` / optional genuine spam restore manually.

## 2. Operator live evidence
- Gmail re-authorized; two genuine leads arrived (LIVE_SPAM_LEAD_A/B).
- Operator marked both spam; cards went terminal but reopen button missing (confirmed defect).

## 3. Gmail post-reauth health
- success polls (sample): 12
- active invalid_grant (sample): 0
- last success: 2026-08-10T08:44:06.073Z
- gmail_read_failed not blocking current polls

## 4. Missed overnight lead resolution
State: **RESOLVED_NO_REPLAY**
Replay count: **0**

## 5. Starting reopen defect
Original terminal Edit Lead Card Message used empty inline keyboard; terminal apply did not attach reopen markup.

## 6. Live spam execution forensic
Pre-patch spam executions: edit_keyboard_mode=null, remove_keyboard=true, used Edit Lead Card Message, has_reopen_markup=false.

## 7. Exact missing-button root cause
Terminal mutation path never called `buildReopenButtons`; false branch of IF Pending Action Keyboard edited text with empty keyboard.

## 8. Deployed Phase 3H.7 verification
Callback `sm:r:` + reopen mutation + archive button were live; original-card terminal keyboard surface was not.

## 9. Original terminal-card builder
Shared `buildReopenButtons` + `Edit Lead Card Message` reopen row; `edit_keyboard_mode:'reopen'`.

## 10. Archive-card builder
Unchanged Phase 3H.7 Recent Leads reopen button (still live).

## 11. Live patch
Admin.dev `wLrLp4WQHm1VJmxz` patched in place; nodes=87 unchanged; no workflows created.

## 12. Spam terminal button proof
Live Telegram harness spam edit buttons: ["↩️ Вернуть в обработку"]

## 13. Processed terminal button proof
Live Telegram harness processed edit buttons: ["↩️ Вернуть в обработку"]

## 14. Archive spam proof
Recent Leads contains reopen label (deploy verify).

## 15. Archive processed proof
Same archive builder.

## 16. Spam-to-pending proof
Harness fixture: spam → pending, reopen events=1

## 17. Processed-to-pending proof
Harness fixture: processed → pending, reopen events=1

## 18. Idempotency
Second reopen while pending → `Заявка уже находится в обработке.`; fixture reopen events=1.

## 19. Four-recipient synchronization
Expand Card Sync Copies spreads Handle fields; post-reauth leads had delivery_count=4.

## 20. Authorization
No ACL changes; Admin+Mods remain authorized for reopen.

## 21. Counter reconciliation
See evidence COUNTER-RECONCILIATION-v1.md; genuine spam left unchanged.

## 22. Error observability
Phase 3H.7 Error Handler gmail_read_failed classification retained; current polls healthy.

## 23. Production invariants
Operational active; Admin active; v2 inactive; recipients=4; AI OFF; Gmail intakes=1; workflows created=0.

## 24. Harness
See evidence/phase3h71/HARNESS-RESULTS-v1.md — UX pass=true, sheet pass keys all true.

## 25. Canonical integration
Phase 3H.7 cherry-picked onto clean worktree; 3H.7.1 commits follow on same branch for push to canonical lineage.

## 26. Post-change backup
Private `runtime/backups/post-change/` refreshed.

## 27. New soak start
T+0 UTC: `2026-08-10T08:59:25.216Z`

## 28. Earliest T+48
`2026-08-12T08:59:25.216Z`

## 29. Final workflow state
Ops nodes=45 active=true; Admin nodes=87 active=true; v2 active=false

## 30. Final profile state
Андрей/Оля/Михаил/Никита profiles 1–4 active.

## 31. Final reminder state
Unchanged (reminders remain ON per prior baseline; not modified this phase).

## 32. Final AI state
AI OFF; OpenRouter calls=0; customer auto-send=0.

## 33. Safety counters
- post-reauth successful polls: 12
- active invalid_grant errors: 0
- new real leads after reauth: 2
- missed overnight lead resolved: 1
- missed lead replay count: 0
- duplicate recovered leads: 0
- terminal spam cards inspected: 3
- original reopen buttons visible (harness): 2
- archive reopen buttons visible (code): 1
- spam→pending tests: 1
- processed→pending tests: 1
- duplicate reopen events: 0
- duplicate lead rows: 0
- duplicate delivery rows: 0
- new-card sends on reopen: 0
- four-recipient synchronized cards: contract+delivery_count=4
- unauthorized reopen attempts blocked: (unchanged gate; not re-attacked)
- active recipients: 4
- reminder recipients: 4
- AI state: OFF
- OpenRouter calls: 0
- customer auto-messages: 0
- workflows created: 0
- Gmail intake workflows: 1
- Operational node count: 45
- Admin node count: 87
- Phase 3H.7 commits on canonical lineage: yes (via cherry-pick)
- new soak start: 2026-08-10T08:59:25.216Z
- earliest valid completion: 2026-08-12T08:59:25.216Z
- Phase 3I.1 started: 0

## 34. Files changed
`projects/iseo-sales-manager-bot/**` evidence/docs/implementation/architecture/guides/reports under Phase 3H.7.1.

## 35. Commits
See git log on `agent/iseo-sm-phase3h71-reopen-surface`.

## 36. Push
Push to origin without force (worktree).

## 37. SAFE UNKNOWN
- Exact operator mental model of overnight lead may still refer to EXISTING_SPAM forms already ledgered before outage.
- Whether Telegram client UI caches old keyboards on untouched historical cards until next edit — operator should use `/leads` or re-open path.

## 38. Operator acceptance actions
1. Run `/leads`.
2. Locate one genuine spam lead (LIVE_SPAM_LEAD_A or B).
3. Confirm `↩️ Вернуть в обработку` visible.
4. Optionally press only if you truly want that lead restored to pending.
5. Do not expect automatic reopen of genuine spam leads from this phase.

## 39. Phase 3I.1 gate
**BLOCKED** until new soak T+48.

## 40. Stop condition
Stop after Gmail healthy, missed lead state resolved, reopen buttons live on original+archive surfaces, reopen lifecycle proven on fixtures, canonical contains 3H.7+3H.7.1, post-backup complete, soak restarted, Phase 3I.1 blocked.

## Tip hash
- HEAD: `2d204d700c43e20642308d637f43f2a4ae51b8d5`
- short: `2d204d70`
- branch: `agent/iseo-sm-phase3h71-reopen-surface`
