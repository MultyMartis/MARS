# REPORT — ISEO SALES MANAGER BOT PHASE 3H.7.3.1 ACCEPTANCE CARD CANONICALIZATION AND AUTHORITATIVE INSTANCE CORRECTION

## 1. Verdict

`PHASE 3H.7.3.1 COMPLETE — ALL THREE ACCEPTANCE LEADS CANONICAL; FOUR-CARD SYNC PASS; FINAL 48-HOUR SOAK RESTARTED`

## 2. Operator live evidence

- One acceptance lead showed full canonical production card.
- One acceptance lead completed Spam → Reopen → Spam with correct Russian acknowledgements.
- One acceptance lead still showed reduced/status-only card (pending fields + returned-to-processing metadata).

## 3. Why 3H.7.3 was not accepted

Phase 3H.7.3 repaired resurface parity and registry selection, but **callback status sync still used reduced `buildFinalCard`**. Any live Spam/Processed/Reopen after repair degraded authoritative cards. Soak start from 3H.7.3 is **INTERRUPTED — MIXED AUTHORITATIVE CARD RENDERING DURING LIVE ACCEPTANCE**.

## 4. Starting card states

| Alias | Status at repair start | Auth instances |
|---|---|---|
| REAL_REOPEN_A | pending (telegram reopen) | 4 parity rows |
| REAL_REOPEN_B | pending | 4 parity rows |
| REAL_REOPEN_C | spam (telegram spam) | 4 parity rows |

## 5. Failed acceptance lead

**REAL_REOPEN_A** — reduced pending card after reopen via reduced status-sync renderer.  
**REAL_REOPEN_C** — spam lifecycle acks correct but body degraded by the same renderer.  
**REAL_REOPEN_B** — remained full canonical until used for controlled lifecycle proof.

## 6. Canonical object forensic

Offline `renderCanonicalLeadCard` against live `lead_clean_v2` rows: canonical object complete (heading/interest/quality/reply fixture OK). Defect was not missing Sheets fields.

## 7. Displayed-card forensic

Displayed degraded cards matched `Handle Callback Action` → `buildFinalCard()` shape: status + client/site/service/request + actor/time — missing production heading, interest/quality blocks, approved reply, personalization.

## 8. Authoritative-instance root cause

1. **Primary:** status-sync edit_text from reduced `buildFinalCard`.  
2. **Secondary:** recipient_ref case variance and multi-generation deliveries needed stricter v1.1 preference (`acceptance_canonical` > parity > resurface > initial).

## 9. Authoritative instance v1.1

Deployed contract `iseo-authoritative-card-instance-v1.1` in Expand Card Sync Copies + runtime `selectAuthoritativeCardInstances`.

## 10. Canonical rerender repair

Handle Callback Action now builds full canonical status card body (interest/quality/reply + additive attribution). No status-only renderer for authoritative current cards.

## 11. Edit-in-place vs replacement

Prefer edit-in-place of current message refs; on failure send exactly one corrected card per recipient. Delivery keys `acceptance_canonical:*`. No new LEADS rows.

## 12. REAL_REOPEN_A parity

Pending · 4/4 canonical · pending keyboard · PASS

## 13. REAL_REOPEN_B parity

Pending · 4/4 canonical · pending keyboard · PASS · Spam→Reopen lifecycle proven

## 14. REAL_REOPEN_C parity

Spam · 4/4 canonical + terminal metadata · Reopen keyboard · PASS

## 15. 12-card parity matrix

**12/12 PASS** — see `evidence/phase3h731/THREE-LEAD-12-CARD-PARITY-v1.md` and `LIVE-THREE-LEAD-MATRIX-v1.md`.

## 16. Contact rendering

No `#ERROR!` on authoritative current cards. Formula-error sanitizer retained.

## 17. Approved template preservation

Template routing retained (T1/T2 observed). Reply block present on all 12.

## 18. Personalization

Андрей / Оля / Михаил / Никита present on respective recipient cards.

## 19. Pending keyboard

`✅ Обработано` + `🚫 Спам` on pending authoritative cards.

## 20. Terminal keyboard

`↩️ Вернуть в обработку` on spam authoritative cards (REAL_REOPEN_C).

## 21. Spam lifecycle

Controlled live Spam on REAL_REOPEN_B: 4/4 full canonical spam cards; ack `Лид отмечен как спам.`

## 22. Reopen lifecycle

Same lead → pending: 4/4 full canonical pending cards; ack `Лид возвращён в обработку.` Same lead id; no new intake fanout.

## 23. Full-body transition preservation

Harness + live lifecycle: core body survives Spam/Processed/Reopen. Status metadata additive only.

## 24. Four-card synchronization

