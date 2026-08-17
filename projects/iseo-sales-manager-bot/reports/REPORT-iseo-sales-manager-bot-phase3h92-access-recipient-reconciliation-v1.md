# REPORT — ISEO-SALES-MANAGER-BOT Phase 3H.9.2 ACCESS RECIPIENT-SET RECONCILIATION

**Process-line:** ISEO-SALES-MANAGER-BOT — PHASE 3H.9.2 ACCESS RECIPIENT-SET RECONCILIATION AND FOUR-RECIPIENT PRE-WINDOW RESTORE  
**Captured:** 2026-08-17 Europe/Moscow  
**Canonical worktree:** `X:\AI MARS STORAGE\git-sync-iseo-sm-phase3h92-20260817-200430\repo` @ `953e6472`  
**Dirty `X:\AI MARS`:** not mutated

## 1. Verdict

`PHASE 3H.9.2 COMPLETE — APPROVED FOUR-RECIPIENT LIVE STATE RESTORED; NEXT 10:00 READY`

MOD_A (profile 3) was the revoked approved recipient. Classification: `UNAUTHORIZED_STATE_DRIFT`. Restored via existing `/moderator_add`. Live ACCESS=4, CONFIG=4, Operational resolver=4, reminder resolver=4. Next natural window: **2026-08-18 10:00 Europe/Moscow**. Soak not restarted. Phase 3I.1 blocked. AI OFF.

## 2. Starting live recipient state

ACCESS live staff = **3**. CONFIG `pending_reminder_active_recipients_count` = **4**. Operational/reminder resolvers = **3**. Drift vs approved four-recipient baseline.

## 3. Approved recipient baseline

ADMIN_A, MOD_A, MOD_B, MOD_C — all active. Proven by Phase 3H.6 four-recipient baseline, `PRODUCTION-BASELINE-PRE-AI-SOAK-FOUR-RECIPIENT-v1.md`, and ACCESS snapshot exec `32813` (2026-08-16 19:09:53 Europe/Moscow) immediately before the drift. CONFIG cache is not authority.

## 4. Revoked profile

**MOD_A** · profile_no **3** · hash12 `518CC34C4C0F` · role moderator.

Pre-restore: active=no · cards=no · reminder=no · personalized replies wiped · `revoked_at` 2026-08-16 19:10:18 Europe/Moscow.

Not MOD_C. MOD_C was revoked then restored the same evening.

## 5. Revocation timeline

| When (Europe/Moscow) | Exec | Action | MOD_A |
|---|---|---|---|
| 2026-08-16 19:09:53 | `32813` | `/moderators` | active |
| 2026-08-16 19:10:07 | `32814` | `/moderator_remove` | still active (MOD_C revoked) |
| 2026-08-16 19:10:17 | **`32815`** | **`/moderator_remove`** | **revoked** |
| 2026-08-16 19:10:27 | `32816` | `/moderator_remove` | revoked (MOD_B revoked) |
| 2026-08-16 20:23:54 | `32881` | `/moderator_pending` | listed revoked |
| 2026-08-16 20:24:04 | `32882` | `/moderator_add` | still revoked (MOD_B restored) |
| 2026-08-16 20:24:16 | `32883` | `/moderator_add` | still revoked (MOD_C restored) |
| 2026-08-17 16:17:10 | `33571` | `/moderator_add` | **active** (this phase) |

## 6. Revocation source/action

Actor: ADMIN_A (`3FBE21323E22`). Source: `admin_command`. Command: `/moderator_remove`. ACCESS_EVENTS: `moderator_revoked`, prior=active. Not harness, not migration, not reminder automation.

## 7. Operator authorization search

No later charter reduced the approved set to three. Phase 3H.9 / 3H.9.1 still required four recipients. CONFIG remained 4. This phase’s operator-approved set explicitly includes MOD_A active. Incomplete restore after a 20-second mass-revoke is not an explicit baseline change.

## 8. Authorization classification

`UNAUTHORIZED_STATE_DRIFT`

## 9. Restoration decision

Restore **only** MOD_A. Same existing row, same profile_no 3, same staff identity. Do not create/renumber. Do not mutate MOD_B/MOD_C.

## 10. Access mutation

Existing `/moderator_add` contract (exec `33571`). Temporary Admin webhook `P3H92 Restore WH` used because Telegram Trigger webhook inject returns 403; removed in `finally`. Admin code hashes vs pre-change: **0**. Node count 100. Notify Access Subject did not run (Sheets upsert strips `notify_text`).

## 11. Profile identity preservation

