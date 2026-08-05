# REPORT — ISEO SALES MANAGER BOT PHASE 3G.1.1 LIVE REPLY PROFILE SEED AND PERSONALIZED TEMPLATE ACCEPTANCE

## 1. Verdict

`COMPLETE — LIVE PROFILES SEEDED; OPERATOR TEMPLATE ACCEPTANCE PENDING`

Live ACCESS_CONTROL reply-profile columns repaired and seeded. T1/T3 personalized acceptance injects delivered 4/4 Telegram successes with zero duplicates. Fail-closed harness band **9/9 PASS**. Operator visual sign-off on latest Telegram cards still required.

## 2. Operator-approved scope

Close Phase 3G.1 live profile seed defect; prove personalized T1/T3 client copy for ADMIN_A (Андрей) and MOD_A (Михаил); preserve AI OFF, reminders OFF, revoked access, and production invariants.

## 3. Starting contour

- Operational.dev `xSnXPy8cEHoZw6xG` active, 45 nodes
- Admin.dev `wLrLp4WQHm1VJmxz` active, 84 nodes
- Sales-Manager-v2 `h8I2Tl2yl4uzhUnB` inactive
- Phase 3G.1 offline harness 100/100 PASS; live profile columns **missing** despite sidecar ok
- AI OFF; reminders OFF; stats epoch 05.08.2026 unchanged

## 4. Live profile seed defect

Phase 3G.1 Sheets sidecar reported ok but did **not** create ACCESS_CONTROL profile columns. Admin `/reply_profiles` showed `—` for all fields; personalization appeared OFF. Six headers missing: `reply_sender_name`, `reply_sender_enabled`, `reply_company_name`, `reply_profile_version`, `reply_profile_updated_at`, `reply_profile_updated_by`. Evidence: `evidence/phase3g1-1/LIVE-PROFILE-SEED-DEFECT-v1.md`.

## 5. Root cause

Sidecar false positive without header verification; Admin Upsert schema mapped profile fields while sheet lacked columns; n8n appendOrUpdate failed with `Column names were updated after the node's setup`; initial seed used brittle short display_name exact match against multi-token/username-shaped live rows. Evidence: `evidence/phase3g1-1/PROFILE-SEED-ROOT-CAUSE-v1.md`.

## 6. Repair actions

1. Created headers via Sheets API HTTP `values.update` → `ACCESS_CONTROL!Q1:V1`
2. Seeded 24 cells via `values.batchUpdate` with label-aware row matching
3. Patched Admin Upsert ACCESS_CONTROL schema to include profile fields aligned with live headers
4. Narrow Ops patch: `classifyProbableTest` early-return for `PHASE_3G11_TEMPLATE_ACCEPTANCE_HUMAN`

No role changes. No revoked-user restoration. No workflow creation.

## 7. Approved profile values (live)

| Label | Client name | Enabled | Access |
|-------|-------------|---------|--------|
| ADMIN_A | Андрей | yes | active |
| MOD_A | Михаил | yes | active |
| MOD_B_REVOKED | Оля | no | revoked |
| MOD_C_REVOKED | Никита | no | revoked |

Evidence: `evidence/phase3g1-1/APPROVED-PROFILE-VALUES-v1.md`.

## 8. Live readback proof

Admin path simulation (Read ACCESS_CONTROL + reply profile helpers) confirms `/reply_profiles` and `/my_reply_profile` for ADMIN_A and MOD_A match contract. Revoked rows show disabled profiles. Evidence: `evidence/phase3g1-1/LIVE-PROFILE-READBACK-v1.md`.

## 9. T1 personalized acceptance

- Template: `T1_EXISTING_SITE_GROWTH`
- Site: `t1-accept.iseo-phase3g11.local` (sanitized)
- `geo_ai_clause`: false
- ADMIN_A: `Меня зовут Андрей, компания INTLSEO` + site line + audit CTA
- MOD_A: identical except `Меня зовут Михаил, компания INTLSEO`
- `Мопс` in client copy: 0; guidance outside `<pre>`
- Evidence: `evidence/phase3g1-1/T1-PERSONALIZED-ACCEPTANCE-v1.md`

## 10. T3 personalized acceptance

- Template: `T3_MEANINGFUL_TASK`
- Task summary: разобраться, почему снизился поисковый трафик
- ADMIN_A / MOD_A personalized as T1 pattern
- `Мопс` in client copy: 0; guidance outside `<pre>`
- Evidence: `evidence/phase3g1-1/T3-PERSONALIZED-ACCEPTANCE-v1.md`

## 11. No nickname leak

Zero `Мопс` occurrences in client copy across T1/T3 acceptance set and fail-closed harness. No display-name, username, or actor fallbacks. Evidence: `evidence/phase3g1-1/NO-NICKNAME-LEAK-v1.md`.

## 12. Test delivery idempotency

| Counter | Value |
|---------|------:|
| test business fixtures | 2 |
| recipient drafts | 4 |
| Telegram successes | 4 |
| duplicate sends | 0 (incl. 3 later polls) |
| revoked sends | 0 |
| AI provider calls | 0 |

