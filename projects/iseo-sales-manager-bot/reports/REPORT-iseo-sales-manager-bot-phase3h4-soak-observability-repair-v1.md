# REPORT — ISEO SALES MANAGER BOT PHASE 3H.4 SOAK OBSERVABILITY REPAIR

## 1. Verdict

`PHASE 3H.4 COMPLETE — SOAK OBSERVABILITY REPAIRED; 48-HOUR SOAK RESTARTED`

Soak restart T+0: **2026-08-06 19:15 Europe/Moscow**. Earliest valid PASS: **2026-08-08 19:15 Europe/Moscow**. Do not use soak-passed verdict yet.

## 2. Operator-approved scope

Phase 3H.4 observability repair during active pre-AI soak; **not** Phase 3I.1. AI remains OFF. Reminders remain ON.

## 3. Worktree / branch

Base: `origin/mars/canonical-post-recovery` @ `380cebd7`. Branch: `agent/iseo-sm-phase3h4-soak-observability-repair`.

## 4. Starting contour

Ops `xSnXPy8cEHoZw6xG` active 45 · Admin `wLrLp4WQHm1VJmxz` active 85 · v2 inactive · AI OFF · reminders ON 10:00 Europe/Moscow · active recipients=3 · Nikita revoked.

## 5. Pre-repair backup

Storage: `git-sync-iseo-sm-phase3h4-20260806-185304/runtime/backups/pre-repair/`. sha256 Operational.dev `73DCB2DE6B01A4AADAD761CA735131D7C0F569F51049D806568E851C16D6E56E` · Admin.dev `24318EA9B0EE4B601C4C304204BBD816527793FAE92C7970DD174CB228C1AFB7`.

## 6. Reminder status forensic

Admin executions **24194**, **24196**: Telegram Trigger received `/reminder_status`; auth admin PASS; Reminder Commands SyntaxError; Capture/Send never ran.

## 7. Reminder status root cause

Admin long-form `statusText` contained literal `,\n` between array elements — invalid JS. Moderator short-form syntactically fine.

## 8. Reminder status repair

Reminder Commands Code node patched on Admin.dev. Offline `node --check` PASS; `brokenLiteral=false`.

## 9. Reminder status live acceptance

ADMIN_A and MOD_A `/reminder_status` visible reply PASS.

## 10. Gmail poll forensic

Classification `POLLING_ACTIVE_BUT_HEARTBEAT_NOT_WRITTEN_ON_EMPTY_RUNS`. Schedule Trigger minutesInterval=2 active; empty runs returned `[]` from Update Last Success; `last_poll_success_at` frozen 2026-08-05T10:34:00.459Z (= 05.08.2026 13:34 МСК).

## 11. Schedule trigger acceptance

~2 min cadence confirmed active post-repair; empty route completes to Runtime State write.

## 12. Gmail poll heartbeat contract

Version `iseo-gmail-poll-heartbeat-v1.0`; compact JSON + mirror keys on every successful poll including empty runs.

## 13. Three consecutive polls proof

Executions **24222**, **24223**, **24228** — empty-run heartbeat CONFIG writes PASS.

## 14. Status data source matrix

Poll line → scheduled heartbeat keys. Production lead line → `last_production_processed_*`. Not `/health` probe. Not synthetic `msg_synth_*` stamps.

## 15. Last processed lead forensic

Wrong 22:23 МСК from `msg_synth_3g11d_t1_*` at `last_lead_success_at=2026-08-05T19:23:37.997Z`. Authoritative production: `lead_19fd2052066e18b7` lifecycle_changed_at 2026-08-05T14:22:55.186Z (= 05.08.2026 17:22 МСК).

## 16. Status live acceptance

ADMIN_A `/status` poll + production lead lines PASS post-repair and CONFIG backfill.

## 17. Health semantic separation

`/health` Gmail probe is on-demand; must not substitute for scheduled poll heartbeat in `/status`.

## 18. Reminder config invariants

enabled=true · 10:00 Europe/Moscow · min=1 · source LEADS · tests excluded · `pending_reminder_active_recipients_count=3` backfilled.

## 19. Production invariants

AI OFF · no customer auto-send · workflows_created=0 · stats epoch unchanged received=1 pending=0 processed=1 spam=0.

## 20. Harness results

Reminder Commands / Status / Health syntax validated via `node --check`; live Reminder SyntaxError eliminated.

## 21. Operational patch

Update Last Success / Runtime State: heartbeat on empty polls; `last_production_processed_*` on non-test success only.

## 22. Admin patch

Reminder Commands, Status, Health Code nodes patched in-place; temporary webhook nodes removed; final Admin nodes=85.

## 23. CONFIG backfill

`pending_reminder_active_recipients_count=3` · `last_production_processed_at=2026-08-05T14:22:55.186Z` · `last_production_processed_lead_id=lead_19fd2052066e18b7`.

## 24. Post-repair backup

