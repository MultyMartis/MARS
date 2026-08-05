# REPORT — ISEO SALES MANAGER BOT PHASE 3G.1 INTLSEO APPROVED FIRST-CONTACT STANDARD AND PERSONALIZED MANAGER ASSIST V1

## 1. Verdict

`COMPLETE — APPROVED TEMPLATES AND PERSONALIZATION READY; OPERATOR ACCEPTANCE PENDING`

Offline harness **100/100 PASS**. Live Operational/Admin patched in place (same workflow IDs). AI remains OFF. Reminders remain OFF. Sales-Manager-v2 inactive. Operator Telegram visual sign-off still required.

## 2. Operator-approved scope

INTLSEO first-contact templates + reply-construction policy; recipient-specific approved sender-name personalization; constrained AI-assist contract without global AI enablement.

## 3. Starting contour

- Operational.dev `xSnXPy8cEHoZw6xG` active, 45 nodes, AI OFF, reminders OFF
- Admin.dev `wLrLp4WQHm1VJmxz` active, 82 nodes
- Sales-Manager-v2 `h8I2Tl2yl4uzhUnB` inactive
- Clean ledger epoch 05.08.2026; stats baseline 1/1/0/0
- Access: Андрей admin active; Мопс moderator active; Оля/Никита revoked

## 4. Current reply-path forensic

Previously: Parse → Processor (`sm-reply-v2.1`) → Format → Expand cloned **one shared** `first_reply_text` to all recipients.

Gap: no `reply_sender_name`; nickname risk; free-form/legacy style not equal to INTLSEO commercial standard.

Plan executed: shared template **route** before CLEAN write; **personalize after Expand**; LEADS holds shared metadata; LEAD_DELIVERIES / RECIPIENT_REPLIES hold personalized drafts.

## 5. INTLSEO first-contact policy

Always: `Добрый день!` + approved first name + `INTLSEO` + concise next step; audit video/materials language where template requires.  
Never: tariffs-first, guarantees, fabricated site study, auto-send, guidance inside client `<pre>`.

## 6. Approved templates

1. `T1_EXISTING_SITE_GROWTH`
2. `T2_SITE_MISSING`
3. `T3_MEANINGFUL_TASK`
4. `T4_NEW_SITE_DEVELOPMENT`
5. `T5_SPECIAL_PROJECT`

Versions: `iseo-first-contact-v1.0` / `iseo-template-set-v1.0` / `iseo-sales-policy-v1.0`. Legacy `sm-reply-v2.1` retained as rollback/history only.

## 7. Template precedence

T5 > T4 > T3 > T1 > T2 > safe T2 fallback.

## 8. Deterministic router

`implementation/runtime-libs/approved-template-router-v1.mjs` — outputs template id/reason/CTA/theme/geo clause/website/task summary/flags/confidence/warnings.

## 9. Deterministic task summaries

Controlled dictionary in router (`traffic_decline`, `conversion_low`, …). No invention when unsafe → route away from T3.

## 10. Reply-profile contract

Additive ACCESS_CONTROL fields: `reply_sender_name`, `reply_sender_enabled`, `reply_company_name`, `reply_profile_version`, `reply_profile_updated_at`, `reply_profile_updated_by`.  
Version `iseo-recipient-name-v1.0`. Never derive from Telegram display/username/actor/role.

## 11. Approved sender names

- Андрей → Андрей  
- Мопс → Михаил  
- Оля → Оля (prepared; remains revoked / ineligible)  
- Никита → Никита (prepared; remains revoked / ineligible)

## 12. Sender-name validation

Non-empty human first name; Cyrillic/Latin; no `@`, URL, phone, emoji, role/company labels; no auto-shorten of full names.

## 13. Missing-name fail-closed

Card delivers; copy omitted; manager warning `⚠️ Не задано имя для ответа клиенту. Обратитесь к администратору.`; `recipient_reply_state=blocked_missing_sender_name`; not a Telegram delivery failure.

## 14. Recipient-level personalization

After eligible Expand; each recipient gets own draft + name snapshot.

## 15. One lead / multiple drafts

One business LEADS row; N LEAD_DELIVERIES / RECIPIENT_REPLIES personalized records; one lifecycle/statistics unit.

## 16. Storage model

- LEADS: shared template/meta fields  
- LEAD_DELIVERIES extended + `RECIPIENT_REPLIES` tab created  
- No second spreadsheet file

## 17. Telegram client-copy block

Heading: `✉️ Готовый первый ответ — нажмите, чтобы скопировать` + `<pre>` + auto-send disclaimer outside copy.

## 18. Manager guidance

Separate `💡 Подсказка менеджеру` block; no internal codes in card text.

## 19. AI OFF mode

Default. Deterministic route/render/guidance. Provider calls on AI OFF path = 0.

## 20. AI-assisted mode

Contract ready: router first → structured fields only → validator → render. Not globally enabled.

## 21. AI prompt contract

`buildAiAssistSystemPrompt` locks template/CTA/name/company; Russian structured JSON only; no raw PII.

## 22. AI validation

