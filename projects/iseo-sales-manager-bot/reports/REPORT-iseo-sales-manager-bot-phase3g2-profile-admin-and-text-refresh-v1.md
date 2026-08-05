# REPORT — ISEO SALES MANAGER BOT PHASE 3G.2 REPLY PROFILE ADMINISTRATION AND FULL TEXT CONTRACT REFRESH V1

## 1. Verdict

`COMPLETE — PROFILE ADMIN AND TEXT REFRESH READY; OPERATOR ACCEPTANCE PENDING`

Immutable reply-profile numbers 1–4 seeded and read back. Number-based Admin profile commands live. Help/start/AI/stats/config/reminder/unknown texts refreshed. Offline harness **42/42 PASS**. Live command acceptance via local libs + live Sheets oneshots **PASS**; MOD_A disable/enable restored. Operator must still visually confirm Telegram surfaces. Commits: `51b633c6`, `fd7f0522` (push follows).

## 2. Operator-approved scope

Stable numeric reply-profile identifiers; Admin-only number-based name administration; systematic Telegram text-contract refresh across Admin.dev / docs so post–3E–3G command, AI, reminder, and lead-model wording is accurate. AI stays OFF. Reminders stay OFF. No auto-send to customers. No revoked-user restoration via name commands.

## 3. Starting contour

- Operational.dev active, **45** nodes; AI OFF; reminders OFF; Parser 3.3; sole Gmail intake
- Admin.dev active, **84** nodes (pre–Append PROFILE_EVENTS)
- Sales-Manager-v2 inactive
- Profiles seeded from 3G.1.1 (names present; numbers not yet immutable public addresses)
- Stats epoch **05.08.2026** Europe/Moscow; LEADS authoritative

## 4. User-visible text inventory

Registry S01–S26 inventoried against live help/start/AI/profile surfaces. Evidence: `evidence/phase3g2/USER-VISIBLE-TEXT-INVENTORY-v1.md`. Display nickname cues rewritten to label **MOD_A** in evidence.

## 5. Stale-text audit

Pre-patch forensic showed username-token profile addressing (`<пользователь>`), help substring risk, missing `reply_profile_number` on upsert schema, and wording drift. Post-patch: number syntax, explicit help templates, Stats→LEADS, refreshed Start/AI/Config/Reminder/Unknown. Evidence: `STALE-TEXT-AUDIT-v1.md`.

## 6. Stable profile-number contract

`reply_profile_number` immutable positive integer; independent of row order / Telegram identity; Admin mutations by number only; name commands must not change role/status. Live unique 1–4 confirmed. Evidence: `PROFILE-NUMBER-CONTRACT-v1.md`.

## 7. Initial number assignment

| № | Label | Client name | Enabled | Access |
|--:|-------|-------------|---------|--------|
| 1 | ADMIN_A | Андрей | true | active |
| 2 | MOD_B_REVOKED | Оля | false | revoked |
| 3 | MOD_A | Михаил | true | active |
| 4 | MOD_C_REVOKED | Никита | false | revoked |

Seed: 4 rows + 4 PROFILE_EVENTS. Renumbered existing profiles: **0**. Duplicates: **0**. Evidence: `PROFILE-NUMBER-SEED-v1.md`.

## 8. `/reply_profiles`

Admin list shows four profiles by number with Russian role/status/personalization labels. Moderator denied. Evidence: `REPLY-PROFILE-COMMANDS-v1.md`.

## 9. `/reply_profile`

`/reply_profile 3` returns MOD_A card (Михаил, enabled, moderator, active) with intro example. Invalid `999` → not-found pointing to `/reply_profiles`.

## 10. `/reply_name_set`

Admin number syntax only. Live set path for №3 Михаил exercised. Multi-token rejected with example `/reply_name_set 3 Михаил`. Does not auto-enable; does not change access.

## 11. `/reply_name_enable`

Admin-only. Requires valid name + eligible recipient. Live enable after disable restored MOD_A enabled=true. Revoked enable denied (harness). Missing-name enable denied (harness).

## 12. `/reply_name_disable`

Admin-only. Live disable on №3 set personalization OFF while preserving name Михаил and access active. Role/status unchanged.

## 13. `/my_reply_profile`

Available to Admin + moderator. Moderator help lists **only** this among profile cmds. Live MOD_A self card matches №3.

