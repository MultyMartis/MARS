# REPORT — ISEO SALES MANAGER BOT PHASE 3D.8.2 ACTOR ATTRIBUTION AND REVOKED MODERATOR VISIBILITY

**Date:** 2026-08-05  
**Project:** `iseo-sales-manager-bot`  
**Contour:** Operational.dev `xSnXPy8cEHoZw6xG` · Admin.dev `wLrLp4WQHm1VJmxz` · Sales-Manager-v2 inactive

## 1. Verdict

**COMPLETE — PATCH READY; LIVE ATTRIBUTION CONFIRMATION PENDING**

## 2. Operator-approved scope

Operator explicitly approved Phase 3D.8.2: close 3D.8.1 with live Admin/moderator actions; replace generic `Кем: сотрудник` with ACCESS_CONTROL safe actor label; enhance `/moderator_pending` to show revoked former moderators with stable reactivation codes. Do not restore Olya/Nikita.

## 3. Phase 3D.8.1 closeout

**PHASE 3D.8.1 COMPLETE — ADMIN AND MODERATOR ACTIONS READY**

| Check | Result |
|-------|--------|
| Admin processed action | PASS |
| Moderator spam action | PASS |
| Callback loading ended | PASS |
| Success feedback appeared | PASS |
| Processed final card | PASS |
| Spam final card | PASS |
| Buttons removed | PASS |
| No automatic client messages | PASS |
| No additional workflows | PASS |
| Attribution at close | `Кем: сотрудник` (limitation → 3D.8.2) |

## 4. Environment

- environment=production
- ai_enabled=false
- parser_version=sm-parser-v3.2
- message_format_version=sm-msg-v2.2

## 5. Canonical baseline

Worktree based on `origin/mars/canonical-post-recovery` @ `188ff8d4` (Phase 3D.8.1). Also verified ancestors `79709aad` (3D.8 follow-up) and Phase 3D.8 lineage present.

## 6. Current workflow state

| Workflow | Active | Nodes |
|----------|--------|-------|
| Sales-Manager-v2 | false | 19 |
| Operational.dev | true | 45 |
| Admin.dev | true | 59 |

Admin Telegram Trigger: `message` + `callback_query`. Workflows created=0. Ops unmodified.

## 7. Current access state

- Андрей = admin / active
- Мопс = moderator / active
- Оля = moderator / revoked (intentional, unchanged)
- Никита = moderator / revoked (intentional, unchanged)

## 8. Actor authorization

ACCESS_CONTROL by exact Telegram user id; role admin|moderator + status=active required for lifecycle actions. Username/display/callback data are not authorization sources.

## 9. Actor identity source

Check User Authorization exports `access_display_name` and `access_username` from the matched ACCESS_CONTROL row. Handle Callback Action uses these fields only for attribution.

## 10. Display precedence

1. ACCESS_CONTROL display_name  
2. ACCESS_CONTROL @username  
3. `сотрудник`  
Combined `Name · @username` when both exist and concise.

## 11. Actor snapshot

On applied transition: `actor_ref`, `actor_role_snapshot`, `actor_display_snapshot`, timestamp, action. Persisted in LEAD_EVENTS `detail` JSON and final card text. Idempotent/conflict do not create a second applied snapshot.

## 12. Processed-card attribution

Final block:

```
✅ Обработан
Кем: <safe actor label>
Время: DD.MM.YYYY HH:MM МСК
```

## 13. Spam-card attribution

```
🚫 Спам
Кем: <safe actor label>
Время: DD.MM.YYYY HH:MM МСК
```

## 14. LEAD_EVENTS attribution

Append-only on mutate-true applied branch. `detail` includes opaque actor, role snapshot, safe display snapshot, prior/new status, source=`telegram_callback`.

## 15. Multi-copy synchronization

Actor resolved once; same `edit_text` reused for all known delivered copies. Edit failures isolated; no lifecycle rollback.

## 16. `/moderator_pending` previous limitation

Showed only pending applications; revoked former moderators disappeared from both `/moderators` and `/moderator_pending`.

## 17. Pending section