Storage: `git-sync-iseo-sm-phase3h4-20260806-185304/runtime/backups/post-repair/` (raw private; sha256 in private manifest).

## 25. Soak attempt 1 interruption

Started 06.08.2026 14:20 МСК — **INVALIDATED** by observability repair (`INTERRUPTED BY OBSERVABILITY REPAIR`). Polling was running; not a production delivery failure unless poll itself broken.

## 26. Soak restart receipt

New T+0 **2026-08-06 19:15 Europe/Moscow** · earliest PASS **2026-08-08 19:15 Europe/Moscow**.

## 27. Soak checkpoint T+0 v2

See `evidence/phase3h4/SOAK-CHECKPOINT-T0-v2.md`. Supersedes attempt 1 T0 for clock purposes.

## 28. Final workflow state

Ops active 45 · Admin active 85 · v2 inactive · workflows_created=0.

## 29. Final profiles

1 ADMIN_A enabled · 2 MOD_B enabled · 3 MOD_A enabled · 4 Nikita revoked.

## 30. Final access state

active recipients=3 · revoked=1.

## 31. Final reminder state

ON · 10:00 Europe/Moscow · source LEADS · zero-pending armed.

## 32. Final AI state

OFF · OpenRouter calls=0.

## 33. Final reporting state

manual / только вручную.

## 34. Production statistics

received=1 · pending=0 · processed=1 · spam=0 (unless genuine arrival during soak).

## 35. Phase 3H.4 acceptance receipt

See `evidence/phase3h4/PHASE3H4-ACCEPTANCE-RECEIPT-v1.md`.

## 36. Architecture docs created

`GMAIL-POLL-HEARTBEAT-CONTRACT-v1.md` · `OPERATIONAL-STATUS-TRUTH-CONTRACT-v1.md`.

## 37. Implementation docs created

`REMINDER-STATUS-COMMAND-REPAIR-v1.md` · `SCHEDULED-POLL-OBSERVABILITY-v1.md` · `STATUS-DATA-SOURCE-REPAIR-v1.md`.

## 38. Evidence pack

22 files under `evidence/phase3h4/` (forensic, acceptance, soak restart, invariants, harness).

## 39. Safety counters

| Counter | Value |
|---|---:|
| workflows created | 0 |
| production leads lost/duplicated | 0/0 |
| AI | OFF |
| reminder enabled | true |
| active recipients | 3 |
| pre-repair silent `/reminder_status` (admin) | reproduced then fixed |
| empty-poll heartbeat writes (sample) | 3 PASS |
| Phase 3I.1 started | false |
| soak attempt 1 | INVALIDATED |
| soak attempt 2 T+0 set | true |

## 40. Files created

All `evidence/phase3h4/*.md` (22) · 5 architecture/implementation docs · this report.

## 41. Files updated

README.md · OPERATIONAL-INDEX.md · product/CURRENT-PRODUCTION-BASELINE-v1.md · PRODUCTION-BASELINE-PRE-AI-SOAK-v1.md · KNOWN-LIMITATIONS-v1.md · PRODUCT-ROADMAP-v1.md · architecture/DAILY-PENDING-REMINDER-CONTRACT-v1.md · TELEGRAM-TEXT-CONTRACT-v2.md · CLEAN-PRODUCTION-LEDGER-v1.md · implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md · OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md · REMINDER-EXACTLY-ONCE-v1.md · USER-VISIBLE-TEXT-REGISTRY-v1.md · guides/TELEGRAM-COMMAND-REFERENCE-v1.md · OPERATOR-RUNBOOK-v1.md · PRE-AI-SOAK-RUNBOOK-v1.md.

## 42. Security validation

No Telegram numeric IDs, usernames, emails, workbook IDs, raw exports, or screenshots in committed evidence. Pre/post repair raw exports remain Storage private. sha256 cited only.

## 43. Commits

Not performed in this documentation wave — operator/parent agent charter.

## 44. Push

Not performed — documentation-only wave in agent worktree.

## 45. Risks

- Soak PASS unavailable until 2026-08-08 19:15 Europe/Moscow minimum
- First multi-send reminder day with pending≥1 may still occur only during soak window
- Legacy synthetic rows remain in historical tabs (excluded from production display)

## 46. SAFE UNKNOWN

Exact post-repair workflow export sha256 not committed (private manifest only). Additional stable-cadence poll observation may still be running beyond the three cited executions.

## 47. Remaining operator actions

1. Run soak checkpoints per `guides/PRE-AI-SOAK-RUNBOOK-v1.md` from new T+0
2. Confirm `/status` `/reminder_status` `/health` visually as ADMIN_A
3. Do not start Phase 3I.1 until soak PASS + explicit approval

## 48. Phase 3I.1 gate

Blocked until soak PASS + explicit operator approval. AI stays OFF.

## 49. Stop condition

Phase 3H.4 observability repairs deployed · evidence + architecture docs committed · soak restarted · 3I.1 not started — **met**.
