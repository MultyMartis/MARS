# REPORT — ISEO-SALES-MANAGER-BOT PHASE 3H.8.2.2 CURRENT-STATE SELECTOR

**Process-line:** `ISEO-SALES-MANAGER-BOT — PHASE 3H.8.2.2 REMINDER CURRENT-STATE SELECTOR HARDENING`  
**Date:** 2026-08-14

---

## 1. Verdict

`PHASE 3H.8.2.2 COMPLETE — REMINDER CURRENT-STATE SELECTOR HARDENED; REAL 10:00 ACCEPTANCE PENDING`

Also: `COMPLETE — AUTHORITATIVE UNIQUE PENDING COUNT PROVEN; NEXT WINDOW READY`

---

## 2. Prior pending-31 defect

Phase 3H.8.2 reported eligible pending ≈31 from non-deduped CLEAN rows. Phase 3H.8.2.1 proved unique first-row selector count ≈10 with 20 duplicate excess rows. First-row semantics remained unsafe for current-state authority.

---

## 3. Old selector behavior

`CURRENT_SELECTOR_FIRST_ROW_DEPENDENT = YES`  
Filter pending → exclude tests → first `best.set(key,r)` wins. Later rows ignored. Terminal CLEAN rows never entered the map, so historical pending could survive a later spam/processed copy.

---

## 4. Duplicate CLEAN evidence

| Alias | Rows | Statuses |
|---|---|---|
| LEAD_C3EF8E536C35 | 16 | pending |
| LEAD_F4C9D9693444 | 6 | new/pending |

Duplicate source deferred (no cleanup this phase).

---

## 5. Current-state source precedence

`LEADS_CURRENT` → `LEAD_EVENTS_LATEST` → `CLEAN_LATEST_FALLBACK` → `SAFE_UNKNOWN` (fail closed).

---

## 6. New selector contract

`iseo-reminder-current-state-selector-v1.0`  
`pending_count = unique lead_id where resolved_status=pending AND eligible=true`

---

## 7. LEADS current-state resolution

Product SoT: `lead_clean_v2` manager lifecycle fields. Latest authority timestamp across **all** statuses per lead.

---

## 8. LEAD_EVENTS fallback

Implemented in library/harness. Production Build Claims does not add an EVENTS Sheets read (quota).

---

## 9. CLEAN fallback

`CLEAN_LATEST_FALLBACK` when manager authority fields absent; ambiguous ordering → SAFE_UNKNOWN.

---

## 10. SAFE_UNKNOWN behavior

`eligible=false`. Hard resolution failure → `ERROR_CURRENT_STATE_RESOLUTION`.

---

## 11. Test/archive exclusion

Preserved. Live eligible test leaks=0, archive leaks=0.

---

## 12. Terminal-state precedence

pending→spam and pending→processed harness PASS; terminal wins over historical pending.

---

## 13. Reopen semantics

Harness + live `REMINDER_ACCEPTANCE_LEAD_2`: pending restored, counted once, not mutated this phase.

---

## 14. Acceptance lead

Same ID; pending; not test; eligible; **exactly once** in matrix.

---

## 15–17. Counts (live 13:12 MSK)

| raw CLEAN pending rows | 30 |
| unique CLEAN lead IDs | 10 |
| authoritative current pending | **10** |
| terminal leads removed (global) | 6 |
| duplicate excess ignored | 20 |
| test leaks | 0 |
| archive leaks | 0 |
| SAFE_UNKNOWN (global) | 2 |
| acceptance lead occurrences | 1 |

---

## 18. Current candidate matrix

See `evidence/phase3h822/CURRENT-CANDIDATE-MATRIX-v1.md` (10 rows; all authoritative pending).

---

## 19. Duplicate-row effect

After repair: no inflation; cannot keep stale pending over later terminal. Source cleanup deferred.

---

## 20. Sheets read complexity

Production reads unchanged (4 logical). **per-lead Sheets calls = 0**.

---

## 21. 429 retry regression

phase3h82 harness 23/23 PASS; cases 19–20 PASS.

---

## 22. Exactly-once regression

4 recipients / claim keys unchanged; cases 22–23 PASS.

---

## 23. Reminder UX count

Message uses authoritative unique pending (N=10 today). One reminder per recipient, not per lead.

---

## 24. Live read-only pre-window proof

PASS — no claims, no Telegram, authoritative pending=10, acceptance once.

---

## 25. Next 10:00 readiness

enabled=true; 10:00 Europe/Moscow; recipients CONFIG=4; last_window empty; selector+429 active; no manual send.

---

## 26. Deferred CLEAN-duplication follow-up

`KNOWN FOLLOW-UP — CLEAN DUPLICATE ROW PRODUCTION SOURCE FORENSIC`

---

## 27. System invariants

Ops unchanged; AI OFF; soak interrupted; Phase 3I.1 blocked; no new workflows.

---

## 28. Backup

Private pre/post under STORAGE incoming; sanitized manifests in `evidence/phase3h822/`.

---

## 29. Git

Worktree `git-sync-iseo-sm-phase3h822-*` from `origin/mars/canonical-post-recovery`; scope `projects/iseo-sales-manager-bot/**`.

---

## 30. Soak state

Not restarted.

---

## 31. Phase 3I.1 gate

Blocked.

---

## 32. Stop condition

First-row dependence removed; unique current-state objects; terminal precedence; reopen restores pending; acceptance once; authoritative count proven; no per-lead Sheets calls; 429 intact; next window ready; no manual reminder.

### Required counters

| Counter | Value |
|---|---|
| raw CLEAN pending rows | 30 |
| unique CLEAN lead IDs | 10 |
| authoritative current pending | 10 |
| terminal leads removed | 6 |
| duplicate excess rows ignored | 20 |
| test leaks | 0 |
| archive leaks | 0 |
| SAFE_UNKNOWN | 2 |
| acceptance lead occurrences | 1 |
| Sheets reads per evaluation | 4 logical |
| per-lead Sheets calls | 0 |
| reminder recipients | 4 |
| next-date claims | 0 |
| mutations | 0 |
| reminders sent | 0 |
| AI state | OFF |
| OpenRouter calls | 0 |
| workflows created | 0 |
| soak restarted | 0 |
| Phase 3I.1 started | 0 |

**Not claimed:** `REMINDER LIVE PASS`
