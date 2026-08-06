# REPORT — ISEO SALES MANAGER BOT PHASE 3G.2.3 MODERATOR START READ-AFTER-REHYDRATE REPAIR

## 1. Verdict

`COMPLETE — MODERATOR START PROFILE REPAIRED; OPERATOR ACCEPTANCE PENDING`

Moderator `/start` stale pre-rehydrate read proven (exec 24097) and repaired on Admin.dev Start: reply-name now prefers post-rehydrate `access_upsert` via unified resolver contract. Offline harness **30/30 PASS**. Contour unchanged. Operator Telegram visual still required.

## 2. Operator evidence

- ADMIN_A: `/start`, `/my_reply_profile` (Андрей), `/reply_profiles` 1–4, `/config` verified — contour healthy.
- MOD_A: `/my_reply_profile` correct (Михаил · enabled · active · cards); `/start` showed `Имя в ответах: не задано` while storage/upsert already had Михаил in the same execution class.

## 3. Starting defect

`COMPLETE — PROFILE RESOLVER UNIFIED; MODERATOR START READ-AFTER-REHYDRATE REPAIR PENDING` — Start Reply ignored Auth rehydrate output and rendered blank sheet cells as «не задано».

## 4. Execution-order forensic

Proven order: Trigger → Normalize → CONFIG collapse → **Read ACCESS_CONTROL** → **Check User Authorization** (normalize + rehydrate → `access_upsert`) → Route → **Start** → Prepare/Upsert last_seen → Capture → Telegram Send. Detail: `evidence/phase3g2-3/START-EXECUTION-ORDER-v1.md`.

## 5. Stale object root cause

Start read `$('Read ACCESS_CONTROL')` (pre-rehydrate). Auth already had `access_upsert.reply_sender_name=Михаил`. Upsert writeback fixed the *next* `/start`, not the current reply. Evidence: `MODERATOR-START-STALE-READ-FORENSIC-v1.md` (exec 24097 vs 24098).

## 6. Repair

Admin.dev Start only: prefer `j.access_upsert`; sheet fallback; fail-closed; stamp `iseo-reply-profile-resolver-v1.0`. Deploy deactivate→PUT→activate same ID. Start hash `9436A389742AF744` → `7E0A13DB067254EF`. Nodes **85**. Ops untouched. `READ-AFTER-REHYDRATE-REPAIR-v1.md`.

## 7. Unified resolver usage

Name line uses `reply_sender_name` only through resolver contract / `resolveStartReplySenderName`. No display_name, username, or nickname fallback. No hardcoded Михаил.

## 8. Read-after-rehydrate behavior

Within one `/start` execution, Start consumes post-rehydrate profile before Telegram Send. Does not depend on the next command.

## 9. Moderator start acceptance

Offline 24097-shape → `Имя в ответах: Михаил` **PASS**. Live post-deploy MOD_A visual **PENDING**.

## 10. Moderator self-profile consistency

`/my_reply_profile` already agreed with storage (24100). Contract: Start and self-profile both resolve Михаил from the same authoritative fields.

## 11. Repeated start anti-wipe

Harness #5–#6 PASS. Live 24097→24098 restored sheet without duplicate-row signal. Operator repeat matrix pending.

## 12. Admin regression

Admin `/start` text contract unchanged (no mandatory reply-name). Harness #27 PASS. Profiles 1–4 unchanged.

## 13. Production invariants

LEADS / LEAD_EVENTS / reporting untouched. AI OFF. Reminders OFF. Sole Gmail = Operational.dev. v2 inactive. Workflows created=0. Access changes=0. Leads modified/lost/duplicated=0. `PRODUCTION-INVARIANTS-v1.md`.

## 14. Harness

`phase3g23-harness.mjs` **30/30 PASS** — `HARNESS-RESULTS-v1.md`.

## 15. Final profile state

1 ADMIN_A Андрей enabled active · 2 MOD_B_REVOKED Оля disabled revoked · 3 MOD_A Михаил enabled active · 4 MOD_C_REVOKED Никита disabled revoked.

## 16. Final workflow state

Admin.dev `wLrLp4WQHm1VJmxz` active **85** · Operational.dev `xSnXPy8cEHoZw6xG` active **45** · Sales-Manager-v2 inactive · workflows created **0**.

## 17. Final AI state

**OFF**

## 18. Final reminder state

**OFF**

## 19. Safety counters

| Counter | Value |
|---------|------:|
| MOD_A `/start` responses tested (forensic window) | 3 |
| MOD_A `/start` responses showing Михаил (post-repair contract / harness) | harness PASS |
| stale start responses (post-repair contract) | 0 |
| profile wipes | 0 |
| blank active profile names | 0 |
| duplicate profile rows | 0 |
| access changes | 0 |
| production leads modified | 0 |
| AI | OFF |
| reminders | OFF |
| workflows created | 0 |
| real leads lost | 0 |
| real leads duplicated | 0 |

## 20. Files changed

- `implementation/runtime-libs/reply-profile-resolver-v1.mjs` (+ `resolveStartReplySenderName`)
- `implementation/runtime-libs/reply-profile-commands-v1.mjs` (re-export)
- `implementation/harness/phase3g23-harness.mjs`
- `architecture/UNIFIED-REPLY-PROFILE-RESOLVER-v1.md`
- `implementation/REPLY-PROFILE-READ-PATH-UNIFICATION-v1.md`
- `implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md`
- `product/CURRENT-PRODUCTION-BASELINE-v1.md`
- `product/KNOWN-LIMITATIONS-v1.md`
- `guides/OPERATOR-RUNBOOK-v1.md`
- `OPERATIONAL-INDEX.md`
- `evidence/phase3g2-3/**`
- `reports/REPORT-iseo-sales-manager-bot-phase3g2-3-moderator-start-profile-repair-v1.md`
- Live: Admin.dev Start node (not in git as raw workflow JSON)

## 21. Security validation

No Telegram IDs, raw executions, or unsanitized exports in evidence. Labels ADMIN_A / MOD_A only. No customer contact. No secrets committed (`private/` stays in Storage runtime only).

## 22. Commit

`fix(iseo-sales-manager-bot): resolve moderator profile before start reply`  
Tip hash: *(filled after commit)*  
Ancestors verified in worktree base: `d2665fac`, `5f5e0be4`, `84406d87`.

## 23. Push

`origin/mars/canonical-post-recovery` — *(filled after push)*

## 24. Remaining operator action

1. MOD_A: `/start` → `/my_reply_profile` → `/start` — both starts must show Михаил.
2. ADMIN_A: `/start`, `/reply_profiles`, `/my_reply_profile` — no regression.
3. Confirm AI OFF / reminders OFF unchanged.

## 25. Stop condition

Stop after: Start shows Михаил in-contract for same-execution rehydrate; anti-wipe holds; self-profile agrees; ADMIN_A intact; production invariants hold; AI/reminders OFF; canonical commit pushed; operator packet delivered. Do not enable AI/reminders; do not restore revoked users; do not activate v2; do not create workflows; do not contact customers; do not alter production leads.