Unchanged logical filter: public/pending users with application codes and first-seen time.

## 18. Revoked section

Former moderators with status=revoked, stable code, revoked date. Excludes public/blocked/Admin/active.

## 19. Stable code behavior

`accessCode(user_id)` unchanged across revoke; `/moderator_add CODE` restores same row. Not exercised for Olya/Nikita this phase.

## 20. `/moderators` boundary

Active moderators only. Count represents active-only.

## 21. Blocked-user boundary

Blocked users excluded from revoked section; no blocked-admin surface added.

## 22. Empty-state matrix

Harness covers pending+revoked, pending-only, revoked-only, both-empty. Exactly one reply body.

## 23. Admin help

`/moderator_pending — новые заявки и временно отозванные модераторы`

## 24. Harness

**49/49 PASS** (`implementation/harness/phase3d82-harness.mjs`).

## 25. Live revoked-list acceptance

Live ACCESS_CONTROL snapshot (from prior Admin executions) + patched formatter produces revoked section with Olya + Nikita and stable codes (codes redacted in git). No ACCESS mutation, no notifications. Operator Telegram `/moderator_pending` visual confirm recommended.

## 26. Live actor acceptance

Admin.dev patched; markers verified live (`actor_display_snapshot`, revoked list helpers). Live ACCESS display fields resolve Admin and Мопс labels in simulation. Post-patch Telegram clicks on new pending fixtures remain **pending** (prior 3D.8.1 cards already show legacy `Кем: сотрудник`).

## 27. Final access state

Unchanged intentional set (§7). Olya role changes=0; Nikita role changes=0.

## 28. Final workflow state

See §6. Same Admin ID patched; Ops active; v2 inactive.

## 29. Safety counters

- AI provider calls=0
- automatic client messages=0
- workflows created=0
- parser runtime changes=0
- reminder implementation changes=0
- Olya role changes=0
- Nikita role changes=0
- destructive Git operations=0

## 30. Files created

- `evidence/phase3d8-2/*` (12 contract/acceptance files + HARNESS-RESULT.json)
- `implementation/runtime-libs/phase3d82-actor-moderator-lib.mjs`
- `implementation/harness/phase3d82-harness.mjs`
- this report

## 31. Files changed

README · OPERATIONAL-INDEX · TELEGRAM-UX / ADMIN-COMMAND contracts · ADMIN-WORKFLOW-PATCH-SPEC · TEST-HARNESS-SPEC · OPERATOR-RUNBOOK · KNOWN-LIMITATIONS · PRODUCT-ROADMAP · MODERATOR-LIFECYCLE-UX-SPEC · Phase 3D.8.1 report/evidence closeout

## 32. Security validation

No Telegram IDs, chat IDs, actor hashes linked to identities, real usernames, phones, emails, workbook IDs, raw callbacks, or unsanitized workflow exports in git evidence. Private raw exports remain under STORAGE tmp/backups only.

## 33. Commit

`feat(iseo-sales-manager-bot): attribute lead actions and list revoked moderators` (this wave)

## 34. Push

`origin/mars/canonical-post-recovery` (no force) — this wave

## 35. Risks

- Historical 3D.8.1 final cards retain legacy `Кем: сотрудник` until new transitions occur.
- Operator Telegram `/moderator_pending` visual confirm still recommended though live ACCESS+formatter simulation PASS.

## 36. SAFE UNKNOWN

Exact dual-recipient visual confirmation of post-patch actor labels on both Admin and moderator chat copies (awaits new pending fixtures + clicks).

## 37. Remaining operator actions

1. Send `/moderator_pending` — confirm revoked section shows Olya + Nikita + codes.  
2. Optionally click processed/spam on ≤2 new synthetic pending fixtures to confirm named `Кем:` lines live.

## 38. Stop condition

Stopped after 3D.8.1 live closeout, actor attribution + revoked list implemented and patched live, harness PASS, evidence/docs, commit/push. No restore of Olya/Nikita. No reminders. No Parser 3.3. No AI. No Sales-Manager-v2 activation. No new workflows. No client contact.