## 14. Name validation

Accepts Андрей/Михаил/Оля/Никита patterns. Rejects multi-token, username, URL, emoji. Moderator mutations accepted: **0**. Evidence: `NAME-VALIDATION-v1.md`.

## 15. Authorization

Profile list/get/set/enable/disable: Admin. Moderator mutations → `Эта команда доступна только администратору.` Access role changes by name commands: **0**.

## 16. Profile mutation history

PROFILE_EVENTS tab + Append PROFILE_EVENTS node. Prepare Access Upsert flattens reply fields. Historical reply snapshots modified: **0**. Evidence: `PROFILE-MUTATION-HISTORY-v1.md`.

## 17. Admin help

Explicit ROLE-AWARE-HELP-BUILDER-v2 template; full reply-profile section with `<номер>`; no substring corruption. Evidence: `ADMIN-HELP-ACCEPTANCE-v1.md`.

## 18. Moderator help

Among profile commands: only `/my_reply_profile`. Reminder status only (no config). Evidence: `MODERATOR-HELP-ACCEPTANCE-v1.md`.

## 19. Start text

Role-aware Russian `/start`; Admin shows ИИ/напоминания выключены and `/reply_profiles`; moderator shows `/my_reply_profile`. Evidence: `START-TEXT-ACCEPTANCE-v1.md`.

## 20. Unknown-command text

Unknown Command node updated in PATCH-RECEIPT; fixed Russian fail-closed posture per TEXT-CONTRACT-v2 (no raw enums/IDs).

## 21. AI text

`/ai_status` OFF; Russian ИИ labels; approved templates without provider; no auto-send. Evidence: `AI-TEXT-ACCEPTANCE-v1.md`.

## 22. Reminder text

Help distinguishes status vs Admin-only config; production engine **OFF**. Evidence: `REMINDER-TEXT-ACCEPTANCE-v1.md`.

## 23. Lead-card text

Card layout remains TELEGRAM-UX-v1; customer copy uses `reply_sender_name` only (Михаил for MOD_A). Nickname must never appear in client `<pre>`. First-contact standard unchanged from 3G.1/3G.1.1.

## 24. Stats text

Authoritative **LEADS**; epoch **05.08.2026**; help line updated. Evidence: `STATS-TEXT-ACCEPTANCE-v1.md`.

## 25. Config text

Allowlisted non-secret keys; Russian labels; no secrets. Evidence: `CONFIG-TEXT-ACCEPTANCE-v1.md`.

## 26. Access and moderator text

Access grant/revoke remain separate from reply-name commands. Revoked MOD_B_REVOKED / MOD_C_REVOKED keep numbers 2/4, disabled personalization, no cards. Opaque moderator codes unchanged.

## 27. Documentation audit

README, OPERATIONAL-INDEX, product baselines, architecture numbering/text contract, implementation admin-commands/help/registry, guides/command reference refreshed for 3G.2. Evidence: `DOCUMENTATION-REFRESH-v1.md`.

## 28. Canonical command reference

`guides/TELEGRAM-COMMAND-REFERENCE-v1.md` covers live command families including number-based reply profiles. Evidence: `COMMAND-REFERENCE-COVERAGE-v1.md`.

## 29. Telegram text contract

`architecture/TELEGRAM-TEXT-CONTRACT-v2.md` is text authority; registry S01–S26 mapped. Evidence: `TEXT-CONTRACT-COVERAGE-v1.md`.

## 30. Harness

Offline Phase 3G.2 harness **42/42 PASS**. Evidence: `HARNESS-RESULTS-v1.md`.

## 31. Admin live acceptance

Live acceptance via local libs + live Sheets read/upsert oneshots **PASS**: `/reply_profiles`, `/reply_profile 3`, set/disable/enable cycle, invalid number/name, help/start/AI surfaces. Final Sheets readback: numbers unique; MOD_A Михаил enabled №3.

## 32. Moderator live acceptance

Moderator denied for `/reply_profiles` and name mutations. `/my_reply_profile` returns MOD_A self card. Help role-safe.

## 33. Profile snapshot regression

Historical recipient reply snapshots unmodified (**0**). Disable preserves name. Numbers stable across mutations. Evidence: `PROFILE-NUMBER-STABILITY-v1.md`, harness #27.

## 34. Production invariants

