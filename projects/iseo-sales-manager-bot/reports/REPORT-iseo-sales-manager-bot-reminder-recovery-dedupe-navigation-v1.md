# REPORT — ISEO Sales Manager Bot — Reminder Recovery Dedupe + Group Navigation

**Date:** 2026-08-21  
**Contour:** Admin.dev \`wLrLp4WQHm1VJmxz\`  
**Worktree:** \`X:\\AI MARS STORAGE\\git-sync-iseo-sm-reminder-recovery-nav-20260821-142657\\repo\`  
**Branch:** \`agent/iseo-sm-reminder-recovery-nav\`

---

## 1. Verdict

**TECHNICAL COMPLETE — SAME-WINDOW DUPLICATE FIXED; NEXT NATURAL WINDOW ACCEPTANCE PENDING**

Alternate allowed phrasing also applies for code/deploy scope:  
**REMINDER RECOVERY DEDUPE PASS — PRIMARY DELIVERY PRESERVED; GROUP NAVIGATION DEPLOYED**

Soak: **not started**.

---

## 2. Natural primary delivery

| Item | Value |
|------|-------|
| Exec | \`36699\` |
| UTC | \`2026-08-21T07:00:11Z\` → \`07:01:23Z\` (~10:01 MSK) |
| Window | \`pending-reminder:2026-08-21:10:00:Europe/Moscow\` |
| Pending | 13 |
| Recipients | 1 (ADMIN_A) |
| Telegram | success \`message_id=1060\` |
| Ledger | delivered \`msg:1060\` |
| \`last_window\` | **not stamped** (success-path gap) |

**PRIMARY DELIVERY = SUCCESS**

---

## 3. Natural recovery duplicate

| Item | Value |
|------|-------|
| Exec | \`36708\` |
| UTC | \`2026-08-21T07:15:11Z\` (~10:15 MSK) |
| Same window key | yes |
| Telegram | success \`message_id=1061\` (duplicate digest) |

---

## 4. Exact duplicate root cause

1. Success path after \`Upsert REMINDER_DELIVERIES Delivered\` did **not** call \`Reminder Mark Window Complete\` → \`last_window\` empty → recovery gate proceeded.  
2. Recovery ledger read returned an empty item → delivered skip missed → ADMIN_A re-claimed/sent.

First divergence: **missing post-success window completion**, then **failed recipient-level delivery visibility** at recovery eval.

---

## 5. Business-window identity

Reused: \`pending-reminder:<date>:<configured-time>:<tz>\`  
Primary and recovery shared \`…:2026-08-21:10:00:Europe/Moscow\`. No second identity model.

---

## 6. Recipient-level idempotency

Skip Telegram only when ledger status is \`delivered\`/\`sent\` for \`window|recipient_ref\`.  
\`claimed\` alone remains recoverable. Harness proves partial multi-recipient behavior without hardcoding recipient count.

---

## 7. Claims

Primary: 1 claim created then delivered.  
Recovery: attempted another claim/send for the same key; delivered upsert 429.

---

## 8. Delivery ledger

Post-incident sheet retains primary delivered row (\`msg:1060\`). Recovery did not overwrite.

---

## 9. Window completion

Repair: \`Reminder Post Deliver Window\` marks complete only when delivered recipients ≥ intended count, then stamps \`last_window\` via existing Mark Complete path.

---

## 10. Repair

Deployed Admin.dev **102 → 104** nodes (PUT 200, active):

- Collapse ACCESS → ledger read  
- Post Deliver → Mark Window Complete  
- Build Claims delivery-only skip + digest v1.1 filter buttons  
- \`sm:g:\` normalize + group_open handler  

---

## 11. Partial-recipient recovery

Harness case: A delivered / B claimed / C absent → recovery sends B+C only.

---

## 12. Main digest UX

Body structure preserved (title, categories, counters). Lead buttons removed from main message.

---

## 13. Group buttons

Dynamic category buttons (count>0) + older-than-day + all.

---

## 14. Category navigation

\`sm:g:c:<hash>\` → current pending in category, oldest first.

---

## 15. Older-than-24h filter

\`sm:g:o24\` → pending with \`age_days >= 1\`, oldest first. View/filter only.

---

## 16. All-pending filter

\`sm:g:all\` (+ pagination).

---

## 17. Pagination

Page size 12; \`⬅️\` / \`➡️ Показать ещё\` via \`sm:g:<filter>:pN\`.

---

## 18. Exact lead navigation

\`sm:q:<opaque lead_id token>\` → current CLEAN resolve (unchanged contract).

---

## 19. Compact lead view

Existing queue_open compact card + actions (processed/spam/raw/full_card).

---

## 20. Stale/current-state behavior

Group/lead clicks rebuild from current CLEAN; snapshot counts on old messages may lag.

---

## 21. Card status sync regression

Empty full_card keyboard guard preserved. New callbacks non-empty. empty_callback_buttons = 0.

---

## 22. Current ACCESS

Probe: active **1** admin (ADMIN_A); revoked **3**. Nobody restored.

---

## 23. Test routing

Harness offline only for idempotency. No moderator/customer Telegram tests. AI OFF.

---

## 24. Backup

PRE sha16 \`9C6CE5F34757F201\` · POST sha16 \`ACD4BD539427F169\` under STORAGE incoming private backups (manifests in evidence).

---

## 25. Git

- Card-sync \`9a69ef08\` cherry-picked as \`5b8ca157\` onto clean worktree from \`origin/mars/canonical-post-recovery\`.  
- This wave: selective commits under \`projects/iseo-sales-manager-bot/**\` then push (no force).

---

## 26. Reminder live acceptance state

**PRIMARY DELIVERY LIVE PASS — SAME-WINDOW DUPLICATE RECOVERY DEFECT FOUND** (today).  
After repair: technical fix deployed; **next natural window** required for \`REMINDER LIVE PASS\`.

---

## 27. Soak state

**NOT STARTED** (duplicate occurred; final soak blocked until next natural reminder proves zero duplicate + group nav).

---

## 28. Remaining stabilization tasks

- Next natural Mon–Fri 10:00 MSK acceptance (ADMIN_A-only if ACCESS unchanged)  
- Deferred: test-lead cleanup; CLEAN duplicate-row forensic  
- Do not begin 48h soak from today’s window  

---

## Counters

| Counter | Value |
|---------|------:|
| natural primary reminder sends | 1 |
| natural recovery reminder sends | 1 |
| duplicate production digests observed | 1 |
| business windows inspected | 1 (\`2026-08-21\`) |
| claims primary | 1 |
| claims recovery | 1 (attempt) |
| Telegram successes primary | 1 |
| Telegram successes recovery | 1 |
| recipients skipped as already delivered (harness) | ≥1 scenarios |
| duplicate sends after repair harness | **0** |
| group filters rendered (harness) | ≥3 |
| group navigation tests | harness + deploy verify |
| lead action tests | reuse existing queue_open path (0 live customer mutations) |
| wrong lead resolutions | **0** |
| empty callback buttons generated | **0** |
| moderator test messages | **0** |
| customer test messages | **0** |
| real customer state mutations | **0** |
| workflows modified | **1** (Admin.dev) |
| AI calls | **0** |

---

## Execution safety

- cwd / worktree: STORAGE clean worktree under \`X:\\AI MARS STORAGE\\...\`  
- scope lock honored: \`projects/iseo-sales-manager-bot/**\` + authorized n8n/Sheets probes  
- destructive ops: none on git dirty tree; tmp probe workflows deleted  
- protected zone touch: none  