Evidence: `evidence/phase3g1-1/TEST-DELIVERY-IDEMPOTENCY-v1.md`.

## 13. Production invariants

AI OFF; reminders OFF; Sales-Manager-v2 inactive; sole Gmail intake preserved; workflows created=0; access-role changes=0; automatic client messages=0; existing production lead not regenerated. Evidence: `evidence/phase3g1-1/PRODUCTION-INVARIANTS-v1.md`.

## 14. Fail-closed harness

Phase 3G.1.1 band: **9/9 PASS** — missing name, invalid `@` name, disabled flag, no display-name/nickname/username fallbacks, ready profiles render. Evidence: `evidence/phase3g1-1/HARNESS-RESULTS-v1.md`. Phase 3G.1 full harness 100/100 PASS remains baseline.

## 15. Final workflow state

Ops 45 active (narrow acceptance patch); Admin 84 active (schema aligned); v2 inactive. Evidence: `evidence/phase3g1-1/FINAL-WORKFLOW-STATE-v1.md`.

## 16. TEST_LEADS / production LEADS separation

TEST_LEADS sanitized mirror rows appended: 2. Production LEADS business rows for acceptance: 0 (excluded via `exclude_from_prod_stats` + synthetic markers). No production stats inflation claimed.

## 17. Earlier exploratory batches

Pre-repair inject batches were test_suppressed with empty client copy. Operator must visually accept **latest** T1/T3 acceptance-set cards only — not earlier empty-copy cards in Telegram history.

## 18. AI final state

OFF. OpenRouter nodes disabled. `/ai_status` expected OFF. AI provider calls on acceptance path: 0.

## 19. Reminder final state

OFF. `pending_reminders_enabled=false`. Unchanged from Phase 3F.1 baseline.

## 20. Access final state

ADMIN_A admin active; MOD_A moderator active; MOD_B_REVOKED and MOD_C_REVOKED remain revoked. Profile names seeded; eligibility unchanged.

## 21. Reporting invariant

One business lead = one reporting row. No per-recipient reporting multiplication. Shared template metadata only in human reporting policy.

## 22. Statistics invariant

Stats baseline epoch unchanged. Acceptance fixtures excluded from production stats. Phase does not regenerate existing production lead.

## 23. Existing lead protection

No regenerate/resend of existing production lead. Acceptance uses synthetic TEST_LEADS mirrors and marked inject path only.

## 24. Regression

Exactly-once delivery preserved. OpenRouter disabled. v2 inactive. Callbacks/pending/reminder commands untouched except narrow Ops probable_test early-return for acceptance marker.

## 25. Operator visual acceptance (pending)

Confirm in Telegram:

1. T1 card as ADMIN_A — Андрей + INTLSEO + site + audit CTA
2. T1 card as MOD_A — Михаил + INTLSEO + site + audit CTA
3. T3 card as ADMIN_A — traffic-decline task + Андрей intro
4. T3 card as MOD_A — traffic-decline task + Михаил intro
5. `/reply_profiles`, `/my_reply_profile`, `/ai_status` (OFF)

Do **not** press lifecycle buttons. Do **not** clean fixtures until sign-off.

## 26. Safety counters

| Counter | Value |
|---------|------:|
| Telegram successes (acceptance) | 4 |
| duplicate sends | 0 |
| revoked sends | 0 |
| AI provider calls | 0 |
| workflows created | 0 |
| access-role changes | 0 |
| `Мопс` in client copy | 0 |
| automatic client messages | 0 |
| reminders enabled | false |
| TEST_LEADS rows | 2 |
| production LEADS acceptance rows | 0 |

## 27. Files created

`evidence/phase3g1-1/` — 12 artifacts (defect, root cause, values, readback, T1/T3 acceptance, nickname leak, idempotency, invariants, harness, workflow state, receipt). This report.

## 28. Files changed

README, OPERATIONAL-INDEX, product baselines, architecture reply-profile docs, implementation specs, TEST-HARNESS-SPEC, OPERATOR-RUNBOOK.

## 29. Security validation

No credentials, Telegram IDs, phones, emails, workbook URLs, or customer PII in committed artifacts. Labels ADMIN_A / MOD_A only.

## 30. Commit

1. `504fe270` — `fix(iseo-sales-manager-bot): seed live reply profiles`
2. `374656b0` — `test(iseo-sales-manager-bot): prove personalized template delivery`
3. (this docs tip hash recorded after push) — `docs(iseo-sales-manager-bot): record phase 3g1.1 commit hashes`

## 31. Push

Push without force to `origin/mars/canonical-post-recovery` from clean worktree `work/iseo-sm-phase3g11-20260806-022452`.

## SAFE UNKNOWN

- Exact production reporting workbook cell values after acceptance inject not re-read in documentation wave
- Full operator in-chat visual sign-off not yet recorded

## Stop condition

Met for engineering closeout of Phase 3G.1.1 profile seed repair + T1/T3 acceptance inject proof. **Stopped for operator visual acceptance** before declaring full human acceptance complete. AI not enabled. Reminders not enabled. Revoked users not restored. No customer messages sent.