AI OFF; reminders OFF; Sales-Manager-v2 inactive; sole Gmail intake preserved (**Gmail Fetch Leads**); workflows created=0; no automatic customer messages; no revoked restoration via name cmds; Parser 3.3 / LEADS epoch preserved.

## 35. Final profile state

| Label | № | Name | Enabled | Access |
|-------|--:|------|---------|--------|
| ADMIN_A | 1 | Андрей | true | active |
| MOD_B_REVOKED | 2 | Оля | false | revoked |
| MOD_A | 3 | Михаил | true | active |
| MOD_C_REVOKED | 4 | Никита | false | revoked |

Final MOD_A: name **Михаил**, enabled **true**, number **3**.

## 36. Final AI state

**OFF**. OpenRouter disabled. `/ai_status` выключен.

## 37. Final reminder state

**OFF**. `pending_reminders_enabled=false` posture unchanged.

## 38. Final workflow state

Ops **45** active; Admin **85** active (84 + Append PROFILE_EVENTS); v2 inactive. Evidence: `FINAL-WORKFLOW-STATE-v1.md`.

## 39. Final access state

ADMIN_A admin active; MOD_A moderator active; MOD_B_REVOKED / MOD_C_REVOKED remain revoked. Access roles unchanged by this phase’s name commands.

## 40. Safety counters

| Counter | Value |
|---------|------:|
| stable reply-profile numbers | 4 |
| duplicate profile numbers | 0 |
| renumbered existing profiles | 0 |
| moderator name mutations accepted | 0 |
| access roles changed by name commands | 0 |
| historical reply snapshots modified | 0 |
| AI state | OFF |
| reminders state | OFF |
| workflows created | 0 |
| Admin nodes | 85 |
| Ops nodes | 45 |
| Sales-Manager-v2 active | false |
| sole Gmail intake preserved | yes |
| automatic client messages | 0 |
| destructive Git operations | 0 |

## 41. Files created

- `evidence/phase3g2/*` (22 evidence artifacts, filled this wave)
- `implementation/harness/phase3g2-harness.mjs` (prior wave)
- Architecture/implementation/guides docs for numbering + text contract (prior wave)
- This report: `reports/REPORT-iseo-sales-manager-bot-phase3g2-profile-admin-and-text-refresh-v1.md`

## 42. Files changed

README, OPERATIONAL-INDEX, product baselines, architecture reply/text docs, implementation patch notes / admin commands / help builder / text registry, guides (command reference, runbook), Admin live workflow (in place; not in git export).

## 43. Security validation

No credentials, Telegram IDs, phones, emails, workbook IDs, or customer PII in committed evidence/report. Labels ADMIN_A / MOD_A / MOD_B_REVOKED / MOD_C_REVOKED only. Display nickname rewritten to MOD_A in evidence samples.

## 44. Commit

- `51b633c6` — `feat(iseo-sales-manager-bot): add numbered reply profile administration`
- `fd7f0522` — `docs(iseo-sales-manager-bot): refresh commands and user-facing texts`

## 45. Push

Push to `origin/mars/canonical-post-recovery` (no force) authorized by phase charter; executed after report tip update.

## 46. Risks

- Operator visual Telegram confirmation still required before human acceptance is complete
- In-workflow upsert simulation may surface non-200 on some harness paths; live Sheets oneshots + final readback are the authoritative mutation proof
- Reminder activation remains an explicit separate operator decision

## 47. SAFE UNKNOWN

- Exact operator in-chat visual confirmation timestamps not yet recorded
- Full production LEADS cell rollup after this wave not re-read in documentation closeout
- Git tip hashes for 3G.2 commits unknown until commit wave runs

## 48. Remaining operator actions

1. Visually confirm Admin `/help` (profile section number syntax)
2. Visually confirm moderator `/help` (only `/my_reply_profile` among profiles)
3. Confirm `/reply_profiles`, `/reply_profile 3`, `/my_reply_profile`
4. Confirm `/start`, `/ai_status` OFF, `/stats` epoch 05.08.2026
5. Authorize selective commit + push wave when ready

## 49. Stop condition

Met for engineering closeout of Phase 3G.2 profile-number administration + text-contract refresh + live acceptance proof. **Stopped for operator visual Telegram acceptance** and for pending commit/push. AI not enabled. Reminders not enabled. Revoked users not restored. No customer messages sent.
