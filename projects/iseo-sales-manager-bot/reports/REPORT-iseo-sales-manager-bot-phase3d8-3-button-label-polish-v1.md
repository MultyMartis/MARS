# REPORT — ISEO SALES MANAGER BOT PHASE 3D.8.3 BUTTON LABEL POLISH AND 3D.8.2 LIVE CLOSEOUT

**Date:** 2026-08-05  
**Project:** `iseo-sales-manager-bot`  
**Contour:** Operational.dev `xSnXPy8cEHoZw6xG` · Admin.dev `wLrLp4WQHm1VJmxz` · Sales-Manager-v2 inactive  
**Canonical base:** `origin/mars/canonical-post-recovery` @ `f4c94a44` (includes `28504b9a`)

## 1. Verdict

**PHASE 3D.8.3 COMPLETE — ACTION BUTTON LABELS UPDATED**

## 2. Operator approval

Operator confirmed Phase 3D.8.2 live actor-attribution acceptance succeeded and approved the pending-button caption polish to exactly `✅ Обработано` / `🚫 Спам` without callback or lifecycle changes.

## 3. Phase 3D.8.2 live closeout

**PHASE 3D.8.2 COMPLETE — ACTOR ATTRIBUTION AND REVOKED MODERATOR VISIBILITY READY**

| Check | Result |
|-------|--------|
| `/moderator_pending` revoked section live | PASS |
| Оля / Никита visible with stable codes | PASS |
| Roles unchanged (no restore) | PASS |
| Admin → spam attribution | PASS |
| Moderator → processed attribution | PASS |
| Safe names (no raw IDs) | PASS |
| Callback feedback + final lifecycle cards | PASS |
| Buttons removed after transition | PASS |
| No client messages / no new workflows | PASS |

Honesty: acted-card copies confirmed by operator; independent second-copy runtime re-export for these two fixtures was not separately attached (multi-copy contract unchanged).

## 4. Current workflow state

| Workflow | Active | Nodes |
|----------|--------|------:|
| Sales-Manager-v2 | false | 19 |
| Operational.dev | true | 45 |
| Admin.dev | true | 59 |

CONFIG: production · AI OFF · `sm-parser-v3.2` · `sm-msg-v2.2`. Access: Андрей admin/active · Мопс moderator/active · Оля/Никита revoked.

## 5. Previous button labels

- `✅ Отметить обработанным`
- `🚫 Отметить как спам`

## 6. New button labels

- `✅ Обработано`
- `🚫 Спам`

Patched on Operational.dev only: Format `buildReplyMarkup` + Send With Buttons `inlineKeyboard` texts.

## 7. Callback invariance

`sm:p:<opaque-token>` / `sm:s:<opaque-token>` unchanged. Send expressions still `telegram_callback_processed` / `telegram_callback_spam`. Normalize + Handle Callback unchanged. Live synth showed prefixes + 12-char tokens on both copies.

## 8. Final-status wording boundary

| Surface | Text |
|---------|-------|
| Action button | `✅ Обработано` |
| Completed state | `✅ Обработан` |
| Spam button / spam final | `🚫 Спам` |
| Feedback processed | `Лид отмечен как обработанный.` |
| Feedback spam | `Лид отмечен как спам.` |

## 9. Delivery regression

One synthetic business lead → 2 eligible recipients → 2 Send OK with new labels → LEAD_DELIVERIES 2 → 0 duplicates across ≥3 polls → 1 schedule trigger → Gmail sole intake preserved.

## 10. Callback regression

Authorization, processed/spam mutation, button removal, idempotent/conflict contracts unchanged (Admin.dev not patched for labels). Buttons not auto-pressed in 3D.8.3 acceptance.

## 11. Actor-attribution regression

`buildFinalCardAttributionBlock` / ACCESS_CONTROL attribution unchanged; 3D.8.2 live closeout PASS.

## 12. Moderator-management regression

`/moderator_pending` revoked list + `/moderators` active-only + `/my_status` present — harness PASS; roles unchanged.

## 13. Harness

`implementation/harness/phase3d83-harness.mjs` — **30/30 PASS**. Extended live-GET checks during patch session also PASS.

## 14. Live acceptance

Marker `PHASE_3D8_3_BUTTON_LABEL_ACCEPTANCE`. Both recipient API messages carried `✅ Обработано` / `🚫 Спам`. Operator visual optional (API markup sufficient). Buttons not pressed.

## 15. Final workflow state

Same IDs. Ops 45 active · Admin 59 active · v2 inactive · OpenRouter disabled · workflows created=0.

## 16. Safety counters

- AI provider calls=0
- automatic client messages=0
- workflows created=0
- parser changes=0
- reminder changes=0
- access-role changes=0
- callback contract changes=0
- lifecycle schema changes=0

## 17. Files created

- `evidence/phase3d8-3/*` (closeout, forensic, contracts, acceptance, harness result)
- `implementation/harness/phase3d83-harness.mjs`
- this report

## 18. Files changed

README · OPERATIONAL-INDEX · TELEGRAM-UX-CONTRACT · OPERATIONAL-WORKFLOW-PATCH-SPEC · TEST-HARNESS-SPEC · OPERATOR-RUNBOOK · CURRENT-PRODUCTION-BASELINE · Phase 3D.8.2 report/evidence closeout

## 19. Security validation

No credentials, Telegram IDs, chat IDs, real usernames, phones, emails, workbook IDs, raw callback payloads, screenshots, or unsanitized workflow exports in git scope. Private tooling remains under STORAGE incoming only.

## 20. Commit

`2da22ea6` — `style(iseo-sales-manager-bot): shorten lead action button labels`

## 21. Push

`origin/mars/canonical-post-recovery` @ `9c3c8b48` (no force). Style commit `2da22ea6`; tip-hash docs `33f7da1a` / align `9c3c8b48`.

## 22. Risks

- Historical docs/guides outside this allowlist may still show long button captions until separately updated.
- Operator visual on Telegram client remains optional if further human confirmation desired.

## 23. SAFE UNKNOWN

- Independent second-copy runtime attachment for the two 3D.8.2 attribution fixtures (acted copies operator-confirmed).
- Whether every historical pending card already in chat was edited (only new sends use new labels).

## 24. Remaining operator actions

- Optional: glance at the new pending synthetic card labels in Telegram.
- Do not restore Olya/Nikita; do not enable AI; do not activate Sales-Manager-v2.

## 25. Stop condition

Phase 3D.8.2 closeout recorded · visible labels updated · callback contract unchanged · harness PASS · live/API acceptance PASS · canonical commit/push · this report.

## Execution safety

- cwd: clean worktree under `X:\AI MARS STORAGE\git-sync-iseo-sm-phase3d83-*`
- scope lock honored: yes (`projects/iseo-sales-manager-bot/**`)
- destructive ops: none
- protected zone touch: none