Same hash12 `518CC34C4C0F`. Same profile_no **3** (rehydrated exec `33572` via existing `rehydrateReplyProfile` seed; reply targeted ADMIN_A chat). Profiles created: **0**. Renumbered: **0**.

## 12. Historical fan-out safety

Lead send path not entered. Reminder send not invoked. Historical leads replayed: **0**. Restoration changes eligibility going forward only.

## 13. CONFIG reconciliation

CONFIG already cached 4. After restore, live ACCESS=4 matches cache. **No CONFIG write.** CONFIG did not override ACCESS.

## 14. Operational recipient resolver

Read-only predicate on post-restore ACCESS: **4** unique (ADMIN_A, MOD_A, MOD_B, MOD_C). Duplicates 0. Revoked included 0. Fifth 0. All have Telegram destinations. No lead manufactured. No Telegram send.

## 15. Reminder recipient resolver

Read-only: eligible **4**, same four aliases. `/reminder_status` exec `33574`: «Получателей: 4». Production claims created: **0**. `last_window` not stamped. Send Reminder: false.

## 16. Current pending state

Authoritative pending: **13** (`/pending_count` exec `33575`). SAFE_UNKNOWN: **2** (last 3H.9.1 selector snapshot; selector not re-run this phase). Acceptance-ready genuine pending ≥1: **yes**. Statuses untouched.

## 17. Sheets credential health

CONFIG read OK · ACCESS read OK · CLEAN read OK · active `invalid_grant` = **0**. No OAuth reconnect this phase.

## 18. Next natural 10:00 readiness

**2026-08-18 10:00 Europe/Moscow.** Reminder enabled. Time 10:00. Recipients live=4. CONFIG=4. Pending≥1. Current-state selector active. 429 retry present. Credential healthy. No sent claim for 2026-08-18. `last_window` empty. Same-window 10:15 recovery available. Production reminder **not** invoked.

## 19. Test-message counters

| Counter | Value |
|---|---|
| ADMIN_A test messages | **0** |
| ADMIN_A operational command replies (add / start-to-admin-chat / moderators / reminder_status / pending_count) | 5 — not tests |
| Moderator test messages | **0** |
| Customer test messages | **0** |
| Four-recipient test lead | 0 |
| Four-recipient test reminder | 0 |

## 20. Production invariants

| Counter | Value |
|---|---|
| approved profiles | 4 |
| active profiles before | 3 |
| revoked profiles before | 1 |
| unauthorized drift profiles | 1 |
| profiles restored | 1 |
| profiles created | 0 |
| active profiles after | 4 |
| Operational recipients resolved | 4 |
| reminder recipients resolved | 4 |
| CONFIG recipients | 4 |
| historical leads replayed | 0 |
| production reminder claims created | 0 |
| production reminders sent | 0 |
| ADMIN_A test messages | 0 |
| moderator test messages | 0 |
| customer test messages | 0 |
| current authoritative pending | 13 |
| active invalid_grant errors | 0 |
| workflows created | 0 |
| AI state | OFF |
| soak restarted | 0 |
| Phase 3I.1 started | 0 |

## 21. Post-change backup

Private: `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\phase3h92-local\backups\post-change-2026-08-17T13-18-29-902Z`. Sanitized manifest in `evidence/phase3h92/POST-CHANGE-BACKUP-MANIFEST-v1.md`. No PII in git.

## 22. Git

Worked in clean worktree, not dirty MAIN. Base `origin/mars/canonical-post-recovery` @ `953e6472`. Scope `projects/iseo-sales-manager-bot/**`. No CONFIG write (cache already 4), so no separate CONFIG-cache commit. Isolated harness: `implementation/harness/phase3h92-recipient-resolution-harness.mjs` (16/16). Commits: `716601b9` restore baseline · `8757fec7` resolver proof · docs commit this wave. Push: `HEAD:mars/canonical-post-recovery` without force.

## 23. Soak state

**Interrupted.** Not restarted. Four-recipient acceptance still requires a natural 10:00 run with 4 claims / 4 Telegram attempts / 4 deliveries / 0 duplicates before any T+0.

## 24. Phase 3I.1 gate

**Blocked.** AI OFF.

## 25. Stop condition

Missing approved profile identified (MOD_A). History reconstructed. Authorization classified. Profile restored. ACCESS=4. CONFIG=4. Resolvers=4 unique. No historical replay. No production reminder send. Pending untouched. Credential healthy. Next 10:00 ready. Soak interrupted. 3I.1 blocked.

Leftover (out of scope): MOD_B/MOD_C `reply_profile_number` still null from the Aug 16 upsert wipe. Card/reminder selection uses role+status+destination, not profile number.