Rejects guarantees/prices/deadlines/full client message/name-company changes/injection/invalid JSON.

## 23. Deterministic fallback

On AI reject → deterministic summary/guidance; delivery continues.

## 24. Admin profile commands

`/reply_profiles`, `/reply_profile`, `/reply_name_set`, `/reply_name_enable`, `/reply_name_disable` (Admin mutation).

## 25. Moderator profile view

`/my_reply_profile` only; mutations denied.

## 26. Template fixture corpus

Harness covers routing, templates, profiles, personalization, guidance, AI OFF, AI assist rejects, storage invariants (see `HARNESS-RESULTS-v1.md`).

## 27. Live test-only acceptance

Live workflow patch + Sheets seed completed. Full TEST_LEADS dual-card Telegram visual battery: **operator pending**. Harness stands as primary automated proof.

## 28. Test cleanup

No TEST_LEADS rows intentionally written to production LEADS/reporting in this wave. Local patch backups under Storage incoming (not git).

## 29. Reporting invariant

One business lead = one reporting row; no per-recipient reporting multiplication; shared template fields only in human sheet policy.

## 30. Statistics invariant

Target unchanged baseline 1/1/0/0 unless a real lead arrives independently. Phase does not regenerate Евгений.

## 31. Existing lead protection

No regenerate/resend of existing production lead; prospective standard for new leads after activation.

## 32. Regression

Exactly-once delivery path preserved; OpenRouter disabled; v2 inactive; callbacks/pending/reminder commands untouched except Help list additions.

## 33. Harness

100/100 PASS — `evidence/phase3g1/HARNESS-RESULTS-v1.md`.

## 34. Operator visual acceptance

### Packet (expected client lines)

1. T1 as Андрей — `Меня зовут Андрей, компания INTLSEO.`  
2. T1 as Михаил — `Меня зовут Михаил, компания INTLSEO.`  
3. T2 as Андрей  
4. T3 as Михаил  
5. T4 as Андрей  
6. T5 as Михаил  
7. Missing-name blocked warning  
8. Manager guidance separate  
9. `/reply_profiles`  
10. `/my_reply_profile`  
11. `/ai_status` (OFF)

**Мопс must never appear in client copy.**

## 35. Production activation state

Deterministic templates + personalization **deployed** on Operational.dev. Treat as **test-ready / pending operator visual acceptance** for final human sign-off language.

## 36. AI final state

OFF. Assist contract ready; live provider proof deferred.

## 37. Reminder final state

OFF.

## 38. Final workflow state

See `evidence/phase3g1/FINAL-WORKFLOW-STATE-v1.md` — Ops 45 active; Admin 84 active; v2 inactive.

## 39. Final access state

Андрей admin active; Мопс moderator active; Оля/Никита revoked. Profile names seeded; eligibility unchanged.

## 40. Safety counters

| Counter | Value |
|---------|------:|
| approved templates | 5 |
| active recipient profiles with approved names | 2 |
| client-copy occurrences of `Мопс` (harness) | 0 |
| Telegram-display-name fallbacks | 0 |
| username fallbacks | 0 |
| missing-name unsafe drafts | 0 |
| reporting lead multiplication | 0 |
| AI OFF provider calls (harness) | 0 |
| AI sandbox provider calls | 0 (deferred) |
| automatic client messages | 0 |
| reminders enabled | false |
| Sales-Manager-v2 active | false |
| workflows created | 0 |
| access-role changes | 0 |
| existing real leads modified | 0 |
| destructive deletions | 0 |
| destructive Git operations | 0 |

## 41. Files created

Runtime libs, harness, architecture/implementation docs, `evidence/phase3g1/*`, this report.

## 42. Files changed

README, OPERATIONAL-INDEX, product baselines, UX/ledger/docs, formatter/processor, patch specs, guides.

## 43. Security validation

No credentials, Telegram IDs, phones, emails, workbook URLs, raw exports, or customer PII committed. Live backups remain under Storage incoming only.

## 44. Commit

(filled after git wave)

## 45. Push

(filled after git wave)

## 46. Risks

- Operator must visually confirm live cards before calling human acceptance complete  
- CLEAN tab name in Ops mapping may still show historical `lead_clean_v2` label while ledger docs say LEADS — additive columns applied to mapped append node; confirm sheet headers in console if a write fails  
- Help lists profile commands; dedicated Reply Profile Commands node handles execution

## 47. SAFE UNKNOWN

- Exact production reporting workbook cell values after this wave not re-read in this session  
- Full dual-card Telegram live battery not operator-confirmed in-chat in this session

## 48. Remaining operator actions

1. Visually accept Telegram packet (section 34)  
2. Spot-check `/reply_profiles`, `/my_reply_profile`, `/ai_status`  
3. Confirm stats still clean  
4. Explicitly acknowledge production activation language

## 49. Stop condition

Met for engineering closeout of 3G.1 implementation + live deploy of deterministic path; **stopped for operator visual acceptance** before claiming full human acceptance complete. AI not enabled. Reminders not enabled. Revoked users not restored. No customer messages sent.
