# REPORT — ISEO Sales Manager Bot — Natural Reminder Action Card Fix v1

Date: 2026-08-31  
Process-line: ISEO-SALES-MANAGER-BOT — NATURAL REMINDER EXACT LEAD ACTIONABLE CARD FORENSIC/FIX  
Workflow: Admin.dev `wLrLp4WQHm1VJmxz` (Operational.dev `xSnXPy8cEHoZw6xG` untouched)

## 1. Verdict

**TECHNICAL FIX PASS — NEXT NATURAL REMINDER CONFIRMATION PENDING**

Root causes proven on today's natural production traffic (exec 51238/51239). Admin.dev patched: static action keyboard on in-place card edit + suppress stray visible `Карточка` after successful card sync. Live deploy checks PASS. Await next natural reminder for operator-visible confirmation.

## 2. Today's natural live defect

Operator path: reminder → group → exact lead.

- Card text: correct
- Actions: missing (`✅ Обработано`, `🚫 Спам`, `📄 Исходная заявка`)
- Extra message: standalone `Карточка`

Not soak traffic — direct production evidence overrides prior harness PASS prose.

## 3. Natural execution trace

| Exec | Callback | Outcome | Edit | Stray reply |
|---|---|---|---|---|
| 51238 | `sm:q:c422c6ec15b5` | `queue_opened` | pending edit ok | `Карточка` |
| 51239 | `sm:q:3183ec40e360` | `queue_opened` | pending edit ok | `Карточка` |

Chain: Handle → Edit Lead Card Message Pending → Aggregate → Prepare → Capture → Safe Telegram Reply.

## 4. Realtime vs reminder difference

Group list (`group_opened`, `skip_card_edits: true`) preserves digest via existing contract — no stray reply.

Exact lead (`queue_opened`, in-place edit) used whole-object edit keyboard (markup dropped) and propagated ack title into visible reply. See `REALTIME-VS-REMINDER-CARD-DIFF-v1.md`.

## 5. Exact first divergence

1. **Missing buttons:** `Edit Lead Card Message Pending` — `ACTION_KEYBOARD_NOT_ATTACHED` (whole-object inlineKeyboard).
2. **Stray `Карточка`:** `Aggregate Card Sync Result` — `SEPARATE_TITLE_MESSAGE_BRANCH`.

## 6. Missing action-button root cause

Handle populated correct `sm:p/s/i` callbacks and card text. Telegram edit returned ok without `reply_markup` due to n8n whole-object keyboard expression — same class as reminder-inline-nav ROOT-CAUSE.

## 7. Stray `Карточка` root cause

`answer_text: 'Карточка'` copied to `reply_text` after successful in-place edit; downstream Safe Telegram Reply sent it because `IF Telegram Has Buttons` was false. Suppression contract added for successful card-edit paths.

## 8. Repair

**Admin.dev only** (deploy `2026-08-31T07:37:21.914Z`):

1. `Edit Lead Card Message Pending` — static fixedCollection keyboard with field expressions
2. `Aggregate Card Sync Result` — `CARD_EDIT_SUPPRESS_REPLY` / `suppress_visible_reply`
3. `Prepare Callback Answer` — honor suppress
4. `Capture Admin Reply` — skip empty suppressed items

Patches: `implementation/patches/*natural-reminder-action-card-fix.js`

## 9. Post-fix pending card contract

Pending lead via `sm:q:*`: in-place edit with ✅ / 🚫 / 📄 callbacks bound to Handle-resolved stable tokens. Static live verification PASS; no synthetic Telegram sent.

## 10. Terminal-card behavior

Unchanged — non-pending authoritative status still uses terminal edit modes without pending action trio.

## 11. Natural branch proof

Patched nodes sit on the production `sm:q:*` connection chain (no parallel test route). See `NATURAL-BRANCH-CONFIG-PROOF-v1.md` and `post-deploy-verify.json`.

## 12. Status callback contract

Buttons map to existing `sm:p/s/i` handlers; status logic not rebuilt. Static proof from pre-fix exec callback fields.

## 13. Olya/ACCESS invariants

MOD_B unchanged. No ACCESS mutations. No Olya test traffic. No real Olya lead mutations by this task.

## 14. Test traffic

| Counter | Value |
|---|---|
| ADMIN_A synthetic messages | 0 |
| Olya test messages | 0 |
| Other moderator test messages | 0 |
| Customer test messages | 0 |
| AI calls | 0 |

## 15. Workflow backup

- PRE: `Admin.dev.PRE-2026-08-31T07-26-02-721Z.json` (+ deploy-wave PRE `07-37-21-914Z`)
- POST: `Admin.dev.POST-2026-08-31T07-37-21-914Z.json`
- Private STORAGE only — not in Git

## 16. Git

Clean worktree commits under `projects/iseo-sales-manager-bot/**`; push to `origin/mars/canonical-post-recovery`.

## 17. Soak status

No soak running. **Do not start** in this task.

## 18. Next gate

**READY FOR NEW 48H NATURAL-TRAFFIC-ONLY SOAK** — stop; await operator approval after next natural reminder confirms actions + zero stray `Карточка`.

---

## Counters

| Metric | Value |
|---|---|
| natural reminder defects inspected | 1 (class, 2 anchor execs) |
| pending exact leads inspected | 2 (51238, 51239) |
| pending exact leads with actions before | 0 |
| pending exact leads with actions after | 2 (static deploy proof; live click pending) |
| standalone `Карточка` before | 2 |
| standalone `Карточка` after | 0 (contract deployed; live pending) |
| empty callbacks | 0 |
| wrong lead resolutions | 0 |
| ACCESS mutations | 0 |
| Olya real leads mutated | 0 |
| ADMIN_A synthetic messages | 0 |
| Olya test messages | 0 |
| other moderator test messages | 0 |
| customer test messages | 0 |
| Operational.dev modifications | 0 |
| Admin.dev modifications | 4 nodes |
| AI calls | 0 |

## Changed files (Git)

- `implementation/patches/AggregateCardSyncResult.natural-reminder-action-card-fix.js`
- `implementation/patches/PrepareCallbackAnswer.natural-reminder-action-card-fix.js`
- `implementation/patches/CaptureAdminReply.natural-reminder-action-card-fix.js`
- `evidence/current-stabilization/natural-reminder-action-card-fix/*` (14 files)
- `reports/REPORT-iseo-sales-manager-bot-natural-reminder-action-card-fix-v1.md`