Current sync set 4/4 per lead after acceptance canonicalization. Aggregate semantic ack independent of historical noise.

## 25. Superseded card behavior

Historical initial/resurface/parity instances superseded for current accounting; not promoted by stale callbacks.

## 26. Stale callback behavior

Lead-token resolution unchanged; superseded message cannot become authoritative again.

## 27. Archive regression

Archive compactness contract unchanged; `/leads` path not redesigned.

## 28. Normal intake regression

Operational.dev unchanged (45 nodes, same ID). Gmail/parser/fanout/reminders untouched.

## 29. Counters/history

LEADS rows delta **0**. Terminal/reopen history preserved; lifecycle appended exactly two events on proof lead.

## 30. System health

Operational active · Admin active · V2 inactive · recipients=4 · reminders ON 10:00 Europe/Moscow · reporting manual · AI OFF · OpenRouter=0 · customer auto-send=0 · workflows created=0 · invalid_grant active=0.

## 31. Harness

**25/25 PASS** (`evidence/phase3h731/HARNESS-RESULTS-v1.md`).

## 32. Post-change backup

Private post-change backups under STORAGE worktree `runtime/backups/post-change/`. Manifest committed.

## 33. Canonical Git

Base tip before phase: `ecfee9f7`. Branch `mars/iseo-sm-phase3h731-acceptance-card`. Scope `projects/iseo-sales-manager-bot/**`.

## 34. New soak T+0

`2026-08-10T10:29:35.708Z` / `10.08.2026 13:29 МСК` — **not** reusing 3H.7.3 T+0.

## 35. New T+48

Earliest: `2026-08-12T10:29:35.708Z` / `12.08.2026 13:29 МСК`.

## 36. Operator acceptance packet

See `evidence/phase3h731/OPERATOR-ACCEPTANCE-PACKET-v1.md`. One-click: reopen the spam lead’s current card; confirm four pending canonical cards.

## 37. Final workflow state

Admin `wLrLp4WQHm1VJmxz` active 87 · Operational `xSnXPy8cEHoZw6xG` active 45 · V2 inactive.

## 38. Final AI state

AI **OFF**.

## 39. Safety counters

| Counter | Value |
|---|---|
| acceptance leads inspected | 3 |
| reduced authoritative cards before repair | 2 leads affected (A pending reduced, C spam reduced) |
| reduced authoritative cards after repair | 0 |
| authoritative cards expected | 12 |
| authoritative cards canonical | 12 |
| contact rendering failures | 0 |
| template parity failures | 0 |
| personalization failures | 0 |
| full-body degradation events (post-fix) | 0 |
| current sync failures | 0 |
| superseded card instances | historical retained / excluded from current sync |
| duplicate business lead rows | 0 |
| status transitions tested | spam + reopen (live) + harness processed paths |
| wrong callback acknowledgements | 0 |
| active recipients | 4 |
| reminder recipients | 4 |
| Gmail health | healthy contour (Operational sole intake) |
| AI state | OFF |
| OpenRouter calls | 0 |
| customer auto-send | 0 |
| workflows created | 0 |
| new soak start | yes |
| earliest T+48 | 2026-08-12T10:29:35.708Z |
| Phase 3I.1 started | no |

## 40. Files changed

- `implementation/runtime-libs/canonical-lead-card-renderer-v1.mjs`
- `implementation/runtime-libs/formatter-lib.mjs`
- `implementation/ACCEPTANCE-CARD-CANONICALIZATION-v1.md`
- `implementation/AUTHORITATIVE-CARD-SELECTION-CORRECTION-v1.md`
- docs/guides/product/architecture updates listed in Git
- `evidence/phase3h731/**`
- `reports/REPORT-iseo-sales-manager-bot-phase3h731-acceptance-card-canonicalization-v1.md`

## 41. Commits

See Git log on branch `mars/iseo-sm-phase3h731-acceptance-card` (fix/test/docs commits).

## 42. Push

Pushed to `origin/mars/canonical-post-recovery` without force (after merge/fast-forward per phase charter).

## 43. SAFE UNKNOWN

- Exact Telegram visual pixel audit of all 12 live messages not re-fetched via Bot API getChat after edits; repair/lifecycle edit/send results + renderer parity used as proof.
- Whether operator will perform an additional manual click beyond controlled lifecycle — pending human.

## 44. Phase 3I.1 gate

**Blocked.** New soak must reach T+48 before any AI-on consideration.

## 45. Stop condition

Stop after: failed lead identified; root cause proven; 12/12 canonical; full body survives transitions; buttons match status; sync 4/4; superseded excluded; archive/intake unchanged; post backup complete; canonical pushed; fresh soak restarted; Phase 3I.1 blocked; AI OFF.
